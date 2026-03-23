# binary-ops.cpp__vec_binary_op_non_contiguous

Tags: #loop

```json
{
  "title": "Non-Contiguous Vector Binary Operation",
  "summary": "This function performs a binary operation on two non-contiguous vectors, converting the results to the destination type.",
  "details": "The function iterates over the input vector 'x' and performs a binary operation with the corresponding element from vector 'y'. The results are converted to the destination type 'dst_t' using type conversion tables. The function assumes that the vectors 'x' and 'y' have the same number of elements as the destination vector 'z'.",
  "rationale": "The function is likely implemented this way to allow for efficient processing of non-contiguous vectors, where the elements of 'y' are stored in a separate memory block.",
  "performance": "The function has a time complexity of O(n), where n is the number of elements in the input vectors. The use of type conversion tables and pointer arithmetic may improve performance by reducing the number of memory accesses.",
  "hidden_insights": [
    "The function uses pointer arithmetic to access the elements of vector 'y' in a non-contiguous manner.",
    "The use of type conversion tables allows for efficient conversion between different data types."
  ],
  "where_used": [
    "Neural network inference engines",
    "Scientific computing applications"
  ],
  "tags": [
    "vector operations",
    "binary operations",
    "non-contiguous memory access",
    "type conversion"
  ],
  "markdown": "## Non-Contiguous Vector Binary Operation\n\nThis function performs a binary operation on two non-contiguous vectors, converting the results to the destination type.\n\n### Function Signature\n\n```cpp\nvoid vec_binary_op_non_contiguous(const int64_t n, const int64_t ne10, const int64_t nb10, dst_t * z, const src0_t * x, const src1_t * y)\n```\n\n### Parameters\n\n* `n`: The number of elements in the input vectors.\n* `ne10`: The number of elements in each block of vector 'y'.\n* `nb10`: The number of blocks in vector 'y'.\n* `z`: The destination vector.\n* `x`: The first input vector.\n* `y`: The second input vector.\n\n### Example Use Case\n\nThis function can be used in neural network inference engines to perform binary operations on non-contiguous vectors.\n\n### Performance Considerations\n\nThe function has a time complexity of O(n), where n is the number of elements in the input vectors. The use of type conversion tables and pointer arithmetic may improve performance by reducing the number of memory accesses.\n"
}
