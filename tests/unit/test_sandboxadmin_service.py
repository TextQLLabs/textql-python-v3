"""Unit tests for the SandboxAdmin service (sdk.sandbox_admin)."""
import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response

BASE_PATH = "/textql.rpc.public.sandbox_admin.SandboxAdminService"


def _tiny_backoff(**overrides):
    kwargs = dict(
        initial_interval=1,
        max_interval=5,
        exponent=1.0,
        max_elapsed_time=5000,
    )
    kwargs.update(overrides)
    return utils.BackoffStrategy(**kwargs)


def _retry_config():
    return utils.RetryConfig(
        strategy="backoff",
        backoff=_tiny_backoff(),
        retry_connection_errors=True,
    )


# ---------------------------------------------------------------------------
# get_sandbox
# ---------------------------------------------------------------------------


def test_get_sandbox_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "sandbox": {"sandboxId": "sb-1", "status": "running"},
                "liveAvailable": True,
                "memoryUsageBytes": 1024,
            },
        )
    )

    resp = bundle.sdk.sandbox_admin.get_sandbox(sandbox_id="sb-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetSandbox"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"

    assert resp.sandbox.sandbox_id == "sb-1"
    assert resp.sandbox.status == "running"
    assert resp.live_available is True
    assert resp.memory_usage_bytes == 1024


def test_get_sandbox_memory_usage_bytes_string_variant(make_sdk):
    # memory_usage_bytes is Union[int, str] per the model.
    bundle = make_sdk(lambda req: json_response(200, {"memoryUsageBytes": "unknown"}))
    resp = bundle.sdk.sandbox_admin.get_sandbox(sandbox_id="sb-1")
    assert resp.memory_usage_bytes == "unknown"


@pytest.mark.asyncio
async def test_get_sandbox_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"liveAvailable": False}))
    resp = await bundle.sdk.sandbox_admin.get_sandbox_async(sandbox_id="sb-2")

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-2"
    assert resp.live_available is False


def test_get_sandbox_no_sandbox_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.get_sandbox()
    body = bundle.transport.body_json()
    assert "sandboxId" not in body


def test_get_sandbox_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.get_sandbox(sandbox_id="missing")
    assert exc_info.value.status_code == 404


def test_get_sandbox_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.get_sandbox(sandbox_id="sb-1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_get_sandbox_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.sandbox_admin.get_sandbox_async(sandbox_id="sb-1")
    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# list (ListSandboxes)
# ---------------------------------------------------------------------------


def test_list_sandboxes_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "sandboxes": [{"sandboxId": "sb-1"}, {"sandboxId": "sb-2"}],
                "nextCursor": "cursor-1",
            },
        )
    )

    resp = bundle.sdk.sandbox_admin.list(status="running", limit=10, cursor="c0")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListSandboxes"

    body = bundle.transport.body_json()
    assert body["status"] == "running"
    assert body["limit"] == 10
    assert body["cursor"] == "c0"

    assert len(resp.sandboxes) == 2
    assert resp.sandboxes[0].sandbox_id == "sb-1"
    assert resp.next_cursor == "cursor-1"


def test_list_sandboxes_optional_fields_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list()
    body = bundle.transport.body_json()
    assert body == {}


@pytest.mark.asyncio
async def test_list_sandboxes_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"sandboxes": []}))
    resp = await bundle.sdk.sandbox_admin.list_async(status="all")
    body = bundle.transport.body_json()
    assert body["status"] == "all"
    assert resp.sandboxes == []


def test_list_sandboxes_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.list()
    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# list_executions (ListSandboxExecutions)
# ---------------------------------------------------------------------------


def test_list_executions_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list_executions(
        sandbox_id="sb-1", limit=5, cursor="cur"
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListSandboxExecutions"
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"
    assert body["limit"] == 5
    assert body["cursor"] == "cur"


@pytest.mark.asyncio
async def test_list_executions_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.sandbox_admin.list_executions_async(sandbox_id="sb-1")
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"
    assert "limit" not in body
    assert "cursor" not in body


def test_list_executions_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.list_executions(sandbox_id="sb-1")
    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# list_sandbox_egress (ListSandboxEgress)
# ---------------------------------------------------------------------------


def test_list_sandbox_egress_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list_sandbox_egress(sandbox_id="sb-1", limit=25)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListSandboxEgress"
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"
    assert body["limit"] == 25


@pytest.mark.asyncio
async def test_list_sandbox_egress_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.sandbox_admin.list_sandbox_egress_async(sandbox_id="sb-1")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"
    assert "limit" not in body


def test_list_sandbox_egress_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.list_sandbox_egress(sandbox_id="sb-1")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_sandbox_files (ListSandboxFiles) -- path handling, incl. traversal-like
# ---------------------------------------------------------------------------


def test_list_sandbox_files_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "available": True,
                "entries": [{"name": "a.txt", "isDir": False}],
            },
        )
    )
    resp = bundle.sdk.sandbox_admin.list_sandbox_files(sandbox_id="sb-1", path="dir")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListSandboxFiles"
    body = bundle.transport.body_json()
    assert body["path"] == "dir"
    assert resp.available is True
    assert len(resp.entries) == 1
    assert resp.entries[0].name == "a.txt"


def test_list_sandbox_files_empty_path_means_root(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list_sandbox_files(sandbox_id="sb-1", path="")
    body = bundle.transport.body_json()
    # path is a plain Optional[str] field (not OptionalNullable), and the
    # model's serializer only omits a field when its value is None -- an
    # explicit "" is a real value, so it IS included in the serialized body
    # (as opposed to OptionalNullable fields, which additionally distinguish
    # "unset" from "explicitly set to null"). This documents actual behavior.
    assert body["path"] == ""


def test_list_sandbox_files_path_traversal_string_passed_through_verbatim(make_sdk):
    # The SDK does zero client-side path validation/sanitization -- it should
    # pass whatever string is given straight through as request body data.
    # This documents that expected behavior; it is not a bug for the SDK
    # (a thin transport layer) to do this -- validation is a server concern.
    traversal = "../../etc/passwd"
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list_sandbox_files(sandbox_id="sb-1", path=traversal)

    body = bundle.transport.body_json()
    assert body["path"] == traversal

    # Also confirm it isn't double-encoded or altered in the raw request body
    # bytes (which would indicate a serialization bug).
    raw = bundle.transport.last_request.content.decode("utf-8")
    assert traversal in raw
    assert "%2e%2e" not in raw.lower()  # no unexpected URL-encoding of body JSON


def test_list_sandbox_files_path_with_null_bytes_and_unicode(make_sdk):
    tricky = "../☃/dir\x00name"
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list_sandbox_files(sandbox_id="sb-1", path=tricky)
    body = bundle.transport.body_json()
    assert body["path"] == tricky


@pytest.mark.asyncio
async def test_list_sandbox_files_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"available": False}))
    resp = await bundle.sdk.sandbox_admin.list_sandbox_files_async(
        sandbox_id="sb-1", path="../secret"
    )
    body = bundle.transport.body_json()
    assert body["path"] == "../secret"
    assert resp.available is False


def test_list_sandbox_files_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no sandbox"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.list_sandbox_files(sandbox_id="missing")
    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# list_sandbox_spend (ListSandboxSpend)
# ---------------------------------------------------------------------------


def test_list_sandbox_spend_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list_sandbox_spend(sandbox_id="sb-1")
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListSandboxSpend"
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"


@pytest.mark.asyncio
async def test_list_sandbox_spend_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.sandbox_admin.list_sandbox_spend_async(sandbox_id="sb-1")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_list_sandbox_spend_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.list_sandbox_spend(sandbox_id="sb-1")
    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# read_file (ReadSandboxFile) -- content vs binary_content handling
# ---------------------------------------------------------------------------


def test_read_file_text_content(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "available": True,
                "name": "notes.txt",
                "sizeBytes": 42,
                "mimeType": "text/plain",
                "content": "hello world",
                "isBinary": False,
            },
        )
    )
    resp = bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="notes.txt")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ReadSandboxFile"
    body = bundle.transport.body_json()
    assert body["path"] == "notes.txt"

    assert resp.content == "hello world"
    assert resp.binary_content is None
    assert resp.is_binary is False
    assert resp.size_bytes == 42
    assert resp.mime_type == "text/plain"


def test_read_file_binary_content_variant(make_sdk):
    # Binary files: `content` is empty/absent, `binary_content` carries the
    # payload (presumably base64-encoded by the server -- the SDK treats it
    # as an opaque string either way, no decoding performed client-side).
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "available": True,
                "name": "image.png",
                "mimeType": "image/png",
                "binaryContent": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB",
                "isBinary": True,
            },
        )
    )
    resp = bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="image.png")

    assert resp.is_binary is True
    assert resp.binary_content == "iVBORw0KGgoAAAANSUhEUgAAAAEAAAAB"
    assert resp.content is None
    # The SDK must not attempt to base64-decode or otherwise transform this
    # value -- it should come through completely opaque/untouched.


def test_read_file_size_bytes_string_variant(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"sizeBytes": "huge"}))
    resp = bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="f")
    assert resp.size_bytes == "huge"


def test_read_file_truncated_flag(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"truncated": True}))
    resp = bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="big.log")
    assert resp.truncated is True


def test_read_file_not_available_when_sandbox_stopped(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"available": False}))
    resp = bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="f")
    assert resp.available is False


def test_read_file_path_traversal_string_passed_through_verbatim(make_sdk):
    traversal = "../../etc/passwd"
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path=traversal)
    body = bundle.transport.body_json()
    assert body["path"] == traversal


@pytest.mark.asyncio
async def test_read_file_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"content": "abc"}))
    resp = await bundle.sdk.sandbox_admin.read_file_async(
        sandbox_id="sb-1", path="f.txt"
    )
    body = bundle.transport.body_json()
    assert body["path"] == "f.txt"
    assert resp.content == "abc"


def test_read_file_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "file not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="missing.txt")
    assert exc_info.value.status_code == 404


def test_read_file_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="f.txt")
    assert exc_info.value.status_code == 500


def test_read_file_unexpected_non_json_status_raises(make_sdk):
    # A 304 with a text/plain body isn't handled by any branch (200 JSON,
    # 4XX, 5XX, default JSON) -- confirm it falls through to the final raise.
    bundle = make_sdk(lambda req: text_response(304, ""))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.sandbox_admin.read_file(sandbox_id="sb-1", path="f.txt")


# ---------------------------------------------------------------------------
# restart_sandbox (RestartSandbox)
# ---------------------------------------------------------------------------


def test_restart_sandbox_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.restart_sandbox(sandbox_id="sb-1")
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RestartSandbox"
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"


@pytest.mark.asyncio
async def test_restart_sandbox_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.sandbox_admin.restart_sandbox_async(sandbox_id="sb-1")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_restart_sandbox_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.restart_sandbox(sandbox_id="sb-1")
    assert exc_info.value.status_code == 409


# ---------------------------------------------------------------------------
# stop (StopSandbox)
# ---------------------------------------------------------------------------


def test_stop_sandbox_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.stop(sandbox_id="sb-1")
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/StopSandbox"
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"


@pytest.mark.asyncio
async def test_stop_sandbox_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.sandbox_admin.stop_async(sandbox_id="sb-1")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["sandboxId"] == "sb-1"


def test_stop_sandbox_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.stop(sandbox_id="sb-1")
    assert exc_info.value.status_code == 403


def test_stop_sandbox_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.stop(sandbox_id="sb-1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_stop_sandbox_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.sandbox_admin.stop_async(sandbox_id="sb-1")
    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# Retries (representative subset: get_sandbox, list_sandbox_files)
# ---------------------------------------------------------------------------


def test_get_sandbox_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {"liveAvailable": True}),
        ]
    )
    bundle = make_sdk(handler)

    resp = bundle.sdk.sandbox_admin.get_sandbox(
        sandbox_id="sb-1", retries=_retry_config()
    )

    assert resp.live_available is True
    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_list_sandbox_files_async_retries_on_500_then_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {"available": True}),
        ]
    )
    bundle = make_sdk(handler)

    resp = await bundle.sdk.sandbox_admin.list_sandbox_files_async(
        sandbox_id="sb-1", path="dir", retries=_retry_config()
    )

    assert resp.available is True
    assert len(bundle.transport.requests) == 2


def test_stop_sandbox_retries_exhausted_raises(make_sdk):
    # Every attempt fails with 500; with a tiny max_elapsed_time the retry
    # loop should give up quickly and surface the last error response.
    bundle = make_sdk(lambda req: json_response(500, {"message": "persistent failure"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox_admin.stop(sandbox_id="sb-1", retries=_retry_config())
    assert exc_info.value.status_code == 500
    # Confirm it actually retried more than once before giving up.
    assert len(bundle.transport.requests) >= 2


# ---------------------------------------------------------------------------
# Per-call overrides
# ---------------------------------------------------------------------------


def test_get_sandbox_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.get_sandbox(
        sandbox_id="sb-1", server_url="https://override.invalid"
    )
    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override.invalid")


def test_list_sandbox_files_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.list_sandbox_files(
        sandbox_id="sb-1",
        path="dir",
        http_headers={"X-Custom-Header": "custom-value"},
    )
    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_read_file_timeout_ms_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"content": "x"}))
    resp = bundle.sdk.sandbox_admin.read_file(
        sandbox_id="sb-1", path="f", timeout_ms=15000
    )
    assert resp.content == "x"


def test_get_sandbox_connect_timeout_ms_header(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox_admin.get_sandbox(sandbox_id="sb-1", connect_timeout_ms=2500.0)
    req = bundle.transport.last_request
    assert req.headers.get("Connect-Timeout-Ms") in ("2500.0", "2500")
