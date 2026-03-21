# peg-parser.cpp__add_parser

{
  "title": "add_parser Function",
  "summary": "Adds a new parser to the arena and returns its unique identifier.",
  "details": "This function takes a parser variant as input, adds it to the end of the parsers vector, and returns the index of the newly added parser. The parser is moved into the vector to avoid unnecessary copies.",
  "rationale": "The function uses move semantics to efficiently transfer ownership of the parser to the vector, reducing memory allocation and deallocation overhead.",
  "performance": "The function has a time complexity of O(1) since it only involves a single push operation at the end of the vector.",
  "hidden_insights": [
    "The use of move semantics can improve performance by reducing the number of copies made.",
    "The function assumes that the input parser is a valid variant, but does not perform any validation."
  ],
  "where_used": [
    "common_peg_arena class",
    "parser management"
  ],
  "tags": [
    "parser",
    "arena",
    "move semantics"
  ],
  "markdown": "# add_parser Function\n\nAdds a new parser to the arena and returns its unique identifier.\n\n## Details\n\nThis function takes a parser variant as input, adds it to the end of the parsers vector, and returns the index of the newly added parser. The parser is moved into the vector to avoid unnecessary copies.\n\n## Rationale\n\nThe function uses move semantics to efficiently transfer ownership of the parser to the vector, reducing memory allocation and deallocation overhead.\n\n## Performance\n\nThe function has a time complexity of O(1) since it only involves a single push operation at the end of the vector.\n\n## Hidden Insights\n\n* The use of move semantics can improve performance by reducing the number of copies made.\n* The function assumes that the input parser is a valid variant, but does not perform any validation.\n\n## Where Used\n\n* common_peg_arena class\n* parser management"
