# console.cpp__delete_at_cursor

Tags: #loop #memory

```json
{
  "title": "delete_at_cursor",
  "summary": "Deletes a character at the current cursor position in a line, updating the line and widths vectors accordingly.",
  "details": "This function is responsible for deleting a character at the current cursor position in a line. It updates the line and widths vectors by erasing the character at the specified position and adjusting the widths of the remaining characters. It also updates the cursor position by moving it to the left by the total width of the deleted character and the spaces inserted to maintain the correct formatting.",
  "rationale": "The function is implemented this way to ensure that the line and widths vectors are updated correctly after deleting a character. It uses the `next_utf8_char_pos` function to determine the position of the next character in the line, and the `put_codepoint` function to insert spaces to maintain the correct formatting.",
  "performance": "The function has a time complexity of O(n), where n is the number of characters in the line. This is because it needs to iterate over the remaining characters in the line to update their widths.",
  "hidden_insights": [
    "The function uses the `next_utf8_char_pos` function to determine the position of the next character in the line, which is necessary to handle Unicode characters correctly.",
    "The function uses the `put_codepoint` function to insert spaces to maintain the correct formatting, which is necessary to ensure that the line remains correctly formatted after deleting a character."
  ],
  "where_used": [
    "console.cpp"
  ],
  "tags": [
    "delete character",
    "cursor position",
    "line formatting"
  ],
  "markdown": "### delete_at_cursor
Deletes a character at the current cursor position in a line, updating the line and widths vectors accordingly.
#### Parameters
* `line`: the line to delete a character from
* `widths`: the vector of character widths
* `char_pos`: the current cursor position
* `byte_pos`: the current byte position
#### Returns
* None
#### Notes
* This function is responsible for updating the line and widths vectors after deleting a character.
* It uses the `next_utf8_char_pos` function to determine the position of the next character in the line.
* It uses the `put_codepoint` function to insert spaces to maintain the correct formatting."
}
