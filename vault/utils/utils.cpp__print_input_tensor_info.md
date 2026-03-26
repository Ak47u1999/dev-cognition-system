# utils.cpp__print_input_tensor_info

Tags: #loop

<think>
Okay, let's take a look at this C++ function. The function is called print_input_tensor_info and takes a name and a tensor. The goal is to analyze it and generate the required JSON.

First, the function starts by printing the name, shape, and address of the tensor. Then there's a switch statement based on the element type. For f32, it checks if the name contains "self_kq_mask". If not, it prints the first float value. If it does, it loops through rows and columns to print each value, checking for negative infinity. For f16, i32, and i64, it prints the first element or all elements depending on the type.

The summary should be a short title like "Tensor Info Printer". The summary paragraph needs to explain that it prints tensor details and data based on element type. Details should elaborate on the different cases and the special handling for "self_kq_mask".

Rationale might be about debugging, needing to inspect tensor data during model execution. Performance considerations could mention that printing all elements is slow for large tensors. Hidden insights might include the conditional output for certain names and the use of std::isinf for f32.

Where_used could be modules handling model inputs or debugging. Tags would be things like OpenVINO, debugging, etc. The markdown note should structure all these points clearly.
</think>

{
  "title": "Tensor Info Printer",
  "summary": "Prints detailed information about a tensor including shape, data type, memory address, and sample values based on element type.",
  "details": "This function outputs tensor metadata (name, shape, address) and processes element data differently based on type. For f32 tensors, it conditionally prints either the first value or a full 2D matrix for 'self_kq_mask' tensors. Special handling includes negative infinity detection. Other types (f16, i32, i64) print first element or full array.",
  "rationale": "Designed for debugging/inspection during model execution. Conditional formatting for specific tensor names suggests domain-specific knowledge of expected input patterns. Type-specific handling ensures appropriate data representation for different numerical types.",
  "performance": "May be slow for large tensors due to O(n) element printing. Matrix printing for 'self_kq_mask' could be particularly expensive for high-dimensional data. Avoid in production code paths.",
  "hidden_insights": [
    "Special case for 'self_kq_mask' tensors indicates potential use in attention mechanisms",
    "Negative infinity detection implies handling of special floating-point values",
    "Uses linear indexing for 2D tensors assuming row-major layout",
    "Prints raw pointer address for memory debugging purposes"
  ],
  "where_used": [
    "Model input validation modules",
    "Inference pipeline debugging",
    "Tensor shape verification utilities",
    "OpenVINO model execution tracing"
  ],
  "tags": [
    "OpenVINO",
    "debugging",
    "tensor",
    "C++",
    "model-inspection"
  ],
  "markdown": "## Tensor Info Printer\n\nPrints detailed information about a tensor including shape, data type, memory address, and sample values based on element type.\n\n### Key Features\n- Outputs tensor metadata (name, shape, address)\n- Type-specific data formatting for f32, f16, i32, i64\n- Special handling for 'self_kq_mask' tensors\n- Negative infinity detection for f32 values\n\n### Usage Context\nUsed for debugging/inspection during model execution. The function's conditional formatting for specific tensor names suggests domain-specific knowledge of expected input patterns.\n\n### Performance Notes\n- May be slow for large tensors due to O(n) element printing\n- Matrix printing for 'self_kq_mask' could be particularly expensive for high-dimensional data\n\n### Hidden Insights\n- Special case for 'self_kq_mask' tensors indicates potential use in attention mechanisms\n- Negative infinity detection implies handling of special floating-point values\n- Uses linear indexing for 2D tensors assuming row-major layout\n- Prints raw pointer address for memory debugging purposes\n\n### Call Sites\n- Model input validation modules\n- Inference pipeline debugging\n- Tensor shape verification utilities\n- OpenVINO model execution tracing"
}
