# json-schema-to-grammar.cpp__check_errors

```json
{
  "title": "Error Handling Function",
  "summary": "Checks for errors and warnings after JSON schema conversion and handles them accordingly.",
  "details": "This function checks if there are any errors or warnings after converting a JSON schema. If errors are found, it throws an invalid_argument exception with a message containing the error details. If warnings are found, it prints them to the standard error stream.",
  "rationale": "The function is implemented this way to provide immediate feedback to the user in case of errors and to allow for warnings to be printed to the standard error stream.",
  "performance": "This function has a time complexity of O(n), where n is the number of errors or warnings, as it iterates over the _errors and _warnings containers.",
  "hidden_insights": [
    "The function uses string_join to concatenate the error messages into a single string.",
    "The function uses fprintf to print warnings to the standard error stream."
  ],
  "where_used": [
    "json_schema_converter.cpp"
  ],
  "tags": [
    "error handling",
    "json schema conversion",
    "warning handling"
  ],
  "markdown": "### Error Handling Function\n\nChecks for errors and warnings after JSON schema conversion and handles them accordingly.\n\n#### Details\nThis function checks if there are any errors or warnings after converting a JSON schema. If errors are found, it throws an invalid_argument exception with a message containing the error details. If warnings are found, it prints them to the standard error stream.\n\n#### Rationale\nThe function is implemented this way to provide immediate feedback to the user in case of errors and to allow for warnings to be printed to the standard error stream.\n\n#### Performance\nThis function has a time complexity of O(n), where n is the number of errors or warnings, as it iterates over the _errors and _warnings containers.\n\n#### Hidden Insights\n* The function uses string_join to concatenate the error messages into a single string.\n* The function uses fprintf to print warnings to the standard error stream.\n\n#### Where Used\n* json_schema_converter.cpp"
}
