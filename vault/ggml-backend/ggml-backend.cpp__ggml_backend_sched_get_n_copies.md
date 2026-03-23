# ggml-backend.cpp__ggml_backend_sched_get_n_copies

Tags: #ggml

{
  "title": "ggml_backend_sched_get_n_copies",
  "summary": "Returns the number of copies from a given schedule.",
  "details": "This function retrieves the number of copies from a schedule object. It takes a pointer to a schedule object as input and returns the corresponding value.",
  "rationale": "The function is likely implemented this way to provide a simple and efficient way to access the number of copies from a schedule object.",
  "performance": "The function has a time complexity of O(1) since it only involves a single pointer dereference.",
  "hidden_insights": [
    "The function assumes that the schedule object is valid, which is checked by the GGML_ASSERT macro."
  ],
  "where_used": [
    "ggml_backend_sched.c"
  ],
  "tags": [
    "C",
    "ggml",
    "schedule",
    "copies"
  ],
  "markdown": "# ggml_backend_sched_get_n_copies\n\nThis function retrieves the number of copies from a schedule object.\n\n## Parameters\n\n* `sched`: A pointer to a schedule object.\n\n## Returns\n\nThe number of copies from the schedule object.\n\n## Assumptions\n\nThe function assumes that the schedule object is valid.\n\n## Performance\n\nThe function has a time complexity of O(1) since it only involves a single pointer dereference.\n\n## Where Used\n\n* `ggml_backend_sched.c`"
