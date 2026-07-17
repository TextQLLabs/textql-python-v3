"""Unit tests for the LibraryService (sdk.library_service)."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, utils

LIB_PATH = "/textql.rpc.public.patches.LibraryService"


# ---------------------------------------------------------------------------
# library_service_list_golden_files / _async
# ---------------------------------------------------------------------------


def test_list_golden_files_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "golden": [
                    {
                        "path": "queries/foo.sql",
                        "setByMemberId": "member-1",
                        "setAt": "2024-01-01T00:00:00Z",
                    }
                ]
            },
        )
    )

    result = bundle.sdk.library_service.library_service_list_golden_files(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListGoldenFiles"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    # The request model has zero fields, so the serialized body is always {}.
    assert body == {}

    assert len(result.golden) == 1
    assert result.golden[0].path == "queries/foo.sql"
    assert result.golden[0].set_by_member_id == "member-1"


def test_list_golden_files_empty_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    result = bundle.sdk.library_service.library_service_list_golden_files(body={})

    assert result.golden == []


@pytest.mark.asyncio
async def test_list_golden_files_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    result = await bundle.sdk.library_service.library_service_list_golden_files_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListGoldenFiles"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {}
    assert result.golden == []


def test_list_golden_files_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.library_service.library_service_list_golden_files(body={})

    assert exc_info.value.status_code == 404


def test_list_golden_files_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.library_service.library_service_list_golden_files(body={})

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_list_golden_files_async_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.library_service.library_service_list_golden_files_async(body={})

    assert exc_info.value.status_code == 401


@pytest.mark.asyncio
async def test_list_golden_files_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.library_service.library_service_list_golden_files_async(body={})

    assert exc_info.value.status_code == 503


def test_list_golden_files_retries_backoff_eventually_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"golden": []}),
        ]
    )
    bundle = make_sdk(handler)

    retries = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=True,
    )

    result = bundle.sdk.library_service.library_service_list_golden_files(
        body={}, retries=retries
    )

    assert len(bundle.transport.requests) == 2
    assert result.golden == []


def test_list_golden_files_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    override_url = "https://override.invalid"
    bundle.sdk.library_service.library_service_list_golden_files(
        body={}, server_url=override_url
    )

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_list_golden_files_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    bundle.sdk.library_service.library_service_list_golden_files(
        body={}, http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


# ---------------------------------------------------------------------------
# library_service_set_library_file_golden / _async
# ---------------------------------------------------------------------------


def test_set_library_file_golden_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "golden": [
                    {"path": "queries/foo.sql", "setByMemberId": "member-1"},
                ]
            },
        )
    )

    result = bundle.sdk.library_service.library_service_set_library_file_golden(
        path="queries/foo.sql", golden=True
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/SetLibraryFileGolden"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "queries/foo.sql", "golden": True}
    assert result.golden[0].path == "queries/foo.sql"


def test_set_library_file_golden_retire(make_sdk):
    """golden=False retires (per the docstring 'true = certify, false =
    retire'); ensure `False` is not dropped as falsy during serialization."""
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    bundle.sdk.library_service.library_service_set_library_file_golden(
        path="queries/bar.sql", golden=False
    )

    body = bundle.transport.body_json()
    assert body == {"path": "queries/bar.sql", "golden": False}


@pytest.mark.asyncio
async def test_set_library_file_golden_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    result = await bundle.sdk.library_service.library_service_set_library_file_golden_async(
        path="queries/baz.sql", golden=True
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/SetLibraryFileGolden"
    body = bundle.transport.body_json()
    assert body == {"path": "queries/baz.sql", "golden": True}
    assert result.golden == []


def test_set_library_file_golden_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad path"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.library_service.library_service_set_library_file_golden(
            path="bad", golden=True
        )

    assert exc_info.value.status_code == 400


def test_set_library_file_golden_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.library_service.library_service_set_library_file_golden(
            path="x", golden=True
        )

    assert exc_info.value.status_code == 502


@pytest.mark.asyncio
async def test_set_library_file_golden_async_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.library_service.library_service_set_library_file_golden_async(
            path="missing", golden=True
        )

    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_set_library_file_golden_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.library_service.library_service_set_library_file_golden_async(
            path="x", golden=True
        )

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_set_library_file_golden_async_retries_backoff_eventually_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(502, {"message": "temporary failure"}),
            json_response(200, {"golden": []}),
        ]
    )
    bundle = make_sdk(handler)

    retries = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=True,
    )

    result = await bundle.sdk.library_service.library_service_set_library_file_golden_async(
        path="queries/retry.sql", golden=True, retries=retries
    )

    assert len(bundle.transport.requests) == 2
    assert result.golden == []


def test_set_library_file_golden_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    override_url = "https://override.invalid"
    bundle.sdk.library_service.library_service_set_library_file_golden(
        path="x", golden=True, server_url=override_url
    )

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_set_library_file_golden_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    bundle.sdk.library_service.library_service_set_library_file_golden(
        path="x", golden=True, http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_set_library_file_golden_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"golden": []}))

    result = bundle.sdk.library_service.library_service_set_library_file_golden(
        path="x", golden=True, timeout_ms=5000
    )

    assert bundle.transport.last_request.url.path == f"{LIB_PATH}/SetLibraryFileGolden"
    assert result.golden == []
