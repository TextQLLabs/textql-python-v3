"""Unit tests for the Mcp service (sdk.mcp)."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, models, utils

BASE_PATH = "/textql.rpc.public.mcp.MCPService"


# ---------------------------------------------------------------------------
# UpsertMCPServers
# ---------------------------------------------------------------------------


def test_upsert_mcp_servers_multiple_servers(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "mcpServers": [
                    {"mcpServer": {"httpConfig": {"url": "https://a.example.com"}}},
                    {"mcpServer": {"sseConfig": {"url": "https://b.example.com"}}},
                ]
            },
        )
    )

    result = bundle.sdk.mcp.upsert_mcp_servers(
        mcp_servers=[
            {
                "http_config": {"url": "https://a.example.com", "headers": {"A": "1"}},
                "name": "server-a",
            },
            {
                "sse_config": {"url": "https://b.example.com"},
                "name": "server-b",
            },
        ]
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/UpsertMCPServers"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert len(body["mcpServers"]) == 2
    assert body["mcpServers"][0]["httpConfig"]["url"] == "https://a.example.com"
    assert body["mcpServers"][0]["name"] == "server-a"
    assert body["mcpServers"][1]["sseConfig"]["url"] == "https://b.example.com"

    assert len(result.mcp_servers) == 2


def test_upsert_mcp_servers_empty_list(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"mcpServers": []}))

    result = bundle.sdk.mcp.upsert_mcp_servers(mcp_servers=[])

    body = bundle.transport.body_json()
    assert body["mcpServers"] == []
    assert result.mcp_servers == []


def test_upsert_mcp_servers_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.mcp.upsert_mcp_servers()

    body = bundle.transport.body_json()
    assert body == {}


@pytest.mark.asyncio
async def test_upsert_mcp_servers_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"mcpServers": []}))

    result = await bundle.sdk.mcp.upsert_mcp_servers_async(
        mcp_servers=[{"http_config": {"url": "https://x.example.com"}, "name": "x"}]
    )

    body = bundle.transport.body_json()
    assert len(body["mcpServers"]) == 1
    assert result.mcp_servers == []


def test_upsert_mcp_servers_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid config"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.upsert_mcp_servers(
            mcp_servers=[{"http_config": {"url": "bad"}, "name": "x"}]
        )

    assert exc_info.value.status_code == 422


def test_upsert_mcp_servers_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.upsert_mcp_servers(mcp_servers=[])

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# GetMCPServers
# ---------------------------------------------------------------------------


def test_get_servers_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "mcpServers": [
                    {
                        "mcpServer": {
                            "httpConfig": {"url": "https://a.example.com"},
                            "id": "srv-1",
                        },
                        "tools": [{"name": "tool1"}],
                    }
                ]
            },
        )
    )

    result = bundle.sdk.mcp.get_servers(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetMCPServers"
    assert len(result.mcp_servers) == 1
    assert result.mcp_servers[0].mcp_server.id == "srv-1"


@pytest.mark.asyncio
async def test_get_servers_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"mcpServers": []}))

    result = await bundle.sdk.mcp.get_servers_async(
        body=models.TextqlRPCPublicMCPGetMCPServersRequest()
    )

    assert result.mcp_servers == []


def test_get_servers_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.get_servers(body={})

    assert exc_info.value.status_code == 401


# ---------------------------------------------------------------------------
# DeleteMCPServer
# ---------------------------------------------------------------------------


def test_delete_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.mcp.delete(id="srv-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteMCPServer"
    body = bundle.transport.body_json()
    assert body["id"] == "srv-1"
    assert result.success is True


@pytest.mark.asyncio
async def test_delete_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False, "error": "nope"}))

    result = await bundle.sdk.mcp.delete_async(id="srv-2")

    body = bundle.transport.body_json()
    assert body["id"] == "srv-2"
    assert result.success is False
    assert result.error == "nope"


def test_delete_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.delete(id="missing")

    assert exc_info.value.status_code == 404


def test_delete_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.delete(id="srv-1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ToggleMCPServer
# ---------------------------------------------------------------------------


def test_toggle_server_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.mcp.toggle_server(id="srv-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ToggleMCPServer"
    body = bundle.transport.body_json()
    assert body["id"] == "srv-1"
    assert result.success is True


@pytest.mark.asyncio
async def test_toggle_server_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    await bundle.sdk.mcp.toggle_server_async(id="srv-2")

    body = bundle.transport.body_json()
    assert body["id"] == "srv-2"


def test_toggle_server_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad id"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.toggle_server(id="x")

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# OAuth flow: InitiateOAuthFlow / HandleOAuthCallback / ClearOAuthToken
# ---------------------------------------------------------------------------


def test_initiate_o_auth_flow_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "authorizationUrl": "https://auth.example.com/authorize?client_id=x",
            },
        )
    )

    result = bundle.sdk.mcp.initiate_o_auth_flow(server_id="srv-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/InitiateOAuthFlow"
    body = bundle.transport.body_json()
    assert body["serverId"] == "srv-1"
    assert result.success is True
    assert result.authorization_url.startswith("https://auth.example.com")


@pytest.mark.asyncio
async def test_initiate_o_auth_flow_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": False, "error": "no such server"})
    )

    result = await bundle.sdk.mcp.initiate_o_auth_flow_async(server_id="srv-x")

    assert result.success is False
    assert result.error == "no such server"


def test_initiate_o_auth_flow_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.initiate_o_auth_flow(server_id="missing")

    assert exc_info.value.status_code == 404


def test_handle_o_auth_callback_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.mcp.handle_o_auth_callback(
        server_id="srv-1", code="auth-code-123", state="state-abc"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/HandleOAuthCallback"
    body = bundle.transport.body_json()
    assert body["serverId"] == "srv-1"
    assert body["code"] == "auth-code-123"
    assert body["state"] == "state-abc"
    assert result.success is True


@pytest.mark.asyncio
async def test_handle_o_auth_callback_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": False, "error": "state mismatch"})
    )

    result = await bundle.sdk.mcp.handle_o_auth_callback_async(
        server_id="srv-1", code="c", state="s"
    )

    assert result.success is False
    assert result.error == "state mismatch"


def test_handle_o_auth_callback_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid code"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.handle_o_auth_callback(server_id="srv-1", code="bad", state="s")

    assert exc_info.value.status_code == 400


def test_clear_o_auth_token_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.mcp.clear_o_auth_token(server_id="srv-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ClearOAuthToken"
    body = bundle.transport.body_json()
    assert body["serverId"] == "srv-1"
    assert result.success is True


@pytest.mark.asyncio
async def test_clear_o_auth_token_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    await bundle.sdk.mcp.clear_o_auth_token_async(server_id="srv-2")

    body = bundle.transport.body_json()
    assert body["serverId"] == "srv-2"


def test_clear_o_auth_token_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.mcp.clear_o_auth_token(server_id="srv-1")

    assert exc_info.value.status_code == 503


def test_oauth_flow_end_to_end(make_sdk):
    """Simulates initiate -> callback -> clear across a sequence of
    responses on the same mocked transport."""
    responses = iter(
        [
            json_response(
                200,
                {
                    "success": True,
                    "authorizationUrl": "https://auth.example.com/authorize",
                },
            ),
            json_response(200, {"success": True}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(lambda req: next(responses))

    initiate = bundle.sdk.mcp.initiate_o_auth_flow(server_id="srv-1")
    assert initiate.success is True

    callback = bundle.sdk.mcp.handle_o_auth_callback(
        server_id="srv-1", code="code", state="state"
    )
    assert callback.success is True

    cleared = bundle.sdk.mcp.clear_o_auth_token(server_id="srv-1")
    assert cleared.success is True

    assert len(bundle.transport.requests) == 3
    assert bundle.transport.requests[0].url.path == f"{BASE_PATH}/InitiateOAuthFlow"
    assert bundle.transport.requests[1].url.path == f"{BASE_PATH}/HandleOAuthCallback"
    assert bundle.transport.requests[2].url.path == f"{BASE_PATH}/ClearOAuthToken"


# ---------------------------------------------------------------------------
# retries / server_url / http_headers / timeout_ms overrides
# ---------------------------------------------------------------------------


def test_toggle_server_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)

    result = bundle.sdk.mcp.toggle_server(
        id="srv-1",
        retries=utils.RetryConfig(
            strategy="backoff",
            backoff=utils.BackoffStrategy(
                initial_interval=1,
                max_interval=5,
                exponent=1.0,
                max_elapsed_time=5000,
            ),
            retry_connection_errors=False,
        ),
    )

    assert len(bundle.transport.requests) == 2
    assert result.success is True


@pytest.mark.asyncio
async def test_upsert_mcp_servers_retries_on_500_then_succeeds_async(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"mcpServers": []}),
        ]
    )
    bundle = make_sdk(handler)

    result = await bundle.sdk.mcp.upsert_mcp_servers_async(
        mcp_servers=[],
        retries=utils.RetryConfig(
            strategy="backoff",
            backoff=utils.BackoffStrategy(
                initial_interval=1,
                max_interval=5,
                exponent=1.0,
                max_elapsed_time=5000,
            ),
            retry_connection_errors=False,
        ),
    )

    assert len(bundle.transport.requests) == 2
    assert result.mcp_servers == []


def test_delete_server_url_override(make_sdk):
    captured = {}

    def handler(req):
        captured["url"] = str(req.url)
        return json_response(200, {})

    bundle = make_sdk(handler)

    bundle.sdk.mcp.delete(id="srv-1", server_url="https://override.invalid")

    assert captured["url"].startswith("https://override.invalid")


def test_initiate_o_auth_flow_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.mcp.initiate_o_auth_flow(
        server_id="srv-1", http_headers={"X-Trace-Id": "trace-123"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Trace-Id"] == "trace-123"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_get_servers_timeout_ms_override_does_not_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.mcp.get_servers(body={}, timeout_ms=20000)

    assert len(bundle.transport.requests) == 1
