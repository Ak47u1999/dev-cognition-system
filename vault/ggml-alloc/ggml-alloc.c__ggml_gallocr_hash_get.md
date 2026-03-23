# ggml-alloc.c__ggml_gallocr_hash_get

Tags: #ggml

# ggml_gallocr_hash_get

Retrieves a hash node from a gallocr hash set based on a tensor.

## Parameters

* `galloc`: a gallocr object
* `t`: a tensor

## Returns

A pointer to a hash node in the gallocr's hash set.

## Notes

This function uses a pointer to a hash node, which may lead to memory leaks if not properly managed.

## See Also

* `ggml_hash_find_or_insert`
