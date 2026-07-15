# TeamsService

## Overview

### Available Operations

* [list_users](#list_users) - ListUsers

## list_users

ListUsers

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_ListUsers" method="post" path="/textql.rpc.public.teams.TeamsService/ListUsers" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.teams_service.list_users(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `body`                                                              | [models.GoogleProtobufEmpty](../../models/googleprotobufempty.md)   | :heavy_check_mark:                                                  | N/A                                                                 |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TeamsServiceListUsersResponse](../../models/teamsservicelistusersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |