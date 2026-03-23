# ggml-cann.cpp__ggml_backend_cann_device_event_new

Tags: #ggml #memory

```json
{
  "title": "ggml_backend_cann_device_event_new",
  "summary": "Creates a new event for a CANN device in the GGML backend.",
  "details": "This function creates a new event for a CANN device by setting the device context, creating an ACL event, and returning a new ggml_backend_event object with the device and context set.",
  "rationale": "The function may be implemented this way to ensure proper initialization of the device context and event creation, which is necessary for subsequent operations.",
  "performance": "The function's performance is likely not a major concern, as it only involves a few simple operations. However, the ACL event creation may have some overhead.",
  "hidden_insights": [
    "The function uses the ACL library to create an event, which suggests that the GGML backend is using NVIDIA's AI Compute Library (ACL) for its operations.",
    "The device context is stored in a separate structure, which may be used for other purposes in the GGML backend."
  ],
  "where_used": [
    "ggml_backend_cann_device_context",
    "ggml_cann_set_device",
    "aclrtEvent"
  ],
  "tags": [
    "GGML",
    "CANN",
    "ACL",
    "event creation"
  ],
  "markdown": "### ggml_backend_cann_device_event_new
Creates a new event for a CANN device in the GGML backend.

This function is used to initialize a new event for a CANN device. It sets the device context and creates an ACL event, which is then returned as a new `ggml_backend_event` object.

#### Parameters
* `dev`: The device context to use for the event.

#### Returns
A new `ggml_backend_event` object with the device and context set.

#### Notes
The function uses the ACL library to create an event, which suggests that the GGML backend is using NVIDIA's AI Compute Library (ACL) for its operations."
