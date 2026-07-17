"""Unit tests for the Sandbox service (sdk.sandbox), fully mocking the HTTP transport per tests/conftest.py."""
import json

import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response

BASE_PATH = "/textql.rpc.public.sandbox_query.SandboxQueryService"


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
# Basic request shape / auth / URL
# ---------------------------------------------------------------------------


def test_execute_query_sql_variant_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"arrowData": "AAA", "totalRows": 3})
    )

    resp = bundle.sdk.sandbox.execute_query(
        body={
            "sql_query": {"query": "SELECT * FROM t"},
            "source_name": "src1",
            "connector_id": 7,
        }
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ExecuteQuery"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["sqlQuery"]["query"] == "SELECT * FROM t"
    assert body["sourceName"] == "src1"
    assert body["connectorId"] == 7
    assert "libraryTql" not in body

    assert resp.arrow_data == "AAA"
    assert resp.total_rows == 3


def test_execute_query_library_tql_variant_serializes_distinctly(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.sandbox.execute_query(
        body={
            "library_tql": {},
            "source_name": "src2",
        }
    )

    body = bundle.transport.body_json()
    assert "libraryTql" in body
    assert "sqlQuery" not in body
    assert body["sourceName"] == "src2"


@pytest.mark.asyncio
async def test_execute_query_async_sql_variant(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalRows": 1}))
    resp = await bundle.sdk.sandbox.execute_query_async(
        body={"sql_query": {"query": "SELECT 1"}}
    )
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["sqlQuery"]["query"] == "SELECT 1"
    assert resp.total_rows == 1


# ---------------------------------------------------------------------------
# execute_query -- query string edge cases
# ---------------------------------------------------------------------------


def test_execute_query_empty_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": ""}})
    body = bundle.transport.body_json()
    assert body["sqlQuery"]["query"] == ""


def test_execute_query_special_characters_and_unicode(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    tricky_query = (
        "SELECT * FROM \"tab\\le\" WHERE name = 'O''Brien' "
        "AND note = 'line1\nline2\ttabbed' "
        "AND emoji = '☃\U0001F600' AND unicode = 'éü中文' "
        'AND quote = "she said \\"hi\\""'
    )
    bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": tricky_query}})

    raw = bundle.transport.last_request.content
    decoded = json.loads(raw)
    assert decoded["sqlQuery"]["query"] == tricky_query


def test_execute_query_very_long_query_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    long_query = "SELECT " + ", ".join(f"col{i}" for i in range(20000)) + " FROM t"
    bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": long_query}})
    body = bundle.transport.body_json()
    assert body["sqlQuery"]["query"] == long_query
    assert len(body["sqlQuery"]["query"]) == len(long_query)


def test_execute_query_with_parameters(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(
        body={
            "sql_query": {"query": "SELECT * FROM t WHERE id = :id"},
            "parameters": [{"name": "id", "value": "42"}],
        }
    )
    body = bundle.transport.body_json()
    assert body["parameters"] == [{"name": "id", "value": "42"}]


def test_execute_query_max_rows_int_variant(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(
        body={"sql_query": {"query": "SELECT 1"}, "max_rows": 100}
    )
    body = bundle.transport.body_json()
    assert body["maxRows"] == 100


def test_execute_query_max_rows_string_variant(make_sdk):
    # max_rows is Union[int, str] per the model -- verify string form
    # round-trips correctly too.
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(
        body={"sql_query": {"query": "SELECT 1"}, "max_rows": "unlimited"}
    )
    body = bundle.transport.body_json()
    assert body["maxRows"] == "unlimited"


def test_execute_query_optional_fields_omitted_when_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    body = bundle.transport.body_json()
    assert "sourceName" not in body
    assert "connectorId" not in body
    assert "parameters" not in body
    assert "maxRows" not in body


# ---------------------------------------------------------------------------
# Response unmarshaling
# ---------------------------------------------------------------------------


def test_execute_query_response_total_rows_as_string(make_sdk):
    # totalRows is Union[int, str] on the response too.
    bundle = make_sdk(lambda req: json_response(200, {"totalRows": "many"}))
    resp = bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    assert resp.total_rows == "many"


def test_execute_query_response_refreshed_token_null_vs_absent(make_sdk):
    from textql_sdk.types import UNSET

    bundle = make_sdk(lambda req: json_response(200, {"refreshedToken": None}))
    resp = bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    assert resp.refreshed_token is None

    bundle2 = make_sdk(lambda req: json_response(200, {}))
    resp2 = bundle2.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    # When the field is absent from the response entirely, the OptionalNullable
    # field decodes to the UNSET sentinel, not None -- these are distinct.
    assert resp2.refreshed_token == UNSET
    assert isinstance(resp2.refreshed_token, type(UNSET))


def test_execute_query_response_error_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"error": "execution failed"}))
    resp = bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "bad"}})
    assert resp.error == "execution failed"


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


def test_execute_query_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    assert exc_info.value.status_code == 400


def test_execute_query_4xx_not_found(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "sandbox not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    assert exc_info.value.status_code == 404


def test_execute_query_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "internal error"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    assert exc_info.value.status_code == 500


def test_execute_query_5xx_bad_gateway(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})
    assert exc_info.value.status_code == 502


@pytest.mark.asyncio
async def test_execute_query_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "unprocessable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.sandbox.execute_query_async(
            body={"sql_query": {"query": "SELECT 1"}}
        )
    assert exc_info.value.status_code == 422


@pytest.mark.asyncio
async def test_execute_query_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.sandbox.execute_query_async(
            body={"sql_query": {"query": "SELECT 1"}}
        )
    assert exc_info.value.status_code == 503


def test_execute_query_unexpected_status_raises_default_error(make_sdk):
    bundle = make_sdk(lambda req: text_response(304, ""))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.sandbox.execute_query(body={"sql_query": {"query": "SELECT 1"}})


# ---------------------------------------------------------------------------
# Retries
# ---------------------------------------------------------------------------


def test_execute_query_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"totalRows": 1}),
        ]
    )
    bundle = make_sdk(handler)

    resp = bundle.sdk.sandbox.execute_query(
        body={"sql_query": {"query": "SELECT 1"}},
        retries=_retry_config(),
    )

    assert resp.total_rows == 1
    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_execute_query_async_retries_on_500_then_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"totalRows": 1}),
        ]
    )
    bundle = make_sdk(handler)

    resp = await bundle.sdk.sandbox.execute_query_async(
        body={"sql_query": {"query": "SELECT 1"}},
        retries=_retry_config(),
    )

    assert resp.total_rows == 1
    assert len(bundle.transport.requests) == 2


def test_execute_query_retries_exhausted_raises(make_sdk):
    # Every attempt fails with 500; with a tiny max_elapsed_time the retry
    # loop should give up quickly and surface the last error response.
    bundle = make_sdk(lambda req: json_response(500, {"message": "persistent failure"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.sandbox.execute_query(
            body={"sql_query": {"query": "SELECT 1"}},
            retries=_retry_config(),
        )
    assert exc_info.value.status_code == 500
    # Confirm it actually retried more than once before giving up.
    assert len(bundle.transport.requests) >= 2


# ---------------------------------------------------------------------------
# Per-call overrides
# ---------------------------------------------------------------------------


def test_execute_query_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(
        body={"sql_query": {"query": "SELECT 1"}},
        server_url="https://override.invalid",
    )
    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override.invalid")


def test_execute_query_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(
        body={"sql_query": {"query": "SELECT 1"}},
        http_headers={"X-Custom-Header": "custom-value"},
    )
    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_execute_query_timeout_ms_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalRows": 1}))
    resp = bundle.sdk.sandbox.execute_query(
        body={"sql_query": {"query": "SELECT 1"}},
        timeout_ms=15000,
    )
    assert resp.total_rows == 1


def test_execute_query_connect_timeout_ms_header(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.sandbox.execute_query(
        body={"sql_query": {"query": "SELECT 1"}},
        connect_timeout_ms=2500.0,
    )
    req = bundle.transport.last_request
    assert req.headers.get("Connect-Timeout-Ms") == "2500.0" or req.headers.get(
        "Connect-Timeout-Ms"
    ) == "2500"
