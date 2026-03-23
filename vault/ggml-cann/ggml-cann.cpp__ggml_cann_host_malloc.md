# ggml-cann.cpp__ggml_cann_host_malloc

Tags: #ggml #memory

```json
{
  "title": "ggml_cann_host_malloc",
  "summary": "Allocates pinned memory on the host using the CUDA Runtime API.",
  "details": "This function allocates a block of pinned memory on the host using the CUDA Runtime API's aclrtMallocHost. The allocated memory is pinned, meaning it is mapped to a specific physical address, which can improve performance in certain scenarios. The function takes a size parameter, which is rounded up to the nearest multiple of the specified alignment (128 bytes in this case).",
  "rationale": "Pinned memory is used to improve performance in scenarios where the host and device have a high bandwidth connection, such as in deep learning workloads. The use of pinned memory allows for faster data transfer between the host and device.",
  "performance": "The use of pinned memory can improve performance in certain scenarios, but it also increases memory usage. The function also logs a warning if the allocation fails, which can be useful for debugging purposes.",
  "hidden_insights": [
    "The function uses the GGML_PAD macro to round up the size parameter to the nearest multiple of the alignment.",
    "The function checks if the environment variable GGML_CANN_NO_PINNED is set, and if so, returns nullptr."
  ],
  "where_used": [
    "ggml-cann.cpp"
  ],
  "tags": [
    "cuda",
    "pinned memory",
    "host memory",
    "allocation"
  ],
  "markdown": "## ggml_cann_host_malloc\nAllocates pinned memory on the host using the CUDA Runtime API.\n\n### Purpose\nThis function is used to allocate a block of pinned memory on the host, which can improve performance in certain scenarios.\n\n### Parameters\n* `size`: The size of the memory block to allocate.\n\n### Return Value\nThe function returns a pointer to the allocated memory block, or nullptr if the allocation fails.\n\n### Notes\nThe function uses the GGML_PAD macro to round up the size parameter to the nearest multiple of the alignment. The function also checks if the environment variable GGML_CANN_NO_PINNED is set, and if so, returns nullptr."
}
