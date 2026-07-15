# AgentService

## Overview

### Available Operations

* [duplicate](#duplicate) - DuplicateAgent
* [trigger_agent](#trigger_agent) - TriggerAgent

## duplicate

DuplicateAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_DuplicateAgent" method="post" path="/textql.rpc.public.agent.AgentService/DuplicateAgent" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agent_service.duplicate()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentServiceDuplicateAgentResponse](../../models/agentserviceduplicateagentresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## trigger_agent

TriggerAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_TriggerAgent" method="post" path="/textql.rpc.public.agent.AgentService/TriggerAgent" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agent_service.trigger_agent()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentServiceTriggerAgentResponse](../../models/agentservicetriggeragentresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |