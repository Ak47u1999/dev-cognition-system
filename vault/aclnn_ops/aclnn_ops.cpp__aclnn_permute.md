# aclnn_ops.cpp__aclnn_permute

Tags: #ggml #memory

```json
{
  "title": "aclnn_permute Function",
  "summary": "The aclnn_permute function is used to permute the dimensions of an ACL tensor.",
  "details": "This function takes in a ggml_backend_cann_context object, an ACL tensor source, an ACL tensor destination, a new dimension array, and the number of dimensions. It creates an ACL integer array from the new dimension array and then calls the Permute ACLNN operation on the context, source tensor, dimensions, and destination tensor.",
  "rationale": "The function is likely implemented this way to provide a simple interface for permuting tensor dimensions, leveraging the existing ACLNN operation.",
  "performance": "The performance of this function is likely dependent on the underlying ACLNN operation and the size of the tensor being permuted.",
  "hidden_insights": [
    "The function uses a ggml_cann_create_int_array to create an ACL integer array from the new dimension array.",
    "The Permute ACLNN operation is called on the context, source tensor, dimensions, and destination tensor."
  ],
  "where_used": [
    "aclnn_ops.cpp",
    "Other modules that require tensor permutation"
  ],
  "tags": [
    "aclnn",
    "tensor permutation",
    "ggml_backend_cann_context"
  ],
  "markdown": "### aclnn_permute Function
The `aclnn_permute` function is used to permute the dimensions of an ACL tensor.

#### Summary
This function takes in a `ggml_backend_cann_context` object, an ACL tensor source, an ACL tensor destination, a new dimension array, and the number of dimensions. It creates an ACL integer array from the new dimension array and then calls the Permute ACLNN operation on the context, source tensor, dimensions, and destination tensor.

#### Details
The function is likely implemented this way to provide a simple interface for permuting tensor dimensions, leveraging the existing ACLNN operation.

#### Performance
The performance of this function is likely dependent on the underlying ACLNN operation and the size of the tensor being permuted.

#### Hidden Insights
* The function uses a `ggml_cann_create_int_array` to create an ACL integer array from the new dimension array.
* The Permute ACLNN operation is called on the context, source tensor, dimensions, and destination tensor.

#### Where Used
* `aclnn_ops.cpp`
* Other modules that require tensor permutation

#### Tags
* aclnn
* tensor permutation
* `ggml_backend_cann_context`"
}
