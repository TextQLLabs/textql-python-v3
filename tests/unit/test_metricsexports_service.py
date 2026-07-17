"""Unit tests for the MetricsExports service (sdk.metrics_exports)."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, models, utils

BASE_PATH = "/textql.rpc.public.metrics_export.MetricsExportService"


# ---------------------------------------------------------------------------
# ConfigureMetricsExport
# ---------------------------------------------------------------------------


def test_configure_sync_all_fields(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "config": {
                    "prometheusEnabled": True,
                    "otlpEnabled": True,
                    "otlpEndpoint": "https://otlp.example.com",
                    "otlpProtocol": "grpc",
                    "pushIntervalSeconds": 60,
                }
            },
        )
    )

    result = bundle.sdk.metrics_exports.configure(
        prometheus_enabled=True,
        otlp_enabled=True,
        otlp_endpoint="https://otlp.example.com",
        otlp_headers="Authorization=Bearer xyz",
        otlp_protocol="grpc",
        push_interval_seconds=60,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ConfigureMetricsExport"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["prometheusEnabled"] is True
    assert body["otlpEnabled"] is True
    assert body["otlpEndpoint"] == "https://otlp.example.com"
    assert body["otlpHeaders"] == "Authorization=Bearer xyz"
    assert body["otlpProtocol"] == "grpc"
    assert body["pushIntervalSeconds"] == 60

    assert result.config.prometheus_enabled is True
    assert result.config.otlp_endpoint == "https://otlp.example.com"
    assert result.config.push_interval_seconds == 60


def test_configure_sync_no_fields_empty_body(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.metrics_exports.configure()

    body = bundle.transport.body_json()
    assert body == {}


@pytest.mark.asyncio
async def test_configure_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {}}))

    result = await bundle.sdk.metrics_exports.configure_async(prometheus_enabled=False)

    body = bundle.transport.body_json()
    assert body["prometheusEnabled"] is False
    assert result.config is not None


def test_configure_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad protocol"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.configure(otlp_protocol="invalid")

    assert exc_info.value.status_code == 400


def test_configure_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.configure()

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# GetMetricsExportConfig
# ---------------------------------------------------------------------------


def test_get_metrics_export_config_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "config": {
                    "prometheusEnabled": False,
                    "otlpEnabled": True,
                    "otlpEndpoint": "https://collector.example.com",
                }
            },
        )
    )

    result = bundle.sdk.metrics_exports.get_metrics_export_config(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetMetricsExportConfig"
    assert result.config.otlp_enabled is True
    assert result.config.otlp_endpoint == "https://collector.example.com"


@pytest.mark.asyncio
async def test_get_metrics_export_config_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.metrics_exports.get_metrics_export_config_async(
        body=models.TextqlRPCPublicMetricsExportGetMetricsExportConfigRequest()
    )

    assert result.config is None


def test_get_metrics_export_config_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not configured"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.get_metrics_export_config(body={})

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# DeleteMetricsExportConfig
# ---------------------------------------------------------------------------


def test_delete_config_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.metrics_exports.delete_config(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteMetricsExportConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


@pytest.mark.asyncio
async def test_delete_config_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.metrics_exports.delete_config_async(
        body=models.TextqlRPCPublicMetricsExportDeleteMetricsExportConfigRequest()
    )

    assert len(bundle.transport.requests) == 1


def test_delete_config_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.delete_config(body={})

    assert exc_info.value.status_code == 403


def test_delete_config_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.delete_config(body={})

    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# TestMetricsExportConnection -- business-logic success/failure vs HTTP error
# ---------------------------------------------------------------------------


def test_test_connection_sync_success(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.metrics_exports.test_connection(
        otlp_endpoint="https://good.example.com",
        otlp_protocol="grpc",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/TestMetricsExportConnection"
    body = bundle.transport.body_json()
    assert body["otlpEndpoint"] == "https://good.example.com"
    assert body["otlpProtocol"] == "grpc"

    assert result.success is True
    assert result.error_message is None


def test_test_connection_sync_business_logic_failure_is_200(make_sdk):
    """A connection test that fails for business reasons (e.g. bad
    credentials, unreachable endpoint) still comes back as HTTP 200 with
    success=False -- this must NOT raise, unlike a real HTTP error."""
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"success": False, "errorMessage": "connection refused"},
        )
    )

    result = bundle.sdk.metrics_exports.test_connection(
        otlp_endpoint="https://unreachable.example.com"
    )

    assert result.success is False
    assert result.error_message == "connection refused"


@pytest.mark.asyncio
async def test_test_connection_async_business_logic_failure(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"success": False, "errorMessage": "auth failed"}
        )
    )

    result = await bundle.sdk.metrics_exports.test_connection_async(
        otlp_endpoint="https://x.example.com"
    )

    assert result.success is False
    assert result.error_message == "auth failed"


def test_test_connection_http_error_4xx_raises(make_sdk):
    """A real HTTP-level error (e.g. malformed request) is distinct from a
    business-logic connection failure and must raise."""
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.test_connection(otlp_endpoint="bad")

    assert exc_info.value.status_code == 400


def test_test_connection_http_error_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.test_connection()

    assert exc_info.value.status_code == 503


def test_test_connection_no_fields_empty_body(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.metrics_exports.test_connection()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# TriggerMetricsPush
# ---------------------------------------------------------------------------


def test_trigger_push_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"triggered": True}))

    result = bundle.sdk.metrics_exports.trigger_push(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/TriggerMetricsPush"
    assert result.triggered is True


@pytest.mark.asyncio
async def test_trigger_push_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"triggered": False}))

    result = await bundle.sdk.metrics_exports.trigger_push_async(
        body=models.TextqlRPCPublicMetricsExportTriggerMetricsPushRequest()
    )

    assert result.triggered is False


def test_trigger_push_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "already running"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.trigger_push(body={})

    assert exc_info.value.status_code == 409


def test_trigger_push_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.metrics_exports.trigger_push(body={})

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# retries / server_url / http_headers / timeout_ms overrides
# ---------------------------------------------------------------------------


def test_configure_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"config": {"prometheusEnabled": True}}),
        ]
    )
    bundle = make_sdk(handler)

    result = bundle.sdk.metrics_exports.configure(
        prometheus_enabled=True,
        retries=utils.RetryConfig(
            strategy="backoff",
            backoff=utils.BackoffStrategy(
                initial_interval=1,
                max_interval=5,
                exponent=1.0,
                max_elapsed_time=5000,
            ),
            retry_connection_errors=False,
        ),
    )

    assert len(bundle.transport.requests) == 2
    assert result.config.prometheus_enabled is True


@pytest.mark.asyncio
async def test_trigger_push_retries_on_500_then_succeeds_async(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"triggered": True}),
        ]
    )
    bundle = make_sdk(handler)

    result = await bundle.sdk.metrics_exports.trigger_push_async(
        body={},
        retries=utils.RetryConfig(
            strategy="backoff",
            backoff=utils.BackoffStrategy(
                initial_interval=1,
                max_interval=5,
                exponent=1.0,
                max_elapsed_time=5000,
            ),
            retry_connection_errors=False,
        ),
    )

    assert len(bundle.transport.requests) == 2
    assert result.triggered is True


def test_test_connection_server_url_override(make_sdk):
    captured = {}

    def handler(req):
        captured["url"] = str(req.url)
        return json_response(200, {"success": True})

    bundle = make_sdk(handler)

    bundle.sdk.metrics_exports.test_connection(server_url="https://override.invalid")

    assert captured["url"].startswith("https://override.invalid")


def test_configure_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.metrics_exports.configure(
        http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_trigger_push_timeout_ms_override_does_not_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"triggered": True}))

    bundle.sdk.metrics_exports.trigger_push(body={}, timeout_ms=15000)

    assert len(bundle.transport.requests) == 1
