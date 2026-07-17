"""Unit tests for Libraries submodule operations: add_submodule, remove_library_submodule, list_library_submodules."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors

SUBMODULE_PATH = "/textql.rpc.public.patches.LibraryService/AddLibrarySubmodule"
REMOVE_PATH = "/textql.rpc.public.patches.LibraryService/RemoveLibrarySubmodule"
LIST_PATH = "/textql.rpc.public.patches.LibraryService/ListLibrarySubmodules"


# ---------------------------------------------------------------------------
# add_submodule
# ---------------------------------------------------------------------------


def test_add_submodule_sync_builds_request_and_unmarshals_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"path": "vendor/foo", "url": "https://github.com/example/foo.git", "branch": "main"},
        )
    )

    result = bundle.sdk.libraries.add_submodule(
        url="https://github.com/example/foo.git",
        path="vendor/foo",
        branch="main",
    )

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == SUBMODULE_PATH
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["url"] == "https://github.com/example/foo.git"
    assert body["path"] == "vendor/foo"
    assert body["branch"] == "main"

    assert result.path == "vendor/foo"
    assert result.url == "https://github.com/example/foo.git"
    assert result.branch == "main"


@pytest.mark.asyncio
async def test_add_submodule_async_builds_request_and_unmarshals_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"path": "vendor/bar", "url": "https://github.com/example/bar.git", "branch": "dev"},
        )
    )

    result = await bundle.sdk.libraries.add_submodule_async(
        url="https://github.com/example/bar.git",
        path="vendor/bar",
        branch="dev",
    )

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == SUBMODULE_PATH
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["url"] == "https://github.com/example/bar.git"
    assert body["path"] == "vendor/bar"
    assert body["branch"] == "dev"

    assert result.path == "vendor/bar"
    assert result.branch == "dev"


def test_add_submodule_branch_omitted_is_absent_from_body(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.add_submodule(
        url="https://github.com/example/foo.git",
        path="vendor/foo",
    )

    body = bundle.transport.body_json()
    assert "branch" not in body
    assert body["url"] == "https://github.com/example/foo.git"
    assert body["path"] == "vendor/foo"


def test_add_submodule_branch_explicit_value_present_in_body(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.add_submodule(
        url="https://github.com/example/foo.git",
        path="vendor/foo",
        branch="main",
    )

    body = bundle.transport.body_json()
    assert body["branch"] == "main"


def test_add_submodule_branch_explicit_none_serializes_as_json_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.add_submodule(
        url="https://github.com/example/foo.git",
        path="vendor/foo",
        branch=None,
    )

    body = bundle.transport.body_json()
    assert "branch" in body
    assert body["branch"] is None


def test_add_submodule_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(422, {"message": "invalid submodule url"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.add_submodule(
            url="not-a-valid-url",
            path="vendor/foo",
        )

    assert exc_info.value.status_code == 422


def test_add_submodule_unicode_path_and_url(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "path": "vendor/日本語-módulo",
                "url": "https://github.com/example/héllo-wörld.git",
                "branch": "función/über-brânch",
            },
        )
    )

    result = bundle.sdk.libraries.add_submodule(
        url="https://github.com/example/héllo-wörld.git",
        path="vendor/日本語-módulo",
        branch="función/über-brânch",
    )

    body = bundle.transport.body_json()
    assert body["url"] == "https://github.com/example/héllo-wörld.git"
    assert body["path"] == "vendor/日本語-módulo"
    assert body["branch"] == "función/über-brânch"

    assert result.path == "vendor/日本語-módulo"
    assert result.url == "https://github.com/example/héllo-wörld.git"
    assert result.branch == "función/über-brânch"


# ---------------------------------------------------------------------------
# remove_library_submodule
# ---------------------------------------------------------------------------


def test_remove_library_submodule_sync_builds_request_and_unmarshals_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.remove_library_submodule(path="vendor/foo")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == REMOVE_PATH
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["path"] == "vendor/foo"


@pytest.mark.asyncio
async def test_remove_library_submodule_async_builds_request_and_unmarshals_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.libraries.remove_library_submodule_async(path="vendor/bar")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == REMOVE_PATH
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["path"] == "vendor/bar"


# ---------------------------------------------------------------------------
# list_library_submodules
# ---------------------------------------------------------------------------


def test_list_library_submodules_sync_builds_request_and_unmarshals_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "submodules": [
                    {
                        "name": "foo",
                        "path": "vendor/foo",
                        "url": "https://github.com/example/foo.git",
                        "branch": "main",
                    }
                ]
            },
        )
    )

    result = bundle.sdk.libraries.list_library_submodules(body={})

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == LIST_PATH
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    assert result.submodules is not None
    assert len(result.submodules) == 1
    assert result.submodules[0].name == "foo"
    assert result.submodules[0].path == "vendor/foo"


@pytest.mark.asyncio
async def test_list_library_submodules_async_builds_request_and_unmarshals_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "submodules": [
                    {
                        "name": "bar",
                        "path": "vendor/bar",
                        "url": "https://github.com/example/bar.git",
                        "branch": "dev",
                    }
                ]
            },
        )
    )

    result = await bundle.sdk.libraries.list_library_submodules_async(body={})

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == LIST_PATH
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    assert result.submodules is not None
    assert len(result.submodules) == 1
    assert result.submodules[0].name == "bar"
