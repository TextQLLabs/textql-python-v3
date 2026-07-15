# ScimTokens

## Overview

### Available Operations

* [list](#list) - ListScimTokens

## list

ListScimTokens

### Example Usage

<!-- UsageSnippet language="python" operationID="ScimService_ListScimTokens" method="post" path="/textql.rpc.public.scim.ScimService/ListScimTokens" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.scim_tokens.list(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                   | Type                                                                                                        | Required                                                                                                    | Description                                                                                                 |
| ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                      | [models.TextqlRPCPublicScimListScimTokensRequest](../../models/textqlrpcpublicscimlistscimtokensrequest.md) | :heavy_check_mark:                                                                                          | N/A                                                                                                         |
| `connect_timeout_ms`                                                                                        | *Optional[float]*                                                                                           | :heavy_minus_sign:                                                                                          | N/A                                                                                                         |
| `retries`                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                            | :heavy_minus_sign:                                                                                          | Configuration to override the default retry behavior of the client.                                         |

### Response

**[models.ScimServiceListScimTokensResponse](../../models/scimservicelistscimtokensresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |