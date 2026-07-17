"""Shared mock-transport test harness used by every file under tests/unit."""

from __future__ import annotations

import json as _json
from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional

import httpx
import pytest

from textql_sdk import Textql

FAKE_API_KEY = "test-tql-api-key-123"
FAKE_BASE_URL = "https://textql-sdk-tests.invalid"

# The header name the SDK sends the API key under. See
# src/textql_sdk/models/security.py (`field_name="tql_api_key"`).
AUTH_HEADER_NAME = "tql_api_key"

Handler = Callable[[httpx.Request], httpx.Response]


class RecordingTransport(httpx.BaseTransport, httpx.AsyncBaseTransport):
    """Records every request and delegates response generation to a handler.
    Works for both sync and async SDK clients."""

    def __init__(self, handler: Handler):
        self.handler = handler
        self.requests: List[httpx.Request] = []

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        # Force-read streamed request bodies now so callers can inspect
        # request.content after the (sync) call returns.
        request.read()
        self.requests.append(request)
        return self.handler(request)

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        await request.aread()
        self.requests.append(request)
        return self.handler(request)

    @property
    def last_request(self) -> httpx.Request:
        assert self.requests, "no request was recorded"
        return self.requests[-1]

    def body_json(self, index: int = -1) -> Any:
        req = self.requests[index]
        if not req.content:
            return None
        return _json.loads(req.content)


@dataclass
class MockedSDK:
    """A live Textql instance plus the transport recording its traffic."""

    sdk: Textql
    transport: RecordingTransport

    def close(self):
        self.sdk.__exit__(None, None, None)


def json_response(
    status_code: int,
    payload: Any,
    headers: Optional[dict] = None,
) -> httpx.Response:
    hdrs = {"content-type": "application/json"}
    if headers:
        hdrs.update(headers)
    return httpx.Response(status_code, content=_json.dumps(payload), headers=hdrs)


def text_response(
    status_code: int,
    text: str,
    content_type: str = "text/plain",
    headers: Optional[dict] = None,
) -> httpx.Response:
    hdrs = {"content-type": content_type}
    if headers:
        hdrs.update(headers)
    return httpx.Response(status_code, content=text, headers=hdrs)


@pytest.fixture
def make_sdk(monkeypatch):
    """Factory: make_sdk(handler, **textql_kwargs) -> MockedSDK. `handler`
    takes an httpx.Request and returns an httpx.Response for both clients."""
    monkeypatch.delenv("TEXTQL_API_KEY", raising=False)

    created: List[MockedSDK] = []

    def _make(handler: Handler, *, api_key: Optional[str] = FAKE_API_KEY, **kwargs) -> MockedSDK:
        transport = RecordingTransport(handler)
        client = httpx.Client(transport=transport, base_url=FAKE_BASE_URL)
        async_client = httpx.AsyncClient(transport=transport, base_url=FAKE_BASE_URL)
        sdk = Textql(
            api_key=api_key,
            server_url=FAKE_BASE_URL,
            client=client,
            async_client=async_client,
            **kwargs,
        )
        bundle = MockedSDK(sdk=sdk, transport=transport)
        created.append(bundle)
        return bundle

    yield _make

    for bundle in created:
        try:
            bundle.close()
        except Exception:
            pass


@pytest.fixture
def sequence_handler():
    """Factory: sequence_handler([resp1, resp2, ...]) -> handler returning
    responses in order, raising if called more times than queued."""

    def _make(responses: List[httpx.Response]) -> Handler:
        it = iter(responses)

        def handler(request: httpx.Request) -> httpx.Response:
            try:
                return next(it)
            except StopIteration as exc:
                raise AssertionError(
                    f"handler called more times than responses were queued "
                    f"(request: {request.method} {request.url})"
                ) from exc

        return handler

    return _make
