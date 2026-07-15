# TextqlRPCPublicChatCellLifecycle

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicChatCellLifecycle

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicChatCellLifecycle = "LIFECYCLE_UNKNOWN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"LIFECYCLE_UNKNOWN"`
- `"LIFECYCLE_CREATING"`
- `"LIFECYCLE_CREATED"`
- `"LIFECYCLE_EXECUTING"`
- `"LIFECYCLE_EXECUTED"`
- `"LIFECYCLE_HALTED"`
- `"LIFECYCLE_HANDOFF_PENDING"`
