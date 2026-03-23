# aclnn_ops.cpp__ggml_cann_repeat

Tags: #ggml

```json
{
  "title": "ggml_cann_repeat",
  "summary": "Repeats a tensor in the specified dimensions.",
  "details": "This function repeats a tensor in the specified dimensions by creating ACL tensors and calling the aclnn_repeat function. It first checks if the tensor can be repeated using the ggml_can_repeat function.",
  "rationale": "The function may be implemented this way to leverage the aclnn_repeat function, which is likely optimized for performance.",
  "performance": "The performance of this function is likely dependent on the aclnn_repeat function and the size of the tensors.",
  "hidden_insights": [
    "The repeatsArray is calculated by dividing the corresponding dimensions of the destination tensor by the source tensor.",
    "The ggml_can_repeat function is used to check if the tensor can be repeated."
  ],
  "where_used": [
    "ggml_backend_cann_context",
    "ggml_tensor"
  ],
  "tags": [
    "tensor",
    "repeating",
    "acl",
    "cann"
  ],
  "markdown": "### ggml_cann_repeat
Repeats a tensor in the specified dimensions.
#### Details
This function repeats a tensor in the specified dimensions by creating ACL tensors and calling the aclnn_repeat function. It first checks if the tensor can be repeated using the ggml_can_repeat function.
#### Performance
The performance of this function is likely dependent on the aclnn_repeat function and the size of the tensors.
#### Notes
* The repeatsArray is calculated by dividing the corresponding dimensions of the destination tensor by the source tensor.
* The ggml_can_repeat function is used to check if the tensor can be repeated."
}
