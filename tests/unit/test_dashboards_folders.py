"""Unit tests for Dashboards folder-management operations: create_folder, delete_folder, list_folders, move_to_folder, update_dashboard_folder."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

DASH_PATH = "/textql.rpc.public.dashboard.DashboardService"


# --------------------------------------------------------------------------
# create_folder
# --------------------------------------------------------------------------


def test_create_folder_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    bundle.sdk.dashboards.create_folder(name="My Folder", parent_id="root-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/CreateDashboardFolder"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"name": "My Folder", "parentId": "root-1"}


def test_create_folder_omits_unset_parent_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    bundle.sdk.dashboards.create_folder(name="Root Folder")

    body = bundle.transport.body_json()
    assert body == {"name": "Root Folder"}
    assert "parentId" not in body


def test_create_folder_explicit_null_parent_id(make_sdk):
    """parent_id explicitly set to None (move to root) must serialize as
    JSON null rather than being dropped."""
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    bundle.sdk.dashboards.create_folder(name="Root Folder", parent_id=None)

    body = bundle.transport.body_json()
    assert body["parentId"] is None


@pytest.mark.asyncio
async def test_create_folder_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    await bundle.sdk.dashboards.create_folder_async(name="Async Folder")

    req = bundle.transport.last_request
    assert req.url.path == f"{DASH_PATH}/CreateDashboardFolder"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"name": "Async Folder"}


def test_create_folder_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad name"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.create_folder(name="")

    assert exc_info.value.status_code == 400


def test_create_folder_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.create_folder(name="X")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# delete_folder
# --------------------------------------------------------------------------


def test_delete_folder_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.dashboards.delete_folder(folder_id="f1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/DeleteDashboardFolder"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"folderId": "f1"}


@pytest.mark.asyncio
async def test_delete_folder_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.dashboards.delete_folder_async(folder_id="f1")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/DeleteDashboardFolder"
    assert bundle.transport.body_json() == {"folderId": "f1"}


def test_delete_folder_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.delete_folder(folder_id="missing")

    assert exc_info.value.status_code == 404


def test_delete_folder_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.delete_folder(folder_id="f1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_folders  (body is an empty request model, but is still required)
# --------------------------------------------------------------------------


def test_list_folders_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "folders": [
                    {
                        "id": "f1",
                        "name": "Top",
                        "children": [{"id": "f2", "name": "Nested"}],
                    }
                ]
            },
        )
    )

    result = bundle.sdk.dashboards.list_folders(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/ListDashboardFolders"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert result.folders[0].id == "f1"
    assert result.folders[0].children[0].id == "f2"


@pytest.mark.asyncio
async def test_list_folders_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folders": []}))

    result = await bundle.sdk.dashboards.list_folders_async(body={})

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/ListDashboardFolders"
    assert result.folders == []


def test_list_folders_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.list_folders(body={})

    assert exc_info.value.status_code == 403


# --------------------------------------------------------------------------
# move_to_folder
# --------------------------------------------------------------------------


def test_move_to_folder_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.move_to_folder(dashboard_id="d1", folder_id="f1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/MoveDashboardToFolder"
    assert bundle.transport.body_json() == {"dashboardId": "d1", "folderId": "f1"}


def test_move_to_folder_null_folder_id_moves_to_root(make_sdk):
    """folder_id=None ('move to root/uncategorized' per docstring) must
    serialize as an explicit JSON null, distinguishable from omission."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.move_to_folder(dashboard_id="d1", folder_id=None)

    body = bundle.transport.body_json()
    assert body["folderId"] is None


def test_move_to_folder_omits_unset_folder_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.move_to_folder(dashboard_id="d1")

    body = bundle.transport.body_json()
    assert body == {"dashboardId": "d1"}
    assert "folderId" not in body


@pytest.mark.asyncio
async def test_move_to_folder_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    await bundle.sdk.dashboards.move_to_folder_async(dashboard_id="d1", folder_id="f2")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/MoveDashboardToFolder"
    assert bundle.transport.body_json() == {"dashboardId": "d1", "folderId": "f2"}


def test_move_to_folder_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "dashboard not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.move_to_folder(dashboard_id="missing", folder_id="f1")

    assert exc_info.value.status_code == 404


def test_move_to_folder_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.move_to_folder(dashboard_id="d1", folder_id="f1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# update_dashboard_folder
# --------------------------------------------------------------------------


def test_update_dashboard_folder_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    bundle.sdk.dashboards.update_dashboard_folder(
        folder_id="f1", name="Renamed", parent_id="new-parent"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/UpdateDashboardFolder"
    assert bundle.transport.body_json() == {
        "folderId": "f1",
        "name": "Renamed",
        "parentId": "new-parent",
    }


def test_update_dashboard_folder_empty_string_parent_moves_to_root(make_sdk):
    """Per docstring: empty string parent_id = move folder to root. This is a
    plain (non-null) string value and should just pass through."""
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    bundle.sdk.dashboards.update_dashboard_folder(folder_id="f1", parent_id="")

    body = bundle.transport.body_json()
    assert body["parentId"] == ""


def test_update_dashboard_folder_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    bundle.sdk.dashboards.update_dashboard_folder(folder_id="f1")

    body = bundle.transport.body_json()
    assert body == {"folderId": "f1"}


@pytest.mark.asyncio
async def test_update_dashboard_folder_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folder": {"id": "f1"}}))

    await bundle.sdk.dashboards.update_dashboard_folder_async(folder_id="f1", name="X")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/UpdateDashboardFolder"
    assert bundle.transport.body_json() == {"folderId": "f1", "name": "X"}


def test_update_dashboard_folder_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.update_dashboard_folder(folder_id="missing")

    assert exc_info.value.status_code == 404


def test_update_dashboard_folder_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.update_dashboard_folder(folder_id="f1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# retries / overrides
# --------------------------------------------------------------------------


def test_create_folder_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"folder": {"id": "f1"}}),
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

    bundle.sdk.dashboards.create_folder(name="Retried", retries=retry_config)

    assert len(bundle.transport.requests) == 2


def test_move_to_folder_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))
    override_url = "https://override.invalid"

    bundle.sdk.dashboards.move_to_folder(
        dashboard_id="d1", folder_id="f1", server_url=override_url
    )

    assert str(bundle.transport.last_request.url).startswith(override_url)
