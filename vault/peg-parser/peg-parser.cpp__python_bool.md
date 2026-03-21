# peg-parser.cpp__python_bool

```json
{
  "title": "python_bool",
  "summary": "Creates a PEG parser rule for Python boolean values.",
  "details": "This function generates a PEG parser rule named 'python-bool' that matches Python boolean values. It uses a sequence of a choice between 'True' and 'False' literals, followed by a space.",
  "rationale": "The use of a choice between literals is a common pattern in PEG parsers for matching specific values. The space after the boolean value is likely to handle cases where the value is followed by other characters.",
  "performance": "The performance of this function is likely to be good, as it uses a simple and efficient PEG parser rule. However, the actual performance may depend on the specific use case and the input data.",
  "hidden_insights": [
    "The use of a lambda function to define the parser rule allows for a concise and expressive syntax.",
    "The 'space' function is likely a utility function that matches one or more whitespace characters, which is a common pattern in PEG parsers."
  ],
  "where_used": [
    "peg_parser_builder.cpp",
    "python_parser.cpp"
  ],
  "tags": [
    "PEG parser",
    "Python",
    "boolean",
    "rule"
  ],
  "markdown": "### python_bool\n\nCreates a PEG parser rule for Python boolean values.\n\nThis function generates a PEG parser rule named 'python-bool' that matches Python boolean values. It uses a sequence of a choice between 'True' and 'False' literals, followed by a space.\n\n#### Rationale\n\nThe use of a choice between literals is a common pattern in PEG parsers for matching specific values. The space after the boolean value is likely to handle cases where the value is followed by other characters.\n\n#### Performance\n\nThe performance of this function is likely to be good, as it uses a simple and efficient PEG parser rule. However, the actual performance may depend on the specific use case and the input data.\n\n#### Where Used\n\n* peg_parser_builder.cpp\n* python_parser.cpp"
}
