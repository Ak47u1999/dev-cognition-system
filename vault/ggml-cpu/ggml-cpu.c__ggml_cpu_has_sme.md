# ggml-cpu.c__ggml_cpu_has_sme

Tags: #ggml

```json
{
  "title": "Check for Secure Monitor Extension (SME)",
  "summary": "This function checks if the Secure Monitor Extension (SME) is supported on the current CPU architecture.",
  "details": "The function uses preprocessor directives to check for the presence of the __ARM_ARCH and __ARM_FEATURE_SME macros, which indicate support for ARM architecture and the SME feature respectively. If both conditions are met, the function returns 1, indicating SME support. Otherwise, it returns 0.",
  "rationale": "The function uses preprocessor directives to avoid runtime overhead and provide a simple way to check for SME support.",
  "performance": "This function has a constant time complexity, making it suitable for performance-critical code paths.",
  "hidden_insights": [
    "The function relies on preprocessor directives, which may not be suitable for all build systems or architectures.",
    "The SME feature is specific to ARM architecture, so this function will always return 0 on non-ARM platforms."
  ],
  "where_used": [
    "Other functions or modules that require SME support",
    "Platform-specific code that needs to adapt to SME availability"
  ],
  "tags": [
    "ARM",
    "SME",
    "Secure Monitor Extension",
    "CPU architecture"
  ],
  "markdown": "### Check for Secure Monitor Extension (SME)
This function checks if the Secure Monitor Extension (SME) is supported on the current CPU architecture.
#### Details
The function uses preprocessor directives to check for the presence of the __ARM_ARCH and __ARM_FEATURE_SME macros, which indicate support for ARM architecture and the SME feature respectively.
#### Rationale
The function uses preprocessor directives to avoid runtime overhead and provide a simple way to check for SME support.
#### Performance
This function has a constant time complexity, making it suitable for performance-critical code paths.
#### Where Used
Other functions or modules that require SME support
Platform-specific code that needs to adapt to SME availability
#### Tags
ARM
SME
Secure Monitor Extension
CPU architecture"
}
