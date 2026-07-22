import httpx

from .types import BeforeRequestContext, BeforeRequestHook, Hooks

_RPC_PREFIX = "/rpc/public"


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
    hooks.register_before_request_hook(_RPCPublicPrefixHook())
