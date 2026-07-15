# SlackService

## Overview

### Available Operations

* [list_channels](#list_channels) - ListChannels
* [list_installations](#list_installations) - ListInstallations

## list_channels

ListChannels

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_ListChannels" method="post" path="/textql.rpc.public.slack.SlackService/ListChannels" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack_service.list_channels(body={})

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

**[models.SlackServiceListChannelsResponse](../../models/slackservicelistchannelsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## list_installations

ListInstallations

### Example Usage

<!-- UsageSnippet language="python" operationID="SlackService_ListInstallations" method="post" path="/textql.rpc.public.slack.SlackService/ListInstallations" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.slack_service.list_installations(body={})

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

**[models.SlackServiceListInstallationsResponse](../../models/slackservicelistinstallationsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |