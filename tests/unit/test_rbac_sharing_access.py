"""Unit tests for Rbac object-level sharing and access-control operations."""
import pytest

from textql_sdk import errors
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

BASE_PATH = "/textql.rpc.public.rbac.RBACService"


# ---------------------------------------------------------------------------
# share_object / share_object_async
# ---------------------------------------------------------------------------


def test_share_object_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.share_object(
        object_type="dashboard",
        object_id="dash-1",
        member_id="member-1",
        access_type="editor",
        is_public=False,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ShareObject"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"
    assert body["memberId"] == "member-1"
    assert body["accessType"] == "editor"
    assert body["isPublic"] is False

    assert result.success is True


@pytest.mark.asyncio
async def test_share_object_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.share_object_async(
        object_type="dashboard",
        object_id="dash-1",
        member_id="member-1",
        access_type="viewer",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ShareObject"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectId"] == "dash-1"
    assert body["accessType"] == "viewer"
    assert result.success is True


def test_share_object_with_expires_at_serializes_timestamp(make_sdk):
    import datetime as dt

    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    expiry = dt.datetime(2030, 1, 1, tzinfo=dt.timezone.utc)
    bundle.sdk.rbac.share_object(
        object_type="dashboard",
        object_id="dash-1",
        member_id="member-1",
        access_type="viewer",
        expires_at=expiry,
    )

    body = bundle.transport.body_json()
    assert body["expiresAt"].startswith("2030-01-01T00:00:00")


def test_share_object_403_forbidden_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(403, {"message": "not permitted to share this object"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.share_object(
            object_type="dashboard", object_id="dash-1", member_id="m1", access_type="owner"
        )

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_share_object_async_403_forbidden_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.share_object_async(
            object_type="dashboard", object_id="dash-1", member_id="m1", access_type="owner"
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# share_object_with_role / share_object_with_role_async
# ---------------------------------------------------------------------------


def test_share_object_with_role_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.share_object_with_role(
        object_type="agent",
        object_id="agent-1",
        role_id="role-1",
        access_type="editor",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ShareObjectWithRole"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "agent"
    assert body["objectId"] == "agent-1"
    assert body["roleId"] == "role-1"
    assert body["accessType"] == "editor"
    assert result.success is True


@pytest.mark.asyncio
async def test_share_object_with_role_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.share_object_with_role_async(
        object_type="agent",
        object_id="agent-1",
        role_id="role-1",
        access_type="viewer",
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ShareObjectWithRole"
    body = bundle.transport.body_json()
    assert body["roleId"] == "role-1"
    assert result.success is True


def test_share_object_with_role_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.share_object_with_role(
            object_type="agent", object_id="agent-1", role_id="role-1", access_type="owner"
        )

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_share_object_with_role_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.share_object_with_role_async(
            object_type="agent", object_id="agent-1", role_id="role-1", access_type="owner"
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# share_with_group / share_with_group_async
# (source method name is `share_with_group`, RPC is ShareObjectWithGroup)
# ---------------------------------------------------------------------------


def test_share_with_group_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.share_with_group(
        object_type="dataset",
        object_id="ds-1",
        group_id="group-1",
        access_type="viewer",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ShareObjectWithGroup"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dataset"
    assert body["objectId"] == "ds-1"
    assert body["groupId"] == "group-1"
    assert body["accessType"] == "viewer"
    assert result.success is True


@pytest.mark.asyncio
async def test_share_with_group_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.share_with_group_async(
        object_type="dataset",
        object_id="ds-1",
        group_id="group-1",
        access_type="editor",
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ShareObjectWithGroup"
    body = bundle.transport.body_json()
    assert body["groupId"] == "group-1"
    assert result.success is True


def test_share_with_group_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.share_with_group(
            object_type="dataset", object_id="ds-1", group_id="group-1", access_type="owner"
        )

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_share_with_group_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.share_with_group_async(
            object_type="dataset", object_id="ds-1", group_id="group-1", access_type="owner"
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# get_object_access / get_object_access_async
# ---------------------------------------------------------------------------


def test_get_object_access_sends_correct_request_and_unmarshals(make_sdk):
    payload = {
        "accessEntries": [
            {
                "id": "access-1",
                "objectType": "dashboard",
                "objectId": "dash-1",
                "memberId": "member-1",
                "accessType": "owner",
                "isPublic": False,
            }
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.rbac.get_object_access(object_type="dashboard", object_id="dash-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetObjectAccess"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"

    assert len(result.access_entries) == 1
    entry = result.access_entries[0]
    assert entry.id == "access-1"
    assert entry.member_id == "member-1"
    assert entry.access_type == "owner"
    assert entry.is_public is False


@pytest.mark.asyncio
async def test_get_object_access_async_sends_correct_request(make_sdk):
    payload = {"accessEntries": []}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.rbac.get_object_access_async(
        object_type="dashboard", object_id="dash-1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetObjectAccess"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert result.access_entries == []


def test_get_object_access_empty_string_object_id_still_sent(make_sdk):
    """Edge case: an empty-string object_id must still be included in the
    request body (not silently dropped), since object_type="" != absent."""
    bundle = make_sdk(lambda req: json_response(200, {"accessEntries": []}))

    bundle.sdk.rbac.get_object_access(object_type="dashboard", object_id="")

    body = bundle.transport.body_json()
    assert "objectId" in body
    assert body["objectId"] == ""


def test_get_object_access_whitespace_and_special_char_object_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"accessEntries": []}))

    weird_id = "  weird/id?with#chars&é中文  "
    bundle.sdk.rbac.get_object_access(object_type="dashboard", object_id=weird_id)

    body = bundle.transport.body_json()
    assert body["objectId"] == weird_id


def test_get_object_access_very_long_object_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"accessEntries": []}))

    long_id = "x" * 5000
    bundle.sdk.rbac.get_object_access(object_type="dashboard", object_id=long_id)

    body = bundle.transport.body_json()
    assert body["objectId"] == long_id
    assert len(body["objectId"]) == 5000


def test_get_object_access_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_object_access(object_type="dashboard", object_id="dash-1")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_get_object_access_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.get_object_access_async(
            object_type="dashboard", object_id="dash-1"
        )

    assert exc_info.value.status_code == 403


def test_get_object_access_401_unauthorized(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_object_access(object_type="dashboard", object_id="dash-1")

    assert exc_info.value.status_code == 401


# ---------------------------------------------------------------------------
# update_object_access / update_object_access_async
# ---------------------------------------------------------------------------


def test_update_object_access_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.update_object_access(
        access_id="access-1", access_type="editor"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpdateObjectAccess"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["accessId"] == "access-1"
    assert body["accessType"] == "editor"
    assert result.success is True


@pytest.mark.asyncio
async def test_update_object_access_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.update_object_access_async(
        access_id="access-1", access_type="viewer"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/UpdateObjectAccess"
    body = bundle.transport.body_json()
    assert body["accessType"] == "viewer"
    assert result.success is True


def test_update_object_access_expires_at_included_when_set(make_sdk):
    import datetime as dt

    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    expiry = dt.datetime(2031, 6, 15, tzinfo=dt.timezone.utc)
    bundle.sdk.rbac.update_object_access(
        access_id="access-1", access_type="viewer", expires_at=expiry
    )

    body = bundle.transport.body_json()
    assert body["expiresAt"].startswith("2031-06-15")


def test_update_object_access_expires_at_omitted_when_not_passed(make_sdk):
    """expires_at is a plain Optional[datetime] = None (not OptionalNullable);
    when not passed it should not appear in the serialized body."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.update_object_access(access_id="access-1", access_type="viewer")

    body = bundle.transport.body_json()
    assert "expiresAt" not in body


def test_update_object_access_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.update_object_access(access_id="access-1", access_type="owner")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_update_object_access_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.update_object_access_async(
            access_id="access-1", access_type="owner"
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# update_object_visibility / update_object_visibility_async
# ---------------------------------------------------------------------------


def test_update_object_visibility_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.update_object_visibility(
        object_type="dashboard", object_id="dash-1", is_public=True
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpdateObjectVisibility"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"
    assert body["isPublic"] is True
    assert result.success is True


@pytest.mark.asyncio
async def test_update_object_visibility_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.update_object_visibility_async(
        object_type="dashboard", object_id="dash-1", is_public=False
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/UpdateObjectVisibility"
    body = bundle.transport.body_json()
    assert body["isPublic"] is False
    assert result.success is True


def test_update_object_visibility_is_public_false_is_sent_explicitly(make_sdk):
    """is_public=False must be serialized as `false`, not omitted (a common
    truthiness bug: `if is_public:` would silently drop `False`)."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.update_object_visibility(
        object_type="dashboard", object_id="dash-1", is_public=False
    )

    body = bundle.transport.body_json()
    assert "isPublic" in body
    assert body["isPublic"] is False


def test_update_object_visibility_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.update_object_visibility(
            object_type="dashboard", object_id="dash-1", is_public=True
        )

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_update_object_visibility_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.update_object_visibility_async(
            object_type="dashboard", object_id="dash-1", is_public=True
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# has_object_access / has_object_access_async
# ---------------------------------------------------------------------------


def test_has_object_access_granted_true(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": True}))

    result = bundle.sdk.rbac.has_object_access(
        object_type="dashboard", object_id="dash-1", member_id="member-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/HasObjectAccess"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"
    assert body["memberId"] == "member-1"

    assert result.has_access is True


def test_has_object_access_denied_false(make_sdk):
    """Critical access-control assertion: a denied response must unmarshal to
    False, distinguishable from the granted case (guards against an
    always-truthy bug)."""
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": False}))

    result = bundle.sdk.rbac.has_object_access(
        object_type="dashboard", object_id="dash-1", member_id="member-1"
    )

    assert result.has_access is False
    assert result.has_access is not True


@pytest.mark.asyncio
async def test_has_object_access_async_granted_true(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": True}))

    result = await bundle.sdk.rbac.has_object_access_async(
        object_type="dashboard", object_id="dash-1", role_id="role-1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/HasObjectAccess"
    body = bundle.transport.body_json()
    assert body["roleId"] == "role-1"
    assert result.has_access is True


@pytest.mark.asyncio
async def test_has_object_access_async_denied_false(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": False}))

    result = await bundle.sdk.rbac.has_object_access_async(
        object_type="dashboard", object_id="dash-1", group_id="group-1"
    )

    assert result.has_access is False


def test_has_object_access_member_role_group_unset_by_default_omitted(make_sdk):
    """member_id, role_id, group_id are OptionalNullable[str] = UNSET; when
    not passed they must be omitted entirely from the request body."""
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": True}))

    bundle.sdk.rbac.has_object_access(object_type="dashboard", object_id="dash-1")

    body = bundle.transport.body_json()
    assert "memberId" not in body
    assert "roleId" not in body
    assert "groupId" not in body


def test_has_object_access_member_id_explicit_none_serializes_as_null(make_sdk):
    """When explicitly passed as None, member_id (Nullable) must serialize as
    JSON null -- distinct from omission."""
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": True}))

    bundle.sdk.rbac.has_object_access(
        object_type="dashboard", object_id="dash-1", member_id=None
    )

    body = bundle.transport.body_json()
    assert "memberId" in body
    assert body["memberId"] is None


def test_has_object_access_empty_string_object_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": False}))

    bundle.sdk.rbac.has_object_access(object_type="dashboard", object_id="")

    body = bundle.transport.body_json()
    assert "objectId" in body
    assert body["objectId"] == ""


def test_has_object_access_malformed_whitespace_object_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"hasAccess": False}))

    bundle.sdk.rbac.has_object_access(object_type="dashboard", object_id="   ")

    body = bundle.transport.body_json()
    assert body["objectId"] == "   "


def test_has_object_access_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.has_object_access(object_type="dashboard", object_id="dash-1")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_has_object_access_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.has_object_access_async(
            object_type="dashboard", object_id="dash-1"
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# revoke_object_access / revoke_object_access_async
# ---------------------------------------------------------------------------


def test_revoke_object_access_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.revoke_object_access(
        object_type="dashboard", object_id="dash-1", member_id="member-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RevokeObjectAccess"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"
    assert body["memberId"] == "member-1"
    assert result.success is True


@pytest.mark.asyncio
async def test_revoke_object_access_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.revoke_object_access_async(
        object_type="dashboard", object_id="dash-1", role_id="role-1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/RevokeObjectAccess"
    body = bundle.transport.body_json()
    assert body["roleId"] == "role-1"
    assert result.success is True


def test_revoke_object_access_unset_fields_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.revoke_object_access(object_type="dashboard", object_id="dash-1")

    body = bundle.transport.body_json()
    assert "memberId" not in body
    assert "roleId" not in body
    assert "groupId" not in body


def test_revoke_object_access_group_id_explicit_none_is_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.revoke_object_access(
        object_type="dashboard", object_id="dash-1", group_id=None
    )

    body = bundle.transport.body_json()
    assert "groupId" in body
    assert body["groupId"] is None


def test_revoke_object_access_empty_string_object_id_still_sent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.revoke_object_access(object_type="dashboard", object_id="")

    body = bundle.transport.body_json()
    assert body["objectId"] == ""


def test_revoke_object_access_403_forbidden_raises(make_sdk):
    """The single most important test in this file: a forbidden revoke must
    surface as a TextqlDefaultError with status_code 403, not be silently
    swallowed or reported as success."""
    bundle = make_sdk(lambda req: json_response(403, {"message": "not allowed to revoke"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.revoke_object_access(
            object_type="dashboard", object_id="dash-1", member_id="member-1"
        )

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_revoke_object_access_async_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.revoke_object_access_async(
            object_type="dashboard", object_id="dash-1", member_id="member-1"
        )

    assert exc_info.value.status_code == 403


def test_revoke_object_access_404_not_found(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "access record not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.revoke_object_access(
            object_type="dashboard", object_id="does-not-exist", member_id="member-1"
        )

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# generate_share_link / generate_share_link_async
# ---------------------------------------------------------------------------


def test_generate_share_link_sends_correct_request_and_unmarshals(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"shareLink": "https://app.textql.com/share/abc123"}
        )
    )

    result = bundle.sdk.rbac.generate_share_link(
        object_type="dashboard", object_id="dash-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GenerateShareLink"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"

    assert result.share_link == "https://app.textql.com/share/abc123"


@pytest.mark.asyncio
async def test_generate_share_link_async_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"shareLink": "https://app.textql.com/share/xyz"})
    )

    result = await bundle.sdk.rbac.generate_share_link_async(
        object_type="dashboard", object_id="dash-1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GenerateShareLink"
    assert result.share_link == "https://app.textql.com/share/xyz"


def test_generate_share_link_empty_object_id_still_sent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"shareLink": "https://x/y"}))

    bundle.sdk.rbac.generate_share_link(object_type="dashboard", object_id="")

    body = bundle.transport.body_json()
    assert body["objectId"] == ""


def test_generate_share_link_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.generate_share_link(object_type="dashboard", object_id="dash-1")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_generate_share_link_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.generate_share_link_async(
            object_type="dashboard", object_id="dash-1"
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# request_access / request_access_async
# ---------------------------------------------------------------------------


def test_request_access_sends_correct_request_and_unmarshals(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": True, "requestId": "req-1"})
    )

    result = bundle.sdk.rbac.request_access(
        object_type="dashboard",
        object_id="dash-1",
        requested_access_type="editor",
        justification="I need to edit quarterly numbers",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RequestAccess"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"
    assert body["requestedAccessType"] == "editor"
    assert body["justification"] == "I need to edit quarterly numbers"

    assert result.success is True
    assert result.request_id == "req-1"


@pytest.mark.asyncio
async def test_request_access_async_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": True, "requestId": "req-2"})
    )

    result = await bundle.sdk.rbac.request_access_async(
        object_type="dashboard",
        object_id="dash-1",
        requested_access_type="viewer",
        justification="need read access",
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/RequestAccess"
    body = bundle.transport.body_json()
    assert body["requestedAccessType"] == "viewer"
    assert result.request_id == "req-2"


def test_request_access_request_message_unset_omitted(make_sdk):
    """request_message is OptionalNullable[str] = UNSET; when not passed it
    must be omitted entirely."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.request_access(
        object_type="dashboard",
        object_id="dash-1",
        requested_access_type="viewer",
        justification="justification text",
    )

    body = bundle.transport.body_json()
    assert "requestMessage" not in body


def test_request_access_request_message_explicit_value_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.request_access(
        object_type="dashboard",
        object_id="dash-1",
        requested_access_type="viewer",
        justification="justification text",
        request_message="please approve asap",
    )

    body = bundle.transport.body_json()
    assert body["requestMessage"] == "please approve asap"


def test_request_access_request_message_explicit_none_is_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.request_access(
        object_type="dashboard",
        object_id="dash-1",
        requested_access_type="viewer",
        justification="justification text",
        request_message=None,
    )

    body = bundle.transport.body_json()
    assert "requestMessage" in body
    assert body["requestMessage"] is None


def test_request_access_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.request_access(
            object_type="dashboard",
            object_id="dash-1",
            requested_access_type="owner",
            justification="j",
        )

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_request_access_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.request_access_async(
            object_type="dashboard",
            object_id="dash-1",
            requested_access_type="owner",
            justification="j",
        )

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# approve_access_request / approve_access_request_async
# ---------------------------------------------------------------------------


def test_approve_access_request_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.approve_access_request(request_id="req-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ApproveAccessRequest"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["requestId"] == "req-1"
    assert result.success is True


@pytest.mark.asyncio
async def test_approve_access_request_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.approve_access_request_async(request_id="req-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ApproveAccessRequest"
    body = bundle.transport.body_json()
    assert body["requestId"] == "req-2"
    assert result.success is True


def test_approve_access_request_403_forbidden(make_sdk):
    """A non-admin approving an access request should surface 403, not
    silently succeed."""
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.approve_access_request(request_id="req-1")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_approve_access_request_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.approve_access_request_async(request_id="req-1")

    assert exc_info.value.status_code == 403


def test_approve_access_request_404_not_found(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "request not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.approve_access_request(request_id="does-not-exist")

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# reject_access_request / reject_access_request_async
# ---------------------------------------------------------------------------


def test_reject_access_request_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.reject_access_request(
        request_id="req-1", rejection_reason="insufficient justification"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RejectAccessRequest"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["requestId"] == "req-1"
    assert body["rejectionReason"] == "insufficient justification"
    assert result.success is True


@pytest.mark.asyncio
async def test_reject_access_request_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.reject_access_request_async(request_id="req-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/RejectAccessRequest"
    body = bundle.transport.body_json()
    assert body["requestId"] == "req-2"
    assert result.success is True


def test_reject_access_request_rejection_reason_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.reject_access_request(request_id="req-1")

    body = bundle.transport.body_json()
    assert "rejectionReason" not in body


def test_reject_access_request_rejection_reason_explicit_none_is_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.rbac.reject_access_request(request_id="req-1", rejection_reason=None)

    body = bundle.transport.body_json()
    assert "rejectionReason" in body
    assert body["rejectionReason"] is None


def test_reject_access_request_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.reject_access_request(request_id="req-1")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_reject_access_request_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.reject_access_request_async(request_id="req-1")

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# list_access_requests / list_access_requests_async
# ---------------------------------------------------------------------------


def _sample_access_requests():
    return [
        {
            "id": "req-1",
            "objectType": "dashboard",
            "objectId": "dash-1",
            "memberId": "member-1",
            "requestedAccessType": "editor",
            "justification": "need to edit",
            "status": "pending",
        },
        {
            "id": "req-2",
            "objectType": "dataset",
            "objectId": "ds-1",
            "memberId": "member-2",
            "requestedAccessType": "viewer",
            "justification": "need to view",
            "status": "approved",
            "reviewedBy": "admin-1",
        },
        {
            "id": "req-3",
            "objectType": "agent",
            "objectId": "agent-1",
            "memberId": "member-3",
            "requestedAccessType": "owner",
            "justification": "need full control",
            "status": "rejected",
            "reviewedBy": "admin-1",
            "rejectionReason": "not authorized",
        },
    ]


def test_list_access_requests_multi_item_response_unmarshals(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"requests": _sample_access_requests()})
    )

    result = bundle.sdk.rbac.list_access_requests(
        object_type="dashboard", object_id="dash-1", status="pending"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListAccessRequests"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["objectType"] == "dashboard"
    assert body["objectId"] == "dash-1"
    assert body["status"] == "pending"

    assert len(result.requests) == 3
    ids = [r.id for r in result.requests]
    assert ids == ["req-1", "req-2", "req-3"]
    statuses = [r.status for r in result.requests]
    assert statuses == ["pending", "approved", "rejected"]
    assert result.requests[2].rejection_reason == "not authorized"
    assert result.requests[1].reviewed_by == "admin-1"


@pytest.mark.asyncio
async def test_list_access_requests_async_multi_item_response_unmarshals(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"requests": _sample_access_requests()})
    )

    result = await bundle.sdk.rbac.list_access_requests_async()

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListAccessRequests"
    assert len(result.requests) == 3


def test_list_access_requests_all_filters_unset_by_default_omitted(make_sdk):
    """object_type, object_id, status are all OptionalNullable[str] = UNSET;
    calling with no filters should omit all three from the body."""
    bundle = make_sdk(lambda req: json_response(200, {"requests": []}))

    bundle.sdk.rbac.list_access_requests()

    body = bundle.transport.body_json()
    assert "objectType" not in body
    assert "objectId" not in body
    assert "status" not in body


def test_list_access_requests_status_explicit_none_is_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"requests": []}))

    bundle.sdk.rbac.list_access_requests(status=None)

    body = bundle.transport.body_json()
    assert "status" in body
    assert body["status"] is None


def test_list_access_requests_empty_list_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"requests": []}))

    result = bundle.sdk.rbac.list_access_requests(status="pending")

    assert result.requests == []


def test_list_access_requests_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_access_requests()

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_list_access_requests_async_403_forbidden(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.list_access_requests_async()

    assert exc_info.value.status_code == 403


def test_list_access_requests_401_unauthorized(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_access_requests()

    assert exc_info.value.status_code == 401
