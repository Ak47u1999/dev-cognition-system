# ggml-cann.cpp__ggml_cann_can_fuse

Tags: #ggml #loop

```json
{
  "title": "ggml_cann_can_fuse",
  "summary": "Checks if the CANN backend can fuse operations in a graph.",
  "details": "This function determines whether the CANN backend can fuse operations in a graph. It first checks if the operations can be fused in general using the `ggml_can_fuse` function. If they can, it then checks if the specific operations ADD and RMS_NORM can be fused, which requires that the input tensors have the same shape.",
  "rationale": "The function is implemented this way to provide a specific check for the CANN backend, which has its own requirements for fusing operations.",
  "performance": "The function has a time complexity of O(1) if the operations can be fused, and O(n) otherwise, where n is the number of operations.",
  "hidden_insights": [
    "The function assumes that the input graph is valid and that the operations are correctly represented.",
    "The function does not handle the case where the input tensors have different shapes but can be broadcasted to the same shape."
  ],
  "where_used": [
    "ggml_cann.cpp"
  ],
  "tags": [
    "CANN",
    "graph fusion",
    "tensor operations"
  ],
  "markdown": "## ggml_cann_can_fuse
Checks if the CANN backend can fuse operations in a graph.
### Purpose
This function determines whether the CANN backend can fuse operations in a graph.
### Details
It first checks if the operations can be fused in general using the `ggml_can_fuse` function. If they can, it then checks if the specific operations ADD and RMS_NORM can be fused, which requires that the input tensors have the same shape.
### Rationale
The function is implemented this way to provide a specific check for the CANN backend, which has its own requirements for fusing operations.
### Performance
The function has a time complexity of O(1) if the operations can be fused, and O(n) otherwise, where n is the number of operations.
### Hidden Insights
* The function assumes that the input graph is valid and that the operations are correctly represented.
* The function does not handle the case where the input tensors have different shapes but can be broadcasted to the same shape.
### Where Used
* `ggml_cann.cpp`
### Tags
* CANN
* graph fusion
* tensor operations"
}
