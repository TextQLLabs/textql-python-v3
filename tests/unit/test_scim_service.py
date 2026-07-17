"""Unit tests for the Scim service (sdk.scim)."""
import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response

BASE_PATH = "/textql.rpc.public.scim.ScimService"


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
# create_o_auth_client (expires_in_days: OptionalNullable[int])
# ---------------------------------------------------------------------------


def test_create_o_auth_client_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "id": "client-1",
                "clientId": "cid-1",
                "clientSecret": "secret-xyz",
                "description": "my client",
            },
        )
    )
    resp = bundle.sdk.scim.create_o_auth_client(
        description="my client", expires_in_days=30
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateScimOAuthClient"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["description"] == "my client"
    assert body["expiresInDays"] == 30

    assert resp.id == "client-1"
    assert resp.client_id == "cid-1"
    assert resp.client_secret == "secret-xyz"


def test_create_o_auth_client_expires_in_days_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.create_o_auth_client(description="d")
    body = bundle.transport.body_json()
    assert body == {"description": "d"}
    assert "expiresInDays" not in body


def test_create_o_auth_client_expires_in_days_explicit_none_included_as_null(make_sdk):
    # expires_in_days is OptionalNullable[int] -- explicitly passing None
    # must serialize as JSON null, distinct from omission (UNSET).
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.create_o_auth_client(description="d", expires_in_days=None)
    body = bundle.transport.body_json()
    assert "expiresInDays" in body
    assert body["expiresInDays"] is None


def test_create_o_auth_client_no_args_omits_both_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.create_o_auth_client()
    body = bundle.transport.body_json()
    assert body == {}


@pytest.mark.asyncio
async def test_create_o_auth_client_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"id": "client-2"}))
    resp = await bundle.sdk.scim.create_o_auth_client_async(
        description="d2", expires_in_days=7
    )
    body = bundle.transport.body_json()
    assert body["expiresInDays"] == 7
    assert resp.id == "client-2"


def test_create_o_auth_client_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.create_o_auth_client(description="d")
    assert exc_info.value.status_code == 400


def test_create_o_auth_client_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.create_o_auth_client(description="d")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# create_scim_token (expires_in_days: OptionalNullable[int])
# ---------------------------------------------------------------------------


def test_create_scim_token_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "id": "tok-1",
                "token": "scim-token-value",
                "description": "my token",
                "expiresAt": "2030-01-01T00:00:00Z",
            },
        )
    )
    resp = bundle.sdk.scim.create_scim_token(description="my token", expires_in_days=90)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateScimToken"

    body = bundle.transport.body_json()
    assert body["description"] == "my token"
    assert body["expiresInDays"] == 90

    assert resp.id == "tok-1"
    assert resp.token == "scim-token-value"
    assert resp.description == "my token"


def test_create_scim_token_expires_in_days_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.create_scim_token(description="d")
    body = bundle.transport.body_json()
    assert "expiresInDays" not in body


def test_create_scim_token_expires_in_days_explicit_none_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.create_scim_token(description="d", expires_in_days=None)
    body = bundle.transport.body_json()
    assert "expiresInDays" in body
    assert body["expiresInDays"] is None


@pytest.mark.asyncio
async def test_create_scim_token_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"token": "async-token"}))
    resp = await bundle.sdk.scim.create_scim_token_async(description="d2")
    assert resp.token == "async-token"


def test_create_scim_token_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.create_scim_token(description="d")
    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# list_scim_o_auth_clients (body: TextqlRPCPublicScimListScimOAuthClientsRequest)
# ---------------------------------------------------------------------------


def test_list_scim_o_auth_clients_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "clients": [
                    {"id": "c1", "clientId": "cid-1"},
                    {"id": "c2", "clientId": "cid-2"},
                ]
            },
        )
    )
    resp = bundle.sdk.scim.list_scim_o_auth_clients(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListScimOAuthClients"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    assert len(resp.clients) == 2
    assert resp.clients[0].client_id == "cid-1"


@pytest.mark.asyncio
async def test_list_scim_o_auth_clients_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"clients": []}))
    resp = await bundle.sdk.scim.list_scim_o_auth_clients_async(body={})
    assert resp.clients == []


def test_list_scim_o_auth_clients_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.list_scim_o_auth_clients(body={})
    assert exc_info.value.status_code == 401


def test_list_scim_o_auth_clients_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.list_scim_o_auth_clients(body={})
    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# list (ListScimTokens) -- body: TextqlRPCPublicScimListScimTokensRequest
# ---------------------------------------------------------------------------


def test_list_scim_tokens_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "tokens": [
                    {"id": "t1", "description": "tok one"},
                    {"id": "t2", "description": "tok two", "revokedAt": "2025-01-01T00:00:00Z"},
                ]
            },
        )
    )
    resp = bundle.sdk.scim.list(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ListScimTokens"

    assert len(resp.tokens) == 2
    assert resp.tokens[0].id == "t1"
    assert resp.tokens[1].revoked_at is not None


def test_list_scim_tokens_response_does_not_include_token_secret(make_sdk):
    # ListScimTokens' per-item model (TextqlRPCPublicScimScimToken) has no
    # `token` field at all -- confirm the SDK's model genuinely omits it
    # (list responses are metadata-only; only CreateScimToken returns the
    # plaintext token value, and only once, at creation time).
    bundle = make_sdk(lambda req: json_response(200, {"tokens": [{"id": "t1"}]}))
    resp = bundle.sdk.scim.list(body={})
    assert not hasattr(resp.tokens[0], "token")


@pytest.mark.asyncio
async def test_list_scim_tokens_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"tokens": []}))
    resp = await bundle.sdk.scim.list_async(body={})
    assert resp.tokens == []


def test_list_scim_tokens_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.list(body={})
    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# revoke_o_auth_client
# ---------------------------------------------------------------------------


def test_revoke_o_auth_client_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.revoke_o_auth_client(id="client-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RevokeScimOAuthClient"
    body = bundle.transport.body_json()
    assert body["id"] == "client-1"


@pytest.mark.asyncio
async def test_revoke_o_auth_client_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.scim.revoke_o_auth_client_async(id="client-2")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_revoke_o_auth_client_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.revoke_o_auth_client(id="missing")
    assert exc_info.value.status_code == 404


def test_revoke_o_auth_client_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.revoke_o_auth_client(id="client-1")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# revoke_scim_token
# ---------------------------------------------------------------------------


def test_revoke_scim_token_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.revoke_scim_token(id="tok-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RevokeScimToken"
    body = bundle.transport.body_json()
    assert body["id"] == "tok-1"


@pytest.mark.asyncio
async def test_revoke_scim_token_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    await bundle.sdk.scim.revoke_scim_token_async(id="tok-2")
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["id"] == "tok-2"


def test_revoke_scim_token_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.revoke_scim_token(id="tok-1")
    assert exc_info.value.status_code == 400


def test_revoke_scim_token_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.revoke_scim_token(id="tok-1")
    assert exc_info.value.status_code == 502


def test_revoke_scim_token_unexpected_non_json_status_raises(make_sdk):
    bundle = make_sdk(lambda req: text_response(304, ""))
    with pytest.raises(errors.TextqlDefaultError):
        bundle.sdk.scim.revoke_scim_token(id="tok-1")


# ---------------------------------------------------------------------------
# Retries (representative subset: create_scim_token, list_scim_o_auth_clients)
# ---------------------------------------------------------------------------


def test_create_scim_token_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {"token": "final-token"}),
        ]
    )
    bundle = make_sdk(handler)

    resp = bundle.sdk.scim.create_scim_token(
        description="d", retries=_retry_config()
    )
    assert resp.token == "final-token"
    assert len(bundle.transport.requests) == 2


@pytest.mark.asyncio
async def test_list_scim_o_auth_clients_async_retries_on_500_then_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary"}),
            json_response(200, {"clients": [{"id": "c1"}]}),
        ]
    )
    bundle = make_sdk(handler)

    resp = await bundle.sdk.scim.list_scim_o_auth_clients_async(
        body={}, retries=_retry_config()
    )
    assert len(resp.clients) == 1
    assert len(bundle.transport.requests) == 2


def test_revoke_scim_token_retries_exhausted_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "persistent"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.scim.revoke_scim_token(id="tok-1", retries=_retry_config())
    assert exc_info.value.status_code == 500
    assert len(bundle.transport.requests) >= 2


# ---------------------------------------------------------------------------
# Per-call overrides
# ---------------------------------------------------------------------------


def test_create_scim_token_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.create_scim_token(
        description="d", server_url="https://override.invalid"
    )
    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override.invalid")


def test_list_scim_tokens_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.list(body={}, http_headers={"X-Custom-Header": "custom-value"})
    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_revoke_scim_token_timeout_ms_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.revoke_scim_token(id="tok-1", timeout_ms=15000)


def test_create_o_auth_client_connect_timeout_ms_header(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.scim.create_o_auth_client(description="d", connect_timeout_ms=2500.0)
    req = bundle.transport.last_request
    assert req.headers.get("Connect-Timeout-Ms") in ("2500.0", "2500")
