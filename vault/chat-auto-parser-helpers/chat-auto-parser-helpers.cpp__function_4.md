# chat-auto-parser-helpers.cpp__function_4

### is_marker_opener Function

Checks if a given character is a marker opener.

This function is a lambda expression that takes a single character as input and returns a boolean value indicating whether the character is either '<' or '['.

#### Usage

```cpp
auto is_marker_opener = [](char c) -> bool { return c == '<' || c == '['; }
```
