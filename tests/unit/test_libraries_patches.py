"""Unit tests for sdk.libraries patch-related operations."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors

PATCH_PATH_PREFIX = "/textql.rpc.public.patches.LibraryService"


# ---------------------------------------------------------------------------
# approve_patch
# ---------------------------------------------------------------------------


def test_approve_patch_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "merged": True,
                "approvalCount": 2,
                "requiredApprovals": 2,
                "alreadyApproved": False,
            },
        )
    )

    result = bundle.sdk.libraries.approve_patch(
        patch_id="patch-123", expected_git_ref="refs/heads/main"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/ApprovePatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-123", "expectedGitRef": "refs/heads/main"}
    assert result.merged is True
    assert result.approval_count == 2


@pytest.mark.asyncio
async def test_approve_patch_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "merged": False,
                "approvalCount": 1,
                "requiredApprovals": 2,
                "alreadyApproved": True,
            },
        )
    )

    result = await bundle.sdk.libraries.approve_patch_async(
        patch_id="patch-async-1", expected_git_ref="refs/heads/dev"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/ApprovePatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-async-1", "expectedGitRef": "refs/heads/dev"}
    assert result.already_approved is True


def test_approve_patch_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "already merged"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.approve_patch(patch_id="patch-conflict")

    assert exc_info.value.status_code == 409
    assert exc_info.value.raw_response is not None
    assert "already merged" in exc_info.value.body


@pytest.mark.asyncio
async def test_approve_patch_5xx_raises_textql_default_error_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.approve_patch_async(patch_id="patch-503")

    assert exc_info.value.status_code == 503


def test_approve_patch_expected_git_ref_omitted_when_not_passed(make_sdk):
    # expected_git_ref has a default of None and is a plain Optional[str]
    # (not nullable), so omitting the kwarg entirely must drop the key.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.approve_patch(patch_id="only-patch-id")

    body = bundle.transport.body_json()
    assert body == {"patchId": "only-patch-id"}
    assert "expectedGitRef" not in body


def test_approve_patch_explicit_none_expected_git_ref_is_omitted(make_sdk):
    # expected_git_ref is a plain Optional[str] field (not OptionalNullable),
    # so explicit None behaves the same as omission: the key is dropped.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.approve_patch(patch_id="pid", expected_git_ref=None)

    body = bundle.transport.body_json()
    assert body == {"patchId": "pid"}


def test_approve_patch_unicode_and_empty_patch_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.approve_patch(patch_id="", expected_git_ref="")
    body = bundle.transport.body_json()
    # empty string is not None, so both keys should be present with "" values
    assert body == {"patchId": "", "expectedGitRef": ""}

    unicode_id = "patch-é中文-\U0001F600"
    bundle.sdk.libraries.approve_patch(patch_id=unicode_id)
    body2 = bundle.transport.body_json()
    assert body2["patchId"] == unicode_id


# ---------------------------------------------------------------------------
# deny_patch
# ---------------------------------------------------------------------------


def test_deny_patch_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.libraries.deny_patch(
        patch_id="patch-456", expected_git_ref="refs/heads/main"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/DenyPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-456", "expectedGitRef": "refs/heads/main"}
    # response model is GoogleProtobufEmpty
    assert result is not None


@pytest.mark.asyncio
async def test_deny_patch_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.libraries.deny_patch_async(
        patch_id="patch-789", expected_git_ref="refs/heads/feature"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/DenyPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-789", "expectedGitRef": "refs/heads/feature"}


def test_deny_patch_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "patch not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.deny_patch(patch_id="missing-patch")

    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_deny_patch_5xx_raises_textql_default_error_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.deny_patch_async(patch_id="patch-500")

    assert exc_info.value.status_code == 500


def test_deny_patch_omitted_expected_git_ref(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.deny_patch(patch_id="pid-only")

    body = bundle.transport.body_json()
    assert body == {"patchId": "pid-only"}


def test_deny_patch_unicode_patch_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    unicode_id = "パッチ-éè"

    bundle.sdk.libraries.deny_patch(patch_id=unicode_id)

    body = bundle.transport.body_json()
    assert body["patchId"] == unicode_id


# ---------------------------------------------------------------------------
# get_patch
# ---------------------------------------------------------------------------


def _sample_patch_payload():
    return {
        "id": "patch-1",
        "number": 42,
        "authorId": "member-1",
        "title": "Fix the thing",
        "description": "This fixes the thing",
        "aiGenerated": False,
        "status": "PATCH_STATUS_OPEN",
        "gitRef": "refs/heads/patch-1",
        "revision": 3,
        "createdAt": "2026-01-01T00:00:00Z",
        "updatedAt": "2026-01-02T00:00:00Z",
        "approvalCount": 1,
        "requiredApprovals": 2,
    }


def test_get_patch_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    result = bundle.sdk.libraries.get_patch(patch_id="patch-1", revision=3)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-1", "revision": 3}
    assert result.id == "patch-1"
    assert result.number == 42
    assert result.status == "PATCH_STATUS_OPEN"


@pytest.mark.asyncio
async def test_get_patch_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    result = await bundle.sdk.libraries.get_patch_async(patch_id="patch-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    # revision omitted entirely -> UNSET, no key
    assert body == {"patchId": "patch-1"}
    assert result.title == "Fix the thing"


def test_get_patch_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.get_patch(patch_id="bad-patch")

    assert exc_info.value.status_code == 400


@pytest.mark.asyncio
async def test_get_patch_5xx_raises_textql_default_error_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.get_patch_async(patch_id="patch-502")

    assert exc_info.value.status_code == 502


def test_get_patch_revision_unset_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    bundle.sdk.libraries.get_patch(patch_id="p1")

    body = bundle.transport.body_json()
    assert "revision" not in body
    assert body == {"patchId": "p1"}


def test_get_patch_revision_explicit_value_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    bundle.sdk.libraries.get_patch(patch_id="p1", revision=7)

    body = bundle.transport.body_json()
    assert body["revision"] == 7


def test_get_patch_revision_explicit_none_is_json_null(make_sdk):
    # revision is OptionalNullable[int]; explicit None (distinct from
    # omission) should serialize the field as JSON null because it's in
    # nullable_fields and marked as explicitly set via
    # __pydantic_fields_set__.
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    bundle.sdk.libraries.get_patch(patch_id="p1", revision=None)

    body = bundle.transport.body_json()
    assert "revision" in body
    assert body["revision"] is None


def test_get_patch_empty_string_patch_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    bundle.sdk.libraries.get_patch(patch_id="")

    body = bundle.transport.body_json()
    assert body == {"patchId": ""}


def test_get_patch_unicode_patch_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))
    unicode_id = "ünicode-patch-中文-\U0001F4A9"

    bundle.sdk.libraries.get_patch(patch_id=unicode_id)

    body = bundle.transport.body_json()
    assert body["patchId"] == unicode_id


# ---------------------------------------------------------------------------
# get_patch_by_number (distinct from get_patch: takes an int `number`, not a
# `patch_id` string)
# ---------------------------------------------------------------------------


def test_get_patch_by_number_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    result = bundle.sdk.libraries.get_patch_by_number(number=42)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetPatchByNumber"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"number": 42}
    assert result.number == 42


@pytest.mark.asyncio
async def test_get_patch_by_number_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    result = await bundle.sdk.libraries.get_patch_by_number_async(number=99)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetPatchByNumber"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"number": 99}
    assert result.id == "patch-1"


def test_get_patch_by_number_zero_and_large_values(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, _sample_patch_payload()))

    bundle.sdk.libraries.get_patch_by_number(number=0)
    assert bundle.transport.body_json() == {"number": 0}

    bundle.sdk.libraries.get_patch_by_number(number=2**31 - 1)
    assert bundle.transport.body_json() == {"number": 2**31 - 1}


# ---------------------------------------------------------------------------
# get_raw_patch
# ---------------------------------------------------------------------------


def test_get_raw_patch_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"rawPatch": "diff --git a/x b/x\n"})
    )

    result = bundle.sdk.libraries.get_raw_patch(patch_number=7)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetRawPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchNumber": 7}
    assert result.raw_patch == "diff --git a/x b/x\n"


@pytest.mark.asyncio
async def test_get_raw_patch_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"rawPatch": "diff content"}))

    result = await bundle.sdk.libraries.get_raw_patch_async(patch_number=8)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetRawPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchNumber": 8}
    assert result.raw_patch == "diff content"


def test_get_raw_patch_large_payload(make_sdk):
    large_diff = "+line\n" * 50_000
    bundle = make_sdk(lambda req: json_response(200, {"rawPatch": large_diff}))

    result = bundle.sdk.libraries.get_raw_patch(patch_number=1)

    assert len(result.raw_patch) == len(large_diff)


# ---------------------------------------------------------------------------
# get_patch_capabilities
# ---------------------------------------------------------------------------


def test_get_patch_capabilities_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "capabilities": {
                    "canApprove": True,
                    "canDeny": False,
                    "canRestore": False,
                    "callerApproved": True,
                },
                "status": "PATCH_STATUS_OPEN",
            },
        )
    )

    result = bundle.sdk.libraries.get_patch_capabilities(patch_id="patch-cap-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetPatchCapabilities"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-cap-1"}
    assert result.capabilities.can_approve is True
    assert result.status == "PATCH_STATUS_OPEN"


@pytest.mark.asyncio
async def test_get_patch_capabilities_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "capabilities": {"canApprove": False, "canDeny": True},
                "status": "PATCH_STATUS_DENIED",
            },
        )
    )

    result = await bundle.sdk.libraries.get_patch_capabilities_async(
        patch_id="patch-cap-2"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetPatchCapabilities"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-cap-2"}
    assert result.capabilities.can_deny is True


def test_get_patch_capabilities_empty_patch_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_patch_capabilities(patch_id="")

    body = bundle.transport.body_json()
    assert body == {"patchId": ""}


# ---------------------------------------------------------------------------
# get_history_file_diff
# ---------------------------------------------------------------------------


def test_get_history_file_diff_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "commitId": "abc123",
                "path": "some/file.txt",
                "changeType": "LIBRARY_HISTORY_CHANGE_TYPE_MODIFIED",
                "beforeContent": "old",
                "afterContent": "new",
                "isBinary": False,
            },
        )
    )

    result = bundle.sdk.libraries.get_history_file_diff(
        commit_id="abc123", path="some/file.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetLibraryHistoryFileDiff"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"commitId": "abc123", "path": "some/file.txt"}
    assert result.commit_id == "abc123"
    assert result.after_content == "new"


@pytest.mark.asyncio
async def test_get_history_file_diff_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "commitId": "def456",
                "path": "dir/other.txt",
                "isBinary": True,
            },
        )
    )

    result = await bundle.sdk.libraries.get_history_file_diff_async(
        commit_id="def456", path="dir/other.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/GetLibraryHistoryFileDiff"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"commitId": "def456", "path": "dir/other.txt"}
    assert result.is_binary is True


def test_get_history_file_diff_unicode_and_special_char_path(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    unicode_path = "dír/中文 file (v2) [final].txt"

    bundle.sdk.libraries.get_history_file_diff(commit_id="c1", path=unicode_path)

    body = bundle.transport.body_json()
    assert body["path"] == unicode_path


def test_get_history_file_diff_large_content_payload(make_sdk):
    huge_before = "a" * 200_000
    huge_after = "b" * 200_000
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "commitId": "big-commit",
                "path": "big/file.txt",
                "beforeContent": huge_before,
                "afterContent": huge_after,
            },
        )
    )

    result = bundle.sdk.libraries.get_history_file_diff(
        commit_id="big-commit", path="big/file.txt"
    )

    assert len(result.before_content) == 200_000
    assert len(result.after_content) == 200_000


# ---------------------------------------------------------------------------
# list_patch_reviewers
# ---------------------------------------------------------------------------


def test_list_patch_reviewers_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "reviewers": [
                    {
                        "memberId": "member-1",
                        "name": "Alice",
                        "email": "alice@example.com",
                        "isAdmin": True,
                        "isCodeOwner": False,
                    },
                    {
                        "memberId": "member-2",
                        "name": "Bob",
                        "email": "bob@example.com",
                        "isAdmin": False,
                        "isCodeOwner": True,
                    },
                ]
            },
        )
    )

    result = bundle.sdk.libraries.list_patch_reviewers(patch_id="patch-r1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/ListPatchReviewers"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-r1"}
    assert len(result.reviewers) == 2
    assert result.reviewers[0].name == "Alice"


@pytest.mark.asyncio
async def test_list_patch_reviewers_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reviewers": []}))

    result = await bundle.sdk.libraries.list_patch_reviewers_async(
        patch_id="patch-r2"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/ListPatchReviewers"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-r2"}
    assert result.reviewers == []


def test_list_patch_reviewers_empty_patch_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reviewers": []}))

    bundle.sdk.libraries.list_patch_reviewers(patch_id="")

    body = bundle.transport.body_json()
    assert body == {"patchId": ""}


# ---------------------------------------------------------------------------
# list_patches
# ---------------------------------------------------------------------------


def test_list_patches_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "patches": [_sample_patch_payload()],
                "nextPageToken": "next-token",
                "counts": {},
            },
        )
    )

    result = bundle.sdk.libraries.list_patches(
        page_size=25,
        page_token="cursor-1",
        statuses=["PATCH_STATUS_OPEN", "PATCH_STATUS_APPROVED"],
        include_auto_approved=True,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/ListPatches"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "pageSize": 25,
        "pageToken": "cursor-1",
        "statuses": ["PATCH_STATUS_OPEN", "PATCH_STATUS_APPROVED"],
        "includeAutoApproved": True,
    }
    assert len(result.patches) == 1
    assert result.next_page_token == "next-token"


@pytest.mark.asyncio
async def test_list_patches_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"patches": [], "counts": {}})
    )

    result = await bundle.sdk.libraries.list_patches_async(page_size=10)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/ListPatches"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"pageSize": 10}
    assert result.patches == []


def test_list_patches_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.list_patches()

    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_list_patches_5xx_raises_textql_default_error_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.list_patches_async()

    assert exc_info.value.status_code == 500


def test_list_patches_all_fields_unset_by_default(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_patches()

    body = bundle.transport.body_json()
    # everything is OptionalNullable/Optional and omitted -> empty body
    assert body in (None, {})


def test_list_patches_page_size_explicit_none_is_json_null(make_sdk):
    # page_size is OptionalNullable[int]; explicit None should serialize
    # as JSON null (distinct from omission).
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_patches(page_size=None)

    body = bundle.transport.body_json()
    assert "pageSize" in body
    assert body["pageSize"] is None


def test_list_patches_page_token_explicit_none_is_json_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_patches(page_token=None)

    body = bundle.transport.body_json()
    assert "pageToken" in body
    assert body["pageToken"] is None


def test_list_patches_include_auto_approved_explicit_none_is_json_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_patches(include_auto_approved=None)

    body = bundle.transport.body_json()
    assert "includeAutoApproved" in body
    assert body["includeAutoApproved"] is None


def test_list_patches_explicit_values_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_patches(
        page_size=100, page_token="tok", include_auto_approved=False
    )

    body = bundle.transport.body_json()
    assert body == {
        "pageSize": 100,
        "pageToken": "tok",
        "includeAutoApproved": False,
    }


def test_list_patches_large_page_size(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"patches": [], "counts": {}})
    )

    bundle.sdk.libraries.list_patches(page_size=1_000_000)

    body = bundle.transport.body_json()
    assert body["pageSize"] == 1_000_000


def test_list_patches_unicode_page_token(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"patches": [], "counts": {}})
    )
    token = "cursor-é中文-\U0001F600"

    bundle.sdk.libraries.list_patches(page_token=token)

    body = bundle.transport.body_json()
    assert body["pageToken"] == token


def test_list_patches_empty_statuses_list_present(make_sdk):
    # statuses is Optional[Iterable[...]] (not OptionalNullable) -- passing
    # an empty list is a non-None value, so it should be serialized as [].
    bundle = make_sdk(
        lambda req: json_response(200, {"patches": [], "counts": {}})
    )

    bundle.sdk.libraries.list_patches(statuses=[])

    body = bundle.transport.body_json()
    assert body.get("statuses") == []


# ---------------------------------------------------------------------------
# request_patch_review
# ---------------------------------------------------------------------------


def test_request_patch_review_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"sent": True}))

    result = bundle.sdk.libraries.request_patch_review(
        patch_id="patch-req-1", reviewer_member_id="member-9"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/RequestPatchReview"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-req-1", "reviewerMemberId": "member-9"}
    assert result.sent is True


@pytest.mark.asyncio
async def test_request_patch_review_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"sent": False}))

    result = await bundle.sdk.libraries.request_patch_review_async(
        patch_id="patch-req-2", reviewer_member_id="member-10"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/RequestPatchReview"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-req-2", "reviewerMemberId": "member-10"}
    assert result.sent is False


def test_request_patch_review_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid reviewer"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.request_patch_review(
            patch_id="p1", reviewer_member_id="bad-member"
        )

    assert exc_info.value.status_code == 422


@pytest.mark.asyncio
async def test_request_patch_review_5xx_raises_textql_default_error_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(504, {"message": "timeout"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.request_patch_review_async(
            patch_id="p1", reviewer_member_id="m1"
        )

    assert exc_info.value.status_code == 504


def test_request_patch_review_omitted_reviewer_member_id(make_sdk):
    # reviewer_member_id is a plain Optional[str] (not nullable) -- omission
    # drops the key entirely.
    bundle = make_sdk(lambda req: json_response(200, {"sent": True}))

    bundle.sdk.libraries.request_patch_review(patch_id="p-only")

    body = bundle.transport.body_json()
    assert body == {"patchId": "p-only"}


def test_request_patch_review_explicit_none_reviewer_member_id_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"sent": True}))

    bundle.sdk.libraries.request_patch_review(
        patch_id="p-none", reviewer_member_id=None
    )

    body = bundle.transport.body_json()
    # not a nullable field, so explicit None behaves like omission
    assert body == {"patchId": "p-none"}


def test_request_patch_review_unicode_and_long_reviewer_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"sent": True}))
    long_id = "member-" + "x" * 5000
    unicode_id = "member-é中文"

    bundle.sdk.libraries.request_patch_review(
        patch_id="p1", reviewer_member_id=long_id
    )
    body = bundle.transport.body_json()
    assert body["reviewerMemberId"] == long_id

    bundle.sdk.libraries.request_patch_review(
        patch_id="p1", reviewer_member_id=unicode_id
    )
    body2 = bundle.transport.body_json()
    assert body2["reviewerMemberId"] == unicode_id


# ---------------------------------------------------------------------------
# restore_patch
# ---------------------------------------------------------------------------


def test_restore_patch_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.restore_patch(
        patch_id="patch-restore-1", expected_git_ref="refs/heads/main"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/RestorePatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "patchId": "patch-restore-1",
        "expectedGitRef": "refs/heads/main",
    }


@pytest.mark.asyncio
async def test_restore_patch_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.libraries.restore_patch_async(
        patch_id="patch-restore-2", expected_git_ref="refs/heads/dev"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/RestorePatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "patchId": "patch-restore-2",
        "expectedGitRef": "refs/heads/dev",
    }


def test_restore_patch_empty_string_ids(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.restore_patch(patch_id="", expected_git_ref="")

    body = bundle.transport.body_json()
    assert body == {"patchId": "", "expectedGitRef": ""}


# ---------------------------------------------------------------------------
# revert_patch
# ---------------------------------------------------------------------------


def test_revert_patch_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"revertPatch": _sample_patch_payload()}
        )
    )

    result = bundle.sdk.libraries.revert_patch(patch_id="patch-orig-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/RevertPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-orig-1"}
    assert result.revert_patch.id == "patch-1"


@pytest.mark.asyncio
async def test_revert_patch_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"revertPatch": _sample_patch_payload()}
        )
    )

    result = await bundle.sdk.libraries.revert_patch_async(patch_id="patch-orig-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATCH_PATH_PREFIX}/RevertPatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-orig-2"}
    assert result.revert_patch.number == 42


def test_revert_patch_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.revert_patch(patch_id="forbidden-patch")

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_revert_patch_5xx_raises_textql_default_error_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "internal error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.revert_patch_async(patch_id="patch-500")

    assert exc_info.value.status_code == 500


def test_revert_patch_empty_string_patch_id(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"revertPatch": _sample_patch_payload()})
    )

    bundle.sdk.libraries.revert_patch(patch_id="")

    body = bundle.transport.body_json()
    assert body == {"patchId": ""}


def test_revert_patch_unicode_patch_id(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"revertPatch": _sample_patch_payload()})
    )
    unicode_id = "revert-é中文-\U0001F680"

    bundle.sdk.libraries.revert_patch(patch_id=unicode_id)

    body = bundle.transport.body_json()
    assert body["patchId"] == unicode_id
