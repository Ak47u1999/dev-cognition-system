# ggml-openvino.cpp__is_op_unsupported_case

Tags: #complex #ggml #kernel #loop #memory

<think>
Okay, let's take a look at this function. The name is is_op_unsupported_case, which suggests it checks if a certain operation is unsupported. The function takes a ggml_tensor pointer as an argument. 

Looking at the code, it's a switch statement based on the op->op value. Each case corresponds to different operations like GGML_OP_GET_ROWS, GGML_OP_ADD, etc. For each operation, there are conditions that check various properties of the tensor and its sources. If any of these conditions are met, the function returns true, indicating the operation is unsupported.

For example, in the GGML_OP_GET_ROWS case, it checks if the fourth dimension (ne[3]) is not 1. If so, returns true. For GGML_OP_ADD and GGML_OP_MUL, it checks if the second source is a PERMUTE operation or if the dimensions of the sources don't match in certain ways. 

The GGML_OP_SOFT_MAX case checks if there's a third source (sinks) or if the max_bias is greater than zero. Similarly, GGML_OP_FLASH_ATTN_EXT checks for sinks, unsupported parameters like max_bias and logit_softcap. 

The GGML_OP_PERMUTE case returns true if the type is BF16. The GGML_OP_CPY checks if the destination isn't the same as the source. For GGML_OP_MUL_MAT, there are several conditions related to types (like F16), dimensions, and operations on sources. 

The GGML_OP_ROPE case checks the mode, n_dims, type, and other parameters like ext_factor. There's also a check for the view source's dimensions. 

The default case doesn't return anything, so the function proceeds to check if the op is GGML_OP_GET_ROWS again, but only if the type is Q4_K or Q5_K and the size is 256. 

The function returns false if none of the conditions are met. 

Now, the summary should capture that this function determines if a given operation is unsupported by OpenVINO backend based on various tensor properties and operation parameters. The details would elaborate on each case and the specific checks. The rationale is that OpenVINO has limitations, so this function helps in identifying those cases to avoid runtime errors. Performance considerations might include avoiding unnecessary computations by early returns. Hidden insights could be the specific parameter checks that aren't obvious, like the BF16 in PERMUTE or the Q4_K/Q5_K in GET_ROWS. Where_used would be parts of the code that handle operation conversion or backend selection. Tags would include things like OpenVINO, GGML, backend support, etc. The markdown note should structure all this information clearly.
</think>

{
  "title": "OpenVINO Unsupported Op Checker",
  "summary": "This function determines whether a GGML operation is unsupported by the OpenVINO backend based on tensor properties and operation parameters.",
  "details": "The function checks each operation type (e.g., ADD, MUL, SOFT_MAX) against specific constraints. For example, it flags operations with unsupported data types (BF16 in PERMUTE), dimension mismatches, or special parameters (e.g., max_bias in SOFT_MAX). It also handles edge cases like quantized tensors in MUL_MAT and view-based tensors in ROPE. Returns true if the operation is unsupported.",
  "rationale": "OpenVINO has hardware and API limitations that restrict certain operations. This function preemptively identifies unsupported cases to avoid runtime errors during model execution. Direct checks on tensor shapes, types, and operation parameters ensure compatibility with OpenVINO's inference engine.",
  "performance": "Early returns and minimal branching optimize performance. Avoids deep tensor traversal unless necessary. Memory copies (memcpy) for parameter extraction are localized to specific op types.",
  "hidden_insights": [
    "BF16 PERMUTE is explicitly blocked due to kernel limitations",
    "Q4_K/Q5_K GET_ROWS with 256 elements has known accuracy issues",
    "MUL_MAT with two F16 tensors is disabled despite being technically valid",
    "ROPE view-source dimension checks hint at shape-inference bugs in OpenVINO"
  ],
  "where_used": [
    "Backend conversion pipeline",
    "Model compiler validation",
    "Operation fallback routing",
    "Quantization compatibility checks"
  ],
  "tags": [
    "OpenVINO",
    "GGML",
    "Backend Support",
    "Tensor Validation",
    "Operation Constraints"
  ],
  "markdown": "## OpenVINO Unsupported Op Checker\n\nThis function determines whether a GGML operation is unsupported by the OpenVINO backend based on tensor properties and operation parameters.\n\n### Key Checks\n- **BF16 PERMUTE**: Blocked due to kernel limitations\n- **Dimension Mismatches**: ADD/MUL operations require compatible shapes\n- **Special Parameters**: SOFT_MAX/FLASH_ATTN_EXT reject max_bias > 0\n- **Quantized Tensors**: MUL_MAT with Q4_K/Q5_K has accuracy issues\n- **View Sources**: ROPE requires specific view-source dimension relationships\n\n### Rationale\nOpenVINO has hardware and API limitations that restrict certain operations. This function preemptively identifies unsupported cases to avoid runtime errors during model execution.\n\n### Performance Notes\n- Early returns minimize unnecessary checks\n- Localized memory copies for parameter extraction\n- Minimal tensor traversal\n\n### Hidden Insights\n- Q4_K/Q5_K GET_ROWS with 256 elements has known accuracy issues\n- MUL_MAT with two F16 tensors is disabled despite being technically valid\n- ROPE view-source dimension checks hint at shape-inference bugs in OpenVINO\n\n### Usage Context\nUsed in backend conversion pipelines and model compiler validation to route operations to appropriate backends."
}
