#!/usr/bin/env python3
"""
Batch pipeline: analyze all C files in a repository and save Obsidian notes.

Usage:
    python backend/batch_pipeline.py --repo external/llama.cpp --vault ./vault
    python backend/batch_pipeline.py --repo external/llama.cpp --skip-existing
"""
import os
import sys
import re
import json
import argparse
import warnings

# Suppress FutureWarning from tree-sitter
warnings.filterwarnings("ignore", category=FutureWarning)

sys.path.insert(0, os.path.dirname(__file__))
import config

from ai.ollama_client import query_ollama, OllamaUnavailableError
from ai.prompts import build_prompt
from ai.tagger import tag_code
from obsidian.writer import save_note, sanitize_title

_done = 0
_total = 0


def _log(msg: str):
    print(msg, flush=True)


def _increment_done():
    global _done
    _done += 1
    return _done


def find_c_files(repo_path: str, skip_dirs: set = None) -> list:
    # Only skip non-source directories; include tests, examples, etc.
    skip_dirs = skip_dirs or {".git", "build"}
    c_files = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for f in files:
            if f.endswith(".c") or f.endswith(".cpp"):
                c_files.append(os.path.join(root, f))
    return sorted(c_files)


def extract_functions_from_file(source_path: str) -> list:
    with open(source_path, "rb") as f:
        source_bytes = f.read()
    try:
        from parser.parser import get_parser
        from parser.extractor import extract_functions as ts_extract
        parser = get_parser()
        tree = parser.parse(source_bytes)
        return ts_extract(tree, source_bytes)
    except Exception:
        from parser.extractor import extract_functions_from_source_bytes
        return extract_functions_from_source_bytes(source_bytes)


def process_function(source_path: str, fn: dict, index: int,
                     vault_path: str, use_llm: bool, skip_existing: bool) -> str | None:
    basename = os.path.basename(source_path)
    file_stem = re.sub(r"[^a-zA-Z0-9_\-]", "_", os.path.splitext(basename)[0])
    file_vault = os.path.join(vault_path, file_stem)

    fn_name = fn.get("name") if isinstance(fn, dict) else None
    label = fn_name if fn_name else f"function_{index}"
    title = f"{basename}::{label}"

    if skip_existing:
        candidate = os.path.join(file_vault, sanitize_title(title) + ".md")
        if os.path.exists(candidate):
            done = _increment_done()
            _log(f"[{done}/{_total}] SKIP {title}")
            return None

    code = fn.get("code") if isinstance(fn, dict) else str(fn)
    prompt = build_prompt(code, filename=basename)
    result = None
    tps = None
    if use_llm:
        try:
            result, tps = query_ollama(prompt)
        except OllamaUnavailableError as e:
            print(f"\n[pipeline] FATAL: {e}", flush=True)
            sys.exit(1)
        except Exception as e:
            _log(f"  Ollama error for {title}: {e}")

    if result:
        try:
            payload = json.loads(result)
            md = payload.get("markdown") or payload.get("summary") or result
        except Exception:
            md = result
    else:
        md = "### Prompt\n\n```\n" + prompt + "\n```"

    tags = tag_code(fn.get("code") if isinstance(fn, dict) else None)
    if tags:
        md = "Tags: " + " ".join(["#" + t for t in tags]) + "\n\n" + md

    path = save_note(title, md, vault_path=file_vault)
    done = _increment_done()
    tps_str = f"  {tps:.1f} tok/s" if tps is not None else ""
    _log(f"[{done}/{_total}] Saved {path}{tps_str}")
    return path


def process_file(source_path: str, vault_path: str, use_llm: bool,
                 skip_existing: bool) -> list:
    funcs = extract_functions_from_file(source_path)
    saved = []
    for i, fn in enumerate(funcs, start=1):
        path = process_function(source_path, fn, i, vault_path, use_groq, skip_existing)
        if path:
            saved.append(path)
    return saved


def main():
    global _total

    p = argparse.ArgumentParser(description="Batch-analyze all C files in a repository.")
    p.add_argument("--repo", "-r", required=True, help="Path to the repository root")
    p.add_argument("--vault", "-v",
                   default=config.VAULT_PATH,
                   help="Obsidian vault output directory")
    p.add_argument("--no-llm", action="store_true", help="Save prompts only, skip Ollama calls")
    p.add_argument("--skip-existing", action="store_true", default=True,
                   help="Skip functions already saved to vault (default: True)")
    p.add_argument("--no-skip", dest="skip_existing", action="store_false",
                   help="Re-analyze even if note already exists")
    args = p.parse_args()

    c_files = find_c_files(args.repo)
    if not c_files:
        print(f"No .c / .cpp files found under {args.repo}")
        sys.exit(1)

    # Pre-count total functions
    print(f"Scanning {len(c_files)} C/C++ files...")
    all_tasks = []
    for path in c_files:
        funcs = extract_functions_from_file(path)
        for i, fn in enumerate(funcs, start=1):
            all_tasks.append((path, fn, i))

    _total = len(all_tasks)
    print(f"Found {_total} functions across {len(c_files)} files")
    print(f"Vault: {args.vault} | Skip existing: {args.skip_existing}\n")

    use_llm = not args.no_llm
    saved_count = 0

    for path, fn, idx in all_tasks:
        try:
            result = process_function(path, fn, idx, args.vault, use_llm, args.skip_existing)
            if result:
                saved_count += 1
        except Exception as e:
            _log(f"  ERROR processing {path} function {idx}: {e}")

    print(f"\nDone. {saved_count} new notes saved to {args.vault}")


if __name__ == "__main__":
    main()
