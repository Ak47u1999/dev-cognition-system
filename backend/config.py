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


# ── Groq ──────────────────────────────────────────────────────────────────────
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
GROQ_URL: str = os.getenv("GROQ_URL", "https://api.groq.com/openai/v1/chat/completions")
GROQ_MODEL: str = os.getenv("GROQ_MODEL", "qwen/qwen3-32b")
GROQ_MIN_INTERVAL: float = float(os.getenv("GROQ_MIN_INTERVAL", "10"))
MOCK_GROQ: bool = os.getenv("MOCK_GROQ", "0").lower() in ("1", "true", "yes")

# ── Vault ─────────────────────────────────────────────────────────────────────
VAULT_PATH: str = os.getenv("VAULT_PATH", str(Path.cwd() / "vault"))
