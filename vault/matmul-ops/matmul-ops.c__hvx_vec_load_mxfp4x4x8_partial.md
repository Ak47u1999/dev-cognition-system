# matmul-ops.c__hvx_vec_load_mxfp4x4x8_partial

Tags: #loop

<think>
Okay, let's take a look at this function. The name is hvx_vec_load_mxfp4x4x8_partial. It's a static inline function, which suggests it's meant to be used internally and inlined for performance. The return type is HVX_Vector_x8, which probably represents an array of 8 HVX vectors. The function takes a pointer to uint8_t and a uint32_t n.

First, the function casts the input pointer to a pointer of HVX_Vector. Then it calculates qk as QK_Q4_0x4x2, which is 256. The variables nb and nloe are the number of full blocks and the leftover elements. The mask_h4 is a vector with 0x0F splatted, and lut is a lookup table from kvalues_mxfp4_lut.

The main loop processes each block. For each block, it splits the vector into two parts: the lower 4 bits and the upper 4 bits by shifting. Then it applies the lookup table to both parts. The loop is unrolled with #pragma unroll(2), which might help with performance by reducing loop overhead.

The if (nloe) block handles the remaining elements. It does a similar split but then zips the even and odd parts together using vshuff, then applies the lookup table again. This seems to handle the case where the total elements aren't a multiple of 256.

The function is likely part of a matrix multiplication routine optimized for Hexagon Vectors (HVX), which is used in Qualcomm processors. The use of HVX intrinsics suggests it's for SIMD processing, handling data in parallel. The MXFP4 format probably refers to a 4-bit floating-point representation, and the lookup table is used to convert these 4-bit values into a different format, maybe for higher precision or to prepare for multiplication.

Performance considerations would include the use of SIMD to process multiple elements at once, the unrolling of loops to reduce overhead, and efficient memory access patterns. The static inline ensures that the function is inlined, avoiding function call overhead. The handling of partial blocks with the nloe case ensures that all data is processed without unnecessary padding.

Non-obvious insights might include the specific use of the lookup table for 4-bit values, the way the data is split and recombined in the partial block, and the use of vector shuffling to interleave even and odd parts. The function is probably part of a larger library for quantized neural networks, where 4-bit weights are common to save memory and increase speed.

Tags would include SIMD, HVX, MXFP4, quantization, lookup tables, etc. The where_used would be in modules handling matrix multiplications, especially in neural network inference on Qualcomm hardware.
</think>

{
  "title": "MXFP4 Vector Loader",
  "summary": "This function loads and processes 4-bit MXFP4 data using Hexagon Vector eXtensions (HVX) for efficient SIMD operations, handling both full and partial blocks.",
  "details": "The function processes 4-bit MXFP4 data stored in 8-bit arrays, splitting each byte into two 4-bit values. It uses HVX vector intrinsics to load data, apply a lookup table for conversion, and handle partial blocks. The implementation processes data in 256-element blocks (128 bytes) with unrolled loops for performance. For partial blocks, it combines even/odd 4-bit values using vector shuffling.",
  "rationale": "MXFP4 quantization reduces memory footprint and increases throughput. The HVX SIMD approach maximizes parallelism, while the lookup table enables fast 4-bit to higher-precision conversion. The unrolled loop and inline declaration minimize overhead for performance-critical code paths.",
  "performance": "Optimized for Hexagon V60/V65 cores with 128-bit/256-bit vector registers. Processes 256 elements per iteration in full blocks, with efficient partial block handling. Memory access is sequential and aligned for cache-friendly operations.",
  "hidden_insights": [
    "The lookup table (kvalues_mxfp4_lut) likely maps 4-bit values to 8-bit or 16-bit floating-point representations",
    "Vector shuffling in partial blocks recombines even/odd 4-bit values into contiguous vectors",
    "The 'restrict' keyword ensures no aliasing between input pointer and internal vector pointer",
    "The mask 0x0F extracts lower 4 bits, while the upper 4 bits are obtained via right shift"
  ],
  "where_used": [
    "Quantized matrix multiplication kernels",
    "Neural network inference engines (e.g., GGML, TensorRT)",
    "Memory-constrained ML accelerators",
    "Qualcomm Hexagon DSP compute modules"
  ],
  "tags": [
    "SIMD",
    "HVX",
    "MXFP4",
    "quantization",
    "lookup-table",
    "vector-intrinsics",
    "memory-optimization"
  ],
  "markdown": "## MXFP4 Vector Loader\n\nThis function loads and processes 4-bit MXFP4 data using Hexagon Vector eXtensions (HVX) for efficient SIMD operations. It handles both full and partial blocks of data, splitting 8-bit values into two 4-bit components and applying a lookup table for conversion.\n\n### Key Features\n- Processes 256-element blocks (128 bytes) with unrolled loops\n- Uses vector shuffling for partial block handling\n- Optimized for Qualcomm Hexagon V60/V65 cores\n- Combines even/odd 4-bit values using bitwise operations\n\n### Implementation Notes\n- The lookup table `kvalues_mxfp4_lut` maps 4-bit values to higher-precision representations\n- Memory access is sequential and aligned for cache efficiency\n- `restrict` keyword ensures no pointer aliasing\n- Vector shuffling recombines even/odd 4-bit values in partial blocks\n\n### Performance Considerations\n- SIMD parallelism maximizes throughput\n- Loop unrolling reduces overhead\n- Inlined for minimal function call overhead\n- Efficient handling of partial blocks avoids unnecessary padding\n\nUsed in quantized matrix multiplication kernels and neural network inference engines on Qualcomm Hexagon DSPs."
}
