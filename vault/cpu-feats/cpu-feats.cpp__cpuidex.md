# cpu-feats.cpp__cpuidex

```json
{
  "title": "CPUID Extended Function",
  "summary": "A wrapper function for the __cpuidex intrinsic, which retrieves extended CPU information.",
  "details": "The cpuidex function takes an array of four integers to store the CPU information and two integers representing the EAX and ECX registers. It calls the __cpuidex intrinsic to retrieve the extended CPU information and stores it in the provided array.",
  "rationale": "This function is likely implemented as a wrapper to provide a more convenient interface for retrieving CPU information, making it easier to use in various parts of the codebase.",
  "performance": "The performance impact of this function is likely negligible, as it simply calls an intrinsic function and does not perform any significant computations.",
  "hidden_insights": [
    "The __cpuidex intrinsic is a low-level function that interacts directly with the CPU, making it a good candidate for optimization in performance-critical code.",
    "The use of an intrinsic function like __cpuidex can provide better performance than a software implementation, as it is optimized for the specific CPU architecture."
  ],
  "where_used": [
    "cpu_info.c",
    "cpu_features.h",
    "system_info.c"
  ],
  "tags": [
    "CPUID",
    "x86",
    "intrinsic",
    "wrapper"
  ],
  "markdown": "### CPUID Extended Function\n\nA wrapper function for the `__cpuidex` intrinsic, which retrieves extended CPU information.\n\n#### Purpose\n\nThe `cpuidex` function takes an array of four integers to store the CPU information and two integers representing the EAX and ECX registers. It calls the `__cpuidex` intrinsic to retrieve the extended CPU information and stores it in the provided array.\n\n#### Rationale\n\nThis function is likely implemented as a wrapper to provide a more convenient interface for retrieving CPU information, making it easier to use in various parts of the codebase.\n\n#### Performance\n\nThe performance impact of this function is likely negligible, as it simply calls an intrinsic function and does not perform any significant computations.\n\n#### Where Used\n\n* `cpu_info.c`\n* `cpu_features.h`\n* `system_info.c`"
}
