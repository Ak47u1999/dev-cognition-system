"""Tests for backend/obsidian/writer.py — note saving and title sanitization."""
import sys
import os
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from obsidian.writer import sanitize_title, save_note, _ensure_vault


class TestSanitizeTitle(unittest.TestCase):
    def test_double_colon_replaced_with_double_underscore(self):
        self.assertEqual(sanitize_title("foo::bar"), "foo__bar")

    def test_forward_slash_removed(self):
        self.assertEqual(sanitize_title("foo/bar"), "foobar")

    def test_backslash_removed(self):
        self.assertEqual(sanitize_title("foo\\bar"), "foobar")

    def test_colon_removed(self):
        self.assertEqual(sanitize_title("foo:bar"), "foobar")

    def test_asterisk_removed(self):
        self.assertEqual(sanitize_title("foo*bar"), "foobar")

    def test_question_mark_removed(self):
        self.assertEqual(sanitize_title("foo?bar"), "foobar")

    def test_double_quote_removed(self):
        self.assertEqual(sanitize_title('foo"bar'), "foobar")

    def test_angle_brackets_removed(self):
        self.assertEqual(sanitize_title("foo<bar>"), "foobar")

    def test_pipe_removed(self):
        self.assertEqual(sanitize_title("foo|bar"), "foobar")

    def test_leading_trailing_whitespace_stripped(self):
        self.assertEqual(sanitize_title("  hello  "), "hello")

    def test_normal_name_unchanged(self):
        self.assertEqual(sanitize_title("my_function"), "my_function")

    def test_spaces_preserved(self):
        # sanitize_title does NOT strip internal spaces
        self.assertEqual(sanitize_title("Hello World"), "Hello World")

    def test_dotted_filename_preserved(self):
        self.assertEqual(sanitize_title("sample.c__add"), "sample.c__add")

    def test_double_colon_in_c_method(self):
        # e.g. "sample.c::add" -> "sample.c__add" with colon stripped
        # :: replaced with __, then lone : stripped
        result = sanitize_title("sample.c::add")
        self.assertEqual(result, "sample.c__add")


class TestEnsureVault(unittest.TestCase):
    def test_creates_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            target = os.path.join(tmpdir, "new_vault")
            self.assertFalse(os.path.exists(target))
            _ensure_vault(target)
            self.assertTrue(os.path.isdir(target))

    def test_idempotent_on_existing_directory(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # calling twice should not raise
            _ensure_vault(tmpdir)
            _ensure_vault(tmpdir)


class TestSaveNote(unittest.TestCase):
    def test_creates_markdown_file(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = save_note("my_note", "Some content.", vault_path=tmpdir)
            self.assertTrue(os.path.exists(path))
            self.assertTrue(path.endswith(".md"))

    def test_file_starts_with_h1_title(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = save_note("my_note", "Content here.", vault_path=tmpdir)
            with open(path) as f:
                text = f.read()
            self.assertTrue(text.startswith("# my_note"))

    def test_file_contains_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = save_note("my_note", "Important content.", vault_path=tmpdir)
            with open(path) as f:
                text = f.read()
            self.assertIn("Important content.", text)

    def test_title_sanitized_in_filename(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # "sample.c::add" → sanitized to "sample.c__add"
            path = save_note("sample.c::add", "body", vault_path=tmpdir)
            self.assertIn("sample.c__add", os.path.basename(path))

    def test_skip_if_exists_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            save_note("my_note", "original", vault_path=tmpdir)
            path = save_note("my_note", "overwritten", vault_path=tmpdir, skip_if_exists=True)
            with open(path) as f:
                text = f.read()
            self.assertNotIn("overwritten", text)
            self.assertIn("original", text)

    def test_overwrite_when_not_skipping(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            save_note("my_note", "original", vault_path=tmpdir)
            path = save_note("my_note", "updated", vault_path=tmpdir, skip_if_exists=False)
            with open(path) as f:
                text = f.read()
            self.assertIn("updated", text)

    def test_returns_file_path_string(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            result = save_note("some_note", "content", vault_path=tmpdir)
            self.assertIsInstance(result, str)

    def test_vault_created_if_not_exists(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            new_vault = os.path.join(tmpdir, "subdir", "vault")
            save_note("my_note", "content", vault_path=new_vault)
            self.assertTrue(os.path.isdir(new_vault))


if __name__ == "__main__":
    unittest.main()
