import os
import re
from datetime import datetime

VAULT_PATH = os.getenv("VAULT_PATH", os.path.join(os.getcwd(), "vault"))


def _ensure_vault(path: str):
    os.makedirs(path, exist_ok=True)
    return path


def _sanitize_title(title: str) -> str:
    title = title.replace("::", "__")
    title = re.sub(r'[\\/*?:"<>|]', '', title)
    title = title.strip()
    return title


def save_note(title: str, content: str, vault_path: str = None) -> str:
    vault_path = vault_path or VAULT_PATH
    _ensure_vault(vault_path)
    title = _sanitize_title(title)
    filename = os.path.join(vault_path, f"{title}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(content)
        f.write("\n")
    return filename
