# common.cpp__fs_validate_filename

Tags: #loop

```json
{
  "title": "Filename Validation",
  "summary": "This function validates a filename according to a set of rules, including length, character set, and forbidden characters.",
  "details": "The function checks the filename for various conditions, such as length, presence of forbidden characters, and invalid Unicode codepoints. It also checks for subdirectories, leading/trailing whitespace, and invalid path separators.",
  "rationale": "The function is implemented this way to ensure that filenames are valid and safe to use on various operating systems, including Linux and Windows.",
  "performance": "The function has a time complexity of O(n), where n is the length of the filename, due to the use of a while loop and string operations.",
  "hidden_insights": [
    "The function uses the `utf8_parse_result` struct to parse Unicode codepoints from the filename.",
    "The function checks for forbidden Unicode codepoints, including control characters, surrogate pairs, and replacement characters.",
    "The function rejects filenames with leading or trailing whitespace, as well as filenames with trailing periods."
  ],
  "where_used": [
    "Filesystem-related modules",
    "Filename validation utilities"
  ],
  "tags": [
    "filename validation",
    "utf-8",
    "unicode",
    "filesystem"
  ],
  "markdown": "### Filename Validation
This function validates a filename according to a set of rules, including length, character set, and forbidden characters.

#### Rules
* Length: The filename must be between 1 and 255 characters long.
* Character set: The filename must only contain valid Unicode codepoints.
* Forbidden characters: The filename must not contain certain forbidden characters, including control characters, surrogate pairs, and replacement characters.
* Subdirectories: The filename must not contain subdirectory separators (e.g. `/`, `\`).
* Leading/trailing whitespace: The filename must not have leading or trailing whitespace.
* Invalid path separators: The filename must not contain invalid path separators (e.g. `:`).

#### Example Use Cases
* Valid filename: `example.txt`
* Invalid filename: `example.txt/` (contains subdirectory separator)
* Invalid filename: `example.txt ` (contains leading whitespace)
* Invalid filename: `example.txt.` (contains trailing period)
"
}
```
