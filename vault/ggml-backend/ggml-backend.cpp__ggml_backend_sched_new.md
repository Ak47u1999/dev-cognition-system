# ggml-backend.cpp__ggml_backend_sched_new

Tags: #ggml #loop #memory

```json
{
  "title": "ggml_backend_sched_new",
  "summary": "Creates a new ggml_backend_sched_t instance, initializing its internal data structures and allocating memory for its components.",
  "details": "This function is the constructor for the ggml_backend_sched_t data structure. It takes several parameters, including the number of backends, the buffer type, and the graph size. It initializes the internal data structures, such as the hash set, tensor backend IDs, and node backend IDs, and allocates memory for the context buffer and splits.",
  "rationale": "The function is implemented this way to ensure that the internal data structures are properly initialized and memory is allocated for the context buffer and splits. The use of calloc and malloc ensures that the memory is properly initialized and allocated.",
  "performance": "The function has a time complexity of O(n), where n is the number of backends. The space complexity is also O(n), as it allocates memory for the context buffer and splits.",
  "hidden_insights": [
    "The function uses a hash set to store the tensor backend IDs, which allows for efficient lookup and insertion.",
    "The function allocates memory for the context buffer and splits using calloc and malloc, which ensures that the memory is properly initialized and allocated."
  ],
  "where_used": [
    "ggml_backend_sched.c",
    "ggml_backend.c"
  ],
  "tags": [
    "ggml",
    "backend",
    "sched",
    "constructor",
    "memory allocation"
  ],
  "markdown": "## ggml_backend_sched_new
### Description
Creates a new ggml_backend_sched_t instance, initializing its internal data structures and allocating memory for its components.

### Parameters
* `backends`: The array of backends
* `bufts`: The array of buffer types
* `n_backends`: The number of backends
* `graph_size`: The size of the graph
* `parallel`: Whether to use parallel execution
* `op_offload`: Whether to offload operations

### Returns
A new ggml_backend_sched_t instance

### Notes
The function uses a hash set to store the tensor backend IDs, which allows for efficient lookup and insertion. The function allocates memory for the context buffer and splits using calloc and malloc, which ensures that the memory is properly initialized and allocated."
}
