"""Unit tests for sdk.rbac (RBACService) group-management operations."""
from __future__ import annotations

import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors

PATH_PREFIX = "/textql.rpc.public.rbac.RBACService"


# ---------------------------------------------------------------------------
# CreateGroup
# ---------------------------------------------------------------------------


def test_create_group_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "group": {
                    "id": "g1",
                    "orgId": "org1",
                    "name": "Engineers",
                    "description": "eng team",
                    "isSystem": False,
                    "memberCount": 2,
                    "connectorCount": 1,
                }
            },
        )
    )

    result = bundle.sdk.rbac.create_group(
        name="Engineers",
        description="eng team",
        member_ids=["u1", "u2"],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/CreateGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "Engineers"
    assert body["description"] == "eng team"
    assert body["memberIds"] == ["u1", "u2"]

    assert result.group.id == "g1"
    assert result.group.org_id == "org1"
    assert result.group.name == "Engineers"
    assert result.group.description == "eng team"
    assert result.group.is_system is False
    assert result.group.member_count == 2
    assert result.group.connector_count == 1


async def test_create_group_async_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"group": {"id": "g2", "name": "Sales"}})
    )

    result = await bundle.sdk.rbac.create_group_async(
        name="Sales", description="sales team", member_ids=["u3"]
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/CreateGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "Sales"
    assert body["description"] == "sales team"
    assert body["memberIds"] == ["u3"]

    assert result.group.id == "g2"
    assert result.group.name == "Sales"


def test_create_group_description_omitted_when_not_passed(make_sdk):
    """description is a plain Optional[str] field (not OptionalNullable), so
    leaving it unset means it's simply None on the model, and the model's
    custom serializer drops None values for fields listed in
    `optional_fields` -- confirm that behavior empirically."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_group(name="NoDescription")

    body = bundle.transport.body_json()
    assert body["name"] == "NoDescription"
    assert "description" not in body
    assert "memberIds" not in body


def test_create_group_description_explicit_none_is_also_omitted(make_sdk):
    """Explicitly passing description=None for this plain-Optional field
    produces the same result as omitting it (dropped from JSON), unlike a
    true OptionalNullable field where explicit None survives as JSON null."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_group(name="ExplicitNone", description=None)

    body = bundle.transport.body_json()
    assert "description" not in body


def test_create_group_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.create_group(name="X")

    assert exc_info.value.status_code == 403
    assert "forbidden" in str(exc_info.value)


async def test_create_group_async_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "duplicate name"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.create_group_async(name="X")

    assert exc_info.value.status_code == 409
    assert "duplicate name" in str(exc_info.value)


# ---------------------------------------------------------------------------
# UpdateGroup
# ---------------------------------------------------------------------------


def test_update_group_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"group": {"id": "g1", "name": "Renamed", "description": "new desc"}}
        )
    )

    result = bundle.sdk.rbac.update_group(
        group_id="g1", name="Renamed", description="new desc"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/UpdateGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"
    assert body["name"] == "Renamed"
    assert body["description"] == "new desc"

    assert result.group.id == "g1"
    assert result.group.name == "Renamed"
    assert result.group.description == "new desc"


async def test_update_group_async_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"group": {"id": "g2", "name": "Renamed2"}})
    )

    result = await bundle.sdk.rbac.update_group_async(group_id="g2", name="Renamed2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/UpdateGroup"
    body = bundle.transport.body_json()
    assert body["groupId"] == "g2"
    assert body["name"] == "Renamed2"
    assert result.group.name == "Renamed2"


def test_update_group_fields_omitted_when_unset(make_sdk):
    """name/description are plain Optional[str] fields on
    TextqlRPCPublicRbacUpdateGroupRequest. When not passed, they default to
    None and the custom model_serializer drops them entirely from JSON."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.update_group(group_id="g1")

    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"
    assert "name" not in body
    assert "description" not in body


def test_update_group_fields_explicit_none_also_omitted(make_sdk):
    """Confirms name/description are NOT OptionalNullable: explicit None
    produces the same omitted-from-JSON result as leaving them unset (a true
    OptionalNullable field would instead serialize explicit None as JSON
    null; see e.g. agents.update's slack_channel_id for contrast)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.update_group(group_id="g1", name=None, description=None)

    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"
    assert "name" not in body
    assert "description" not in body


def test_update_group_explicit_value_serializes(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.update_group(
        group_id="g1", name="NewName", description="NewDescription"
    )

    body = bundle.transport.body_json()
    assert body["name"] == "NewName"
    assert body["description"] == "NewDescription"


def test_update_group_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "group not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.update_group(group_id="missing")

    assert exc_info.value.status_code == 404
    assert "group not found" in str(exc_info.value)


async def test_update_group_async_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.update_group_async(group_id="g1")

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# DeleteGroup
# ---------------------------------------------------------------------------


def test_delete_group_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.delete_group(group_id="g1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/DeleteGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"
    assert result.success is True


async def test_delete_group_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.delete_group_async(group_id="g2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/DeleteGroup"
    body = bundle.transport.body_json()
    assert body["groupId"] == "g2"
    assert result.success is True


def test_delete_group_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.delete_group(group_id="missing")

    assert exc_info.value.status_code == 404
    assert "not found" in str(exc_info.value)


async def test_delete_group_async_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "cannot delete system group"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.delete_group_async(group_id="g-system")

    assert exc_info.value.status_code == 403
    assert "cannot delete system group" in str(exc_info.value)


# ---------------------------------------------------------------------------
# GetGroup
# ---------------------------------------------------------------------------


def test_get_group_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "group": {"id": "g1", "name": "Engineers"},
                "memberIds": ["u1", "u2", "u3"],
            },
        )
    )

    result = bundle.sdk.rbac.get_group(group_id="g1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/GetGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"
    assert result.group.id == "g1"
    assert result.group.name == "Engineers"
    assert result.member_ids == ["u1", "u2", "u3"]


async def test_get_group_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"group": {"id": "g9"}, "memberIds": []})
    )

    result = await bundle.sdk.rbac.get_group_async(group_id="g9")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/GetGroup"
    assert result.group.id == "g9"
    assert result.member_ids == []


def test_get_group_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no group"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_group(group_id="does-not-exist")

    assert exc_info.value.status_code == 404
    assert "no group" in str(exc_info.value)


async def test_get_group_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.get_group_async(group_id="g1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ListGroups
#
# NB: unlike most other RBAC group operations, list_groups takes `body`
# directly (a TextqlRPCPublicRbacListGroupsRequest, which currently has no
# fields at all -- see textql_rpc_public_rbac_listgroupsrequest.py) rather
# than individual kwargs that get wrapped into a body for you.
# ---------------------------------------------------------------------------


def test_list_groups_sync_multi_item_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "groups": [
                    {"id": "g1", "name": "Engineers", "memberCount": 5},
                    {"id": "g2", "name": "Sales", "memberCount": 3},
                    {"id": "g3", "name": "Support", "memberCount": 0, "isSystem": True},
                ]
            },
        )
    )

    result = bundle.sdk.rbac.list_groups(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListGroups"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    assert len(result.groups) == 3
    assert [g.id for g in result.groups] == ["g1", "g2", "g3"]
    assert result.groups[0].name == "Engineers"
    assert result.groups[0].member_count == 5
    assert result.groups[2].is_system is True


async def test_list_groups_async_multi_item_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "groups": [
                    {"id": "g1", "name": "A"},
                    {"id": "g2", "name": "B"},
                ]
            },
        )
    )

    result = await bundle.sdk.rbac.list_groups_async(body={})

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ListGroups"
    assert len(result.groups) == 2
    assert result.groups[1].id == "g2"


def test_list_groups_empty_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"groups": []}))

    result = bundle.sdk.rbac.list_groups(body={})

    assert result.groups == []


def test_list_groups_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_groups(body={})

    assert exc_info.value.status_code == 401
    assert "unauthorized" in str(exc_info.value)


async def test_list_groups_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.list_groups_async(body={})

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# AddGroupMember
# ---------------------------------------------------------------------------


def test_add_group_member_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.add_group_member(group_id="g1", member_id="u1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/AddGroupMember"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"
    assert body["memberId"] == "u1"
    assert result.success is True


async def test_add_group_member_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.add_group_member_async(group_id="g2", member_id="u2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/AddGroupMember"
    body = bundle.transport.body_json()
    assert body["groupId"] == "g2"
    assert body["memberId"] == "u2"
    assert result.success is True


def test_add_group_member_empty_string_ids_pass_through_unmodified(make_sdk):
    """Empty-string group_id/member_id should be sent through verbatim in the
    request body, not silently dropped or coerced -- an access-control bug
    here (e.g. treating "" as None/omitted) could mean a caller's intended
    empty-string ID gets ignored or replaced with server-side defaults."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.add_group_member(group_id="", member_id="")

    body = bundle.transport.body_json()
    assert body["groupId"] == ""
    assert body["memberId"] == ""


def test_add_group_member_unusual_ids_pass_through_unmodified(make_sdk):
    """IDs containing unusual characters (whitespace, unicode, path-like
    separators) must be passed through byte-for-byte."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    weird_group_id = "  g/../1  "
    weird_member_id = "u-snowman-null-ish"

    bundle.sdk.rbac.add_group_member(group_id=weird_group_id, member_id=weird_member_id)

    body = bundle.transport.body_json()
    assert body["groupId"] == weird_group_id
    assert body["memberId"] == weird_member_id


def test_add_group_member_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "group not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.add_group_member(group_id="missing", member_id="u1")

    assert exc_info.value.status_code == 404
    assert "group not found" in str(exc_info.value)


async def test_add_group_member_async_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.add_group_member_async(group_id="g1", member_id="u1")

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# RemoveGroupMember
# ---------------------------------------------------------------------------


def test_remove_group_member_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.remove_group_member(group_id="g1", member_id="u1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/RemoveGroupMember"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"
    assert body["memberId"] == "u1"
    assert result.success is True


async def test_remove_group_member_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.remove_group_member_async(
        group_id="g2", member_id="u2"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/RemoveGroupMember"
    body = bundle.transport.body_json()
    assert body["groupId"] == "g2"
    assert body["memberId"] == "u2"
    assert result.success is True


def test_remove_group_member_empty_string_ids_pass_through_unmodified(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.remove_group_member(group_id="", member_id="")

    body = bundle.transport.body_json()
    assert body["groupId"] == ""
    assert body["memberId"] == ""


def test_remove_group_member_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "member not in group"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.remove_group_member(group_id="g1", member_id="not-a-member")

    assert exc_info.value.status_code == 404
    assert "member not in group" in str(exc_info.value)


async def test_remove_group_member_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.remove_group_member_async(group_id="g1", member_id="u1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# GetMemberGroups
# ---------------------------------------------------------------------------


def test_get_member_groups_sync_multi_item_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "memberGroups": {
                    "u1": {
                        "groups": [
                            {"id": "g1", "name": "Engineers"},
                            {"id": "g2", "name": "Admins"},
                        ]
                    },
                    "u2": {"groups": [{"id": "g3", "name": "Sales"}]},
                    "u3": {"groups": []},
                }
            },
        )
    )

    result = bundle.sdk.rbac.get_member_groups(member_ids=["u1", "u2", "u3"])

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/GetMemberGroups"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["memberIds"] == ["u1", "u2", "u3"]

    assert set(result.member_groups.keys()) == {"u1", "u2", "u3"}
    assert len(result.member_groups["u1"].groups) == 2
    assert result.member_groups["u1"].groups[0].id == "g1"
    assert result.member_groups["u1"].groups[1].name == "Admins"
    assert result.member_groups["u2"].groups[0].id == "g3"
    assert result.member_groups["u3"].groups == []


async def test_get_member_groups_async_multi_item_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "memberGroups": {
                    "u1": {"groups": [{"id": "g1"}, {"id": "g2"}]},
                }
            },
        )
    )

    result = await bundle.sdk.rbac.get_member_groups_async(member_ids=["u1"])

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/GetMemberGroups"
    assert len(result.member_groups["u1"].groups) == 2


def test_get_member_groups_empty_string_member_id_passes_through(make_sdk):
    """An empty-string entry in member_ids should be preserved verbatim in
    the list sent to the server, not filtered out or coerced."""
    bundle = make_sdk(lambda req: json_response(200, {"memberGroups": {}}))

    bundle.sdk.rbac.get_member_groups(member_ids=["", "u1", ""])

    body = bundle.transport.body_json()
    assert body["memberIds"] == ["", "u1", ""]


def test_get_member_groups_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad member id"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_member_groups(member_ids=["bad"])

    assert exc_info.value.status_code == 400
    assert "bad member id" in str(exc_info.value)


async def test_get_member_groups_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.get_member_groups_async(member_ids=["u1"])

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ConvertRoleToGroup
# ---------------------------------------------------------------------------


def test_convert_role_to_group_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"groupId": "g-new", "migratedMemberCount": 4}
        )
    )

    result = bundle.sdk.rbac.convert_role_to_group(
        role_id="r1", drop_permissions=True
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ConvertRoleToGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["roleId"] == "r1"
    assert body["dropPermissions"] is True

    assert result.group_id == "g-new"
    assert result.migrated_member_count == 4


async def test_convert_role_to_group_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"groupId": "g-new2", "migratedMemberCount": 1})
    )

    result = await bundle.sdk.rbac.convert_role_to_group_async(
        role_id="r2", drop_permissions=False
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/ConvertRoleToGroup"
    body = bundle.transport.body_json()
    assert body["roleId"] == "r2"
    assert body["dropPermissions"] is False
    assert result.group_id == "g-new2"
    assert result.migrated_member_count == 1


def test_convert_role_to_group_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "role not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.convert_role_to_group(role_id="missing")

    assert exc_info.value.status_code == 404
    assert "role not found" in str(exc_info.value)


async def test_convert_role_to_group_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.convert_role_to_group_async(role_id="r1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ListGroupConnectors
# ---------------------------------------------------------------------------


def test_list_group_connectors_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "connectors": [
                    {
                        "accessId": "a1",
                        "connectorId": "c1",
                        "connectorName": "Snowflake",
                        "accessType": "read",
                    },
                    {
                        "accessId": "a2",
                        "connectorId": "c2",
                        "connectorName": "Postgres",
                        "accessType": "write",
                    },
                ]
            },
        )
    )

    result = bundle.sdk.rbac.list_group_connectors(group_id="g1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListGroupConnectors"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["groupId"] == "g1"

    assert len(result.connectors) == 2
    assert result.connectors[0].connector_id == "c1"
    assert result.connectors[0].connector_name == "Snowflake"
    assert result.connectors[0].access_type == "read"
    assert result.connectors[1].connector_id == "c2"


async def test_list_group_connectors_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"connectors": []}))

    result = await bundle.sdk.rbac.list_group_connectors_async(group_id="g2")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ListGroupConnectors"
    assert result.connectors == []


def test_list_group_connectors_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "group not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_group_connectors(group_id="missing")

    assert exc_info.value.status_code == 404
    assert "group not found" in str(exc_info.value)


async def test_list_group_connectors_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.list_group_connectors_async(group_id="g1")

    assert exc_info.value.status_code == 500
