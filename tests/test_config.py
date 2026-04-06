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

    def test_ollama_url_has_default(self):
        self.assertEqual(
            self.cfg.OLLAMA_URL,
            "http://localhost:11434/v1/chat/completions"
        )

    def test_ollama_model_defaults_to_qwen(self):
        self.assertEqual(self.cfg.OLLAMA_MODEL, "qwen2.5-coder:14b")

    def test_ollama_min_interval_default_is_float(self):
        self.assertIsInstance(self.cfg.OLLAMA_MIN_INTERVAL, float)
        self.assertEqual(self.cfg.OLLAMA_MIN_INTERVAL, 0.0)

    def test_mock_llm_defaults_false(self):
        self.assertFalse(self.cfg.MOCK_LLM)


class TestConfigFromEnv(unittest.TestCase):
    """Values from the environment must override defaults."""

    def test_ollama_model_picked_up_from_env(self):
        cfg = _reload_config({"OLLAMA_MODEL": "qwen2.5-coder:14b"})
        self.assertEqual(cfg.OLLAMA_MODEL, "qwen2.5-coder:14b")

    def test_custom_model_picked_up(self):
        cfg = _reload_config({"OLLAMA_MODEL": "llama3.2:3b"})
        self.assertEqual(cfg.OLLAMA_MODEL, "llama3.2:3b")

    def test_ollama_min_interval_cast_to_float(self):
        cfg = _reload_config({"OLLAMA_MIN_INTERVAL": "15"})
        self.assertIsInstance(cfg.OLLAMA_MIN_INTERVAL, float)
        self.assertEqual(cfg.OLLAMA_MIN_INTERVAL, 15.0)

    def test_mock_llm_truthy_values(self):
        for val in ("1", "true", "yes", "TRUE", "YES"):
            with self.subTest(val=val):
                cfg = _reload_config({"MOCK_LLM": val})
                self.assertTrue(cfg.MOCK_LLM)

    def test_mock_llm_falsy_values(self):
        for val in ("0", "false", "no", ""):
            with self.subTest(val=val):
                cfg = _reload_config({"MOCK_LLM": val})
                self.assertFalse(cfg.MOCK_LLM)

    def test_vault_path_picked_up_from_env(self):
        cfg = _reload_config({"VAULT_PATH": "/tmp/my_vault"})
        self.assertEqual(cfg.VAULT_PATH, "/tmp/my_vault")

    def test_custom_ollama_url(self):
        cfg = _reload_config({"OLLAMA_URL": "http://192.168.1.10:11434/v1/chat/completions"})
        self.assertEqual(cfg.OLLAMA_URL, "http://192.168.1.10:11434/v1/chat/completions")


class TestConfigTypes(unittest.TestCase):
    """All config values must be correctly typed regardless of env content."""

    def setUp(self):
        self.cfg = _reload_config({
            "OLLAMA_MODEL": "qwen2.5-coder:14b",
            "OLLAMA_MIN_INTERVAL": "0",
            "MOCK_LLM": "0",
            "VAULT_PATH": "./vault",
        })

    def test_ollama_url_is_str(self):
        self.assertIsInstance(self.cfg.OLLAMA_URL, str)

    def test_ollama_model_is_str(self):
        self.assertIsInstance(self.cfg.OLLAMA_MODEL, str)

    def test_ollama_min_interval_is_float(self):
        self.assertIsInstance(self.cfg.OLLAMA_MIN_INTERVAL, float)

    def test_mock_llm_is_bool(self):
        self.assertIsInstance(self.cfg.MOCK_LLM, bool)

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
