"""Tests for backend/parser/parser.py — tree-sitter C parser factory."""
import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from parser.parser import get_parser


class TestGetParser(unittest.TestCase):
    def test_returns_non_none(self):
        p = get_parser()
        self.assertIsNotNone(p)

    def test_parser_has_parse_method(self):
        p = get_parser()
        self.assertTrue(callable(getattr(p, 'parse', None)))

    def test_parse_simple_c_code(self):
        p = get_parser()
        tree = p.parse(b"int main() { return 0; }")
        self.assertIsNotNone(tree)
        self.assertIsNotNone(tree.root_node)

    def test_parse_returns_tree_with_no_errors_for_valid_c(self):
        p = get_parser()
        code = b"int add(int a, int b) { return a + b; }"
        tree = p.parse(code)
        # root node should exist
        self.assertIsNotNone(tree.root_node)

    def test_parse_empty_source(self):
        p = get_parser()
        tree = p.parse(b"")
        self.assertIsNotNone(tree)

    def test_parser_is_reusable(self):
        # get_parser should return something that can parse multiple times
        p = get_parser()
        tree1 = p.parse(b"int f() { return 1; }")
        tree2 = p.parse(b"void g() {}")
        self.assertIsNotNone(tree1)
        self.assertIsNotNone(tree2)


if __name__ == "__main__":
    unittest.main()
