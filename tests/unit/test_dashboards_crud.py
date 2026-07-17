"""Unit tests for Dashboards CRUD operations: create_dashboard, get, list, update_dashboard, delete, duplicate, spawn."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

DASH_PATH = "/textql.rpc.public.dashboard.DashboardService"


# --------------------------------------------------------------------------
# create_dashboard
# --------------------------------------------------------------------------


def test_create_dashboard_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    result = bundle.sdk.dashboards.create_dashboard(
        name="My Dashboard",
        description="a description",
        code="st.title('hi')",
        type_="DASHBOARD_TYPE_STREAMLIT",
        html_url="https://example.com",
        chat_id="chat-1",
        cell_id="cell-1",
        folder_id="folder-1",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/CreateDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "name": "My Dashboard",
        "description": "a description",
        "code": "st.title('hi')",
        "type": "DASHBOARD_TYPE_STREAMLIT",
        "htmlUrl": "https://example.com",
        "chatId": "chat-1",
        "cellId": "cell-1",
        "folderId": "folder-1",
    }
    assert result.dashboard.id == "d1"


@pytest.mark.asyncio
async def test_create_dashboard_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    result = await bundle.sdk.dashboards.create_dashboard_async(name="Async Dash")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/CreateDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"name": "Async Dash"}
    assert result.dashboard.id == "d1"


def test_create_dashboard_omits_unset_nullable_fields(make_sdk):
    """OptionalNullable fields left at UNSET (description, html_url, chat_id,
    cell_id, folder_id) must be omitted entirely from the serialized body."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {}}))

    bundle.sdk.dashboards.create_dashboard(name="Bare")

    body = bundle.transport.body_json()
    assert body == {"name": "Bare"}
    for key in ("description", "htmlUrl", "chatId", "cellId", "folderId"):
        assert key not in body


def test_create_dashboard_explicit_null_included(make_sdk):
    """Explicitly passing None for an OptionalNullable field should serialize
    as a JSON null, not be omitted."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {}}))

    bundle.sdk.dashboards.create_dashboard(name="X", description=None, folder_id=None)

    body = bundle.transport.body_json()
    assert body["description"] is None
    assert body["folderId"] is None
    assert "name" in body


def test_create_dashboard_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.create_dashboard(name="Bad")

    assert exc_info.value.status_code == 422


def test_create_dashboard_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.create_dashboard(name="Bad")

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_create_dashboard_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "nope"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.dashboards.create_dashboard_async(name="Bad")

    assert exc_info.value.status_code == 404


# --------------------------------------------------------------------------
# get
# --------------------------------------------------------------------------


def test_get_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1", "name": "Foo"}}))

    result = bundle.sdk.dashboards.get(dashboard_id="d1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/GetDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"dashboardId": "d1"}
    assert result.dashboard.name == "Foo"


@pytest.mark.asyncio
async def test_get_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    result = await bundle.sdk.dashboards.get_async(dashboard_id="d1")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/GetDashboard"
    assert result.dashboard.id == "d1"


def test_get_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get(dashboard_id="missing")

    assert exc_info.value.status_code == 404


def test_get_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.get(dashboard_id="d1")

    assert exc_info.value.status_code == 503


# --------------------------------------------------------------------------
# list
# --------------------------------------------------------------------------


def test_list_sync_sends_all_filters(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboards": []}))

    bundle.sdk.dashboards.list(
        search_term="quarterly",
        my_dashboards_only=True,
        sort_by="DASHBOARD_SORT_FIELD_NAME",
        sort_direction="SORT_DIRECTION_ASC",
        limit=10,
        offset=5,
        folder_id="folder-1",
        uncategorized_only=False,
        creator_member_id="member-1",
        shared_with_me=True,
        creator_member_ids=["m1", "m2"],
        status_filter="DASHBOARD_STATUS_PUBLISHED",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/ListDashboards"
    body = bundle.transport.body_json()
    assert body == {
        "searchTerm": "quarterly",
        "myDashboardsOnly": True,
        "sortBy": "DASHBOARD_SORT_FIELD_NAME",
        "sortDirection": "SORT_DIRECTION_ASC",
        "limit": 10,
        "offset": 5,
        "folderId": "folder-1",
        "uncategorizedOnly": False,
        "creatorMemberId": "member-1",
        "sharedWithMe": True,
        "creatorMemberIds": ["m1", "m2"],
        "statusFilter": "DASHBOARD_STATUS_PUBLISHED",
    }


def test_list_omits_unset_fields_by_default(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboards": []}))

    bundle.sdk.dashboards.list()

    body = bundle.transport.body_json()
    assert body == {}


def test_list_explicit_null_search_term_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboards": []}))

    bundle.sdk.dashboards.list(search_term=None, folder_id=None)

    body = bundle.transport.body_json()
    assert body["searchTerm"] is None
    assert body["folderId"] is None


@pytest.mark.asyncio
async def test_list_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboards": [{"id": "d1"}]}))

    result = await bundle.sdk.dashboards.list_async(limit=1)

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/ListDashboards"
    assert bundle.transport.body_json() == {"limit": 1}
    assert len(result.dashboards) == 1


def test_list_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad filter"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.list(limit=-1)

    assert exc_info.value.status_code == 400


# --------------------------------------------------------------------------
# update_dashboard
# --------------------------------------------------------------------------


def test_update_dashboard_sync_basic_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard(
        dashboard_id="d1",
        name="New Name",
        description="new desc",
        code="print(1)",
        type_="DASHBOARD_TYPE_HTML",
        html_url="https://x.test",
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{DASH_PATH}/UpdateDashboard"
    body = bundle.transport.body_json()
    assert body == {
        "dashboardId": "d1",
        "name": "New Name",
        "description": "new desc",
        "code": "print(1)",
        "type": "DASHBOARD_TYPE_HTML",
        "htmlUrl": "https://x.test",
    }


def test_update_dashboard_with_data_sources_sql_query(make_sdk):
    """Exercise the data_sources union type (DataSourcesPatch -> DataSource
    union) with a sql_query variant, including nested query parameters."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard(
        dashboard_id="d1",
        data_sources={
            "sources": [
                {
                    "sql_query": {"query": "select 1", "connector_id": 42},
                    "name": "main_query",
                    "parameters": [
                        {"name": "region", "type": "string", "default": "EU"},
                    ],
                },
            ]
        },
    )

    body = bundle.transport.body_json()
    assert body["dashboardId"] == "d1"
    sources = body["dataSources"]["sources"]
    assert sources[0]["sqlQuery"] == {"query": "select 1", "connectorId": 42}
    assert sources[0]["name"] == "main_query"
    assert sources[0]["parameters"] == [
        {"name": "region", "type": "string", "default": "EU"}
    ]


def test_update_dashboard_with_data_sources_multiple_source_types(make_sdk):
    """Nested union DataSource type: mix python_code and library_tql variants
    in the same request, verifying the discriminated union serializes each
    member using its own aliasing rules."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.update_dashboard(
        dashboard_id="d1",
        data_sources={
            "sources": [
                {
                    "python_code": {"code": "df = pd.DataFrame()"},
                    "name": "py_source",
                },
                {
                    "library_tql": {
                        "tql_path": "lib/foo.tql",
                        "connector_id": 7,
                        "params_json": "{}",
                    },
                    "name": "tql_source",
                },
            ]
        },
    )

    body = bundle.transport.body_json()
    sources = body["dataSources"]["sources"]
    assert sources[0]["pythonCode"] == {"code": "df = pd.DataFrame()"}
    assert sources[0]["name"] == "py_source"
    assert sources[1]["libraryTql"] == {
        "tqlPath": "lib/foo.tql",
        "connectorId": 7,
        "paramsJson": "{}",
    }
    assert sources[1]["name"] == "tql_source"


def test_update_dashboard_explicit_null_vs_unset(make_sdk):
    """name/description/code/html_url are OptionalNullable[str] = UNSET by
    default. Explicit None must serialize to JSON null; leaving unset must
    omit the key entirely."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {}}))

    bundle.sdk.dashboards.update_dashboard(dashboard_id="d1", name=None)

    body = bundle.transport.body_json()
    assert body["name"] is None
    for key in ("description", "code", "htmlUrl"):
        assert key not in body


@pytest.mark.asyncio
async def test_update_dashboard_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    result = await bundle.sdk.dashboards.update_dashboard_async(
        dashboard_id="d1", name="Async Update"
    )

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/UpdateDashboard"
    assert bundle.transport.body_json() == {"dashboardId": "d1", "name": "Async Update"}
    assert result.dashboard.id == "d1"


def test_update_dashboard_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.update_dashboard(dashboard_id="d1", name="X")

    assert exc_info.value.status_code == 409


def test_update_dashboard_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.update_dashboard(dashboard_id="d1", name="X")

    assert exc_info.value.status_code == 502


# --------------------------------------------------------------------------
# delete
# --------------------------------------------------------------------------


def test_delete_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.dashboards.delete(dashboard_id="d1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{DASH_PATH}/DeleteDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"dashboardId": "d1"}


@pytest.mark.asyncio
async def test_delete_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.dashboards.delete_async(dashboard_id="d1")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/DeleteDashboard"


def test_delete_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.delete(dashboard_id="missing")

    assert exc_info.value.status_code == 404


def test_delete_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.delete(dashboard_id="d1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# duplicate
# --------------------------------------------------------------------------


def test_duplicate_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d2"}}))

    result = bundle.sdk.dashboards.duplicate(dashboard_id="d1", name="Copy Name")

    req = bundle.transport.last_request
    assert req.url.path == f"{DASH_PATH}/DuplicateDashboard"
    assert bundle.transport.body_json() == {"dashboardId": "d1", "name": "Copy Name"}
    assert result.dashboard.id == "d2"


def test_duplicate_omits_unset_name(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d2"}}))

    bundle.sdk.dashboards.duplicate(dashboard_id="d1")

    body = bundle.transport.body_json()
    assert body == {"dashboardId": "d1"}
    assert "name" not in body


@pytest.mark.asyncio
async def test_duplicate_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d2"}}))

    result = await bundle.sdk.dashboards.duplicate_async(dashboard_id="d1")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/DuplicateDashboard"
    assert result.dashboard.id == "d2"


def test_duplicate_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.duplicate(dashboard_id="d1")

    assert exc_info.value.status_code == 403


# --------------------------------------------------------------------------
# spawn
# --------------------------------------------------------------------------


def test_spawn_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"refreshedAt": "2024-01-01T00:00:00Z"}))

    result = bundle.sdk.dashboards.spawn(
        dashboard_id="d1",
        force_restart=True,
        refresh_data_only=False,
        refresh_source_names=["src1", "src2"],
        refresh_code_only=True,
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{DASH_PATH}/SpawnDashboard"
    assert bundle.transport.body_json() == {
        "dashboardId": "d1",
        "forceRestart": True,
        "refreshDataOnly": False,
        "refreshSourceNames": ["src1", "src2"],
        "refreshCodeOnly": True,
    }
    assert result.refreshed_at is not None


@pytest.mark.asyncio
async def test_spawn_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.dashboards.spawn_async(dashboard_id="d1")

    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/SpawnDashboard"
    assert bundle.transport.body_json() == {"dashboardId": "d1"}


def test_spawn_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "already running"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.spawn(dashboard_id="d1")

    assert exc_info.value.status_code == 409


def test_spawn_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.dashboards.spawn(dashboard_id="d1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# retries / server_url / http_headers / timeout_ms overrides
# --------------------------------------------------------------------------


def test_create_dashboard_retries_backoff_then_success(make_sdk, sequence_handler):
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

    result = bundle.sdk.dashboards.create_dashboard(name="Retried", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result.dashboard.id == "d1"


@pytest.mark.asyncio
async def test_get_async_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(502, {"message": "transient"}),
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

    result = await bundle.sdk.dashboards.get_async(dashboard_id="d1", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result.dashboard.id == "d1"


def test_get_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))
    override_url = "https://override.invalid"

    bundle.sdk.dashboards.get(dashboard_id="d1", server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_get_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    bundle.sdk.dashboards.get(
        dashboard_id="d1", http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    # Auth header should still be present alongside the custom header.
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_get_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "d1"}}))

    result = bundle.sdk.dashboards.get(dashboard_id="d1", timeout_ms=5000)

    assert result.dashboard.id == "d1"
    assert bundle.transport.last_request.url.path == f"{DASH_PATH}/GetDashboard"
