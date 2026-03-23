# common.cpp__utf8_to_wstring

```json
{
  "title": "utf8_to_wstring",
  "summary": "Converts a UTF-8 encoded string to a wide string.",
  "details": "This function takes a UTF-8 encoded string and returns its equivalent wide string representation. It uses the MultiByteToWideChar function to perform the conversion.",
  "rationale": "The function is implemented this way to provide a straightforward conversion from UTF-8 to wide string, which is commonly used in Windows API calls.",
  "performance": "The function has a time complexity of O(n), where n is the size of the input string. This is because it uses a loop to iterate over the input string.",
  "hidden_insights": [
    "The function uses the MultiByteToWideChar function, which is a Windows API function that performs the conversion from multi-byte character sets to wide character sets.",
    "The function returns an empty wide string if the input string is empty or if the conversion fails."
  ],
  "where_used": [
    "Windows API calls",
    "C++ applications that require wide string support"
  ],
  "tags": [
    "UTF-8",
    "Wide String",
    "Conversion",
    "Windows API"
  ],
  "markdown": "### utf8_to_wstring
Converts a UTF-8 encoded string to a wide string.

#### Description
This function takes a UTF-8 encoded string and returns its equivalent wide string representation.

#### Parameters
* `str`: The UTF-8 encoded string to be converted.

#### Returns
The wide string representation of the input string.

#### Notes
The function returns an empty wide string if the input string is empty or if the conversion fails."
}
