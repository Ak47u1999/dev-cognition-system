"""Tests for backend/parser/extractor.py — function extraction from C source."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from parser.extractor import extract_functions_from_source_bytes, extract_functions

# Minimal C source used across tests
SIMPLE_C = b"""
int add(int a, int b) {
    return a + b;
}

int mul(int a, int b) {
    return a * b;
}
"""

RECURSIVE_C = b"""
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}
"""

LOOP_C = b"""
void fill(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = i;
    }
}
"""


class TestExtractFunctionsFromSourceBytes(unittest.TestCase):
    def test_returns_list(self):
        result = extract_functions_from_source_bytes(SIMPLE_C)
        self.assertIsInstance(result, list)

    def test_finds_all_functions(self):
        result = extract_functions_from_source_bytes(SIMPLE_C)
        self.assertEqual(len(result), 2)

    def test_each_result_has_code_key(self):
        for fn in extract_functions_from_source_bytes(SIMPLE_C):
            self.assertIn("code", fn)

    def test_code_is_string(self):
        for fn in extract_functions_from_source_bytes(SIMPLE_C):
            self.assertIsInstance(fn["code"], str)

    def test_code_contains_return_statement(self):
        result = extract_functions_from_source_bytes(SIMPLE_C)
        sources = " ".join(fn["code"] for fn in result)
        self.assertIn("return", sources)

    def test_max_functions_limits_results(self):
        result = extract_functions_from_source_bytes(SIMPLE_C, max_functions=1)
        self.assertEqual(len(result), 1)

    def test_max_functions_zero_returns_empty(self):
        result = extract_functions_from_source_bytes(SIMPLE_C, max_functions=0)
        self.assertEqual(len(result), 0)

    def test_empty_source_returns_empty_list(self):
        result = extract_functions_from_source_bytes(b"")
        self.assertEqual(result, [])

    def test_source_with_only_declarations_returns_empty(self):
        src = b"extern void foo(int a);\nextern int bar(void);\n"
        result = extract_functions_from_source_bytes(src)
        self.assertEqual(result, [])

    def test_recursive_function_detected(self):
        result = extract_functions_from_source_bytes(RECURSIVE_C)
        self.assertGreater(len(result), 0)
        self.assertIn("factorial", result[0]["code"])

    def test_loop_function_detected(self):
        result = extract_functions_from_source_bytes(LOOP_C)
        self.assertGreater(len(result), 0)
        self.assertIn("for", result[0]["code"])

    def test_start_end_bytes_present(self):
        result = extract_functions_from_source_bytes(SIMPLE_C)
        for fn in result:
            self.assertIn("start", fn)
            self.assertIn("end", fn)

    def test_start_less_than_end(self):
        result = extract_functions_from_source_bytes(SIMPLE_C)
        for fn in result:
            self.assertLess(fn["start"], fn["end"])


class TestExtractFunctionsTreeSitter(unittest.TestCase):
    """Tests for the tree-sitter-backed extractor."""

    def _get_tree(self, source: bytes):
        from parser.parser import get_parser
        return get_parser().parse(source)

    def test_returns_list(self):
        tree = self._get_tree(SIMPLE_C)
        result = extract_functions(tree, SIMPLE_C)
        self.assertIsInstance(result, list)

    def test_finds_both_functions(self):
        tree = self._get_tree(SIMPLE_C)
        result = extract_functions(tree, SIMPLE_C)
        self.assertEqual(len(result), 2)

    def test_each_has_code_and_name(self):
        tree = self._get_tree(SIMPLE_C)
        for fn in extract_functions(tree, SIMPLE_C):
            self.assertIn("code", fn)
            self.assertIn("name", fn)

    def test_function_names_extracted(self):
        tree = self._get_tree(SIMPLE_C)
        names = {fn["name"] for fn in extract_functions(tree, SIMPLE_C)}
        self.assertIn("add", names)
        self.assertIn("mul", names)

    def test_code_slices_correctly(self):
        tree = self._get_tree(SIMPLE_C)
        result = extract_functions(tree, SIMPLE_C)
        for fn in result:
            # start/end are byte offsets into SIMPLE_C
            self.assertEqual(
                fn["code"],
                SIMPLE_C[fn["start"]:fn["end"]].decode("utf-8")
            )

    def test_empty_source(self):
        tree = self._get_tree(b"")
        result = extract_functions(tree, b"")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
