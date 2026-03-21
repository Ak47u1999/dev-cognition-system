# download.cpp__function_19

Tags: #recursion

```json
{
  "title": "Digest Validation Function",
  "summary": "A helper function to validate and normalize OCI digests.",
  "details": "This function takes a string representing an OCI digest and checks if it matches the expected format. It uses a regular expression to validate the format and then normalizes the hex characters to lowercase. The function throws a runtime error if the digest is invalid.",
  "rationale": "The function is implemented as a lambda function to keep it concise and focused on a single task. The use of a regular expression allows for easy extension to support other algorithms in the future.",
  "performance": "The function has a time complexity of O(n), where n is the length of the input string. This is because the regular expression match and string transformation operations have a linear time complexity.",
  "hidden_insights": [
    "The function uses a static regular expression object to avoid compiling the regex pattern every time it's used.",
    "The use of `std::tolower` to normalize the hex characters is more efficient than using a loop or a `std::string` constructor."
  ],
  "where_used": [
    "OCI manifest validation module",
    "Container image download function"
  ],
  "tags": [
    "OCI",
    "digest validation",
    "regular expression",
    "string normalization"
  ],
  "markdown": "### Digest Validation Function
A helper function to validate and normalize OCI digests.

#### Purpose
The purpose of this function is to validate and normalize OCI digests.

#### Implementation
The function uses a regular expression to validate the format of the digest and then normalizes the hex characters to lowercase.

#### Example Use Case
```cpp
std::string digest = "sha256:1234567890abcdef1234567890abcdef";
try {
    std::string normalized = validate_oci_digest(digest);
    // use the normalized digest
} catch (const std::runtime_error& e) {
    // handle invalid digest error
}
```"
