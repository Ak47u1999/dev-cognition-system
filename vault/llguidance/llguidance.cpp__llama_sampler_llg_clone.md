# llguidance.cpp__llama_sampler_llg_clone

```json
{
  "title": "llama_sampler_llg_clone",
  "summary": "Clones a llama_sampler instance with llg context.",
  "details": "This function creates a new llama_sampler instance with the same llg context as the input sampler. It initializes the new sampler with the same vocabulary and then copies the state from the input sampler, including the grammar and tokenizer.",
  "rationale": "The function is implemented this way to ensure that the new sampler has the same context as the input sampler, while also allowing for efficient copying of the state.",
  "performance": "The function has a time complexity of O(n), where n is the size of the grammar and tokenizer data. This is because it needs to clone the grammar and tokenizer.",
  "hidden_insights": [
    "The function uses a scope to ensure that the result_ctx pointer is valid even if an exception is thrown.",
    "The function assumes that the input sampler has an llg context."
  ],
  "where_used": [
    "llama_sampler_llg_init",
    "llama_sampler_llg_free"
  ],
  "tags": [
    "cloning",
    "llama_sampler",
    "llg_context"
  ],
  "markdown": "### llama_sampler_llg_clone\n\nClones a llama_sampler instance with llg context.\n\n#### Details\n\nThis function creates a new llama_sampler instance with the same llg context as the input sampler. It initializes the new sampler with the same vocabulary and then copies the state from the input sampler, including the grammar and tokenizer.\n\n#### Rationale\n\nThe function is implemented this way to ensure that the new sampler has the same context as the input sampler, while also allowing for efficient copying of the state.\n\n#### Performance\n\nThe function has a time complexity of O(n), where n is the size of the grammar and tokenizer data. This is because it needs to clone the grammar and tokenizer.\n\n#### Hidden Insights\n\n* The function uses a scope to ensure that the result_ctx pointer is valid even if an exception is thrown.\n* The function assumes that the input sampler has an llg context.\n\n#### Where Used\n\n* llama_sampler_llg_init\n* llama_sampler_llg_free\n\n#### Tags\n\n* cloning\n* llama_sampler\n* llg_context"
}
