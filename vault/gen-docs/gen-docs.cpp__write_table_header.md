# gen-docs.cpp__write_table_header

### write_table_header

Writes the header for a table to an output stream.

This function is used to generate a table header with two columns: Argument and Explanation. It is typically used in documentation or logging contexts.

### Usage

```cpp
static void write_table_header(std::ostringstream & ss) {
    ss << '| Argument | Explanation |
';
    ss << '| -------- | ----------- |
';
}
```
