# ggml-cpu.c__ggml_cpu_has_fma

Tags: #ggml

```json
{
  "title": "Check for FMA Instruction",
  "summary": "This function checks if the CPU supports the FMA (Fused Multiply-Add) instruction.",
  "details": "The function uses a preprocessor directive to check if the __FMA__ macro is defined. If it is, the function returns 1, indicating that the CPU supports FMA. Otherwise, it returns 0.",
  "rationale": "The function is implemented this way to provide a simple and efficient way to check for FMA support. The preprocessor directive allows the compiler to optimize the function at compile-time.",
  "performance": "The function has a constant time complexity, making it suitable for performance-critical code.",
  "hidden_insights": [
    "The function relies on the compiler's ability to define the __FMA__ macro when FMA is supported.",
    "The function does not actually check for FMA support at runtime, but rather relies on the preprocessor directive."
  ],
  "where_used": [
    "Optimized math libraries",
    "High-performance applications",
    "Embedded systems"
  ],
  "tags": [
    "FMA",
    "CPU",
    "Instruction set",
    "Preprocessor directive"
  ],
  "markdown": "## Check for FMA Instruction\n\nThis function checks if the CPU supports the FMA (Fused Multiply-Add) instruction.\n\n### Summary\n\nThe function uses a preprocessor directive to check if the __FMA__ macro is defined. If it is, the function returns 1, indicating that the CPU supports FMA. Otherwise, it returns 0.\n\n### Details\n\nThe function is implemented this way to provide a simple and efficient way to check for FMA support. The preprocessor directive allows the compiler to optimize the function at compile-time.\n\n### Performance\n\nThe function has a constant time complexity, making it suitable for performance-critical code.\n\n### Where Used\n\n* Optimized math libraries\n* High-performance applications\n* Embedded systems\n\n### Tags\n\n* FMA\n* CPU\n* Instruction set\n* Preprocessor directive"
}
