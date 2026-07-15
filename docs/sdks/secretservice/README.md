# SecretService

## Overview

### Available Operations

* [get_api_access_key](#get_api_access_key) - GetApiAccessKey
* [migrate_secret_to_api_connector](#migrate_secret_to_api_connector) - MigrateSecretToApiConnector

## get_api_access_key

GetApiAccessKey

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_GetApiAccessKey" method="post" path="/textql.rpc.public.secret.SecretService/GetApiAccessKey" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_service.get_api_access_key()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `id`                                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SecretServiceGetAPIAccessKeyResponse](../../models/secretservicegetapiaccesskeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## migrate_secret_to_api_connector

MigrateSecretToApiConnector

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_MigrateSecretToApiConnector" method="post" path="/textql.rpc.public.secret.SecretService/MigrateSecretToApiConnector" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_service.migrate_secret_to_api_connector()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                       | *Optional[float]*                                                          | :heavy_minus_sign:                                                         | N/A                                                                        |
| `secret_name`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `api_access_key_id`                                                        | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | empty = create new API connector                                           |
| `header_name`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `hosts`                                                                    | List[*str*]                                                                | :heavy_minus_sign:                                                         | Fields used when creating a new API connector (api_access_key_id is empty) |
| `description`                                                              | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | N/A                                                                        |
| `value_prefix`                                                             | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | e.g. "Bearer ", prepended to the secret value                              |
| `name`                                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | display name for the new API connector                                     |
| `retries`                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)           | :heavy_minus_sign:                                                         | Configuration to override the default retry behavior of the client.        |

### Response

**[models.SecretServiceMigrateSecretToAPIConnectorResponse](../../models/secretservicemigratesecrettoapiconnectorresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |