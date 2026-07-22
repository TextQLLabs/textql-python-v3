"""Streaming bridge over Connect-RPC.

The TextQL API exposes several server-streaming RPCs that have no HTTP/JSON
shape in the OpenAPI spec, so they are not part of the Speakeasy-generated SDK
surface. This module bridges them with Connect-RPC (https://connectrpc.com),
talking the Connect protocol directly to the same gateway, authenticated with
the same ``tql_api_key`` header.

Configure the server and API key once on the :class:`~textql_sdk.Textql` SDK;
streaming inherits both -- you never pass a server URL or think about the
``/rpc/public`` mount::

    from textql_sdk import Textql
    from textql_sdk.streaming import create_streaming_client

    sdk = Textql(api_key=..., server_url=...)   # server_url optional
    streaming = create_streaming_client(sdk)
    async for event in streaming.chats.watch_chat(WatchChatRequest(chat_id=chat_id)):
        ...

Without an SDK instance, pass ``api_key`` directly; ``server_url`` defaults to
the same server list the generated SDK uses (from the Speakeasy config).

Server-streaming methods: ``chats.watch_chat``, ``chats.stream_chat``,
``agents.stream_agent_status``, ``apps.stream_app_activity``,
``dashboards.watch_dashboard_health``,
``playbooks.stream_template_data_status``. Unary RPCs on these clients work too,
but prefer the generated :class:`~textql_sdk.Textql` SDK for those.

For any other service under :mod:`textql_sdk._connect`, use
:func:`create_connect_client` as an escape hatch.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple, TypeVar
from urllib.parse import urlparse

from connectrpc.client import ConnectClient, ConnectClientSync
from connectrpc.request import RequestContext

from .sdk import Textql
from .sdkconfiguration import SERVERS
from ._connect.public.agent_connect import AgentServiceClient, AgentServiceClientSync
from ._connect.public.apps_connect import AppServiceClient, AppServiceClientSync
from ._connect.public.chat_connect import ChatServiceClient, ChatServiceClientSync
from ._connect.public.dashboard_connect import (
    DashboardServiceClient,
    DashboardServiceClientSync,
)
from ._connect.public.playbook_connect import (
    PlaybookServiceClient,
    PlaybookServiceClientSync,
)

_AsyncClientT = TypeVar("_AsyncClientT", bound=ConnectClient)
_SyncClientT = TypeVar("_SyncClientT", bound=ConnectClientSync)


def _rpc_base_url(server_url: str) -> str:
    """Connect RPCs are always mounted at ``/rpc/public`` on the host. Append it
    to whatever base the SDK provides -- idempotently, so a base that already
    carries the prefix isn't doubled."""
    url = urlparse(server_url)
    base = url.path.rstrip("/")
    path = base if base.endswith("/rpc/public") else f"{base}/rpc/public"
    return f"{url.scheme}://{url.netloc}{path}"


def _resolve(
    sdk: Optional[Textql], api_key: Optional[str], server_url: Optional[str]
) -> Tuple[str, str]:
    """Resolve (base address, api_key), preferring explicit args, then a
    configured SDK, then the generated server default."""
    if sdk is not None:
        config = sdk.sdk_configuration
        if server_url is None:
            server_url = config.get_server_details()[0]
        if api_key is None:
            security = config.security() if callable(config.security) else config.security
            api_key = security.api_key if security is not None else None
    if server_url is None:
        server_url = SERVERS[0]
    if not api_key:
        raise ValueError(
            "no api_key available: pass api_key=... or an sdk configured with one"
        )
    return _rpc_base_url(server_url), api_key


class _ApiKeyInterceptor:
    """Async metadata interceptor that attaches the ``tql_api_key`` header."""

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def on_start(self, ctx: RequestContext) -> None:
        ctx.request_headers()["tql_api_key"] = self._api_key

    async def on_end(
        self, token: None, ctx: RequestContext, error: Optional[Exception]
    ) -> None:
        return None


class _ApiKeyInterceptorSync:
    """Sync metadata interceptor that attaches the ``tql_api_key`` header."""

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    def on_start_sync(self, ctx: RequestContext) -> None:
        ctx.request_headers()["tql_api_key"] = self._api_key

    def on_end_sync(
        self, token: None, ctx: RequestContext, error: Optional[Exception]
    ) -> None:
        return None


def create_connect_client(
    service_client: type[_AsyncClientT],
    sdk: Optional[Textql] = None,
    *,
    api_key: Optional[str] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
) -> _AsyncClientT:
    """Build an authenticated async Connect client for a single service.

    Escape hatch for services not covered by :func:`create_streaming_client` --
    pass any generated ``*ServiceClient`` class from :mod:`textql_sdk._connect`::

        from textql_sdk.streaming import create_connect_client
        from textql_sdk._connect.public.feed_connect import FeedServiceClient

        feed = create_connect_client(FeedServiceClient, sdk)
    """
    address, key = _resolve(sdk, api_key, server_url)
    return service_client(
        address, interceptors=[_ApiKeyInterceptor(key)], timeout_ms=timeout_ms
    )


def create_connect_client_sync(
    service_client: type[_SyncClientT],
    sdk: Optional[Textql] = None,
    *,
    api_key: Optional[str] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
) -> _SyncClientT:
    """Sync counterpart to :func:`create_connect_client` -- pass a generated
    ``*ServiceClientSync`` class."""
    address, key = _resolve(sdk, api_key, server_url)
    return service_client(
        address, interceptors=[_ApiKeyInterceptorSync(key)], timeout_ms=timeout_ms
    )


@dataclass
class StreamingClient:
    """Async Connect clients for the server-streaming services. Streaming
    methods return async iterators of protobuf messages."""

    agents: AgentServiceClient
    apps: AppServiceClient
    chats: ChatServiceClient
    dashboards: DashboardServiceClient
    playbooks: PlaybookServiceClient


@dataclass
class StreamingClientSync:
    """Sync counterpart to :class:`StreamingClient`. Streaming methods return
    plain iterators of protobuf messages."""

    agents: AgentServiceClientSync
    apps: AppServiceClientSync
    chats: ChatServiceClientSync
    dashboards: DashboardServiceClientSync
    playbooks: PlaybookServiceClientSync


def create_streaming_client(
    sdk: Optional[Textql] = None,
    *,
    api_key: Optional[str] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
) -> StreamingClient:
    """Streaming bridge over Connect-RPC for the server-streaming endpoints that
    have no HTTP/JSON shape in the OpenAPI spec.

    Pass a configured :class:`~textql_sdk.Textql` to inherit its server and API
    key, or pass ``api_key`` directly.

    Server-streaming methods: ``chats.watch_chat``, ``chats.stream_chat``,
    ``agents.stream_agent_status``, ``apps.stream_app_activity``,
    ``dashboards.watch_dashboard_health``,
    ``playbooks.stream_template_data_status``.
    """
    address, key = _resolve(sdk, api_key, server_url)
    interceptor = _ApiKeyInterceptor(key)

    def build(service_client: type[_AsyncClientT]) -> _AsyncClientT:
        return service_client(
            address, interceptors=[interceptor], timeout_ms=timeout_ms
        )

    return StreamingClient(
        agents=build(AgentServiceClient),
        apps=build(AppServiceClient),
        chats=build(ChatServiceClient),
        dashboards=build(DashboardServiceClient),
        playbooks=build(PlaybookServiceClient),
    )


def create_streaming_client_sync(
    sdk: Optional[Textql] = None,
    *,
    api_key: Optional[str] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
) -> StreamingClientSync:
    """Sync counterpart to :func:`create_streaming_client`. Streaming methods
    return plain iterators (usable in a ``for`` loop)."""
    address, key = _resolve(sdk, api_key, server_url)
    interceptor = _ApiKeyInterceptorSync(key)

    def build(service_client: type[_SyncClientT]) -> _SyncClientT:
        return service_client(
            address, interceptors=[interceptor], timeout_ms=timeout_ms
        )

    return StreamingClientSync(
        agents=build(AgentServiceClientSync),
        apps=build(AppServiceClientSync),
        chats=build(ChatServiceClientSync),
        dashboards=build(DashboardServiceClientSync),
        playbooks=build(PlaybookServiceClientSync),
    )


__all__ = [
    "StreamingClient",
    "StreamingClientSync",
    "create_connect_client",
    "create_connect_client_sync",
    "create_streaming_client",
    "create_streaming_client_sync",
]
