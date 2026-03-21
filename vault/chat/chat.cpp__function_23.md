# chat.cpp__function_23

Tags: #loop

```json
{
  "title": "build_chat_peg_parser",
  "summary": "Builds a parser for chat input in Functionary v3.2 format, handling normal content and tool calls.",
  "details": "The function creates a parser that can handle two types of input: normal content and tool calls. Normal content is parsed until the end of the input or the next tool call, while tool calls are parsed until the next tool call or the end of the input. The parser is built using a peg parser and can handle parallel tool calls.",
  "rationale": "The function is implemented this way to handle the specific format of Functionary v3.2 input and to allow for parallel tool calls.",
  "performance": "The performance of the function is likely to be good due to the use of a peg parser, which is a efficient way to parse structured input.",
  "hidden_insights": [
    "The function uses a peg parser, which is a type of parser that is well-suited to parsing structured input.",
    "The function can handle parallel tool calls, which allows it to parse input that contains multiple tool calls."
  ],
  "where_used": [
    "chat_parser.cpp"
  ],
  "tags": [
    "peg_parser",
    "chat_input",
    "functionary_v3_2"
  ],
  "markdown": "### build_chat_peg_parser
Builds a parser for chat input in Functionary v3.2 format, handling normal content and tool calls.
#### Details
The function creates a parser that can handle two types of input: normal content and tool calls. Normal content is parsed until the end of the input or the next tool call, while tool calls are parsed until the next tool call or the end of the input.
#### Rationale
The function is implemented this way to handle the specific format of Functionary v3.2 input and to allow for parallel tool calls.
#### Performance
The performance of the function is likely to be good due to the use of a peg parser, which is a efficient way to parse structured input.
#### Hidden Insights
* The function uses a peg parser, which is a type of parser that is well-suited to parsing structured input.
* The function can handle parallel tool calls, which allows it to parse input that contains multiple tool calls.
#### Where Used
* chat_parser.cpp
#### Tags
* peg_parser
* chat_input
* functionary_v3_2"
}
