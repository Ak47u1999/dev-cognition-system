# ggml-cpu.c__ggml_is_numa

Tags: #ggml

```json
{
  "title": "Check for NUMA",
  "summary": "This function checks if the system has multiple NUMA (Non-Uniform Memory Access) nodes.",
  "details": "The function `ggml_is_numa` returns a boolean value indicating whether the system has more than one NUMA node. It does this by checking the `n_nodes` field of the `g_state.numa` structure.",
  "rationale": "The function is likely implemented this way to provide a simple and efficient way to check for NUMA support, without requiring a complex implementation.",
  "performance": "The function has a constant time complexity, making it suitable for performance-critical code paths.",
  "hidden_insights": [
    "The `g_state.numa` structure is likely a global state variable that stores information about the system's NUMA configuration.",
    "The `n_nodes` field is likely an integer that represents the number of NUMA nodes in the system."
  ],
  "where_used": [
    "NUMA-aware memory allocation functions",
    "Performance-critical code paths that require NUMA support"
  ],
  "tags": [
    "NUMA",
    "memory",
    "performance",
    "system configuration"
  ],
  "markdown": "## Check for NUMA\n\nThis function checks if the system has multiple NUMA (Non-Uniform Memory Access) nodes.\n\n### Details\n\nThe function `ggml_is_numa` returns a boolean value indicating whether the system has more than one NUMA node. It does this by checking the `n_nodes` field of the `g_state.numa` structure.\n\n### Rationale\n\nThe function is likely implemented this way to provide a simple and efficient way to check for NUMA support, without requiring a complex implementation.\n\n### Performance\n\nThe function has a constant time complexity, making it suitable for performance-critical code paths.\n\n### Hidden Insights\n\n* The `g_state.numa` structure is likely a global state variable that stores information about the system's NUMA configuration.\n* The `n_nodes` field is likely an integer that represents the number of NUMA nodes in the system.\n\n### Where Used\n\n* NUMA-aware memory allocation functions\n* Performance-critical code paths that require NUMA support\n\n### Tags\n\n* NUMA\n* memory\n* performance\n* system configuration"
}
