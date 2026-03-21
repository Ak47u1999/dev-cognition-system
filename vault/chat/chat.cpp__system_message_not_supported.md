# chat.cpp__system_message_not_supported

```json
{
  "title": "Merge or Remove System Prompt",
  "summary": "This function checks if the first message in a list of messages has a 'system' role and merges or removes it based on the presence of additional messages.",
  "details": "The function iterates over the list of messages and checks if the first message has a 'system' role. If there are additional messages, it merges the content of the first message with the second message and removes the first message. If there is only one message, it removes the message.",
  "rationale": "This implementation may be used to handle system prompts in a chat or messaging system where the template does not support the 'system' role.",
  "performance": "The function has a time complexity of O(n) where n is the number of messages in the list, as it iterates over the list to check for the 'system' role and merge or remove messages.",
  "hidden_insights": [
    "The function uses the `front()` and `at()` methods to access the first message and its content.",
    "The `erase()` method is used to remove messages from the list."
  ],
  "where_used": [
    "Chat or messaging system templates",
    "Message processing or filtering modules"
  ],
  "tags": [
    "system prompt",
    "message merging",
    "template support"
  ],
  "markdown": "### Merge or Remove System Prompt
This function checks if the first message in a list of messages has a 'system' role and merges or removes it based on the presence of additional messages.

#### Purpose
The purpose of this function is to handle system prompts in a chat or messaging system where the template does not support the 'system' role.

#### Implementation
The function iterates over the list of messages and checks if the first message has a 'system' role. If there are additional messages, it merges the content of the first message with the second message and removes the first message. If there is only one message, it removes the message.

#### Performance
The function has a time complexity of O(n) where n is the number of messages in the list, as it iterates over the list to check for the 'system' role and merge or remove messages.

#### Usage
This function may be used in chat or messaging system templates or message processing or filtering modules."
}
