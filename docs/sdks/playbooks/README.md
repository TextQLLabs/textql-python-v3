# Playbooks

## Overview

### Available Operations

* [attach_dashboard](#attach_dashboard) - AttachDashboard
* [attach_dataset](#attach_dataset) - AttachDataset
* [cancel_template_execution](#cancel_template_execution) - Cancel template execution for a specific template header
* [create_playbook](#create_playbook) - CreatePlaybook
* [deactivate](#deactivate) - DeactivatePlaybook
* [delete](#delete) - DeletePlaybook
* [demo_playbook](#demo_playbook) - DemoPlaybook
* [deploy](#deploy) - DeployPlaybook
* [duplicate](#duplicate) - DuplicatePlaybook
* [favorite_report](#favorite_report) - Favorite report management
* [get_active_subscribed_count](#get_active_subscribed_count) - GetActiveSubscribedPlaybooksCount
* [get_chat_reports_summary](#get_chat_reports_summary) - Lightweight endpoint for chat report drawer - returns summaries without full blocks
* [get_members_with](#get_members_with) - GetMembersWithPlaybooks
* [fetch](#fetch) - GetPlaybook
* [get_batch_run](#get_batch_run) - Get a specific batch run
* [get_extended_qn](#get_extended_qn) - Playbook Extended quant.new operations
* [get_playbook_lineage](#get_playbook_lineage) - GetPlaybookLineage
* [get_reports](#get_reports) - GetPlaybookReports
* [get_playbook_reports_batch](#get_playbook_reports_batch) - Get reports for multiple template data IDs in a single batch request
* [get](#get) - GetPlaybooks
* [get_playbooks_previews](#get_playbooks_previews) - GetPlaybooksPreviews
* [get_qn_playbook](#get_qn_playbook) - GetQNPlaybook
* [get_report_by_id](#get_report_by_id) - Get a single report by ID
* [get_reports_with_filters](#get_reports_with_filters) - GetReportsWithFilters
* [list_slack_channel_context_playbooks](#list_slack_channel_context_playbooks) - List all Slack channels context playbook mappings for the organization
* [list_all_teams_channel_context_playbooks](#list_all_teams_channel_context_playbooks) - ListAllTeamsChannelContextPlaybooks
* [list_batch_runs](#list_batch_runs) - List batch runs for a playbook
* [list_slack_channels_for_context](#list_slack_channels_for_context) - List Slack channel IDs where the given playbook is set as the context
* [list_teams_channels_for_context_playbook](#list_teams_channels_for_context_playbook) - ListTeamsChannelsForContextPlaybook
* [mark_report_as_read](#mark_report_as_read) - Report read tracking
* [preview_slack_report](#preview_slack_report) - PreviewSlackReport
* [remove_dashboard](#remove_dashboard) - RemoveDashboard
* [remove_dataset](#remove_dataset) - RemoveDataset
* [run](#run) - RunPlaybook
* [set_slack_channel_context_playbook](#set_slack_channel_context_playbook) - Set the context playbook for a Slack channel. This associates the given  playbook to a Slack channel so that Slack messages in that channel use the  playbook's context by default.
* [set_teams_channel_context](#set_teams_channel_context) - SetTeamsChannelContextPlaybook
* [subscribe](#subscribe) - SubscribeToPlaybook
* [unset_slack_channel_context_playbook](#unset_slack_channel_context_playbook) - Unset the context playbook for a Slack channel. This clears any association  so that messages in this channel no longer use a specific playbook context.
* [unset_teams_channel_context](#unset_teams_channel_context) - UnsetTeamsChannelContextPlaybook
* [unsubscribe](#unsubscribe) - UnsubscribeFromPlaybook
* [update](#update) - UpdatePlaybook
* [update_extended_qn](#update_extended_qn) - UpdatePlaybookExtendedQn

## attach_dashboard

AttachDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_AttachDashboard" method="post" path="/textql.rpc.public.playbook.PlaybookService/AttachDashboard" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.attach_dashboard()

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

**[models.PlaybookServiceAttachDashboardResponse](../../models/playbookserviceattachdashboardresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## attach_dataset

AttachDataset

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_AttachDataset" method="post" path="/textql.rpc.public.playbook.PlaybookService/AttachDataset" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.attach_dataset()

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

**[models.PlaybookServiceAttachDatasetResponse](../../models/playbookserviceattachdatasetresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## cancel_template_execution

Cancel template execution for a specific template header

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_CancelTemplateExecution" method="post" path="/textql.rpc.public.playbook.PlaybookService/CancelTemplateExecution" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.cancel_template_execution()

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

## create_playbook

CreatePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_CreatePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/CreatePlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.create_playbook(body={})

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

## deactivate

DeactivatePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_DeactivatePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/DeactivatePlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.deactivate()

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

**[models.PlaybookServiceDeactivatePlaybookResponse](../../models/playbookservicedeactivateplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## delete

DeletePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_DeletePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/DeletePlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.delete()

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

**[models.PlaybookServiceDeletePlaybookResponse](../../models/playbookservicedeleteplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## demo_playbook

DemoPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_DemoPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/DemoPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.demo_playbook()

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

## deploy

DeployPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_DeployPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/DeployPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.deploy()

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

**[models.PlaybookServiceDeployPlaybookResponse](../../models/playbookservicedeployplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## duplicate

DuplicatePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_DuplicatePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/DuplicatePlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.duplicate()

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

## favorite_report

Favorite report management

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_FavoriteReport" method="post" path="/textql.rpc.public.playbook.PlaybookService/FavoriteReport" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.favorite_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `report_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceFavoriteReportResponse](../../models/playbookservicefavoritereportresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_active_subscribed_count

GetActiveSubscribedPlaybooksCount

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetActiveSubscribedPlaybooksCount" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetActiveSubscribedPlaybooksCount" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_active_subscribed_count(body={})

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

## get_chat_reports_summary

Lightweight endpoint for chat report drawer - returns summaries without full blocks

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetChatReportsSummary" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetChatReportsSummary" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_chat_reports_summary()

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

**[models.PlaybookServiceGetChatReportsSummaryResponse](../../models/playbookservicegetchatreportssummaryresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_members_with

GetMembersWithPlaybooks

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetMembersWithPlaybooks" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetMembersWithPlaybooks" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_members_with(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                             | Type                                                                                                                                  | Required                                                                                                                              | Description                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                | [models.TextqlRPCPublicPlaybookGetMembersWithPlaybooksRequest](../../models/textqlrpcpublicplaybookgetmemberswithplaybooksrequest.md) | :heavy_check_mark:                                                                                                                    | N/A                                                                                                                                   |
| `connect_timeout_ms`                                                                                                                  | *Optional[float]*                                                                                                                     | :heavy_minus_sign:                                                                                                                    | N/A                                                                                                                                   |
| `retries`                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                      | :heavy_minus_sign:                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                   |

### Response

**[models.PlaybookServiceGetMembersWithPlaybooksResponse](../../models/playbookservicegetmemberswithplaybooksresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## fetch

GetPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.fetch()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceGetPlaybookResponse](../../models/playbookservicegetplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_batch_run

Get a specific batch run

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookBatchRun" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookBatchRun" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_batch_run()

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

## get_extended_qn

Playbook Extended quant.new operations

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookExtendedQn" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookExtendedQn" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_extended_qn()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceGetPlaybookExtendedQnResponse](../../models/playbookservicegetplaybookextendedqnresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_playbook_lineage

GetPlaybookLineage

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookLineage" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookLineage" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_playbook_lineage()

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

## get_reports

GetPlaybookReports

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookReports" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookReports" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_reports()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `limit`                                                             | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `offset`                                                            | *Optional[int]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `chat_id`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | UUID                                                                |
| `template_data_id`                                                  | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | UUID                                                                |
| `batch_run_id`                                                      | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | UUID - filter reports by batch run                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceGetPlaybookReportsResponse](../../models/playbookservicegetplaybookreportsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_playbook_reports_batch

Get reports for multiple template data IDs in a single batch request

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybookReportsBatch" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybookReportsBatch" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_playbook_reports_batch()

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

## get

GetPlaybooks

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybooks" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybooks" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                                  | *Optional[float]*                                                                                                     | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `member_only`                                                                                                         | *Optional[bool]*                                                                                                      | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `limit`                                                                                                               | *Optional[int]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `offset`                                                                                                              | *Optional[int]*                                                                                                       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `search_term`                                                                                                         | *OptionalNullable[str]*                                                                                               | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `status_filter`                                                                                                       | [Optional[models.TextqlRPCPublicPlaybookPlaybookStatus]](../../models/textqlrpcpublicplaybookplaybookstatus.md)       | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `creator_member_id`                                                                                                   | *OptionalNullable[str]*                                                                                               | :heavy_minus_sign:                                                                                                    | single-select; superseded by `creator_member_ids` when that is non-empty                                              |
| `sort_by`                                                                                                             | [Optional[models.TextqlRPCPublicPlaybookPlaybookSortField]](../../models/textqlrpcpublicplaybookplaybooksortfield.md) | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `sort_direction`                                                                                                      | [Optional[models.TextqlRPCPublicCommonSortDirection]](../../models/textqlrpcpubliccommonsortdirection.md)             | :heavy_minus_sign:                                                                                                    | Common enum for sort direction used across multiple services                                                          |
| `subscribed_first`                                                                                                    | *OptionalNullable[bool]*                                                                                              | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `only_subscribed`                                                                                                     | *OptionalNullable[bool]*                                                                                              | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `shared_with_me`                                                                                                      | *OptionalNullable[bool]*                                                                                              | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `include_shared_drafts`                                                                                               | *OptionalNullable[bool]*                                                                                              | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `statuses`                                                                                                            | List[[models.TextqlRPCPublicPlaybookPlaybookStatus](../../models/textqlrpcpublicplaybookplaybookstatus.md)]           | :heavy_minus_sign:                                                                                                    | Multi-select filters (union). Each supersedes its single-value counterpart when non-empty.                            |
| `creator_member_ids`                                                                                                  | List[*str*]                                                                                                           | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.PlaybookServiceGetPlaybooksResponse](../../models/playbookservicegetplaybooksresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_playbooks_previews

GetPlaybooksPreviews

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetPlaybooksPreviews" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetPlaybooksPreviews" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_playbooks_previews()

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

## get_qn_playbook

GetQNPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetQNPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetQNPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_qn_playbook()

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

**[models.PlaybookServiceGetQNPlaybookResponse](../../models/playbookservicegetqnplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_report_by_id

Get a single report by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetReportById" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetReportById" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.get_report_by_id()

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

## get_reports_with_filters

GetReportsWithFilters

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_GetReportsWithFilters" method="post" path="/textql.rpc.public.playbook.PlaybookService/GetReportsWithFilters" -->
```python
from textql_sdk import Textql
from textql_sdk.utils import parse_datetime


with Textql() as textql:

    res = textql.playbooks.get_reports_with_filters(filters={
        "start_time": parse_datetime("2023-01-15T01:30:15.01Z"),
        "end_time": parse_datetime("2023-01-15T01:30:15.01Z"),
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                     | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                          | *Optional[float]*                                                                                             | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `filters`                                                                                                     | [Optional[models.TextqlRPCPublicPlaybookReportFilters]](../../models/textqlrpcpublicplaybookreportfilters.md) | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `retries`                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                              | :heavy_minus_sign:                                                                                            | Configuration to override the default retry behavior of the client.                                           |

### Response

**[models.PlaybookServiceGetReportsWithFiltersResponse](../../models/playbookservicegetreportswithfiltersresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_slack_channel_context_playbooks

List all Slack channels context playbook mappings for the organization

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_ListAllSlackChannelContextPlaybooks" method="post" path="/textql.rpc.public.playbook.PlaybookService/ListAllSlackChannelContextPlaybooks" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.list_slack_channel_context_playbooks(body={})

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

## list_all_teams_channel_context_playbooks

ListAllTeamsChannelContextPlaybooks

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_ListAllTeamsChannelContextPlaybooks" method="post" path="/textql.rpc.public.playbook.PlaybookService/ListAllTeamsChannelContextPlaybooks" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.list_all_teams_channel_context_playbooks(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                     | Type                                                                                                                                                          | Required                                                                                                                                                      | Description                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                                                        | [models.TextqlRPCPublicPlaybookListAllTeamsChannelContextPlaybooksRequest](../../models/textqlrpcpublicplaybooklistallteamschannelcontextplaybooksrequest.md) | :heavy_check_mark:                                                                                                                                            | N/A                                                                                                                                                           |
| `connect_timeout_ms`                                                                                                                                          | *Optional[float]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                            | N/A                                                                                                                                                           |
| `retries`                                                                                                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                              | :heavy_minus_sign:                                                                                                                                            | Configuration to override the default retry behavior of the client.                                                                                           |

### Response

**[models.PlaybookServiceListAllTeamsChannelContextPlaybooksResponse](../../models/playbookservicelistallteamschannelcontextplaybooksresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_batch_runs

List batch runs for a playbook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_ListPlaybookBatchRuns" method="post" path="/textql.rpc.public.playbook.PlaybookService/ListPlaybookBatchRuns" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.list_batch_runs()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `limit`                                                             | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Max number of results (default: 50)                                 |
| `offset`                                                            | *OptionalNullable[int]*                                             | :heavy_minus_sign:                                                  | Offset for pagination (default: 0)                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceListPlaybookBatchRunsResponse](../../models/playbookservicelistplaybookbatchrunsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_slack_channels_for_context

List Slack channel IDs where the given playbook is set as the context

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_ListSlackChannelsForContextPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/ListSlackChannelsForContextPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.list_slack_channels_for_context()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceListSlackChannelsForContextPlaybookResponse](../../models/playbookservicelistslackchannelsforcontextplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_teams_channels_for_context_playbook

ListTeamsChannelsForContextPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_ListTeamsChannelsForContextPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/ListTeamsChannelsForContextPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.list_teams_channels_for_context_playbook()

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

## mark_report_as_read

Report read tracking

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_MarkReportAsRead" method="post" path="/textql.rpc.public.playbook.PlaybookService/MarkReportAsRead" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.mark_report_as_read()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `report_id`                                                         | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceMarkReportAsReadResponse](../../models/playbookservicemarkreportasreadresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## preview_slack_report

PreviewSlackReport

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_PreviewSlackReport" method="post" path="/textql.rpc.public.playbook.PlaybookService/PreviewSlackReport" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.preview_slack_report()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                              | *Optional[float]*                                                                                 | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `playbook_id`                                                                                     | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `cell`                                                                                            | [Optional[models.TextqlRPCPublicCellsReportCell]](../../models/textqlrpcpubliccellsreportcell.md) | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `chat_id`                                                                                         | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `slack_channel_id`                                                                                | *Optional[str]*                                                                                   | :heavy_minus_sign:                                                                                | N/A                                                                                               |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.PlaybookServicePreviewSlackReportResponse](../../models/playbookservicepreviewslackreportresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## remove_dashboard

RemoveDashboard

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_RemoveDashboard" method="post" path="/textql.rpc.public.playbook.PlaybookService/RemoveDashboard" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.remove_dashboard()

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

## remove_dataset

RemoveDataset

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_RemoveDataset" method="post" path="/textql.rpc.public.playbook.PlaybookService/RemoveDataset" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.remove_dataset()

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

## run

RunPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_RunPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/RunPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.run()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `dry_run`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | If true, runs without sending notifications                         |
| `template_id`                                                       | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceRunPlaybookResponse](../../models/playbookservicerunplaybookresponse.md)**

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
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.set_slack_channel_context_playbook()

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

## set_teams_channel_context

SetTeamsChannelContextPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_SetTeamsChannelContextPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/SetTeamsChannelContextPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.set_teams_channel_context()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `teams_channel_id`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceSetTeamsChannelContextPlaybookResponse](../../models/playbookservicesetteamschannelcontextplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## subscribe

SubscribeToPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_SubscribeToPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/SubscribeToPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.subscribe()

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

**[models.PlaybookServiceSubscribeToPlaybookResponse](../../models/playbookservicesubscribetoplaybookresponse.md)**

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
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.unset_slack_channel_context_playbook()

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

## unset_teams_channel_context

UnsetTeamsChannelContextPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_UnsetTeamsChannelContextPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/UnsetTeamsChannelContextPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.unset_teams_channel_context()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `teams_channel_id`                                                  | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceUnsetTeamsChannelContextPlaybookResponse](../../models/playbookserviceunsetteamschannelcontextplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## unsubscribe

UnsubscribeFromPlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_UnsubscribeFromPlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/UnsubscribeFromPlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.unsubscribe()

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

**[models.PlaybookServiceUnsubscribeFromPlaybookResponse](../../models/playbookserviceunsubscribefromplaybookresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## update

UpdatePlaybook

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_UpdatePlaybook" method="post" path="/textql.rpc.public.playbook.PlaybookService/UpdatePlaybook" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.update()

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

## update_extended_qn

UpdatePlaybookExtendedQn

### Example Usage

<!-- UsageSnippet language="python" operationID="PlaybookService_UpdatePlaybookExtendedQn" method="post" path="/textql.rpc.public.playbook.PlaybookService/UpdatePlaybookExtendedQn" -->
```python
from textql_sdk import Textql


with Textql() as textql:

    res = textql.playbooks.update_extended_qn()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `playbook_id`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | UUID                                                                |
| `summary`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `template`                                                          | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 |
| `tags`                                                              | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 |
| `ratings`                                                           | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | JSON string for flexible rating data                                |
| `favorite_report_id`                                                | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | UUID                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.PlaybookServiceUpdatePlaybookExtendedQnResponse](../../models/playbookserviceupdateplaybookextendedqnresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |