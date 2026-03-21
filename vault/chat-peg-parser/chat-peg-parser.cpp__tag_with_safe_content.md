# chat-peg-parser.cpp__tag_with_safe_content

```json
{
  "title": "tag_with_safe_content",
  "summary": "Constructs a PEG parser for safely parsing content within a tag.",
  "details": "This function generates a PEG parser that safely parses content within a tag by ignoring a specified marker. It returns a parser that matches zero or more occurrences of the specified parser or a parser that matches the tag name followed by any content except the marker.",
  "rationale": "The function uses a PEG parser to safely parse content within a tag, allowing for flexible and efficient parsing of complex data structures.",
  "performance": "The function uses a recursive approach to generate the PEG parser, which may have performance implications for large inputs.",
  "hidden_insights": [
    "The function uses the `negate` function to invert the meaning of the `literal` function, allowing it to match any character except the specified marker.",
    "The `until` function is used to match any character until the specified marker is encountered."
  ],
  "where_used": [
    "chat_peg_builder module",
    "common_peg_parser class"
  ],
  "tags": [
    "PEG parser",
    "safe parsing",
    "content parsing"
  ],
  "markdown": "### tag_with_safe_content\n\nConstructs a PEG parser for safely parsing content within a tag.\n\n#### Summary\n\nThis function generates a PEG parser that safely parses content within a tag by ignoring a specified marker.\n\n#### Details\n\nThe function returns a parser that matches zero or more occurrences of the specified parser or a parser that matches the tag name followed by any content except the marker.\n\n#### Rationale\n\nThe function uses a PEG parser to safely parse content within a tag, allowing for flexible and efficient parsing of complex data structures.\n\n#### Performance\n\nThe function uses a recursive approach to generate the PEG parser, which may have performance implications for large inputs.\n\n#### Hidden Insights\n\n* The function uses the `negate` function to invert the meaning of the `literal` function, allowing it to match any character except the specified marker.\n* The `until` function is used to match any character until the specified marker is encountered.\n\n#### Where Used\n\n* chat_peg_builder module\n* common_peg_parser class\n\n#### Tags\n\n* PEG parser\n* safe parsing\n* content parsing"
}
