# chat.cpp__common_chat_templates_apply_legacy

Tags: #ggml #loop #recursion

```json
{
  "title": "Legacy Chat Template Application",
  "summary": "This function applies a legacy chat template to a given set of chat messages, handling buffer resizing and error checking.",
  "details": "The function iterates over the input messages, concatenating their content parts and storing them in a vector. It then applies the chat template to the concatenated content, resizing the buffer if necessary. The function returns a common_chat_params object containing the applied template and grammar.",
  "rationale": "The function is implemented this way to handle legacy chat templates, which may not support the new buffer resizing mechanism.",
  "performance": "The function has a time complexity of O(n), where n is the number of input messages. The buffer resizing operation may incur additional overhead.",
  "hidden_insights": [
    "The function uses a vector to store the concatenated content, which allows for efficient resizing of the buffer.",
    "The function checks the result of the chat template application twice to ensure that the buffer is large enough."
  ],
  "where_used": [
    "common_chat_templates_apply_legacy function",
    "common_chat_templates_apply function"
  ],
  "tags": [
    "chat",
    "template",
    "legacy",
    "buffer",
    "resizing"
  ],
  "markdown": "### Legacy Chat Template Application
This function applies a legacy chat template to a given set of chat messages, handling buffer resizing and error checking.

#### Functionality
The function iterates over the input messages, concatenating their content parts and storing them in a vector. It then applies the chat template to the concatenated content, resizing the buffer if necessary.

#### Performance
The function has a time complexity of O(n), where n is the number of input messages. The buffer resizing operation may incur additional overhead.

#### Hidden Insights
* The function uses a vector to store the concatenated content, which allows for efficient resizing of the buffer.
* The function checks the result of the chat template application twice to ensure that the buffer is large enough.
" 
}
