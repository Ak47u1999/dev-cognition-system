# kleidiai.cpp__kleidiai_collect_q8_chain

Tags: #ggml #kernel

{
  "title": "kleidiai_collect_q8_chain",
  "summary": "Collects a chain of Q8 kernels for kleidiai operations.",
  "details": "This function is responsible for collecting a chain of kernels for kleidiai operations in Q8 format. It starts by retrieving the primary kernel using `kleidiai_primary_kernel_q8` and then uses `kleidiai_collect_kernel_chain_common` to collect the kernel chain. The kernel selection function `ggml_kleidiai_select_kernels_q8_0` is used to determine which kernels to include in the chain.",
  "rationale": "The function is likely implemented this way to separate the kernel collection logic from the kernel selection logic, making it easier to modify or replace the kernel selection function without affecting the rest of the code.",
  "performance": "The performance of this function is likely dependent on the performance of the `kleidiai_collect_kernel_chain_common` function and the `ggml_kleidiai_select_kernels_q8_0` function. The use of a lambda function to select kernels may incur a small performance overhead.",
  "hidden_insights": [
    "The function uses a lambda function to select kernels, which may incur a small performance overhead.",
    "The `kleidiai_collect_kernel_chain_common` function is likely a generic function that can be used to collect kernel chains for different types of operations."
  ],
  "where_used": [
    "kleidiai.cpp"
  ],
  "tags": [
    "kleidiai",
    "q8",
    "kernel chain",
    "cpu features"
  ],
  "markdown": "# kleidiai_collect_q8_chain
Collects a chain of Q8 kernels for kleidiai operations.

## Summary
This function is responsible for collecting a chain of kernels for kleidiai operations in Q8 format.

## Details
The function starts by retrieving the primary kernel using `kleidiai_primary_kernel_q8` and then uses `kleidiai_collect_kernel_chain_common` to collect the kernel chain. The kernel selection function `ggml_kleidiai_select_kernels_q8_0` is used to determine which kernels to include in the chain.

## Rationale
The function is likely implemented this way to separate the kernel collection logic from the kernel selection logic, making it easier to modify or replace the kernel selection function without affecting the rest of the code.

## Performance
The performance of this function is likely dependent on the performance of the `kleidiai_collect_kernel_chain_common` function and the `ggml_kleidiai_select_kernels_q8_0` function. The use of a lambda function to select kernels may incur a small performance overhead."
