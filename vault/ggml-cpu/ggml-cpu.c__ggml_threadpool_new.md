# ggml-cpu.c__ggml_threadpool_new

Tags: #ggml #memory

```json
{
  "title": "ggml_threadpool_new",
  "summary": "Creates a new thread pool instance based on the provided parameters.",
  "details": "This function initializes a new thread pool using the given parameters. It calls the internal implementation function `ggml_threadpool_new_impl` to perform the actual creation.",
  "rationale": "The function is likely implemented this way to encapsulate the creation logic and provide a simpler interface for users.",
  "performance": "The performance impact of this function is minimal, as it only involves a function call and does not perform any significant computations.",
  "hidden_insights": [
    "The `ggml_threadpool_new_impl` function is not shown in this snippet, but it likely performs the actual creation of the thread pool instance.",
    "The `NULL` arguments passed to `ggml_threadpool_new_impl` suggest that some default values or behaviors are used for unspecified parameters."
  ],
  "where_used": [
    "ggml_threadpool.c",
    "main.c"
  ],
  "tags": [
    "thread pool",
    "creation",
    "initialization"
  ],
  "markdown": "## ggml_threadpool_new
Creates a new thread pool instance based on the provided parameters.
### Details
This function initializes a new thread pool using the given parameters. It calls the internal implementation function `ggml_threadpool_new_impl` to perform the actual creation.
### Performance
The performance impact of this function is minimal, as it only involves a function call and does not perform any significant computations.
### Where Used
* `ggml_threadpool.c`
* `main.c`"
}
