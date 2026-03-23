"""Tests for backend/pipeline.py — analyze_file end-to-end (no Groq API calls)."""
import sys
import os
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

# pipeline.py uses relative imports so we must run from backend/ context
# We patch query_groq to avoid any network calls
import pipeline


SAMPLE_C_PATH = os.path.join(os.path.dirname(__file__), '..', 'backend', 'sample.c')


class TestAnalyzeFile(unittest.TestCase):

    def test_returns_list_of_saved_paths(self):
        with tempfile.TemporaryDirectory() as vault:
            result = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False)
        self.assertIsInstance(result, list)

    def test_saves_at_least_one_note_for_sample_c(self):
        with tempfile.TemporaryDirectory() as vault:
            result = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False)
        self.assertGreater(len(result), 0)

    def test_saved_notes_are_markdown_files(self):
        with tempfile.TemporaryDirectory() as vault:
            for path in pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False):
                self.assertTrue(path.endswith(".md"), f"Expected .md, got: {path}")

    def test_max_functions_limits_notes(self):
        with tempfile.TemporaryDirectory() as vault:
            result = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False, max_functions=1)
        self.assertEqual(len(result), 1)

    def test_skip_existing_skips_already_written_notes(self):
        with tempfile.TemporaryDirectory() as vault:
            first_run = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False)
            second_run = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False, skip_existing=True)
        # second run should produce no new notes (all already exist)
        self.assertEqual(len(second_run), 0)

    def test_no_skip_rewrites_existing_notes(self):
        with tempfile.TemporaryDirectory() as vault:
            first = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False)
            second = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False, skip_existing=False)
        # Both runs should produce the same number of notes
        self.assertEqual(len(first), len(second))

    def test_note_content_includes_prompt_when_no_groq(self):
        with tempfile.TemporaryDirectory() as vault:
            paths = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False)
            with open(paths[0]) as f:
                content = f.read()
        # Without Groq the note should include the raw prompt section
        self.assertIn("Prompt", content)

    def test_groq_result_written_to_note(self):
        import json
        mock_payload = json.dumps({
            "title": "add", "summary": "Adds two ints.",
            "details": "Returns a + b.", "rationale": "Simple.", "performance": "O(1).",
            "hidden_insights": [], "where_used": [], "tags": [], "markdown": "## add\n\nAdds two ints."
        })
        with tempfile.TemporaryDirectory() as vault:
            with patch('pipeline.query_groq', return_value=mock_payload):
                paths = pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=True, max_functions=1)
            with open(paths[0]) as f:
                content = f.read()
        self.assertIn("Adds two ints.", content)

    def test_vault_subdirectory_created_per_file(self):
        with tempfile.TemporaryDirectory() as vault:
            pipeline.analyze_file(SAMPLE_C_PATH, vault, use_groq=False)
            stem = os.path.splitext(os.path.basename(SAMPLE_C_PATH))[0]
            self.assertTrue(os.path.isdir(os.path.join(vault, stem)))


if __name__ == "__main__":
    unittest.main()
