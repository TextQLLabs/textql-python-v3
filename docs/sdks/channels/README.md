# Channels

## Overview

### Available Operations

* [list](#list) - ListChannels

## list

ListChannels

### Example Usage

<!-- UsageSnippet language="python" operationID="TeamsService_ListChannels" method="post" path="/textql.rpc.public.teams.TeamsService/ListChannels" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.channels.list(body={})

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

**[models.TeamsServiceListChannelsResponse](../../models/teamsservicelistchannelsresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |