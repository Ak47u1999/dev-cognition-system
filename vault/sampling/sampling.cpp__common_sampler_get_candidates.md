# sampling.cpp__common_sampler_get_candidates

Tags: #loop

```json
{
  "title": "common_sampler_get_candidates",
  "summary": "Returns a pointer to the current sampling candidates array, optionally sorting it if requested.",
  "details": "This function retrieves the current sampling candidates array from the common sampler structure. If sorting is enabled, it sorts the array in descending order of token probability and updates the selected token index accordingly.",
  "rationale": "The function may be implemented this way to allow for efficient sorting of the sampling candidates array, which is a common operation in language models like LLaMA.",
  "performance": "The use of std::sort for sorting the array has a time complexity of O(n log n), which is efficient for large arrays. However, the function may still be a performance bottleneck if the array is very large.",
  "hidden_insights": [
    "The function uses a lambda function to specify the sorting order, which is a concise way to define a comparison function.",
    "The function updates the sorted flag of the sampling candidates array to indicate that it has been sorted."
  ],
  "where_used": [
    "sampling.cpp",
    "common_sampler.h"
  ],
  "tags": [
    "sampling",
    "sorting",
    "LLaMA"
  ],
  "markdown": "## common_sampler_get_candidates
Returns a pointer to the current sampling candidates array, optionally sorting it if requested.
### Description
This function retrieves the current sampling candidates array from the common sampler structure. If sorting is enabled, it sorts the array in descending order of token probability and updates the selected token index accordingly.
### Parameters
* `gsmpl`: the common sampler structure
* `do_sort`: a boolean indicating whether to sort the array
### Returns
A pointer to the current sampling candidates array
### Notes
The function uses a lambda function to specify the sorting order, which is a concise way to define a comparison function. The function updates the sorted flag of the sampling candidates array to indicate that it has been sorted."
}
