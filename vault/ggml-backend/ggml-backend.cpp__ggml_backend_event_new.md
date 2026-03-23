# ggml-backend.cpp__ggml_backend_event_new

Tags: #ggml #loop #memory

{
  "title": "ggml_backend_event_new",
  "summary": "Creates a new event based on the provided device.",
  "details": "This function creates a new event by calling the event_new method of the device's interface. It checks if the device is null or if the event_new method is null, in which case it returns null.",
  "rationale": "The function is implemented this way to allow for a transition period to the device interface, where a null device is allowed.",
  "performance": "The function has a time complexity of O(1) as it only involves a constant number of operations.",
  "hidden_insights": [
    "The function uses the device's interface to create a new event, which suggests that the device interface is responsible for managing events.",
    "The function allows for a null device, which may be used for testing or debugging purposes."
  ],
  "where_used": [
    "ggml_backend_dev_t device"
  ],
  "tags": [
    "event creation",
    "device interface",
    "transition period"
  ],
  "markdown": "### ggml_backend_event_new
Creates a new event based on the provided device.
#### Purpose
This function creates a new event by calling the event_new method of the device's interface.
#### Parameters
* `device`: The device to create the event from.
#### Return Value
A new event, or null if the device is null or the event_new method is null.
#### Notes
This function is used to allow for a transition period to the device interface, where a null device is allowed."
