# Chat

## Overview

### Available Operations

* [approve_context_prompt_change](#approve_context_prompt_change) - ApproveContextPromptChange
* [cancel_stream](#cancel_stream) - CancelStream
* [get_history](#get_history) - GetChatHistory
* [rate_cell](#rate_cell) - RateChatCell appends a row to cell_rating for every click; thumbs-down also upserts a user_thumbs_down thread_warning.

## approve_context_prompt_change

ApproveContextPromptChange

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_ApproveContextPromptChange" method="post" path="/textql.rpc.public.chat.ChatService/ApproveContextPromptChange" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat.approve_context_prompt_change()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cell_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `edited_context`                                                    | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceApproveContextPromptChangeResponse](../../models/chatserviceapprovecontextpromptchangeresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## cancel_stream

CancelStream

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_CancelStream" method="post" path="/textql.rpc.public.chat.ChatService/CancelStream" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat.cancel_stream()

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

**[models.ChatServiceCancelStreamResponse](../../models/chatservicecancelstreamresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_history

GetChatHistory

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_GetChatHistory" method="post" path="/textql.rpc.public.chat.ChatService/GetChatHistory" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat.get_history()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `skip`                                                              | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceGetChatHistoryResponse](../../models/chatservicegetchathistoryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## rate_cell

RateChatCell appends a row to cell_rating for every click; thumbs-down also upserts a user_thumbs_down thread_warning.

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_RateChatCell" method="post" path="/textql.rpc.public.chat.ChatService/RateChatCell" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat.rate_cell()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                            | *Optional[float]*                                                                               | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `chat_id`                                                                                       | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `cell_id`                                                                                       | *Optional[str]*                                                                                 | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `rating`                                                                                        | [Optional[models.TextqlRPCPublicChatCellRating]](../../models/textqlrpcpublicchatcellrating.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |
| `reason`                                                                                        | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | free-text "why" captured from the rating modal                                                  |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |

### Response

**[models.ChatServiceRateChatCellResponse](../../models/chatserviceratechatcellresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |