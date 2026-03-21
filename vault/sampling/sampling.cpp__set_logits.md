# sampling.cpp__set_logits

Tags: #ggml #loop #recursion

```json
{
  "title": "Common Sampler",
  "summary": "The common sampler is a struct that holds various parameters and samplers for language model generation. It provides methods for resetting the sampler, setting logits, and measuring time.",
  "details": "The common sampler is a key component in the language model generation process. It holds various parameters and samplers that are used to generate text. The sampler can be reset, and logits can be set using the `set_logits` method. The `tm` method returns a time measurement object.",
  "rationale": "The common sampler is implemented as a struct to encapsulate the various parameters and samplers. This allows for easy access and modification of these parameters. The use of a struct also makes the code more organized and easier to understand.",
  "performance": "The performance of the common sampler is not explicitly optimized. However, the use of a ring buffer and a vector for storing tokens suggests that the sampler is designed for efficient memory usage and fast access to tokens.",
  "hidden_insights": [
    "The common sampler uses a ring buffer to store previous tokens, which allows for efficient access to these tokens.",
    "The sampler uses a vector to store the current tokens, which allows for fast insertion and removal of tokens."
  ],
  "where_used": [
    "The common sampler is likely used in the language model generation module.",
    "It may also be used in other modules that require language model generation."
  ],
  "tags": [
    "language model",
    "generation",
    "sampler",
    "parameters",
    "samplers"
  ],
  "markdown": "## Common Sampler
The common sampler is a struct that holds various parameters and samplers for language model generation.
### Methods
* `reset()`: Resets the sampler.
* `set_logits()`: Sets the logits for the sampler.
* `tm()`: Returns a time measurement object.
### Parameters
* `params`: The common parameters sampling object.
* `grmr`: The grammar sampler.
* `chain`: The chain sampler.
* `prev`: The ring buffer of previous tokens.
* `cur`: The vector of current tokens.
* `cur_p`: The current token data array.
### Performance
The performance of the common sampler is not explicitly optimized. However, the use of a ring buffer and a vector for storing tokens suggests that the sampler is designed for efficient memory usage and fast access to tokens."
}
