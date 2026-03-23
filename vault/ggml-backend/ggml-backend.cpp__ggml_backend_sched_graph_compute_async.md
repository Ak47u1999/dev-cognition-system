# ggml-backend.cpp__ggml_backend_sched_graph_compute_async

Tags: #ggml #kernel

{
  "title": "ggml_backend_sched_graph_compute_async",
  "summary": "Computes the graph asynchronously using the given schedule.",
  "details": "This function is responsible for computing the graph asynchronously using the provided schedule. It first checks if the schedule is not reset and not allocated, and if so, resets it. Then, it checks if the schedule is not allocated, and if so, allocates the graph. Finally, it computes the splits in the schedule.",
  "rationale": "The function is implemented this way to ensure that the schedule is properly reset and allocated before computing the graph. This is likely done to prevent unexpected behavior or errors.",
  "performance": "The performance of this function is likely to be good, as it only performs a few checks and allocations before computing the splits. However, the actual performance will depend on the implementation of the `ggml_backend_sched_compute_splits` function.",
  "hidden_insights": [
    "The function uses a flag to check if the schedule is reset, which suggests that the schedule can be reset multiple times.",
    "The function uses a separate function to allocate the graph, which suggests that graph allocation is a complex process."
  ],
  "where_used": [
    "ggml_backend_sched_graph_compute_async is likely called from the main graph computation loop.",
    "It may also be called from other functions that require asynchronous graph computation."
  ],
  "tags": [
    "async",
    "graph",
    "schedule",
    "allocation"
  ],
  "markdown": "### ggml_backend_sched_graph_compute_async
Computes the graph asynchronously using the given schedule.
#### Purpose
This function is responsible for computing the graph asynchronously using the provided schedule.
#### Details
* Checks if the schedule is not reset and not allocated, and if so, resets it.
* Checks if the schedule is not allocated, and if so, allocates the graph.
* Computes the splits in the schedule.
#### Rationale
The function is implemented this way to ensure that the schedule is properly reset and allocated before computing the graph.
#### Performance
The performance of this function is likely to be good, as it only performs a few checks and allocations before computing the splits.
#### Where Used
* Main graph computation loop
* Other functions that require asynchronous graph computation"
