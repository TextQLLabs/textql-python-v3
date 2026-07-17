"""Unit tests for miscellaneous Dashboards operations: check_health, view stats, members, preview, screenshot, scheduling."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

DASH_PATH = "/textql.rpc.public.dashboard.DashboardService"


# --------------------------------------------------------------------------
# check_health
# --------------------------------------------------------------------------


def test_check_health_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"dashboards": [{"dashboard_id": "d1", "status": "HEALTHY"}]}
        )
    )

    result = bundle.sdk.dashboards.check_health(dashboard_ids=["d1", "d2"])

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/CheckDashboardHealth"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"dashboardIds": ["d1", "d2"]}
    assert len(result.dashboards) == 1


def test_check_health_omits_unset_dashboard_ids(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboards": []}))

    bundle.sdk.dashboards.check_health()

    body = bundle.transport.body_json()
    assert body == {}


@pytest.mark.asyncio
async def test_check_health_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboards": []}))

    await bundle.sdk.dashboards.check_health_async(dashboard_ids=["d1"])

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/CheckDashboardHealth"
    assert bundle.transport.body_json() == {"dashboardIds": ["d1"]}


def test_check_health_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad ids"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.check_health(dashboard_ids=["bad"])

    assert exc_info.value.status_code == 400


def test_check_health_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.check_health()

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# get_dashboard_view_stats
# --------------------------------------------------------------------------


def test_get_dashboard_view_stats_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"view_count": 42}))

    bundle.sdk.dashboards.get_dashboard_view_stats(dashboard_id="d1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/GetDashboardViewStats"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"dashboardId": "d1"}


@pytest.mark.asyncio
async def test_get_dashboard_view_stats_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.dashboards.get_dashboard_view_stats_async(dashboard_id="d1")

    assert (
        bundle.transport.last_request.url.path == f"{DASH_PATH}/GetDashboardViewStats"
    )


def test_get_dashboard_view_stats_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get_dashboard_view_stats(dashboard_id="missing")

    assert exc_info.value.status_code == 404


def test_get_dashboard_view_stats_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get_dashboard_view_stats(dashboard_id="d1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# get_members_with_dashboards (empty body request model)
# --------------------------------------------------------------------------


def test_get_members_with_dashboards_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"members": [{"memberId": "m1", "memberName": "Alice"}]}
        )
    )

    result = bundle.sdk.dashboards.get_members_with_dashboards(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/GetMembersWithDashboards"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert result.members[0].member_id == "m1"


@pytest.mark.asyncio
async def test_get_members_with_dashboards_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))

    result = await bundle.sdk.dashboards.get_members_with_dashboards_async(body={})

    assert (
        bundle.transport.last_request.url.path
        == f"{DASH_PATH}/GetMembersWithDashboards"
    )
    assert result.members == []


def test_get_members_with_dashboards_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get_members_with_dashboards(body={})

    assert exc_info.value.status_code == 403


def test_get_members_with_dashboards_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get_members_with_dashboards(body={})

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# preview_config
# --------------------------------------------------------------------------


def test_preview_config_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.preview_config(
        patch_ref="refs/patches/123", dashboard_path="dashboards/sales.dashboard"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/PreviewConfigDashboard"
    assert bundle.transport.body_json() == {
        "patchRef": "refs/patches/123",
        "dashboardPath": "dashboards/sales.dashboard",
    }


@pytest.mark.asyncio
async def test_preview_config_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    await bundle.sdk.dashboards.preview_config_async(
        patch_ref="refs/patches/abc", dashboard_path="dashboards/foo.dashboard"
    )

    assert (
        bundle.transport.last_request.url.path == f"{DASH_PATH}/PreviewConfigDashboard"
    )
    assert bundle.transport.body_json() == {
        "patchRef": "refs/patches/abc",
        "dashboardPath": "dashboards/foo.dashboard",
    }


def test_preview_config_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "not authorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.preview_config(
            patch_ref="refs/patches/x", dashboard_path="dashboards/x.dashboard"
        )

    assert exc_info.value.status_code == 403


def test_preview_config_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.preview_config(
            patch_ref="refs/patches/x", dashboard_path="dashboards/x.dashboard"
        )

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# regenerate_screenshot
# --------------------------------------------------------------------------


def test_regenerate_screenshot_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"screenshot_url": "https://x/y.png"}))

    bundle.sdk.dashboards.regenerate_screenshot(dashboard_id="d1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/RegenerateScreenshot"
    assert bundle.transport.body_json() == {"dashboardId": "d1"}


@pytest.mark.asyncio
async def test_regenerate_screenshot_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.dashboards.regenerate_screenshot_async(dashboard_id="d1")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/RegenerateScreenshot"


def test_regenerate_screenshot_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.regenerate_screenshot(dashboard_id="missing")

    assert exc_info.value.status_code == 404


def test_regenerate_screenshot_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.regenerate_screenshot(dashboard_id="d1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# run_scheduled_dashboard
# --------------------------------------------------------------------------


def test_run_scheduled_dashboard_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.run_scheduled_dashboard(dashboard_id="d1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/RunScheduledDashboard"
    assert bundle.transport.body_json() == {"dashboardId": "d1"}


@pytest.mark.asyncio
async def test_run_scheduled_dashboard_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    await bundle.sdk.dashboards.run_scheduled_dashboard_async(dashboard_id="d1")

    assert (
        bundle.transport.last_request.url.path == f"{DASH_PATH}/RunScheduledDashboard"
    )


def test_run_scheduled_dashboard_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.run_scheduled_dashboard(dashboard_id="missing")

    assert exc_info.value.status_code == 404


def test_run_scheduled_dashboard_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.run_scheduled_dashboard(dashboard_id="d1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# update_dashboard_schedule
# --------------------------------------------------------------------------


def test_update_dashboard_schedule_sync_with_normal_cron(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard_schedule(
        dashboard_id="d1",
        schedule_enabled=True,
        cron_string="0 9 * * MON-FRI",
        data_sources=[
            {
                "sql_query": {"query": "select 1", "connector_id": 1},
                "name": "daily_query",
            }
        ],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/UpdateDashboardSchedule"
    body = bundle.transport.body_json()
    assert body["dashboardId"] == "d1"
    assert body["scheduleEnabled"] is True
    assert body["cronString"] == "0 9 * * MON-FRI"
    assert body["dataSources"] == [
        {
            "sqlQuery": {"query": "select 1", "connectorId": 1},
            "name": "daily_query",
        }
    ]


def test_update_dashboard_schedule_with_malformed_cron_string_passes_through(make_sdk):
    """The SDK should not attempt to validate cron syntax -- an obviously
    malformed string must be passed through verbatim to the wire, letting the
    server decide whether to reject it."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard_schedule(
        dashboard_id="d1",
        schedule_enabled=True,
        cron_string="not a cron string !!!",
    )

    body = bundle.transport.body_json()
    assert body["cronString"] == "not a cron string !!!"


def test_update_dashboard_schedule_with_empty_cron_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard_schedule(
        dashboard_id="d1", schedule_enabled=False, cron_string=""
    )

    body = bundle.transport.body_json()
    assert body["cronString"] == ""
    assert body["scheduleEnabled"] is False


def test_update_dashboard_schedule_explicit_null_cron_disables_schedule(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard_schedule(
        dashboard_id="d1", schedule_enabled=False, cron_string=None
    )

    body = bundle.transport.body_json()
    assert body["cronString"] is None


def test_update_dashboard_schedule_omits_unset_cron_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard_schedule(dashboard_id="d1")

    body = bundle.transport.body_json()
    assert body == {"dashboardId": "d1"}
    assert "cronString" not in body


def test_update_dashboard_schedule_multiple_data_source_types(make_sdk):
    """Exercise the data_sources list with more than one union-member type at
    once (ontology_sql + file), similar to the dashboard config scenario."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard_schedule(
        dashboard_id="d1",
        data_sources=[
            {
                "ontology_sql": {"query": "select * from ontology"},
                "name": "ontology_source",
            },
            {
                "file": {
                    "dataset_id": "ds1",
                    "file_name": "data.csv",
                    "sheet_index": 0,
                },
                "name": "file_source",
            },
        ],
    )

    body = bundle.transport.body_json()
    sources = body["dataSources"]
    assert sources[0]["ontologySql"] == {"query": "select * from ontology"}
    assert sources[0]["name"] == "ontology_source"
    assert sources[1]["file"] == {
        "datasetId": "ds1",
        "fileName": "data.csv",
        "sheetIndex": 0,
    }
    assert sources[1]["name"] == "file_source"


@pytest.mark.asyncio
async def test_update_dashboard_schedule_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    await bundle.sdk.dashboards.update_dashboard_schedule_async(
        dashboard_id="d1", schedule_enabled=True, cron_string="*/5 * * * *"
    )

    assert (
        bundle.transport.last_request.url.path == f"{DASH_PATH}/UpdateDashboardSchedule"
    )
    body = bundle.transport.body_json()
    assert body["cronString"] == "*/5 * * * *"


def test_update_dashboard_schedule_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid cron"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.update_dashboard_schedule(
            dashboard_id="d1", cron_string="garbage"
        )

    assert exc_info.value.status_code == 400


def test_update_dashboard_schedule_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.update_dashboard_schedule(dashboard_id="d1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# retries / overrides
# --------------------------------------------------------------------------


def test_check_health_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(429, {"message": "rate limited"}),
            json_response(200, {"dashboards": []}),
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

    bundle.sdk.dashboards.check_health(retries=retry_config)

    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_update_dashboard_schedule_retries_backoff_then_success(
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

    await bundle.sdk.dashboards.update_dashboard_schedule_async(
        dashboard_id="d1", retries=retry_config
    )

    assert len(bundle.transport.requests) == 2


def test_preview_config_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))
    override_url = "https://override.invalid"

    bundle.sdk.dashboards.preview_config(
        patch_ref="ref", dashboard_path="path.dashboard", server_url=override_url
    )

    assert str(bundle.transport.last_request.url).startswith(override_url)


def test_regenerate_screenshot_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.dashboards.regenerate_screenshot(
        dashboard_id="d1", http_headers={"X-Custom": "abc"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom"] == "abc"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
