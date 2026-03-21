# common.cpp__cpu_get_num_physical_cores

Tags: #gpu #loop #threading

```json
{
  "title": "cpu_get_num_physical_cores",
  "summary": "This function retrieves the number of physical CPU cores available on the system.",
  "details": "The function uses different methods to determine the number of physical CPU cores depending on the operating system. On Linux, it reads the thread siblings from the /sys/devices/system/cpu/cpu* files. On macOS, it uses the sysctlbyname function to retrieve the number of physical CPU cores. On Windows, it uses the GetLogicalProcessorInformationEx function to retrieve the number of physical CPU cores.",
  "rationale": "The function uses different methods to determine the number of physical CPU cores because each operating system provides a different API to access this information. The function also uses a fallback method to return the number of hardware threads if the number of physical CPU cores cannot be determined.",
  "performance": "The function has a time complexity of O(n), where n is the number of CPU cores. This is because it reads the thread siblings from the /sys/devices/system/cpu/cpu* files on Linux or uses the sysctlbyname function on macOS. On Windows, it uses the GetLogicalProcessorInformationEx function, which has a time complexity of O(n) as well.",
  "hidden_insights": [
    "The function uses the std::unordered_set data structure to store the thread siblings on Linux.",
    "The function uses the sysctlbyname function on macOS to retrieve the number of physical CPU cores.",
    "The function uses the GetLogicalProcessorInformationEx function on Windows to retrieve the number of physical CPU cores."
  ],
  "where_used": [
    "This function is likely used in applications that require knowledge of the number of physical CPU cores available on the system.",
    "It may be used in applications that need to optimize their performance based on the number of physical CPU cores available."
  ],
  "tags": [
    "cpu",
    "cores",
    "physical",
    "linux",
    "macos",
    "windows",
    "sysctlbyname",
    "GetLogicalProcessorInformationEx"
  ],
  "markdown": "### cpu_get_num_physical_cores
This function retrieves the number of physical CPU cores available on the system.

#### Linux
On Linux, the function reads the thread siblings from the /sys/devices/system/cpu/cpu* files.

#### macOS
On macOS, the function uses the sysctlbyname function to retrieve the number of physical CPU cores.

#### Windows
On Windows, the function uses the GetLogicalProcessorInformationEx function to retrieve the number of physical CPU cores.

#### Performance
The function has a time complexity of O(n), where n is the number of CPU cores.

#### Where Used
This function is likely used in applications that require knowledge of the number of physical CPU cores available on the system."
}
```
