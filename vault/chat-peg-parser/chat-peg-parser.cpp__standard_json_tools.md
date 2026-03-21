# chat-peg-parser.cpp__standard_json_tools

```json
{
  "title": "standard_json_tools",
  "summary": "Constructs a PEG parser for standard JSON tools based on the input JSON layout mode.",
  "details": "This function takes in various parameters to determine the layout mode of the input JSON and dispatches to the appropriate builder to construct a PEG parser. It handles different cases such as function-is-key, nested keys, and flat keys.",
  "rationale": "The function is implemented this way to accommodate different JSON layout modes and provide flexibility in constructing the PEG parser.",
  "performance": "The function has a time complexity of O(n), where n is the number of tools in the input JSON. This is because it iterates over the tools to determine the layout mode and construct the PEG parser.",
  "hidden_insights": [
    "The function uses a dispatch pattern to handle different layout modes, making it more flexible and maintainable.",
    "The use of `optional(section)` allows for optional tool calls, which can improve performance in certain scenarios."
  ],
  "where_used": [
    "chat_peg_builder"
  ],
  "tags": [
    "PEG parser",
    "JSON layout mode",
    "dispatch pattern",
    "optional tool calls"
  ],
  "markdown": "### standard_json_tools
Constructs a PEG parser for standard JSON tools based on the input JSON layout mode.

#### Parameters
* `section_start`: The start marker of the section.
* `section_end`: The end marker of the section.
* `tools`: The input JSON tools.
* `parallel_tool_calls`: Whether to allow parallel tool calls.
* `force_tool_calls`: Whether to force tool calls.
* `name_key`: The key for the tool name.
* `args_key`: The key for the tool arguments.
* `array_wrapped`: Whether to wrap the tool calls in an array.
* `function_is_key`: Whether the function is the key.
* `call_id_key`: The key for the call ID.
* `gen_call_id_key`: The key for the generated call ID.
* `parameters_order`: The order of the parameters.

#### Returns
A PEG parser for the standard JSON tools.
"
}
