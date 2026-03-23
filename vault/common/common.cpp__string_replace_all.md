# common.cpp__string_replace_all

Tags: #loop

```json
{
  "title": "string_replace_all",
  "summary": "Replaces all occurrences of a substring in a string with another substring.",
  "details": "This function iteratively finds all occurrences of the search string in the input string and replaces them with the replace string. It uses a builder string to efficiently construct the modified string.",
  "rationale": "The function uses a builder string to avoid reallocations and improve performance. It also checks if the search string is empty to avoid unnecessary iterations.",
  "performance": "The function has a time complexity of O(n*m), where n is the length of the input string and m is the length of the search string. It uses a reserve to minimize reallocations.",
  "hidden_insights": [
    "The function uses std::move to transfer ownership of the builder string to the input string, avoiding a copy.",
    "The function uses reserve to minimize reallocations of the builder string."
  ],
  "where_used": [
    "string manipulation utilities",
    "text processing modules"
  ],
  "tags": [
    "string manipulation",
    "search and replace",
    "performance optimization"
  ],
  "markdown": "### string_replace_all
Replaces all occurrences of a substring in a string with another substring.

#### Purpose
This function is used to efficiently replace all occurrences of a substring in a string with another substring.

#### Implementation
The function uses a builder string to iteratively find and replace occurrences of the search string.

#### Performance Considerations
The function has a time complexity of O(n*m), where n is the length of the input string and m is the length of the search string. It uses a reserve to minimize reallocations.

#### Usage
This function can be used in string manipulation utilities and text processing modules."
}
