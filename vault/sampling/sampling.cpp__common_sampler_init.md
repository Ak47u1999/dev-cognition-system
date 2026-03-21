# sampling.cpp__common_sampler_init

Tags: #ggml #loop

```json
{
  "title": "common_sampler_init",
  "summary": "Initializes a common sampler based on the provided model and sampling parameters.",
  "details": "This function creates a common sampler by initializing a grammar sampler and a chain sampler. It handles different types of grammars and triggers, and it also feeds generation prompt tokens to the grammar sampler to advance past tokens already placed in the prompt.",
  "rationale": "The function is implemented this way to handle different types of grammars and triggers, and to provide flexibility in the sampling process.",
  "performance": "The performance of this function may be affected by the size of the grammar and the number of triggers. It also uses regular expressions to escape trigger patterns, which may have a performance impact.",
  "hidden_insights": [
    "The function uses a lazy grammar sampler when the grammar is not empty and the lazy flag is set.",
    "The function uses a chain sampler to combine multiple samplers.",
    "The function feeds generation prompt tokens to the grammar sampler to advance past tokens already placed in the prompt."
  ],
  "where_used": [
    "sampling module",
    "generation module"
  ],
  "tags": [
    "sampling",
    "grammar",
    "trigger",
    "performance"
  ],
  "markdown": "## common_sampler_init
Initializes a common sampler based on the provided model and sampling parameters.

### Purpose
The purpose of this function is to create a common sampler that can handle different types of grammars and triggers.

### Parameters
* `model`: The model to use for the sampler.
* `params`: The sampling parameters.

### Return Value
The function returns a pointer to the initialized common sampler.

### Notes
The function uses a lazy grammar sampler when the grammar is not empty and the lazy flag is set. It also feeds generation prompt tokens to the grammar sampler to advance past tokens already placed in the prompt."
}
