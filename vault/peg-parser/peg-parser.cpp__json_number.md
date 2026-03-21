# peg-parser.cpp__json_number

```json
{
  "title": "json_number PEG Rule",
  "summary": "The json_number function defines a PEG (Parsing Expression Grammar) rule for parsing JSON numbers.",
  "details": "This function uses a combination of character classes, sequences, and choices to define the structure of a JSON number. It supports integers, fractions, and exponents, as well as an optional negative sign. The rule also includes a negative lookahead to prevent premature commits of partial numbers.",
  "rationale": "The use of a negative lookahead is necessary to prevent premature commits of partial numbers. This is particularly important in partial mode, where the parser may not have enough information to commit the entire number.",
  "performance": "The performance of this function should be good, as it uses a combination of precomputed character classes and sequences to define the rule. However, the use of a negative lookahead may introduce some overhead.",
  "hidden_insights": [
    "The use of a negative lookahead is a common technique in PEG parsing to prevent premature commits of partial matches.",
    "The `NEED_MORE` state in the `chars` function is used to indicate that the parser needs more input to commit the match."
  ],
  "where_used": [
    "The `json_number` rule is likely used in a JSON parser to parse numbers in JSON data.",
    "It may also be used in other contexts where JSON numbers need to be parsed."
  ],
  "tags": [
    "PEG parsing",
    "JSON parsing",
    "negative lookahead",
    "partial mode"
  ],
  "markdown": "## json_number PEG Rule
The `json_number` function defines a PEG rule for parsing JSON numbers.

### Structure
The rule supports integers, fractions, and exponents, as well as an optional negative sign.

### Negative Lookahead
The rule includes a negative lookahead to prevent premature commits of partial numbers.

### Performance
The performance of this function should be good, as it uses a combination of precomputed character classes and sequences to define the rule.

### Where Used
The `json_number` rule is likely used in a JSON parser to parse numbers in JSON data."
}
