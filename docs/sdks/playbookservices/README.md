# PlaybookServices

## Overview

### Available Operations

* [create_playbook](#create_playbook) - CreatePlaybook
* [demo_playbook](#demo_playbook) - DemoPlaybook
* [get_batch_run](#get_batch_run) - Get a specific batch run
* [get_playbook_lineage](#get_playbook_lineage) - GetPlaybookLineage
* [list_slack_channel_context_playbooks](#list_slack_channel_context_playbooks) - List all Slack channels context playbook mappings for the organization
* [remove_dashboard](#remove_dashboard) - RemoveDashboard
* [set_slack_channel_context_playbook](#set_slack_channel_context_playbook) - Set the context playbook for a Slack channel. This associates the given  playbook to a Slack channel so that Slack messages in that channel use the  playbook's context by default.

## create_playbook

CreatePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_CreatePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/CreatePlaybook" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_services.create_playbook(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                              | [models.TextqlRPCPublicPlaybookCreatePlaybookRequest](../../models/textqlrpcpublicplaybookcreateplaybookrequest.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `connect_timeout_ms`                                                                                                | *Optional[float]*                                                                                                   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.PlaybookServiceCreatePlaybookResponse](../../models/playbookservicecreateplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## demo_playbook

DemoPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_DemoPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/DemoPlaybook" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_services.demo_playbook()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `person_name`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `job_title`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `target_email`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceDemoPlaybookResponse](../../models/playbookservicedemoplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_batch_run

Get a specific batch run

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookBatchRun" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookBatchRun" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_services.get_batch_run()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `batch_run_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceGetPlaybookBatchRunResponse](../../models/playbookservicegetplaybookbatchrunresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_playbook_lineage

GetPlaybookLineage

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookLineage" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookLineage" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_services.get_playbook_lineage()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceGetPlaybookLineageResponse](../../models/playbookservicegetplaybooklineageresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_slack_channel_context_playbooks

List all Slack channels context playbook mappings for the organization

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_ListAllSlackChannelContextPlaybooks" method="post" path="/textql.rpc.public.playbook.PlaybookService/ListAllSlackChannelContextPlaybooks" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_services.list_slack_channel_context_playbooks(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                     | Type                                                                                                                                                          | Required                                                                                                                                                      | Description                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                                        | [models.TextqlRPCPublicPlaybookListAllSlackChannelContextPlaybooksRequest](../../models/textqlrpcpublicplaybooklistallslackchannelcontextplaybooksrequest.md) | :heavy_check_mark:                                                                                                                                            | N/A                                                                                                                                                           |
| `connect_timeout_ms`                                                                                                                                          | *Optional[float]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                            | N/A                                                                                                                                                           |
| `retries`                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                              | :heavy_minus_sign:                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                           |

### Response

**[models.PlaybookServiceListAllSlackChannelContextPlaybooksResponse](../../models/playbookservicelistallslackchannelcontextplaybooksresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## remove_dashboard

RemoveDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_RemoveDashboard" method="post" path="/textql.rpc.public.playbook.PlaybookService/RemoveDashboard" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_services.remove_dashboard()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dashboard_id`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceRemoveDashboardResponse](../../models/playbookserviceremovedashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## set_slack_channel_context_playbook

Set the context playbook for a Slack channel. This associates the given
 playbook to a Slack channel so that Slack messages in that channel use the
 playbook's context by default.

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_SetSlackChannelContextPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/SetSlackChannelContextPlaybook" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_services.set_slack_channel_context_playbook()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | The playbook to associate                                           |
| `slack_channel_id`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | Slack channel ID (e.g., C123...)                                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceSetSlackChannelContextPlaybookResponse](../../models/playbookservicesetslackchannelcontextplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |