import re
from typing import List, Dict


def _get_function_name(node, source_code: bytes) -> str:
    """Recursively extract function name from a function_definition AST node."""
    def find_identifier(n) -> str:
        if n.type == "identifier":
            return source_code[n.start_byte:n.end_byte].decode("utf-8")
        for child in n.children:
            # Check direct identifier children first
            if child.type == "identifier":
                return source_code[child.start_byte:child.end_byte].decode("utf-8")
            # Recurse into declarator wrappers
            if child.type in ("function_declarator", "pointer_declarator",
                               "reference_declarator", "parenthesized_declarator"):
                result = find_identifier(child)
                if result:
                    return result
        return ""

    for child in node.children:
        if child.type in ("function_declarator", "pointer_declarator",
                           "reference_declarator", "parenthesized_declarator"):
            name = find_identifier(child)
            if name:
                return name
    return ""


def extract_functions(tree, source_code: bytes):
    root = tree.root_node
    functions = []

    def walk(node):
        if node.type == "function_definition":
            start = node.start_byte
            end = node.end_byte
            code = source_code[start:end].decode("utf-8")
            functions.append({
                "code": code,
                "start": start,
                "end": end,
                "name": _get_function_name(node, source_code),
            })
        for child in node.children:
            walk(child)

    walk(root)
    return functions


def extract_functions_from_source_bytes(source_code: bytes, max_functions: int = None):
    """Fallback extractor that uses heuristics to find top-level C/C++ function definitions.
    Returns a list of dicts with keys: code, start, end
    """
    s = source_code.decode("utf-8", errors="replace")
    # remove comments and strings to avoid misleading braces/parens
    s_clean = re.sub(r'/\*.*?\*/', '', s, flags=re.S)
    s_clean = re.sub(r'//.*$', '', s_clean, flags=re.M)
    s_clean = re.sub(r'"(?:\\.|[^"\\])*"', '""', s_clean)
    s_clean = re.sub(r"'(?:\\.|[^'\\])*'", "''", s_clean)

    n = len(s_clean)
    funcs = []
    i = 0
    while i < n and (max_functions is None or len(funcs) < max_functions):
        ch = s_clean[i]
        if ch == '{':
            # compute current depth up to i
            depth = 0
            j = 0
            while j < i:
                if s_clean[j] == '{':
                    depth += 1
                elif s_clean[j] == '}':
                    depth -= 1
                j += 1
            # only consider top-level braces as potential function starts
            if depth == 0:
                pos = i - 1
                while pos >= 0 and s_clean[pos].isspace():
                    pos -= 1
                if pos >= 0 and s_clean[pos] == ')':
                    close_paren_pos = pos
                    pcount = 0
                    k = close_paren_pos
                    open_paren_pos = None
                    while k >= 0:
                        if s_clean[k] == ')':
                            pcount += 1
                        elif s_clean[k] == '(':
                            pcount -= 1
                            if pcount == 0:
                                open_paren_pos = k
                                break
                        k -= 1
                    if open_paren_pos is None:
                        i += 1
                        continue
                    # find name before open_paren_pos
                    m = open_paren_pos - 1
                    while m >= 0 and s_clean[m].isspace():
                        m -= 1
                    name_end = m
                    while m >= 0 and (s_clean[m].isalnum() or s_clean[m] in ('_', ':', '>')):
                        m -= 1
                    name = s_clean[m+1:name_end+1]
                    if name and name not in ('if', 'for', 'while', 'switch', 'return', 'sizeof', 'typedef', 'else', 'struct', 'union', 'enum'):
                        # find function body end by matching braces
                        bcount = 0
                        p = i
                        end_pos = None
                        while p < n:
                            if s_clean[p] == '{':
                                bcount += 1
                            elif s_clean[p] == '}':
                                bcount -= 1
                                if bcount == 0:
                                    end_pos = p
                                    break
                            p += 1
                        if end_pos is None:
                            i += 1
                            continue
                        # determine start position for code capture
                        start_pos = s.rfind('\n', 0, m+1)
                        if start_pos == -1:
                            start_pos = 0
                        else:
                            start_pos += 1
                        code = s[start_pos:end_pos+1]
                        funcs.append({
                            "code": code,
                            "start": start_pos,
                            "end": end_pos+1,
                            "name": name,
                        })
                        i = end_pos + 1
                        continue
        i += 1
    return funcs
