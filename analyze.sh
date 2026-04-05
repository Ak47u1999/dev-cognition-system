#!/usr/bin/env bash
# analyze.sh — start Ollama + qwen2.5-coder:14b, run analysis, stop Ollama on exit
# Usage:
#   ./analyze.sh                        # default: external/llama.cpp → ./vault
#   ./analyze.sh --workers 4            # extra args forwarded to batch_pipeline.py
#   ./analyze.sh --no-groq              # offline / mock run
#   ./analyze.sh --repo /path/to/repo   # analyze a different repo

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

MODEL="qwen2.5-coder:14b"
OLLAMA_STARTED_BY_US=0

# ── Cleanup: stop Ollama only if we started it ────────────────────────────────
cleanup() {
    echo ""
    if [ "$OLLAMA_STARTED_BY_US" -eq 1 ]; then
        echo "[analyze] Stopping Ollama service..."
        sudo -n systemctl stop ollama 2>/dev/null || true
        echo "[analyze] Ollama stopped."
    fi
}
trap cleanup EXIT INT TERM

# ── Start Ollama via systemctl if not already running ────────────────────────
if systemctl is-active --quiet ollama; then
    echo "[analyze] Ollama service already running — using existing instance."
else
    echo "[analyze] Starting Ollama service..."
    sudo -n systemctl start ollama
    OLLAMA_STARTED_BY_US=1

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
fi

# ── Verify model is available ─────────────────────────────────────────────────
if ! ollama list 2>/dev/null | grep -q "$MODEL"; then
    echo "[analyze] Model $MODEL not found — pulling now..."
    ollama pull "$MODEL"
fi

# ── Warm up the model (load into VRAM before analysis starts) ─────────────────
echo "[analyze] Loading $MODEL into GPU VRAM..."
curl -sf http://localhost:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d "{\"model\":\"$MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"hi\"}],\"max_tokens\":1}" \
    > /dev/null 2>&1 && echo "[analyze] Model loaded." || echo "[analyze] Warmup skipped."

# ── Monitor Ollama health in background — abort if it dies ───────────────────
SCRIPT_PID=$$
(
    while true; do
        sleep 5
        if ! systemctl is-active --quiet ollama; then
            echo ""
            echo "[analyze] ERROR: Ollama service died unexpectedly. Aborting."
            kill $SCRIPT_PID 2>/dev/null || true
            exit 1
        fi
    done
) &
MONITOR_PID=$!
trap "kill $MONITOR_PID 2>/dev/null; cleanup" EXIT INT TERM

# ── Activate virtualenv if present ───────────────────────────────────────────
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

# ── Run the analysis pipeline ─────────────────────────────────────────────────
echo "[analyze] Starting batch analysis..."
python3 backend/batch_pipeline.py \
    --repo external/llama.cpp \
    --vault ./vault \
    --workers 1 \
    --skip-existing \
    "$@"

echo "[analyze] Analysis complete."
