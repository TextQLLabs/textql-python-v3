# AuditLogService

## Overview

### Available Operations

* [configure_s3_export](#configure_s3_export) - ConfigureS3Export
* [get_s3_export_config](#get_s3_export_config) - GetS3ExportConfig
* [test_otlp_export_connection](#test_otlp_export_connection) - TestOtlpExportConnection
* [trigger_s3_export](#trigger_s3_export) - TriggerS3Export

## configure_s3_export

ConfigureS3Export

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogService_ConfigureS3Export" method="post" path="/textql.rpc.public.audit_log.AuditLogService/ConfigureS3Export" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.audit_log_service.configure_s3_export()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                               | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `connect_timeout_ms`                                                                                    | *Optional[float]*                                                                                       | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `bucket`                                                                                                | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `region`                                                                                                | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `prefix`                                                                                                | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `aws_access_key_id`                                                                                     | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `aws_secret_access_key`                                                                                 | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `enabled`                                                                                               | *Optional[bool]*                                                                                        | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `auth_mode`                                                                                             | [Optional[models.TextqlRPCPublicAuditLogS3AuthMode]](../../models/textqlrpcpublicauditlogs3authmode.md) | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `role_arn`                                                                                              | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `external_id`                                                                                           | *Optional[str]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `export_interval_seconds`                                                                               | *Optional[int]*                                                                                         | :heavy_minus_sign:                                                                                      | N/A                                                                                                     |
| `retries`                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                        | :heavy_minus_sign:                                                                                      | Configuration to override the default retry behavior of the client.                                     |

### Response

**[models.AuditLogServiceConfigureS3ExportResponse](../../models/auditlogserviceconfigures3exportresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## get_s3_export_config

GetS3ExportConfig

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogService_GetS3ExportConfig" method="post" path="/textql.rpc.public.audit_log.AuditLogService/GetS3ExportConfig" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.audit_log_service.get_s3_export_config(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                 | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                    | [models.TextqlRPCPublicAuditLogGetS3ExportConfigRequest](../../models/textqlrpcpublicauditloggets3exportconfigrequest.md) | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `connect_timeout_ms`                                                                                                      | *Optional[float]*                                                                                                         | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `retries`                                                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                          | :heavy_minus_sign:                                                                                                        | Configuration to override the default retry behavior of the client.                                                       |

### Response

**[models.AuditLogServiceGetS3ExportConfigResponse](../../models/auditlogservicegets3exportconfigresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## test_otlp_export_connection

TestOtlpExportConnection

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogService_TestOtlpExportConnection" method="post" path="/textql.rpc.public.audit_log.AuditLogService/TestOtlpExportConnection" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.audit_log_service.test_otlp_export_connection()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `connect_timeout_ms`                                                | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_endpoint`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_headers`                                                      | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `otlp_protocol`                                                     | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.AuditLogServiceTestOtlpExportConnectionResponse](../../models/auditlogservicetestotlpexportconnectionresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |

## trigger_s3_export

TriggerS3Export

### Example Usage

<!-- UsageSnippet language="python" operationID="AuditLogService_TriggerS3Export" method="post" path="/textql.rpc.public.audit_log.AuditLogService/TriggerS3Export" -->
```python
from textql_sdk import TextQL


with TextQL() as text_ql:

    res = text_ql.audit_log_service.trigger_s3_export(body={})

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                             | Type                                                                                                                  | Required                                                                                                              | Description                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `body`                                                                                                                | [models.TextqlRPCPublicAuditLogTriggerS3ExportRequest](../../models/textqlrpcpublicauditlogtriggers3exportrequest.md) | :heavy_check_mark:                                                                                                    | N/A                                                                                                                   |
| `connect_timeout_ms`                                                                                                  | *Optional[float]*                                                                                                     | :heavy_minus_sign:                                                                                                    | N/A                                                                                                                   |
| `retries`                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                      | :heavy_minus_sign:                                                                                                    | Configuration to override the default retry behavior of the client.                                                   |

### Response

**[models.AuditLogServiceTriggerS3ExportResponse](../../models/auditlogservicetriggers3exportresponse.md)**

### Errors

| Error Type                | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.TextqlDefaultError | 4XX, 5XX                  | \*/\*                     |