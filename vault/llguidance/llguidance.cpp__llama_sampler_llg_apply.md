# llguidance.cpp__llama_sampler_llg_apply

Tags: #kernel #loop #memory

```json
{
  "title": "llama_sampler_llg_apply",
  "summary": "Applies LLG guidance to a token data array by setting logit values to negative infinity for tokens not matching the grammar.",
  "details": "This function is part of the LLaMA sampler and is responsible for applying LLG (Log-Linear Grammar) guidance to a token data array. It checks if the grammar is valid and computes the mask if necessary. Then, it iterates over the token data array and sets the logit value of tokens that do not match the grammar to negative infinity.",
  "rationale": "The function may be implemented this way to ensure that tokens not matching the grammar are penalized and less likely to be selected.",
  "performance": "The function has a time complexity of O(n), where n is the size of the token data array. This is because it iterates over the array once.",
  "hidden_insights": [
    "The function uses a bit mask to efficiently check if a token matches the grammar.",
    "The function uses a lazy computation approach to compute the mask only when necessary."
  ],
  "where_used": [
    "llama_sampler_llg"
  ],
  "tags": [
    "LLaMA",
    "sampler",
    "LLG",
    "guidance"
  ],
  "markdown": "### llama_sampler_llg_apply
Applies LLG guidance to a token data array by setting logit values to negative infinity for tokens not matching the grammar.
#### Purpose
This function is part of the LLaMA sampler and is responsible for applying LLG (Log-Linear Grammar) guidance to a token data array.
#### Details
The function checks if the grammar is valid and computes the mask if necessary. Then, it iterates over the token data array and sets the logit value of tokens that do not match the grammar to negative infinity.
#### Performance
The function has a time complexity of O(n), where n is the size of the token data array.
#### Tags
LLaMA, sampler, LLG, guidance"
}
