# ChatServices

## Overview

### Available Operations

* [approve_ontology_change](#approve_ontology_change) - Resolve a halted ask_approval form cell. Submit runs the form's submission  and continues the agent with the outcome; Reject discards it (passive, no  run); Dismiss treats it as a change request (no run, next message says what  to change). All three set the cell's outcome, like the other approve/deny cells.
* [attach_app](#attach_app) - AttachApp
* [attach_dashboard](#attach_dashboard) - AttachDashboard
* [check_permissions](#check_permissions) - CheckChatPermissions
* [duplicate_chat](#duplicate_chat) - DuplicateChat
* [get_artifact](#get_artifact) - GetArtifact
* [get_playbook_chats](#get_playbook_chats) - GetPlaybookChats
* [reject_context_prompt_change](#reject_context_prompt_change) - RejectContextPromptChange
* [send](#send) - SendMessage

## approve_ontology_change

Resolve a halted ask_approval form cell. Submit runs the form's submission
 and continues the agent with the outcome; Reject discards it (passive, no
 run); Dismiss treats it as a change request (no run, next message says what
 to change). All three set the cell's outcome, like the other approve/deny cells.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_ApproveOntologyChange" method="post" path="/textql.rpc.public.chat.ChatService/ApproveOntologyChange" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.approve_ontology_change()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cell_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceApproveOntologyChangeResponse](../../models/chatserviceapproveontologychangeresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## attach_app

AttachApp

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_AttachApp" method="post" path="/textql.rpc.public.chat.ChatService/AttachApp" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.attach_app()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `app_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceAttachAppResponse](../../models/chatserviceattachappresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## attach_dashboard

AttachDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_AttachDashboard" method="post" path="/textql.rpc.public.chat.ChatService/AttachDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.attach_dashboard()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceAttachDashboardResponse](../../models/chatserviceattachdashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## check_permissions

CheckChatPermissions

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_CheckChatPermissions" method="post" path="/textql.rpc.public.chat.ChatService/CheckChatPermissions" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.check_permissions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceCheckChatPermissionsResponse](../../models/chatservicecheckchatpermissionsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## duplicate_chat

DuplicateChat

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_DuplicateChat" method="post" path="/textql.rpc.public.chat.ChatService/DuplicateChat" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.duplicate_chat()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `only_if_different_owner`                                           | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceDuplicateChatResponse](../../models/chatserviceduplicatechatresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_artifact

GetArtifact

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_GetArtifact" method="post" path="/textql.rpc.public.chat.ChatService/GetArtifact" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.get_artifact()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `artifact_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Cell ID or composite "cellId:type:url" for multi-artifact cells     |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceGetArtifactResponse](../../models/chatservicegetartifactresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_playbook_chats

GetPlaybookChats

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_GetPlaybookChats" method="post" path="/textql.rpc.public.chat.ChatService/GetPlaybookChats" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.get_playbook_chats()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `limit`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `skip`                                                              | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceGetPlaybookChatsResponse](../../models/chatservicegetplaybookchatsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## reject_context_prompt_change

RejectContextPromptChange

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_RejectContextPromptChange" method="post" path="/textql.rpc.public.chat.ChatService/RejectContextPromptChange" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.reject_context_prompt_change()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cell_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceRejectContextPromptChangeResponse](../../models/chatservicerejectcontextpromptchangeresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## send

SendMessage

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_SendMessage" method="post" path="/textql.rpc.public.chat.ChatService/SendMessage" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_services.send()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `message`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `image_urls`                                                        | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `message_id`                                                        | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `steering`                                                          | *OptionalNullable[bool]*                                            | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceSendMessageResponse](../../models/chatservicesendmessageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |