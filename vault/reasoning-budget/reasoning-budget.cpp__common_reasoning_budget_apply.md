# reasoning-budget.cpp__common_reasoning_budget_apply

Tags: #loop

```json
{
  "title": "Apply Reasoning Budget",
  "summary": "This function applies a reasoning budget by forcing a specific token in a sequence and setting all other logits to negative infinity.",
  "details": "The function takes a sampler and a token data array as input. It checks if the current state is not in the forcing state, in which case it returns without modifying the logits. If the current position is beyond the last forced token, it also returns. Otherwise, it sets all logits to negative infinity except for the forced token and advances to the next forced token. If all forced tokens have been applied, it sets the state to done and logs a message.",
  "rationale": "This implementation may be chosen to enforce a specific token in a sequence while ignoring other possibilities, which is useful for reasoning budgeting.",
  "performance": "This function has a time complexity of O(n), where n is the size of the token data array, due to the loop that sets all logits to negative infinity.",
  "hidden_insights": [
    "The function uses a separate state variable to keep track of the current position in the forced token sequence.",
    "The use of negative infinity to represent invalid logits is a common convention in probability and statistics."
  ],
  "where_used": [
    "This function is likely used in a larger sequence generation or reasoning system, where the reasoning budget is enforced to control the complexity of the generated sequences."
  ],
  "tags": [
    "reasoning budget",
    "sequence generation",
    "forced token",
    "logits"
  ],
  "markdown": "## Apply Reasoning Budget\n\nThis function applies a reasoning budget by forcing a specific token in a sequence and setting all other logits to negative infinity.\n\n### Details\n\nThe function takes a sampler and a token data array as input. It checks if the current state is not in the forcing state, in which case it returns without modifying the logits. If the current position is beyond the last forced token, it also returns. Otherwise, it sets all logits to negative infinity except for the forced token and advances to the next forced token. If all forced tokens have been applied, it sets the state to done and logs a message.\n\n### Rationale\n\nThis implementation may be chosen to enforce a specific token in a sequence while ignoring other possibilities, which is useful for reasoning budgeting.\n\n### Performance\n\nThis function has a time complexity of O(n), where n is the size of the token data array, due to the loop that sets all logits to negative infinity.\n\n### Hidden Insights\n\n* The function uses a separate state variable to keep track of the current position in the forced token sequence.\n* The use of negative infinity to represent invalid logits is a common convention in probability and statistics.\n\n### Where Used\n\nThis function is likely used in a larger sequence generation or reasoning system, where the reasoning budget is enforced to control the complexity of the generated sequences.\n\n### Tags\n\n* reasoning budget\n* sequence generation\n* forced token\n* logits"
}
