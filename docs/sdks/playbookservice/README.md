# PlaybookService

## Overview

### Available Operations

* [cancel_template_execution](#cancel_template_execution) - Cancel template execution for a specific template header
* [duplicate](#duplicate) - DuplicatePlaybook
* [get_active_subscribed_count](#get_active_subscribed_count) - GetActiveSubscribedPlaybooksCount
* [get_playbook_reports_batch](#get_playbook_reports_batch) - Get reports for multiple template data IDs in a single batch request
* [get_playbooks_previews](#get_playbooks_previews) - GetPlaybooksPreviews
* [get_report_by_id](#get_report_by_id) - Get a single report by ID
* [list_teams_channels_for_context_playbook](#list_teams_channels_for_context_playbook) - ListTeamsChannelsForContextPlaybook
* [remove_dataset](#remove_dataset) - RemoveDataset
* [unset_slack_channel_context_playbook](#unset_slack_channel_context_playbook) - Unset the context playbook for a Slack channel. This clears any association  so that messages in this channel no longer use a specific playbook context.
* [update](#update) - UpdatePlaybook

## cancel_template_execution

Cancel template execution for a specific template header

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_CancelTemplateExecution" method="post" path="/textql.rpc.public.playbook.PlaybookService/CancelTemplateExecution" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.cancel_template_execution()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `template_header_id`                                                | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceCancelTemplateExecutionResponse](../../models/playbookservicecanceltemplateexecutionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## duplicate

DuplicatePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_DuplicatePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/DuplicatePlaybook" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.duplicate()

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

**[models.PlaybookServiceDuplicatePlaybookResponse](../../models/playbookserviceduplicateplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_active_subscribed_count

GetActiveSubscribedPlaybooksCount

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetActiveSubscribedPlaybooksCount" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetActiveSubscribedPlaybooksCount" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.get_active_subscribed_count(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                 | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                                    | [models.TextqlRPCPublicPlaybookGetActiveSubscribedPlaybooksCountRequest](../../models/textqlrpcpublicplaybookgetactivesubscribedplaybookscountrequest.md) | :heavy_check_mark:                                                                                                                                        | N/A                                                                                                                                                       |
| `connect_timeout_ms`                                                                                                                                      | *Optional[float]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                        | N/A                                                                                                                                                       |
| `retries`                                                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                          | :heavy_minus_sign:                                                                                                                                        | Configuration to override the default retry behavior of the client.                                                                                       |

### Response

**[models.PlaybookServiceGetActiveSubscribedPlaybooksCountResponse](../../models/playbookservicegetactivesubscribedplaybookscountresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_playbook_reports_batch

Get reports for multiple template data IDs in a single batch request

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookReportsBatch" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookReportsBatch" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.get_playbook_reports_batch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `template_data_ids`                                                 | List[*str*]                                                         | :heavy_minus_sign:                                                  | List of template data UUIDs to fetch reports for                    |
| `limit_per_template`                                                | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | Max reports to return per template_data_id (default: 100)           |
| `batch_run_id`                                                      | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | UUID - filter reports and artifacts by batch run                    |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceGetPlaybookReportsBatchResponse](../../models/playbookservicegetplaybookreportsbatchresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_playbooks_previews

GetPlaybooksPreviews

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybooksPreviews" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybooksPreviews" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.get_playbooks_previews()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                       | Type                                                                                                            | Required                                                                                                        | Description                                                                                                     |
| --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                            | *Optional[float]*                                                                                               | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `only_subscribed`                                                                                               | *Optional[bool]*                                                                                                | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `status_filter`                                                                                                 | [Optional[models.TextqlRPCPublicPlaybookPlaybookStatus]](../../models/textqlrpcpublicplaybookplaybookstatus.md) | :heavy_minus_sign:                                                                                              | N/A                                                                                                             |
| `retries`                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                | :heavy_minus_sign:                                                                                              | Configuration to override the default retry behavior of the client.                                             |

### Response

**[models.PlaybookServiceGetPlaybooksPreviewsResponse](../../models/playbookservicegetplaybookspreviewsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_report_by_id

Get a single report by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetReportById" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetReportById" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.get_report_by_id()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `report_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceGetReportByIDResponse](../../models/playbookservicegetreportbyidresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_teams_channels_for_context_playbook

ListTeamsChannelsForContextPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_ListTeamsChannelsForContextPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/ListTeamsChannelsForContextPlaybook" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.list_teams_channels_for_context_playbook()

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

**[models.PlaybookServiceListTeamsChannelsForContextPlaybookResponse](../../models/playbookservicelistteamschannelsforcontextplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## remove_dataset

RemoveDataset

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_RemoveDataset" method="post" path="/textql.rpc.public.playbook.PlaybookService/RemoveDataset" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.remove_dataset()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dataset_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceRemoveDatasetResponse](../../models/playbookserviceremovedatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## unset_slack_channel_context_playbook

Unset the context playbook for a Slack channel. This clears any association
 so that messages in this channel no longer use a specific playbook context.

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_UnsetSlackChannelContextPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/UnsetSlackChannelContextPlaybook" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.unset_slack_channel_context_playbook()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `slack_channel_id`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceUnsetSlackChannelContextPlaybookResponse](../../models/playbookserviceunsetslackchannelcontextplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update

UpdatePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_UpdatePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/UpdatePlaybook" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.playbook_service.update()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                      | Type                                                                                                                                                           | Required                                                                                                                                                       | Description                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                                                           | *Optional[float]*                                                                                                                                              | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `playbook_id`                                                                                                                                                  | *Optional[str]*                                                                                                                                                | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `name`                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `prompt`                                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `status`                                                                                                                                                       | [Optional[models.TextqlRPCPublicPlaybookPlaybookStatus]](../../models/textqlrpcpublicplaybookplaybookstatus.md)                                                | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `trigger_type`                                                                                                                                                 | [Optional[models.TextqlRPCPublicPlaybookPlaybookTriggerType]](../../models/textqlrpcpublicplaybookplaybooktriggertype.md)                                      | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `cron_string`                                                                                                                                                  | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `dataset_ids`                                                                                                                                                  | [Optional[models.TextqlRPCPublicPlaybookStringList]](../../models/textqlrpcpublicplaybookstringlist.md)                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `connector_id`                                                                                                                                                 | *OptionalNullable[int]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | : warning: ** DEPRECATED **: This will be removed in a future release, please migrate away from it as soon as possible.<br/><br/>Deprecated: use connector_ids instead |
| `reference_report_id`                                                                                                                                          | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `paradigm_options`                                                                                                                                             | [Optional[models.TextqlRPCPublicParadigmParadigmOptions]](../../models/textqlrpcpublicparadigmparadigmoptions.md)                                              | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `paradigm_type`                                                                                                                                                | [Optional[models.TextqlRPCParadigmParamsParadigmType]](../../models/textqlrpcparadigmparamsparadigmtype.md)                                                    | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `email_addresses`                                                                                                                                              | [Optional[models.TextqlRPCPublicPlaybookStringList]](../../models/textqlrpcpublicplaybookstringlist.md)                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `slack_channel_id`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `tagged_slack_user_ids`                                                                                                                                        | [Optional[models.TextqlRPCPublicPlaybookStringList]](../../models/textqlrpcpublicplaybookstringlist.md)                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `report_output_style`                                                                                                                                          | [Optional[models.TextqlRPCPublicPlaybookPlaybookReportStyle]](../../models/textqlrpcpublicplaybookplaybookreportstyle.md)                                      | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `template_header_id`                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `selected_template_data_ids`                                                                                                                                   | [Optional[models.TextqlRPCPublicPlaybookStringList]](../../models/textqlrpcpublicplaybookstringlist.md)                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `max_concurrent_templates`                                                                                                                                     | *OptionalNullable[int]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `auto_optimize_concurrency`                                                                                                                                    | *OptionalNullable[bool]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `connector_ids`                                                                                                                                                | [Optional[models.TextqlRPCPublicPlaybookInt32List]](../../models/textqlrpcpublicplaybookint32list.md)                                                          | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `template_data_filters`                                                                                                                                        | [Optional[models.TextqlRPCPublicPlaybookFilterConditionList]](../../models/textqlrpcpublicplaybookfilterconditionlist.md)                                      | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `llm_model`                                                                                                                                                    | [Optional[models.TextqlRPCPublicChatLlmModel]](../../models/textqlrpcpublicchatllmmodel.md)                                                                    | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `chat_access_mode`                                                                                                                                             | [Optional[models.TextqlRPCPublicPlaybookChatAccessMode]](../../models/textqlrpcpublicplaybookchataccessmode.md)                                                | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `chat_access_overrides`                                                                                                                                        | [Optional[models.TextqlRPCPublicPlaybookChatAccessOverrideList]](../../models/textqlrpcpublicplaybookchataccessoverridelist.md)                                | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `chat_is_public`                                                                                                                                               | *OptionalNullable[bool]*                                                                                                                                       | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `dashboard_ids`                                                                                                                                                | [Optional[models.TextqlRPCPublicPlaybookStringList]](../../models/textqlrpcpublicplaybookstringlist.md)                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `recipient_email_column`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `teams_channel_id`                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `tagged_teams_user_aad_ids`                                                                                                                                    | [Optional[models.TextqlRPCPublicPlaybookStringList]](../../models/textqlrpcpublicplaybookstringlist.md)                                                        | :heavy_minus_sign:                                                                                                                                             | N/A                                                                                                                                                            |
| `retries`                                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                               | :heavy_minus_sign:                                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                                            |

### Response

**[models.PlaybookServiceUpdatePlaybookResponse](../../models/playbookserviceupdateplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |