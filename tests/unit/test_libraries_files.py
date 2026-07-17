"""Unit tests for the Libraries service file/directory operations (sdk.libraries):"""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors

BASE_PATH = "/textql.rpc.public.patches.LibraryService"


# ---------------------------------------------------------------------------
# get_file / get_file_async  (deep-dive operation)
# ---------------------------------------------------------------------------


def test_get_file_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"file": {"path": "docs/readme.md", "content": "hello world"}}
        )
    )

    result = bundle.sdk.libraries.get_file(path="docs/readme.md")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "docs/readme.md"}

    assert result.file is not None
    assert result.file.path == "docs/readme.md"
    assert result.file.content == "hello world"


@pytest.mark.asyncio
async def test_get_file_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"file": {"path": "docs/readme-async.md", "content": "hello async"}}
        )
    )

    result = await bundle.sdk.libraries.get_file_async(path="docs/readme-async.md")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "docs/readme-async.md"}

    assert result.file is not None
    assert result.file.path == "docs/readme-async.md"


def test_get_file_omits_path_when_not_passed(make_sdk):
    # `path` is a plain Optional[str] and is in optional_fields, so when left
    # at its default None it is omitted from the JSON body entirely.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_file()

    body = bundle.transport.body_json()
    assert body == {}


def test_get_file_unicode_and_special_char_path(make_sdk):
    tricky_path = "文件/path with spaces/emoji😀.txt"
    bundle = make_sdk(lambda req: json_response(200, {"file": {"path": tricky_path}}))

    result = bundle.sdk.libraries.get_file(path=tricky_path)

    body = bundle.transport.body_json()
    assert body == {"path": tricky_path}
    assert result.file.path == tricky_path


@pytest.mark.parametrize("status_code", [400, 404, 422, 500, 503])
def test_get_file_error_statuses_raise_textql_default_error(make_sdk, status_code):
    bundle = make_sdk(
        lambda req: json_response(status_code, {"message": "boom"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.get_file(path="does/not/exist.txt")

    assert exc_info.value.status_code == status_code
    assert "boom" in exc_info.value.body


@pytest.mark.asyncio
async def test_get_file_async_error_status_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.get_file_async(path="missing.txt")

    assert exc_info.value.status_code == 404
    assert "not found" in exc_info.value.body


# ---------------------------------------------------------------------------
# upsert_library_file / upsert_library_file_async  (deep-dive operation)
# ---------------------------------------------------------------------------


def test_upsert_library_file_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"file": {"path": "notes/a.txt"}})
    )

    result = bundle.sdk.libraries.upsert_library_file(
        path="notes/a.txt", content="line one", commit_message="add a.txt"
    )

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpsertLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "notes/a.txt",
        "content": "line one",
        "commitMessage": "add a.txt",
    }
    assert result.file is not None
    assert result.file.path == "notes/a.txt"


@pytest.mark.asyncio
async def test_upsert_library_file_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"file": {"path": "notes/b.txt"}})
    )

    result = await bundle.sdk.libraries.upsert_library_file_async(
        path="notes/b.txt", content="line two", commit_message="add b.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpsertLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "notes/b.txt",
        "content": "line two",
        "commitMessage": "add b.txt",
    }
    assert result.file.path == "notes/b.txt"


@pytest.mark.parametrize("status_code", [400, 403, 409, 500, 502])
def test_upsert_library_file_error_statuses(make_sdk, status_code):
    bundle = make_sdk(lambda req: json_response(status_code, {"message": "denied"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.upsert_library_file(path="x.txt", content="y")

    assert exc_info.value.status_code == status_code
    assert "denied" in exc_info.value.body


@pytest.mark.asyncio
async def test_upsert_library_file_async_error_status(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.upsert_library_file_async(
            path="x.txt", content="y"
        )

    assert exc_info.value.status_code == 500
    assert "server error" in exc_info.value.body


def test_upsert_library_file_commit_message_unset_is_absent(make_sdk):
    # commit_message is OptionalNullable[str] = UNSET by default. When the
    # kwarg is never passed, it stays UNSET (the UNSET sentinel), which the
    # model_serializer always excludes ("val != UNSET_SENTINEL" guard) -- so
    # the key must be completely absent from the JSON body.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_library_file(path="x.txt", content="y")

    body = bundle.transport.body_json()
    assert "commitMessage" not in body
    assert body == {"path": "x.txt", "content": "y"}


def test_upsert_library_file_commit_message_explicit_value_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_library_file(
        path="x.txt", content="y", commit_message="explicit message"
    )

    body = bundle.transport.body_json()
    assert body["commitMessage"] == "explicit message"


def test_upsert_library_file_commit_message_explicit_none_is_null(make_sdk):
    # commit_message is in nullable_fields, so when explicitly passed as None
    # (a real, distinct value from omission/UNSET) it must serialize to JSON
    # null rather than being omitted.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_library_file(
        path="x.txt", content="y", commit_message=None
    )

    body = bundle.transport.body_json()
    assert "commitMessage" in body
    assert body["commitMessage"] is None


def test_upsert_library_file_unicode_path_and_content(make_sdk):
    tricky_path = "文件/path with spaces/emoji😀.txt"
    tricky_content = "内容 with spaces and emoji 🎉 and \n newlines \t tabs"
    bundle = make_sdk(lambda req: json_response(200, {"file": {"path": tricky_path}}))

    result = bundle.sdk.libraries.upsert_library_file(
        path=tricky_path, content=tricky_content
    )

    body = bundle.transport.body_json()
    assert body["path"] == tricky_path
    assert body["content"] == tricky_content
    assert result.file.path == tricky_path


def test_upsert_library_file_empty_string_path(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"file": {"path": ""}}))

    bundle.sdk.libraries.upsert_library_file(path="", content="some content")

    body = bundle.transport.body_json()
    # Empty string is not None, so it must still be included (not omitted).
    assert body["path"] == ""


def test_upsert_library_file_large_content_payload(make_sdk):
    large_content = "A" * 2_000_000  # 2 MB of content
    bundle = make_sdk(lambda req: json_response(200, {"file": {"path": "big.txt"}}))

    bundle.sdk.libraries.upsert_library_file(path="big.txt", content=large_content)

    body = bundle.transport.body_json()
    assert len(body["content"]) == 2_000_000
    assert body["content"] == large_content


# ---------------------------------------------------------------------------
# delete_library_file / delete_library_file_async
# ---------------------------------------------------------------------------


def test_delete_library_file_sync_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.delete_library_file(
        path="notes/a.txt", commit_message="remove a.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "notes/a.txt", "commitMessage": "remove a.txt"}


@pytest.mark.asyncio
async def test_delete_library_file_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.libraries.delete_library_file_async(
        path="notes/b.txt", commit_message="remove b.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "notes/b.txt", "commitMessage": "remove b.txt"}


def test_delete_library_file_response_is_google_protobuf_empty(make_sdk):
    # Response model is GoogleProtobufEmpty for a 200 -- just assert it
    # unmarshals without raising.
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.libraries.delete_library_file(path="notes/a.txt")

    assert result is not None


# ---------------------------------------------------------------------------
# rename_file / rename_file_async
# ---------------------------------------------------------------------------


def test_rename_file_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"file": {"path": "notes/new.txt"}})
    )

    result = bundle.sdk.libraries.rename_file(
        old_path="notes/old.txt",
        new_path="notes/new.txt",
        commit_message="rename",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RenameLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "oldPath": "notes/old.txt",
        "newPath": "notes/new.txt",
        "commitMessage": "rename",
    }
    assert result.file.path == "notes/new.txt"


@pytest.mark.asyncio
async def test_rename_file_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"file": {"path": "notes/new-async.txt"}})
    )

    result = await bundle.sdk.libraries.rename_file_async(
        old_path="notes/old-async.txt",
        new_path="notes/new-async.txt",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RenameLibraryFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "oldPath": "notes/old-async.txt",
        "newPath": "notes/new-async.txt",
    }
    assert "commitMessage" not in body
    assert result.file.path == "notes/new-async.txt"


# ---------------------------------------------------------------------------
# create_library_directory / create_library_directory_async
# ---------------------------------------------------------------------------


def test_create_library_directory_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"entry": {"path": "newdir", "is_dir": True}})
    )

    result = bundle.sdk.libraries.create_library_directory(
        path="newdir", commit_message="mkdir"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateLibraryDirectory"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "newdir", "commitMessage": "mkdir"}
    assert result.entry is not None
    assert result.entry.path == "newdir"


@pytest.mark.asyncio
async def test_create_library_directory_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"entry": {"path": "newdir-async"}})
    )

    result = await bundle.sdk.libraries.create_library_directory_async(
        path="newdir-async"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateLibraryDirectory"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "newdir-async"}
    assert result.entry.path == "newdir-async"


# ---------------------------------------------------------------------------
# delete_library_directory / delete_library_directory_async
# ---------------------------------------------------------------------------


def test_delete_library_directory_sync_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.delete_library_directory(
        path="olddir", commit_message="rmdir", recursive=True
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteLibraryDirectory"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "olddir",
        "commitMessage": "rmdir",
        "recursive": True,
    }


@pytest.mark.asyncio
async def test_delete_library_directory_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.libraries.delete_library_directory_async(
        path="olddir-async", recursive=False
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteLibraryDirectory"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "olddir-async", "recursive": False}


# ---------------------------------------------------------------------------
# list_library_entries / list_library_entries_async
# ---------------------------------------------------------------------------


def test_list_library_entries_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"entries": [{"path": "a.txt"}, {"path": "b.txt", "is_dir": False}]}
        )
    )

    result = bundle.sdk.libraries.list_library_entries(
        path="", recursive=True, include_debug_files=True
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListLibraryEntries"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    # Empty string is not None, so `path` is still included (only a real
    # None is omitted for plain optional fields).
    assert body == {"path": "", "recursive": True, "includeDebugFiles": True}

    assert result.entries is not None
    assert len(result.entries) == 2


@pytest.mark.asyncio
async def test_list_library_entries_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"entries": []}))

    result = await bundle.sdk.libraries.list_library_entries_async(
        path="subdir", include_debug_files=False
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListLibraryEntries"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "subdir", "includeDebugFiles": False}
    assert result.entries == []


def test_list_library_entries_recursive_explicit_none_is_null(make_sdk):
    # `recursive` is OptionalNullable[bool] on this operation -- explicit None
    # should serialize as JSON null, distinct from omission.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_library_entries(path="dir", recursive=None)

    body = bundle.transport.body_json()
    assert "recursive" in body
    assert body["recursive"] is None


def test_list_library_entries_recursive_omitted_is_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_library_entries(path="dir")

    body = bundle.transport.body_json()
    assert "recursive" not in body


# ---------------------------------------------------------------------------
# create_file_upload_url / create_file_upload_url_async  (deep-dive operation)
# ---------------------------------------------------------------------------


def test_create_file_upload_url_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "upload_url": "https://uploads.example.invalid/abc",
                "upload_key": "key-123",
            },
        )
    )

    result = bundle.sdk.libraries.create_file_upload_url(
        path="big/file.bin", mime_type="application/octet-stream", size_bytes=1024
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateLibraryFileUploadUrl"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "big/file.bin",
        "mimeType": "application/octet-stream",
        "sizeBytes": 1024,
    }
    assert result.upload_url == "https://uploads.example.invalid/abc"
    assert result.upload_key == "key-123"


@pytest.mark.asyncio
async def test_create_file_upload_url_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "upload_url": "https://uploads.example.invalid/async",
                "upload_key": "key-async-123",
            },
        )
    )

    result = await bundle.sdk.libraries.create_file_upload_url_async(
        path="big/file-async.bin",
        mime_type="text/plain",
        size_bytes="2048",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateLibraryFileUploadUrl"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "big/file-async.bin",
        "mimeType": "text/plain",
        "sizeBytes": "2048",
    }
    assert result.upload_key == "key-async-123"


@pytest.mark.parametrize("status_code", [400, 401, 413, 500, 503])
def test_create_file_upload_url_error_statuses(make_sdk, status_code):
    bundle = make_sdk(lambda req: json_response(status_code, {"message": "no upload"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.create_file_upload_url(path="x.bin")

    assert exc_info.value.status_code == status_code
    assert "no upload" in exc_info.value.body


@pytest.mark.asyncio
async def test_create_file_upload_url_async_error_status(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.create_file_upload_url_async(path="x.bin")

    assert exc_info.value.status_code == 500


def test_create_file_upload_url_size_bytes_omitted_when_not_passed(make_sdk):
    # size_bytes here is a plain Optional[Union[int, str]] (not
    # OptionalNullable), and is in optional_fields, so omitting the kwarg
    # (None) causes the key to be dropped from the JSON body entirely.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.create_file_upload_url(path="x.bin", mime_type="text/plain")

    body = bundle.transport.body_json()
    assert "sizeBytes" not in body
    assert body == {"path": "x.bin", "mimeType": "text/plain"}


def test_create_file_upload_url_unicode_path(make_sdk):
    tricky_path = "文件/path with spaces/emoji😀.bin"
    bundle = make_sdk(
        lambda req: json_response(200, {"upload_url": "u", "upload_key": "k"})
    )

    bundle.sdk.libraries.create_file_upload_url(path=tricky_path)

    body = bundle.transport.body_json()
    assert body["path"] == tricky_path


# ---------------------------------------------------------------------------
# finalize_file_upload / finalize_file_upload_async  (deep-dive operation)
# ---------------------------------------------------------------------------


def test_finalize_file_upload_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"file": {"path": "big/file.bin"}})
    )

    result = bundle.sdk.libraries.finalize_file_upload(
        path="big/file.bin",
        upload_key="key-123",
        commit_message="finalize upload",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/FinalizeLibraryFileUpload"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "path": "big/file.bin",
        "uploadKey": "key-123",
        "commitMessage": "finalize upload",
    }
    assert result.file.path == "big/file.bin"


@pytest.mark.asyncio
async def test_finalize_file_upload_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"file": {"path": "big/file-async.bin"}})
    )

    result = await bundle.sdk.libraries.finalize_file_upload_async(
        path="big/file-async.bin", upload_key="key-async-123"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/FinalizeLibraryFileUpload"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "big/file-async.bin", "uploadKey": "key-async-123"}
    assert "commitMessage" not in body
    assert result.file.path == "big/file-async.bin"


@pytest.mark.parametrize("status_code", [400, 404, 409, 500, 504])
def test_finalize_file_upload_error_statuses(make_sdk, status_code):
    bundle = make_sdk(
        lambda req: json_response(status_code, {"message": "finalize failed"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.finalize_file_upload(
            path="x.bin", upload_key="key-x"
        )

    assert exc_info.value.status_code == status_code
    assert "finalize failed" in exc_info.value.body


@pytest.mark.asyncio
async def test_finalize_file_upload_async_error_status(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "bad key"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.finalize_file_upload_async(
            path="x.bin", upload_key="bad-key"
        )

    assert exc_info.value.status_code == 422
    assert "bad key" in exc_info.value.body


def test_finalize_file_upload_commit_message_unset_is_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.finalize_file_upload(path="x.bin", upload_key="key-x")

    body = bundle.transport.body_json()
    assert "commitMessage" not in body


def test_finalize_file_upload_commit_message_explicit_value_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.finalize_file_upload(
        path="x.bin", upload_key="key-x", commit_message="explicit"
    )

    body = bundle.transport.body_json()
    assert body["commitMessage"] == "explicit"


def test_finalize_file_upload_commit_message_explicit_none_is_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.finalize_file_upload(
        path="x.bin", upload_key="key-x", commit_message=None
    )

    body = bundle.transport.body_json()
    assert "commitMessage" in body
    assert body["commitMessage"] is None


def test_finalize_file_upload_unicode_path(make_sdk):
    tricky_path = "文件/path with spaces/emoji😀.bin"
    bundle = make_sdk(lambda req: json_response(200, {"file": {"path": tricky_path}}))

    bundle.sdk.libraries.finalize_file_upload(path=tricky_path, upload_key="k")

    body = bundle.transport.body_json()
    assert body["path"] == tricky_path


def test_finalize_file_upload_empty_string_path(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"file": {"path": ""}}))

    bundle.sdk.libraries.finalize_file_upload(path="", upload_key="k")

    body = bundle.transport.body_json()
    assert body["path"] == ""


# ---------------------------------------------------------------------------
# get_file_usage / get_file_usage_async
# ---------------------------------------------------------------------------


def test_get_file_usage_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "files": [{"path": "a.txt"}],
                "next_page_cursor": "cursor-1",
            },
        )
    )

    result = bundle.sdk.libraries.get_file_usage(
        path_prefix="notes/", page_size=25
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetFileUsage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"pathPrefix": "notes/", "pageSize": 25}
    assert result.files is not None
    assert result.next_page_cursor == "cursor-1"


@pytest.mark.asyncio
async def test_get_file_usage_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"files": []}))

    result = await bundle.sdk.libraries.get_file_usage_async(
        page_cursor="cursor-in", page_size=10
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetFileUsage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"pageCursor": "cursor-in", "pageSize": 10}
    assert result.files == []


def test_get_file_usage_path_prefix_explicit_none_is_null(make_sdk):
    # path_prefix is OptionalNullable[str] -- explicit None must serialize
    # to JSON null.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_file_usage(path_prefix=None)

    body = bundle.transport.body_json()
    assert "pathPrefix" in body
    assert body["pathPrefix"] is None


def test_get_file_usage_all_fields_omitted_when_unset(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_file_usage()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# get_file_usage_timeline / get_file_usage_timeline_async
# ---------------------------------------------------------------------------


def test_get_file_usage_timeline_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "days": [
                    {"date": {"year": 2026, "month": 7, "day": 1}}
                ]
            },
        )
    )

    result = bundle.sdk.libraries.get_file_usage_timeline(path_prefix="notes/")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetFileUsageTimeline"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"pathPrefix": "notes/"}
    assert result.days is not None
    assert len(result.days) == 1


@pytest.mark.asyncio
async def test_get_file_usage_timeline_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"days": []}))

    result = await bundle.sdk.libraries.get_file_usage_timeline_async()

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetFileUsageTimeline"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}
    assert result.days == []


# ---------------------------------------------------------------------------
# get_usage_details_for_file / get_usage_details_for_file_async
# ---------------------------------------------------------------------------


def test_get_usage_details_for_file_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"last_used": "2026-07-01T00:00:00Z", "days": []}
        )
    )

    result = bundle.sdk.libraries.get_usage_details_for_file(
        file_path="notes/a.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetUsageDetailsForFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"filePath": "notes/a.txt"}
    assert result.days == []


@pytest.mark.asyncio
async def test_get_usage_details_for_file_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.libraries.get_usage_details_for_file_async(
        file_path="notes/b.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetUsageDetailsForFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"filePath": "notes/b.txt"}
    assert result is not None


def test_get_usage_details_for_file_omits_file_path_when_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_usage_details_for_file()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# list_chats_for_file / list_chats_for_file_async
# ---------------------------------------------------------------------------


def test_list_chats_for_file_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"chats": [{"chat_id": "chat-1"}]})
    )

    result = bundle.sdk.libraries.list_chats_for_file(
        file_path="notes/a.txt", limit=5
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListChatsForFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"filePath": "notes/a.txt", "limit": 5}
    assert result.chats is not None
    assert len(result.chats) == 1


@pytest.mark.asyncio
async def test_list_chats_for_file_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chats": []}))

    result = await bundle.sdk.libraries.list_chats_for_file_async(
        file_path="notes/b.txt"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListChatsForFile"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"filePath": "notes/b.txt"}
    assert result.chats == []


def test_list_chats_for_file_limit_explicit_none_is_null(make_sdk):
    # limit is OptionalNullable[int] -- explicit None must serialize to null.
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_chats_for_file(file_path="notes/a.txt", limit=None)

    body = bundle.transport.body_json()
    assert "limit" in body
    assert body["limit"] is None


def test_list_chats_for_file_limit_omitted_is_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.list_chats_for_file(file_path="notes/a.txt")

    body = bundle.transport.body_json()
    assert "limit" not in body
