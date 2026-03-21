# peg-parser.cpp__marker

{
  "title": "marker() function",
  "summary": "Creates a parser for marker characters (<>) or ([])",
  "details": "The marker() function returns a common PEG parser that matches either sharp bracket (<>) or square bracket ([]) markers. It uses the choice() function to combine two parsers: sharp_bracket_parser and square_bracket_parser. The sharp_bracket_parser matches a literal '<' followed by any characters until a '>', while the square_bracket_parser matches a literal '[' followed by any characters until a ']'.",
  "rationale": "This implementation is likely used to parse marker characters in a text, such as HTML tags or JSON objects.",
  "performance": "The performance of this function is likely to be good, as it uses a combination of literal and until parsers, which are efficient. However, the performance may degrade if the input text is very large, as the until parser may need to scan the entire text.",
  "hidden_insights": [
    "The until parser is used to match any characters until a specific character, which can be more efficient than using a recursive parser.",
    "The choice function is used to combine two parsers, which allows for more flexibility in parsing different types of input."
  ],
  "where_used": [
    "HTML parser",
    "JSON parser",
    "text processing module"
  ],
  "tags": [
    "PEG parser",
    "marker characters",
    "choice function",
    "until parser"
  ],
  "markdown": "# marker() function\n\nCreates a parser for marker characters (<>) or ([])\n\n## Details\n\nThe marker() function returns a common PEG parser that matches either sharp bracket (<>) or square bracket ([]) markers. It uses the choice() function to combine two parsers: sharp_bracket_parser and square_bracket_parser.\n\n## Rationale\n\nThis implementation is likely used to parse marker characters in a text, such as HTML tags or JSON objects.\n\n## Performance\n\nThe performance of this function is likely to be good, as it uses a combination of literal and until parsers, which are efficient. However, the performance may degrade if the input text is very large, as the until parser may need to scan the entire text.\n\n## Hidden Insights\n\n* The until parser is used to match any characters until a specific character, which can be more efficient than using a recursive parser.\n* The choice function is used to combine two parsers, which allows for more flexibility in parsing different types of input.\n\n## Where Used\n\n* HTML parser\n* JSON parser\n* text processing module\n\n## Tags\n\n* PEG parser\n* marker characters\n* choice function\n* until parser"
