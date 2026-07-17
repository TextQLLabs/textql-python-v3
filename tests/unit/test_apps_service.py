"""Unit tests for the Apps service (src/textql_sdk/apps.py), exposed as sdk.apps."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response

PATH_PREFIX = "/textql.rpc.public.app.AppService"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def assert_common(bundle, path_suffix: str, api_key: str = FAKE_API_KEY):
    """Assert method/path/auth-header invariants that apply to every call."""
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/{path_suffix}"
    assert req.headers[AUTH_HEADER_NAME] == api_key


# ---------------------------------------------------------------------------
# heartbeat
# ---------------------------------------------------------------------------


def test_heartbeat_sync_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = bundle.sdk.apps.heartbeat(app_id="app-1")

    assert_common(bundle, "AppHeartbeat")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-1"
    assert resp is not None


async def test_heartbeat_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = await bundle.sdk.apps.heartbeat_async(app_id="app-2")

    assert_common(bundle, "AppHeartbeat")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-2"
    assert resp is not None


def test_heartbeat_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.heartbeat(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_heartbeat_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.heartbeat_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# create_app
# ---------------------------------------------------------------------------


def test_create_app_sync_full_payload(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"app": {"id": "app-123", "name": "My App"}}
        )
    )

    resp = bundle.sdk.apps.create_app(
        name="My App",
        description="a description",
        code="print(1)",
        data_sources=[
            {
                "type": "file",
                "name": "ds1",
                "file": {"dataset_id": "ds-1", "file_name": "a.csv"},
            }
        ],
        compute_functions=[
            {
                "name": "fn1",
                "description": "does a thing",
                "code": "def fn1(): pass",
            }
        ],
        files=[{"path": "main.py", "content": "print('hi')"}],
    )

    assert_common(bundle, "CreateApp")
    body = bundle.transport.body_json()
    assert body["name"] == "My App"
    assert body["description"] == "a description"
    assert body["code"] == "print(1)"
    assert isinstance(body["dataSources"], list)
    assert body["dataSources"][0]["file"]["datasetId"] == "ds-1"
    assert isinstance(body["computeFunctions"], list)
    assert body["computeFunctions"][0]["name"] == "fn1"
    assert isinstance(body["files"], list)
    assert body["files"][0]["path"] == "main.py"

    assert resp.app.id == "app-123"
    assert resp.app.name == "My App"


async def test_create_app_async_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-124"}}))

    resp = await bundle.sdk.apps.create_app_async(name="Async App")

    assert_common(bundle, "CreateApp")
    body = bundle.transport.body_json()
    assert body["name"] == "Async App"
    assert resp.app.id == "app-124"


def test_create_app_description_unset_omits_field(make_sdk):
    """description is OptionalNullable[str]=UNSET by default; omitting it should
    omit the key from the serialized body entirely (per CreateAppRequest's
    model_serializer: 'description' is in nullable_fields, and is only included
    if explicitly set via pydantic_fields_set)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.apps.create_app(name="NoDescription")

    body = bundle.transport.body_json()
    assert "description" not in body
    assert body["name"] == "NoDescription"


def test_create_app_description_explicit_none_included_as_null(make_sdk):
    """Explicitly passing description=None should serialize the field as JSON
    null, since 'description' is in the model's nullable_fields set and will be
    included once pydantic marks the field as explicitly set."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.apps.create_app(name="ExplicitNone", description=None)

    body = bundle.transport.body_json()
    assert "description" in body
    assert body["description"] is None


def test_create_app_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.create_app(name="x")
    assert exc_info.value.status_code == 404


async def test_create_app_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.create_app_async(name="x")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# delete_app
# ---------------------------------------------------------------------------


def test_delete_app_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    resp = bundle.sdk.apps.delete_app(app_id="app-to-delete")
    assert_common(bundle, "DeleteApp")
    assert bundle.transport.body_json()["appId"] == "app-to-delete"
    assert resp is not None


async def test_delete_app_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    resp = await bundle.sdk.apps.delete_app_async(app_id="app-to-delete-2")
    assert_common(bundle, "DeleteApp")
    assert bundle.transport.body_json()["appId"] == "app-to-delete-2"
    assert resp is not None


def test_delete_app_400_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.delete_app(app_id="x")
    assert exc_info.value.status_code == 400


async def test_delete_app_async_503_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.delete_app_async(app_id="x")
    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# duplicate
# ---------------------------------------------------------------------------


def test_duplicate_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"app": {"id": "dup-1", "name": "Copy of X"}})
    )
    resp = bundle.sdk.apps.duplicate(app_id="orig-1")
    assert_common(bundle, "DuplicateApp")
    assert bundle.transport.body_json()["appId"] == "orig-1"
    assert resp.app.id == "dup-1"
    assert resp.app.name == "Copy of X"


async def test_duplicate_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "dup-2"}}))
    resp = await bundle.sdk.apps.duplicate_async(app_id="orig-2")
    assert_common(bundle, "DuplicateApp")
    assert resp.app.id == "dup-2"


def test_duplicate_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.duplicate(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_duplicate_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.duplicate_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get
# ---------------------------------------------------------------------------


def test_get_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"app": {"id": "app-1", "name": "Foo"}, "hasWritePermission": True}
        )
    )
    resp = bundle.sdk.apps.get(app_id="app-1")
    assert_common(bundle, "GetApp")
    assert bundle.transport.body_json()["appId"] == "app-1"
    assert resp.app.id == "app-1"
    assert resp.has_write_permission is True


async def test_get_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"app": {"id": "app-2"}, "hasWritePermission": False})
    )
    resp = await bundle.sdk.apps.get_async(app_id="app-2")
    assert_common(bundle, "GetApp")
    assert resp.has_write_permission is False


def test_get_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.get(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_get_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.get_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_app_version
# ---------------------------------------------------------------------------


def test_get_app_version_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"version": {"versionNumber": 3}})
    )
    resp = bundle.sdk.apps.get_app_version(app_id="app-1", version_number=3)
    assert_common(bundle, "GetAppVersion")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-1"
    assert body["versionNumber"] == 3
    assert resp.version.version_number == 3


async def test_get_app_version_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"version": {"versionNumber": 5}}))
    resp = await bundle.sdk.apps.get_app_version_async(app_id="app-1", version_number=5)
    assert_common(bundle, "GetAppVersion")
    assert resp.version.version_number == 5


def test_get_app_version_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.get_app_version(app_id="app-1", version_number=99)
    assert exc_info.value.status_code == 404


async def test_get_app_version_async_502_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.get_app_version_async(app_id="app-1", version_number=99)
    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# get_app_view_stats
# ---------------------------------------------------------------------------


def test_get_app_view_stats_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalViews": 42}))
    resp = bundle.sdk.apps.get_app_view_stats(app_id="app-1")
    assert_common(bundle, "GetAppViewStats")
    assert bundle.transport.body_json()["appId"] == "app-1"
    assert resp.total_views == 42


async def test_get_app_view_stats_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalViews": 7}))
    resp = await bundle.sdk.apps.get_app_view_stats_async(app_id="app-2")
    assert_common(bundle, "GetAppViewStats")
    assert resp.total_views == 7


def test_get_app_view_stats_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.get_app_view_stats(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_get_app_view_stats_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.get_app_view_stats_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_members_with_apps
# ---------------------------------------------------------------------------


def test_get_members_with_apps_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))
    resp = bundle.sdk.apps.get_members_with_apps(body={})
    assert_common(bundle, "GetMembersWithApps")
    assert resp.members == []


async def test_get_members_with_apps_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))
    resp = await bundle.sdk.apps.get_members_with_apps_async(body={})
    assert_common(bundle, "GetMembersWithApps")
    assert resp.members == []


def test_get_members_with_apps_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.get_members_with_apps(body={})
    assert exc_info.value.status_code == 404


async def test_get_members_with_apps_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.get_members_with_apps_async(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# invoke_compute_function
# ---------------------------------------------------------------------------


def test_invoke_compute_function_sync_nested_payload_roundtrip(make_sdk):
    """params_json is a plain string field (JSON-encoded by the caller, not a
    dict/object type on the wire) -- verify it passes through byte-for-byte and
    that the response's result_json round-trips too."""
    import json as _json

    nested_payload = {"a": 1, "b": {"c": [1, 2, 3], "d": None}, "e": "text"}
    params_json_str = _json.dumps(nested_payload)

    bundle = make_sdk(
        lambda req: json_response(200, {"resultJson": _json.dumps({"ok": True})})
    )

    resp = bundle.sdk.apps.invoke_compute_function(
        app_id="app-1",
        function_name="my_fn",
        params_json=params_json_str,
    )

    assert_common(bundle, "InvokeAppComputeFunction")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-1"
    assert body["functionName"] == "my_fn"
    # paramsJson is sent as a raw JSON *string*, so decoding it should recover
    # the original nested dict.
    assert isinstance(body["paramsJson"], str)
    assert _json.loads(body["paramsJson"]) == nested_payload

    assert _json.loads(resp.result_json) == {"ok": True}


async def test_invoke_compute_function_async_nested_payload_roundtrip(make_sdk):
    import json as _json

    nested_payload = {"list": [1, {"x": "y"}], "flag": True}
    params_json_str = _json.dumps(nested_payload)

    bundle = make_sdk(lambda req: json_response(200, {"resultJson": "{}"}))

    resp = await bundle.sdk.apps.invoke_compute_function_async(
        app_id="app-2",
        function_name="my_fn2",
        params_json=params_json_str,
    )

    assert_common(bundle, "InvokeAppComputeFunction")
    body = bundle.transport.body_json()
    assert _json.loads(body["paramsJson"]) == nested_payload
    assert resp.result_json == "{}"


def test_invoke_compute_function_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.invoke_compute_function(app_id="x", function_name="f")
    assert exc_info.value.status_code == 404


async def test_invoke_compute_function_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.invoke_compute_function_async(app_id="x", function_name="f")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list
# ---------------------------------------------------------------------------


def test_list_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"apps": [{"id": "a1"}], "totalCount": 1})
    )
    resp = bundle.sdk.apps.list(limit=10, offset=0)
    assert_common(bundle, "ListApps")
    body = bundle.transport.body_json()
    assert body["limit"] == 10
    assert body["offset"] == 0
    assert resp.total_count == 1
    assert resp.apps[0].id == "a1"


async def test_list_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"apps": [], "totalCount": 0}))
    resp = await bundle.sdk.apps.list_async(limit=5, offset=2)
    assert_common(bundle, "ListApps")
    assert resp.total_count == 0


def test_list_edge_pagination_values_pass_through(make_sdk):
    """limit=0 and negative offset should just be forwarded verbatim -- the SDK
    itself does not validate or clamp these values."""
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.list(limit=0, offset=-5)
    body = bundle.transport.body_json()
    assert body["limit"] == 0
    assert body["offset"] == -5


def test_list_nullable_fields_unset_by_default(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.list()
    body = bundle.transport.body_json()
    assert "searchTerm" not in body
    assert "folderId" not in body
    assert "uncategorizedOnly" not in body
    assert "sharedWithMe" not in body


def test_list_nullable_fields_explicit_values_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.list(
        search_term="foo",
        folder_id="folder-1",
        uncategorized_only=True,
        shared_with_me=False,
    )
    body = bundle.transport.body_json()
    assert body["searchTerm"] == "foo"
    assert body["folderId"] == "folder-1"
    assert body["uncategorizedOnly"] is True
    assert body["sharedWithMe"] is False


def test_list_nullable_fields_explicit_none_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.list(search_term=None, folder_id=None)
    body = bundle.transport.body_json()
    assert "searchTerm" in body
    assert body["searchTerm"] is None
    assert "folderId" in body
    assert body["folderId"] is None


def test_list_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.list()
    assert exc_info.value.status_code == 404


async def test_list_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.list_async()
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_versions
# ---------------------------------------------------------------------------


def test_list_versions_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"versions": []}))
    bundle.sdk.apps.list_versions(app_id="app-1", limit=20, offset=0)
    assert_common(bundle, "ListAppVersions")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-1"
    assert body["limit"] == 20
    assert body["offset"] == 0


async def test_list_versions_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"versions": []}))
    await bundle.sdk.apps.list_versions_async(app_id="app-1", limit=1, offset=1)
    assert_common(bundle, "ListAppVersions")


def test_list_versions_edge_pagination_values_pass_through(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.list_versions(app_id="app-1", limit=0, offset=-1)
    body = bundle.transport.body_json()
    assert body["limit"] == 0
    assert body["offset"] == -1


def test_list_versions_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.list_versions(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_list_versions_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.list_versions_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# move_app_to_folder
# ---------------------------------------------------------------------------


def test_move_app_to_folder_sync_with_folder(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-1"}}))
    resp = bundle.sdk.apps.move_app_to_folder(app_id="app-1", folder_id="folder-1")
    assert_common(bundle, "MoveAppToFolder")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-1"
    assert body["folderId"] == "folder-1"
    assert resp.app.id == "app-1"


def test_move_app_to_folder_empty_string_folder_id(make_sdk):
    """Empty string folder_id (move to root) should be sent as an explicit
    empty string, not omitted."""
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.move_app_to_folder(app_id="app-1", folder_id="")
    body = bundle.transport.body_json()
    assert body["folderId"] == ""


def test_move_app_to_folder_unset_folder_id_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.move_app_to_folder(app_id="app-1")
    body = bundle.transport.body_json()
    assert "folderId" not in body


def test_move_app_to_folder_none_folder_id_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.move_app_to_folder(app_id="app-1", folder_id=None)
    body = bundle.transport.body_json()
    assert "folderId" in body
    assert body["folderId"] is None


def test_move_app_to_folder_empty_string_app_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.move_app_to_folder(app_id="", folder_id="folder-1")
    body = bundle.transport.body_json()
    assert body["appId"] == ""


async def test_move_app_to_folder_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-2"}}))
    resp = await bundle.sdk.apps.move_app_to_folder_async(
        app_id="app-2", folder_id="folder-2"
    )
    assert_common(bundle, "MoveAppToFolder")
    assert resp.app.id == "app-2"


def test_move_app_to_folder_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.move_app_to_folder(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_move_app_to_folder_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.move_app_to_folder_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# refresh
# ---------------------------------------------------------------------------


def test_refresh_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-1"}}))
    resp = bundle.sdk.apps.refresh(app_id="app-1")
    assert_common(bundle, "RefreshApp")
    assert bundle.transport.body_json()["appId"] == "app-1"
    assert resp.app.id == "app-1"


async def test_refresh_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-2"}}))
    resp = await bundle.sdk.apps.refresh_async(app_id="app-2")
    assert_common(bundle, "RefreshApp")
    assert resp.app.id == "app-2"


def test_refresh_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.refresh(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_refresh_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.refresh_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# restore_app_version
# ---------------------------------------------------------------------------


def test_restore_app_version_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-1"}}))
    resp = bundle.sdk.apps.restore_app_version(app_id="app-1", version_number=4)
    assert_common(bundle, "RestoreAppVersion")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-1"
    assert body["versionNumber"] == 4
    assert resp.app.id == "app-1"


async def test_restore_app_version_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-2"}}))
    resp = await bundle.sdk.apps.restore_app_version_async(
        app_id="app-2", version_number=1
    )
    assert_common(bundle, "RestoreAppVersion")
    assert resp.app.id == "app-2"


def test_restore_app_version_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.restore_app_version(app_id="missing", version_number=1)
    assert exc_info.value.status_code == 404


async def test_restore_app_version_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.restore_app_version_async(app_id="missing", version_number=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# set_favorite
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("favorited", [True, False])
def test_set_favorite_sync_boolean_values(make_sdk, favorited):
    bundle = make_sdk(lambda req: json_response(200, {"favorited": favorited}))
    resp = bundle.sdk.apps.set_favorite(
        primitive_type="app", primitive_id="app-1", favorited=favorited
    )
    assert_common(bundle, "SetFavorite")
    body = bundle.transport.body_json()
    assert body["favorited"] is favorited
    assert resp.favorited is favorited


def test_set_favorite_empty_string_ids(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"favorited": True}))
    bundle.sdk.apps.set_favorite(primitive_type="", primitive_id="", favorited=True)
    body = bundle.transport.body_json()
    assert body["primitiveType"] == ""
    assert body["primitiveId"] == ""


async def test_set_favorite_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"favorited": False}))
    resp = await bundle.sdk.apps.set_favorite_async(
        primitive_type="dashboard", primitive_id="dash-1", favorited=False
    )
    assert_common(bundle, "SetFavorite")
    assert resp.favorited is False


def test_set_favorite_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.set_favorite(
            primitive_type="app", primitive_id="missing", favorited=True
        )
    assert exc_info.value.status_code == 404


async def test_set_favorite_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.set_favorite_async(
            primitive_type="app", primitive_id="missing", favorited=True
        )
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------


def test_update_sync_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-1"}}))

    resp = bundle.sdk.apps.update(
        app_id="app-1",
        name="New Name",
        description="New Desc",
        code="print(2)",
        replace_data_sources=True,
        publish=True,
        staleness_seconds=60,
        replace_compute_functions=False,
        replace_files=True,
        schedule_enabled=True,
        cron_string="0 * * * *",
    )

    assert_common(bundle, "UpdateApp")
    body = bundle.transport.body_json()
    assert body["appId"] == "app-1"
    assert body["name"] == "New Name"
    assert body["description"] == "New Desc"
    assert body["code"] == "print(2)"
    assert body["replaceDataSources"] is True
    assert body["publish"] is True
    assert body["stalenessSeconds"] == 60
    assert body["replaceComputeFunctions"] is False
    assert body["replaceFiles"] is True
    assert body["scheduleEnabled"] is True
    assert body["cronString"] == "0 * * * *"
    assert resp.app.id == "app-1"


async def test_update_async_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"app": {"id": "app-2"}}))
    resp = await bundle.sdk.apps.update_async(app_id="app-2", name="Renamed")
    assert_common(bundle, "UpdateApp")
    body = bundle.transport.body_json()
    assert body["name"] == "Renamed"
    assert resp.app.id == "app-2"


def test_update_nullable_fields_unset_by_default(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.update(app_id="app-1")
    body = bundle.transport.body_json()
    for key in (
        "name",
        "description",
        "code",
        "replaceDataSources",
        "publish",
        "stalenessSeconds",
        "replaceComputeFunctions",
        "replaceFiles",
        "scheduleEnabled",
        "cronString",
    ):
        assert key not in body, f"expected {key!r} to be omitted when unset"
    # appId is not nullable, so it should still be present (non-null value).
    assert body["appId"] == "app-1"


def test_update_nullable_fields_explicit_none_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.update(
        app_id="app-1",
        name=None,
        description=None,
        code=None,
        replace_data_sources=None,
        publish=None,
        staleness_seconds=None,
        replace_compute_functions=None,
        replace_files=None,
        schedule_enabled=None,
        cron_string=None,
    )
    body = bundle.transport.body_json()
    for key in (
        "name",
        "description",
        "code",
        "replaceDataSources",
        "publish",
        "stalenessSeconds",
        "replaceComputeFunctions",
        "replaceFiles",
        "scheduleEnabled",
        "cronString",
    ):
        assert key in body, f"expected {key!r} to be present (explicit None)"
        assert body[key] is None


def test_update_list_fields_serialize_as_arrays(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.apps.update(
        app_id="app-1",
        compute_functions=[{"name": "fn1"}, {"name": "fn2"}],
        files=[{"path": "a.py", "content": "1"}, {"path": "b.py", "content": "2"}],
        data_sources=[
            {"type": "file", "file": {"dataset_id": "ds1"}},
        ],
    )
    body = bundle.transport.body_json()
    assert isinstance(body["computeFunctions"], list)
    assert len(body["computeFunctions"]) == 2
    assert body["computeFunctions"][0]["name"] == "fn1"
    assert isinstance(body["files"], list)
    assert len(body["files"]) == 2
    assert body["files"][1]["path"] == "b.py"
    assert isinstance(body["dataSources"], list)
    assert body["dataSources"][0]["file"]["datasetId"] == "ds1"


def test_update_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.update(app_id="missing")
    assert exc_info.value.status_code == 404


async def test_update_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.apps.update_async(app_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# retries
# ---------------------------------------------------------------------------


def test_retries_backoff_retries_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "server error"}),
            json_response(200, {"app": {"id": "app-1"}}),
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

    resp = bundle.sdk.apps.get(app_id="app-1", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.app.id == "app-1"


async def test_retries_backoff_retries_then_succeeds_async(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "server error"}),
            json_response(200, {"app": {"id": "app-2"}}),
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

    resp = await bundle.sdk.apps.get_async(app_id="app-2", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.app.id == "app-2"


# ---------------------------------------------------------------------------
# server_url / http_headers / timeout_ms per-call overrides
# ---------------------------------------------------------------------------


def test_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    override_url = "https://override.invalid"

    bundle.sdk.apps.get(app_id="app-1", server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.apps.get(app_id="app-1", http_headers={"X-Custom-Header": "custom-value"})

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    # auth header should still be present alongside the custom header
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_timeout_ms_override_does_not_break_request(make_sdk):
    """timeout_ms is consumed by the underlying httpx client timeout config, not
    reflected directly in the request; assert the call still completes
    successfully with the override applied (regression/smoke check)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.apps.get(app_id="app-1", timeout_ms=5000)

    assert len(bundle.transport.requests) == 1


# ---------------------------------------------------------------------------
# text/plain (non-JSON) error bodies still raise correctly
# ---------------------------------------------------------------------------


def test_text_error_response_still_raises_default_error(make_sdk):
    bundle = make_sdk(lambda req: text_response(404, "not found"))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.apps.get(app_id="missing")
    assert exc_info.value.status_code == 404
