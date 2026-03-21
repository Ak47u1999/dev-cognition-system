# ngram-map.cpp__common_ngram_map_accept

Tags: #loop

```json
{
  "title": "common_ngram_map_accept",
  "summary": "Updates the value statistics in a common_ngram_map after accepting a draft.",
  "details": "This function updates the value statistics in a common_ngram_map after accepting a draft. It finds the key and value corresponding to the last draft created and updates the value's n_accepted statistic.",
  "rationale": "The function may be implemented this way to ensure that the value statistics are updated correctly after accepting a draft, and to maintain consistency with the rest of the common_ngram_map implementation.",
  "performance": "The function has a time complexity of O(1) since it directly accesses the key and value at the last draft created index.",
  "hidden_insights": [
    "The function assumes that the last draft created index is valid and that the key and value at that index exist.",
    "The function uses a custom logging macro (LOG_INF) to log information about the update."
  ],
  "where_used": [
    "common_ngram_map_send_accepted"
  ],
  "tags": [
    "common_ngram_map",
    "value statistics",
    "draft acceptance"
  ],
  "markdown": "## common_ngram_map_accept\n\nUpdates the value statistics in a common_ngram_map after accepting a draft.\n\n### Details\n\nThis function finds the key and value corresponding to the last draft created and updates the value's n_accepted statistic.\n\n### Performance\n\nThe function has a time complexity of O(1) since it directly accesses the key and value at the last draft created index.\n\n### Hidden Insights\n\n* The function assumes that the last draft created index is valid and that the key and value at that index exist.\n* The function uses a custom logging macro (LOG_INF) to log information about the update."
}
