# peg-parser.cpp__json_bool

```json
{
  "title": "json_bool",
  "summary": "Creates a PEG parser rule for JSON boolean values.",
  "details": "This function generates a PEG parser rule named 'json-bool' that matches JSON boolean values. It uses a sequence of a choice between 'true' and 'false' literals, followed by optional whitespace.",
  "rationale": "The use of a sequence and choice allows for efficient parsing of JSON boolean values, which can be either 'true' or 'false'.",
  "performance": "The use of a sequence and choice can improve parsing performance by reducing the number of possible parsing paths.",
  "hidden_insights": [
    "The use of a lambda function to define the parsing rule allows for easy modification of the rule without changing the surrounding code.",
    "The 'space()' function is used to match optional whitespace, which can improve parsing accuracy."
  ],
  "where_used": [
    "peg-parser.cpp"
  ],
  "tags": [
    "PEG parser",
    "JSON",
    "boolean",
    "rule"
  ],
  "markdown": "### json_bool\n\nCreates a PEG parser rule for JSON boolean values.\n\nThis function generates a PEG parser rule named 'json-bool' that matches JSON boolean values. It uses a sequence of a choice between 'true' and 'false' literals, followed by optional whitespace.\n\n#### Rationale\n\nThe use of a sequence and choice allows for efficient parsing of JSON boolean values, which can be either 'true' or 'false'.\n\n#### Performance\n\nThe use of a sequence and choice can improve parsing performance by reducing the number of possible parsing paths.\n\n#### Hidden Insights\n\n* The use of a lambda function to define the parsing rule allows for easy modification of the rule without changing the surrounding code.\n* The 'space()' function is used to match optional whitespace, which can improve parsing accuracy.\n\n#### Where Used\n\n* peg-parser.cpp"
}
