# ApiOAuth

## Overview

### Available Operations

* [exchange_client_credentials](#exchange_client_credentials) - ExchangeApiOAuthClientCredentials
* [exchange_code](#exchange_code) - ExchangeApiOAuthCode
* [exchange_jwt_bearer](#exchange_jwt_bearer) - ExchangeApiOAuthJwtBearer
* [get_config](#get_config) - GetApiOAuthConfig
* [get_status](#get_status) - GetApiOAuthStatus
* [get_url](#get_url) - GetApiOAuthURL
* [initiate_device_authorization](#initiate_device_authorization) - InitiateDeviceAuthorization
* [poll_device_code_token](#poll_device_code_token) - PollDeviceCodeToken
* [revoke_token](#revoke_token) - RevokeApiOAuthToken
* [upsert_config](#upsert_config) - Shared OAuth app configuration. Requires connector write permission.

## exchange_client_credentials

ExchangeApiOAuthClientCredentials

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_ExchangeApiOAuthClientCredentials" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthClientCredentials" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.exchange_client_credentials()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `ref`                                                                                                   | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.APIOAuthServiceExchangeAPIOAuthClientCredentialsResponse](../../models/apioauthserviceexchangeapioauthclientcredentialsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## exchange_code

ExchangeApiOAuthCode

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_ExchangeApiOAuthCode" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthCode" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.exchange_code()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `ref`                                                                                                   | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `code`                                                                                                  | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `state`                                                                                                 | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `code_verifier`                                                                                         | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `redirect_uri`                                                                                          | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | Must match the redirect_uri used in GetApiOAuthURL. Omit for the UI callback.                           |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.APIOAuthServiceExchangeAPIOAuthCodeResponse](../../models/apioauthserviceexchangeapioauthcoderesponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## exchange_jwt_bearer

ExchangeApiOAuthJwtBearer

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_ExchangeApiOAuthJwtBearer" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/ExchangeApiOAuthJwtBearer" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.exchange_jwt_bearer()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `ref`                                                                                                   | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.APIOAuthServiceExchangeAPIOAuthJwtBearerResponse](../../models/apioauthserviceexchangeapioauthjwtbearerresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_config

GetApiOAuthConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_GetApiOAuthConfig" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.get_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `api_access_key_id`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.APIOAuthServiceGetAPIOAuthConfigResponse](../../models/apioauthservicegetapioauthconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_status

GetApiOAuthStatus

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_GetApiOAuthStatus" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthStatus" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.get_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `api_access_key_id`                                                 | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.APIOAuthServiceGetAPIOAuthStatusResponse](../../models/apioauthservicegetapioauthstatusresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_url

GetApiOAuthURL

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_GetApiOAuthURL" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/GetApiOAuthURL" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.get_url()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                   | Type                                                                                                                                                                        | Required                                                                                                                                                                    | Description                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                        | *Optional[float]*                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |
| `ref`                                                                                                                                                                       | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md)                                                                     | :heavy_minus_sign:                                                                                                                                                          | N/A                                                                                                                                                                         |
| `state`                                                                                                                                                                     | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Caller-generated CSRF state. Validate the returned state before exchanging.                                                                                                 |
| `redirect_uri`                                                                                                                                                              | *Optional[str]*                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                          | Callback registered with the provider. Requires HTTPS, except for loopback<br/> HTTP callbacks. Omit to use the TextQL UI callback. Pass the same URI to<br/> ExchangeApiOAuthCode. |
| `retries`                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                            | :heavy_minus_sign:                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                         |

### Response

**[models.APIOAuthServiceGetAPIOAuthURLResponse](../../models/apioauthservicegetapioauthurlresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## initiate_device_authorization

InitiateDeviceAuthorization

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_InitiateDeviceAuthorization" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/InitiateDeviceAuthorization" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.initiate_device_authorization()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `ref`                                                                                                   | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.APIOAuthServiceInitiateDeviceAuthorizationResponse](../../models/apioauthserviceinitiatedeviceauthorizationresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## poll_device_code_token

PollDeviceCodeToken

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_PollDeviceCodeToken" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/PollDeviceCodeToken" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.poll_device_code_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `ref`                                                                                                   | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `device_code`                                                                                           | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.APIOAuthServicePollDeviceCodeTokenResponse](../../models/apioauthservicepolldevicecodetokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## revoke_token

RevokeApiOAuthToken

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_RevokeApiOAuthToken" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/RevokeApiOAuthToken" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.revoke_token()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `ref`                                                                                                   | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.APIOAuthServiceRevokeAPIOAuthTokenResponse](../../models/apioauthservicerevokeapioauthtokenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## upsert_config

Shared OAuth app configuration. Requires connector write permission.

### Example Usage

<!-- UsageSnippet language="python" operationID="ApiOAuthService_UpsertApiOAuthConfig" method="post" path="/textql.rpc.public.api_oauth.ApiOAuthService/UpsertApiOAuthConfig" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.api_o_auth.upsert_config()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `client_id`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `client_secret`                                                                                         | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `auth_url`                                                                                              | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `token_url`                                                                                             | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `scopes`                                                                                                | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `use_pkce`                                                                                              | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `token_auth_method`                                                                                     | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `extra_config`                                                                                          | Dict[str, *str*]                                                                                        | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `ref`                                                                                                   | [Optional[models.TextqlRPCPublicSecretAPIAccessRef]](../../models/textqlrpcpublicsecretapiaccessref.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `auth_header`                                                                                           | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `auth_prefix`                                                                                           | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `grant_type`                                                                                            | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | "authorization_code" (default), "client_credentials", "jwt_bearer", or "device_code"                    |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.APIOAuthServiceUpsertAPIOAuthConfigResponse](../../models/apioauthserviceupsertapioauthconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |