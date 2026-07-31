import os

import httpx

from ..sdkconfiguration import SDKConfiguration
from .types import BeforeRequestContext, BeforeRequestHook, Hooks, SDKInitHook

_RPC_PREFIX = "/rpc/public"


def server_url_from_env() -> str:
    """The deployment every client talks to. An on-prem install sets this once
    instead of passing ``server_url`` at each construction site. The plain host
    belongs here; ``_RPCPublicPrefixHook`` appends ``/rpc/public``."""
    return (os.getenv("TEXTQL_SERVER_URL") or "").strip()


class _ServerURLFromEnvHook(SDKInitHook):
    """Points every client at ``TEXTQL_SERVER_URL``. Runs before
    ``get_server_details`` resolves a base, so precedence is an explicit
    ``server_url``/``server_idx``, then the environment, then ``SERVERS[0]`` --
    which is ``app.textql.com`` and is the wrong answer everywhere on-prem."""

    def sdk_init(self, config: SDKConfiguration) -> SDKConfiguration:
        if config.server_url or config.server_idx is not None:
            return config
        server_url = server_url_from_env()
        if server_url:
            config.server_url = server_url
        return config


class _RPCPublicPrefixHook(BeforeRequestHook):
    """Connect RPCs are mounted under ``/rpc/public`` on the host, but the
    generated operations build paths like ``/textql.rpc.public.<svc>/<method>``
    off a bare base URL. Insert the mount prefix so callers can point
    ``TEXTQL_SERVER_URL`` at the plain host (e.g. ``https://app.textql.com``).
    Idempotent -- a base that already carries the prefix isn't doubled."""

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> httpx.Request:
        path = request.url.path
        if _RPC_PREFIX in path or not path.startswith("/textql."):
            return request
        request.url = request.url.copy_with(path=f"{_RPC_PREFIX}{path}")
        return request


def init_hooks(hooks: Hooks):
    """Add hooks by calling hooks.register{sdk_init/before_request/after_success/after_error}Hook
    with an instance of a hook that implements that specific Hook interface
    Hooks are registered per SDK instance, and are valid for the lifetime of the SDK instance"""
    hooks.register_sdk_init_hook(_ServerURLFromEnvHook())
    hooks.register_before_request_hook(_RPCPublicPrefixHook())
