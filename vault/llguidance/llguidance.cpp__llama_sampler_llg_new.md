# llguidance.cpp__llama_sampler_llg_new

Tags: #memory

```json
{
  "title": "llg_matcher creation function",
  "summary": "Creates a new LlgMatcher instance based on the provided tokenizer, grammar kind, and grammar data.",
  "details": "This function initializes a new LlgMatcher instance using the provided tokenizer, grammar kind, and grammar data. It also sets the log level based on the environment variable LLGUIDANCE_LOG_LEVEL. If an error occurs during matcher creation, it logs the error and returns nullptr.",
  "rationale": "The function is implemented this way to allow for flexible configuration of the log level and to handle potential errors during matcher creation.",
  "performance": "The function has a time complexity of O(1) as it only performs a constant number of operations. However, the performance may be affected by the complexity of the grammar data and the tokenizer.",
  "hidden_insights": [
    "The function uses the getenv function to retrieve the log level from the environment variable LLGUIDANCE_LOG_LEVEL.",
    "The function uses the atoi function to convert the log level string to an integer."
  ],
  "where_used": [
    "llguidance.cpp"
  ],
  "tags": [
    "llg_matcher",
    "tokenizer",
    "grammar_kind",
    "grammar_data",
    "log_level"
  ],
  "markdown": "### llg_matcher creation function
Creates a new LlgMatcher instance based on the provided tokenizer, grammar kind, and grammar data.
#### Parameters
* `tokenizer`: The tokenizer to use for the matcher.
* `grammar_kind`: The kind of grammar to use for the matcher.
* `grammar_data`: The data for the grammar to use for the matcher.
#### Returns
A new LlgMatcher instance, or nullptr if an error occurs during creation.
#### Notes
The function sets the log level based on the environment variable LLGUIDANCE_LOG_LEVEL. If an error occurs during matcher creation, it logs the error and returns nullptr."
}
