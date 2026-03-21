# speculative.cpp__create_state_ngram_cache

```json
{
  "title": "create_state_ngram_cache",
  "summary": "Creates a speculative state n-gram cache object.",
  "details": "This function initializes a common_speculative_state_ngram_cache object with the given configuration and parameters. It takes in the static and dynamic path, a common_speculative_config object, and returns a fully constructed state n-gram cache object.",
  "rationale": "The function may be implemented this way to allow for easy configuration and customization of the cache object.",
  "performance": "No specific performance considerations are mentioned in the code.",
  "hidden_insights": [
    "The n_draft value is hardcoded to 8, but it's intended to be configurable.",
    "The save_static and save_dynamic flags are hardcoded to false, but they're intended to be configurable."
  ],
  "where_used": [
    "common/common.h"
  ],
  "tags": [
    "speculative",
    "cache",
    "n-gram",
    "configuration"
  ],
  "markdown": "### create_state_ngram_cache
Creates a speculative state n-gram cache object.

#### Parameters
* `path_static`: The static path.
* `path_dynamic`: The dynamic path.
* `config`: The common speculative config object.

#### Returns
A fully constructed state n-gram cache object.
"
}
