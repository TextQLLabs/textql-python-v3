"""Unit tests for Libraries owners/permissions operations: effective owners, approval rules, auto-approve rules."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors

BASE_PATH = "/textql.rpc.public.patches.LibraryService"


# ---------------------------------------------------------------------------
# get_effective_owners / get_effective_owners_async
# ---------------------------------------------------------------------------


def test_get_effective_owners_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "path": "src/lib",
                "entries": [
                    {"roleId": "role-1", "permission": "LIBRARY_PERMISSION_READ_WRITE"}
                ],
            },
        )
    )

    result = bundle.sdk.libraries.get_effective_owners(path="src/lib")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetEffectiveLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib"}

    assert result.path == "src/lib"
    assert result.entries[0].role_id == "role-1"
    assert result.entries[0].permission == "LIBRARY_PERMISSION_READ_WRITE"


@pytest.mark.asyncio
async def test_get_effective_owners_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"path": "src/lib-async", "entries": []})
    )

    result = await bundle.sdk.libraries.get_effective_owners_async(path="src/lib-async")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetEffectiveLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib-async"}
    assert result.path == "src/lib-async"


# ---------------------------------------------------------------------------
# get_library_owners / get_library_owners_async
# ---------------------------------------------------------------------------


def test_get_library_owners_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "owners": {
                    "path": "src/lib",
                    "entries": [
                        {
                            "roleId": "role-2",
                            "permission": "LIBRARY_PERMISSION_READ",
                        }
                    ],
                    "canWrite": True,
                    "updatedAt": "2026-01-01T00:00:00Z",
                }
            },
        )
    )

    result = bundle.sdk.libraries.get_library_owners(path="src/lib")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib"}

    assert result.owners.path == "src/lib"
    assert result.owners.can_write is True
    assert result.owners.entries[0].role_id == "role-2"


@pytest.mark.asyncio
async def test_get_library_owners_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"owners": {"path": "src/lib-async"}})
    )

    result = await bundle.sdk.libraries.get_library_owners_async(path="src/lib-async")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib-async"}
    assert result.owners.path == "src/lib-async"


def test_get_library_owners_omits_path_when_not_passed(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_library_owners()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# upsert_owners / upsert_owners_async  (deep-dive operation)
# ---------------------------------------------------------------------------


def test_upsert_owners_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "owners": {
                    "path": "src/lib",
                    "entries": [
                        {"roleId": "role-1", "permission": "LIBRARY_PERMISSION_READ_WRITE"}
                    ],
                }
            },
        )
    )

    result = bundle.sdk.libraries.upsert_owners(
        path="src/lib",
        role_ids=["role-1", "role-2"],
        permissions=["LIBRARY_PERMISSION_READ_WRITE", "LIBRARY_PERMISSION_READ"],
        commit_message="grant owners",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpsertLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "src/lib",
        "roleIds": ["role-1", "role-2"],
        "permissions": ["LIBRARY_PERMISSION_READ_WRITE", "LIBRARY_PERMISSION_READ"],
        "commitMessage": "grant owners",
    }

    assert result.owners.path == "src/lib"
    assert result.owners.entries[0].role_id == "role-1"


@pytest.mark.asyncio
async def test_upsert_owners_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"owners": {"path": "src/lib"}}))

    result = await bundle.sdk.libraries.upsert_owners_async(
        path="src/lib",
        role_ids=["role-1"],
        permissions=["LIBRARY_PERMISSION_READ"],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpsertLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "src/lib",
        "roleIds": ["role-1"],
        "permissions": ["LIBRARY_PERMISSION_READ"],
    }
    assert result.owners.path == "src/lib"


def test_upsert_owners_omits_unset_fields(make_sdk):
    # path/roleIds/permissions are plain Optional and omitted-if-None;
    # commitMessage is OptionalNullable[str] (UNSET default) and is also
    # omitted when not explicitly passed.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_owners()

    body = bundle.transport.body_json()
    assert body == {}


def test_upsert_owners_commit_message_explicit_none_serializes_as_null(make_sdk):
    # commit_message is OptionalNullable[str]; passing None explicitly (as a
    # real kwarg value, not leaving it at the UNSET default) should mark the
    # pydantic field as "set" and serialize to JSON null rather than being
    # omitted.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_owners(path="src/lib", commit_message=None)

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib", "commitMessage": None}


def test_upsert_owners_empty_list_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_owners(path="src/lib", role_ids=[], permissions=[])

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib", "roleIds": [], "permissions": []}


def test_upsert_owners_unicode_path(make_sdk):
    tricky_path = "库/目录 with spaces/emoji😀"
    bundle = make_sdk(lambda req: json_response(200, {"owners": {"path": tricky_path}}))

    result = bundle.sdk.libraries.upsert_owners(
        path=tricky_path, role_ids=["ro^le-é"], commit_message="备注"
    )

    body = bundle.transport.body_json()
    assert body == {
        "path": tricky_path,
        "roleIds": ["ro^le-é"],
        "commitMessage": "备注",
    }
    assert result.owners.path == tricky_path


def test_upsert_owners_error_status_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.upsert_owners(path="src/lib", role_ids=["role-1"])

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_upsert_owners_async_error_status_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.upsert_owners_async(path="src/lib")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# delete_owners / delete_owners_async  (deep-dive operation)
# ---------------------------------------------------------------------------


def test_delete_owners_sync_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.libraries.delete_owners(
        path="src/lib", role_ids=["role-1"], commit_message="remove owner"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "src/lib",
        "roleIds": ["role-1"],
        "commitMessage": "remove owner",
    }

    # GoogleProtobufEmpty has no fields; unmarshaling {} must not raise.
    assert result is not None


@pytest.mark.asyncio
async def test_delete_owners_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.libraries.delete_owners_async(
        path="src/lib", role_ids=["role-1", "role-2"]
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteLibraryOwners"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib", "roleIds": ["role-1", "role-2"]}
    assert result is not None


def test_delete_owners_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.delete_owners()

    body = bundle.transport.body_json()
    assert body == {}


def test_delete_owners_commit_message_explicit_none_serializes_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.delete_owners(path="src/lib", commit_message=None)

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib", "commitMessage": None}


def test_delete_owners_empty_role_ids_list(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.delete_owners(path="src/lib", role_ids=[])

    body = bundle.transport.body_json()
    assert body == {"path": "src/lib", "roleIds": []}


def test_delete_owners_error_status_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.delete_owners(path="src/missing")

    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_owners_async_error_status_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.delete_owners_async(path="src/lib")

    assert exc_info.value.status_code == 409


# ---------------------------------------------------------------------------
# get_codeowner_coverage / get_codeowner_coverage_async
# ---------------------------------------------------------------------------


def test_get_codeowner_coverage_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "totalFiles": 100,
                "coveredFiles": 80,
                "coveragePct": 80.0,
                "uncoveredFiles": ["a.txt", "b.txt"],
            },
        )
    )

    result = bundle.sdk.libraries.get_codeowner_coverage(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetCodeownerCoverage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}

    assert result.total_files == 100
    assert result.covered_files == 80
    assert result.coverage_pct == 80.0
    assert result.uncovered_files == ["a.txt", "b.txt"]


@pytest.mark.asyncio
async def test_get_codeowner_coverage_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalFiles": 5}))

    result = await bundle.sdk.libraries.get_codeowner_coverage_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetCodeownerCoverage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.total_files == 5


# ---------------------------------------------------------------------------
# create_approval_rule / create_approval_rule_async  (deep-dive operation)
# ---------------------------------------------------------------------------


def test_create_approval_rule_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "rule": {
                    "id": "rule-1",
                    "directoryPath": "src/lib",
                    "requiredApprovals": 2,
                    "roleIds": ["role-1"],
                    "enabled": True,
                    "createdAt": "2026-01-01T00:00:00Z",
                    "updatedAt": "2026-01-01T00:00:00Z",
                }
            },
        )
    )

    result = bundle.sdk.libraries.create_approval_rule(
        rule={
            "directory_path": "src/lib",
            "required_approvals": 2,
            "role_ids": ["role-1"],
            "enabled": True,
        }
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateApprovalRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "rule": {
            "directoryPath": "src/lib",
            "requiredApprovals": 2,
            "roleIds": ["role-1"],
            "enabled": True,
        }
    }

    assert result.rule.id == "rule-1"
    assert result.rule.required_approvals == 2
    assert result.rule.enabled is True


@pytest.mark.asyncio
async def test_create_approval_rule_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"rule": {"id": "rule-async", "enabled": False}})
    )

    result = await bundle.sdk.libraries.create_approval_rule_async(
        rule={"directory_path": "src/lib", "required_approvals": 1}
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateApprovalRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"rule": {"directoryPath": "src/lib", "requiredApprovals": 1}}
    assert result.rule.id == "rule-async"


def test_create_approval_rule_omits_rule_when_not_passed(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.create_approval_rule()

    body = bundle.transport.body_json()
    assert body == {}


def test_create_approval_rule_enabled_unset_vs_explicit_none(make_sdk):
    # `enabled` on ApprovalRuleInput is OptionalNullable[bool]: omitted when
    # left at the UNSET default, present as JSON null when explicitly passed
    # as None.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.create_approval_rule(rule={"directory_path": "src/lib"})
    body_unset = bundle.transport.body_json()
    assert body_unset == {"rule": {"directoryPath": "src/lib"}}
    assert "enabled" not in body_unset["rule"]

    bundle.sdk.libraries.create_approval_rule(
        rule={"directory_path": "src/lib", "enabled": None}
    )
    body_explicit_none = bundle.transport.body_json()
    assert body_explicit_none == {
        "rule": {"directoryPath": "src/lib", "enabled": None}
    }


def test_create_approval_rule_unicode_directory_path(make_sdk):
    tricky_path = "库/规则 path*/emoji🚀"
    bundle = make_sdk(
        lambda req: json_response(200, {"rule": {"directoryPath": tricky_path}})
    )

    result = bundle.sdk.libraries.create_approval_rule(
        rule={"directory_path": tricky_path, "role_ids": []}
    )

    body = bundle.transport.body_json()
    assert body == {"rule": {"directoryPath": tricky_path, "roleIds": []}}
    assert result.rule.directory_path == tricky_path


def test_create_approval_rule_error_status_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid rule"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.create_approval_rule(rule={"directory_path": "src/lib"})

    assert exc_info.value.status_code == 422


@pytest.mark.asyncio
async def test_create_approval_rule_async_error_status_raises_textql_default_error(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.create_approval_rule_async()

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# update_approval_rule / update_approval_rule_async
# ---------------------------------------------------------------------------


def test_update_approval_rule_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"rule": {"id": "rule-1", "requiredApprovals": 3}}
        )
    )

    result = bundle.sdk.libraries.update_approval_rule(
        id="rule-1",
        rule={"required_approvals": 3},
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpdateApprovalRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "rule-1", "rule": {"requiredApprovals": 3}}

    assert result.rule.id == "rule-1"
    assert result.rule.required_approvals == 3


@pytest.mark.asyncio
async def test_update_approval_rule_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"rule": {"id": "rule-2"}}))

    result = await bundle.sdk.libraries.update_approval_rule_async(
        id="rule-2", rule={"enabled": False}
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpdateApprovalRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "rule-2", "rule": {"enabled": False}}
    assert result.rule.id == "rule-2"


def test_update_approval_rule_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.update_approval_rule()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# delete_approval_rule / delete_approval_rule_async
# ---------------------------------------------------------------------------


def test_delete_approval_rule_sync_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.libraries.delete_approval_rule(id="rule-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteApprovalRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "rule-1"}
    assert result is not None


@pytest.mark.asyncio
async def test_delete_approval_rule_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.libraries.delete_approval_rule_async(id="rule-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteApprovalRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "rule-2"}
    assert result is not None


def test_delete_approval_rule_error_status_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.delete_approval_rule(id="missing-rule")

    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_approval_rule_async_error_status_raises_textql_default_error(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.delete_approval_rule_async(id="rule-x")

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# list_approval_rules / list_approval_rules_async
# ---------------------------------------------------------------------------


def test_list_approval_rules_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "rules": [
                    {"id": "rule-1", "directoryPath": "src"},
                    {"id": "rule-2", "directoryPath": "docs"},
                ]
            },
        )
    )

    result = bundle.sdk.libraries.list_approval_rules(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListApprovalRules"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}

    assert len(result.rules) == 2
    assert result.rules[0].id == "rule-1"
    assert result.rules[1].directory_path == "docs"


@pytest.mark.asyncio
async def test_list_approval_rules_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"rules": []}))

    result = await bundle.sdk.libraries.list_approval_rules_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListApprovalRules"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.rules == []


# ---------------------------------------------------------------------------
# create_context_patch_auto_approve_rule / create_context_patch_auto_approve_rule_async
# (deep-dive operation)
# ---------------------------------------------------------------------------


def test_create_context_patch_auto_approve_rule_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "rule": {
                    "id": "capa-1",
                    "directoryPath": "src/lib",
                    "alwaysAutoApprove": True,
                    "roleIds": ["role-1"],
                    "agentIds": ["agent-1"],
                    "enabled": True,
                }
            },
        )
    )

    result = bundle.sdk.libraries.create_context_patch_auto_approve_rule(
        rule={
            "directory_path": "src/lib",
            "always_auto_approve": True,
            "role_ids": ["role-1"],
            "agent_ids": ["agent-1"],
            "enabled": True,
        }
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateContextPatchAutoApproveRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "rule": {
            "directoryPath": "src/lib",
            "alwaysAutoApprove": True,
            "roleIds": ["role-1"],
            "agentIds": ["agent-1"],
            "enabled": True,
        }
    }

    assert result.rule.id == "capa-1"
    assert result.rule.always_auto_approve is True
    assert result.rule.agent_ids == ["agent-1"]


@pytest.mark.asyncio
async def test_create_context_patch_auto_approve_rule_async_request_and_response(
    make_sdk,
):
    bundle = make_sdk(
        lambda req: json_response(200, {"rule": {"id": "capa-async"}})
    )

    result = await bundle.sdk.libraries.create_context_patch_auto_approve_rule_async(
        rule={"directory_path": "src/lib", "always_auto_approve": False}
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateContextPatchAutoApproveRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "rule": {"directoryPath": "src/lib", "alwaysAutoApprove": False}
    }
    assert result.rule.id == "capa-async"


def test_create_context_patch_auto_approve_rule_omits_rule_when_not_passed(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.create_context_patch_auto_approve_rule()

    body = bundle.transport.body_json()
    assert body == {}


def test_create_context_patch_auto_approve_rule_enabled_unset_vs_explicit_none(
    make_sdk,
):
    # `enabled` on ContextPatchAutoApproveRuleInput is OptionalNullable[bool]:
    # omitted when left at the UNSET default, present as JSON null when
    # explicitly passed as None.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.create_context_patch_auto_approve_rule(
        rule={"directory_path": "src/lib"}
    )
    body_unset = bundle.transport.body_json()
    assert body_unset == {"rule": {"directoryPath": "src/lib"}}
    assert "enabled" not in body_unset["rule"]

    bundle.sdk.libraries.create_context_patch_auto_approve_rule(
        rule={"directory_path": "src/lib", "enabled": None}
    )
    body_explicit_none = bundle.transport.body_json()
    assert body_explicit_none == {
        "rule": {"directoryPath": "src/lib", "enabled": None}
    }


def test_create_context_patch_auto_approve_rule_empty_lists_and_unicode(make_sdk):
    tricky_path = "库/patches 路径*/emoji🎉"
    bundle = make_sdk(
        lambda req: json_response(200, {"rule": {"directoryPath": tricky_path}})
    )

    result = bundle.sdk.libraries.create_context_patch_auto_approve_rule(
        rule={
            "directory_path": tricky_path,
            "role_ids": [],
            "agent_ids": [],
        }
    )

    body = bundle.transport.body_json()
    assert body == {
        "rule": {
            "directoryPath": tricky_path,
            "roleIds": [],
            "agentIds": [],
        }
    }
    assert result.rule.directory_path == tricky_path


def test_create_context_patch_auto_approve_rule_error_status_raises_textql_default_error(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.create_context_patch_auto_approve_rule(
            rule={"directory_path": "src/lib"}
        )

    assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_create_context_patch_auto_approve_rule_async_error_status_raises_textql_default_error(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.create_context_patch_auto_approve_rule_async()

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# update_context_patch_auto_approve_rule / update_context_patch_auto_approve_rule_async
# ---------------------------------------------------------------------------


def test_update_context_patch_auto_approve_rule_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"rule": {"id": "capa-1", "alwaysAutoApprove": True}}
        )
    )

    result = bundle.sdk.libraries.update_context_patch_auto_approve_rule(
        id="capa-1", rule={"always_auto_approve": True}
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpdateContextPatchAutoApproveRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "capa-1", "rule": {"alwaysAutoApprove": True}}

    assert result.rule.id == "capa-1"
    assert result.rule.always_auto_approve is True


@pytest.mark.asyncio
async def test_update_context_patch_auto_approve_rule_async_request_and_response(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(200, {"rule": {"id": "capa-2"}}))

    result = await bundle.sdk.libraries.update_context_patch_auto_approve_rule_async(
        id="capa-2", rule={"enabled": False}
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpdateContextPatchAutoApproveRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "capa-2", "rule": {"enabled": False}}
    assert result.rule.id == "capa-2"


def test_update_context_patch_auto_approve_rule_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.update_context_patch_auto_approve_rule()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# delete_context_patch_auto_approve_rule / delete_context_patch_auto_approve_rule_async
# ---------------------------------------------------------------------------


def test_delete_context_patch_auto_approve_rule_sync_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.libraries.delete_context_patch_auto_approve_rule(id="capa-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteContextPatchAutoApproveRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "capa-1"}
    assert result is not None


@pytest.mark.asyncio
async def test_delete_context_patch_auto_approve_rule_async_request_and_response(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.libraries.delete_context_patch_auto_approve_rule_async(
        id="capa-2"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteContextPatchAutoApproveRule"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"id": "capa-2"}
    assert result is not None


def test_delete_context_patch_auto_approve_rule_error_status_raises_textql_default_error(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.delete_context_patch_auto_approve_rule(id="missing")

    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_delete_context_patch_auto_approve_rule_async_error_status_raises_textql_default_error(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.delete_context_patch_auto_approve_rule_async(
            id="capa-x"
        )

    assert exc_info.value.status_code == 401


# ---------------------------------------------------------------------------
# list_context_patch_auto_approve_rules / list_context_patch_auto_approve_rules_async
# ---------------------------------------------------------------------------


def test_list_context_patch_auto_approve_rules_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "rules": [
                    {"id": "capa-1", "directoryPath": "src"},
                    {"id": "capa-2", "directoryPath": "docs"},
                ]
            },
        )
    )

    result = bundle.sdk.libraries.list_context_patch_auto_approve_rules(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListContextPatchAutoApproveRules"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}

    assert len(result.rules) == 2
    assert result.rules[0].id == "capa-1"
    assert result.rules[1].directory_path == "docs"


@pytest.mark.asyncio
async def test_list_context_patch_auto_approve_rules_async_request_and_response(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(200, {"rules": []}))

    result = await bundle.sdk.libraries.list_context_patch_auto_approve_rules_async(
        body={}
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListContextPatchAutoApproveRules"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.rules == []
