# aclnn_ops.cpp__cann_copy

Tags: #ggml

# aclnn_copy
Copies the contents of one ACL tensor to another.

## Details
This function performs an inplace copy of the contents of the source ACL tensor (`acl_src`) to the destination ACL tensor (`acl_dst`). It uses the `GGML_CANN_CALL_ACLNN_OP` macro to call the `InplaceCopy` operation on the CANN context.

## Performance
The inplace copy operation is likely to be efficient as it avoids the need to allocate new memory for the destination tensor.

## Where Used
* `aclnn_ops.cpp`
