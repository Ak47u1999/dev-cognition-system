# Dev Cognition System

> **AI-powered C/C++ code intelligence pipeline** — transforms raw source repositories into a richly annotated [Obsidian](https://obsidian.md) knowledge base using local [Ollama](https://ollama.com) LLMs.

---

## Table of Contents

- [What It Does](#what-it-does)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Output — The Achievement Vault](#output--the-achievement-vault)
- [Architecture](#architecture)
- [Contributing](#contributing)

---

## What It Does

Dev Cognition System ingests a C/C++ source repository (e.g. [llama.cpp](https://github.com/ggerganov/llama.cpp)), extracts every function, sends each one to a local Ollama LLM for deep semantic analysis, and writes structured Obsidian markdown notes to a local vault.

**End result:** a searchable, AI-annotated knowledge base of every function in a large codebase — perfect for onboarding, code review, and architectural understanding. Runs entirely offline — no API keys or cloud accounts required.

Key capabilities:
- 🔍 **Accurate function extraction** via [Tree-Sitter](https://tree-sitter.github.io) (with regex fallback)
- 🤖 **Deep LLM analysis** — summary, rationale, performance notes, hidden insights, call sites
- 🏷️ **Automatic tagging** — `#memory`, `#gpu`, `#loop`, `#recursion`, `#kernel`, `#threading`, and more
- ⚡ **Concurrent processing** — multi-threaded batch pipeline with configurable workers
- 🔒 **Fully local** — all inference via [Ollama](https://ollama.com), no data leaves your machine
- 💾 **Incremental runs** — skip already-analyzed functions with `--skip-existing`
- 🧪 **Offline mode** — `MOCK_LLM=1` uses heuristic fallback without any LLM calls

---

## How It Works

```
C/C++ Source Repo
       │
       ▼
 ┌─────────────┐     Tree-Sitter       ┌─────────────────┐
 │  Discovery  │ ──── parser ────────► │ Function List   │
 │ (find *.c)  │    + regex fallback   │ {name, code,    │
 └─────────────┘                       │  start, end}    │
                                       └────────┬────────┘
                                                │
                                                ▼
                                       ┌─────────────────┐
                                       │  Heuristic      │
                                       │  Tagger         │
                                       │  (#ggml, #gpu…) │
                                       └────────┬────────┘
                                                │
                                                ▼
                                       ┌─────────────────┐
                                       │  Prompt Builder │
                                       │  (prompts.py)   │
                                       └────────┬────────┘
                                                │
                                                ▼
                                       ┌─────────────────┐
                                       │   Ollama API    │
                                       │ qwen2.5-coder   │
                                       │  (local, fast)  │
                                       └────────┬────────┘
                                                │  JSON response
                                                ▼
                                       ┌─────────────────┐
                                       │  Markdown Note  │◄── fallback if API fails
                                       │  Writer         │
                                       └────────┬────────┘
                                                │
                                                ▼
                              vault/{group}/{file}__{function}.md
```

---

## Project Structure

```
dev-cognition-system/
├── init.sh                   # ★ Start here — apt bootstrap, venv setup, then calls analyze.sh
├── analyze.sh                # Activates venv and launches batch_pipeline.py
├── .env.example              # Environment variable template (copy to .env)
├── requirements.txt          # Python dependencies
├── backend/
│   ├── batch_pipeline.py     # Multi-threaded batch analyzer (called by analyze.sh)
│   ├── pipeline.py           # Single-file pipeline (for manual/dev use)
│   ├── main.py               # Minimal single-file entry point (dev/testing)
│   ├── sample.c              # Sample C file for testing the parser
│   ├── ai/
│   │   ├── ollama_client.py  # Ollama local inference client (retries, fallback)
│   │   ├── prompts.py        # LLM prompt templates
│   │   └── tagger.py         # Heuristic code tagger
│   ├── parser/
│   │   ├── parser.py         # Tree-Sitter C/C++ parser wrapper
│   │   └── extractor.py      # Function extraction logic
│   ├── obsidian/
│   │   └── writer.py         # Markdown note writer
│   ├── api/                  # (planned) REST API layer
│   ├── chunker/              # (planned) semantic chunking module
│   ├── graph/                # (planned) call-graph analysis
│   └── build/                # (planned) build-system integration
├── vault/                    # Generated output (gitignored — see below)
└── external/                 # Source repos to analyze (gitignored)
```

---

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.9+ | 3.11 recommended |
| pip | latest | `python -m pip install --upgrade pip` |
| [Ollama](https://ollama.com) | latest | Runs models locally — install from [ollama.com](https://ollama.com) |
| GPU (optional) | — | NVIDIA/AMD GPU accelerates inference; CPU-only works too |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ak47u1999/dev-cognition-system.git
cd dev-cognition-system
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and start Ollama

1. Install Ollama from [https://ollama.com](https://ollama.com)
2. Pull the default model:

```bash
ollama pull qwen2.5-coder:14b
```

3. Ollama starts automatically as a service. Verify it's running:

```bash
curl http://localhost:11434/
```

### 5. Configure environment variables

```bash
cp .env.example .env
```

The defaults in `.env.example` work out of the box for a local Ollama setup — no changes required unless you want a different model or vault path.

---

## Configuration

All settings live in `.env`. Copy `.env.example` to get started.

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_URL` | `http://localhost:11434/v1/chat/completions` | Ollama OpenAI-compatible endpoint |
| `OLLAMA_MODEL` | `qwen2.5-coder:14b` | Model to use (must be pulled via `ollama pull`) |
| `OLLAMA_MIN_INTERVAL` | `0` | Minimum seconds between calls (0 = no throttle for local) |
| `OLLAMA_KEEP_ALIVE` | `-1` | Keep model in VRAM indefinitely (`-1` = never unload) |
| `VAULT_PATH` | `./vault` | Output directory for generated Obsidian notes |
| `MOCK_LLM` | `0` | Set to `1` to use heuristic fallback (no LLM calls) |

---

## Usage

### Analyze a single C file

```bash
python backend/main.py --source backend/sample.c --vault ./vault
```

**Options:**

| Flag | Description |
|------|-------------|
| `--source <file>` | Path to the `.c` file to analyze |
| `--vault <dir>` | Output vault directory (default: `./vault`) |
| `--no-groq` | Save prompts only, skip LLM calls |
| `--max <n>` | Limit to first N functions |
| `--skip-existing` | Skip functions that already have notes |

### Batch analyze an entire repository ⭐ Recommended

```bash
python backend/batch_pipeline.py \
  --repo external/llama.cpp \
  --vault ./vault \
  --workers 5 \
  --skip-existing
```

**Options:**

| Flag | Default | Description |
|------|---------|-------------|
| `--repo <dir>` | *(required)* | Root of the C/C++ repository to analyze |
| `--vault <dir>` | `./vault` | Output vault directory |
| `--workers <n>` | `5` | Number of concurrent worker threads |
| `--no-groq` | — | Use heuristic fallback, skip LLM |
| `--skip-existing` | — | Skip already-analyzed functions |

**Example output:**

```
Scanning 178 C files...
Found 8,432 functions across 178 files
Vault: ./vault | Workers: 5 | Skip existing: True

[1/8432] Saved vault/ggml-alloc/ggml-alloc.c__ggml_tallocr_alloc.md
[2/8432] Saved vault/ggml-alloc/ggml-alloc.c__ggml_dyn_tallocr_new.md
...
Done. 2,145 new notes saved to ./vault
```

### Test with offline/mock mode

```bash
MOCK_LLM=1 python backend/batch_pipeline.py --repo external/llama.cpp --vault ./vault
```

---

## Output — The Achievement Vault

The pipeline writes Obsidian-compatible markdown notes to `./vault/`. Each note is one analyzed function.

### File naming convention

```
vault/
└── {source-file-stem}/
    └── {source-file}__{function-name}.md
```

Example:
```
vault/
└── ggml-alloc/
    ├── ggml-alloc.c__ggml_tallocr_alloc.md
    ├── ggml-alloc.c__ggml_dyn_tallocr_new.md
    └── ggml-alloc.c__ggml_dyn_tallocr_alloc.md
```

### Note structure

Each note contains:

```markdown
# ggml-alloc.c__ggml_tallocr_alloc

Tags: #ggml #memory

## ggml_tallocr_alloc Function

### Summary
Allocates memory for a tensor within a buffer, ensuring proper alignment
and bounds checking.

### Details
This function is part of the ggml library, responsible for memory
management of tensor allocations. It uses GGML_PAD to align addresses
to the required boundary before committing the allocation.

### Rationale
Designed for high-performance inference where allocation overhead must
be minimal and predictable.

### Performance
O(1) time complexity. No heap allocation — operates directly on a
pre-allocated buffer.

### Hidden Insights
- Uses `GGML_PAD` macro to guarantee alignment for SIMD operations
- The `assert` verifies alignment post-allocation, not just pre-check
- Compatible with both CPU and GPU backend buffer layouts

### Where Used
- `ggml_backend_alloc_ctx_tensors`
- `ggml_gallocr_alloc_graph`
```

### Automatic tags applied

| Tag | Triggered when code contains |
|-----|------------------------------|
| `#ggml` | `ggml_` prefix |
| `#memory` | `malloc`, `free`, `alloc`, `mmap` |
| `#loop` | `for`, `while` |
| `#recursion` | Self-referencing function call |
| `#gpu` | `cuda`, `metal`, `opencl`, `vulkan` |
| `#kernel` | `__global__`, `__kernel__` |
| `#threading` | `pthread`, `mutex`, `thread` |
| `#accel` | `avx`, `neon`, `simd` |
| `#large` | Function > 100 lines |
| `#complex` | Function > 200 lines |

### Opening in Obsidian

1. Open Obsidian → **Open folder as vault**
2. Select the `./vault` directory
3. Use **Graph View** to explore function relationships via shared tags
4. Use **Search** (`Ctrl+Shift+F`) to find functions by tag, concept, or keyword

---

## Architecture

```
backend/
├── ai/
│   ├── ollama_client.py # Local Ollama inference client
│   │                    # • OpenAI-compatible HTTP API
│   │                    # • Connection retries (up to 3 attempts)
│   │                    # • JSON response parsing + error recovery
│   │                    # • Heuristic fallback when Ollama unavailable
│   ├── prompts.py       # Prompt templates for LLM
│   └── tagger.py        # Regex-based heuristic tagger
├── parser/
│   ├── parser.py        # Tree-Sitter C language parser
│   └── extractor.py     # Function boundary extraction
│                        # • Primary: Tree-Sitter AST walk
│                        # • Fallback: brace-counting regex
└── obsidian/
    └── writer.py        # Writes .md files to vault
```

---

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Install dev dependencies and make your changes
4. Test with `MOCK_LLM=1` to run fully offline during development
5. Submit a pull request

---

## ⚡ Running the Pipeline — Commands & Expected Output

### Quick test (single file)

```bash
cd dev-cognition-system
source venv/bin/activate   # Windows: venv\Scripts\activate

python backend/main.py \
  --source backend/sample.c \
  --vault ./vault \
  --skip-existing
```

### Full batch run (entire repository)

```bash
python backend/batch_pipeline.py \
  --repo external/llama.cpp \
  --vault ./vault \
  --workers 5 \
  --skip-existing
```

> **Tip:** With local Ollama you can use multiple workers freely — there's no cloud rate limit. Tune `--workers` to match your GPU throughput.

---

### 📺 Terminal output

```
Scanning 178 C files...
Found 8432 functions across 178 files
Vault: ./vault | Workers: 5 | Skip existing: True

[1/8432]    Saved vault/ggml-alloc/ggml-alloc.c__ggml_tallocr_alloc.md
[2/8432]    Saved vault/ggml-alloc/ggml-alloc.c__ggml_dyn_tallocr_new.md
[3/8432]    Saved vault/ggml-alloc/ggml-alloc.c__ggml_vbuffer_alloc.md
...
Done. 8432 new notes saved to ./vault
```

---

### 🚀 Performance guide

Speed depends on your hardware. Ollama runs `qwen2.5-coder:14b` fully locally with no cloud rate limits.

| Hardware | Approx tokens/s | Time for ~8 400 functions |
|----------|:---------------:|:-------------------------:|
| RTX 4090 (24 GB) | ~80–120 | ~2–3 hrs |
| RTX 3080 (10 GB) | ~30–50 | ~5–8 hrs |
| Apple M2 Pro | ~20–35 | ~8–12 hrs |
| CPU only | ~5–10 | ~24–48 hrs |

> **Tip:** Use `--workers 5` (or more) on GPU — local inference parallelises well. For CPU-only, stick to `--workers 1` to avoid memory pressure.

> Run it before you sleep — wake up to a fully annotated codebase. 🌙

---

*Built with [Ollama](https://ollama.com) · [Tree-Sitter](https://tree-sitter.github.io) · [Obsidian](https://obsidian.md)*
