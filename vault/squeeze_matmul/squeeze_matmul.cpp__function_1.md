# squeeze_matmul.cpp__function_1

Tags: #ggml #kernel #memory #recursion

<think>
Okay, let's take a look at this code. The function is called SqueezeMatmul, and it's part of the OpenVINO framework, specifically in the GGML frontend pass. The comment mentions that it's for quantized models where NPUW expects a 3D activation in DQ optimization, like DQMatMulGQ2i.

So, the main purpose here is to modify the MatMul operation by adding Squeeze and Unsqueeze operations. The code uses a pattern matcher to find MatMul nodes where the activation has a rank of 4 and the weights have a rank of 2. When that's the case, it inserts a Squeeze on the activation along axis 0, performs the MatMul, and then an Unsqueeze to restore the shape. This is probably to adjust the dimensions to fit the expected input for the quantized model on the NPU.

The rationale might be to handle the dimensionality changes required by the hardware or specific optimizations. By squeezing and then unsqueezing, they can manipulate the tensor shapes without changing the actual data, which is necessary for compatibility with certain hardware accelerators.

Performance considerations would include the overhead of adding these operations. However, since Squeeze and Unsqueeze are typically low-cost operations, the impact might be minimal. The code checks for dynamic ranks and skips if they're not static, which is important for avoiding errors in dynamic shapes.

Hidden insights could be that this pass is specific to certain quantization formats, maybe GQ2i, and that it's part of a larger optimization pipeline. Also, the use of copy_runtime_info ensures that the new nodes inherit the original's runtime information, preserving any optimizations or metadata.

As for where this is used, it's likely in the frontend conversion process when dealing with GGML models, especially those that are quantized and target NPUs. The tags would include things like OpenVINO, optimization, quantization, etc.

Putting this all together into the JSON structure with the required keys. Need to make sure the markdown is formatted correctly without code fences and that all the keys are present. Also, check that the JSON is valid and the summary and details clearly explain the function's purpose and implementation.
</think>

{
  "title": "SqueezeMatmul Optimization Pass",
  "summary": "This OpenVINO pass modifies MatMul operations in quantized models by inserting Squeeze/Unsqueeze operations to adjust tensor dimensions for NPU compatibility.",
  "details": "The pass identifies MatMul patterns with 4D activation tensors and 2D weight tensors. It inserts a Squeeze operation on the activation tensor along axis 0 before MatMul, then adds an Unsqueeze operation on the output to restore original dimensions. This transforms 4D→2D→3D→4D tensor flow to meet NPU requirements for Dynamic Quantization (DQ) optimizations like DQMatMulGQ2i.",
  "rationale": "Quantized models for NPUs often require specific tensor shapes. Squeezing/Unsqueezing allows dimensionality manipulation without data copying, maintaining numerical precision while adapting to hardware constraints. The pattern matching ensures this only applies to static-shape tensors to avoid runtime errors.",
  "performance": "Minimal overhead from Squeeze/Unsqueeze operations (O(1) computation). Avoids unnecessary data duplication. Static shape checks prevent runtime failures in dynamic scenarios.",
  "hidden_insights": [
    "Specifically targets GQ2i quantization format based on context",
    "Preserves original node's runtime information via copy_runtime_info",
    "Axis 0 selection implies batch/channel dimension manipulation",
    "Only applies to 4D→2D MatMul patterns (common in CNNs)",
    "Implies NPU expects 3D intermediate tensors for quantization"
  ],
  "where_used": [
    "GGML frontend conversion pipeline",
    "Quantized model optimization workflows",
    "NPU-specific model compilation",
    "Dynamic Quantization (DQ) optimization passes",
    "Model post-processing for hardware acceleration"
  ],
  "tags": [
    "OpenVINO",
    "quantization",
    "optimization",
    "pattern-matching",
    "NPU",
    "GGML",
    "tensor-shape",
    "MatMul"
  ],
  "markdown": "## SqueezeMatmul Optimization Pass\n\nThis OpenVINO pass modifies MatMul operations in quantized models by inserting Squeeze/Unsqueeze operations to adjust tensor dimensions for NPU compatibility.\n\n### Key Details\n- **Target Pattern**: MatMul with 4D activation and 2D weight tensors\n- **Transformation**: Inserts Squeeze(axis=0) before MatMul and Unsqueeze(axis=0) after\n- **Purpose**: Meet NPU requirements for Dynamic Quantization (DQ) optimizations like DQMatMulGQ2i\n- **Constraints**: Only applies to static-shape tensors\n\n### Implementation Notes\n- Uses OpenVINO's pattern matching infrastructure\n- Preserves original node metadata via copy_runtime_info\n- Avoids unnecessary operations for dynamic shapes\n\n### Performance Considerations\n- Squeeze/Unsqueeze operations have negligible computational cost\n- Maintains memory efficiency by avoiding data duplication\n\n### Related Concepts\n- [[OpenVINO]]\n- [[Quantization]]\n- [[NPU Optimization]]\n- [[GGML Frontend]]"
}
