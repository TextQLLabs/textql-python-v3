# SecretServices

## Overview

### Available Operations

* [delete_api_access_key](#delete_api_access_key) - DeleteApiAccessKey
* [delete_secret](#delete_secret) - DeleteSecret
* [list_api_access_keys](#list_api_access_keys) - ListApiAccessKeys
* [list_secrets](#list_secrets) - ListSecrets
* [put_secret](#put_secret) - PutSecret
* [test_api_access_key](#test_api_access_key) - TestApiAccessKey

## delete_api_access_key

DeleteApiAccessKey

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_DeleteApiAccessKey" method="post" path="/textql.rpc.public.secret.SecretService/DeleteApiAccessKey" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_services.delete_api_access_key()

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

**[models.SecretServiceDeleteAPIAccessKeyResponse](../../models/secretservicedeleteapiaccesskeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_secret

DeleteSecret

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_DeleteSecret" method="post" path="/textql.rpc.public.secret.SecretService/DeleteSecret" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_services.delete_secret()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SecretServiceDeleteSecretResponse](../../models/secretservicedeletesecretresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_api_access_keys

ListApiAccessKeys

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_ListApiAccessKeys" method="post" path="/textql.rpc.public.secret.SecretService/ListApiAccessKeys" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_services.list_api_access_keys(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                | [models.TextqlRPCPublicSecretListAPIAccessKeysRequest](../../models/textqlrpcpublicsecretlistapiaccesskeysrequest.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `connect_timeout_ms`                                                                                                  | *Optional[float]*                                                                                                     | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.SecretServiceListAPIAccessKeysResponse](../../models/secretservicelistapiaccesskeysresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_secrets

ListSecrets

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_ListSecrets" method="post" path="/textql.rpc.public.secret.SecretService/ListSecrets" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_services.list_secrets(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                 | Type                                                                                                      | Required                                                                                                  | Description                                                                                               |
| --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                    | [models.TextqlRPCPublicSecretListSecretsRequest](../../models/textqlrpcpublicsecretlistsecretsrequest.md) | :heavy_check_mark:                                                                                        | N/A                                                                                                       |
| `connect_timeout_ms`                                                                                      | *Optional[float]*                                                                                         | :heavy_minus_sign:                                                                                        | N/A                                                                                                       |
| `retries`                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                          | :heavy_minus_sign:                                                                                        | Configuration to override the default retry behavior of the client.                                       |

### Response

**[models.SecretServiceListSecretsResponse](../../models/secretservicelistsecretsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## put_secret

PutSecret

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_PutSecret" method="post" path="/textql.rpc.public.secret.SecretService/PutSecret" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_services.put_secret()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `name`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `value`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `link`                                                              | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `is_private`                                                        | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SecretServicePutSecretResponse](../../models/secretserviceputsecretresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## test_api_access_key

TestApiAccessKey

### Example Usage

<!-- UsageSnippet language="python" operationID="SecretService_TestApiAccessKey" method="post" path="/textql.rpc.public.secret.SecretService/TestApiAccessKey" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.secret_services.test_api_access_key()

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

**[models.SecretServiceTestAPIAccessKeyResponse](../../models/secretservicetestapiaccesskeyresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |