# common.cpp__fs_create_directory_with_parents

Tags: #loop

```json
{
  "title": "Create Directory with Parents",
  "summary": "This function creates a directory with its parents if they do not exist. It uses the Windows API for Windows and the POSIX API for Unix-like systems.",
  "details": "The function takes a path as input and checks if the directory already exists. If it does, it checks if it's a directory. If not, it returns false. If the directory does not exist, it creates its parents procedurally by splitting the path into sub-paths and creating each sub-path. If any of the sub-paths cannot be created, the function returns false.",
  "rationale": "This function is implemented this way to handle the differences between Windows and Unix-like systems. Windows uses the Windows API, while Unix-like systems use the POSIX API. The function uses the appropriate API for each system to create directories.",
  "performance": "The function has a time complexity of O(n), where n is the length of the path. This is because it needs to iterate over each character in the path to split it into sub-paths.",
  "hidden_insights": [
    "The function uses the `utf8_to_wstring` function to convert the path from UTF-8 to a wide string on Windows. This is necessary because the Windows API uses wide strings.",
    "The function uses the `GetFileAttributesW` function to check if a directory exists on Windows. This function returns the attributes of the file, which includes the directory attribute.",
    "The function uses the `stat` function to check if a directory exists on Unix-like systems. This function returns information about the file, including its type."
  ],
  "where_used": [
    "File system utilities",
    "Directory creation functions"
  ],
  "tags": [
    "directory creation",
    "file system",
    "Windows API",
    "POSIX API"
  ],
  "markdown": "## Create Directory with Parents
This function creates a directory with its parents if they do not exist.

### Usage
```cpp
bool fs_create_directory_with_parents(const std::string & path)
```
### Parameters
* `path`: The path to the directory to create.

### Returns
* `true` if the directory and its parents are created successfully.
* `false` if any of the sub-paths cannot be created.

### Notes
This function uses the Windows API on Windows and the POSIX API on Unix-like systems. It is designed to handle the differences between these two systems."
