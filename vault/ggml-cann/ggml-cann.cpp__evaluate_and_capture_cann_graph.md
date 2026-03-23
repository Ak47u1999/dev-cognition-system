# ggml-cann.cpp__evaluate_and_capture_cann_graph

Tags: #complex #ggml #kernel #loop

```json
{
  "title": "Evaluate and Capture CANN Graph",
  "summary": "This function evaluates and captures a CANN graph, performing graph execution if CANN graphs are not enabled or graph capture is required.",
  "details": "The function first checks if CANN graph capture is required and if CANN graphs are enabled. If both conditions are met, it begins CANN graph capture. It then iterates over the nodes in the graph, performing operations such as fusion, execution, and logging. If CANN graphs are enabled, it executes the CANN graph and ends CANN graph capture if capture is required.",
  "rationale": "The function is implemented this way to handle both CANN graph and non-CANN graph scenarios, allowing for flexibility and adaptability.",
  "performance": "The function's performance is optimized by using caching and asynchronous execution, reducing the overhead of graph execution.",
  "hidden_insights": [
    "The function uses a static boolean variable to store the result of parsing an environment variable, which is used to determine whether to perform operator fusion.",
    "The function uses a cache to store the matched CANN graph, which is used to execute the graph asynchronously."
  ],
  "where_used": [
    "ggml-cann.cpp",
    "ggml_backend_cann_context"
  ],
  "tags": [
    "CANN",
    "graph",
    "execution",
    "capture",
    "fission",
    "logging"
  ],
  "markdown": "## Evaluate and Capture CANN Graph
### Purpose
This function evaluates and captures a CANN graph, performing graph execution if CANN graphs are not enabled or graph capture is required.

### Implementation
The function first checks if CANN graph capture is required and if CANN graphs are enabled. If both conditions are met, it begins CANN graph capture. It then iterates over the nodes in the graph, performing operations such as fusion, execution, and logging. If CANN graphs are enabled, it executes the CANN graph and ends CANN graph capture if capture is required.

### Performance
The function's performance is optimized by using caching and asynchronous execution, reducing the overhead of graph execution.

### Hidden Insights
* The function uses a static boolean variable to store the result of parsing an environment variable, which is used to determine whether to perform operator fusion.
* The function uses a cache to store the matched CANN graph, which is used to execute the graph asynchronously.

### Where Used
* `ggml-cann.cpp`
* `ggml_backend_cann_context`"
}
