# mmq.cpp__pack_qs

Tags: #loop

```json
{
  "title": "pack_qs function",
  "summary": "The pack_qs function is used to pack nibbles from a TB structure into a packed_B buffer.",
  "details": "This function takes a packed_B buffer, a TB structure, and an integer KB as input. It first loads 8 nibbles from the TB structure into 8 __m256i vectors, transposes them, and stores them in a temporary buffer. It then loads another 8 nibbles from the TB structure, transposes them, and stores them in the temporary buffer. Finally, it packs the nibbles from the temporary buffer into the packed_B buffer using __m512i vectors.",
  "rationale": "The function is implemented this way to fully utilize the vector length of __m512i and to pack the nibbles in a way that minimizes the number of memory accesses.",
  "performance": "The function uses SIMD instructions to pack the nibbles, which can significantly improve performance. However, the use of temporary buffers and the packing process may introduce some overhead.",
  "hidden_insights": [
    "The function uses a temporary buffer to store the transposed nibbles, which allows it to pack the nibbles in a way that minimizes the number of memory accesses.",
    "The function uses __m512i vectors to pack the nibbles, which can fully utilize the vector length and improve performance."
  ],
  "where_used": [
    "tb_pack.cpp",
    "tb_unpack.cpp"
  ],
  "tags": [
    "SIMD",
    "packing",
    "nibbles",
    "TB structure"
  ],
  "markdown": "## pack_qs function\n\nThe `pack_qs` function is used to pack nibbles from a TB structure into a packed_B buffer.\n\n### Details\n\nThis function takes a packed_B buffer, a TB structure, and an integer KB as input. It first loads 8 nibbles from the TB structure into 8 `__m256i` vectors, transposes them, and stores them in a temporary buffer. It then loads another 8 nibbles from the TB structure, transposes them, and stores them in the temporary buffer. Finally, it packs the nibbles from the temporary buffer into the packed_B buffer using `__m512i` vectors.\n\n### Rationale\n\nThe function is implemented this way to fully utilize the vector length of `__m512i` and to pack the nibbles in a way that minimizes the number of memory accesses.\n\n### Performance\n\nThe function uses SIMD instructions to pack the nibbles, which can significantly improve performance. However, the use of temporary buffers and the packing process may introduce some overhead.\n\n### Hidden Insights\n\n* The function uses a temporary buffer to store the transposed nibbles, which allows it to pack the nibbles in a way that minimizes the number of memory accesses.\n* The function uses `__m512i` vectors to pack the nibbles, which can fully utilize the vector length and improve performance.\n\n### Where Used\n\n* `tb_pack.cpp`\n* `tb_unpack.cpp`\n\n### Tags\n\n* SIMD\n* packing\n* nibbles\n* TB structure"
}
