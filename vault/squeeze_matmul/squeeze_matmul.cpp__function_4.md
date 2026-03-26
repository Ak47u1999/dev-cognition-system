# squeeze_matmul.cpp__function_4

Tags: #ggml #kernel #memory #recursion

<think>
Okay, let's take a look at this code. The function is part of a pass in an optimization framework, probably related to neural network model transformations. The class is called SqueezeMatmul, and it's in the pass namespace. The constructor sets up a matcher for a MatMul operation with specific input patterns.

The code uses OpenVINO's opset, so this is likely part of the OpenVINO framework. The goal here seems to be modifying the model by inserting Squeeze and Unsqueeze operations around a MatMul. The comment mentions quantized models and NPUW expecting 3D activations, which suggests this is for optimizing quantized models on a specific hardware (NPUW).

The callback function checks if the activation and weight tensors have static ranks. If the activation is 4D and weights are 2D, it adds a Squeeze on the first axis, performs MatMul, then an Unsqueeze. This would convert a 4D activation to 3D, do the multiplication, then restore the original shape. The rationale is probably to meet hardware requirements that expect 3D tensors for certain operations, like DQMatMulGQ2i.

Performance considerations would involve the overhead of adding these operations versus the gain from using optimized hardware paths. The hidden insight here is that the transformation is only applied when the ranks are static and specific, which might limit its applicability but ensures correctness. The tags should include things like OpenVINO, model optimization, quantization, etc. The where_used would be in model conversion or optimization passes for NPUW targets.
</think>

{
  "title": "SqueezeMatmul Pass",
  "summary": "Transforms 4D activation inputs to 3D for MatMul operations in quantized models to meet hardware requirements.",
  "details": "This OpenVINO pass identifies MatMul operations with 4D activation inputs and 2D weight inputs in quantized models. It inserts Squeeze/Unsqueeze operations to convert 4D activations to 3D format required by NPUW hardware (e.g., DQMatMulGQ2i), while preserving original tensor shapes through runtime information copying.",
  "rationale": "Quantized models on NPUW require 3D activations for optimized execution. This transformation enables hardware compatibility by temporarily reducing activation rank during MatMul while maintaining data integrity through shape-preserving operations.",
  "performance": "Adds minimal overhead through squeeze/unsqueeze operations but enables hardware-specific optimizations. Static shape requirements limit applicability to fixed-rank models.",
  "hidden_insights": [
    "Only applies when both input shapes are statically known",
    "Preserves original node naming for model traceability",
    "Requires exact rank match (4D activation, 2D weights)",
    "Runtime info propagation ensures execution consistency"
  ],
  "where_used": [
    "Model quantization pipelines",
    "NPUW-specific model conversion tools",
    "Dynamic Quantization (DQ) optimization passes",
    "GGML frontend transformations"
  ],
  "tags": [
    "OpenVINO",
    "Model Optimization",
    "Quantization",
    "Hardware Compatibility",
    "Graph Transformation"
  ],
  "markdown": "## SqueezeMatmul Pass\n\nTransforms 4D activation inputs to 3D for MatMul operations in quantized models to meet hardware requirements.\n\n### Details\nThis OpenVINO pass identifies MatMul operations with 4D activation inputs and 2D weight inputs in quantized models. It inserts Squeeze/Unsqueeze operations to convert 4D activations to 3D format required by NPUW hardware (e.g., DQMatMulGQ2i), while preserving original tensor shapes through runtime information copying.\n\n### Rationale\nQuantized models on NPUW require 3D activations for optimized execution. This transformation enables hardware compatibility by temporarily reducing activation rank during MatMul while maintaining data integrity through shape-preserving operations.\n\n### Performance\nAdds minimal overhead through squeeze/unsqueeze operations but enables hardware-specific optimizations. Static shape requirements limit applicability to fixed-rank models.\n\n### Hidden Insights\n- Only applies when both input shapes are statically known\n- Preserves original node naming for model traceability\n- Requires exact rank match (4D activation, 2D weights)\n- Runtime info propagation ensures execution consistency\n\n### Where Used\n- Model quantization pipelines\n- NPUW-specific model conversion tools\n- Dynamic Quantization (DQ) optimization passes\n- GGML frontend transformations"
}
