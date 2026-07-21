# TextqlRPCPublicChatThreadWarningType

ThreadWarningType is the canonical set of thread warning types

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicChatThreadWarningType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicChatThreadWarningType = "THREAD_WARNING_TYPE_UNSPECIFIED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"THREAD_WARNING_TYPE_UNSPECIFIED"`
- `"THREAD_WARNING_TYPE_MISSING_CONTEXT"`
- `"THREAD_WARNING_TYPE_ERROR_LOOP"`
- `"THREAD_WARNING_TYPE_EXCESSIVE_TOOL_CALLS"`
- `"THREAD_WARNING_TYPE_SLOW_QUERY"`
- `"THREAD_WARNING_TYPE_NO_RESULTS"`
- `"THREAD_WARNING_TYPE_USER_FRUSTRATION"`
- `"THREAD_WARNING_TYPE_POTENTIAL_HALLUCINATION"`
- `"THREAD_WARNING_TYPE_IGNORED_INSTRUCTION"`
- `"THREAD_WARNING_TYPE_USER_THUMBS_DOWN"`
- `"THREAD_WARNING_TYPE_NO_CONCLUSION"`
- `"THREAD_WARNING_TYPE_USER_THUMBS_UP"`
- `"THREAD_WARNING_TYPE_GOAL_ACHIEVED"`
- `"THREAD_WARNING_TYPE_USER_SATISFACTION"`
