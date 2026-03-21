# chat.cpp__common_chat_params_init_lfm2

```json
{
  "title": "common_chat_params_init_lfm2",
  "summary": "Initializes common chat parameters for LFM2 chat templates.",
  "details": "This function initializes common chat parameters for LFM2 chat templates by applying the template directly, setting the format to PEG Native, and enabling thinking. It also extracts reasoning and tool information from the inputs and builds a parser and grammar based on the tool choice.",
  "rationale": "The function is implemented this way to provide a flexible and customizable way to initialize common chat parameters for LFM2 chat templates.",
  "performance": "The function has a time complexity of O(n), where n is the number of tools in the inputs. This is because it iterates over the tools to build the grammar.",
  "hidden_insights": [
    "The function uses a lambda function to build the parser and grammar, which allows for a more concise and expressive way to define the grammar rules.",
    "The function uses the `foreach_function` function to iterate over the tools and build the grammar, which allows for a more efficient way to handle large numbers of tools."
  ],
  "where_used": [
    "LFM2 chat templates",
    "Common chat parameters initialization"
  ],
  "tags": [
    "LFM2",
    "Common chat parameters",
    "Parser",
    "Grammar",
    "Thinking"
  ],
  "markdown": "### common_chat_params_init_lfm2
Initializes common chat parameters for LFM2 chat templates.

#### Summary
This function initializes common chat parameters for LFM2 chat templates by applying the template directly, setting the format to PEG Native, and enabling thinking.

#### Details
The function takes in a `common_chat_template` and `autoparser::generation_params` as inputs and returns a `common_chat_params` object. It applies the template directly to the inputs, sets the format to PEG Native, and enables thinking. It also extracts reasoning and tool information from the inputs and builds a parser and grammar based on the tool choice.

#### Performance
The function has a time complexity of O(n), where n is the number of tools in the inputs. This is because it iterates over the tools to build the grammar.

#### Hidden Insights
* The function uses a lambda function to build the parser and grammar, which allows for a more concise and expressive way to define the grammar rules.
* The function uses the `foreach_function` function to iterate over the tools and build the grammar, which allows for a more efficient way to handle large numbers of tools.
" 
}
