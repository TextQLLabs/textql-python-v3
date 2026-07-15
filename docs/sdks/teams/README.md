# Teams

## Overview

### Available Operations

* [create_uuid](#create_uuid) - CreateTeamsUuid
* [delete_installation](#delete_installation) - DeleteInstallation
* [get_current_user](#get_current_user) - GetCurrentUser
* [handle_o_auth_callback](#handle_o_auth_callback) - HandleTeamsOAuthCallback
* [list](#list) - ListChannels
* [list_installations](#list_installations) - ListInstallations
* [list_users](#list_users) - ListUsers
* [sync_workspace](#sync_workspace) - SyncWorkspace

## create_uuid

CreateTeamsUuid

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_CreateTeamsUuid" method="post" path="/textql.rpc.public.teams.TeamsService/CreateTeamsUuid" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.create_uuid(body={})

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

**[models.TeamsServiceCreateTeamsUUIDResponse](../../models/teamsservicecreateteamsuuidresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete_installation

DeleteInstallation

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_DeleteInstallation" method="post" path="/textql.rpc.public.teams.TeamsService/DeleteInstallation" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.delete_installation()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tenant_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TeamsServiceDeleteInstallationResponse](../../models/teamsservicedeleteinstallationresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_current_user

GetCurrentUser

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_GetCurrentUser" method="post" path="/textql.rpc.public.teams.TeamsService/GetCurrentUser" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.get_current_user(body={})

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

**[models.TeamsServiceGetCurrentUserResponse](../../models/teamsservicegetcurrentuserresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## handle_o_auth_callback

HandleTeamsOAuthCallback

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_HandleTeamsOAuthCallback" method="post" path="/textql.rpc.public.teams.TeamsService/HandleTeamsOAuthCallback" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.handle_o_auth_callback()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `code`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `state`                                                             | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TeamsServiceHandleTeamsOAuthCallbackResponse](../../models/teamsservicehandleteamsoauthcallbackresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list

ListChannels

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_ListChannels" method="post" path="/textql.rpc.public.teams.TeamsService/ListChannels" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.list(body={})

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

**[models.TeamsServiceListChannelsResponse](../../models/teamsservicelistchannelsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_installations

ListInstallations

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_ListInstallations" method="post" path="/textql.rpc.public.teams.TeamsService/ListInstallations" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.list_installations(body={})

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

**[models.TeamsServiceListInstallationsResponse](../../models/teamsservicelistinstallationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_users

ListUsers

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_ListUsers" method="post" path="/textql.rpc.public.teams.TeamsService/ListUsers" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.list_users(body={})

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

## sync_workspace

SyncWorkspace

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_SyncWorkspace" method="post" path="/textql.rpc.public.teams.TeamsService/SyncWorkspace" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.teams.sync_workspace()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tenant_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TeamsServiceSyncWorkspaceResponse](../../models/teamsservicesyncworkspaceresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |