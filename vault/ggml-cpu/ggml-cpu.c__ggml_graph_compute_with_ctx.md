# ggml-cpu.c__ggml_graph_compute_with_ctx

Tags: #ggml #kernel #memory

```json
{
  "title": "ggml_graph_compute_with_ctx",
  "summary": "Computes a graph using the provided context and plan.",
  "details": "This function computes a graph using the provided context and plan. It first creates a plan for the graph computation, then allocates a buffer for the work data, and finally calls the graph computation function with the plan.",
  "rationale": "The function may be implemented this way to separate the plan creation and graph computation into two distinct steps, allowing for more flexibility and reusability.",
  "performance": "The performance of this function may be affected by the size of the work buffer and the number of threads used for computation.",
  "hidden_insights": [
    "The `ggml_new_buffer` function is used to allocate a buffer for the work data, which may be a memory-intensive operation.",
    "The `cplan.work_size` field is used to determine the size of the work buffer, which may be a critical performance factor."
  ],
  "where_used": [
    "ggml_graph_compute",
    "ggml_context"
  ],
  "tags": [
    "graph computation",
    "plan creation",
    "buffer allocation"
  ],
  "markdown": "### ggml_graph_compute_with_ctx
Computes a graph using the provided context and plan.
#### Details
This function separates the plan creation and graph computation into two distinct steps, allowing for more flexibility and reusability.
#### Performance Considerations
The performance of this function may be affected by the size of the work buffer and the number of threads used for computation.
#### Non-Obvious Insights
* The `ggml_new_buffer` function is used to allocate a buffer for the work data, which may be a memory-intensive operation.
* The `cplan.work_size` field is used to determine the size of the work buffer, which may be a critical performance factor.
#### Where Used
* `ggml_graph_compute`
* `ggml_context`
#### Tags
* graph computation
* plan creation
* buffer allocation"
}
