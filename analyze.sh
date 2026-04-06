#!/usr/bin/env bash
# analyze.sh — restart Ollama fresh, load model from .env, run analysis, stop Ollama on exit
# Usage:
#   ./analyze.sh                        # default: external/llama.cpp → ./vault
#   ./analyze.sh --no-llm               # offline / mock run
#   ./analyze.sh --repo /path/to/repo   # analyze a different repo

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# ── Load .env so OLLAMA_MODEL and other vars are available in this shell ──────
if [ -f ".env" ]; then
    set -a
    # shellcheck source=.env
    source .env
    set +a
fi
MODEL="${OLLAMA_MODEL:-qwen2.5-coder:14b}"

# ── Cleanup: always stop Ollama on exit ──────────────────────────────────────
cleanup() {
    echo ""
    echo "[analyze] Stopping Ollama service..."
    sudo -n systemctl stop ollama 2>/dev/null || true
    echo "[analyze] Ollama stopped."
}
trap cleanup EXIT INT TERM

# ── Always restart Ollama for a clean state (avoids port timeout issues) ─────
echo "[analyze] Restarting Ollama service..."
sudo -n systemctl stop ollama 2>/dev/null || true
sleep 2
# Inject keep-alive so model stays in VRAM during long file scans
sudo -n systemctl set-environment OLLAMA_KEEP_ALIVE="${OLLAMA_KEEP_ALIVE:--1}"
sudo -n systemctl start ollama

# Wait for API to be ready (up to 30s)
echo -n "[analyze] Waiting for Ollama API"
for i in $(seq 1 30); do
    if curl -sf http://localhost:11434/ > /dev/null 2>&1; then
        echo " ready."
        break
    fi
    echo -n "."
    sleep 1
    if [ "$i" -eq 30 ]; then
        echo ""
        echo "[analyze] ERROR: Ollama did not start in 30s. Check: journalctl -u ollama -n 20"
        exit 1
    fi
done

# ── Verify model is available ─────────────────────────────────────────────────
if ! ollama list 2>/dev/null | grep -q "$MODEL"; then
    echo "[analyze] Model $MODEL not found — pulling now..."
    ollama pull "$MODEL"
fi

# ── Warm up the model (load into VRAM before analysis starts) ─────────────────
echo "[analyze] Loading $MODEL into GPU VRAM..."
curl -sf http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"$MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"hi\"}],\"max_tokens\":1,\"keep_alive\":-1}" \
    > /dev/null 2>&1 && echo "[analyze] Model loaded." || echo "[analyze] Warmup skipped."

# ── Activate virtualenv if present ───────────────────────────────────────────
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

# ── Run the analysis pipeline ─────────────────────────────────────────────────
echo "[analyze] Starting batch analysis..."
python3 backend/batch_pipeline.py \
    --repo external/llama.cpp \
    --vault ./vault \
    --skip-existing \
    "$@"

echo "[analyze] Analysis complete."
