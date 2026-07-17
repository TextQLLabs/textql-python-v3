"""Unit tests for Rbac API key and service account operations."""
from __future__ import annotations

import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors

PATH_PREFIX = "/textql.rpc.public.rbac.RBACService"


# ---------------------------------------------------------------------------
# CreateApiKey
# ---------------------------------------------------------------------------


def test_create_api_key_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "apiKey": {"id": "key-1", "memberId": "m1", "status": "API_KEY_STATUS_ACTIVE"},
                "apiKeyHash": "hashed-secret-value",
            },
        )
    )

    result = bundle.sdk.rbac.create_api_key(
        name="ci-key",
        assumed_roles=["role-1", "role-2"],
        expiry_seconds=3600,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/CreateApiKey"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "ci-key"
    assert body["assumedRoles"] == ["role-1", "role-2"]
    assert body["expirySeconds"] == 3600

    # The secret/hash returned by the server round-trips through unmarshaling.
    assert result.api_key_hash == "hashed-secret-value"
    assert result.api_key.id == "key-1"
    assert result.api_key.status == "API_KEY_STATUS_ACTIVE"


async def test_create_api_key_async_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"apiKey": {"id": "key-2"}, "apiKeyHash": "another-secret"},
        )
    )

    result = await bundle.sdk.rbac.create_api_key_async(
        name="ci-key-async",
        assumed_roles=["role-3"],
        expiry_seconds=7200,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/CreateApiKey"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "ci-key-async"
    assert body["assumedRoles"] == ["role-3"]
    assert body["expirySeconds"] == 7200

    assert result.api_key_hash == "another-secret"
    assert result.api_key.id == "key-2"


def test_create_api_key_no_server_generated_field_leaks_when_not_passed(make_sdk):
    """SECURITY: create_api_key's real kwargs are connect_timeout_ms,
    expiry_seconds, assumed_roles, inherit_all_roles, name, target_member_id,
    client_id, suppress_superadmin (see rbac.py create_api_key signature).
    None of these are server-generated identifiers/secrets. But the *response*
    model TextqlRPCPublicRbacAPIKey has an "id" field, and the request must
    never contain server-assigned identifiers like "id"/"apiKeyId"/"key" that
    the caller did not explicitly supply -- that would be a sign the SDK is
    letting a client dictate what should be a server-issued key ID/secret."""
    bundle = make_sdk(lambda req: json_response(200, {"apiKey": {"id": "srv-assigned"}, "apiKeyHash": "secret"}))

    bundle.sdk.rbac.create_api_key(name="minimal-key")

    body = bundle.transport.body_json()
    for forbidden in ("id", "apiKeyId", "api_key_id", "key", "secret", "apiKeyHash", "api_key_hash"):
        assert forbidden not in body, f"unexpected server-generated-looking field {forbidden!r} in request body: {body}"
    # Only the field we actually set (plus nothing else) should be present.
    assert body == {"name": "minimal-key"}


def test_create_api_key_optional_nullable_unset_omits_fields(make_sdk):
    """expiry_seconds, inherit_all_roles, name, target_member_id, client_id
    are all OptionalNullable[...] = UNSET by default; leaving them unset must
    omit them entirely from the serialized body."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_api_key()

    body = bundle.transport.body_json()
    assert "expirySeconds" not in body
    assert "inheritAllRoles" not in body
    assert "name" not in body
    assert "targetMemberId" not in body
    assert "clientId" not in body
    # assumed_roles / suppress_superadmin are plain Optional (non-nullable);
    # also omitted when not passed.
    assert "assumedRoles" not in body
    assert "suppressSuperadmin" not in body


def test_create_api_key_optional_nullable_explicit_none_serializes_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_api_key(
        expiry_seconds=None,
        inherit_all_roles=None,
        name=None,
        target_member_id=None,
        client_id=None,
    )

    body = bundle.transport.body_json()
    assert body["expirySeconds"] is None
    assert body["inheritAllRoles"] is None
    assert body["name"] is None
    assert body["targetMemberId"] is None
    assert body["clientId"] is None


def test_create_api_key_optional_nullable_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_api_key(
        expiry_seconds=86400,
        inherit_all_roles=True,
        name="named-key",
        target_member_id="member-42",
        client_id="client-abc",
        suppress_superadmin=True,
    )

    body = bundle.transport.body_json()
    assert body["expirySeconds"] == 86400
    assert body["inheritAllRoles"] is True
    assert body["name"] == "named-key"
    assert body["targetMemberId"] == "member-42"
    assert body["clientId"] == "client-abc"
    assert body["suppressSuperadmin"] is True


def test_create_api_key_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden: missing organization:write"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.create_api_key(name="x", target_member_id="someone-elses-service-account")

    assert exc_info.value.status_code == 403
    assert "forbidden" in str(exc_info.value)


async def test_create_api_key_async_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.create_api_key_async(name="x")

    assert exc_info.value.status_code == 403


def test_create_api_key_401_unauthorized_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "invalid credentials"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.create_api_key(name="x")

    assert exc_info.value.status_code == 401


# ---------------------------------------------------------------------------
# RotateApiKey
# ---------------------------------------------------------------------------


def test_rotate_api_key_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "apiKey": {"id": "key-new", "status": "API_KEY_STATUS_ACTIVE"},
                "apiKeyHash": "rotated-secret-value",
                "revokedApiKeyId": "key-old",
            },
        )
    )

    result = bundle.sdk.rbac.rotate_api_key(api_key_id="key-old")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/RotateApiKey"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"apiKeyId": "key-old"}

    # The newly-minted secret round-trips as given in the mock response.
    assert result.api_key_hash == "rotated-secret-value"
    assert result.api_key.id == "key-new"
    assert result.revoked_api_key_id == "key-old"


async def test_rotate_api_key_async_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"apiKey": {"id": "key-new-2"}, "apiKeyHash": "rotated-secret-2", "revokedApiKeyId": "key-old-2"},
        )
    )

    result = await bundle.sdk.rbac.rotate_api_key_async(api_key_id="key-old-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/RotateApiKey"
    body = bundle.transport.body_json()
    assert body == {"apiKeyId": "key-old-2"}

    assert result.api_key_hash == "rotated-secret-2"
    assert result.revoked_api_key_id == "key-old-2"


def test_rotate_api_key_no_server_generated_field_leaks_when_not_passed(make_sdk):
    """SECURITY: rotate_api_key's only real kwarg (besides cross-cutting
    connect_timeout_ms/retries/etc) is api_key_id (see
    TextqlRPCPublicRbacRotateAPIKeyRequest -- the request body has exactly one
    field, apiKeyId). The response contains freshly minted apiKey/apiKeyHash/
    revokedApiKeyId; none of that should ever appear in the *request* body."""
    bundle = make_sdk(
        lambda req: json_response(200, {"apiKey": {"id": "x"}, "apiKeyHash": "h", "revokedApiKeyId": "old"})
    )

    bundle.sdk.rbac.rotate_api_key(api_key_id="key-123")

    body = bundle.transport.body_json()
    assert body == {"apiKeyId": "key-123"}
    for forbidden in ("id", "key", "secret", "apiKeyHash", "api_key_hash", "revokedApiKeyId", "apiKey"):
        assert forbidden not in body, f"unexpected server-generated-looking field {forbidden!r} in request body: {body}"


def test_rotate_api_key_empty_string_id_sends_well_formed_request(make_sdk):
    """Edge case: an empty-string api_key_id must still be sent through
    verbatim (not silently dropped/coerced to None/omitted), since apiKeyId
    is a plain Optional[str] field (not OptionalNullable) -- see
    textql_rpc_public_rbac_rotateapikeyrequest.py. If the SDK dropped it, a
    caller passing a blank/invalid id would get a confusing "field missing"
    server error instead of a clear "invalid id" error."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.rotate_api_key(api_key_id="")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/RotateApiKey"
    body = bundle.transport.body_json()
    assert body["apiKeyId"] == ""


def test_rotate_api_key_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.rotate_api_key(api_key_id="key-1")

    assert exc_info.value.status_code == 403


async def test_rotate_api_key_async_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.rotate_api_key_async(api_key_id="key-1")

    assert exc_info.value.status_code == 403


def test_rotate_api_key_409_conflict_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "api key already rotated"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.rotate_api_key(api_key_id="key-1")

    assert exc_info.value.status_code == 409


# ---------------------------------------------------------------------------
# RevokeApiKey
# ---------------------------------------------------------------------------


def test_revoke_api_key_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.revoke_api_key(api_key_id="key-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/RevokeApiKey"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"apiKeyId": "key-1"}
    assert result.success is True


async def test_revoke_api_key_async_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.revoke_api_key_async(api_key_id="key-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/RevokeApiKey"
    body = bundle.transport.body_json()
    assert body == {"apiKeyId": "key-2"}
    assert result.success is True


def test_revoke_api_key_empty_string_id_sends_well_formed_request(make_sdk):
    """Edge case: an empty/clearly-invalid api_key_id must be sent verbatim,
    not silently dropped -- see rotate_api_key equivalent test above for the
    same reasoning."""
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = bundle.sdk.rbac.revoke_api_key(api_key_id="")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/RevokeApiKey"
    body = bundle.transport.body_json()
    assert body["apiKeyId"] == ""
    assert result.success is False


def test_revoke_api_key_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.revoke_api_key(api_key_id="key-1")

    assert exc_info.value.status_code == 403


async def test_revoke_api_key_async_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.revoke_api_key_async(api_key_id="key-1")

    assert exc_info.value.status_code == 403


def test_revoke_api_key_404_not_found_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "api key not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.revoke_api_key(api_key_id="does-not-exist")

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# ListApiKeys
# ---------------------------------------------------------------------------


def test_list_api_keys_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "apiKeys": [
                    {"id": "k1", "name": "active-key", "status": "API_KEY_STATUS_ACTIVE"},
                    {"id": "k2", "name": "revoked-key", "status": "API_KEY_STATUS_REVOKED"},
                    {"id": "k3", "name": "expired-key", "status": "API_KEY_STATUS_EXPIRED"},
                ],
                "nextPageToken": "next-page",
            },
        )
    )

    result = bundle.sdk.rbac.list_api_keys(
        scope="API_KEY_SCOPE_SERVICE_ACCOUNTS",
        service_account_member_id="sa-1",
        include_revoked=True,
        search_term="ci",
        sort_by="API_KEY_SORT_FIELD_CREATED_AT",
        sort_direction="SORT_DIRECTION_DESC",
        page_size=25,
        page_token="cursor-1",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListApiKeys"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["scope"] == "API_KEY_SCOPE_SERVICE_ACCOUNTS"
    assert body["serviceAccountMemberId"] == "sa-1"
    assert body["includeRevoked"] is True
    assert body["searchTerm"] == "ci"
    assert body["sortBy"] == "API_KEY_SORT_FIELD_CREATED_AT"
    assert body["sortDirection"] == "SORT_DIRECTION_DESC"
    assert body["pageSize"] == 25
    assert body["pageToken"] == "cursor-1"

    assert len(result.api_keys) == 3
    statuses = {k.id: k.status for k in result.api_keys}
    assert statuses["k1"] == "API_KEY_STATUS_ACTIVE"
    assert statuses["k2"] == "API_KEY_STATUS_REVOKED"
    assert statuses["k3"] == "API_KEY_STATUS_EXPIRED"
    assert result.next_page_token == "next-page"


async def test_list_api_keys_async_multi_item_enum_roundtrip(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "apiKeys": [
                    {"id": "a1", "status": "API_KEY_STATUS_ACTIVE"},
                    {"id": "a2", "status": "API_KEY_STATUS_REVOKED"},
                ],
                "nextPageToken": None,
            },
        )
    )

    result = await bundle.sdk.rbac.list_api_keys_async(include_revoked=True)

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/ListApiKeys"
    body = bundle.transport.body_json()
    assert body["includeRevoked"] is True

    assert len(result.api_keys) == 2
    assert result.api_keys[0].status == "API_KEY_STATUS_ACTIVE"
    assert result.api_keys[1].status == "API_KEY_STATUS_REVOKED"
    assert result.next_page_token is None


def test_list_api_keys_optional_nullable_unset_omits_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.list_api_keys()

    body = bundle.transport.body_json()
    assert "serviceAccountMemberId" not in body
    assert "includeRevoked" not in body
    assert "searchTerm" not in body
    assert "pageSize" not in body
    assert "pageToken" not in body
    assert "scope" not in body
    assert "sortBy" not in body
    assert "sortDirection" not in body


def test_list_api_keys_optional_nullable_explicit_none(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.list_api_keys(
        service_account_member_id=None,
        include_revoked=None,
        search_term=None,
        page_size=None,
        page_token=None,
    )

    body = bundle.transport.body_json()
    assert body["serviceAccountMemberId"] is None
    assert body["includeRevoked"] is None
    assert body["searchTerm"] is None
    assert body["pageSize"] is None
    assert body["pageToken"] is None


def test_list_api_keys_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_api_keys()

    assert exc_info.value.status_code == 403


async def test_list_api_keys_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.list_api_keys_async()

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# CreateServiceAccount
# ---------------------------------------------------------------------------


def test_create_service_account_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"memberId": "sa-member-1", "email": "sa-1@service.textql.com"})
    )

    result = bundle.sdk.rbac.create_service_account(
        name="ci-bot",
        description="used by CI",
        owner_member_id="owner-1",
        role_ids=["role-a", "role-b"],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/CreateServiceAccount"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "ci-bot"
    assert body["description"] == "used by CI"
    assert body["ownerMemberId"] == "owner-1"
    assert body["roleIds"] == ["role-a", "role-b"]

    assert result.member_id == "sa-member-1"
    assert result.email == "sa-1@service.textql.com"


async def test_create_service_account_async_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"memberId": "sa-member-2", "email": "sa-2@service.textql.com"})
    )

    result = await bundle.sdk.rbac.create_service_account_async(name="ci-bot-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/CreateServiceAccount"
    body = bundle.transport.body_json()
    assert body["name"] == "ci-bot-2"

    assert result.member_id == "sa-member-2"
    assert result.email == "sa-2@service.textql.com"


def test_create_service_account_no_server_generated_field_leaks_when_not_passed(make_sdk):
    """SECURITY: create_service_account's real kwargs are connect_timeout_ms,
    name, description, owner_member_id, role_ids (see rbac.py
    create_service_account signature / TextqlRPCPublicRbacCreateServiceAccountRequest).
    The *response* carries a server-assigned memberId/email
    (TextqlRPCPublicRbacCreateServiceAccountResponse); neither of those field
    names -- nor any other server-generated-looking identifier -- must appear
    in the outgoing request body unless the caller passed them (they are not
    even valid request kwargs here, so they should never appear)."""
    bundle = make_sdk(lambda req: json_response(200, {"memberId": "srv-assigned", "email": "x@y.com"}))

    bundle.sdk.rbac.create_service_account(name="minimal-sa")

    body = bundle.transport.body_json()
    for forbidden in ("memberId", "member_id", "id", "service_account_id", "serviceAccountId", "email"):
        assert forbidden not in body, f"unexpected server-generated-looking field {forbidden!r} in request body: {body}"
    assert body == {"name": "minimal-sa"}


def test_create_service_account_optional_nullable_unset_omits_fields(make_sdk):
    """description and owner_member_id are OptionalNullable[str] = UNSET;
    name is a plain Optional[str]; role_ids is a plain Optional[List[str]].
    None of these should appear when not passed."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_service_account()

    body = bundle.transport.body_json()
    assert "description" not in body
    assert "ownerMemberId" not in body
    assert "name" not in body
    assert "roleIds" not in body


def test_create_service_account_optional_nullable_explicit_none(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_service_account(description=None, owner_member_id=None)

    body = bundle.transport.body_json()
    assert body["description"] is None
    assert body["ownerMemberId"] is None


def test_create_service_account_optional_nullable_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.create_service_account(description="a real description", owner_member_id="owner-99")

    body = bundle.transport.body_json()
    assert body["description"] == "a real description"
    assert body["ownerMemberId"] == "owner-99"


def test_create_service_account_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden: missing organization:write"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.create_service_account(name="attacker-bot")

    assert exc_info.value.status_code == 403
    assert "forbidden" in str(exc_info.value)


async def test_create_service_account_async_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.create_service_account_async(name="x")

    assert exc_info.value.status_code == 403


def test_create_service_account_409_conflict_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "service account name already exists"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.create_service_account(name="duplicate-bot")

    assert exc_info.value.status_code == 409


# ---------------------------------------------------------------------------
# DeleteServiceAccount
# ---------------------------------------------------------------------------


def test_delete_service_account_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.rbac.delete_service_account(member_id="sa-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/DeleteServiceAccount"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"memberId": "sa-1"}
    assert result.success is True


async def test_delete_service_account_async_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.rbac.delete_service_account_async(member_id="sa-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/DeleteServiceAccount"
    body = bundle.transport.body_json()
    assert body == {"memberId": "sa-2"}
    assert result.success is True


def test_delete_service_account_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.delete_service_account(member_id="sa-1")

    assert exc_info.value.status_code == 403


async def test_delete_service_account_async_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.delete_service_account_async(member_id="sa-1")

    assert exc_info.value.status_code == 403


def test_delete_service_account_404_not_found_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "service account not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.delete_service_account(member_id="does-not-exist")

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# ListServiceAccounts
# ---------------------------------------------------------------------------


def test_list_service_accounts_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "serviceAccounts": [
                    {"memberId": "sa-1", "email": "sa1@service.textql.com", "displayName": "CI Bot"},
                    {"memberId": "sa-2", "email": "sa2@service.textql.com", "displayName": "Embed Bot"},
                    {"memberId": "sa-3", "email": "sa3@service.textql.com", "displayName": "Ops Bot"},
                ],
                "nextPageToken": "next-cursor",
            },
        )
    )

    result = bundle.sdk.rbac.list_service_accounts(search_term="bot", page_size=10, page_token="cursor-0")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListServiceAccounts"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["searchTerm"] == "bot"
    assert body["pageSize"] == 10
    assert body["pageToken"] == "cursor-0"

    assert len(result.service_accounts) == 3
    member_ids = [sa.member_id for sa in result.service_accounts]
    assert member_ids == ["sa-1", "sa-2", "sa-3"]
    assert result.service_accounts[0].display_name == "CI Bot"
    assert result.next_page_token == "next-cursor"


async def test_list_service_accounts_async_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"serviceAccounts": [{"memberId": "sa-4", "email": "sa4@service.textql.com"}], "nextPageToken": None},
        )
    )

    result = await bundle.sdk.rbac.list_service_accounts_async()

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/ListServiceAccounts"
    assert len(result.service_accounts) == 1
    assert result.service_accounts[0].member_id == "sa-4"
    assert result.next_page_token is None


def test_list_service_accounts_optional_nullable_unset_omits_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.list_service_accounts()

    body = bundle.transport.body_json()
    assert "searchTerm" not in body
    assert "pageSize" not in body
    assert "pageToken" not in body


def test_list_service_accounts_optional_nullable_explicit_none(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.rbac.list_service_accounts(search_term=None, page_size=None, page_token=None)

    body = bundle.transport.body_json()
    assert body["searchTerm"] is None
    assert body["pageSize"] is None
    assert body["pageToken"] is None


def test_list_service_accounts_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.list_service_accounts()

    assert exc_info.value.status_code == 403


async def test_list_service_accounts_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.list_service_accounts_async()

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# GetEmbedUserApiKey
# ---------------------------------------------------------------------------


def test_get_embed_user_api_key_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "apiKeyBase64": "ZW1iZWQtc2VjcmV0LWJhc2U2NA==",
                "apiKeyShort": "sk_abcd1234",
                "serviceAccountEmail": "embed-user@service.textql.com",
            },
        )
    )

    result = bundle.sdk.rbac.get_embed_user_api_key(member_id="embed-user-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/GetEmbedUserApiKey"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"memberId": "embed-user-1"}

    # The embed secret round-trips as given in the mock response.
    assert result.api_key_base64 == "ZW1iZWQtc2VjcmV0LWJhc2U2NA=="
    assert result.api_key_short == "sk_abcd1234"
    assert result.service_account_email == "embed-user@service.textql.com"


async def test_get_embed_user_api_key_async_builds_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "apiKeyBase64": "YXN5bmMtc2VjcmV0",
                "apiKeyShort": "sk_efgh5678",
                "serviceAccountEmail": "embed-user-2@service.textql.com",
            },
        )
    )

    result = await bundle.sdk.rbac.get_embed_user_api_key_async(member_id="embed-user-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/GetEmbedUserApiKey"
    body = bundle.transport.body_json()
    assert body == {"memberId": "embed-user-2"}

    assert result.api_key_base64 == "YXN5bmMtc2VjcmV0"
    assert result.service_account_email == "embed-user-2@service.textql.com"


def test_get_embed_user_api_key_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_embed_user_api_key(member_id="embed-user-1")

    assert exc_info.value.status_code == 403


async def test_get_embed_user_api_key_async_403_forbidden_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.rbac.get_embed_user_api_key_async(member_id="embed-user-1")

    assert exc_info.value.status_code == 403


def test_get_embed_user_api_key_401_unauthorized_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.rbac.get_embed_user_api_key(member_id="embed-user-1")

    assert exc_info.value.status_code == 401
