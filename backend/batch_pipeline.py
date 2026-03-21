#!/usr/bin/env python3
"""
Batch pipeline: analyze all C files in a repository and save Obsidian notes.

Usage:
    python backend/batch_pipeline.py --repo external/llama.cpp --vault ./vault
    python backend/batch_pipeline.py --repo external/llama.cpp --workers 5 --skip-existing
"""
import os
import sys
import re
import json
import argparse
import threading
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv

load_dotenv()

# Suppress FutureWarning from tree-sitter
warnings.filterwarnings("ignore", category=FutureWarning)

sys.path.insert(0, os.path.dirname(__file__))

from ai.groq_client import query_groq
from ai.prompts import build_prompt
from ai.tagger import tag_code
from obsidian.writer import save_note

_print_lock = threading.Lock()
_counter_lock = threading.Lock()
_done = 0
_total = 0


def _log(msg: str):
    with _print_lock:
        print(msg, flush=True)


def _increment_done():
    global _done
    with _counter_lock:
        _done += 1
        return _done


def find_c_files(repo_path: str, skip_dirs: set = None) -> list:
    skip_dirs = skip_dirs or {"build", ".git", "tests", "test", "examples", "ci", "docs", "scripts"}
    c_files = []
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for f in files:
            if f.endswith(".c"):
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
                     vault_path: str, use_groq: bool, skip_existing: bool) -> str | None:
    basename = os.path.basename(source_path)
    file_stem = re.sub(r"[^a-zA-Z0-9_\-]", "_", os.path.splitext(basename)[0])
    file_vault = os.path.join(vault_path, file_stem)

    fn_name = fn.get("name") if isinstance(fn, dict) else None
    label = fn_name if fn_name else f"function_{index}"
    title = f"{basename}::{label}"

    if skip_existing:
        safe = re.sub(r"[^\w\-]", "_", title)
        candidate = os.path.join(file_vault, safe + ".md")
        if os.path.exists(candidate):
            done = _increment_done()
            _log(f"[{done}/{_total}] SKIP {title}")
            return None

    code = fn.get("code") if isinstance(fn, dict) else str(fn)
    prompt = build_prompt(code, filename=basename)
    result = None
    if use_groq:
        try:
            result = query_groq(prompt)
        except Exception as e:
            _log(f"  Groq error for {title}: {e}")

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
    _log(f"[{done}/{_total}] Saved {path}")
    return path


def process_file(source_path: str, vault_path: str, use_groq: bool,
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
                   default=os.getenv("VAULT_PATH", os.path.join(os.getcwd(), "vault")),
                   help="Obsidian vault output directory")
    p.add_argument("--workers", "-w", type=int, default=5,
                   help="Number of concurrent Groq workers (default: 5)")
    p.add_argument("--no-groq", action="store_true", help="Save prompts only, skip Groq calls")
    p.add_argument("--skip-existing", action="store_true", default=True,
                   help="Skip functions already saved to vault (default: True)")
    p.add_argument("--no-skip", dest="skip_existing", action="store_false",
                   help="Re-analyze even if note already exists")
    args = p.parse_args()

    c_files = find_c_files(args.repo)
    if not c_files:
        print(f"No .c files found under {args.repo}")
        sys.exit(1)

    # Pre-count total functions
    print(f"Scanning {len(c_files)} C files...")
    all_tasks = []
    for path in c_files:
        funcs = extract_functions_from_file(path)
        for i, fn in enumerate(funcs, start=1):
            all_tasks.append((path, fn, i))

    _total = len(all_tasks)
    print(f"Found {_total} functions across {len(c_files)} files")
    print(f"Vault: {args.vault} | Workers: {args.workers} | Skip existing: {args.skip_existing}\n")

    use_groq = not args.no_groq
    saved_count = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(process_function, path, fn, idx,
                            args.vault, use_groq, args.skip_existing): (path, idx)
            for path, fn, idx in all_tasks
        }
        for future in as_completed(futures):
            try:
                result = future.result()
                if result:
                    saved_count += 1
            except Exception as e:
                src, idx = futures[future]
                _log(f"  ERROR processing {src} function {idx}: {e}")

    print(f"\nDone. {saved_count} new notes saved to {args.vault}")


if __name__ == "__main__":
    main()
