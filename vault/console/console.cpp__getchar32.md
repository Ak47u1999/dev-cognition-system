# console.cpp__getchar32

Tags: #loop #memory

```json
{
  "title": "getchar32 Function",
  "summary": "The getchar32 function reads a single character from the console and returns it as a char32_t. It handles surrogate pairs and special keys.",
  "details": "The getchar32 function is a C function that reads a single character from the console and returns it as a char32_t. It is designed to handle surrogate pairs, which are pairs of Unicode characters that represent a single code point. The function also handles special keys such as arrow keys, home, end, and delete.",
  "rationale": "The function is implemented this way to handle the complexities of Unicode characters and special keys. The use of surrogate pairs and special key handling allows the function to accurately read input from the console.",
  "performance": "The function has a time complexity of O(1), making it efficient for reading single characters from the console. However, the use of while loops and conditional statements may introduce some overhead.",
  "hidden_insights": [
    "The function uses the GetStdHandle function to get a handle to the console input buffer.",
    "The function uses the ReadConsoleInputW function to read a single input record from the console input buffer.",
    "The function uses the wint_t type to represent wide characters."
  ],
  "where_used": [
    "console.cpp",
    "main.cpp",
    "input.cpp"
  ],
  "tags": [
    "console",
    "input",
    "unicode",
    "surrogate pairs",
    "special keys"
  ],
  "markdown": "### getchar32 Function
The getchar32 function reads a single character from the console and returns it as a char32_t.
#### Purpose
The purpose of the getchar32 function is to accurately read input from the console, handling surrogate pairs and special keys.
#### Implementation
The function uses the GetStdHandle function to get a handle to the console input buffer, and then uses the ReadConsoleInputW function to read a single input record from the console input buffer.
#### Handling Surrogate Pairs
The function handles surrogate pairs by checking if the input character is a high surrogate, and if so, it waits for the next input character to be a low surrogate. If the next input character is a low surrogate, it returns the combined code point.
#### Handling Special Keys
The function handles special keys such as arrow keys, home, end, and delete by checking the virtual key code and control key state.
#### Performance
The function has a time complexity of O(1), making it efficient for reading single characters from the console.
#### Where Used
The getchar32 function is used in the console.cpp, main.cpp, and input.cpp files.
#### Tags
console, input, unicode, surrogate pairs, special keys"
}
