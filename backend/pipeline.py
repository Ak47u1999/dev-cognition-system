#!/usr/bin/env python3
import os
import json
import argparse
import re
from typing import Optional
import config

from ai.groq_client import query_groq
from ai.prompts import build_prompt
from ai.tagger import tag_code
from obsidian.writer import save_note, sanitize_title
from parser.extractor import extract_functions_from_source_bytes


def analyze_file(source_path: str, vault_path: str, use_groq: bool = True,
                 max_functions: Optional[int] = None, skip_existing: bool = False):
    basename = os.path.basename(source_path)
    file_stem = re.sub(r'[^a-zA-Z0-9_\-]', '_', os.path.splitext(basename)[0])
    file_vault = os.path.join(vault_path, file_stem)

    with open(source_path, "rb") as f:
        source_bytes = f.read()
    # Try tree-sitter first if available, fall back to heuristic extractor
    funcs = None
    try:
        from parser.parser import get_parser
        from parser.extractor import extract_functions as ts_extract
        parser = get_parser()
        tree = parser.parse(source_bytes)
        funcs = ts_extract(tree, source_bytes)
    except Exception as e:
        print("Tree-sitter not available or failed, using fallback extractor:", e)
        funcs = extract_functions_from_source_bytes(source_bytes, max_functions)

    if max_functions:
        funcs = funcs[:int(max_functions)]
    saved = []
    for i, fn in enumerate(funcs, start=1):
        fn_name = fn.get("name") if isinstance(fn, dict) else None
        label = fn_name if fn_name else f"function_{i}"
        title = f"{basename}::{label}"

        if skip_existing:
            candidate = os.path.join(file_vault, sanitize_title(title) + ".md")
            if os.path.exists(candidate):
                continue

        code = fn.get("code") if isinstance(fn, dict) else str(fn)
        prompt = build_prompt(code, filename=basename)
        result = None
        if use_groq:
            try:
                result = query_groq(prompt)
            except Exception as e:
                print("Groq request failed:", e)
                result = None
        if result:
            try:
                payload = json.loads(result)
                md = payload.get("markdown") or payload.get("summary") or result
            except Exception:
                md = result
        else:
            md = "### Prompt\n\n" + "```\n" + prompt + "\n```"
        # heuristic tagging
        tags = tag_code(fn.get("code") if isinstance(fn, dict) else None)
        if tags:
            tag_line = "Tags: " + " ".join(["#" + t for t in tags]) + "\n\n"
            md = tag_line + md
        path = save_note(title, md, vault_path=file_vault)
        print("Saved note:", path)
        saved.append(path)
    return saved


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", "-s", default="backend/sample.c", help="C source file to analyze")
    p.add_argument("--vault", "-v", default=config.VAULT_PATH, help="Obsidian vault path")
    p.add_argument("--no-groq", action="store_true", help="Do not call Groq; save prompts instead")
    p.add_argument("--max", type=int, help="Max functions to process")
    p.add_argument("--skip-existing", action="store_true", default=True, help="Skip functions already saved to vault (default: True)")
    p.add_argument("--no-skip", dest="skip_existing", action="store_false",
                   help="Re-analyze even if note already exists")
    args = p.parse_args()
    analyze_file(args.source, args.vault, use_groq=not args.no_groq, max_functions=args.max, skip_existing=args.skip_existing)


if __name__ == "__main__":
    main()
