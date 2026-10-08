"""Streaming bridge over Connect-RPC.

The TextQL API exposes several server-streaming RPCs that have no HTTP/JSON
shape in the OpenAPI spec, so they are not part of the Speakeasy-generated SDK
surface. This module bridges them with Connect-RPC (https://connectrpc.com),
talking the Connect protocol directly to the same gateway, authenticated with
the same ``tql_api_key`` header, or with ``Authorization: Bearer`` when the SDK
was built with :func:`textql_sdk.oauth.from_tokens`.

Configure the server and API key once on the :class:`~textql_sdk.Textql` SDK;
streaming inherits both -- you never pass a server URL or think about the
``/rpc/public`` mount::

    from textql_sdk import Textql
    from textql_sdk.streaming import create_streaming_client

    sdk = Textql(api_key=..., server_url=...)   # server_url optional
    streaming = create_streaming_client(sdk)
    async for event in streaming.chats.watch_chat(WatchChatRequest(chat_id=chat_id)):
        ...

Without an SDK instance, pass ``api_key`` directly; ``server_url`` falls back to
``TEXTQL_SERVER_URL``, then to the same server list the generated SDK uses (from
the Speakeasy config).

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
from typing import Optional, Tuple, TypeVar, Union
from urllib.parse import urlparse

from connectrpc.client import ConnectClient, ConnectClientSync
from connectrpc.code import Code
from connectrpc.errors import ConnectError
from connectrpc.request import RequestContext

# The Connect transport is pyqwest, not httpx. Imported under the same aliases
# connectrpc.client uses, so the `http_client` annotations below match what
# ConnectClient actually accepts.
from pyqwest import Client as HTTPClient
from pyqwest import SyncClient as SyncHTTPClient

from .sdk import Textql
from ._hooks.registration import server_url_from_env
from .oauth import TokenManager, token_manager_of
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


_Credential = Union[str, TokenManager]


def _resolve(
    sdk: Optional[Textql],
    api_key: Optional[str],
    server_url: Optional[str],
    tokens: Optional[TokenManager] = None,
) -> Tuple[str, _Credential]:
    """Resolve (base address, credential), preferring explicit args, then a
    configured SDK, then ``TEXTQL_SERVER_URL``, then the generated default.
    The credential is an api key or a :class:`TokenManager`."""
    credential: Optional[_Credential] = tokens or api_key
    if sdk is not None:
        config = sdk.sdk_configuration
        if server_url is None:
            server_url = config.get_server_details()[0]
        if credential is None:
            credential = token_manager_of(sdk)
        if credential is None:
            security = config.security() if callable(config.security) else config.security
            credential = security.api_key if security is not None else None
    if server_url is None:
        server_url = server_url_from_env() or SERVERS[0]
    if not credential:
        raise ValueError(
            "no credentials available: pass api_key=..., tokens=..., or an sdk "
            "configured with either"
        )
    return _rpc_base_url(server_url), credential


class _ApiKeyInterceptor:
    """Async metadata interceptor that attaches the ``tql_api_key`` header."""

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def on_start(self, ctx: RequestContext) -> None:
        ctx.request_headers()["tql_api_key"] = self._api_key

    # pylint: disable=unused-argument
    # Parameter names must match MetadataInterceptor exactly: the protocol does
    # not mark them positional-only, so pyright matches structurally by name.
    # Renaming them (e.g. to _token) silently breaks conformance even though
    # connectrpc only ever calls this positionally.
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

    # pylint: disable=unused-argument
    # See _ApiKeyInterceptor.on_end -- names are load-bearing for the protocol.
    def on_end_sync(
        self, token: None, ctx: RequestContext, error: Optional[Exception]
    ) -> None:
        return None


class _TokenInterceptor:
    """Async metadata interceptor that attaches ``Authorization: Bearer``.

    A stream cannot be replayed after a 401, so an ``unauthenticated`` error
    refreshes the token for the next call and still surfaces to the caller."""

    def __init__(self, manager: TokenManager) -> None:
        self._manager = manager

    async def on_start(self, ctx: RequestContext) -> str:
        token = await self._manager.access_token_async()
        ctx.request_headers()["authorization"] = f"Bearer {token}"
        return token

    # pylint: disable=unused-argument
    # See _ApiKeyInterceptor.on_end -- names are load-bearing for the protocol.
    async def on_end(
        self, token: str, ctx: RequestContext, error: Optional[Exception]
    ) -> None:
        if _unauthenticated(error):
            await self._manager.access_token_async(stale=token)


class _TokenInterceptorSync:
    """Sync counterpart to :class:`_TokenInterceptor`."""

    def __init__(self, manager: TokenManager) -> None:
        self._manager = manager

    def on_start_sync(self, ctx: RequestContext) -> str:
        token = self._manager.access_token()
        ctx.request_headers()["authorization"] = f"Bearer {token}"
        return token

    # pylint: disable=unused-argument
    # See _ApiKeyInterceptor.on_end -- names are load-bearing for the protocol.
    def on_end_sync(
        self, token: str, ctx: RequestContext, error: Optional[Exception]
    ) -> None:
        if _unauthenticated(error):
            self._manager.access_token(stale=token)


def _unauthenticated(error: Optional[Exception]) -> bool:
    return isinstance(error, ConnectError) and error.code == Code.UNAUTHENTICATED


def _interceptor(credential: _Credential):
    if isinstance(credential, TokenManager):
        return _TokenInterceptor(credential)
    return _ApiKeyInterceptor(credential)


def _interceptor_sync(credential: _Credential):
    if isinstance(credential, TokenManager):
        return _TokenInterceptorSync(credential)
    return _ApiKeyInterceptorSync(credential)


def create_connect_client(
    service_client: type[_AsyncClientT],
    sdk: Optional[Textql] = None,
    *,
    api_key: Optional[str] = None,
    tokens: Optional[TokenManager] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_client: Optional[HTTPClient] = None,
) -> _AsyncClientT:
    """Build an authenticated async Connect client for a single service.

    Escape hatch for services not covered by :func:`create_streaming_client` --
    pass any generated ``*ServiceClient`` class from :mod:`textql_sdk._connect`::

        from textql_sdk.streaming import create_connect_client
        from textql_sdk._connect.public.feed_connect import FeedServiceClient

        feed = create_connect_client(FeedServiceClient, sdk)

    ``http_client`` accepts a ``pyqwest.Client`` for custom TLS -- see
    :func:`create_streaming_client`.
    """
    address, credential = _resolve(sdk, api_key, server_url, tokens)
    return service_client(
        address,
        interceptors=[_interceptor(credential)],
        timeout_ms=timeout_ms,
        http_client=http_client,
    )


def create_connect_client_sync(
    service_client: type[_SyncClientT],
    sdk: Optional[Textql] = None,
    *,
    api_key: Optional[str] = None,
    tokens: Optional[TokenManager] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_client: Optional[SyncHTTPClient] = None,
) -> _SyncClientT:
    """Sync counterpart to :func:`create_connect_client` -- pass a generated
    ``*ServiceClientSync`` class."""
    address, credential = _resolve(sdk, api_key, server_url, tokens)
    return service_client(
        address,
        interceptors=[_interceptor_sync(credential)],
        timeout_ms=timeout_ms,
        http_client=http_client,
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
    tokens: Optional[TokenManager] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_client: Optional[HTTPClient] = None,
) -> StreamingClient:
    """Streaming bridge over Connect-RPC for the server-streaming endpoints that
    have no HTTP/JSON shape in the OpenAPI spec.

    Pass a configured :class:`~textql_sdk.Textql` to inherit its server and
    credentials (an API key, or the token pair from
    :func:`textql_sdk.oauth.from_tokens`), or pass ``api_key`` or ``tokens``
    directly.

    Server-streaming methods: ``chats.watch_chat``, ``chats.stream_chat``,
    ``agents.stream_agent_status``, ``apps.stream_app_activity``,
    ``dashboards.watch_dashboard_health``,
    ``playbooks.stream_template_data_status``.

    ``http_client`` takes a ``pyqwest.Client`` when you need custom TLS -- a
    private CA or mTLS. This transport is independent of the ``httpx`` client on
    the ``Textql`` SDK, so ``verify=`` there does not apply here and both must be
    configured. A transport you build yourself trusts *nothing* unless you pass
    ``tls_include_system_certs=True``::

        import pyqwest
        transport = pyqwest.HTTPTransport(
            tls_ca_cert=pathlib.Path("corp-ca.pem").read_bytes(),
            tls_include_system_certs=True,
        )
        streaming = create_streaming_client(sdk, http_client=pyqwest.Client(transport))

    Leave it as ``None`` to use the shared default transport, which already
    trusts the system store.
    """
    address, credential = _resolve(sdk, api_key, server_url, tokens)
    interceptor = _interceptor(credential)

    def build(service_client: type[_AsyncClientT]) -> _AsyncClientT:
        return service_client(
            address,
            interceptors=[interceptor],
            timeout_ms=timeout_ms,
            http_client=http_client,
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
    tokens: Optional[TokenManager] = None,
    server_url: Optional[str] = None,
    timeout_ms: Optional[int] = None,
    http_client: Optional[SyncHTTPClient] = None,
) -> StreamingClientSync:
    """Sync counterpart to :func:`create_streaming_client`. Streaming methods
    return plain iterators (usable in a ``for`` loop). ``http_client`` takes a
    ``pyqwest.SyncClient``."""
    address, credential = _resolve(sdk, api_key, server_url, tokens)
    interceptor = _interceptor_sync(credential)

    def build(service_client: type[_SyncClientT]) -> _SyncClientT:
        return service_client(
            address,
            interceptors=[interceptor],
            timeout_ms=timeout_ms,
            http_client=http_client,
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
