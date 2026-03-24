"""Tests for backend/config.py — env-driven configuration loading."""
import sys
import os
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))


def _reload_config(env_overrides: dict):
    """
    Reload config module with a controlled environment.
    dotenv loading is suppressed so only os.environ values are used.
    """
    import importlib
    with patch.dict(os.environ, env_overrides, clear=True):
        with patch('dotenv.load_dotenv'):  # suppress .env file reads
            import config
            importlib.reload(config)
            return config


class TestConfigDefaults(unittest.TestCase):
    """When no env vars are set, config must fall back to safe defaults."""

    def setUp(self):
        self.cfg = _reload_config({})

    def test_groq_url_has_default(self):
        self.assertEqual(
            self.cfg.GROQ_URL,
            "https://api.groq.com/openai/v1/chat/completions"
        )

    def test_groq_model_defaults_to_qwen(self):
        self.assertEqual(self.cfg.GROQ_MODEL, "qwen/qwen3-32b")

    def test_groq_min_interval_default_is_float(self):
        self.assertIsInstance(self.cfg.GROQ_MIN_INTERVAL, float)
        self.assertEqual(self.cfg.GROQ_MIN_INTERVAL, 10.0)

    def test_mock_groq_defaults_false(self):
        self.assertFalse(self.cfg.MOCK_GROQ)

    def test_groq_api_key_defaults_empty_string(self):
        self.assertEqual(self.cfg.GROQ_API_KEY, "")


class TestConfigFromEnv(unittest.TestCase):
    """Values from the environment must override defaults."""

    def test_groq_model_picked_up_from_env(self):
        cfg = _reload_config({"GROQ_MODEL": "qwen/qwen3-32b"})
        self.assertEqual(cfg.GROQ_MODEL, "qwen/qwen3-32b")

    def test_custom_model_picked_up(self):
        cfg = _reload_config({"GROQ_MODEL": "llama-3.3-70b-versatile"})
        self.assertEqual(cfg.GROQ_MODEL, "llama-3.3-70b-versatile")

    def test_groq_min_interval_cast_to_float(self):
        cfg = _reload_config({"GROQ_MIN_INTERVAL": "15"})
        self.assertIsInstance(cfg.GROQ_MIN_INTERVAL, float)
        self.assertEqual(cfg.GROQ_MIN_INTERVAL, 15.0)

    def test_mock_groq_truthy_values(self):
        for val in ("1", "true", "yes", "TRUE", "YES"):
            with self.subTest(val=val):
                cfg = _reload_config({"MOCK_GROQ": val})
                self.assertTrue(cfg.MOCK_GROQ)

    def test_mock_groq_falsy_values(self):
        for val in ("0", "false", "no", ""):
            with self.subTest(val=val):
                cfg = _reload_config({"MOCK_GROQ": val})
                self.assertFalse(cfg.MOCK_GROQ)

    def test_vault_path_picked_up_from_env(self):
        cfg = _reload_config({"VAULT_PATH": "/tmp/my_vault"})
        self.assertEqual(cfg.VAULT_PATH, "/tmp/my_vault")

    def test_groq_api_key_picked_up_from_env(self):
        cfg = _reload_config({"GROQ_API_KEY": "gsk_test_key"})
        self.assertEqual(cfg.GROQ_API_KEY, "gsk_test_key")

    def test_custom_groq_url(self):
        cfg = _reload_config({"GROQ_URL": "https://proxy.example.com/v1/chat"})
        self.assertEqual(cfg.GROQ_URL, "https://proxy.example.com/v1/chat")


class TestConfigTypes(unittest.TestCase):
    """All config values must be correctly typed regardless of env content."""

    def setUp(self):
        self.cfg = _reload_config({
            "GROQ_API_KEY": "key123",
            "GROQ_MODEL": "qwen/qwen3-32b",
            "GROQ_MIN_INTERVAL": "10",
            "MOCK_GROQ": "0",
            "VAULT_PATH": "./vault",
        })

    def test_groq_api_key_is_str(self):
        self.assertIsInstance(self.cfg.GROQ_API_KEY, str)

    def test_groq_url_is_str(self):
        self.assertIsInstance(self.cfg.GROQ_URL, str)

    def test_groq_model_is_str(self):
        self.assertIsInstance(self.cfg.GROQ_MODEL, str)

    def test_groq_min_interval_is_float(self):
        self.assertIsInstance(self.cfg.GROQ_MIN_INTERVAL, float)

    def test_mock_groq_is_bool(self):
        self.assertIsInstance(self.cfg.MOCK_GROQ, bool)

    def test_vault_path_is_str(self):
        self.assertIsInstance(self.cfg.VAULT_PATH, str)


class TestConfigRequire(unittest.TestCase):
    """_require() must raise EnvironmentError when a key is missing."""

    def test_require_raises_when_key_missing(self):
        cfg = _reload_config({})
        with self.assertRaises(EnvironmentError) as ctx:
            cfg._require("NONEXISTENT_KEY")
        self.assertIn("NONEXISTENT_KEY", str(ctx.exception))

    def test_require_returns_value_when_key_present(self):
        with patch.dict(os.environ, {"MY_KEY": "my_value"}):
            cfg = _reload_config({"MY_KEY": "my_value"})
            self.assertEqual(cfg._require("MY_KEY"), "my_value")


if __name__ == "__main__":
    unittest.main()
