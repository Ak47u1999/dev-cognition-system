# ggml-hexagon.cpp__ggml_hexagon_supported_ssm_conv

Tags: #ggml #loop

<think>
Okay, let's take a look at this function. The name is ggml_hexagon_supported_ssm_conv, which suggests it's checking if a certain convolution operation is supported by the Hexagon hardware. The function takes a session and an operation tensor as parameters.

First, it checks the types of the source and destination tensors. All must be FP32. If not, returns false. That makes sense because hardware might only support specific data types.

Next, it checks the dimensions. The third dimension (ne[3]) of each tensor must be 1. So, the tensors are effectively 3D. Then it calculates some variables like d_conv, d_inner, n_t, n_s based on the dimensions of the source and destination tensors. These probably represent the convolution depth, inner dimension, number of time steps, and spatial steps.

The function then verifies the shapes of the source and destination tensors against these variables. For example, src0's first dimension should be d_conv - 1 + n_t. This seems to be checking the correct input size for a convolution operation. If any of these checks fail, it returns false.

There's a TODO about non-contiguous tensors. The function checks if all tensors are contiguous. If not, returns false. Contiguous memory is important for hardware acceleration, so this makes sense.

Putting it all together, this function is a validation step to ensure that the given convolution operation meets the requirements for execution on Hexagon. It's part of the backend that decides whether to offload the operation to the hardware or handle it in software.

Performance-wise, checking these conditions upfront avoids runtime errors and ensures efficient execution. The hidden insight is that the function is part of a larger system that routes operations to different accelerators based on their compatibility. The tags would include things like validation, hardware support, etc.
</think>

```json
{
  "title": "Hexagon SSM Conv Support Check",
  "summary": "Validates if a convolution operation meets Hexagon hardware requirements for execution.",
  "details": "This function checks if a convolution operation (op) is compatible with Hexagon hardware by verifying tensor types, dimensions, and contiguity. It ensures all tensors are FP32, confirms 3D tensor shapes, validates dimensional consistency between inputs and outputs, and requires contiguous memory layouts.",
  "rationale": "Hardware accelerators like Hexagon require strict tensor format constraints for efficient execution. This validation prevents runtime errors and ensures optimal performance by rejecting incompatible operations before scheduling.",
  "performance": "Early validation avoids costly hardware dispatch failures. Contiguity checks reduce memory overhead by preventing unnecessary tensor copies.",
  "hidden_insights": [
    "The 'd_conv - 1 + n_t' pattern suggests a causal convolution with kernel size d_conv",
    "The 3D tensor requirement implies temporal/spectral processing (e.g., audio models)",
    "FP32-only support indicates hardware limitations or precision requirements"
  ],
  "where_used": [
    "ggml_hexagon_schedule_op()",
    "ggml_hexagon_graph_compute()",
    "Model loading/compilation pipeline",
    "Quantization conversion modules"
  ],
  "tags": [
    "hardware-validation",
    "tensor-shape-check",
    "FP32-only",
    "contiguity-check",
    "Hexagon",
    "SSM-convolution"
  ],
  "markdown": "## Hexagon SSM Conv Support Check\n\nValidates if a convolution operation meets Hexagon hardware requirements for execution.\n\n### Key Checks:\n- All tensors must be FP32\n- Tensors must be effectively 3D (ne[3] == 1)\n- Input/output dimensional consistency:\n  - src0: (d_conv-1 + n_t) × d_inner × n_s\n  - src1: d_conv × d_inner\n  - dst: d_inner × n_t × n_s\n- All tensors must be contiguous\n\n### Performance Notes:\n- Early validation prevents hardware dispatch failures\n- Contiguity requirement avoids runtime memory copies\n\n### Implementation Details:\n- Uses tensor shape arithmetic to verify convolution parameters\n- TODO: Add non-contiguous tensor support\n\nUsed in hardware scheduling and model compilation pipelines."
}
```
