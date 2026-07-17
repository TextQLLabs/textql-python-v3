"""Unit tests for Rbac service role/permission/member-role operations:"""
from __future__ import annotations

import pytest

from textql_sdk import errors

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

RBAC_PATH = "/textql.rpc.public.rbac.RBACService"


# --------------------------------------------------------------------------
# create_role
# --------------------------------------------------------------------------


def test_create_role_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"role": {"id": "r1", "name": "Analyst", "description": "desc"}}
        )
    )

    result = bundle.sdk.rbac.create_role(name="Analyst", description="desc")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/CreateRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"name": "Analyst", "description": "desc"}
    assert result.role.id == "r1"
    assert result.role.name == "Analyst"
    assert result.role.description == "desc"


def test_create_role_omits_unset_description(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"role": {"id": "r1"}}))

    bundle.sdk.rbac.create_role(name="Bare Role")

    body = bundle.transport.body_json()
    assert body == {"name": "Bare Role"}
    assert "description" not in body


@pytest.mark.asyncio
async def test_create_role_async_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"role": {"id": "r2", "name": "Async Role"}})
    )

    result = await bundle.sdk.rbac.create_role_async(name="Async Role")

    req = bundle.transport.last_request
    assert req.url.path == f"{RBAC_PATH}/CreateRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"name": "Async Role"}
    assert result.role.id == "r2"


def test_create_role_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid name"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.create_role(name="")

    assert exc_info.value.status_code == 400


# --------------------------------------------------------------------------
# update_role
# --------------------------------------------------------------------------


def test_update_role_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"role": {"id": "r1", "name": "Renamed", "description": "new desc"}}
        )
    )

    result = bundle.sdk.rbac.update_role(
        role_id="r1",
        name="Renamed",
        description="new desc",
        default_model_id=42,
        allowed_model_ids=[1, 2, 3],
        allow_model_choice=True,
        clear_allowed_model_ids=False,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/UpdateRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {
        "roleId": "r1",
        "name": "Renamed",
        "description": "new desc",
        "defaultModelId": 42,
        "allowedModelIds": [1, 2, 3],
        "allowModelChoice": True,
        "clearAllowedModelIds": False,
    }
    assert result.role.id == "r1"
    assert result.role.name == "Renamed"


def test_update_role_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"role": {"id": "r1"}}))

    bundle.sdk.rbac.update_role(role_id="r1", name="Just Rename")

    body = bundle.transport.body_json()
    assert body == {"roleId": "r1", "name": "Just Rename"}


@pytest.mark.asyncio
async def test_update_role_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"role": {"id": "r1", "name": "X"}}))

    result = await bundle.sdk.rbac.update_role_async(role_id="r1", name="X")

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/UpdateRole"
    assert bundle.transport.body_json() == {"roleId": "r1", "name": "X"}
    assert result.role.name == "X"


def test_update_role_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "role not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.update_role(role_id="missing", name="X")

    assert exc_info.value.status_code == 404


# --------------------------------------------------------------------------
# delete_role
# --------------------------------------------------------------------------


def test_delete_role_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.delete_role(role_id="r1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/DeleteRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"roleId": "r1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_delete_role_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.delete_role_async(role_id="r1")

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/DeleteRole"
    assert bundle.transport.body_json() == {"roleId": "r1"}
    assert result.success is True


def test_delete_role_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.delete_role(role_id="missing")

    assert exc_info.value.status_code == 404


# --------------------------------------------------------------------------
# get_role
# --------------------------------------------------------------------------


def test_get_role_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "role": {
                    "id": "r1",
                    "orgId": "org-1",
                    "name": "Admin",
                    "description": "Full access",
                    "isSystem": True,
                }
            },
        )
    )

    result = bundle.sdk.rbac.get_role(role_id="r1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/GetRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"roleId": "r1"}
    assert result.role.id == "r1"
    assert result.role.org_id == "org-1"
    assert result.role.name == "Admin"
    assert result.role.is_system is True


@pytest.mark.asyncio
async def test_get_role_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"role": {"id": "r1", "name": "Admin"}}))

    result = await bundle.sdk.rbac.get_role_async(role_id="r1")

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/GetRole"
    assert bundle.transport.body_json() == {"roleId": "r1"}
    assert result.role.name == "Admin"


def test_get_role_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_role(role_id="missing")

    assert exc_info.value.status_code == 404


# --------------------------------------------------------------------------
# list_roles  (empty request body model, but still required)
# --------------------------------------------------------------------------


def test_list_roles_sync_sends_correct_request_with_multiple_roles(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "roles": [
                    {"id": "r1", "name": "Admin", "description": "Full access", "isSystem": True},
                    {"id": "r2", "name": "Editor", "description": "Can edit content"},
                    {"id": "r3", "name": "Viewer", "description": "Read only", "isSystem": False},
                ]
            },
        )
    )

    result = bundle.sdk.rbac.list_roles(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/ListRoles"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert len(result.roles) == 3
    assert [r.id for r in result.roles] == ["r1", "r2", "r3"]
    assert [r.name for r in result.roles] == ["Admin", "Editor", "Viewer"]
    assert result.roles[0].is_system is True
    assert result.roles[2].is_system is False


@pytest.mark.asyncio
async def test_list_roles_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"roles": []}))

    result = await bundle.sdk.rbac.list_roles_async(body={})

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/ListRoles"
    assert result.roles == []


def test_list_roles_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_roles(body={})

    assert exc_info.value.status_code == 403


# --------------------------------------------------------------------------
# assign_permission_to_role
# --------------------------------------------------------------------------


def test_assign_permission_to_role_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.assign_permission_to_role(role_id="r1", permission_id="p1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/AssignPermissionToRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"roleId": "r1", "permissionId": "p1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_assign_permission_to_role_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.assign_permission_to_role_async(
        role_id="r1", permission_id="p1"
    )

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/AssignPermissionToRole"
    assert bundle.transport.body_json() == {"roleId": "r1", "permissionId": "p1"}
    assert result.success is True


def test_assign_permission_to_role_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "permission not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.assign_permission_to_role(role_id="r1", permission_id="missing")

    assert exc_info.value.status_code == 404


# --------------------------------------------------------------------------
# remove_permission_from_role
# --------------------------------------------------------------------------


def test_remove_permission_from_role_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.remove_permission_from_role(role_id="r1", permission_id="p1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/RemovePermissionFromRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"roleId": "r1", "permissionId": "p1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_remove_permission_from_role_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.remove_permission_from_role_async(
        role_id="r1", permission_id="p1"
    )

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/RemovePermissionFromRole"
    assert bundle.transport.body_json() == {"roleId": "r1", "permissionId": "p1"}
    assert result.success is True


def test_remove_permission_from_role_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not assigned"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.remove_permission_from_role(role_id="r1", permission_id="p1")

    assert exc_info.value.status_code == 404


# --------------------------------------------------------------------------
# get_role_permissions
# --------------------------------------------------------------------------


def test_get_role_permissions_sync_sends_correct_request_with_multiple_permissions(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "permissions": [
                    {"id": "p1", "resource": "dashboard", "action": "read", "description": "View dashboards"},
                    {"id": "p2", "resource": "dashboard", "action": "write", "description": "Edit dashboards"},
                    {"id": "p3", "resource": "connector", "action": "delete", "description": "Delete connectors"},
                ]
            },
        )
    )

    result = bundle.sdk.rbac.get_role_permissions(role_id="r1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/GetRolePermissions"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"roleId": "r1"}
    assert len(result.permissions) == 3
    assert [p.id for p in result.permissions] == ["p1", "p2", "p3"]
    assert result.permissions[0].resource == "dashboard"
    assert result.permissions[0].action == "read"
    assert result.permissions[2].action == "delete"


@pytest.mark.asyncio
async def test_get_role_permissions_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"permissions": []}))

    result = await bundle.sdk.rbac.get_role_permissions_async(role_id="r1")

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/GetRolePermissions"
    assert bundle.transport.body_json() == {"roleId": "r1"}
    assert result.permissions == []


def test_get_role_permissions_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "role not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_role_permissions(role_id="missing")

    assert exc_info.value.status_code == 404


# --------------------------------------------------------------------------
# list_permissions  (empty request body model, but still required)
# --------------------------------------------------------------------------


def test_list_permissions_sync_sends_correct_request_with_multiple_permissions(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "permissions": [
                    {"id": "p1", "resource": "dashboard", "action": "read"},
                    {"id": "p2", "resource": "connector", "action": "write"},
                    {"id": "p3", "resource": "agent", "action": "execute"},
                    {"id": "p4", "resource": "org", "action": "admin"},
                ]
            },
        )
    )

    result = bundle.sdk.rbac.list_permissions(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/ListPermissions"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert len(result.permissions) == 4
    assert [p.id for p in result.permissions] == ["p1", "p2", "p3", "p4"]
    assert [p.action for p in result.permissions] == ["read", "write", "execute", "admin"]


@pytest.mark.asyncio
async def test_list_permissions_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"permissions": []}))

    result = await bundle.sdk.rbac.list_permissions_async(body={})

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/ListPermissions"
    assert result.permissions == []


def test_list_permissions_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_permissions(body={})

    assert exc_info.value.status_code == 403


# --------------------------------------------------------------------------
# assign_role_to_member  ("deep dive" target: access-granting operation)
# --------------------------------------------------------------------------


def test_assign_role_to_member_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.assign_role_to_member(member_id="m1", role_id="r1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/AssignRoleToMember"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"memberId": "m1", "roleId": "r1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_assign_role_to_member_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.assign_role_to_member_async(member_id="m1", role_id="r1")

    req = bundle.transport.last_request
    assert req.url.path == f"{RBAC_PATH}/AssignRoleToMember"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"memberId": "m1", "roleId": "r1"}
    assert result.success is True


def test_assign_role_to_member_sync_403_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(403, {"message": "insufficient privileges to grant role"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.assign_role_to_member(member_id="m1", role_id="r1")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_assign_role_to_member_async_403_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(403, {"message": "insufficient privileges to grant role"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.assign_role_to_member_async(member_id="m1", role_id="r1")

    assert exc_info.value.status_code == 403


def test_assign_role_to_member_omits_unset_fields(make_sdk):
    """member_id/role_id are both plain Optional[str] (no OptionalNullable
    wrapper) in TextqlRPCPublicRbacAssignRoleToMemberRequest, so simply
    omitting a kwarg must drop the corresponding key rather than emit null."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.assign_role_to_member(member_id="m1")

    body = bundle.transport.body_json()
    assert body == {"memberId": "m1"}
    assert "roleId" not in body


def test_assign_role_to_member_explicit_value_present_in_body(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.assign_role_to_member(member_id="m1", role_id="r1")

    body = bundle.transport.body_json()
    assert body["memberId"] == "m1"
    assert body["roleId"] == "r1"


def test_assign_role_to_member_4xx_non_403_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "member not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.assign_role_to_member(member_id="missing", role_id="r1")

    assert exc_info.value.status_code == 404


def test_assign_role_to_member_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.assign_role_to_member(member_id="m1", role_id="r1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# remove_role_from_member  ("deep dive" target: access-revoking operation)
# --------------------------------------------------------------------------


def test_remove_role_from_member_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.remove_role_from_member(member_id="m1", role_id="r1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/RemoveRoleFromMember"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"memberId": "m1", "roleId": "r1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_remove_role_from_member_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.remove_role_from_member_async(member_id="m1", role_id="r1")

    req = bundle.transport.last_request
    assert req.url.path == f"{RBAC_PATH}/RemoveRoleFromMember"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"memberId": "m1", "roleId": "r1"}
    assert result.success is True


def test_remove_role_from_member_sync_403_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(403, {"message": "insufficient privileges to revoke role"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.remove_role_from_member(member_id="m1", role_id="r1")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_remove_role_from_member_async_403_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(403, {"message": "insufficient privileges to revoke role"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.remove_role_from_member_async(member_id="m1", role_id="r1")

    assert exc_info.value.status_code == 403


def test_remove_role_from_member_omits_unset_fields(make_sdk):
    """member_id/role_id are both plain Optional[str] (no OptionalNullable
    wrapper) in TextqlRPCPublicRbacRemoveRoleFromMemberRequest, so omitting a
    kwarg must drop the corresponding key rather than emit null."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.remove_role_from_member(role_id="r1")

    body = bundle.transport.body_json()
    assert body == {"roleId": "r1"}
    assert "memberId" not in body


def test_remove_role_from_member_explicit_value_present_in_body(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.remove_role_from_member(member_id="m1", role_id="r1")

    body = bundle.transport.body_json()
    assert body["memberId"] == "m1"
    assert body["roleId"] == "r1"


def test_remove_role_from_member_4xx_non_403_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "assignment not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.remove_role_from_member(member_id="m1", role_id="missing")

    assert exc_info.value.status_code == 404


def test_remove_role_from_member_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.remove_role_from_member(member_id="m1", role_id="r1")

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# get_member_roles
# --------------------------------------------------------------------------


def test_get_member_roles_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "memberRoles": {
                    "m1": {"roles": [{"id": "r1", "name": "Admin"}]},
                    "m2": {"roles": [{"id": "r2", "name": "Viewer"}, {"id": "r3", "name": "Editor"}]},
                }
            },
        )
    )

    result = bundle.sdk.rbac.get_member_roles(member_ids=["m1", "m2"])

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/GetMemberRoles"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"memberIds": ["m1", "m2"]}
    assert set(result.member_roles.keys()) == {"m1", "m2"}
    assert result.member_roles["m1"].roles[0].id == "r1"
    assert len(result.member_roles["m2"].roles) == 2
    assert result.member_roles["m2"].roles[1].name == "Editor"


@pytest.mark.asyncio
async def test_get_member_roles_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"memberRoles": {}}))

    result = await bundle.sdk.rbac.get_member_roles_async(member_ids=["m1"])

    assert bundle.transport.last_request.url.path == f"{RBAC_PATH}/GetMemberRoles"
    assert bundle.transport.body_json() == {"memberIds": ["m1"]}
    assert result.member_roles == {}


def test_get_member_roles_omits_unset_member_ids(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"memberRoles": {}}))

    bundle.sdk.rbac.get_member_roles()

    body = bundle.transport.body_json()
    assert body == {}
    assert "memberIds" not in body


def test_get_member_roles_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_member_roles(member_ids=["m1"])

    assert exc_info.value.status_code == 403


# --------------------------------------------------------------------------
# get_current_member_roles_and_permissions  (empty request body model)
# --------------------------------------------------------------------------


def test_get_current_member_roles_and_permissions_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "roles": [
                    {"id": "r1", "name": "Admin"},
                    {"id": "r2", "name": "Editor"},
                ],
                "permissions": [
                    {"id": "p1", "resource": "dashboard", "action": "read"},
                    {"id": "p2", "resource": "dashboard", "action": "write"},
                    {"id": "p3", "resource": "connector", "action": "read"},
                ],
            },
        )
    )

    result = bundle.sdk.rbac.get_current_member_roles_and_permissions(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{RBAC_PATH}/GetCurrentMemberRolesAndPermissions"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert [r.id for r in result.roles] == ["r1", "r2"]
    assert len(result.permissions) == 3
    assert result.permissions[1].action == "write"


@pytest.mark.asyncio
async def test_get_current_member_roles_and_permissions_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"roles": [], "permissions": []}))

    result = await bundle.sdk.rbac.get_current_member_roles_and_permissions_async(body={})

    assert (
        bundle.transport.last_request.url.path
        == f"{RBAC_PATH}/GetCurrentMemberRolesAndPermissions"
    )
    assert result.roles == []
    assert result.permissions == []


def test_get_current_member_roles_and_permissions_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthenticated"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_current_member_roles_and_permissions(body={})

    assert exc_info.value.status_code == 401
