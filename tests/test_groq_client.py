"""Tests for backend/ai/groq_client.py — fallback, mock, and rate-limiter logic."""
import sys
import os
import json
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

import ai.groq_client as groq_client


SAMPLE_PROMPT = (
    "Analyze the following C function...\n\nCode:\n\nint add(int a, int b) { return a + b; }"
)


class TestFallbackResponse(unittest.TestCase):
    def _parse(self, prompt, error=None):
        raw = groq_client._fallback_response_from_prompt(prompt, error=error)
        return json.loads(raw)  # must be valid JSON

    def test_returns_valid_json(self):
        raw = groq_client._fallback_response_from_prompt(SAMPLE_PROMPT)
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
        data = self._parse(SAMPLE_PROMPT, error="rate_limit_exceeded")
        self.assertIn("rate_limit_exceeded", data["markdown"])

    def test_no_error_field_in_markdown_when_none(self):
        data = self._parse(SAMPLE_PROMPT, error=None)
        self.assertNotIn("Note:", data["markdown"])

    def test_generic_prompt_without_code_marker(self):
        # No "Code:\n\n" marker — function should not crash
        data = self._parse("just a raw prompt with no marker")
        self.assertIsInstance(data, dict)


class TestMockResponse(unittest.TestCase):
    def test_returns_valid_json(self):
        raw = groq_client._mock_response(SAMPLE_PROMPT)
        data = json.loads(raw)
        self.assertIsInstance(data, dict)

    def test_same_as_fallback(self):
        # _mock_response is a thin wrapper around _fallback_response_from_prompt
        mock_raw = groq_client._mock_response(SAMPLE_PROMPT)
        fallback_raw = groq_client._fallback_response_from_prompt(SAMPLE_PROMPT, error="MOCK_RESPONSE")
        self.assertEqual(json.loads(mock_raw), json.loads(fallback_raw))


class TestQueryGroqMockMode(unittest.TestCase):
    def test_returns_fallback_when_mock_env_set(self):
        with patch.dict(os.environ, {"MOCK_GROQ": "1", "GROQ_API_KEY": "fake"}):
            # Reload module-level constants that were captured at import time
            with patch.object(groq_client, 'MOCK', True):
                result = groq_client.query_groq(SAMPLE_PROMPT)
        data = json.loads(result)
        self.assertIsInstance(data, dict)

    def test_returns_fallback_when_no_api_key(self):
        with patch.object(groq_client, 'GROQ_API_KEY', None):
            with patch.object(groq_client, 'MOCK', False):
                result = groq_client.query_groq(SAMPLE_PROMPT)
        data = json.loads(result)
        self.assertIsInstance(data, dict)

    def test_returns_fallback_on_http_error(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.raise_for_status.side_effect = Exception("server error")
        mock_resp.text = "Internal Server Error"

        with patch.object(groq_client, 'MOCK', False):
            with patch.object(groq_client, 'GROQ_API_KEY', 'fake-key'):
                with patch.object(groq_client, '_rate_limited_post', return_value=mock_resp):
                    result = groq_client.query_groq(SAMPLE_PROMPT)
        data = json.loads(result)
        self.assertIsInstance(data, dict)

    def test_returns_content_on_success(self):
        expected_content = json.dumps({"title": "add", "summary": "adds two ints",
                                       "details": "", "rationale": "", "performance": "",
                                       "hidden_insights": [], "where_used": [], "tags": [],
                                       "markdown": ""})
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.return_value = {
            "choices": [{"message": {"content": expected_content}}]
        }

        with patch.object(groq_client, 'MOCK', False):
            with patch.object(groq_client, 'GROQ_API_KEY', 'fake-key'):
                with patch.object(groq_client, '_rate_limited_post', return_value=mock_resp):
                    result = groq_client.query_groq(SAMPLE_PROMPT)
        self.assertEqual(result, expected_content)


class TestQueryGroq429Retry(unittest.TestCase):
    """429 responses must be retried with backoff, not immediately fall back."""

    def _make_429(self, retry_after=None):
        resp = MagicMock()
        resp.status_code = 429
        resp.raise_for_status.return_value = None
        headers = {}
        if retry_after is not None:
            headers["retry-after"] = retry_after
        resp.headers = headers
        return resp

    def _make_200(self, content="ok"):
        resp = MagicMock()
        resp.status_code = 200
        resp.raise_for_status.return_value = None
        resp.json.return_value = {"choices": [{"message": {"content": content}}]}
        return resp

    @patch('time.sleep', return_value=None)
    def test_retries_after_429_and_succeeds(self, mock_sleep):
        """After one 429, the next call should succeed and return real content."""
        expected = json.dumps({"title": "add"})
        side_effects = [self._make_429(), self._make_200(expected)]

        with patch.object(groq_client, 'MOCK', False):
            with patch.object(groq_client, 'GROQ_API_KEY', 'fake-key'):
                with patch.object(groq_client, '_rate_limited_post', side_effect=side_effects):
                    result = groq_client.query_groq(SAMPLE_PROMPT)

        self.assertEqual(result, expected)
        mock_sleep.assert_called()  # must have waited before retrying

    @patch('time.sleep', return_value=None)
    def test_uses_retry_after_header_numeric(self, mock_sleep):
        """retry-after: "20" should sleep for 20 seconds."""
        resp_429 = self._make_429(retry_after="20")
        resp_200 = self._make_200("content")

        with patch.object(groq_client, 'MOCK', False):
            with patch.object(groq_client, 'GROQ_API_KEY', 'fake-key'):
                with patch.object(groq_client, '_rate_limited_post',
                                  side_effect=[resp_429, resp_200]):
                    groq_client.query_groq(SAMPLE_PROMPT)

        mock_sleep.assert_any_call(20.0)

    @patch('time.sleep', return_value=None)
    def test_uses_retry_after_header_with_s_suffix(self, mock_sleep):
        """retry-after: "10s" (string with suffix) should parse to 10.0."""
        resp_429 = self._make_429(retry_after="10s")
        resp_200 = self._make_200("content")

        with patch.object(groq_client, 'MOCK', False):
            with patch.object(groq_client, 'GROQ_API_KEY', 'fake-key'):
                with patch.object(groq_client, '_rate_limited_post',
                                  side_effect=[resp_429, resp_200]):
                    groq_client.query_groq(SAMPLE_PROMPT)

        mock_sleep.assert_any_call(10.0)

    @patch('time.sleep', return_value=None)
    def test_falls_back_after_max_retries_exhausted(self, mock_sleep):
        """If every attempt returns 429, fall back gracefully after max retries."""
        with patch.object(groq_client, 'MOCK', False):
            with patch.object(groq_client, 'GROQ_API_KEY', 'fake-key'):
                with patch.object(groq_client, '_rate_limited_post',
                                  return_value=self._make_429()):
                    with patch.object(groq_client, '_MAX_RETRIES', 3):
                        result = groq_client.query_groq(SAMPLE_PROMPT)

        data = json.loads(result)
        self.assertIsInstance(data, dict)  # graceful fallback, not an exception

    @patch('time.sleep', return_value=None)
    def test_exponential_backoff_without_header(self, mock_sleep):
        """Without a retry-after header, backoff should grow exponentially."""
        resp_429_1 = self._make_429()  # no header
        resp_429_2 = self._make_429()
        resp_200 = self._make_200("ok")

        with patch.object(groq_client, 'MOCK', False):
            with patch.object(groq_client, 'GROQ_API_KEY', 'fake-key'):
                with patch.object(groq_client, '_RETRY_BASE', 5.0):
                    with patch.object(groq_client, '_rate_limited_post',
                                      side_effect=[resp_429_1, resp_429_2, resp_200]):
                        groq_client.query_groq(SAMPLE_PROMPT)

        sleep_calls = [c.args[0] for c in mock_sleep.call_args_list]
        # attempt 0 → 5*2^0=5, attempt 1 → 5*2^1=10
        self.assertIn(5.0, sleep_calls)
        self.assertIn(10.0, sleep_calls)


if __name__ == "__main__":
    unittest.main()

