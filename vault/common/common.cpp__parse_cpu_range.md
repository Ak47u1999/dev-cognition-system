# common.cpp__parse_cpu_range

Tags: #ggml #loop

```json
{
  "title": "parse_cpu_range",
  "summary": "Parses a CPU range string and sets a boolean mask accordingly.",
  "details": "This function takes a string representing a CPU range and a boolean array as input. It parses the range string to extract the start and end indices, and then sets the corresponding elements in the boolean array to true. The function returns true if the parsing is successful, and false otherwise.",
  "rationale": "The function is implemented this way to provide a simple and efficient way to parse CPU range strings and set boolean masks. The use of std::stoull for parsing the indices ensures that the function can handle a wide range of input values.",
  "performance": "The function has a time complexity of O(n), where n is the number of elements in the boolean array. This is because the function iterates over the array once to set the corresponding elements to true.",
  "hidden_insights": [
    "The function assumes that the input range string is in the format [<start>]-[<end>].",
    "The function uses std::stoull to parse the indices, which can throw an exception if the input string is not a valid integer.",
    "The function checks if the start and end indices are within the bounds of the boolean array to prevent out-of-bounds access."
  ],
  "where_used": [
    "cpu_range_parser.cpp",
    "thread_manager.cpp"
  ],
  "tags": [
    "cpu_range",
    "boolean_mask",
    "threading"
  ],
  "markdown": "### parse_cpu_range
Parses a CPU range string and sets a boolean mask accordingly.

#### Parameters
* `range`: A string representing a CPU range.
* `boolmask`: A boolean array to be set accordingly.

#### Returns
* `true` if the parsing is successful, `false` otherwise.

#### Notes
The function assumes that the input range string is in the format [<start>]-[<end>]. The function uses `std::stoull` to parse the indices, which can throw an exception if the input string is not a valid integer. The function checks if the start and end indices are within the bounds of the boolean array to prevent out-of-bounds access."
}
