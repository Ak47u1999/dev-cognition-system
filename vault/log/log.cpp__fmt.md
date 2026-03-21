# log.cpp__fmt

Tags: #loop #memory #recursion

```json
{
  "title": "Log Message Formatter",
  "summary": "This function formats a log message using the provided format string and arguments, and stores it in a circular buffer.",
  "details": "The function takes a format string and a variable argument list, and uses the `vsnprintf` function to format the message. It then stores the formatted message in a circular buffer, along with other metadata such as the log level, prefix, and timestamp. If the buffer is full, it expands the buffer by doubling its size.",
  "rationale": "The function is implemented this way to allow for efficient and thread-safe logging. The use of a circular buffer allows for a fixed amount of memory to be used for logging, and the use of a mutex ensures that only one thread can access the buffer at a time.",
  "performance": "The function has a time complexity of O(n), where n is the length of the format string. The use of `vsnprintf` and `std::stringstream` can be slow for large format strings. However, the function is designed to be used in a logging context, where the format string is typically short and the number of log messages is relatively small.",
  "hidden_insights": [
    "The function uses a `std::lock_guard` to ensure that the mutex is released when an exception is thrown.",
    "The function uses `va_copy` to create a copy of the variable argument list, which is necessary because `vsnprintf` modifies the original list.",
    "The function uses `std::stringstream` to implement a hack for bolding arguments in the format string."
  ],
  "where_used": [
    "Logging module",
    "Worker thread"
  ],
  "tags": [
    "logging",
    "circular buffer",
    "mutex",
    "vsnprintf",
    "std::stringstream"
  ],
  "markdown": "### Log Message Formatter
This function formats a log message using the provided format string and arguments, and stores it in a circular buffer.

#### Details
The function takes a format string and a variable argument list, and uses the `vsnprintf` function to format the message. It then stores the formatted message in a circular buffer, along with other metadata such as the log level, prefix, and timestamp. If the buffer is full, it expands the buffer by doubling its size.

#### Rationale
The function is implemented this way to allow for efficient and thread-safe logging. The use of a circular buffer allows for a fixed amount of memory to be used for logging, and the use of a mutex ensures that only one thread can access the buffer at a time.

#### Performance
The function has a time complexity of O(n), where n is the length of the format string. The use of `vsnprintf` and `std::stringstream` can be slow for large format strings. However, the function is designed to be used in a logging context, where the format string is typically short and the number of log messages is relatively small."
}
```
