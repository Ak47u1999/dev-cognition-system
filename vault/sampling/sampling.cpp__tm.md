# sampling.cpp__tm

{
  "title": "common_time_meas tm() function",
  "summary": "A simple function that returns a common_time_meas object.",
  "details": "This function creates a common_time_meas object with the total time in microseconds and a flag indicating whether performance metrics should be collected.",
  "rationale": "The function is likely implemented this way to encapsulate the creation of a common_time_meas object with specific parameters.",
  "performance": "The performance of this function is likely to be very low, as it only involves a simple function call and object creation.",
  "hidden_insights": ["The function uses a common_time_meas object, which may be used for performance measurement or profiling.", "The params.no_perf flag may be used to disable performance metrics collection."],
  "where_used": ["likely in performance measurement or profiling code"],
  "tags": ["performance measurement", "profiling", "common_time_meas"],
  "markdown": "## common_time_meas tm() function\n\nA simple function that returns a common_time_meas object.\n\n### Purpose\n\nThis function creates a common_time_meas object with the total time in microseconds and a flag indicating whether performance metrics should be collected.\n\n### Rationale\n\nThe function is likely implemented this way to encapsulate the creation of a common_time_meas object with specific parameters.\n\n### Performance\n\nThe performance of this function is likely to be very low, as it only involves a simple function call and object creation.\n\n### Hidden Insights\n\n* The function uses a common_time_meas object, which may be used for performance measurement or profiling.\n* The params.no_perf flag may be used to disable performance metrics collection.\n\n### Where Used\n\nlikely in performance measurement or profiling code\n\n### Tags\n\n* performance measurement\n* profiling\n* common_time_meas"
