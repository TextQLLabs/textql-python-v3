"""Unit tests for sdk.audit_logs (AuditLogService) covering all 11 operations."""
from __future__ import annotations

import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, utils

PATH_PREFIX = "/textql.rpc.public.audit_log.AuditLogService"


# ---------------------------------------------------------------------------
# ConfigureOtlpExport
# ---------------------------------------------------------------------------


def test_configure_otlp_export_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"config": {"enabled": True, "otlpEndpoint": "https://otel.example.com"}}
        )
    )

    result = bundle.sdk.audit_logs.configure_otlp_export(
        enabled=True,
        otlp_endpoint="https://otel.example.com",
        otlp_headers="Authorization=Bearer xyz",
        otlp_protocol="grpc",
        push_interval_seconds=60,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ConfigureOtlpExport"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["enabled"] is True
    assert body["otlpEndpoint"] == "https://otel.example.com"
    assert body["otlpHeaders"] == "Authorization=Bearer xyz"
    assert body["otlpProtocol"] == "grpc"
    assert body["pushIntervalSeconds"] == 60

    assert result.config.enabled is True
    assert result.config.otlp_endpoint == "https://otel.example.com"


async def test_configure_otlp_export_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"enabled": False}}))

    result = await bundle.sdk.audit_logs.configure_otlp_export_async(enabled=False)

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ConfigureOtlpExport"
    assert result.config.enabled is False


def test_configure_otlp_export_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad endpoint"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.configure_otlp_export(otlp_endpoint="not-a-url")

    assert exc_info.value.status_code == 400
    assert "bad endpoint" in str(exc_info.value)


async def test_configure_otlp_export_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.configure_otlp_export_async(enabled=True)

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ConfigureS3Export
# ---------------------------------------------------------------------------


def test_configure_s3_export_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"bucket": "my-bucket", "region": "us-east-1"}}))

    result = bundle.sdk.audit_logs.configure_s3_export(
        bucket="my-bucket",
        region="us-east-1",
        prefix="logs/",
        aws_access_key_id="AKIA...",
        aws_secret_access_key="secret",
        enabled=True,
        role_arn="arn:aws:iam::123:role/x",
        external_id="ext-1",
        export_interval_seconds=300,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ConfigureS3Export"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["bucket"] == "my-bucket"
    assert body["region"] == "us-east-1"
    assert body["prefix"] == "logs/"
    assert body["awsAccessKeyId"] == "AKIA..."
    assert body["awsSecretAccessKey"] == "secret"
    assert body["enabled"] is True
    assert body["roleArn"] == "arn:aws:iam::123:role/x"
    assert body["externalId"] == "ext-1"
    assert body["exportIntervalSeconds"] == 300

    assert result.config.bucket == "my-bucket"
    assert result.config.region == "us-east-1"


async def test_configure_s3_export_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"bucket": "b2"}}))

    result = await bundle.sdk.audit_logs.configure_s3_export_async(bucket="b2")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ConfigureS3Export"
    assert result.config.bucket == "b2"


def test_configure_s3_export_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid bucket"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.configure_s3_export(bucket="")

    assert exc_info.value.status_code == 422
    assert "invalid bucket" in str(exc_info.value)


async def test_configure_s3_export_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.configure_s3_export_async(bucket="b")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# DeleteOtlpExportConfig
# ---------------------------------------------------------------------------


def test_delete_otlp_export_config_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.delete_otlp_export_config(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/DeleteOtlpExportConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}


async def test_delete_otlp_export_config_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.delete_otlp_export_config_async(body={})

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/DeleteOtlpExportConfig"


def test_delete_otlp_export_config_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no config"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.delete_otlp_export_config(body={})

    assert exc_info.value.status_code == 404
    assert "no config" in str(exc_info.value)


async def test_delete_otlp_export_config_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.delete_otlp_export_config_async(body={})

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# DeleteS3ExportConfig
# ---------------------------------------------------------------------------


def test_delete_s3_export_config_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.delete_s3_export_config(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/DeleteS3ExportConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


async def test_delete_s3_export_config_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.delete_s3_export_config_async(body={})

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/DeleteS3ExportConfig"


def test_delete_s3_export_config_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no config"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.delete_s3_export_config(body={})

    assert exc_info.value.status_code == 404


async def test_delete_s3_export_config_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.delete_s3_export_config_async(body={})

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# GetOtlpExportConfig
# ---------------------------------------------------------------------------


def test_get_otlp_export_config_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"config": {"enabled": True, "otlpProtocol": "http"}})
    )

    result = bundle.sdk.audit_logs.get_otlp_export_config(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/GetOtlpExportConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert result.config.enabled is True
    assert result.config.otlp_protocol == "http"


async def test_get_otlp_export_config_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"enabled": False}}))

    result = await bundle.sdk.audit_logs.get_otlp_export_config_async(body={})

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/GetOtlpExportConfig"
    assert result.config.enabled is False


def test_get_otlp_export_config_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no config"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.get_otlp_export_config(body={})

    assert exc_info.value.status_code == 404


async def test_get_otlp_export_config_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.get_otlp_export_config_async(body={})

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# GetS3ExportConfig
# ---------------------------------------------------------------------------


def test_get_s3_export_config_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"bucket": "b1", "region": "eu-west-1"}}))

    result = bundle.sdk.audit_logs.get_s3_export_config(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/GetS3ExportConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert result.config.bucket == "b1"
    assert result.config.region == "eu-west-1"


async def test_get_s3_export_config_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"bucket": "b2"}}))

    result = await bundle.sdk.audit_logs.get_s3_export_config_async(body={})

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/GetS3ExportConfig"
    assert result.config.bucket == "b2"


def test_get_s3_export_config_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no config"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.get_s3_export_config(body={})

    assert exc_info.value.status_code == 404


async def test_get_s3_export_config_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.get_s3_export_config_async(body={})

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ListAuditLogs
# ---------------------------------------------------------------------------


def test_list_sync_with_optional_nullable_fields(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "entries": [{"id": "e1", "actorId": "u1"}, {"id": "e2", "actorId": "u2"}],
                "nextCursor": "cursor-2",
            },
        )
    )

    result = bundle.sdk.audit_logs.list(
        category="auth",
        actor_id="u1",
        action="login",
        resource_type="session",
        cursor="cursor-1",
        page_size=25,
        search_term="failed",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListAuditLogs"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["category"] == "auth"
    assert body["actorId"] == "u1"
    assert body["action"] == "login"
    assert body["resourceType"] == "session"
    assert body["cursor"] == "cursor-1"
    assert body["pageSize"] == 25
    assert body["searchTerm"] == "failed"

    assert len(result.entries) == 2
    assert result.entries[0].id == "e1"
    assert result.next_cursor == "cursor-2"


async def test_list_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"entries": []}))

    result = await bundle.sdk.audit_logs.list_async()

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ListAuditLogs"
    assert result.entries == []


def test_list_optional_nullable_unset_omits_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.list()

    body = bundle.transport.body_json()
    assert "category" not in body
    assert "actorId" not in body
    assert "action" not in body
    assert "resourceType" not in body
    assert "cursor" not in body
    assert "pageSize" not in body
    assert "searchTerm" not in body


def test_list_optional_nullable_explicit_none_serializes_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.list(
        category=None,
        actor_id=None,
        action=None,
        resource_type=None,
        cursor=None,
        page_size=None,
        search_term=None,
    )

    body = bundle.transport.body_json()
    assert body["category"] is None
    assert body["actorId"] is None
    assert body["action"] is None
    assert body["resourceType"] is None
    assert body["cursor"] is None
    assert body["pageSize"] is None
    assert body["searchTerm"] is None


def test_list_after_datetime_serializes_as_rfc3339(make_sdk):
    from datetime import datetime, timezone

    bundle = make_sdk(lambda req: json_response(200, {}))

    after = datetime(2024, 1, 15, 1, 30, 15, tzinfo=timezone.utc)
    bundle.sdk.audit_logs.list(after=after)

    body = bundle.transport.body_json()
    assert "after" in body
    assert body["after"].startswith("2024-01-15T01:30:15")


def test_list_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad cursor"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.list(cursor="invalid")

    assert exc_info.value.status_code == 400
    assert "bad cursor" in str(exc_info.value)


async def test_list_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.list_async()

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# TestOtlpExportConnection
# ---------------------------------------------------------------------------


def test_test_otlp_export_connection_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.audit_logs.test_otlp_export_connection(
        otlp_endpoint="https://otel.example.com",
        otlp_headers="k=v",
        otlp_protocol="grpc",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/TestOtlpExportConnection"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["otlpEndpoint"] == "https://otel.example.com"
    assert body["otlpHeaders"] == "k=v"
    assert body["otlpProtocol"] == "grpc"


async def test_test_otlp_export_connection_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.test_otlp_export_connection_async(otlp_endpoint="https://x")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/TestOtlpExportConnection"


def test_test_otlp_export_connection_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "cannot connect"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.test_otlp_export_connection(otlp_endpoint="bad")

    assert exc_info.value.status_code == 400
    assert "cannot connect" in str(exc_info.value)


async def test_test_otlp_export_connection_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.test_otlp_export_connection_async(otlp_endpoint="x")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# TestS3ExportConnection
# ---------------------------------------------------------------------------


def test_test_s3_export_connection_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.audit_logs.test_s3_export_connection(
        bucket="b1",
        region="us-east-1",
        aws_access_key_id="AKIA",
        aws_secret_access_key="secret",
        role_arn="arn:aws:iam::123:role/x",
        external_id="ext",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/TestS3ExportConnection"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["bucket"] == "b1"
    assert body["region"] == "us-east-1"
    assert body["awsAccessKeyId"] == "AKIA"
    assert body["awsSecretAccessKey"] == "secret"
    assert body["roleArn"] == "arn:aws:iam::123:role/x"
    assert body["externalId"] == "ext"


async def test_test_s3_export_connection_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.test_s3_export_connection_async(bucket="b2")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/TestS3ExportConnection"


def test_test_s3_export_connection_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "access denied"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.test_s3_export_connection(bucket="b1")

    assert exc_info.value.status_code == 403
    assert "access denied" in str(exc_info.value)


async def test_test_s3_export_connection_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.test_s3_export_connection_async(bucket="b1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# TriggerOtlpExport
# ---------------------------------------------------------------------------


def test_trigger_otlp_export_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.trigger_otlp_export(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/TriggerOtlpExport"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


async def test_trigger_otlp_export_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.trigger_otlp_export_async(body={})

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/TriggerOtlpExport"


def test_trigger_otlp_export_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no config"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.trigger_otlp_export(body={})

    assert exc_info.value.status_code == 404


async def test_trigger_otlp_export_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.trigger_otlp_export_async(body={})

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# TriggerS3Export
# ---------------------------------------------------------------------------


def test_trigger_s3_export_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.trigger_s3_export(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/TriggerS3Export"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


async def test_trigger_s3_export_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.trigger_s3_export_async(body={})

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/TriggerS3Export"


def test_trigger_s3_export_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no config"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.audit_logs.trigger_s3_export(body={})

    assert exc_info.value.status_code == 404


async def test_trigger_s3_export_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.audit_logs.trigger_s3_export_async(body={})

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Cross-cutting behavior: retries, server_url override, http_headers,
# timeout_ms.
# ---------------------------------------------------------------------------


def test_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"config": {"bucket": "b1"}}),
        ]
    )
    bundle = make_sdk(handler)

    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=False,
    )

    result = bundle.sdk.audit_logs.configure_s3_export(bucket="b1", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result.config.bucket == "b1"


async def test_retries_async_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"config": {"bucket": "b2"}}),
        ]
    )
    bundle = make_sdk(handler)

    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=False,
    )

    result = await bundle.sdk.audit_logs.configure_s3_export_async(bucket="b2", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result.config.bucket == "b2"


def test_server_url_override_changes_host(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.list(server_url="https://overridden.invalid")

    req = bundle.transport.last_request
    assert req.url.host == "overridden.invalid"


async def test_server_url_override_changes_host_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.list_async(server_url="https://overridden-async.invalid")

    req = bundle.transport.last_request
    assert req.url.host == "overridden-async.invalid"


def test_http_headers_passthrough(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.list(http_headers={"X-Custom-Header": "hello"})

    req = bundle.transport.last_request
    assert req.headers["x-custom-header"] == "hello"


async def test_http_headers_passthrough_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.list_async(http_headers={"X-Custom-Header": "world"})

    req = bundle.transport.last_request
    assert req.headers["x-custom-header"] == "world"


def test_timeout_ms_override_reflected_on_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.audit_logs.list(timeout_ms=1234)

    req = bundle.transport.last_request
    timeout_ext = req.extensions.get("timeout")
    assert timeout_ext is not None
    assert timeout_ext.get("read") == pytest.approx(1.234)


async def test_timeout_ms_override_reflected_on_request_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.audit_logs.list_async(timeout_ms=2000)

    req = bundle.transport.last_request
    timeout_ext = req.extensions.get("timeout")
    assert timeout_ext is not None
    assert timeout_ext.get("read") == pytest.approx(2.0)
