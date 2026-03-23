# ggml-backend.cpp__ggml_backend_sched_print_assignments

Tags: #ggml #kernel #loop

```json
{
  "title": "ggml_backend_sched_print_assignments",
  "summary": "This function prints the assignments of tensors to splits in a schedule.",
  "details": "It iterates over the nodes in a graph and checks if the current node is the start of a new split. If it is, it prints the details of the split, including the number of inputs and their names. Then, it prints the details of each node, including its name, size, and backend, as well as the details of its sources.",
  "rationale": "This function is likely implemented this way to provide a clear and concise view of the assignments of tensors to splits in a schedule.",
  "performance": "This function has a time complexity of O(n), where n is the number of nodes in the graph. It uses a single loop to iterate over the nodes and prints the details of each node and its sources.",
  "hidden_insights": [
    "The function uses a `cur_split` variable to keep track of the current split being processed.",
    "The function uses the `ggml_backend_sched_get_tensor_backend` function to get the backend of a tensor.",
    "The function uses the `fmt_size` function to format the size of a tensor."
  ],
  "where_used": [
    "This function is likely used in the `ggml_backend_sched` module to print the assignments of tensors to splits in a schedule.",
    "It may also be used in other modules that require printing the assignments of tensors to splits."
  ],
  "tags": [
    "schedule",
    "tensor",
    "backend",
    "print"
  ],
  "markdown": "## ggml_backend_sched_print_assignments
This function prints the assignments of tensors to splits in a schedule.

### Purpose
The purpose of this function is to provide a clear and concise view of the assignments of tensors to splits in a schedule.

### How it works
The function iterates over the nodes in a graph and checks if the current node is the start of a new split. If it is, it prints the details of the split, including the number of inputs and their names. Then, it prints the details of each node, including its name, size, and backend, as well as the details of its sources.

### Performance
The function has a time complexity of O(n), where n is the number of nodes in the graph. It uses a single loop to iterate over the nodes and prints the details of each node and its sources.

### Usage
This function is likely used in the `ggml_backend_sched` module to print the assignments of tensors to splits in a schedule. It may also be used in other modules that require printing the assignments of tensors to splits."
}
