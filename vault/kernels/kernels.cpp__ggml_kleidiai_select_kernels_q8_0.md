# kernels.cpp__ggml_kleidiai_select_kernels_q8_0

Tags: #ggml #kernel #loop

```json
{
  "title": "Select Kernels",
  "summary": "Selects a kernel based on the provided CPU features.",
  "details": "This function iterates over a list of kernels and returns the first one that matches the given CPU features. The selection is based on the `required_cpu` field of each kernel.",
  "rationale": "The function is implemented this way to provide a simple and efficient way to select a kernel based on the available CPU features.",
  "performance": "The function has a time complexity of O(n), where n is the number of kernels. This is acceptable since the number of kernels is typically small.",
  "hidden_insights": [
    "The function uses a simple loop to iterate over the kernels, which makes it easy to understand and maintain.",
    "The `GGML_UNUSED(features)` macro is used to silence the compiler warning when the `features` parameter is not used in the non-ARM case."
  ],
  "where_used": [
    "ggml_kleidiai_select_kernels_q8_0"
  ],
  "tags": [
    "kernel selection",
    "CPU features",
    "ARM",
    "SIMD"
  ],
  "markdown": "## Select Kernels
### Description
Selects a kernel based on the provided CPU features.
### Details
This function iterates over a list of kernels and returns the first one that matches the given CPU features. The selection is based on the `required_cpu` field of each kernel.
### Performance
The function has a time complexity of O(n), where n is the number of kernels. This is acceptable since the number of kernels is typically small.
### Where Used
* `ggml_kleidiai_select_kernels_q8_0`"
}
