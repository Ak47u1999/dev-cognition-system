# runtime.cpp__ensure_key_type_allowed

```json
{
  "title": "Ensure Key Type Allowed",
  "summary": "This function checks if a given value is hashable and can be used as an object key.",
  "details": "The function takes a value as input and checks if it is hashable using the `is_hashable()` method. If the value is not hashable, it throws a `std::runtime_error` exception with a message indicating that the type of the value is not allowed as an object key.",
  "rationale": "This function is likely implemented to prevent non-hashable types from being used as object keys, which could lead to unexpected behavior or errors in the program.",
  "performance": "This function has a time complexity of O(1) as it only checks a single property of the input value.",
  "hidden_insights": [
    "The `is_hashable()` method is not a standard C++ method, it's likely a custom method implemented for the `value` class.",
    "The `std::runtime_error` exception is thrown with a message that includes the type of the value, which can be useful for debugging purposes."
  ],
  "where_used": [
    "This function is likely used in a data structure or container that requires hashable keys, such as a hash map or a set."
  ],
  "tags": [
    "hashable",
    "object key",
    "std::runtime_error",
    "value class"
  ],
  "markdown": "### Ensure Key Type Allowed\n\nThis function checks if a given value is hashable and can be used as an object key.\n\n#### Purpose\n\nPrevent non-hashable types from being used as object keys.\n\n#### Implementation\n\nThe function takes a value as input and checks if it is hashable using the `is_hashable()` method. If the value is not hashable, it throws a `std::runtime_error` exception with a message indicating that the type of the value is not allowed as an object key.\n\n#### Example\n\n```cpp\nensure_key_type_allowed(my_value);\n```"
}
