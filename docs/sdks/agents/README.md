# Agents

## Overview

### Available Operations

* [create](#create) - CreateAgent
* [delete](#delete) - DeleteAgent
* [duplicate](#duplicate) - DuplicateAgent
* [get_agent](#get_agent) - GetAgent
* [get_db_schema](#get_db_schema) - GetAgentDBSchema
* [get_db_table_preview](#get_db_table_preview) - GetAgentDBTablePreview
* [get_run](#get_run) - GetAgentRun
* [list_runs](#list_runs) - ListAgentRuns
* [list](#list) - ListAgents
* [reset_agent_avatar](#reset_agent_avatar) - ResetAgentAvatar
* [trigger_agent](#trigger_agent) - TriggerAgent
* [update](#update) - UpdateAgent
* [upload_agent_avatar](#upload_agent_avatar) - UploadAgentAvatar

## create

CreateAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_CreateAgent" method="post" path="/textql.rpc.public.agent.AgentService/CreateAgent" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                   | Type                                                                                                                                                                                                        | Required                                                                                                                                                                                                    | Description                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                                                                        | *Optional[float]*                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `name`                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `prompt`                                                                                                                                                                                                    | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `paradigm_options`                                                                                                                                                                                          | [Optional[models.TextqlRPCPublicParadigmParadigmOptions]](../../models/textqlrpcpublicparadigmparadigmoptions.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `source_suggestion_id`                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `slack_channel_id`                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `slack_dm_user_ids`                                                                                                                                                                                         | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `skip_org_default_channel`                                                                                                                                                                                  | *Optional[bool]*                                                                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `llm_model`                                                                                                                                                                                                 | [Optional[models.TextqlRPCPublicChatLlmModel]](../../models/textqlrpcpublicchatllmmodel.md)                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `fast_mode`                                                                                                                                                                                                 | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `is_stateful`                                                                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `posting_frequency_crons`                                                                                                                                                                                   | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `email_recipient_member_ids`                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `channel_ids`                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `teams_channel_id`                                                                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `teams_dm_user_aad_ids`                                                                                                                                                                                     | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `slack_trigger`                                                                                                                                                                                             | [Optional[models.TextqlRPCPublicAgentSlackAgentTrigger]](../../models/textqlrpcpublicagentslackagenttrigger.md)                                                                                             | :heavy_minus_sign:                                                                                                                                                                                          | N/A                                                                                                                                                                                                         |
| `posting_frequency_cadences`                                                                                                                                                                                | List[*str*]                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                          | Index-aligned with posting_frequency_crons. A non-empty cadence<br/> (HOURLY/FOUR-HOUR/EIGHT-HOUR/DAILY/WEEKLY) marks a flexible schedule whose<br/> cron the backend generates; "" (or an empty list) means exact. |
| `feed_enabled`                                                                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | Unset defaults to true: new agents are delegatable unless the caller opts<br/> out. Mirrors allow_ad_hoc_subagents below.                                                                                   |
| `retries`                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                         |

### Response

**[models.AgentServiceCreateAgentResponse](../../models/agentservicecreateagentresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

DeleteAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_DeleteAgent" method="post" path="/textql.rpc.public.agent.AgentService/DeleteAgent" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.delete()

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

## duplicate

DuplicateAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_DuplicateAgent" method="post" path="/textql.rpc.public.agent.AgentService/DuplicateAgent" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.duplicate()

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

## get_agent

GetAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_GetAgent" method="post" path="/textql.rpc.public.agent.AgentService/GetAgent" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.get_agent()

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

**[models.AgentServiceGetAgentResponse](../../models/agentservicegetagentresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_db_schema

GetAgentDBSchema

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_GetAgentDBSchema" method="post" path="/textql.rpc.public.agent.AgentService/GetAgentDBSchema" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.get_db_schema()

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

**[models.AgentServiceGetAgentDBSchemaResponse](../../models/agentservicegetagentdbschemaresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_db_table_preview

GetAgentDBTablePreview

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_GetAgentDBTablePreview" method="post" path="/textql.rpc.public.agent.AgentService/GetAgentDBTablePreview" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.get_db_table_preview()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `table_name`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | clamped server-side; 0 uses the default                             |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentServiceGetAgentDBTablePreviewResponse](../../models/agentservicegetagentdbtablepreviewresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_run

GetAgentRun

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_GetAgentRun" method="post" path="/textql.rpc.public.agent.AgentService/GetAgentRun" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.get_run()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `run_id`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentServiceGetAgentRunResponse](../../models/agentservicegetagentrunresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_runs

ListAgentRuns

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_ListAgentRuns" method="post" path="/textql.rpc.public.agent.AgentService/ListAgentRuns" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.list_runs()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.list()

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
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.reset_agent_avatar()

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

## trigger_agent

TriggerAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_TriggerAgent" method="post" path="/textql.rpc.public.agent.AgentService/TriggerAgent" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.trigger_agent()

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

## update

UpdateAgent

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_UpdateAgent" method="post" path="/textql.rpc.public.agent.AgentService/UpdateAgent" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.update()

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
| `feed_enabled`                                                                                                                                                                                              | *OptionalNullable[bool]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                          | Feed participation; nil = don't touch (mirrors fast_mode/is_stateful).                                                                                                                                      |
| `retries`                                                                                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                            | :heavy_minus_sign:                                                                                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                                                                                         |

### Response

**[models.AgentServiceUpdateAgentResponse](../../models/agentserviceupdateagentresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## upload_agent_avatar

UploadAgentAvatar

### Example Usage

<!-- UsageSnippet language="python" operationID="AgentService_UploadAgentAvatar" method="post" path="/textql.rpc.public.agent.AgentService/UploadAgentAvatar" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.agents.upload_agent_avatar()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `agent_id`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `image_data`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `file_name`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AgentServiceUploadAgentAvatarResponse](../../models/agentserviceuploadagentavatarresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |