# peg-parser.cpp__single_quoted_string

```json
{
  "title": "single_quoted_string",
  "summary": "Creates a rule for parsing a single-quoted string.",
  "details": "This function returns a rule for parsing a single-quoted string, which is a sequence of a single quote, any string content not including a single quote, and another single quote, followed by optional whitespace.",
  "rationale": "The function uses a lambda function to define the sequence of characters that make up a single-quoted string, allowing for a concise and readable implementation.",
  "performance": "The performance of this function is likely to be good, as it uses a sequence of simple operations to parse the input string.",
  "hidden_insights": [
    "The use of a lambda function allows for a concise implementation of the sequence of characters that make up a single-quoted string.",
    "The function assumes that the input string is well-formed and does not contain any unbalanced quotes."
  ],
  "where_used": [
    "peg_parser_builder.cpp",
    "peg_parser.cpp"
  ],
  "tags": [
    "PEG parser",
    "single-quoted string",
    "rule creation"
  ],
  "markdown": "### single_quoted_string
Creates a rule for parsing a single-quoted string.
#### Details
This function returns a rule for parsing a single-quoted string, which is a sequence of a single quote, any string content not including a single quote, and another single quote, followed by optional whitespace.
#### Rationale
The function uses a lambda function to define the sequence of characters that make up a single-quoted string, allowing for a concise and readable implementation.
#### Performance
The performance of this function is likely to be good, as it uses a sequence of simple operations to parse the input string.
#### Where Used
* peg_parser_builder.cpp
* peg_parser.cpp
#### Tags
* PEG parser
* single-quoted string
* rule creation"
}
