# aclnn_ops.cpp__ggml_cann_argmax

Tags: #ggml

```json
{
  "title": "ggml_cann_argmax",
  "summary": "Computes the argmax operation on a tensor using the ACLNN backend.",
  "details": "This function performs the argmax operation on a tensor by creating ACLNN tensors and calling the ArgMax ACLNN operation. The argmax operation returns the indices of the maximum values in each dimension of the input tensor.",
  "rationale": "The function may be implemented this way to leverage the optimized ACLNN operations for performance-critical tasks.",
  "performance": "The performance of this function is likely to be high due to the use of optimized ACLNN operations.",
  "hidden_insights": [
    "The function assumes that the input tensor has at least three dimensions.",
    "The ArgMax operation is called with a dimensionality of 3, which may be a limitation for tensors with more than three dimensions."
  ],
  "where_used": [
    "ggml_backend_cann_context",
    "ggml_tensor"
  ],
  "tags": [
    "argmax",
    "ACLNN",
    "tensor",
    "operation"
  ],
  "markdown": "## ggml_cann_argmax
Computes the argmax operation on a tensor using the ACLNN backend.

### Summary
This function performs the argmax operation on a tensor by creating ACLNN tensors and calling the ArgMax ACLNN operation.

### Details
The argmax operation returns the indices of the maximum values in each dimension of the input tensor.

### Performance
The performance of this function is likely to be high due to the use of optimized ACLNN operations.

### Limitations
The function assumes that the input tensor has at least three dimensions, and the ArgMax operation is called with a dimensionality of 3, which may be a limitation for tensors with more than three dimensions."
}
