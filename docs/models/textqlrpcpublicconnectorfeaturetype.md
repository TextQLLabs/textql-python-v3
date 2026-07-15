# TextqlRPCPublicConnectorFeatureType

Feature types for nudge queries - identifies which feature a query promotes

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicConnectorFeatureType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicConnectorFeatureType = "FEATURE_TYPE_UNSPECIFIED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"FEATURE_TYPE_UNSPECIFIED"`
- `"FEATURE_TYPE_REPORT"`
- `"FEATURE_TYPE_PLAYBOOK"`
- `"FEATURE_TYPE_DASHBOARD"`
