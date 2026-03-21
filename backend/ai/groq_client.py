import os
import time
import threading
import requests
from typing import Optional
import json
import re

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_URL = os.getenv("GROQ_URL", "https://api.groq.com/openai/v1/chat/completions")
DEFAULT_MODEL = os.getenv("GROQ_MODEL", "llama-3.1-8b-instant")
MOCK = os.getenv("MOCK_GROQ", "0").lower() in ("1", "true", "yes")

_MAX_RETRIES = 6
_RETRY_BASE = 5.0  # seconds base for exponential backoff on 429

# Global rate limiter: enforce minimum interval between API calls across all threads
# llama-3.1-8b-instant free tier: ~30 req/min → 1 req per 2.5s to be safe
_RATE_LOCK = threading.Lock()
_MIN_INTERVAL = float(os.getenv("GROQ_MIN_INTERVAL", "2.5"))
_last_call_time: float = 0.0


def _fallback_response_from_prompt(prompt: str, error: Optional[str] = None) -> str:
    """Generate a conservative JSON analysis from the prompt when the Groq API is unavailable or returns an error."""
    # Try to extract code after a 'Code:' marker
    code = prompt
    marker = "\nCode:\n\n"
    if marker in prompt:
        code = prompt.split(marker, 1)[1]
    # drop preprocessor directives to avoid macro matches like defined(...)
    code = "\n".join([ln for ln in code.splitlines() if not ln.strip().startswith('#')])
    # very small heuristic analysis
    name = "function"
    # find probable function name by looking for identifier before first '(' that is not a keyword
    m = re.search(r"([A-Za-z_][A-Za-z0-9_:<>]*)\s*\(", code)
    if m:
        cand = m.group(1)
        if cand not in ("if", "for", "while", "switch", "return", "sizeof", "typedef", "else", "struct", "union", "enum", "defined"):
            name = cand
    tags = []
    hidden = []
    details = []
    if any(tok in code for tok in ("malloc", "calloc", "realloc", "free", "memcpy", "memmove", "new", "delete")):
        tags.append("memory")
        details.append("Performs heap allocations or raw memory operations.")
    if any(tok in code for tok in ("for(", "for ", "while(", "while ", "do ")):
        tags.append("loop")
        details.append("Contains loops — consider iteration cost and early exits.")
    # detect potential recursion (name used in body after first brace)
    brace_pos = code.find('{')
    if brace_pos != -1 and name != "function":
        body = code[brace_pos+1:]
        # avoid matching the function declaration region by ensuring occurrence is after the first '(' that belongs to the signature
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
        "hidden_insights": hidden,
        "where_used": [],
        "tags": tags,
        "markdown": f"## {name}\n\n{summary}\n\n" + ("\n".join(["- " + d for d in details]) if details else "" ) + ("\n\n**Note:** Groq API error: " + str(error) if error else "")
    }
    return json.dumps(payload)


def _rate_limited_post(headers, payload, timeout):
    """Serialize all API calls with a minimum inter-call interval."""
    global _last_call_time
    with _RATE_LOCK:
        now = time.monotonic()
        wait = _MIN_INTERVAL - (now - _last_call_time)
        if wait > 0:
            time.sleep(wait)
        _last_call_time = time.monotonic()
    return requests.post(GROQ_URL, headers=headers, json=payload, timeout=timeout)


def query_groq(prompt: str, system: Optional[str] = "You are a senior systems engineer.", model: Optional[str] = None, timeout: int = 30) -> str:
    """
    Query Groq chat completions endpoint and return the assistant message content.
    Falls back to a mock response if GROQ_API_KEY is not set or MOCK_GROQ env var is true.
    Retries with exponential backoff on 429 rate-limit responses.
    """
    if MOCK or not GROQ_API_KEY:
        return _fallback_response_from_prompt(prompt, error="MOCK_OR_NO_KEY")

    model = model or DEFAULT_MODEL
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.0
    }

    for attempt in range(_MAX_RETRIES):
        try:
            resp = _rate_limited_post(headers, payload, timeout)
            if resp.status_code == 429:
                retry_after = resp.headers.get("retry-after") or resp.headers.get("x-ratelimit-reset-requests")
                if retry_after:
                    wait = float(retry_after)
                else:
                    wait = _RETRY_BASE * (2 ** attempt)
                if attempt < _MAX_RETRIES - 1:
                    time.sleep(wait)
                    continue
            resp.raise_for_status()
            data = resp.json()
            try:
                return data["choices"][0]["message"]["content"]
            except Exception as e:
                return _fallback_response_from_prompt(prompt, error=f"unexpected-structure:{e}")
        except requests.HTTPError as e:
            try:
                err_text = resp.text
            except Exception:
                err_text = str(e)
            return _fallback_response_from_prompt(prompt, error=err_text)
        except Exception as e:
            return _fallback_response_from_prompt(prompt, error=str(e))

    return _fallback_response_from_prompt(prompt, error="max-retries-exceeded")


# keep older mock response function name for compatibility
def _mock_response(prompt: str) -> str:
    return _fallback_response_from_prompt(prompt, error="MOCK_RESPONSE")
