"""
Central configuration — single source of truth for all env-driven settings.
load_dotenv() is called here so any module that imports config gets the .env values,
regardless of import order.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the project root (two levels up from backend/)
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=_env_path, override=False)


def _require(key: str) -> str:
    val = os.getenv(key)
    if not val:
        raise EnvironmentError(f"Required environment variable '{key}' is not set. Check your .env file.")
    return val


# ── Ollama ────────────────────────────────────────────────────────────────────
OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434/v1/chat/completions")
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "qwen2.5-coder:14b")
OLLAMA_MIN_INTERVAL: float = float(os.getenv("OLLAMA_MIN_INTERVAL", "0"))
MOCK_LLM: bool = os.getenv("MOCK_LLM", "0").lower() in ("1", "true", "yes")

# ── Vault ─────────────────────────────────────────────────────────────────────
VAULT_PATH: str = os.getenv("VAULT_PATH", str(Path.cwd() / "vault"))
