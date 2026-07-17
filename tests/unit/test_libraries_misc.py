"""Unit tests for miscellaneous Libraries operations: get_size_timeline, list_imports, list_library_history, list_skills."""
from __future__ import annotations

from datetime import timedelta

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

LIB_PATH = "/textql.rpc.public.patches.LibraryService"


def _retry_config():
    return utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=False,
    )


# --------------------------------------------------------------------------
# get_size_timeline
# --------------------------------------------------------------------------


def test_get_size_timeline_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "days": [
                    {"date": {"year": 2026, "month": 7, "day": 1}, "totalBytes": "1024", "fileCount": 3}
                ]
            },
        )
    )

    result = bundle.sdk.libraries.get_size_timeline(
        observation_period=timedelta(days=3, minutes=10)
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/GetLibrarySizeTimeline"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    # pydantic serializes timedelta using ISO-8601 duration format.
    assert body == {"observationPeriod": "P3DT10M"}
    assert len(result.days) == 1
    assert result.days[0].file_count == 3


@pytest.mark.asyncio
async def test_get_size_timeline_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"days": []}))

    result = await bundle.sdk.libraries.get_size_timeline_async(
        observation_period=timedelta(days=1)
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/GetLibrarySizeTimeline"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"observationPeriod": "P1D"}
    assert result.days == []


def test_get_size_timeline_omits_unset_observation_period(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"days": []}))

    bundle.sdk.libraries.get_size_timeline()

    body = bundle.transport.body_json()
    assert body == {}


def test_get_size_timeline_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.get_size_timeline()

    assert exc_info.value.status_code == 404


def test_get_size_timeline_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.get_size_timeline()

    assert exc_info.value.status_code == 500


def test_get_size_timeline_connect_timeout_ms_header(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"days": []}))

    bundle.sdk.libraries.get_size_timeline(connect_timeout_ms=2500.0)

    req = bundle.transport.last_request
    assert req.headers.get("Connect-Timeout-Ms") in ("2500.0", "2500")


# --------------------------------------------------------------------------
# list_imports (empty request body model)
# --------------------------------------------------------------------------


def test_list_imports_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "imports": [
                    {
                        "sourcePath": "ontology/a.yaml",
                        "targetPath": "ontology/b.yaml",
                        "alias": "b",
                    }
                ]
            },
        )
    )

    result = bundle.sdk.libraries.list_imports(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListLibraryImports"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert len(result.imports) == 1
    assert result.imports[0].source_path == "ontology/a.yaml"


@pytest.mark.asyncio
async def test_list_imports_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"imports": []}))

    result = await bundle.sdk.libraries.list_imports_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListLibraryImports"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert result.imports == []


def test_list_imports_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.list_imports(body={})

    assert exc_info.value.status_code == 403


def test_list_imports_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.list_imports(body={})

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_library_history
# --------------------------------------------------------------------------


def test_list_library_history_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "history": [
                    {
                        "commitId": "abc123",
                        "committedAt": "2026-07-01T12:00:00Z",
                        "authorEmail": "rodney@textql.com",
                        "authorName": "Rodney",
                        "message": "update ontology",
                        "changedFiles": [
                            {"path": "ontology/a.yaml", "changeType": "MODIFIED"}
                        ],
                    }
                ],
                "nextPageToken": "page-2",
            },
        )
    )

    result = bundle.sdk.libraries.list_library_history(
        page_size=10, page_token="page-1", path="ontology/a.yaml"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListLibraryHistory"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "pageSize": 10,
        "pageToken": "page-1",
        "path": "ontology/a.yaml",
    }
    assert len(result.history) == 1
    assert result.history[0].commit_id == "abc123"
    assert result.next_page_token == "page-2"


@pytest.mark.asyncio
async def test_list_library_history_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"history": []}))

    result = await bundle.sdk.libraries.list_library_history_async(
        page_size=5, page_token="tok"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListLibraryHistory"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"pageSize": 5, "pageToken": "tok"}
    assert result.history == []


def test_list_library_history_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"history": []}))

    bundle.sdk.libraries.list_library_history()

    body = bundle.transport.body_json()
    assert body == {}


def test_list_library_history_explicit_null_path(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"history": []}))

    bundle.sdk.libraries.list_library_history(path=None)

    body = bundle.transport.body_json()
    assert body["path"] is None


def test_list_library_history_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.list_library_history()

    assert exc_info.value.status_code == 404


def test_list_library_history_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.list_library_history()

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_skills (empty request body model)
# --------------------------------------------------------------------------


def test_list_skills_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "skills": [
                    {
                        "trigger": "forecast",
                        "name": "Forecast",
                        "description": "Generates a forecast",
                        "path": "skills/forecast",
                    }
                ]
            },
        )
    )

    result = bundle.sdk.libraries.list_skills(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListSkills"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert len(result.skills) == 1
    assert result.skills[0].trigger == "forecast"


@pytest.mark.asyncio
async def test_list_skills_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"skills": []}))

    result = await bundle.sdk.libraries.list_skills_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{LIB_PATH}/ListSkills"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert result.skills == []


def test_list_skills_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.list_skills(body={})

    assert exc_info.value.status_code == 403


def test_list_skills_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.list_skills(body={})

    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# retries / server_url / http_headers / timeout_ms overrides
# --------------------------------------------------------------------------


def test_get_size_timeline_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "err"}),
            json_response(500, {"message": "err"}),
            json_response(200, {"days": []}),
        ]
    )
    bundle = make_sdk(handler)

    result = bundle.sdk.libraries.get_size_timeline(retries=_retry_config())

    assert result.days == []
    assert len(bundle.transport.requests) == 3
    for req in bundle.transport.requests:
        assert req.method == "POST"
        assert req.url.path == f"{LIB_PATH}/GetLibrarySizeTimeline"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


@pytest.mark.asyncio
async def test_list_library_history_retries_backoff_then_success_async(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(429, {"message": "rate limited"}),
            json_response(200, {"history": []}),
        ]
    )
    bundle = make_sdk(handler)

    result = await bundle.sdk.libraries.list_library_history_async(
        retries=_retry_config()
    )

    assert result.history == []
    assert len(bundle.transport.requests) == 2
    for req in bundle.transport.requests:
        assert req.method == "POST"
        assert req.url.path == f"{LIB_PATH}/ListLibraryHistory"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_list_skills_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(503, {"message": "unavailable"}),
            json_response(200, {"skills": []}),
        ]
    )
    bundle = make_sdk(handler)

    result = bundle.sdk.libraries.list_skills(body={}, retries=_retry_config())

    assert result.skills == []
    assert len(bundle.transport.requests) == 2
    for req in bundle.transport.requests:
        assert req.method == "POST"
        assert req.url.path == f"{LIB_PATH}/ListSkills"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_list_skills_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"skills": []}))
    override_url = "https://override.invalid"

    bundle.sdk.libraries.list_skills(body={}, server_url=override_url)

    assert str(bundle.transport.last_request.url).startswith(override_url)


@pytest.mark.asyncio
async def test_list_skills_server_url_override_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"skills": []}))
    override_url = "https://override.invalid"

    await bundle.sdk.libraries.list_skills_async(body={}, server_url=override_url)

    assert str(bundle.transport.last_request.url).startswith(override_url)


def test_list_imports_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"imports": []}))

    bundle.sdk.libraries.list_imports(
        body={}, http_headers={"X-Custom-Header": "value123"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "value123"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_list_library_history_timeout_ms_override_does_not_break_request(make_sdk):
    """timeout_ms is consumed by the underlying httpx client timeout config, not
    reflected directly on the recorded httpx.Request object in a simple way; we
    just assert the call completes and unmarshals correctly."""
    bundle = make_sdk(lambda req: json_response(200, {"history": []}))

    result = bundle.sdk.libraries.list_library_history(timeout_ms=12345)

    assert result.history == []


@pytest.mark.asyncio
async def test_get_size_timeline_timeout_ms_override_does_not_break_request_async(
    make_sdk,
):
    bundle = make_sdk(lambda req: json_response(200, {"days": []}))

    result = await bundle.sdk.libraries.get_size_timeline_async(timeout_ms=6789)

    assert result.days == []
