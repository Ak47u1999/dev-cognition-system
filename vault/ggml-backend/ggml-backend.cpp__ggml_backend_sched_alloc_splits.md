# ggml-backend.cpp__ggml_backend_sched_alloc_splits

Tags: #ggml #loop #memory

```json
{
  "title": "ggml_backend_sched_alloc_splits",
  "summary": "Checks if backend IDs have changed and allocates a graph if necessary.",
  "details": "This function iterates over the nodes and leafs in the graph, checking if the backend IDs have changed. If they have, it allocates a new graph. If the allocation fails, it attempts to reserve the graph instead. If the graph is reallocated unexpectedly, it aborts the program.",
  "rationale": "The function is implemented this way to handle cases where the graph needs to be reallocated due to changes in backend IDs. The use of `ggml_gallocr_reserve_n` and `ggml_gallocr_alloc_graph` suggests that the graph is being managed by a custom memory allocator.",
  "performance": "The function has a time complexity of O(n), where n is the number of nodes or leafs in the graph. The use of `ggml_gallocr_reserve_n` and `ggml_gallocr_alloc_graph` may have additional performance implications depending on the underlying memory allocator.",
  "hidden_insights": [
    "The function uses a custom memory allocator (`ggml_gallocr`) to manage the graph.",
    "The use of `ggml_gallocr_reserve_n` and `ggml_gallocr_alloc_graph` suggests that the graph is being reallocated in a way that is not immediately apparent from the code.",
    "The function has a debug mode that checks for unexpected graph reallocations."
  ],
  "where_used": [
    "ggml_backend_sched.c"
  ],
  "tags": [
    "memory allocation",
    "graph management",
    "custom allocator"
  ],
  "markdown": "### ggml_backend_sched_alloc_splits
Checks if backend IDs have changed and allocates a graph if necessary.
#### Details
This function iterates over the nodes and leafs in the graph, checking if the backend IDs have changed. If they have, it allocates a new graph. If the allocation fails, it attempts to reserve the graph instead. If the graph is reallocated unexpectedly, it aborts the program.
#### Rationale
The function is implemented this way to handle cases where the graph needs to be reallocated due to changes in backend IDs. The use of `ggml_gallocr_reserve_n` and `ggml_gallocr_alloc_graph` suggests that the graph is being managed by a custom memory allocator.
#### Performance
The function has a time complexity of O(n), where n is the number of nodes or leafs in the graph. The use of `ggml_gallocr_reserve_n` and `ggml_gallocr_alloc_graph` may have additional performance implications depending on the underlying memory allocator.
#### Hidden Insights
* The function uses a custom memory allocator (`ggml_gallocr`) to manage the graph.
* The use of `ggml_gallocr_reserve_n` and `ggml_gallocr_alloc_graph` suggests that the graph is being reallocated in a way that is not immediately apparent from the code.
* The function has a debug mode that checks for unexpected graph reallocations."
}
