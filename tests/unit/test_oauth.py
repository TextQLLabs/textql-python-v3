"""Unit tests for textql_sdk.oauth -- Bearer token auth with refresh."""

import base64
import hashlib
import time
from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from textql_sdk import Textql
from textql_sdk.oauth import (
    OAuthRefreshError,
    authorization_url,
    exchange_code,
    TokenAuth,
    TokenManager,
    from_tokens,
    token_manager_of,
)

from tests.conftest import FAKE_BASE_URL, RecordingTransport, json_response

TOKEN_URL = f"{FAKE_BASE_URL}/oauth/token"


class FakeServer:
    """Accepts exactly one access token; /oauth/token rotates the pair."""

    def __init__(self, valid_token="access-1", refresh_token="refresh-1"):
        self.valid_token = valid_token
        self.refresh_token = refresh_token
        self.refreshes = 0
        self.transport = RecordingTransport(self.handle)

    def handle(self, request: httpx.Request) -> httpx.Response:
        if request.url.path == "/oauth/token":
            form = {k: v[0] for k, v in parse_qs(request.content.decode()).items()}
            if form.get("refresh_token") != self.refresh_token:
                return json_response(400, {"error": "invalid_grant"})
            self.refreshes += 1
            self.valid_token = f"access-{self.refreshes + 1}"
            self.refresh_token = f"refresh-{self.refreshes + 1}"
            return json_response(
                200,
                {
                    "access_token": self.valid_token,
                    "token_type": "Bearer",
                    "expires_in": 3600,
                    "refresh_token": self.refresh_token,
                },
            )
        if request.headers.get("authorization") != f"Bearer {self.valid_token}":
            return json_response(401, {"code": "unauthenticated"})
        return json_response(200, {"chat": {"id": "chat-1"}})

    def manager(self, **kwargs) -> TokenManager:
        kwargs.setdefault("client_id", "client")
        kwargs.setdefault("client_secret", "secret")
        return TokenManager(
            kwargs.pop("access_token", "access-1"),
            kwargs.pop("refresh_token", "refresh-1"),
            token_url=TOKEN_URL,
            http_client=httpx.Client(transport=self.transport),
            **kwargs,
        )

    def sdk(self, manager: TokenManager) -> Textql:
        auth = TokenAuth(manager)
        return Textql(
            server_url=FAKE_BASE_URL,
            client=httpx.Client(transport=self.transport, auth=auth),
            async_client=httpx.AsyncClient(transport=self.transport, auth=auth),
        )

    def api_requests(self):
        return [r for r in self.transport.requests if r.url.path != "/oauth/token"]


def test_sends_bearer_and_drops_env_api_key(monkeypatch):
    monkeypatch.setenv("TEXTQL_API_KEY", "env-key")
    server = FakeServer()
    sdk = server.sdk(server.manager(expires_in=3600))

    assert sdk.chats.create_chat(message="hi").chat.id == "chat-1"

    req = server.api_requests()[-1]
    assert req.headers["authorization"] == "Bearer access-1"
    assert "tql_api_key" not in req.headers
    assert server.refreshes == 0


def test_refreshes_and_retries_once_on_401(monkeypatch):
    monkeypatch.delenv("TEXTQL_API_KEY", raising=False)
    server = FakeServer(valid_token="revoked-elsewhere")
    seen = []
    sdk = server.sdk(server.manager(on_tokens=seen.append))

    assert sdk.chats.create_chat(message="hi").chat.id == "chat-1"

    attempts = server.api_requests()
    assert [r.headers["authorization"] for r in attempts] == [
        "Bearer access-1",
        "Bearer access-2",
    ]
    assert attempts[1].content == attempts[0].content
    assert server.refreshes == 1
    assert [t.refresh_token for t in seen] == ["refresh-2"]


def test_refreshes_before_expiry_without_a_401(monkeypatch):
    monkeypatch.delenv("TEXTQL_API_KEY", raising=False)
    server = FakeServer(valid_token="access-2")
    manager = server.manager(expires_at=time.time() + 30)

    server.sdk(manager).chats.create_chat(message="hi")

    assert [r.headers["authorization"] for r in server.api_requests()] == [
        "Bearer access-2"
    ]
    assert manager.tokens.refresh_token == "refresh-2"
    assert manager.tokens.expires_at > time.time() + 3000


@pytest.mark.asyncio
async def test_async_client_refreshes_on_401(monkeypatch):
    monkeypatch.delenv("TEXTQL_API_KEY", raising=False)
    server = FakeServer(valid_token="revoked-elsewhere")
    sdk = server.sdk(server.manager())

    result = await sdk.chats.create_chat_async(message="hi")

    assert result.chat.id == "chat-1"
    assert server.refreshes == 1


def test_stale_token_already_refreshed_by_another_caller_is_not_replayed():
    server = FakeServer()
    manager = server.manager()

    assert manager.access_token(stale="access-1") == "access-2"
    assert manager.access_token(stale="access-1") == "access-2"
    assert server.refreshes == 1


def test_without_refresh_token_401_is_returned_unchanged(monkeypatch):
    monkeypatch.delenv("TEXTQL_API_KEY", raising=False)
    server = FakeServer(valid_token="other")
    manager = server.manager(refresh_token=None)

    with pytest.raises(Exception):
        server.sdk(manager).chats.create_chat(message="hi")

    assert len(server.api_requests()) == 1
    assert server.refreshes == 0


def test_rejected_refresh_raises_oauth_error():
    server = FakeServer(refresh_token="rotated-elsewhere")
    manager = server.manager(expires_at=time.time())

    with pytest.raises(OAuthRefreshError) as exc:
        manager.access_token()

    assert exc.value.error == "invalid_grant"
    assert exc.value.status_code == 400


def test_from_tokens_derives_token_url_and_exposes_manager():
    sdk = from_tokens(
        "access-1",
        "refresh-1",
        client_id="client",
        client_secret="secret",
        server_url="https://tenant.example.com/rpc/public",
    )

    manager = token_manager_of(sdk)
    assert manager is not None
    assert manager._token_url == "https://tenant.example.com/oauth/token"


def test_from_tokens_rejects_api_key():
    with pytest.raises(ValueError):
        from_tokens("access-1", api_key="key")


def test_refresh_token_requires_client_id():
    with pytest.raises(ValueError):
        TokenManager("access-1", "refresh-1")


def test_authorization_url_uses_s256_pkce():
    req = authorization_url(
        "client",
        "https://tool.example.com/callback",
        scopes=["api:read", "api:write"],
        server_url="https://tenant.example.com/rpc/public",
    )

    url = urlparse(req.url)
    params = {k: v[0] for k, v in parse_qs(url.query).items()}
    assert f"{url.scheme}://{url.netloc}{url.path}" == "https://tenant.example.com/oauth/authorize"
    assert params["response_type"] == "code"
    assert params["client_id"] == "client"
    assert params["redirect_uri"] == "https://tool.example.com/callback"
    assert params["scope"] == "api:read api:write"
    assert params["state"] == req.state
    assert params["code_challenge_method"] == "S256"
    expected = base64.urlsafe_b64encode(
        hashlib.sha256(req.code_verifier.encode()).digest()
    ).rstrip(b"=").decode()
    assert params["code_challenge"] == expected


def test_exchange_code_posts_authorization_code_grant():
    captured = {}

    def handler(request):
        captured.update({k: v[0] for k, v in parse_qs(request.content.decode()).items()})
        captured["url"] = str(request.url)
        return json_response(
            200,
            {"access_token": "access-1", "expires_in": 3600, "refresh_token": "refresh-1"},
        )

    tokens = exchange_code(
        "code-1",
        client_id="client",
        client_secret="secret",
        redirect_uri="https://tool.example.com/callback",
        code_verifier="verifier",
        server_url="https://tenant.example.com",
        http_client=httpx.Client(transport=RecordingTransport(handler)),
    )

    assert captured == {
        "url": "https://tenant.example.com/oauth/token",
        "grant_type": "authorization_code",
        "code": "code-1",
        "client_id": "client",
        "client_secret": "secret",
        "redirect_uri": "https://tool.example.com/callback",
        "code_verifier": "verifier",
    }
    assert tokens.access_token == "access-1"
    assert tokens.refresh_token == "refresh-1"
    assert tokens.expires_at > time.time() + 3000
