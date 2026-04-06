"""Client for local Ollama inference via its OpenAI-compatible HTTP API."""
import time
import threading
import requests
from typing import Optional
import json
import re

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import config

OLLAMA_URL = config.OLLAMA_URL
DEFAULT_MODEL = config.OLLAMA_MODEL
MOCK = config.MOCK_LLM

_MAX_RETRIES = 3
_RETRY_DELAY = 5.0  # seconds between retries on connection errors


class OllamaUnavailableError(RuntimeError):
    """Raised when Ollama cannot be reached after all retries — pipeline should abort."""

# Optional rate limiter: enforces minimum interval between API calls (default 0 for local)
_RATE_LOCK = threading.Lock()
_MIN_INTERVAL = config.OLLAMA_MIN_INTERVAL
_last_call_time: float = 0.0

# Local models can take time on first token; give generous timeout
_DEFAULT_TIMEOUT = 120


def _fallback_response_from_prompt(prompt: str, error: Optional[str] = None) -> str:
    """Generate a conservative JSON analysis from the prompt when Ollama is unavailable."""
    code = prompt
    marker = "\nCode:\n\n"
    if marker in prompt:
        code = prompt.split(marker, 1)[1]
    code = "\n".join([ln for ln in code.splitlines() if not ln.strip().startswith('#')])
    name = "function"
    m = re.search(r"([A-Za-z_][A-Za-z0-9_:<>]*)\s*\(", code)
    if m:
        cand = m.group(1)
        if cand not in ("if", "for", "while", "switch", "return", "sizeof",
                        "typedef", "else", "struct", "union", "enum", "defined"):
            name = cand
    tags = []
    details = []
    if any(tok in code for tok in ("malloc", "calloc", "realloc", "free", "memcpy", "memmove", "new", "delete")):
        tags.append("memory")
        details.append("Performs heap allocations or raw memory operations.")
    if any(tok in code for tok in ("for(", "for ", "while(", "while ", "do ")):
        tags.append("loop")
        details.append("Contains loops — consider iteration cost and early exits.")
    brace_pos = code.find('{')
    if brace_pos != -1 and name != "function":
        body = code[brace_pos + 1:]
        if re.search(r"\b" + re.escape(name) + r"\s*\(", body):
            tags.append("recursion")
            details.append("Calls itself — check recursion depth and tail-call possibility.")
    summary = f"Auto-generated analysis for {name}."
    payload = {
        "title": name,
        "summary": summary,
        "details": "\n".join(details) if details else "No detailed analysis available.",
        "rationale": "Heuristic fallback analysis (no LLM).",
        "performance": "Consider algorithmic complexity where loops or recursion are present.",
        "hidden_insights": [],
        "where_used": [],
        "tags": tags,
        "markdown": f"## {name}\n\n{summary}\n\n"
                    + ("\n".join(["- " + d for d in details]) if details else "")
                    + ("\n\n**Note:** Ollama error: " + str(error) if error else "")
    }
    return json.dumps(payload)


def _rate_limited_post(payload: dict, timeout: int) -> requests.Response:
    """Post to Ollama with an optional minimum inter-call interval."""
    global _last_call_time
    headers = {"Content-Type": "application/json"}
    with _RATE_LOCK:
        now = time.monotonic()
        wait = _MIN_INTERVAL - (now - _last_call_time)
        if wait > 0:
            time.sleep(wait)
        _last_call_time = time.monotonic()
    return requests.post(OLLAMA_URL, headers=headers, json=payload, timeout=timeout)


def query_ollama(
    prompt: str,
    system: Optional[str] = "You are a senior systems engineer.",
    model: Optional[str] = None,
    timeout: int = _DEFAULT_TIMEOUT,
) -> tuple[str, Optional[float]]:
    """
    Query the local Ollama chat completions endpoint.
    Returns (content, tokens_per_sec). tokens_per_sec is None on fallback/mock.
    Retries on connection errors with a short delay.
    """
    if MOCK:
        return _fallback_response_from_prompt(prompt, error="MOCK_LLM"), None

    model = model or DEFAULT_MODEL
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.0,
        "keep_alive": -1,
    }

    for attempt in range(_MAX_RETRIES):
        try:
            t0 = time.monotonic()
            resp = _rate_limited_post(payload, timeout)
            elapsed = time.monotonic() - t0
            resp.raise_for_status()
            data = resp.json()
            try:
                content = data["choices"][0]["message"]["content"]
                content = re.sub(r"^```[a-zA-Z]*\n?", "", content.strip())
                content = re.sub(r"\n?```$", "", content.strip())
                completion_tokens = data.get("usage", {}).get("completion_tokens")
                tps = (completion_tokens / elapsed) if completion_tokens and elapsed > 0 else None
                return content.strip(), tps
            except Exception as e:
                return _fallback_response_from_prompt(prompt, error=f"unexpected-structure:{e}"), None
        except requests.exceptions.ConnectionError as e:
            print(f"[ollama] Connection error (attempt {attempt + 1}/{_MAX_RETRIES}): {e}")
            if attempt < _MAX_RETRIES - 1:
                time.sleep(_RETRY_DELAY)
            else:
                raise OllamaUnavailableError(
                    f"Ollama unreachable at {OLLAMA_URL} after {_MAX_RETRIES} attempts. "
                    "Is the service running?"
                ) from e
        except requests.exceptions.Timeout as e:
            print(f"[ollama] Timeout after {timeout}s (attempt {attempt + 1}/{_MAX_RETRIES}): {e}")
            if attempt < _MAX_RETRIES - 1:
                time.sleep(_RETRY_DELAY)
            else:
                raise OllamaUnavailableError(
                    f"Ollama timed out after {timeout}s on {_MAX_RETRIES} attempts. "
                    "Service may be overloaded or crashed."
                ) from e
        except requests.HTTPError as e:
            try:
                err_text = resp.text
            except Exception:
                err_text = str(e)
            return _fallback_response_from_prompt(prompt, error=err_text), None
        except Exception as e:
            return _fallback_response_from_prompt(prompt, error=str(e)), None

    # unreachable — loop always returns or raises
    raise OllamaUnavailableError("Ollama unavailable.")


# kept for internal tests that exercise the fallback path
def _mock_response(prompt: str) -> str:
    return _fallback_response_from_prompt(prompt, error="MOCK_RESPONSE")
