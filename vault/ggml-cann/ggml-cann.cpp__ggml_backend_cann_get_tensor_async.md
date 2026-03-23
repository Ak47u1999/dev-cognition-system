# ggml-cann.cpp__ggml_backend_cann_get_tensor_async

Tags: #ggml #memory

```json
{
  "title": "ggml_backend_cann_get_tensor_async",
  "summary": "Asynchronously copies a tensor from the device to the host memory.",
  "details": "This function is part of the ggml library and is used to retrieve a tensor from the device memory and copy it to the host memory asynchronously. It takes a backend context, a tensor, and a buffer as input and uses the ACL library to perform the copy operation.",
  "rationale": "The function is implemented this way to allow for asynchronous copying of tensors, which can improve performance by not blocking the execution of other tasks.",
  "performance": "The function uses the ACL library's asynchronous memcpy function, which can improve performance by allowing other tasks to run while the copy operation is in progress.",
  "hidden_insights": [
    "The function checks if the buffer type is supported by the device and if the tensor is not quantized.",
    "The function uses the ACL library's stream API to perform the copy operation asynchronously."
  ],
  "where_used": [
    "ggml_backend_cann_context",
    "ggml_tensor",
    "ggml_backend_buffer_t"
  ],
  "tags": [
    "async",
    "tensor",
    "memcpy",
    "ACL",
    "device",
    "host"
  ],
  "markdown": "### ggml_backend_cann_get_tensor_async
Asynchronously copies a tensor from the device to the host memory.
#### Parameters
* `backend`: The backend context.
* `tensor`: The tensor to copy.
* `data`: The destination buffer.
* `offset`: The offset in the tensor data.
* `size`: The size of the data to copy.
#### Notes
The function checks if the buffer type is supported by the device and if the tensor is not quantized. It uses the ACL library's stream API to perform the copy operation asynchronously."
}
