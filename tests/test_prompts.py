"""Tests for backend/ai/prompts.py — LLM prompt builder."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from ai.prompts import build_prompt


class TestBuildPrompt(unittest.TestCase):
    SIMPLE_CODE = "int add(int a, int b) { return a + b; }"

    def test_returns_string(self):
        result = build_prompt(self.SIMPLE_CODE)
        self.assertIsInstance(result, str)

    def test_contains_code(self):
        result = build_prompt(self.SIMPLE_CODE)
        self.assertIn(self.SIMPLE_CODE, result)

    def test_contains_all_json_keys(self):
        result = build_prompt(self.SIMPLE_CODE)
        for key in ("title", "summary", "details", "rationale",
                    "performance", "hidden_insights", "where_used", "tags", "markdown"):
            self.assertIn(key, result)

    def test_filename_included_in_header(self):
        result = build_prompt(self.SIMPLE_CODE, filename="add.c")
        self.assertIn("File: add.c", result)

    def test_no_filename_omits_file_header(self):
        result = build_prompt(self.SIMPLE_CODE)
        self.assertNotIn("File:", result)

    def test_instructs_json_only_output(self):
        result = build_prompt(self.SIMPLE_CODE)
        self.assertIn("JSON", result)

    def test_empty_code_still_returns_prompt(self):
        result = build_prompt("")
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 20)


if __name__ == "__main__":
    unittest.main()
