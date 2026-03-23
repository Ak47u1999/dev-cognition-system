# common.cpp__common_init_from_params

Tags: #loop #memory

```json
{
  "title": "common_init_from_params",
  "summary": "Initializes a common_init_result object from given parameters, loading a model and creating a context.",
  "details": "This function takes a common_params object as input, loads a model, creates a context, and sets up various adapter settings. It also performs a warm-up run if specified.",
  "rationale": "The function is implemented this way to provide a flexible and customizable initialization process for the common_init_result object.",
  "performance": "The function has a time complexity of O(n), where n is the number of parameters in the common_params object. The warm-up run can also impact performance.",
  "hidden_insights": [
    "The function checks for the presence of a BOS token in the vocabulary and logs a warning if it's not found.",
    "The function uses a fallback SEP token as an EOS token if it's not found in the vocabulary.",
    "The function resets the samplers after the warm-up run to reset the RNG state to the seeded state."
  ],
  "where_used": [
    "common.cpp"
  ],
  "tags": [
    "common_init_result",
    "common_params",
    "model loading",
    "context creation",
    "adapter settings",
    "warm-up run"
  ],
  "markdown": "### common_init_from_params
Initializes a common_init_result object from given parameters, loading a model and creating a context.

#### Parameters
* `common_params & params`: The input parameters for initialization.

#### Returns
* `common_init_result_ptr`: The initialized common_init_result object.

#### Notes
* The function loads a model and creates a context using the input parameters.
* It sets up various adapter settings, including control vector loading and LORA initialization.
* The function also performs a warm-up run if specified, which can impact performance.
* The function checks for the presence of a BOS token in the vocabulary and logs a warning if it's not found.
* The function uses a fallback SEP token as an EOS token if it's not found in the vocabulary.
* The function resets the samplers after the warm-up run to reset the RNG state to the seeded state."
}
