# TextqlRPCPublicDatasetDatasetType

never change the names or numbers of existing dataset types!

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicDatasetDatasetType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicDatasetDatasetType = "TYPE_UNKNOWN"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"TYPE_UNKNOWN"`
- `"TYPE_TABULAR"`
- `"TYPE_DATAFRAME"`
- `"TYPE_DOCUMENT"`
- `"TYPE_TABLEAU"`
- `"TYPE_IMAGE"`
- `"TYPE_TEXT"`
- `"TYPE_POWERBI"`
