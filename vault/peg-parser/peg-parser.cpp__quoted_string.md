# peg-parser.cpp__quoted_string

```json
{
  "title": "quoted_string",
  "summary": "Builds a PEG parser rule for quoted strings.",
  "details": "This function creates a PEG parser rule named 'quoted-string' that matches either a double-quoted or single-quoted string. It uses a choice combinator to allow for either type of quoting.",
  "rationale": "The use of a choice combinator allows for flexibility in the parser and makes it easier to add support for additional types of quoting in the future.",
  "performance": "The performance of this function is likely to be good, as it only involves creating a new parser rule and does not perform any complex operations.",
  "hidden_insights": [
    "The use of a lambda function to create the choice combinator allows for the capture of the current object's context, making it easier to access other parser rules."
  ],
  "where_used": [
    "peg-parser-builder.cpp"
  ],
  "tags": [
    "PEG parser",
    "quoted string",
    "choice combinator"
  ],
  "markdown": "## quoted_string\n\nBuilds a PEG parser rule for quoted strings.\n\nThis function creates a PEG parser rule named 'quoted-string' that matches either a double-quoted or single-quoted string. It uses a choice combinator to allow for either type of quoting.\n\n### Rationale\n\nThe use of a choice combinator allows for flexibility in the parser and makes it easier to add support for additional types of quoting in the future.\n\n### Performance\n\nThe performance of this function is likely to be good, as it only involves creating a new parser rule and does not perform any complex operations.\n\n### Hidden Insights\n\n* The use of a lambda function to create the choice combinator allows for the capture of the current object's context, making it easier to access other parser rules."
}
