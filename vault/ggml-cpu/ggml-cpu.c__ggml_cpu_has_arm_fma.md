# ggml-cpu.c__ggml_cpu_has_arm_fma

Tags: #ggml

```json
{
  "title": "ARM FMA Capability Check",
  "summary": "This function checks if the CPU supports ARM FMA instructions.",
  "details": "The function uses the `__ARM_FEATURE_FMA` macro to determine if the CPU supports ARM FMA instructions. If the macro is defined, the function returns 1, indicating that the CPU supports ARM FMA. Otherwise, it returns 0.",
  "rationale": "The function uses a preprocessor directive to check for the presence of the `__ARM_FEATURE_FMA` macro, which is a common way to detect CPU capabilities in C code.",
  "performance": "This function has a constant time complexity, as it only involves a single macro check.",
  "hidden_insights": [
    "The `__ARM_FEATURE_FMA` macro is a compiler-specific feature that may not be available on all platforms.",
    "The function assumes that the `__ARM_FEATURE_FMA` macro is defined if and only if the CPU supports ARM FMA instructions."
  ],
  "where_used": [
    "Other functions that require ARM FMA support",
    "CPU detection and feature probing code"
  ],
  "tags": [
    "ARM FMA",
    "CPU detection",
    "feature probing"
  ],
  "markdown": "### ARM FMA Capability Check
This function checks if the CPU supports ARM FMA instructions.
#### Purpose
The purpose of this function is to determine if the CPU supports ARM FMA instructions.
#### Implementation
The function uses the `__ARM_FEATURE_FMA` macro to determine if the CPU supports ARM FMA instructions.
#### Rationale
The function uses a preprocessor directive to check for the presence of the `__ARM_FEATURE_FMA` macro, which is a common way to detect CPU capabilities in C code.
#### Performance
This function has a constant time complexity, as it only involves a single macro check.
#### Where Used
This function is likely used in other functions that require ARM FMA support, as well as in CPU detection and feature probing code.
#### Tags
ARM FMA, CPU detection, feature probing"
}
