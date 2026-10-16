# TextqlRPCPublicSecretAPIAuthType

Authentication mode for an API connector. Provider templates have a separate
 auth_type describing how their credentials are entered (e.g. basic_auth).
 OAUTH_U2M shares one OAuth account among members with connector access;
 OAUTH_PER_MEMBER requires each member to connect their own account.

## Example Usage

```python
from textql_sdk.models import TextqlRPCPublicSecretAPIAuthType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TextqlRPCPublicSecretAPIAuthType = "API_AUTH_TYPE_UNSPECIFIED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"API_AUTH_TYPE_UNSPECIFIED"`
- `"API_AUTH_TYPE_TOKEN"`
- `"API_AUTH_TYPE_OAUTH_U2M"`
- `"API_AUTH_TYPE_OAUTH_PER_MEMBER"`
- `"API_AUTH_TYPE_ENV_VAR"`
- `"API_AUTH_TYPE_NONE"`
- `"API_AUTH_TYPE_OTHER"`
