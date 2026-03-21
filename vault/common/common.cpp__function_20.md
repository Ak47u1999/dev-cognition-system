# common.cpp__function_20

Tags: #recursion

{
  "title": "Ensure Trailing Slash",
  "summary": "A lambda function that adds a trailing slash to a given path if it doesn't already exist.",
  "details": "This function takes a string path as input and checks if it ends with a directory separator. If not, it appends the separator to the end of the path. This is useful for ensuring that file paths are properly formatted for operations like directory creation or file access.",
  "rationale": "The function uses a lambda expression to create a small, reusable function. This is a common pattern in C++ for creating simple, one-time-use functions.",
  "performance": "The function has a time complexity of O(1), making it very efficient. It only performs a single operation to check the last character of the string and append the separator if necessary.",
  "hidden_insights": [
    "The use of `DIRECTORY_SEPARATOR` ensures that the function works correctly on different operating systems, where the directory separator may be different (e.g., '/' on Unix-like systems and '\' on Windows)."
  ],
  "where_used": [
    "File system operations",
    "Directory creation",
    "File access"
  ],
  "tags": [
    "path manipulation",
    "directory separator",
    "file system"
  ],
  "markdown": "### Ensure Trailing Slash
A lambda function that adds a trailing slash to a given path if it doesn't already exist.

#### Purpose
Ensure that file paths are properly formatted for operations like directory creation or file access.

#### Usage
```cpp
auto path = ensure_trailing_slash("/path/to/directory");
```
#### Notes
The function uses `DIRECTORY_SEPARATOR` to ensure compatibility with different operating systems."
