# kleidiai.cpp__ggml_ne

Tags: #ggml

# ggml_ne Function

The ggml_ne function is a utility function that retrieves the number of elements in a specified dimension of a GGML tensor.

## Purpose

This function provides a convenient way to access tensor dimensions, which is essential for various operations in the GGML library.

## Usage

The function takes a pointer to a GGML tensor and a dimension index as input, and returns the corresponding number of elements as an integer.

## Example

```cpp
int64_t num_elements = ggml_ne(tensor, 0);
```
