# ChatService

## Overview

### Available Operations

* [attach_dataset](#attach_dataset) - AttachDataset
* [check_streamlit_health](#check_streamlit_health) - CheckStreamlitHealth
* [create_chat](#create_chat) - CreateChat
* [get_completion_parameters](#get_completion_parameters) - GetCompletionParameters
* [poll_events](#poll_events) - PollChatEvents

## attach_dataset

AttachDataset

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_AttachDataset" method="post" path="/textql.rpc.public.chat.ChatService/AttachDataset" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_service.attach_dataset()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | uses latest version                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceAttachDatasetResponse](../../models/chatserviceattachdatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## check_streamlit_health

CheckStreamlitHealth

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_CheckStreamlitHealth" method="post" path="/textql.rpc.public.chat.ChatService/CheckStreamlitHealth" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_service.check_streamlit_health()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cell_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceCheckStreamlitHealthResponse](../../models/chatservicecheckstreamlithealthresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## create_chat

CreateChat

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_CreateChat" method="post" path="/textql.rpc.public.chat.ChatService/CreateChat" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_service.create_chat()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                          | Type                                                                                                                                               | Required                                                                                                                                           | Description                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                               | *Optional[float]*                                                                                                                                  | :heavy_minus_sign:                                                                                                                                 | N/A                                                                                                                                                |
| `paradigm`                                                                                                                                         | [Optional[models.TextqlRPCPublicParadigmParadigm]](../../models/textqlrpcpublicparadigmparadigm.md)                                                | :heavy_minus_sign:                                                                                                                                 | ChatParadigm includes paradigm options                                                                                                             |
| `model`                                                                                                                                            | [Optional[models.TextqlRPCPublicChatLlmModel]](../../models/textqlrpcpublicchatllmmodel.md)                                                        | :heavy_minus_sign:                                                                                                                                 | N/A                                                                                                                                                |
| `message`                                                                                                                                          | *OptionalNullable[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                                 | optionally pre-fill first message                                                                                                                  |
| `playbook_id`                                                                                                                                      | *OptionalNullable[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                                 | optionally associate with a playbook                                                                                                               |
| `research`                                                                                                                                         | *OptionalNullable[bool]*                                                                                                                           | :heavy_minus_sign:                                                                                                                                 | whether to enable report mode for this chat                                                                                                        |
| `dashboard_mode`                                                                                                                                   | *OptionalNullable[bool]*                                                                                                                           | :heavy_minus_sign:                                                                                                                                 | whether to enable dashboard mode for this chat                                                                                                     |
| `methodology`                                                                                                                                      | [Optional[models.TextqlRPCPublicChatMethodology]](../../models/textqlrpcpublicchatmethodology.md)                                                  | :heavy_minus_sign:                                                                                                                                 | N/A                                                                                                                                                |
| `vllm_model_id`                                                                                                                                    | *OptionalNullable[str]*                                                                                                                            | :heavy_minus_sign:                                                                                                                                 | vllm_model_id is the model identifier forwarded to the org's vLLM endpoint.<br/> Only valid when model == MODEL_VLLM. Requires @textql.com superadmin. |
| `fast_mode`                                                                                                                                        | *OptionalNullable[bool]*                                                                                                                           | :heavy_minus_sign:                                                                                                                                 | fast_mode enables Anthropic's fast inference (speed: "fast") for this chat.<br/> Currently supported on Opus 4.6 only. Pricing is 6x standard rates. |
| `retries`                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                   | :heavy_minus_sign:                                                                                                                                 | Configuration to override the default retry behavior of the client.                                                                                |

### Response

**[models.ChatServiceCreateChatResponse](../../models/chatservicecreatechatresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_completion_parameters

GetCompletionParameters

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_GetCompletionParameters" method="post" path="/textql.rpc.public.chat.ChatService/GetCompletionParameters" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_service.get_completion_parameters()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `cell_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServiceGetCompletionParametersResponse](../../models/chatservicegetcompletionparametersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## poll_events

PollChatEvents

### Example Usage

<!-- UsageSnippet language="python" operationID="ChatService_PollChatEvents" method="post" path="/textql.rpc.public.chat.ChatService/PollChatEvents" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.chat_service.poll_events()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `resume_cursor`                                                     | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `min_generation`                                                    | [Optional[models.MinGeneration]](../../models/mingeneration.md)     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ChatServicePollChatEventsResponse](../../models/chatservicepollchateventsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |