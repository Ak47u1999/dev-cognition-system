# ggml-backend-reg.cpp__ggml_backend_load_best

Tags: #ggml #loop

```json
{
  "title": "ggml_backend_load_best",
  "summary": "Loads the best available ggml backend from a list of search paths.",
  "details": "This function iterates over a list of search paths to find the best available ggml backend. It checks for files with a specific prefix and extension, loads the library, and calls the `ggml_backend_score` function to determine the score. The best-scoring library is returned.",
  "rationale": "The function is implemented this way to allow for flexible search paths and to prioritize the best available backend.",
  "performance": "The function has a time complexity of O(n), where n is the number of search paths. This is because it iterates over each search path and checks for files. The function also uses a linear search to find the best-scoring library.",
  "hidden_insights": [
    "The function uses `dl_load_library` to load the library, which returns a pointer to the library handle.",
    "The function uses `dl_get_sym` to get the address of the `ggml_backend_score` function from the library handle.",
    "The function uses `fs::directory_iterator` to iterate over the files in the search path."
  ],
  "where_used": [
    "ggml-backend-reg.cpp"
  ],
  "tags": [
    "ggml",
    "backend",
    "loading",
    "search paths"
  ],
  "markdown": "### ggml_backend_load_best
Loads the best available ggml backend from a list of search paths.

#### Parameters
* `name`: The name of the backend to load.
* `silent`: A flag indicating whether to log errors or not.
* `user_search_path`: The user-provided search path.

#### Returns
The best available ggml backend.

#### Notes
The function iterates over a list of search paths to find the best available ggml backend. It checks for files with a specific prefix and extension, loads the library, and calls the `ggml_backend_score` function to determine the score. The best-scoring library is returned."
}
