# chat.cpp__common_chat_templates_init

Tags: #ggml #loop #memory

```json
{
  "title": "common_chat_templates_init",
  "summary": "Initializes a common chat templates object with a default template and optional tool use template.",
  "details": "This function takes in a llama model, chat template override, BOS token override, and EOS token override. It checks if an explicit template is provided, and if not, it retrieves the default template from the llama model. It then patches the template to prevent errors and initializes the common chat templates object with the default template and optional tool use template.",
  "rationale": "The function is implemented this way to handle different scenarios, such as when an explicit template is provided, when the default template needs to be patched, and when the tool use template needs to be initialized.",
  "performance": "The function has a time complexity of O(n), where n is the length of the template string, due to the string replacement operations.",
  "hidden_insights": [
    "The function uses a temporary hack to prevent chat template errors.",
    "The function uses a temporary fix pending Minja changes.",
    "The function logs warnings when the vocab does not have a specific token."
  ],
  "where_used": [
    "common_chat_templates.cpp"
  ],
  "tags": [
    "llama",
    "chat",
    "templates",
    "initialization"
  ],
  "markdown": "### common_chat_templates_init
Initializes a common chat templates object with a default template and optional tool use template.

#### Parameters
* `model`: The llama model.
* `chat_template_override`: The chat template override.
* `bos_token_override`: The BOS token override.
* `eos_token_override`: The EOS token override.

#### Returns
A common chat templates object.

#### Notes
The function uses a temporary hack to prevent chat template errors and a temporary fix pending Minja changes. It also logs warnings when the vocab does not have a specific token."
}
