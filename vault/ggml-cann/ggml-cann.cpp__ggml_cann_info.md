# ggml-cann.cpp__ggml_cann_info

Tags: #ggml

{
  "title": "ggml_cann_info Function",
  "summary": "Returns a static instance of ggml_cann_device_info.",
  "details": "This function returns a reference to a static instance of ggml_cann_device_info, which is initialized by calling ggml_cann_init(). The instance is reused across function calls, avoiding the overhead of repeated initialization.",
  "rationale": "The use of a static instance allows for lazy initialization and avoids repeated calls to ggml_cann_init(), which may have performance implications.",
  "performance": "The function has a constant time complexity, as it only involves a single static instance and a function call.",
  "hidden_insights": [
    "The use of a static instance can lead to thread-safety issues if not properly synchronized.",
    "The function assumes that ggml_cann_init() is thread-safe."
  ],
  "where_used": [
    "ggml-cann.cpp"
  ],
  "tags": [
    "C++",
    "static instance",
    "lazy initialization"
  ],
  "markdown": "### ggml_cann_info Function\n\nReturns a static instance of ggml_cann_device_info.\n\n#### Details\nThis function returns a reference to a static instance of ggml_cann_device_info, which is initialized by calling ggml_cann_init(). The instance is reused across function calls, avoiding the overhead of repeated initialization.\n\n#### Rationale\nThe use of a static instance allows for lazy initialization and avoids repeated calls to ggml_cann_init(), which may have performance implications.\n\n#### Performance\nThe function has a constant time complexity, as it only involves a single static instance and a function call.\n\n#### Hidden Insights\n* The use of a static instance can lead to thread-safety issues if not properly synchronized.\n* The function assumes that ggml_cann_init() is thread-safe.\n\n#### Where Used\n* ggml-cann.cpp\n\n#### Tags\n* C++\n* static instance\n* lazy initialization"
