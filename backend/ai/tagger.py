import re
from typing import List


def tag_code(code: str) -> List[str]:
    """Return a list of heuristic tags for a function/body of code."""
    tags = set()
    if not code:
        return []
    low = code.lower()
    if 'ggml' in low or 'ggml_' in low:
        tags.add('ggml')
    if any(k in low for k in ('kernel', 'compute', 'matmul', 'gemm', 'convolution', 'softmax', 'wkv')):
        tags.add('kernel')
    if 'cuda' in low or 'hip' in low:
        tags.add('gpu')
    if 'opencl' in low or 'metal' in low:
        tags.add('accel')
    if 'pthread' in low or 'std::thread' in code:
        tags.add('threading')
    if any(k in low for k in ('malloc', 'calloc', 'realloc', 'free', 'memcpy', 'memmove', 'new', 'delete')):
        tags.add('memory')
    # loops
    if re.search(r"\bfor\b|\bwhile\b", code):
        tags.add('loop')
    # recursion detection
    m = re.search(r"([A-Za-z_][A-Za-z0-9_]*)\s*\(", code)
    if m:
        name = m.group(1)
        brace_pos = code.find('{')
        if brace_pos != -1 and re.search(r"\b" + re.escape(name) + r"\s*\(", code[brace_pos+1:]):
            tags.add('recursion')
    # size heuristics
    if len(code.splitlines()) > 200:
        tags.add('large')
    if len(code.splitlines()) > 50 and 'kernel' in tags:
        tags.add('complex')
    return sorted(tags)
