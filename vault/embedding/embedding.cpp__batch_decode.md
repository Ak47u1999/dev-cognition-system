# embedding.cpp__batch_decode

Tags: #ggml #loop

```json
{
  "title": "Batch Embedding Decoding",
  "summary": "This function decodes a batch of sequences and extracts embeddings from the model output.",
  "details": "The function takes a llama_context, llama_batch, and output array as input. It clears the previous kv_cache values, runs the model, and then iterates over the batch to extract token or sequence embeddings. The extracted embeddings are normalized and stored in the output array.",
  "rationale": "The function is implemented this way to efficiently extract embeddings from the model output. The use of llama_get_embeddings_ith and llama_get_embeddings_seq functions allows for flexible handling of different pooling types.",
  "performance": "The function has a time complexity of O(n_tokens), where n_tokens is the number of tokens in the batch. The use of common_embd_normalize function to normalize the embeddings may introduce additional overhead.",
  "hidden_insights": [
    "The function assumes that the output array has enough space to store the extracted embeddings.",
    "The use of GGML_ASSERT macro to check for null pointer exceptions may introduce additional overhead."
  ],
  "where_used": [
    "llama_decode function",
    "common_embd_normalize function"
  ],
  "tags": [
    "embedding",
    "decoding",
    "llama",
    "batch"
  ],
  "markdown": "### Batch Embedding Decoding
This function decodes a batch of sequences and extracts embeddings from the model output.

#### Function Signature
```c
static void batch_decode(llama_context * ctx, llama_batch & batch, float * output, int n_seq, int n_embd_out, int embd_norm)
```

#### Function Description
The function takes a llama_context, llama_batch, and output array as input. It clears the previous kv_cache values, runs the model, and then iterates over the batch to extract token or sequence embeddings. The extracted embeddings are normalized and stored in the output array.

#### Time Complexity
The function has a time complexity of O(n_tokens), where n_tokens is the number of tokens in the batch.

#### Performance Considerations
The use of common_embd_normalize function to normalize the embeddings may introduce additional overhead.

#### Hidden Insights
* The function assumes that the output array has enough space to store the extracted embeddings.
* The use of GGML_ASSERT macro to check for null pointer exceptions may introduce additional overhead."
}
