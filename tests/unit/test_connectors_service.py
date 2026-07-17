"""Unit tests for the Connectors service (sdk.connectors), fully mocking the HTTP transport per tests/conftest.py."""
import json

import httpx
import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response

BASE_PATH = "/textql.rpc.public.connector.ConnectorService"


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
# create / create_async
# ---------------------------------------------------------------------------


def test_create_postgres_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.connectors.create(
        config={
            "postgres": {
                "host": "db.example.com",
                "port": 5432,
                "user": "svc",
                "password": "hunter2",
                "database": "prod",
            },
            "name": "my-postgres",
        },
        allow_sql_write_operations=True,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateConnector"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["config"]["postgres"]["host"] == "db.example.com"
    assert body["config"]["postgres"]["port"] == 5432
    assert body["config"]["name"] == "my-postgres"
    assert body["allowSqlWriteOperations"] is True
    # UNSET fields must be omitted entirely.
    assert "includeDbSessionMetadata" not in body
    assert "access" not in body


def test_create_snowflake_serializes_distinctly_from_postgres(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.connectors.create(
        config={
            "snowflake": {
                "username": "svc_user",
                "password": "s3cr3t",
                "locator": "abc12345",
                "database": "ANALYTICS",
                "warehouse": "COMPUTE_WH",
            },
            "name": "my-snowflake",
        },
    )

    body = bundle.transport.body_json()
    assert "postgres" not in body["config"]
    assert body["config"]["snowflake"]["locator"] == "abc12345"
    assert body["config"]["snowflake"]["warehouse"] == "COMPUTE_WH"
    assert body["config"]["snowflake"]["username"] == "svc_user"


def test_create_nullable_bool_explicit_false_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.connectors.create(
        config={"postgres": {"host": "h"}},
        allow_sql_write_operations=False,
        include_db_session_metadata=None,  # explicit null
    )

    body = bundle.transport.body_json()
    assert body["allowSqlWriteOperations"] is False
    # Explicitly-set None on a Nullable field must serialize as JSON null,
    # not be omitted.
    assert "includeDbSessionMetadata" in body
    assert body["includeDbSessionMetadata"] is None


@pytest.mark.asyncio
async def test_create_async_matches_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.connectors.create_async(
        config={"postgres": {"host": "h2"}},
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateConnector"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["config"]["postgres"]["host"] == "h2"


def test_create_response_unmarshals(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"connectorId": 42, "name": "my-postgres"}
        )
    )
    resp = bundle.sdk.connectors.create(config={"postgres": {"host": "h"}})
    assert resp.connector_id == 42
    assert resp.name == "my-postgres"


def test_create_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad config"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.create(config={"postgres": {"host": "h"}})
    assert exc_info.value.status_code == 400


def test_create_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.create(config={"postgres": {"host": "h"}})
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_create_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "nope"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.connectors.create_async(config={"postgres": {"host": "h"}})
    assert exc_info.value.status_code == 422


# ---------------------------------------------------------------------------
# delete / delete_async
# ---------------------------------------------------------------------------


def test_delete_sends_connector_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.delete(connector_id=99)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteConnector"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"connectorId": 99}


@pytest.mark.asyncio
async def test_delete_async_sends_connector_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.delete_async(connector_id=7)
    body = bundle.transport.body_json()
    assert body == {"connectorId": 7}


def test_delete_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.delete(connector_id=1)
    assert exc_info.value.status_code == 404


def test_delete_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.delete(connector_id=1)
    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# duplicate_connector / duplicate_connector_async
# ---------------------------------------------------------------------------


def test_duplicate_connector(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.duplicate_connector(connector_id=5)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/DuplicateConnector"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"connectorId": 5}


@pytest.mark.asyncio
async def test_duplicate_connector_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.duplicate_connector_async(connector_id=5)
    assert bundle.transport.body_json() == {"connectorId": 5}


def test_duplicate_connector_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.duplicate_connector(connector_id=5)
    assert exc_info.value.status_code == 409


def test_duplicate_connector_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.duplicate_connector(connector_id=5)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# execute_query / execute_query_async -- highest-value operation
# ---------------------------------------------------------------------------


def test_execute_query_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"arrowData": "QVJST1cx", "success": True})
    )

    resp = bundle.sdk.connectors.execute_query(
        connector_id=10, query="SELECT 1", limit=100
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ExecuteQuery"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"connectorId": 10, "query": "SELECT 1", "limit": 100}
    assert resp.success is True
    assert resp.arrow_data == "QVJST1cx"


def test_execute_query_empty_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))
    bundle.sdk.connectors.execute_query(connector_id=1, query="")
    body = bundle.transport.body_json()
    # Empty string is a real, non-None value for an Optional[str] field, so it
    # must be sent, not omitted.
    assert body["query"] == ""


def test_execute_query_special_characters_and_unicode(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    tricky_query = (
        "SELECT * FROM \"tab\\le\" WHERE name = 'O''Brien' "
        "AND note = 'line1\nline2\ttabbed' "
        "AND emoji = '☃\U0001F600' AND unicode = 'éü中文' "
        'AND quote = "she said \\"hi\\""'
    )
    bundle.sdk.connectors.execute_query(connector_id=2, query=tricky_query)

    # Round-trip through the raw request bytes (not the already-parsed
    # body_json helper) to be extra sure escaping survives real JSON decoding.
    raw = bundle.transport.last_request.content
    decoded = json.loads(raw)
    assert decoded["query"] == tricky_query


def test_execute_query_very_long_query_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    long_query = "SELECT " + ", ".join(f"col{i}" for i in range(20000)) + " FROM t"
    bundle.sdk.connectors.execute_query(connector_id=3, query=long_query)
    body = bundle.transport.body_json()
    assert body["query"] == long_query
    assert len(body["query"]) == len(long_query)


def test_execute_query_limit_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.execute_query(connector_id=4, query="SELECT 1")
    body = bundle.transport.body_json()
    assert "limit" not in body


def test_execute_query_limit_explicit_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.execute_query(connector_id=4, query="SELECT 1", limit=None)
    body = bundle.transport.body_json()
    assert "limit" in body
    assert body["limit"] is None


def test_execute_query_limit_zero_and_negative(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.connectors.execute_query(connector_id=4, query="SELECT 1", limit=0)
    assert bundle.transport.body_json()["limit"] == 0

    bundle.sdk.connectors.execute_query(connector_id=4, query="SELECT 1", limit=-1)
    assert bundle.transport.body_json()["limit"] == -1


@pytest.mark.asyncio
async def test_execute_query_async_matches_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    resp = await bundle.sdk.connectors.execute_query_async(
        connector_id=10, query="SELECT 1", limit=5
    )
    body = bundle.transport.body_json()
    assert body == {"connectorId": 10, "query": "SELECT 1", "limit": 5}
    assert resp.success is True


def test_execute_query_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad sql"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.execute_query(connector_id=1, query="SELEC")
    assert exc_info.value.status_code == 400


def test_execute_query_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.execute_query(connector_id=1, query="SELECT 1")
    assert exc_info.value.status_code == 502


def test_execute_query_error_message_in_success_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"success": False, "errorMessage": "syntax error at line 1"}
        )
    )
    resp = bundle.sdk.connectors.execute_query(connector_id=1, query="BAD SQL")
    assert resp.success is False
    assert resp.error_message == "syntax error at line 1"


def test_execute_query_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)

    resp = bundle.sdk.connectors.execute_query(
        connector_id=1,
        query="SELECT 1",
        retries=_retry_config(),
    )

    assert resp.success is True
    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_execute_query_async_retries_on_500_then_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)

    resp = await bundle.sdk.connectors.execute_query_async(
        connector_id=1,
        query="SELECT 1",
        retries=_retry_config(),
    )

    assert resp.success is True
    assert len(bundle.transport.requests) == 2


def test_execute_query_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.execute_query(
        connector_id=1,
        query="SELECT 1",
        server_url="https://override.invalid",
    )
    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override.invalid")


def test_execute_query_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.execute_query(
        connector_id=1,
        query="SELECT 1",
        http_headers={"X-Custom-Header": "custom-value"},
    )
    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    # auth header should still be present alongside custom headers
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_execute_query_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    resp = bundle.sdk.connectors.execute_query(
        connector_id=1,
        query="SELECT 1",
        timeout_ms=15000,
    )
    assert resp.success is True


# ---------------------------------------------------------------------------
# get / get_async
# ---------------------------------------------------------------------------


def test_get_connector(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"connector": {"postgresMetadata": {"host": "h"}, "id": 3}}
        )
    )
    resp = bundle.sdk.connectors.get(connector_id=3)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetConnector"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"connectorId": 3}
    assert resp.connector.id == 3


@pytest.mark.asyncio
async def test_get_connector_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"connector": {"postgresMetadata": {"host": "h"}, "id": 3}}
        )
    )
    resp = await bundle.sdk.connectors.get_async(connector_id=3)
    assert resp.connector.id == 3


def test_get_connector_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "missing"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get(connector_id=999)
    assert exc_info.value.status_code == 404


def test_get_connector_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get(connector_id=999)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_connector_cell_durations / _async
# ---------------------------------------------------------------------------


def test_get_connector_cell_durations(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_connector_cell_durations(
        connector_id=1, days=7, limit=10, offset=0
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetConnectorCellDurations"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"connectorId": 1, "days": 7, "limit": 10, "offset": 0}


@pytest.mark.asyncio
async def test_get_connector_cell_durations_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.get_connector_cell_durations_async(
        connector_id=1, days=7, limit=10, offset=0
    )
    body = bundle.transport.body_json()
    assert body == {"connectorId": 1, "days": 7, "limit": 10, "offset": 0}


def test_get_connector_cell_durations_pagination_edge_values(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_connector_cell_durations(
        connector_id=1, days=0, limit=0, offset=-1
    )
    body = bundle.transport.body_json()
    assert body["limit"] == 0
    assert body["offset"] == -1


def test_get_connector_cell_durations_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_connector_cell_durations(connector_id=1)


def test_get_connector_cell_durations_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_connector_cell_durations(connector_id=1)


# ---------------------------------------------------------------------------
# get_chats / _async
# ---------------------------------------------------------------------------


def test_get_chats(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_chats(connector_id=1)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetConnectorChats"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"connectorId": 1}


@pytest.mark.asyncio
async def test_get_chats_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.get_chats_async(connector_id=1)
    assert bundle.transport.body_json() == {"connectorId": 1}


def test_get_chats_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_chats(connector_id=1)
    assert exc_info.value.status_code == 403


def test_get_chats_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_chats(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_dashboards / _async
# ---------------------------------------------------------------------------


def test_get_dashboards(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_dashboards(connector_id=1)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetConnectorDashboards"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"connectorId": 1}


@pytest.mark.asyncio
async def test_get_dashboards_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.get_dashboards_async(connector_id=1)
    assert bundle.transport.body_json() == {"connectorId": 1}


def test_get_dashboards_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "missing"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_dashboards(connector_id=1)
    assert exc_info.value.status_code == 404


def test_get_dashboards_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_dashboards(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_connector_stats / _async
# ---------------------------------------------------------------------------


def test_get_connector_stats(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_connector_stats(days=30)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetConnectorStats"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"days": 30}


def test_get_connector_stats_all_time_zero(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_connector_stats(days=0)
    assert bundle.transport.body_json()["days"] == 0


@pytest.mark.asyncio
async def test_get_connector_stats_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.get_connector_stats_async(days=30)
    assert bundle.transport.body_json() == {"days": 30}


def test_get_connector_stats_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_connector_stats(days=1)


def test_get_connector_stats_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_connector_stats(days=1)


# ---------------------------------------------------------------------------
# get_usage / _async
# ---------------------------------------------------------------------------


def test_get_usage(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_usage(connector_id=1, days=7)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetConnectorUsage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"connectorId": 1, "days": 7}


@pytest.mark.asyncio
async def test_get_usage_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.get_usage_async(connector_id=1, days=7)
    assert bundle.transport.body_json() == {"connectorId": 1, "days": 7}


def test_get_usage_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_usage(connector_id=1, days=7)


def test_get_usage_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_usage(connector_id=1, days=7)


# ---------------------------------------------------------------------------
# get_connectors / _async  (body is a required TypedDict/model, no fields)
# ---------------------------------------------------------------------------


def test_get_connectors(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "connectors": [
                    {"postgresMetadata": {"host": "h1"}, "id": 1},
                    {"snowflakeMetadata": {"locator": "loc"}, "id": 2},
                ]
            },
        )
    )
    resp = bundle.sdk.connectors.get_connectors(body={})
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetConnectors"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert len(resp.connectors) == 2
    assert resp.connectors[0].id == 1


@pytest.mark.asyncio
async def test_get_connectors_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"connectors": []}))
    resp = await bundle.sdk.connectors.get_connectors_async(body={})
    assert resp.connectors == []


def test_get_connectors_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_connectors(body={})
    assert exc_info.value.status_code == 401


def test_get_connectors_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_connectors(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_example_queries / _async
# ---------------------------------------------------------------------------


def test_get_example_queries(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.get_example_queries(
        connector_contexts=[{"tableau": {}, "connector_id": 1}],
        feature_filter="FEATURE_TYPE_UNSPECIFIED",
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetExampleQueries"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["connectorContexts"][0]["tableau"] == {}
    assert body["connectorContexts"][0]["connectorId"] == 1


@pytest.mark.asyncio
async def test_get_example_queries_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.get_example_queries_async()
    body = bundle.transport.body_json()
    # Both fields optional; with nothing passed the body should be empty (or
    # absent keys only), never containing None-valued optional keys.
    assert "connectorContexts" not in body
    assert "featureFilter" not in body


def test_get_example_queries_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_example_queries()


def test_get_example_queries_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get_example_queries()


# ---------------------------------------------------------------------------
# get_table_preview / _async
# ---------------------------------------------------------------------------


def test_get_table_preview_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"arrowData": "AAA", "success": True})
    )
    resp = bundle.sdk.connectors.get_table_preview(
        connector_id=1,
        table_database="mydb",
        table_schema="public",
        table_name="users",
        limit=50,
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetTablePreview"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "connectorId": 1,
        "tableDatabase": "mydb",
        "tableSchema": "public",
        "tableName": "users",
        "limit": 50,
    }
    assert resp.success is True


def test_get_table_preview_limit_zero(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.get_table_preview(
        connector_id=1, table_name="t", limit=0
    )
    body = bundle.transport.body_json()
    assert body["limit"] == 0


def test_get_table_preview_limit_negative(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.get_table_preview(
        connector_id=1, table_name="t", limit=-5
    )
    body = bundle.transport.body_json()
    assert body["limit"] == -5


def test_get_table_preview_optional_fields_omitted_when_none(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.get_table_preview(connector_id=1, table_name="t")
    body = bundle.transport.body_json()
    assert "tableDatabase" not in body
    assert "tableSchema" not in body
    assert "limit" not in body


@pytest.mark.asyncio
async def test_get_table_preview_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    resp = await bundle.sdk.connectors.get_table_preview_async(
        connector_id=1, table_name="t"
    )
    assert resp.success is True


def test_get_table_preview_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no table"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_table_preview(connector_id=1, table_name="missing")
    assert exc_info.value.status_code == 404


def test_get_table_preview_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.get_table_preview(connector_id=1, table_name="t")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_tables / list_tables_async
# ---------------------------------------------------------------------------


def test_list_tables(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "tables": [
                    {"tableName": "users"},
                    {"tableName": "orders"},
                ]
            },
        )
    )
    resp = bundle.sdk.connectors.list_tables(connector_id=1)
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListConnectorTables"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"connectorId": 1}
    assert len(resp.tables) == 2
    assert resp.tables[0].table_name == "users"


def test_list_tables_error_field_in_200_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"tables": [], "error": "introspection failed"})
    )
    resp = bundle.sdk.connectors.list_tables(connector_id=1)
    assert resp.tables == []
    assert resp.error == "introspection failed"


@pytest.mark.asyncio
async def test_list_tables_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"tables": []}))
    resp = await bundle.sdk.connectors.list_tables_async(connector_id=1)
    assert resp.tables == []


def test_list_tables_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.list_tables(connector_id=1)
    assert exc_info.value.status_code == 400


def test_list_tables_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.list_tables(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_query_templates / _async
# ---------------------------------------------------------------------------


def test_list_query_templates(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.list_query_templates(
        connector_id=1, limit=20, offset=40, days=7
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ListQueryTemplates"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"connectorId": 1, "limit": 20, "offset": 40, "days": 7}


def test_list_query_templates_pagination_edge_values(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.list_query_templates(
        connector_id=1, limit=0, offset=0, days=0
    )
    body = bundle.transport.body_json()
    assert body["limit"] == 0
    assert body["offset"] == 0

    bundle.sdk.connectors.list_query_templates(
        connector_id=1, limit=-1, offset=-10, days=0
    )
    body = bundle.transport.body_json()
    assert body["limit"] == -1
    assert body["offset"] == -10


@pytest.mark.asyncio
async def test_list_query_templates_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.list_query_templates_async(connector_id=1)
    body = bundle.transport.body_json()
    assert body == {"connectorId": 1}


def test_list_query_templates_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.list_query_templates(connector_id=1)


def test_list_query_templates_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.list_query_templates(connector_id=1)


# ---------------------------------------------------------------------------
# test / test_async -- highest-value operation (connection testing)
# ---------------------------------------------------------------------------


def test_test_connector_postgres(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    resp = bundle.sdk.connectors.test(
        config={"postgres": {"host": "h", "port": 5432, "user": "u", "password": "p"}}
    )
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/TestConnector"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["config"]["postgres"]["host"] == "h"
    assert "connectorId" not in body
    assert resp.success is True


def test_test_connector_snowflake_distinct_serialization(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.test(
        config={"snowflake": {"username": "u", "locator": "loc123", "database": "db"}}
    )
    body = bundle.transport.body_json()
    assert "snowflake" in body["config"]
    assert "postgres" not in body["config"]
    assert body["config"]["snowflake"]["locator"] == "loc123"


def test_test_connector_id_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.test(config={"postgres": {"host": "h"}})
    body = bundle.transport.body_json()
    assert "connectorId" not in body


def test_test_connector_id_explicit_value_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.test(
        config={"postgres": {"host": "h"}}, connector_id="conn-123"
    )
    body = bundle.transport.body_json()
    assert body["connectorId"] == "conn-123"


def test_test_connector_id_explicit_null_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.test(config={"postgres": {"host": "h"}}, connector_id=None)
    body = bundle.transport.body_json()
    assert "connectorId" in body
    assert body["connectorId"] is None


def test_test_connector_failure_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"success": False, "error": "connection refused"}
        )
    )
    resp = bundle.sdk.connectors.test(config={"postgres": {"host": "bad-host"}})
    assert resp.success is False
    assert resp.error == "connection refused"


@pytest.mark.asyncio
async def test_test_connector_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    resp = await bundle.sdk.connectors.test_async(
        config={"postgres": {"host": "h"}}
    )
    assert resp.success is True


def test_test_connector_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid config"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.test(config={"postgres": {"host": "h"}})
    assert exc_info.value.status_code == 400


def test_test_connector_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.test(config={"postgres": {"host": "h"}})
    assert exc_info.value.status_code == 500


def test_test_connector_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)
    resp = bundle.sdk.connectors.test(
        config={"postgres": {"host": "h"}}, retries=_retry_config()
    )
    assert resp.success is True
    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_test_connector_async_retries_on_500_then_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)
    resp = await bundle.sdk.connectors.test_async(
        config={"postgres": {"host": "h"}}, retries=_retry_config()
    )
    assert resp.success is True
    assert len(bundle.transport.requests) == 2


def test_test_connector_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.test(
        config={"postgres": {"host": "h"}},
        server_url="https://override2.invalid",
    )
    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override2.invalid")


def test_test_connector_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    bundle.sdk.connectors.test(
        config={"postgres": {"host": "h"}},
        http_headers={"X-Trace-Id": "trace-abc"},
    )
    req = bundle.transport.last_request
    assert req.headers["X-Trace-Id"] == "trace-abc"


# ---------------------------------------------------------------------------
# update / update_async
# ---------------------------------------------------------------------------


def test_update_connector(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.update(
        connector_id=1,
        config={"postgres": {"host": "new-host"}},
        allow_sql_write_operations=True,
    )
    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/UpdateConnector"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["config"]["postgres"]["host"] == "new-host"
    assert body["allowSqlWriteOperations"] is True
    assert "includeDbSessionMetadata" not in body


def test_update_connector_nullable_explicit_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.connectors.update(
        connector_id=1,
        include_db_session_metadata=None,
    )
    body = bundle.transport.body_json()
    assert "includeDbSessionMetadata" in body
    assert body["includeDbSessionMetadata"] is None


@pytest.mark.asyncio
async def test_update_connector_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.connectors.update_async(connector_id=1)
    body = bundle.transport.body_json()
    assert body == {"connectorId": 1}


def test_update_connector_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.update(connector_id=1)
    assert exc_info.value.status_code == 400


def test_update_connector_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.connectors.update(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Unexpected / non-JSON response handling (generic safety net)
# ---------------------------------------------------------------------------


def test_get_connector_unexpected_status_raises_default_error(make_sdk):
    # 3xx isn't handled by any of the explicit branches (200 json / 4xx / 5xx
    # / default json), so the SDK should fall through to the final raise.
    bundle = make_sdk(lambda req: text_response(304, ""))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.connectors.get(connector_id=1)
