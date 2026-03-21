# ngram-map.cpp__common_ngram_simple_draft

Tags: #loop

```json
{
  "title": "Common N-Gram Simple Draft Function",
  "summary": "This function implements a simple self-speculative decoding without a draft model, searching for a matching pattern in the token history.",
  "details": "The function takes a configuration, a list of tokens, and a sampled token as input. It searches for a matching pattern in the token history, using the configuration's n-gram and m-gram sizes. If a match is found, it returns a list of tokens to be verified, otherwise it returns an empty list.",
  "rationale": "This implementation is likely used to provide a simple and efficient way to search for patterns in the token history, without requiring a complex draft model.",
  "performance": "The function has a time complexity of O(n), where n is the length of the token history, due to the linear search for the matching pattern.",
  "hidden_insights": [
    "The function uses a reserve function to preallocate memory for the pattern and draft tokens, which can improve performance by avoiding reallocations.",
    "The function uses a LOG_DBG statement to log information about the matching pattern, which can be useful for debugging purposes."
  ],
  "where_used": [
    "This function is likely used in a larger system that involves natural language processing and token-based operations.",
    "It may be used in a module that generates text based on a given configuration and token history."
  ],
  "tags": [
    "self-speculative decoding",
    "token history",
    "n-gram",
    "m-gram",
    "pattern search"
  ],
  "markdown": "## Common N-Gram Simple Draft Function
This function implements a simple self-speculative decoding without a draft model, searching for a matching pattern in the token history.

### Purpose
The function takes a configuration, a list of tokens, and a sampled token as input. It searches for a matching pattern in the token history, using the configuration's n-gram and m-gram sizes. If a match is found, it returns a list of tokens to be verified, otherwise it returns an empty list.

### Implementation
The function uses a linear search to find the matching pattern in the token history. It preallocates memory for the pattern and draft tokens using the reserve function, which can improve performance by avoiding reallocations.

### Performance
The function has a time complexity of O(n), where n is the length of the token history, due to the linear search for the matching pattern.

### Usage
This function is likely used in a larger system that involves natural language processing and token-based operations. It may be used in a module that generates text based on a given configuration and token history."
}
