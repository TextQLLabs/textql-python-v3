"""Unit tests for Dashboards version operations: get_version, list_versions, restore, discard, publish."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

DASH_PATH = "/textql.rpc.public.dashboard.DashboardService"


# --------------------------------------------------------------------------
# get_version
# --------------------------------------------------------------------------


def test_get_version_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"version": {"id": "v1", "version_number": 3}})
    )

    result = bundle.sdk.dashboards.get_version(dashboard_id="d1", version_number=3)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/GetDashboardVersion"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"dashboardId": "d1", "versionNumber": 3}
    assert result.version.id == "v1"


@pytest.mark.asyncio
async def test_get_version_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"version": {"id": "v1"}}))

    result = await bundle.sdk.dashboards.get_version_async(
        dashboard_id="d1", version_number=1
    )

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/GetDashboardVersion"
    assert result.version.id == "v1"


def test_get_version_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "version not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get_version(dashboard_id="d1", version_number=99)

    assert exc_info.value.status_code == 404


def test_get_version_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get_version(dashboard_id="d1", version_number=1)

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_versions
# --------------------------------------------------------------------------


def test_list_versions_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "versions": [
                    {"id": "v1", "version_number": 1},
                    {"id": "v2", "version_number": 2},
                ],
                "total_count": 2,
            },
        )
    )

    result = bundle.sdk.dashboards.list_versions(dashboard_id="d1", limit=10, offset=0)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/ListDashboardVersions"
    assert bundle.transport.body_json() == {
        "dashboardId": "d1",
        "limit": 10,
        "offset": 0,
    }
    assert result.total_count == 2
    assert len(result.versions) == 2


@pytest.mark.asyncio
async def test_list_versions_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"versions": [], "total_count": 0}))

    result = await bundle.sdk.dashboards.list_versions_async(dashboard_id="d1")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/ListDashboardVersions"
    assert result.total_count == 0


def test_list_versions_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad params"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.list_versions(dashboard_id="d1", limit=-1)

    assert exc_info.value.status_code == 400


# --------------------------------------------------------------------------
# restore_dashboard_version
# --------------------------------------------------------------------------


def test_restore_dashboard_version_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.restore_dashboard_version(dashboard_id="d1", version_number=2)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/RestoreDashboardVersion"
    assert bundle.transport.body_json() == {"dashboardId": "d1", "versionNumber": 2}


@pytest.mark.asyncio
async def test_restore_dashboard_version_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    await bundle.sdk.dashboards.restore_dashboard_version_async(
        dashboard_id="d1", version_number=5
    )

    assert (
        bundle.transport.last_request.url.path == f"{DASH_PATH}/RestoreDashboardVersion"
    )
    assert bundle.transport.body_json() == {"dashboardId": "d1", "versionNumber": 5}


def test_restore_dashboard_version_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "version not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.restore_dashboard_version(
            dashboard_id="d1", version_number=999
        )

    assert exc_info.value.status_code == 404


def test_restore_dashboard_version_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.restore_dashboard_version(dashboard_id="d1", version_number=1)

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# discard_changes
# --------------------------------------------------------------------------


def test_discard_changes_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.discard_changes(dashboard_id="d1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/DiscardDashboardChanges"
    assert bundle.transport.body_json() == {"dashboardId": "d1"}


@pytest.mark.asyncio
async def test_discard_changes_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    await bundle.sdk.dashboards.discard_changes_async(dashboard_id="d1")

    assert (
        bundle.transport.last_request.url.path == f"{DASH_PATH}/DiscardDashboardChanges"
    )


def test_discard_changes_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.discard_changes(dashboard_id="missing")

    assert exc_info.value.status_code == 404


def test_discard_changes_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.discard_changes(dashboard_id="d1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# publish
# --------------------------------------------------------------------------


def test_publish_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.publish(dashboard_id="d1", label="v1.2 release")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/PublishDashboard"
    assert bundle.transport.body_json() == {
        "dashboardId": "d1",
        "label": "v1.2 release",
    }


def test_publish_omits_unset_label(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.publish(dashboard_id="d1")

    body = bundle.transport.body_json()
    assert body == {"dashboardId": "d1"}
    assert "label" not in body


def test_publish_explicit_null_label(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.publish(dashboard_id="d1", label=None)

    body = bundle.transport.body_json()
    assert body["label"] is None


@pytest.mark.asyncio
async def test_publish_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    await bundle.sdk.dashboards.publish_async(dashboard_id="d1", label="async release")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/PublishDashboard"
    assert bundle.transport.body_json() == {
        "dashboardId": "d1",
        "label": "async release",
    }


def test_publish_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "nothing to publish"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.publish(dashboard_id="d1")

    assert exc_info.value.status_code == 422


def test_publish_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.publish(dashboard_id="d1")

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_publish_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.dashboards.publish_async(dashboard_id="d1")

    assert exc_info.value.status_code == 403


# --------------------------------------------------------------------------
# retries / overrides
# --------------------------------------------------------------------------


def test_publish_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(503, {"message": "transient"}),
            json_response(200, {"dashboard": {"id": "d1"}}),
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

    bundle.sdk.dashboards.publish(dashboard_id="d1", retries=retry_config)

    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_restore_dashboard_version_retries_backoff_then_success(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"dashboard": {"id": "d1"}}),
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

    await bundle.sdk.dashboards.restore_dashboard_version_async(
        dashboard_id="d1", version_number=1, retries=retry_config
    )

    assert len(bundle.transport.requests) == 2


def test_publish_timeout_ms_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.publish(dashboard_id="d1", timeout_ms=2500)

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/PublishDashboard"


def test_list_versions_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"versions": []}))

    bundle.sdk.dashboards.list_versions(
        dashboard_id="d1", http_headers={"X-Trace-Id": "trace-123"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Trace-Id"] == "trace-123"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
