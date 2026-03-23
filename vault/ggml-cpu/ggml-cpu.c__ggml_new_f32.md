# ggml-cpu.c__ggml_new_f32

Tags: #ggml #memory

```json
{
  "title": "ggml_new_f32",
  "summary": "Creates a new 1D tensor with a single float value.",
  "details": "This function creates a new 1D tensor with a single float value. It first checks if memory allocation is disabled, then creates a new tensor with a single element of type float32. The value is then set for this tensor element.",
  "rationale": "The function is likely implemented this way to provide a simple way to create a tensor with a single value, which can be useful for various applications such as testing or initialization.",
  "performance": "The function has a time complexity of O(1) since it only performs a constant number of operations. However, the performance may be affected by the underlying memory allocation and tensor creation mechanisms.",
  "hidden_insights": [
    "The function uses the `ggml_get_no_alloc` function to check if memory allocation is disabled, which suggests that the library has a mechanism to control memory allocation.",
    "The function uses the `ggml_new_tensor_1d` function to create a new tensor, which implies that the library has a function to create tensors of different dimensions."
  ],
  "where_used": [
    "ggml.c",
    "tensor.c"
  ],
  "tags": [
    "tensor",
    "memory",
    "allocation"
  ],
  "markdown": "### ggml_new_f32
Creates a new 1D tensor with a single float value.
#### Purpose
This function provides a simple way to create a tensor with a single value.
#### Usage
```c
struct ggml_tensor * tensor = ggml_new_f32(ctx, 1.0f);
```
#### Notes
The function checks if memory allocation is disabled before creating the tensor.
"
}
