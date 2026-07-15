# TextqlRPCPublicPatchesConfigDiagnosticClass

ConfigDiagnosticClass partitions a finding by who can fix it, so an authoring loop
 knows whether to keep iterating.

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicPatchesConfigDiagnosticClass

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicPatchesConfigDiagnosticClass = "CONFIG_DIAGNOSTIC_CLASS_UNSPECIFIED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"CONFIG_DIAGNOSTIC_CLASS_UNSPECIFIED"`
- `"CONFIG_DIAGNOSTIC_CLASS_EDIT_FIXABLE"`
- `"CONFIG_DIAGNOSTIC_CLASS_ORG_STATE_FIXABLE"`
