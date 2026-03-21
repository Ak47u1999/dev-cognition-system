# chat.cpp__function_25

Tags: #loop

```json
{
  "title": "build_chat_peg_parser",
  "summary": "This function builds a parser for chat input using the PEG (Parsing Expression Grammar) parser generator. It supports the Kimi K2 Thinking format and tool calls.",
  "details": "The function takes a lambda function as an argument, which is used to build the parser. It extracts the reasoning and content from the input, and then builds tool call parsers for each available function. The tool calls section is also parsed, and the parser is wrapped for generation prompts.",
  "rationale": "The function is implemented this way to support the Kimi K2 Thinking format and tool calls, which are specific to the chat input. The use of PEG parser generator allows for efficient and flexible parsing of the input.",
  "performance": "The performance of this function is likely to be good, as it uses a parser generator to build the parser. However, the complexity of the parser and the input data may affect performance.",
  "hidden_insights": [
    "The function uses a lambda function to build the parser, which allows for flexible and efficient parsing of the input.",
    "The use of PEG parser generator allows for efficient and flexible parsing of the input.",
    "The function supports the Kimi K2 Thinking format and tool calls, which are specific to the chat input."
  ],
  "where_used": [
    "chat_input_parser.cpp",
    "chat_generator.cpp"
  ],
  "tags": [
    "PEG parser generator",
    "chat input",
    "Kimi K2 Thinking format",
    "tool calls"
  ],
  "markdown": "### build_chat_peg_parser
This function builds a parser for chat input using the PEG (Parsing Expression Grammar) parser generator.
#### Purpose
The purpose of this function is to support the Kimi K2 Thinking format and tool calls in the chat input.
#### Implementation
The function takes a lambda function as an argument, which is used to build the parser. It extracts the reasoning and content from the input, and then builds tool call parsers for each available function. The tool calls section is also parsed, and the parser is wrapped for generation prompts.
#### Performance
The performance of this function is likely to be good, as it uses a parser generator to build the parser. However, the complexity of the parser and the input data may affect performance.
#### Hidden Insights
* The function uses a lambda function to build the parser, which allows for flexible and efficient parsing of the input.
* The use of PEG parser generator allows for efficient and flexible parsing of the input.
* The function supports the Kimi K2 Thinking format and tool calls, which are specific to the chat input.
#### Where Used
* chat_input_parser.cpp
* chat_generator.cpp
#### Tags
* PEG parser generator
* chat input
* Kimi K2 Thinking format
* tool calls"
}
