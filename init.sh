#!/usr/bin/env bash
# init.sh — one-shot environment setup, then launches the analysis pipeline
#
# What it does:
#   1. Checks Python 3 is available
#   2. Creates a virtualenv (venv/) if one doesn't exist
#   3. Installs / upgrades Python dependencies from requirements.txt
#   4. Creates .env pre-configured for local Ollama (qwen2.5-coder:14b)
#   5. Clones external/llama.cpp if missing, or pulls latest if already present
#   6. Hands off to analyze.sh (all extra args are forwarded)
#
# Usage:
#   ./init.sh                   # full setup + analyze
#   ./init.sh --no-groq         # setup + offline/mock run
#   ./init.sh --workers 4       # setup + analyze with 4 workers

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

# ── 0. System dependencies (Debian/Ubuntu only) ──────────────────────────────
if command -v apt-get &>/dev/null; then
    PKGS_NEEDED=()
    command -v python3   &>/dev/null || PKGS_NEEDED+=(python3)
    command -v git       &>/dev/null || PKGS_NEEDED+=(git)
    python3 -m venv --help &>/dev/null 2>&1 || PKGS_NEEDED+=(python3-venv)
    python3 -m pip  --version &>/dev/null 2>&1 || PKGS_NEEDED+=(python3-pip)

    if [ ${#PKGS_NEEDED[@]} -gt 0 ]; then
        info "Installing system packages: ${PKGS_NEEDED[*]}"
        sudo apt-get update -y -qq
        sudo apt-get install -y -qq "${PKGS_NEEDED[@]}"
        success "System packages installed."
    else
        info "System packages already present, skipping apt."
    fi
fi

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
    warn ".env not found — our .env is pre-configured for local Ollama."
    cp .env.example .env

    # Overwrite with local Ollama settings
    cat > .env << 'ENVEOF'
# Local Ollama — OpenAI-compatible endpoint
GROQ_API_KEY=ollama
GROQ_URL=http://localhost:11434/v1/chat/completions
GROQ_MODEL=qwen2.5-coder:14b
GROQ_MIN_INTERVAL=0

# Output vault
VAULT_PATH=./vault

# Set to 1 to skip LLM calls and use heuristic fallback
MOCK_GROQ=0
ENVEOF
    success ".env created with local Ollama settings."
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
