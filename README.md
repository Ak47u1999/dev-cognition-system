# Dev Cognition System

> **AI-powered C/C++ code intelligence pipeline** — transforms raw source repositories into a richly annotated [Obsidian](https://obsidian.md) knowledge base using [Groq](https://groq.com) LLMs.

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

Dev Cognition System ingests a C/C++ source repository (e.g. [llama.cpp](https://github.com/ggerganov/llama.cpp)), extracts every function, sends each one to a Groq LLM for deep semantic analysis, and writes structured Obsidian markdown notes to a local vault.

**End result:** a searchable, AI-annotated knowledge base of every function in a large codebase — perfect for onboarding, code review, and architectural understanding.

Key capabilities:
- 🔍 **Accurate function extraction** via [Tree-Sitter](https://tree-sitter.github.io) (with regex fallback)
- 🤖 **Deep LLM analysis** — summary, rationale, performance notes, hidden insights, call sites
- 🏷️ **Automatic tagging** — `#memory`, `#gpu`, `#loop`, `#recursion`, `#kernel`, `#threading`, and more
- ⚡ **Concurrent processing** — multi-threaded batch pipeline with configurable workers
- 🔄 **Rate-limit aware** — exponential backoff, up to 6 retries, thread-safe Groq client
- 💾 **Incremental runs** — skip already-analyzed functions with `--skip-existing`
- 🧪 **Offline mode** — `MOCK_GROQ=1` uses heuristic fallback without any API calls

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
                                       │   Groq API      │
                                       │  llama-3.1-8b   │
                                       │  (rate-limited) │
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
├── .env.example              # Environment variable template
├── requirements.txt          # Python dependencies
├── backend/
│   ├── main.py               # Single-file analyzer (entry point)
│   ├── pipeline.py           # Alternative pipeline implementation
│   ├── batch_pipeline.py     # Multi-threaded batch analyzer (main entry point)
│   ├── sample.c              # Sample C file for testing
│   ├── ai/
│   │   ├── groq_client.py    # Groq API client (rate limiting, retries, fallback)
│   │   ├── prompts.py        # LLM prompt templates
│   │   └── tagger.py         # Heuristic code tagger
│   ├── parser/
│   │   ├── parser.py         # Tree-Sitter C parser wrapper
│   │   └── extractor.py      # Function extraction logic
│   └── obsidian/
│       └── writer.py         # Markdown note writer
├── vault/                    # Generated output (gitignored — see below)
└── external/                 # Source repos to analyze (gitignored)
```

---

## Prerequisites

| Requirement | Version | Notes |
|-------------|---------|-------|
| Python | 3.9+ | 3.11 recommended |
| pip | latest | `python -m pip install --upgrade pip` |
| Groq account | — | Free tier: ~30 req/min |

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/dev-cognition-system.git
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

### 4. Get your Groq API key

1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Navigate to **API Keys** → **Create API Key**
4. Copy the key (it starts with `gsk_`)

### 5. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and paste your Groq API key:

```env
GROQ_API_KEY=gsk_your_actual_key_here
```

---

## Configuration

All settings live in `.env`. Copy `.env.example` to get started.

| Variable | Default | Description |
|----------|---------|-------------|
| `GROQ_API_KEY` | *(required)* | Your Groq API key from [console.groq.com](https://console.groq.com) |
| `GROQ_MODEL` | `llama-3.1-8b-instant` | LLM model to use for analysis |
| `GROQ_URL` | `https://api.groq.com/openai/v1/chat/completions` | API endpoint (change for proxy setups) |
| `GROQ_MIN_INTERVAL` | `2.5` | Minimum seconds between API calls (free-tier safe) |
| `VAULT_PATH` | `./vault` | Output directory for generated Obsidian notes |
| `MOCK_GROQ` | `0` | Set to `1` to use heuristic fallback (no API calls) |

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
| `--no-groq` | Save prompts only, skip Groq API calls |
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
| `--no-groq` | — | Use heuristic fallback, skip API |
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
MOCK_GROQ=1 python backend/batch_pipeline.py --repo external/llama.cpp --vault ./vault
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
│   ├── groq_client.py   # Thread-safe Groq client
│   │                    # • Rate limiting (GROQ_MIN_INTERVAL)
│   │                    # • Exponential backoff (up to 6 retries)
│   │                    # • JSON response parsing + error recovery
│   │                    # • Heuristic fallback when API unavailable
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
4. Test with `MOCK_GROQ=1` to avoid API usage during development
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
  --workers 1 \
  --skip-existing
```

> **Tip:** Use `--workers 1` on the free tier. Multiple workers won't help when the rate limiter serialises calls, and concurrent requests risk bursting the quota.

---

### 📺 Terminal output

```
Scanning 178 C files...
Found 8432 functions across 178 files
Vault: ./vault | Workers: 1 | Skip existing: True

[1/8432]    Saved vault/ggml-alloc/ggml-alloc.c__ggml_tallocr_alloc.md
[2/8432]    Saved vault/ggml-alloc/ggml-alloc.c__ggml_dyn_tallocr_new.md
[3/8432]    Saved vault/ggml-alloc/ggml-alloc.c__ggml_vbuffer_alloc.md
...
[429 rate limit] Backing off 10.0s (attempt 2/6)...
[4/8432]    Saved vault/quants/quants.c__ggml_vec_dot_q4_0_q8_0.md
...
Done. 8432 new notes saved to ./vault
```

---

### 🕐 Rate limit guide

The Groq free tier allows **~30 requests/minute**. The `GROQ_MIN_INTERVAL` env var controls the delay between calls.

| `GROQ_MIN_INTERVAL` | Req / min | Req / hr | Time for ~8 400 functions | Safe? |
|:-------------------:|:---------:|:--------:|:-------------------------:|:-----:|
| `2.5s` | 24 | 1 440 | ~6 hrs | ⚠️ Hits limit |
| **`6s` ← default** | **10** | **600** | **~14 hrs** | ✅ Recommended |
| `10s` | 6 | 360 | ~23 hrs | ✅ Very safe |

Set your preferred interval in `.env`:

```env
GROQ_MIN_INTERVAL=6   # 10 req/min — safe overnight run
```

> Run it before you sleep — wake up to a fully annotated codebase. 🌙

---

*Built with [Groq](https://groq.com) · [Tree-Sitter](https://tree-sitter.github.io) · [Obsidian](https://obsidian.md)*
