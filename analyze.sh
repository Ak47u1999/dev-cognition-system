#!/usr/bin/env bash
# analyze.sh — activate venv and launch the batch analysis pipeline
# Usage:
#   ./analyze.sh                        # default: external/llama.cpp → ./vault
#   ./analyze.sh --workers 3            # extra args forwarded to batch_pipeline.py
#   ./analyze.sh --no-groq              # offline / mock run
#   ./analyze.sh --repo /path/to/repo   # analyze a different repo

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate virtualenv if present
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

exec python3 backend/batch_pipeline.py \
    --repo external/llama.cpp \
    --vault ./vault \
    --skip-existing \
    "$@"
