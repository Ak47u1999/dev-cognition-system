"""Tests for backend/ai/ollama_client.py — fallback, mock, and retry logic."""
import sys
import os
import json
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

import ai.ollama_client as ollama_client


SAMPLE_PROMPT = (
    "Analyze the following C function...\n\nCode:\n\nint add(int a, int b) { return a + b; }"
)


class TestFallbackResponse(unittest.TestCase):
    def _parse(self, prompt, error=None):
        raw = ollama_client._fallback_response_from_prompt(prompt, error=error)
        return json.loads(raw)

    def test_returns_valid_json(self):
        raw = ollama_client._fallback_response_from_prompt(SAMPLE_PROMPT)
        data = json.loads(raw)
        self.assertIsInstance(data, dict)

    def test_has_required_keys(self):
        data = self._parse(SAMPLE_PROMPT)
        for key in ("title", "summary", "details", "rationale",
                    "performance", "hidden_insights", "where_used", "tags", "markdown"):
            self.assertIn(key, data)

    def test_extracts_function_name_from_code(self):
        data = self._parse(SAMPLE_PROMPT)
        self.assertEqual(data["title"], "add")

    def test_loop_tag_detected_when_for_present(self):
        prompt = "Code:\n\nvoid process() { for(int i=0;i<n;i++){} }"
        data = self._parse(prompt)
        self.assertIn("loop", data["tags"])

    def test_memory_tag_detected_when_malloc_present(self):
        prompt = "Code:\n\nvoid alloc() { malloc(10); }"
        data = self._parse(prompt)
        self.assertIn("memory", data["tags"])

    def test_recursion_tag_detected(self):
        prompt = "Code:\n\nint fib(int n) { return fib(n-1) + fib(n-2); }"
        data = self._parse(prompt)
        self.assertIn("recursion", data["tags"])

    def test_error_included_in_markdown_when_provided(self):
        data = self._parse(SAMPLE_PROMPT, error="connection_refused")
        self.assertIn("connection_refused", data["markdown"])

    def test_no_error_field_in_markdown_when_none(self):
        data = self._parse(SAMPLE_PROMPT, error=None)
        self.assertNotIn("Note:", data["markdown"])

    def test_generic_prompt_without_code_marker(self):
        data = self._parse("just a raw prompt with no marker")
        self.assertIsInstance(data, dict)


class TestMockResponse(unittest.TestCase):
    def test_returns_valid_json(self):
        raw = ollama_client._mock_response(SAMPLE_PROMPT)
        data = json.loads(raw)
        self.assertIsInstance(data, dict)

    def test_same_as_fallback(self):
        mock_raw = ollama_client._mock_response(SAMPLE_PROMPT)
        fallback_raw = ollama_client._fallback_response_from_prompt(SAMPLE_PROMPT, error="MOCK_RESPONSE")
        self.assertEqual(json.loads(mock_raw), json.loads(fallback_raw))


class TestQueryOllamaMockMode(unittest.TestCase):
    def test_returns_fallback_when_mock_env_set(self):
        with patch.object(ollama_client, 'MOCK', True):
            result, tps = ollama_client.query_ollama(SAMPLE_PROMPT)
        data = json.loads(result)
        self.assertIsInstance(data, dict)
        self.assertIsNone(tps)

    def test_returns_fallback_on_http_error(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.raise_for_status.side_effect = Exception("server error")
        mock_resp.text = "Internal Server Error"

        with patch.object(ollama_client, 'MOCK', False):
            with patch.object(ollama_client, '_rate_limited_post', return_value=mock_resp):
                result, tps = ollama_client.query_ollama(SAMPLE_PROMPT)
        data = json.loads(result)
        self.assertIsInstance(data, dict)
        self.assertIsNone(tps)

    def test_returns_content_on_success(self):
        expected_content = json.dumps({"title": "add", "summary": "adds two ints",
                                       "details": "", "rationale": "", "performance": "",
                                       "hidden_insights": [], "where_used": [], "tags": [],
                                       "markdown": ""})
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {
            "choices": [{"message": {"content": expected_content}}],
            "usage": {"completion_tokens": 50},
        }

        with patch.object(ollama_client, 'MOCK', False):
            with patch.object(ollama_client, '_rate_limited_post', return_value=mock_resp):
                result, tps = ollama_client.query_ollama(SAMPLE_PROMPT)
        self.assertEqual(result, expected_content)
        self.assertIsNotNone(tps)
        self.assertGreater(tps, 0)


class TestQueryOllamaRetry(unittest.TestCase):
    """Connection errors must be retried before falling back."""

    @patch('time.sleep', return_value=None)
    def test_retries_on_connection_error_then_succeeds(self, mock_sleep):
        import requests
        expected = json.dumps({"title": "add"})
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {"choices": [{"message": {"content": expected}}]}

        side_effects = [requests.exceptions.ConnectionError("refused"), mock_resp]

        with patch.object(ollama_client, 'MOCK', False):
            with patch.object(ollama_client, '_rate_limited_post', side_effect=side_effects):
                result, tps = ollama_client.query_ollama(SAMPLE_PROMPT)

        self.assertEqual(result, expected)
        mock_sleep.assert_called()

    @patch('time.sleep', return_value=None)
    def test_falls_back_after_max_retries_exhausted(self, mock_sleep):
        import requests
        with patch.object(ollama_client, 'MOCK', False):
            with patch.object(ollama_client, '_rate_limited_post',
                              side_effect=requests.exceptions.ConnectionError("refused")):
                with patch.object(ollama_client, '_MAX_RETRIES', 2):
                    with self.assertRaises(ollama_client.OllamaUnavailableError):
                        ollama_client.query_ollama(SAMPLE_PROMPT)

    @patch('time.sleep', return_value=None)
    def test_falls_back_on_timeout(self, mock_sleep):
        import requests
        with patch.object(ollama_client, 'MOCK', False):
            with patch.object(ollama_client, '_rate_limited_post',
                              side_effect=requests.exceptions.Timeout("timed out")):
                with patch.object(ollama_client, '_MAX_RETRIES', 1):
                    with self.assertRaises(ollama_client.OllamaUnavailableError):
                        ollama_client.query_ollama(SAMPLE_PROMPT)


if __name__ == "__main__":
    unittest.main()
