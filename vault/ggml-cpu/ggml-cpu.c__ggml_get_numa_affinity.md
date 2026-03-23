# ggml-cpu.c__ggml_get_numa_affinity

Tags: #ggml #threading

```json
{
  "title": "Get NUMA Affinity",
  "summary": "This function retrieves the NUMA (Non-Uniform Memory Access) affinity of the current thread.",
  "details": "The function uses the pthread library to get the affinity of the current thread, which specifies the set of CPUs on which the thread can run. The affinity is stored in a cpu_set_t structure, which is then returned by the function.",
  "rationale": "The function may be implemented this way to allow the caller to determine the NUMA affinity of the current thread, which can be useful for optimizing memory access patterns.",
  "performance": "The performance of this function is likely to be low, as it involves a system call to get the affinity of the current thread.",
  "hidden_insights": [
    "The function uses the pthread library, which is a POSIX thread library.",
    "The cpu_set_t structure is used to represent the set of CPUs on which the thread can run."
  ],
  "where_used": [
    "ggml-cpu.c",
    "Other modules that require NUMA affinity information"
  ],
  "tags": [
    "NUMA",
    "Affinity",
    "Thread",
    "POSIX",
    "System Call"
  ],
  "markdown": "### Get NUMA Affinity\n\nThis function retrieves the NUMA affinity of the current thread.\n\n#### Details\n\nThe function uses the pthread library to get the affinity of the current thread, which specifies the set of CPUs on which the thread can run. The affinity is stored in a cpu_set_t structure, which is then returned by the function.\n\n#### Rationale\n\nThe function may be implemented this way to allow the caller to determine the NUMA affinity of the current thread, which can be useful for optimizing memory access patterns.\n\n#### Performance\n\nThe performance of this function is likely to be low, as it involves a system call to get the affinity of the current thread.\n\n#### Hidden Insights\n\n* The function uses the pthread library, which is a POSIX thread library.\n* The cpu_set_t structure is used to represent the set of CPUs on which the thread can run.\n\n#### Where Used\n\n* ggml-cpu.c\n* Other modules that require NUMA affinity information\n\n#### Tags\n\n* NUMA\n* Affinity\n* Thread\n* POSIX\n* System Call"
}
