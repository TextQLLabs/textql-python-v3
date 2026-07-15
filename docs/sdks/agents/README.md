# Agents

## Overview

### Available Operations

* [delete](#delete) - DeleteAgent
* [list_runs](#list_runs) - ListAgentRuns
* [list](#list) - ListAgents
* [reset_agent_avatar](#reset_agent_avatar) - ResetAgentAvatar
* [update](#update) - UpdateAgent

## delete

DeleteAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_DeleteAgent" method="post" path="/textql.rpc.public.agent.AgentService/DeleteAgent" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agents.delete()

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

**[models.AgentServiceDeleteAgentResponse](../../models/agentservicedeleteagentresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_runs

ListAgentRuns

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_ListAgentRuns" method="post" path="/textql.rpc.public.agent.AgentService/ListAgentRuns" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agents.list_runs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `trigger_source`                                                    | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `status`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentServiceListAgentRunsResponse](../../models/agentservicelistagentrunsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list

ListAgents

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_ListAgents" method="post" path="/textql.rpc.public.agent.AgentService/ListAgents" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agents.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_inactive`                                                  | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `include_all_org`                                                   | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `days`                                                              | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentServiceListAgentsResponse](../../models/agentservicelistagentsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## reset_agent_avatar

ResetAgentAvatar

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_ResetAgentAvatar" method="post" path="/textql.rpc.public.agent.AgentService/ResetAgentAvatar" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agents.reset_agent_avatar()

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

**[models.AgentServiceResetAgentAvatarResponse](../../models/agentserviceresetagentavatarresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update

UpdateAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_UpdateAgent" method="post" path="/textql.rpc.public.agent.AgentService/UpdateAgent" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.agents.update()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                   | Type                                                                                                                                                                                                        | Required                                                                                                                                                                                                    | Description                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `agent_id`                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `name`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `prompt`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `is_active`                                                                                                                                                                                                 | *Optional[bool]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `paradigm_options`                                                                                                                                                                                          | [Optional[models.TextqlRPCPublicParadigmParadigmOptions]](../../models/textqlrpcpublicparadigmparadigmoptions.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `slack_channel_id`                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `slack_dm_user_ids`                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `skip_org_default_channel`                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `llm_model`                                                                                                                                                                                                 | [Optional[models.TextqlRPCPublicChatLlmModel]](../../models/textqlrpcpublicchatllmmodel.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `fast_mode`                                                                                                                                                                                                 | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `is_stateful`                                                                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `posting_frequency_crons`                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `email_recipient_member_ids`                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `update_email_recipients`                                                                                                                                                                                   | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `channel_ids`                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `update_channel_ids`                                                                                                                                                                                        | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `teams_channel_id`                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `teams_dm_user_aad_ids`                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `slack_trigger`                                                                                                                                                                                             | [Optional[models.TextqlRPCPublicAgentSlackAgentTrigger]](../../models/textqlrpcpublicagentslackagenttrigger.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `posting_frequency_cadences`                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | Index-aligned with posting_frequency_crons. A non-empty cadence<br/> (HOURLY/FOUR-HOUR/EIGHT-HOUR/DAILY/WEEKLY) marks a flexible schedule whose<br/> cron the backend generates; "" (or an empty list) means exact. |
| `retries`                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                         |

### Response

**[models.AgentServiceUpdateAgentResponse](../../models/agentserviceupdateagentresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |