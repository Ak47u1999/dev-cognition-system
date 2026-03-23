# cpu-feats.cpp__FSGSBASE

```json
{
  "title": "FSGSBASE Function",
  "summary": "The FSGSBASE function checks if the FSGSBASE feature is supported by the CPU.",
  "details": "This function returns a boolean value indicating whether the FSGSBASE feature is supported by the CPU. FSGSBASE is a CPUID feature that allows for the use of the FS and GS base addresses in the CPUID instruction.",
  "rationale": "The function is likely implemented this way to provide a simple and efficient way to check for FSGSBASE support.",
  "performance": "The function has a constant time complexity, making it suitable for performance-critical code.",
  "hidden_insights": [
    "The function uses a global variable f_7_ebx to store the CPUID feature flags.",
    "The FSGSBASE feature is not enabled by default and must be explicitly enabled by the BIOS or UEFI firmware."
  ],
  "where_used": [
    "CPUID feature detection code",
    "Low-level system programming code"
  ],
  "tags": [
    "CPUID",
    "FSGSBASE",
    "CPU feature detection",
    "Low-level programming"
  ],
  "markdown": "## FSGSBASE Function\n\nThe FSGSBASE function checks if the FSGSBASE feature is supported by the CPU.\n\n### Summary\n\nThe FSGSBASE function returns a boolean value indicating whether the FSGSBASE feature is supported by the CPU.\n\n### Details\n\nFSGSBASE is a CPUID feature that allows for the use of the FS and GS base addresses in the CPUID instruction.\n\n### Rationale\n\nThe function is likely implemented this way to provide a simple and efficient way to check for FSGSBASE support.\n\n### Performance\n\nThe function has a constant time complexity, making it suitable for performance-critical code.\n\n### Hidden Insights\n\n* The function uses a global variable f_7_ebx to store the CPUID feature flags.\n* The FSGSBASE feature is not enabled by default and must be explicitly enabled by the BIOS or UEFI firmware.\n\n### Where Used\n\n* CPUID feature detection code\n* Low-level system programming code\n\n### Tags\n\n* CPUID\n* FSGSBASE\n* CPU feature detection\n* Low-level programming"
}
