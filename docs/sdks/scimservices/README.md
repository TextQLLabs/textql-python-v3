# ScimServices

## Overview

### Available Operations

* [create_o_auth_client](#create_o_auth_client) - CreateScimOAuthClient

## create_o_auth_client

CreateScimOAuthClient

### Example Usage

<!-- UsageSnippet language="python" operationID="ScimService_CreateScimOAuthClient" method="post" path="/textql.rpc.public.scim.ScimService/CreateScimOAuthClient" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.scim_services.create_o_auth_client()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `description`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `expires_in_days`                                                   | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ScimServiceCreateScimOAuthClientResponse](../../models/scimservicecreatescimoauthclientresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |