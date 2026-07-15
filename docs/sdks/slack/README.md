# Slack

## Overview

### Available Operations

* [create_uuid](#create_uuid) - CreateSlackUuid
* [delete_installation](#delete_installation) - DeleteInstallation
* [get_current_user](#get_current_user) - GetCurrentUser
* [handle_o_auth_callback](#handle_o_auth_callback) - HandleSlackOAuthCallback
* [list_channels](#list_channels) - ListChannels
* [list_installations](#list_installations) - ListInstallations
* [list_users](#list_users) - ListUsers
* [sync_workspace](#sync_workspace) - SyncWorkspace

## create_uuid

CreateSlackUuid

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_CreateSlackUuid" method="post" path="/textql.rpc.public.slack.SlackService/CreateSlackUuid" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack.create_uuid(body={})

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

**[models.SlackServiceCreateSlackUUIDResponse](../../models/slackservicecreateslackuuidresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_installation

DeleteInstallation

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_DeleteInstallation" method="post" path="/textql.rpc.public.slack.SlackService/DeleteInstallation" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack.delete_installation()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `team_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SlackServiceDeleteInstallationResponse](../../models/slackservicedeleteinstallationresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_current_user

GetCurrentUser

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_GetCurrentUser" method="post" path="/textql.rpc.public.slack.SlackService/GetCurrentUser" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack.get_current_user(body={})

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

## handle_o_auth_callback

HandleSlackOAuthCallback

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_HandleSlackOAuthCallback" method="post" path="/textql.rpc.public.slack.SlackService/HandleSlackOAuthCallback" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack.handle_o_auth_callback()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `code`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | OAuth code from Slack                                               |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | State containing orgId, memberId, uuid                              |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SlackServiceHandleSlackOAuthCallbackResponse](../../models/slackservicehandleslackoauthcallbackresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_channels

ListChannels

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_ListChannels" method="post" path="/textql.rpc.public.slack.SlackService/ListChannels" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack.list_channels(body={})

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

**[models.SlackServiceListChannelsResponse](../../models/slackservicelistchannelsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_installations

ListInstallations

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_ListInstallations" method="post" path="/textql.rpc.public.slack.SlackService/ListInstallations" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack.list_installations(body={})

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

**[models.SlackServiceListInstallationsResponse](../../models/slackservicelistinstallationsresponse.md)**

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

    res = text_ql.slack.list_users(body={})

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

## sync_workspace

SyncWorkspace

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_SyncWorkspace" method="post" path="/textql.rpc.public.slack.SlackService/SyncWorkspace" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack.sync_workspace()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `team_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SlackServiceSyncWorkspaceResponse](../../models/slackservicesyncworkspaceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |