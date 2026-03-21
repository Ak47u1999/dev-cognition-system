# chat.cpp__common_chat_templates_apply_jinja

Tags: #loop

```json
{
  "title": "common_chat_templates_apply_jinja",
  "summary": "This function applies Jinja templates to generate chat responses based on provided inputs and templates.",
  "details": "It takes in a set of common chat templates and inputs, and returns a set of parameters that can be used to generate chat responses. The function applies various workarounds and checks to ensure that the generated responses meet the requirements of the templates and inputs.",
  "rationale": "The function is implemented this way to provide a flexible and customizable way of generating chat responses. It allows for the use of Jinja templates, which can be used to create complex and dynamic responses.",
  "performance": "The function has a time complexity of O(n), where n is the number of templates and inputs. This is because it iterates over the templates and inputs to apply the workarounds and checks.",
  "hidden_insights": [
    "The function uses a workaround to map the developer role to the system role for all models except for GPT-OSS.",
    "It also uses a workaround to require non-null content in tool call messages.",
    "The function checks if the template supports system role and tool calls, and applies workarounds accordingly."
  ],
  "where_used": [
    "common_chat_template_direct_apply",
    "calculate_diff_split",
    "common_chat_extra_context"
  ],
  "tags": [
    "Jinja templates",
    "chat responses",
    "workarounds",
    "checks"
  ],
  "markdown": "### common_chat_templates_apply_jinja
This function applies Jinja templates to generate chat responses based on provided inputs and templates.

#### Purpose
The purpose of this function is to provide a flexible and customizable way of generating chat responses.

#### Workarounds and Checks
The function applies various workarounds and checks to ensure that the generated responses meet the requirements of the templates and inputs.

#### Performance
The function has a time complexity of O(n), where n is the number of templates and inputs.

#### Hidden Insights
* The function uses a workaround to map the developer role to the system role for all models except for GPT-OSS.
* It also uses a workaround to require non-null content in tool call messages.
* The function checks if the template supports system role and tool calls, and applies workarounds accordingly.
"
}
```
