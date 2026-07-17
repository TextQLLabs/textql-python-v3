"""Unit tests for the Libraries remote-sync surface: configure/pull/push, sync conflicts, GitHub OAuth, migration."""
from __future__ import annotations

import pytest

from textql_sdk import errors
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PATH_PREFIX = "/textql.rpc.public.patches.LibraryService"


def assert_common(bundle, path_suffix: str, api_key: str = FAKE_API_KEY):
    """Assert method/path/auth-header invariants that apply to every call."""
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/{path_suffix}"
    assert req.headers[AUTH_HEADER_NAME] == api_key


# ---------------------------------------------------------------------------
# configure_library_remote (deep dive)
# ---------------------------------------------------------------------------


def test_configure_library_remote_sync_full_payload(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"remote": {"id": "rem-1", "remoteUrl": "https://github.com/a/b"}})
    )

    resp = bundle.sdk.libraries.configure_library_remote(
        remote_url="https://github.com/a/b.git",
        auth_type="token",
        token="secret-token",
        default_branch="main",
        use_hosted_github_app=True,
    )

    assert_common(bundle, "ConfigureLibraryRemote")
    body = bundle.transport.body_json()
    assert body["remoteUrl"] == "https://github.com/a/b.git"
    assert body["authType"] == "token"
    assert body["token"] == "secret-token"
    assert body["defaultBranch"] == "main"
    assert body["useHostedGithubApp"] is True

    assert resp.remote.id == "rem-1"


@pytest.mark.asyncio
async def test_configure_library_remote_async_full_payload(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"remote": {"id": "rem-2", "remoteUrl": "https://github.com/a/c"}})
    )

    resp = await bundle.sdk.libraries.configure_library_remote_async(
        remote_url="https://github.com/a/c.git",
        auth_type="ssh",
        ssh_private_key="-----BEGIN KEY-----",
    )

    assert_common(bundle, "ConfigureLibraryRemote")
    body = bundle.transport.body_json()
    assert body["remoteUrl"] == "https://github.com/a/c.git"
    assert body["sshPrivateKey"] == "-----BEGIN KEY-----"
    assert resp.remote.id == "rem-2"


def test_configure_library_remote_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.configure_library_remote(remote_url="https://x")

    assert exc_info.value.status_code == 404


def test_configure_library_remote_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.configure_library_remote(remote_url="https://x")

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_configure_library_remote_async_422_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "bad input"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.configure_library_remote_async(remote_url="https://x")

    assert exc_info.value.status_code == 422


def test_configure_library_remote_nullable_token_unset_omits_field(make_sdk):
    """token is OptionalNullable[str] = UNSET by default; when not passed it
    must be entirely absent from the serialized body (it's in both
    optional_fields and nullable_fields in
    TextqlRPCPublicPatchesConfigureLibraryRemoteRequest.serialize_model, and
    is only emitted if pydantic marks the field as explicitly set)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.configure_library_remote(remote_url="https://x")

    body = bundle.transport.body_json()
    assert "token" not in body
    assert body["remoteUrl"] == "https://x"


def test_configure_library_remote_nullable_token_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.configure_library_remote(remote_url="https://x", token="abc123")

    body = bundle.transport.body_json()
    assert body["token"] == "abc123"


def test_configure_library_remote_nullable_token_explicit_none_is_json_null(make_sdk):
    """Explicitly passing token=None (distinct from omitting it) must survive
    as JSON null in the body, since 'token' is a nullable_field and pydantic's
    __pydantic_fields_set__ will contain 'token' once explicitly passed."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.configure_library_remote(remote_url="https://x", token=None)

    body = bundle.transport.body_json()
    assert "token" in body
    assert body["token"] is None


def test_configure_library_remote_nullable_multiple_fields_unset_vs_explicit(make_sdk):
    """Cross-check several other OptionalNullable fields on the same model:
    ssh_private_key, default_branch, github_app_id, push_mode."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.configure_library_remote(
        remote_url="https://x",
        ssh_private_key=None,
        default_branch="develop",
        github_app_id=None,
        push_mode="force",
    )

    body = bundle.transport.body_json()
    assert body["sshPrivateKey"] is None
    assert body["defaultBranch"] == "develop"
    assert body["githubAppId"] is None
    assert body["pushMode"] == "force"
    # untouched nullable fields remain omitted entirely
    assert "sshKeyPassword" not in body
    assert "signingKey" not in body


def test_configure_library_remote_empty_string_remote_url(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.configure_library_remote(remote_url="")

    body = bundle.transport.body_json()
    assert body["remoteUrl"] == ""


def test_configure_library_remote_unicode_remote_url_and_branch(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    unicode_url = "https://github.com/组织/仓库-测试.git"
    unicode_branch = "功能/branch-émoji-🚀"

    bundle.sdk.libraries.configure_library_remote(
        remote_url=unicode_url,
        default_branch=unicode_branch,
    )

    body = bundle.transport.body_json()
    assert body["remoteUrl"] == unicode_url
    assert body["defaultBranch"] == unicode_branch


def test_configure_library_remote_large_ssh_key_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    large_key = "-----BEGIN KEY-----\n" + ("A" * 50_000) + "\n-----END KEY-----"

    bundle.sdk.libraries.configure_library_remote(
        remote_url="https://x",
        ssh_private_key=large_key,
    )

    body = bundle.transport.body_json()
    assert body["sshPrivateKey"] == large_key
    assert len(body["sshPrivateKey"]) == len(large_key)


def test_configure_library_remote_connect_timeout_ms_header(make_sdk):
    """connect_timeout_ms is serialized as the Connect-Timeout-Ms header, not
    a query param or body field (see LibraryServiceConfigureLibraryRemoteRequest)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.configure_library_remote(remote_url="https://x", connect_timeout_ms=1500.0)

    req = bundle.transport.last_request
    assert req.headers.get("Connect-Timeout-Ms") == "1500.0" or req.headers.get(
        "connect-timeout-ms"
    ) == "1500.0"


# ---------------------------------------------------------------------------
# get_remote
# ---------------------------------------------------------------------------


def test_get_remote_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "remote": {"id": "rem-9", "remoteUrl": "https://github.com/o/r"},
                "hostedGithubAppAvailable": True,
            },
        )
    )

    resp = bundle.sdk.libraries.get_remote(body={})

    assert_common(bundle, "GetLibraryRemote")
    assert resp.remote.id == "rem-9"
    assert resp.hosted_github_app_available is True


@pytest.mark.asyncio
async def test_get_remote_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"hostedGithubAppAvailable": False}))

    resp = await bundle.sdk.libraries.get_remote_async(body={})

    assert_common(bundle, "GetLibraryRemote")
    assert resp.hosted_github_app_available is False


# ---------------------------------------------------------------------------
# remove_remote
# ---------------------------------------------------------------------------


def test_remove_remote_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = bundle.sdk.libraries.remove_remote(body={})

    assert_common(bundle, "RemoveLibraryRemote")
    assert resp is not None


@pytest.mark.asyncio
async def test_remove_remote_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = await bundle.sdk.libraries.remove_remote_async(body={})

    assert_common(bundle, "RemoveLibraryRemote")
    assert resp is not None


# ---------------------------------------------------------------------------
# pull_from_remote (deep dive)
# ---------------------------------------------------------------------------


def test_pull_from_remote_sync_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.pull_from_remote(
        acknowledge_unrelated_histories=True,
        expected_local_head_hash="abc123",
        expected_remote_head_hash="def456",
    )

    assert_common(bundle, "PullLibraryFromRemote")
    body = bundle.transport.body_json()
    assert body["acknowledgeUnrelatedHistories"] is True
    assert body["expectedLocalHeadHash"] == "abc123"
    assert body["expectedRemoteHeadHash"] == "def456"


@pytest.mark.asyncio
async def test_pull_from_remote_async_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.libraries.pull_from_remote_async(
        acknowledge_unrelated_histories=False,
        expected_local_head_hash="hash-1",
    )

    assert_common(bundle, "PullLibraryFromRemote")
    body = bundle.transport.body_json()
    assert body["acknowledgeUnrelatedHistories"] is False
    assert body["expectedLocalHeadHash"] == "hash-1"


def test_pull_from_remote_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.pull_from_remote()

    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_pull_from_remote_async_503_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.pull_from_remote_async()

    assert exc_info.value.status_code == 503


def test_pull_from_remote_omitted_fields_absent(make_sdk):
    """acknowledge_unrelated_histories / expected_local_head_hash /
    expected_remote_head_hash are all plain Optional[...] (NOT
    OptionalNullable) on TextqlRPCPublicPatchesPullLibraryFromRemoteRequest --
    there is no nullable tri-state to exercise here. Omitted fields are simply
    absent from the serialized body."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.pull_from_remote()

    body = bundle.transport.body_json()
    assert body == {}


def test_pull_from_remote_empty_and_unicode_hashes(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.pull_from_remote(
        expected_local_head_hash="",
        expected_remote_head_hash="哈希-🔑-value",
    )

    body = bundle.transport.body_json()
    assert body["expectedLocalHeadHash"] == ""
    assert body["expectedRemoteHeadHash"] == "哈希-🔑-value"


def test_pull_from_remote_large_hash_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    large_hash = "f" * 100_000

    bundle.sdk.libraries.pull_from_remote(expected_local_head_hash=large_hash)

    body = bundle.transport.body_json()
    assert body["expectedLocalHeadHash"] == large_hash


# ---------------------------------------------------------------------------
# preview_library_pull_from_remote
# ---------------------------------------------------------------------------


def test_preview_library_pull_from_remote_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "totalFiles": 5,
                "topLevelFolderCount": 2,
                "unrelatedHistories": False,
            },
        )
    )

    resp = bundle.sdk.libraries.preview_library_pull_from_remote(body={})

    assert_common(bundle, "PreviewLibraryPullFromRemote")
    assert resp.total_files == 5
    assert resp.top_level_folder_count == 2
    assert resp.unrelated_histories is False


@pytest.mark.asyncio
async def test_preview_library_pull_from_remote_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "totalFiles": 0,
                "unrelatedHistoriesRemoteAdditions": ["a.txt"],
                "unrelatedHistoriesConflictPaths": ["b.txt"],
            },
        )
    )

    resp = await bundle.sdk.libraries.preview_library_pull_from_remote_async(body={})

    assert_common(bundle, "PreviewLibraryPullFromRemote")
    assert resp.total_files == 0
    assert resp.unrelated_histories_remote_additions == ["a.txt"]
    assert resp.unrelated_histories_conflict_paths == ["b.txt"]


# ---------------------------------------------------------------------------
# push_library_to_remote (deep dive)
# ---------------------------------------------------------------------------


def test_push_library_to_remote_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = bundle.sdk.libraries.push_library_to_remote(body={})

    assert_common(bundle, "PushLibraryToRemote")
    assert resp is not None
    body = bundle.transport.body_json()
    assert body == {}


@pytest.mark.asyncio
async def test_push_library_to_remote_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = await bundle.sdk.libraries.push_library_to_remote_async(body={})

    assert_common(bundle, "PushLibraryToRemote")
    assert resp is not None


def test_push_library_to_remote_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.push_library_to_remote(body={})

    assert exc_info.value.status_code == 404


def test_push_library_to_remote_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.push_library_to_remote(body={})

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_push_library_to_remote_async_409_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.push_library_to_remote_async(body={})

    assert exc_info.value.status_code == 409


def test_push_library_to_remote_no_nullable_fields_body_always_empty(make_sdk):
    """TextqlRPCPublicPatchesPushLibraryToRemoteRequest has no fields at all
    (neither plain Optional nor OptionalNullable) -- the request body is
    always `{}` regardless of what's passed to `body=`."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.push_library_to_remote(body={})

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# get_library_sync_conflicts
# ---------------------------------------------------------------------------


def test_get_library_sync_conflicts_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "conflicts": [
                    {"id": "c1", "filePath": "a.txt", "oursContent": "x", "theirsContent": "y"}
                ]
            },
        )
    )

    resp = bundle.sdk.libraries.get_library_sync_conflicts(body={})

    assert_common(bundle, "GetLibrarySyncConflicts")
    assert len(resp.conflicts) == 1
    assert resp.conflicts[0].id == "c1"
    assert resp.conflicts[0].file_path == "a.txt"


@pytest.mark.asyncio
async def test_get_library_sync_conflicts_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"conflicts": []}))

    resp = await bundle.sdk.libraries.get_library_sync_conflicts_async(body={})

    assert_common(bundle, "GetLibrarySyncConflicts")
    assert resp.conflicts == []


# ---------------------------------------------------------------------------
# resolve_sync_conflict (deep dive)
# ---------------------------------------------------------------------------


def test_resolve_sync_conflict_sync_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = bundle.sdk.libraries.resolve_sync_conflict(
        conflict_id="conflict-1",
        resolved_content="final content",
    )

    assert_common(bundle, "ResolveLibrarySyncConflict")
    body = bundle.transport.body_json()
    assert body["conflictId"] == "conflict-1"
    assert body["resolvedContent"] == "final content"
    assert resp is not None


@pytest.mark.asyncio
async def test_resolve_sync_conflict_async_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = await bundle.sdk.libraries.resolve_sync_conflict_async(
        conflict_id="conflict-2",
        resolved_content="other content",
    )

    assert_common(bundle, "ResolveLibrarySyncConflict")
    body = bundle.transport.body_json()
    assert body["conflictId"] == "conflict-2"
    assert resp is not None


def test_resolve_sync_conflict_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.resolve_sync_conflict(conflict_id="missing")

    assert exc_info.value.status_code == 404


def test_resolve_sync_conflict_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.resolve_sync_conflict(conflict_id="x")

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_resolve_sync_conflict_async_400_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.resolve_sync_conflict_async(conflict_id="x")

    assert exc_info.value.status_code == 400


def test_resolve_sync_conflict_omitted_fields_absent(make_sdk):
    """conflict_id / resolved_content are plain Optional[str] (NOT
    OptionalNullable) on TextqlRPCPublicPatchesResolveLibrarySyncConflictRequest
    -- there is no nullable tri-state to exercise here; omitting them just
    leaves the keys out of the serialized body entirely."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.resolve_sync_conflict()

    body = bundle.transport.body_json()
    assert body == {}


def test_resolve_sync_conflict_empty_string_conflict_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.resolve_sync_conflict(conflict_id="", resolved_content="")

    body = bundle.transport.body_json()
    assert body["conflictId"] == ""
    assert body["resolvedContent"] == ""


def test_resolve_sync_conflict_unicode_conflict_id_and_content(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    unicode_id = "冲突-🔥-id"
    unicode_content = "résolution finale — 解決済み"

    bundle.sdk.libraries.resolve_sync_conflict(
        conflict_id=unicode_id,
        resolved_content=unicode_content,
    )

    body = bundle.transport.body_json()
    assert body["conflictId"] == unicode_id
    assert body["resolvedContent"] == unicode_content


def test_resolve_sync_conflict_large_resolved_content(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    large_content = "line of resolved content\n" * 10_000

    bundle.sdk.libraries.resolve_sync_conflict(
        conflict_id="conflict-large",
        resolved_content=large_content,
    )

    body = bundle.transport.body_json()
    assert body["resolvedContent"] == large_content
    assert len(body["resolvedContent"]) == len(large_content)


# ---------------------------------------------------------------------------
# list_library_sync_runs
# ---------------------------------------------------------------------------


def test_list_library_sync_runs_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "runs": [{"id": "run-1", "status": "SUCCEEDED"}],
                "nextPageToken": "tok-2",
            },
        )
    )

    resp = bundle.sdk.libraries.list_library_sync_runs(page_size=10, page_token="tok-1")

    assert_common(bundle, "ListLibrarySyncRuns")
    body = bundle.transport.body_json()
    assert body["pageSize"] == 10
    assert body["pageToken"] == "tok-1"
    assert len(resp.runs) == 1
    assert resp.next_page_token == "tok-2"


@pytest.mark.asyncio
async def test_list_library_sync_runs_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"runs": []}))

    resp = await bundle.sdk.libraries.list_library_sync_runs_async(page_size=20)

    assert_common(bundle, "ListLibrarySyncRuns")
    body = bundle.transport.body_json()
    assert body["pageSize"] == 20
    assert resp.runs == []


def test_list_library_sync_runs_nullable_page_size_unset_omits_field(make_sdk):
    """page_size/page_token are OptionalNullable[...] = UNSET by default on
    TextqlRPCPublicPatchesListLibrarySyncRunsRequest; omitting them must omit
    the keys entirely."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_library_sync_runs()

    body = bundle.transport.body_json()
    assert body == {}


def test_list_library_sync_runs_nullable_page_token_explicit_none_is_json_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_library_sync_runs(page_token=None)

    body = bundle.transport.body_json()
    assert "pageToken" in body
    assert body["pageToken"] is None


def test_list_library_sync_runs_nullable_page_size_explicit_none_is_json_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_library_sync_runs(page_size=None)

    body = bundle.transport.body_json()
    assert "pageSize" in body
    assert body["pageSize"] is None


# ---------------------------------------------------------------------------
# update_library_sync_config
# ---------------------------------------------------------------------------


def test_update_library_sync_config_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"remote": {"id": "rem-3", "syncEnabled": True}})
    )

    resp = bundle.sdk.libraries.update_library_sync_config(
        sync_enabled=True,
        sync_interval_minutes=15,
    )

    assert_common(bundle, "UpdateLibrarySyncConfig")
    body = bundle.transport.body_json()
    assert body["syncEnabled"] is True
    assert body["syncIntervalMinutes"] == 15
    assert resp.remote.id == "rem-3"


@pytest.mark.asyncio
async def test_update_library_sync_config_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = await bundle.sdk.libraries.update_library_sync_config_async(sync_enabled=False)

    assert_common(bundle, "UpdateLibrarySyncConfig")
    body = bundle.transport.body_json()
    assert body["syncEnabled"] is False
    assert resp is not None


# ---------------------------------------------------------------------------
# exchange_github_code
# ---------------------------------------------------------------------------


def test_exchange_github_code_sync(make_sdk):
    """code/state/code_verifier are body params here (not query params, as one
    might assume for an OAuth redirect-style endpoint) -- see
    TextqlRPCPublicPatchesExchangeLibraryGithubCodeRequest, which is nested
    under LibraryServiceExchangeLibraryGithubCodeRequest.body."""
    bundle = make_sdk(
        lambda req: json_response(200, {"success": True, "installations": []})
    )

    resp = bundle.sdk.libraries.exchange_github_code(
        code="oauth-code-123",
        state="state-abc",
        code_verifier="verifier-xyz",
    )

    assert_common(bundle, "ExchangeLibraryGithubCode")
    body = bundle.transport.body_json()
    assert body["code"] == "oauth-code-123"
    assert body["state"] == "state-abc"
    assert body["codeVerifier"] == "verifier-xyz"
    assert resp.success is True
    assert resp.installations == []


@pytest.mark.asyncio
async def test_exchange_github_code_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "installations": [{"id": "inst-1", "accountLogin": "acme"}],
            },
        )
    )

    resp = await bundle.sdk.libraries.exchange_github_code_async(code="code-2")

    assert_common(bundle, "ExchangeLibraryGithubCode")
    body = bundle.transport.body_json()
    assert body["code"] == "code-2"
    assert resp.success is True
    assert resp.installations[0].id == "inst-1"


# ---------------------------------------------------------------------------
# get_library_github_o_auth_url
# ---------------------------------------------------------------------------


def test_get_library_github_o_auth_url_sync(make_sdk):
    """state/code_challenge are also body params, not query params -- see
    TextqlRPCPublicPatchesGetLibraryGithubOAuthURLRequest nested under
    LibraryServiceGetLibraryGithubOAuthURLRequest.body."""
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "authorizeUrl": "https://github.com/login/oauth/authorize?x=1",
                "installUrl": "https://github.com/apps/foo/installations/new",
                "available": True,
            },
        )
    )

    resp = bundle.sdk.libraries.get_library_github_o_auth_url(
        state="state-1",
        code_challenge="challenge-1",
    )

    assert_common(bundle, "GetLibraryGithubOAuthURL")
    body = bundle.transport.body_json()
    assert body["state"] == "state-1"
    assert body["codeChallenge"] == "challenge-1"
    assert resp.authorize_url.startswith("https://github.com/login/oauth/authorize")
    assert resp.available is True


@pytest.mark.asyncio
async def test_get_library_github_o_auth_url_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"available": False}))

    resp = await bundle.sdk.libraries.get_library_github_o_auth_url_async(state="state-2")

    assert_common(bundle, "GetLibraryGithubOAuthURL")
    body = bundle.transport.body_json()
    assert body["state"] == "state-2"
    assert resp.available is False


# ---------------------------------------------------------------------------
# plan_merge
# ---------------------------------------------------------------------------


def test_plan_merge_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "outcome": "LIBRARY_MERGE_OUTCOME_FAST_FORWARD",
                "localHeadHash": "local-1",
                "remoteHeadHash": "remote-1",
            },
        )
    )

    resp = bundle.sdk.libraries.plan_merge(body={})

    assert_common(bundle, "PlanLibraryMerge")
    assert resp.outcome == "LIBRARY_MERGE_OUTCOME_FAST_FORWARD"
    assert resp.local_head_hash == "local-1"
    assert resp.remote_head_hash == "remote-1"


@pytest.mark.asyncio
async def test_plan_merge_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "outcome": "LIBRARY_MERGE_OUTCOME_MERGE_REQUIRED",
                "conflictPaths": ["a.txt", "b.txt"],
            },
        )
    )

    resp = await bundle.sdk.libraries.plan_merge_async(body={})

    assert_common(bundle, "PlanLibraryMerge")
    assert resp.outcome == "LIBRARY_MERGE_OUTCOME_MERGE_REQUIRED"
    assert resp.conflict_paths == ["a.txt", "b.txt"]


# ---------------------------------------------------------------------------
# recover
# ---------------------------------------------------------------------------


def test_recover_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = bundle.sdk.libraries.recover(level="RECOVER_LIBRARY_LEVEL_RESET_TO_REMOTE")

    assert_common(bundle, "RecoverLibrary")
    body = bundle.transport.body_json()
    assert body["level"] == "RECOVER_LIBRARY_LEVEL_RESET_TO_REMOTE"
    assert resp is not None


@pytest.mark.asyncio
async def test_recover_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = await bundle.sdk.libraries.recover_async(level="RECOVER_LIBRARY_LEVEL_RECLONE")

    assert_common(bundle, "RecoverLibrary")
    body = bundle.transport.body_json()
    assert body["level"] == "RECOVER_LIBRARY_LEVEL_RECLONE"
    assert resp is not None


# ---------------------------------------------------------------------------
# trigger_config_drift_reconcile
# ---------------------------------------------------------------------------


def test_trigger_config_drift_reconcile_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"drifted": True}))

    resp = bundle.sdk.libraries.trigger_config_drift_reconcile(body={})

    assert_common(bundle, "TriggerConfigDriftReconcile")
    assert resp.drifted is True


@pytest.mark.asyncio
async def test_trigger_config_drift_reconcile_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"drifted": False}))

    resp = await bundle.sdk.libraries.trigger_config_drift_reconcile_async(body={})

    assert_common(bundle, "TriggerConfigDriftReconcile")
    assert resp.drifted is False


# ---------------------------------------------------------------------------
# get_migration_status
# ---------------------------------------------------------------------------


def test_get_migration_status_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"pendingLegacyContextCount": 42}))

    resp = bundle.sdk.libraries.get_migration_status(body={})

    assert_common(bundle, "GetLibraryMigrationStatus")
    assert resp.pending_legacy_context_count == 42


@pytest.mark.asyncio
async def test_get_migration_status_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"pendingLegacyContextCount": 0}))

    resp = await bundle.sdk.libraries.get_migration_status_async(body={})

    assert_common(bundle, "GetLibraryMigrationStatus")
    assert resp.pending_legacy_context_count == 0
