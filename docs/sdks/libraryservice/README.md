# LibraryService

## Overview

### Available Operations

* [library_service_list_golden_files](#library_service_list_golden_files) - ListGoldenFiles
* [library_service_set_library_file_golden](#library_service_set_library_file_golden) - SetLibraryFileGolden

## library_service_list_golden_files

ListGoldenFiles

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_ListGoldenFiles" method="post" path="/textql.rpc.public.patches.LibraryService/ListGoldenFiles" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.library_service.library_service_list_golden_files(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                           | Type                                                                                                                | Required                                                                                                            | Description                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                              | [models.TextqlRPCPublicPatchesListGoldenFilesRequest](../../models/textqlrpcpublicpatcheslistgoldenfilesrequest.md) | :heavy_check_mark:                                                                                                  | N/A                                                                                                                 |
| `connect_timeout_ms`                                                                                                | *Optional[float]*                                                                                                   | :heavy_minus_sign:                                                                                                  | N/A                                                                                                                 |
| `retries`                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                    | :heavy_minus_sign:                                                                                                  | Configuration to override the default retry behavior of the client.                                                 |

### Response

**[models.LibraryServiceListGoldenFilesResponse](../../models/libraryservicelistgoldenfilesresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## library_service_set_library_file_golden

SetLibraryFileGolden

### Example Usage

<!-- UsageSnippet language="python" operationID="LibraryService_SetLibraryFileGolden" method="post" path="/textql.rpc.public.patches.LibraryService/SetLibraryFileGolden" -->
```python
import os
from textql_sdk import Textql


with Textql(
    api_key=os.getenv("TEXTQL_API_KEY", ""),
) as textql:

    res = textql.library_service.library_service_set_library_file_golden()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `path`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `golden`                                                            | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | true = certify, false = retire                                      |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.LibraryServiceSetLibraryFileGoldenResponse](../../models/libraryservicesetlibraryfilegoldenresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |