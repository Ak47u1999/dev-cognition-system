# ggml-alloc.c__ggml_backend_alloc_ctx_tensors_from_buft

Tags: #ggml

{
  "title": "ggml_backend_alloc_ctx_tensors_from_buft",
  "summary": "Allocates context tensors from a buffer type.",
  "details": "This function allocates context tensors from a given buffer type. It calls the implementation function `ggml_backend_alloc_ctx_tensors_from_buft_impl` with the provided context, buffer type, and a pointer to the total allocated bytes.",
  "rationale": "The function is likely implemented this way to encapsulate the allocation logic and provide a simpler interface for users.",
  "performance": "The performance of this function is likely dependent on the implementation of `ggml_backend_alloc_ctx_tensors_from_buft_impl`.",
  "hidden_insights": [
    "The `no_alloc` parameter is set to `false`, indicating that actual allocation will occur."
  ],
  "where_used": [
    "ggml_backend_alloc_ctx_tensors_from_buft_impl"
  ],
  "tags": [
    "memory allocation",
    "context tensors",
    "buffer type"
  ],
  "markdown": "### ggml_backend_alloc_ctx_tensors_from_buft\n\nAllocates context tensors from a buffer type.\n\n#### Parameters\n\n* `ctx`: The context to allocate tensors for.\n* `buft`: The buffer type to allocate from.\n\n#### Returns\n\nThe allocated context tensors.\n\n#### Notes\n\nThis function calls the implementation function `ggml_backend_alloc_ctx_tensors_from_buft_impl` with the provided context, buffer type, and a pointer to the total allocated bytes."
