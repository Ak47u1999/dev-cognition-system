# sampling.cpp__common_perf_print

Tags: #ggml

```json
{
  "title": "common_perf_print",
  "summary": "Prints performance metrics for a given context and sampler.",
  "details": "This function prints performance metrics for a given context and sampler. It measures the sampling time, sampler time, load time, prompt evaluation time, evaluation time, and total time. It also calculates the unaccounted time and the number of graphs reused.",
  "rationale": "The function is implemented this way to provide a clear and concise way to print performance metrics. It uses a TODO comment to indicate that grammar performance measurement is not yet implemented.",
  "performance": "The function has a time complexity of O(1) since it only performs a constant number of operations. However, the llama_perf_sampler and llama_perf_context functions may have a higher time complexity.",
  "hidden_insights": [
    "The sampling time includes the sampler's time and extra time spent in common/sampling.",
    "The unaccounted time is calculated by subtracting the sampling time, prompt evaluation time, and evaluation time from the total time."
  ],
  "where_used": [
    "likely called from llama_perf_sampler and llama_perf_context functions"
  ],
  "tags": [
    "performance",
    "metrics",
    "sampling",
    "evaluation"
  ],
  "markdown": "## common_perf_print
Prints performance metrics for a given context and sampler.

### Performance Metrics
* Sampling time
* Sampler time
* Load time
* Prompt evaluation time
* Evaluation time
* Total time
* Unaccounted time
* Number of graphs reused

### Notes
* The sampling time includes the sampler's time and extra time spent in common/sampling.
* The unaccounted time is calculated by subtracting the sampling time, prompt evaluation time, and evaluation time from the total time."
}
```
