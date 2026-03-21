#!/usr/bin/env bash
# init.sh — one-shot environment setup, then launches the analysis pipeline
#
# What it does:
#   1. Checks Python 3 is available
#   2. Creates a virtualenv (venv/) if one doesn't exist
#   3. Installs / upgrades Python dependencies from requirements.txt
#   4. Copies .env.example → .env if no .env is present, then prompts for GROQ_API_KEY
#   5. Clones external/llama.cpp if missing, or pulls latest if already present
#   6. Hands off to analyze.sh (all extra args are forwarded)
#
# Usage:
#   ./init.sh                   # full setup + analyze
#   ./init.sh --no-groq         # setup + offline/mock run
#   ./init.sh --workers 3       # setup + analyze with 3 workers

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

LLAMA_REPO="https://github.com/ggerganov/llama.cpp.git"
LLAMA_DIR="external/llama.cpp"

# ── helpers ───────────────────────────────────────────────────────────────────
info()    { echo -e "\033[1;34m[init]\033[0m $*"; }
success() { echo -e "\033[1;32m[init]\033[0m $*"; }
warn()    { echo -e "\033[1;33m[init]\033[0m $*"; }
die()     { echo -e "\033[1;31m[init]\033[0m ERROR: $*" >&2; exit 1; }

# ── 1. Python 3 check ─────────────────────────────────────────────────────────
info "Checking Python 3..."
PYTHON=$(command -v python3 || command -v python || true)
[ -z "$PYTHON" ] && die "Python 3 not found. Install it and re-run."
PY_VER=$("$PYTHON" -c "import sys; print(sys.version_info.major)")
[ "$PY_VER" -lt 3 ] && die "Python 3 required, found: $("$PYTHON" --version)"
success "Using $("$PYTHON" --version)"

# ── 2. Virtualenv ─────────────────────────────────────────────────────────────
if [ ! -f "venv/bin/activate" ]; then
    info "Creating virtual environment..."
    "$PYTHON" -m venv venv
    success "venv created."
else
    info "Virtual environment already exists, skipping creation."
fi

source venv/bin/activate

# ── 3. Dependencies ───────────────────────────────────────────────────────────
info "Installing / updating dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt
success "Dependencies ready."

# ── 4. .env setup ────────────────────────────────────────────────────────────
if [ ! -f ".env" ]; then
    warn ".env not found — copying from .env.example"
    cp .env.example .env

    echo ""
    echo "  ┌─────────────────────────────────────────────────────┐"
    echo "  │  A Groq API key is required to run analysis.        │"
    echo "  │  Get a free key at: https://console.groq.com        │"
    echo "  └─────────────────────────────────────────────────────┘"
    echo ""

    # If running interactively, prompt; otherwise skip and warn
    if [ -t 0 ]; then
        read -r -p "  Enter your GROQ_API_KEY (or press Enter to skip): " GROQ_KEY
        if [ -n "$GROQ_KEY" ]; then
            # Replace the placeholder in .env
            sed -i "s/^GROQ_API_KEY=.*/GROQ_API_KEY=${GROQ_KEY}/" .env
            success "GROQ_API_KEY saved to .env"
        else
            warn "Skipped — edit .env manually before analyzing."
        fi
    else
        warn "Non-interactive shell — edit .env and add your GROQ_API_KEY before running."
    fi
else
    info ".env already present, skipping."
fi

# ── 5. llama.cpp repo ─────────────────────────────────────────────────────────
mkdir -p external

if [ ! -d "$LLAMA_DIR/.git" ]; then
    info "Cloning llama.cpp (shallow clone)..."
    git clone --depth=1 "$LLAMA_REPO" "$LLAMA_DIR"
    success "llama.cpp cloned."
else
    info "llama.cpp already present — pulling latest changes..."
    git -C "$LLAMA_DIR" pull --ff-only --quiet && success "llama.cpp up to date." \
        || warn "Pull failed (local changes?). Continuing with existing version."
fi

# ── 6. Hand off to analyze.sh ────────────────────────────────────────────────
echo ""
success "Setup complete. Starting analysis..."
echo ""
exec bash "$SCRIPT_DIR/analyze.sh" "$@"
