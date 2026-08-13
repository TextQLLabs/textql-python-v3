# TextqlRPCAuthAssetURLExpiry

Values are the organization.asset_url_expiry column values — do not renumber.

## Example Usage

```python
from textql_sdk.models import TextqlRPCAuthAssetURLExpiry

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCAuthAssetURLExpiry = "EXPIRY_NONE"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"EXPIRY_NONE"`
- `"EXPIRY_ONE_DAY"`
- `"EXPIRY_SEVEN_DAYS"`
- `"EXPIRY_THIRTY_DAYS"`
- `"EXPIRY_ONE_YEAR"`
- `"EXPIRY_FIFTEEN_MINUTES"`
- `"EXPIRY_ONE_HOUR"`
- `"EXPIRY_SIX_HOURS"`
- `"EXPIRY_TWELVE_HOURS"`
