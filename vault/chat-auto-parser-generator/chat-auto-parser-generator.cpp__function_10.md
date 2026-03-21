# chat-auto-parser-generator.cpp__function_10

```json
{
  "title": "build_tool_parser_json_native",
  "summary": "Builds a PEG parser for tool data in JSON format, handling various formatting options and content wrappers.",
  "details": "This function generates a PEG parser for tool data in JSON format, taking into account various formatting options and content wrappers. It uses the `standard_json_tools` function to create the parser and then handles content wrappers if present. The parser is built with the `reasoning_parser` and `tools_parser` components.",
  "rationale": "The function is implemented this way to provide flexibility in handling different formatting options and content wrappers. It uses a modular approach to build the parser, allowing for easy customization and extension.",
  "performance": "The function has a time complexity of O(n), where n is the size of the input data, due to the use of string concatenation and parsing operations. However, the performance impact is likely to be negligible for most use cases.",
  "hidden_insights": [
    "The function uses the `format` object to store formatting options, which allows for easy customization and extension.",
    "The `standard_json_tools` function is used to create the parser, which provides a pre-built implementation for common JSON parsing tasks."
  ],
  "where_used": [
    "chat-auto-parser-generator.cpp"
  ],
  "tags": [
    "PEG parser",
    "JSON",
    "formatting options",
    "content wrappers"
  ],
  "markdown": "### build_tool_parser_json_native
Builds a PEG parser for tool data in JSON format, handling various formatting options and content wrappers.
#### Details
This function generates a PEG parser for tool data in JSON format, taking into account various formatting options and content wrappers. It uses the `standard_json_tools` function to create the parser and then handles content wrappers if present.
#### Rationale
The function is implemented this way to provide flexibility in handling different formatting options and content wrappers. It uses a modular approach to build the parser, allowing for easy customization and extension.
#### Performance
The function has a time complexity of O(n), where n is the size of the input data, due to the use of string concatenation and parsing operations. However, the performance impact is likely to be negligible for most use cases.
#### Hidden Insights
* The function uses the `format` object to store formatting options, which allows for easy customization and extension.
* The `standard_json_tools` function is used to create the parser, which provides a pre-built implementation for common JSON parsing tasks.
#### Where Used
* chat-auto-parser-generator.cpp
#### Tags
* PEG parser
* JSON
* formatting options
* content wrappers"
}
