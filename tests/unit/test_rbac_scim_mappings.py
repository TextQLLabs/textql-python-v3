"""Unit tests for sdk.rbac (RBACService) SCIM group mapping operations:"""
from __future__ import annotations

import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, utils

PATH_PREFIX = "/textql.rpc.public.rbac.RBACService"


# ---------------------------------------------------------------------------
# ListScimGroupMappings
# ---------------------------------------------------------------------------


def test_list_scim_group_mappings_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"mappings": []}))

    result = bundle.sdk.rbac.list_scim_group_mappings(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListScimGroupMappings"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.mappings == []


async def test_list_scim_group_mappings_async_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"mappings": []}))

    result = await bundle.sdk.rbac.list_scim_group_mappings_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListScimGroupMappings"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.mappings == []


def test_list_scim_group_mappings_sync_multi_item_response_unmarshals(make_sdk):
    payload = {
        "mappings": [
            {
                "id": "map-1",
                "displayName": "Engineering",
                "externalId": "ext-1",
                "roleId": "role-1",
                "roleName": "Engineer",
                "groupId": "",
                "groupName": "",
                "targetMode": "role",
                "isSystem": False,
            },
            {
                "id": "map-2",
                "displayName": "Sales",
                "externalId": "ext-2",
                "roleId": "",
                "roleName": "",
                "groupId": "group-2",
                "groupName": "Sales Group",
                "targetMode": "group",
                "isSystem": True,
            },
            {
                "id": "map-3",
                "displayName": "Admins",
                "externalId": "ext-3",
                "roleId": "role-3",
                "roleName": "Admin",
                "groupId": "",
                "groupName": "",
                "targetMode": "role",
                "isSystem": True,
            },
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.rbac.list_scim_group_mappings(body={})

    assert len(result.mappings) == 3

    m1, m2, m3 = result.mappings
    assert m1.id == "map-1"
    assert m1.display_name == "Engineering"
    assert m1.external_id == "ext-1"
    assert m1.role_id == "role-1"
    assert m1.role_name == "Engineer"
    assert m1.target_mode == "role"
    assert m1.is_system is False

    assert m2.id == "map-2"
    assert m2.group_id == "group-2"
    assert m2.group_name == "Sales Group"
    assert m2.target_mode == "group"
    assert m2.is_system is True

    assert m3.id == "map-3"
    assert m3.role_name == "Admin"
    assert m3.is_system is True


async def test_list_scim_group_mappings_async_multi_item_response_unmarshals(make_sdk):
    payload = {
        "mappings": [
            {"id": "map-a", "displayName": "A", "targetMode": "role"},
            {"id": "map-b", "displayName": "B", "targetMode": "group"},
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.rbac.list_scim_group_mappings_async(body={})

    assert len(result.mappings) == 2
    assert result.mappings[0].id == "map-a"
    assert result.mappings[1].id == "map-b"
    assert result.mappings[1].target_mode == "group"


def test_list_scim_group_mappings_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_scim_group_mappings(body={})

    assert exc_info.value.status_code == 404
    assert "not found" in str(exc_info.value)


async def test_list_scim_group_mappings_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "internal error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.list_scim_group_mappings_async(body={})

    assert exc_info.value.status_code == 500
    assert "internal error" in str(exc_info.value)


# ---------------------------------------------------------------------------
# MigrateAllScimGroupMappings
#
# This is a bulk/destructive-ish operation (migrates every SCIM group mapping
# in one call) so access-control on this endpoint matters -- explicitly cover
# a 403 Forbidden response in addition to the standard success/4xx/5xx cases.
# ---------------------------------------------------------------------------


def test_migrate_all_scim_group_mappings_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"migratedMappingCount": 7}))

    result = bundle.sdk.rbac.migrate_all_scim_group_mappings(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/MigrateAllScimGroupMappings"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.migrated_mapping_count == 7


async def test_migrate_all_scim_group_mappings_async_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"migratedMappingCount": 3}))

    result = await bundle.sdk.rbac.migrate_all_scim_group_mappings_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/MigrateAllScimGroupMappings"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.migrated_mapping_count == 3


def test_migrate_all_scim_group_mappings_sync_forbidden_raises_403(make_sdk):
    """High blast-radius bulk migration: access-control (403) must surface
    as a TextqlDefaultError with status_code 403, not be silently swallowed
    or retried away."""
    bundle = make_sdk(
        lambda req: json_response(403, {"message": "insufficient permissions to migrate all scim group mappings"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.migrate_all_scim_group_mappings(body={})

    assert exc_info.value.status_code == 403
    assert "insufficient permissions" in str(exc_info.value)
    assert len(bundle.transport.requests) == 1


async def test_migrate_all_scim_group_mappings_async_forbidden_raises_403(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.migrate_all_scim_group_mappings_async(body={})

    assert exc_info.value.status_code == 403
    assert "forbidden" in str(exc_info.value)
    assert len(bundle.transport.requests) == 1


def test_migrate_all_scim_group_mappings_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.migrate_all_scim_group_mappings(body={})

    assert exc_info.value.status_code == 400


async def test_migrate_all_scim_group_mappings_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.migrate_all_scim_group_mappings_async(body={})

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# MigrateScimGroupMappingToGroup
# ---------------------------------------------------------------------------


def test_migrate_scim_group_mapping_to_group_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id="map-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/MigrateScimGroupMappingToGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["mappingId"] == "map-1"
    # Response model has no fields, so it just unmarshals to an empty object.
    assert result is not None


async def test_migrate_scim_group_mapping_to_group_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.rbac.migrate_scim_group_mapping_to_group_async(mapping_id="map-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/MigrateScimGroupMappingToGroup"
    body = bundle.transport.body_json()
    assert body["mappingId"] == "map-2"
    assert result is not None


def test_migrate_scim_group_mapping_to_group_omitted_mapping_id_omits_field(make_sdk):
    """mapping_id defaults to None and is a plain Optional[str] (not an
    UNSET-sentinel Nullable field), but the custom model_serializer still
    drops None values for fields in `optional_fields` -- confirm the field is
    absent from the wire body when not passed."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.migrate_scim_group_mapping_to_group()

    body = bundle.transport.body_json()
    assert "mappingId" not in body


def test_migrate_scim_group_mapping_to_group_explicit_none_omits_field(make_sdk):
    """Explicitly passing mapping_id=None behaves the same as omitting it,
    since this is a plain Optional[str] field (no UNSET sentinel tracking via
    __pydantic_fields_set__ like the Nullable fields on other operations)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id=None)

    body = bundle.transport.body_json()
    assert "mappingId" not in body


def test_migrate_scim_group_mapping_to_group_explicit_value_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id="explicit-map-id")

    body = bundle.transport.body_json()
    assert body["mappingId"] == "explicit-map-id"


def test_migrate_scim_group_mapping_to_group_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "mapping not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id="missing")

    assert exc_info.value.status_code == 404
    assert "mapping not found" in str(exc_info.value)


async def test_migrate_scim_group_mapping_to_group_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.migrate_scim_group_mapping_to_group_async(mapping_id="map-1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# RevertScimGroupMappingToRole
# ---------------------------------------------------------------------------


def test_revert_scim_group_mapping_to_role_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.revert_scim_group_mapping_to_role(mapping_id="map-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/RevertScimGroupMappingToRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["mappingId"] == "map-1"
    assert result.success is True


async def test_revert_scim_group_mapping_to_role_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = await bundle.sdk.rbac.revert_scim_group_mapping_to_role_async(mapping_id="map-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/RevertScimGroupMappingToRole"
    body = bundle.transport.body_json()
    assert body["mappingId"] == "map-2"
    assert result.success is False


def test_revert_scim_group_mapping_to_role_omitted_mapping_id_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.revert_scim_group_mapping_to_role()

    body = bundle.transport.body_json()
    assert "mappingId" not in body


def test_revert_scim_group_mapping_to_role_explicit_none_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.revert_scim_group_mapping_to_role(mapping_id=None)

    body = bundle.transport.body_json()
    assert "mappingId" not in body


def test_revert_scim_group_mapping_to_role_explicit_value_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.revert_scim_group_mapping_to_role(mapping_id="explicit-map-id")

    body = bundle.transport.body_json()
    assert body["mappingId"] == "explicit-map-id"


def test_revert_scim_group_mapping_to_role_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "mapping not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.revert_scim_group_mapping_to_role(mapping_id="missing")

    assert exc_info.value.status_code == 404
    assert "mapping not found" in str(exc_info.value)


async def test_revert_scim_group_mapping_to_role_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.revert_scim_group_mapping_to_role_async(mapping_id="map-1")

    assert exc_info.value.status_code == 502
    assert "bad gateway" in str(exc_info.value)


# ---------------------------------------------------------------------------
# Cross-cutting behavior: retries, server_url override, http_headers,
# timeout_ms. These use migrate_scim_group_mapping_to_group,
# revert_scim_group_mapping_to_role, and list_scim_group_mappings as
# convenient vehicles among the 4 SCIM-mapping RBAC operations.
# ---------------------------------------------------------------------------


def test_retries_on_503_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(503, {"message": "temporarily unavailable"}),
            json_response(200, {}),
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

    result = bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id="map-1", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result is not None


async def test_retries_async_on_429_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(429, {"message": "rate limited"}),
            json_response(200, {"success": True}),
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

    result = await bundle.sdk.rbac.revert_scim_group_mapping_to_role_async(
        mapping_id="map-1", retries=retry_config
    )

    assert len(bundle.transport.requests) == 2
    assert result.success is True


def test_retries_multiple_5xx_then_succeeds(make_sdk, sequence_handler):
    """Two failing responses (500 then 502) followed by a 200 -- confirms the
    SDK keeps retrying across more than one failure, not just a single
    retry-then-give-up."""
    handler = sequence_handler(
        [
            json_response(500, {"message": "err1"}),
            json_response(502, {"message": "err2"}),
            json_response(200, {"mappings": [{"id": "map-1"}]}),
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

    result = bundle.sdk.rbac.list_scim_group_mappings(body={}, retries=retry_config)

    assert len(bundle.transport.requests) == 3
    assert result.mappings[0].id == "map-1"


def test_no_retries_configured_5xx_raises_immediately(make_sdk):
    """Contrast case: without a retries= override (and no client-level retry
    config configured by make_sdk), a single 5xx must raise immediately with
    exactly one request recorded -- no implicit retrying."""
    bundle = make_sdk(lambda req: json_response(503, {"message": "down"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id="map-1")

    assert exc_info.value.status_code == 503
    assert len(bundle.transport.requests) == 1


async def test_no_retries_configured_5xx_raises_immediately_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "down"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.revert_scim_group_mapping_to_role_async(mapping_id="map-1")

    assert exc_info.value.status_code == 500
    assert len(bundle.transport.requests) == 1


def test_server_url_override_changes_host(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    override_url = "https://some-other-host.invalid"
    bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id="map-1", server_url=override_url)

    req = bundle.transport.last_request
    assert req.url.scheme == "https"
    assert req.url.host == "some-other-host.invalid"
    assert req.url.host != "textql-sdk-tests.invalid"


async def test_server_url_override_changes_host_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    override_url = "https://some-other-host-async.invalid"
    await bundle.sdk.rbac.revert_scim_group_mapping_to_role_async(
        mapping_id="map-1", server_url=override_url
    )

    req = bundle.transport.last_request
    assert req.url.host == "some-other-host-async.invalid"
    assert req.url.host != "textql-sdk-tests.invalid"


def test_http_headers_passthrough(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.migrate_scim_group_mapping_to_group(
        mapping_id="map-1", http_headers={"X-Custom-Test": "value123"}
    )

    req = bundle.transport.last_request
    assert req.headers["x-custom-test"] == "value123"


async def test_http_headers_passthrough_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    await bundle.sdk.rbac.revert_scim_group_mapping_to_role_async(
        mapping_id="map-1", http_headers={"X-Custom-Test": "value123"}
    )

    req = bundle.transport.last_request
    assert req.headers["x-custom-test"] == "value123"


def test_timeout_ms_override_reflected_on_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.migrate_scim_group_mapping_to_group(mapping_id="map-1", timeout_ms=5000)

    req = bundle.transport.last_request
    timeout_ext = req.extensions.get("timeout")
    assert timeout_ext is not None
    # httpx converts the float-seconds timeout into a dict of connect/read/etc
    # keys; 5000ms == 5.0s.
    assert timeout_ext.get("read") == pytest.approx(5.0)


async def test_timeout_ms_override_reflected_on_request_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    await bundle.sdk.rbac.revert_scim_group_mapping_to_role_async(mapping_id="map-1", timeout_ms=5000)

    req = bundle.transport.last_request
    timeout_ext = req.extensions.get("timeout")
    assert timeout_ext is not None
    assert timeout_ext.get("read") == pytest.approx(5.0)
