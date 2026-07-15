# SlackServices

## Overview

### Available Operations

* [get_current_user](#get_current_user) - GetCurrentUser
* [list_users](#list_users) - ListUsers

## get_current_user

GetCurrentUser

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_GetCurrentUser" method="post" path="/textql.rpc.public.slack.SlackService/GetCurrentUser" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack_services.get_current_user(body={})

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

**[models.SlackServiceGetCurrentUserResponse](../../models/slackservicegetcurrentuserresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_users

ListUsers

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_ListUsers" method="post" path="/textql.rpc.public.slack.SlackService/ListUsers" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack_services.list_users(body={})

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

**[models.SlackServiceListUsersResponse](../../models/slackservicelistusersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |