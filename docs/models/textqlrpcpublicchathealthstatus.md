# TextqlRPCPublicChatHealthStatus

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicChatHealthStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicChatHealthStatus = "STATUS_UNKNOWN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"STATUS_UNKNOWN"`
- `"STATUS_HEALTHY"`
- `"STATUS_MINOR"`
- `"STATUS_MAJOR"`
- `"STATUS_CRITICAL"`
