"""Unit tests for textql_sdk._hooks.SDKHooks -- the before_request/after_success/after_error hook chain."""
import httpx
import pytest

from textql_sdk._hooks import (
    AfterErrorContext,
    AfterErrorHook,
    AfterSuccessContext,
    AfterSuccessHook,
    BeforeRequestContext,
    BeforeRequestHook,
    HookContext,
    SDKHooks,
    SDKInitHook,
)
from textql_sdk.sdkconfiguration import SERVERS, SDKConfiguration
from textql_sdk.utils.logger import get_default_logger


def _sdk_config(**overrides):
    """A real SDKConfiguration, since the SDK's own init hooks read its fields."""
    return SDKConfiguration(
        client=None,
        client_supplied=False,
        async_client=None,
        async_client_supplied=False,
        debug_logger=get_default_logger(),
        server_url=overrides.get("server_url"),
        server_idx=overrides.get("server_idx"),
    )


def _hook_ctx(config=None):
    return HookContext(
        config=config,
        base_url="https://example.invalid",
        operation_id="Test_Op",
        oauth2_scopes=None,
        security_source=None,
        tags=["Test"],
        extensions=None,
    )


class RecordingBeforeRequestHook(BeforeRequestHook):
    def __init__(self, add_header=None):
        self.calls = []
        self.add_header = add_header

    def before_request(self, hook_ctx, request):
        self.calls.append(hook_ctx.operation_id)
        if self.add_header:
            k, v = self.add_header
            request.headers[k] = v
        return request


class ShortCircuitBeforeRequestHook(BeforeRequestHook):
    def __init__(self, exc):
        self.exc = exc

    def before_request(self, hook_ctx, request):
        return self.exc


class RecordingAfterSuccessHook(AfterSuccessHook):
    def __init__(self):
        self.calls = 0

    def after_success(self, hook_ctx, response):
        self.calls += 1
        return response


class RecordingAfterErrorHook(AfterErrorHook):
    def __init__(self, result=None):
        self.seen = []
        self.result = result

    def after_error(self, hook_ctx, response, error):
        self.seen.append((response, error))
        if self.result is not None:
            return self.result
        return response, error


class TestBeforeRequestChain:
    def test_hooks_run_in_registration_order_and_can_mutate_request(self):
        hooks = SDKHooks()
        h1 = RecordingBeforeRequestHook(add_header=("X-First", "1"))
        h2 = RecordingBeforeRequestHook(add_header=("X-Second", "2"))
        hooks.register_before_request_hook(h1)
        hooks.register_before_request_hook(h2)

        req = httpx.Request("GET", "https://example.invalid/")
        result = hooks.before_request(_hook_ctx(), req)

        assert h1.calls == ["Test_Op"]
        assert h2.calls == ["Test_Op"]
        assert result.headers["X-First"] == "1"
        assert result.headers["X-Second"] == "2"

    def test_hook_returning_exception_raises_it(self):
        hooks = SDKHooks()
        boom = ValueError("nope")
        hooks.register_before_request_hook(ShortCircuitBeforeRequestHook(boom))

        req = httpx.Request("GET", "https://example.invalid/")
        with pytest.raises(ValueError, match="nope"):
            hooks.before_request(_hook_ctx(), req)

    def test_no_hooks_registered_returns_request_unchanged(self):
        hooks = SDKHooks()
        req = httpx.Request("GET", "https://example.invalid/")
        result = hooks.before_request(_hook_ctx(), req)
        assert result is req


class TestAfterSuccessChain:
    def test_hooks_run_and_see_response(self):
        hooks = SDKHooks()
        hook = RecordingAfterSuccessHook()
        hooks.register_after_success_hook(hook)

        resp = httpx.Response(200)
        result = hooks.after_success(_hook_ctx(), resp)

        assert hook.calls == 1
        assert result is resp

    def test_hook_returning_exception_raises_it(self):
        class Boom(AfterSuccessHook):
            def after_success(self, hook_ctx, response):
                return RuntimeError("boom")

        hooks = SDKHooks()
        hooks.register_after_success_hook(Boom())

        with pytest.raises(RuntimeError, match="boom"):
            hooks.after_success(_hook_ctx(), httpx.Response(200))


class TestAfterErrorChain:
    def test_hooks_see_response_and_error(self):
        hooks = SDKHooks()
        hook = RecordingAfterErrorHook()
        hooks.register_after_error_hook(hook)

        resp = httpx.Response(500)
        result_resp, result_err = hooks.after_error(_hook_ctx(), resp, None)

        assert hook.seen == [(resp, None)]
        assert result_resp is resp
        assert result_err is None

    def test_hook_can_swallow_error_by_returning_none_none(self):
        hooks = SDKHooks()
        hooks.register_after_error_hook(RecordingAfterErrorHook(result=(None, None)))

        resp, err = hooks.after_error(_hook_ctx(), None, ValueError("transport failed"))

        assert resp is None
        assert err is None

    def test_hook_returning_exception_directly_raises_it(self):
        class Boom(AfterErrorHook):
            def after_error(self, hook_ctx, response, error):
                return KeyError("escalated")

        hooks = SDKHooks()
        hooks.register_after_error_hook(Boom())

        with pytest.raises(KeyError):
            hooks.after_error(_hook_ctx(), None, ValueError("orig"))

    def test_chained_hooks_each_see_previous_hooks_output(self):
        class ReplaceError(AfterErrorHook):
            def after_error(self, hook_ctx, response, error):
                return response, RuntimeError("replaced")

        recorder = RecordingAfterErrorHook()
        hooks = SDKHooks()
        hooks.register_after_error_hook(ReplaceError())
        hooks.register_after_error_hook(recorder)

        hooks.after_error(_hook_ctx(), None, ValueError("orig"))

        assert isinstance(recorder.seen[0][1], RuntimeError)
        assert str(recorder.seen[0][1]) == "replaced"


class TestSdkInitHook:
    # SDKHooks() registers the SDK's own init hooks, which read real
    # SDKConfiguration fields, so these pass a config rather than a bare stub.
    def test_sdk_init_hooks_can_transform_config(self):
        class SetLanguage(SDKInitHook):
            def sdk_init(self, config):
                config.language = "python-modified"
                return config

        hooks = SDKHooks()
        hooks.register_sdk_init_hook(SetLanguage())

        result = hooks.sdk_init(_sdk_config())
        assert result.language == "python-modified"

    def test_registered_hooks_are_applied_in_order(self):
        class Append(SDKInitHook):
            def __init__(self, suffix):
                self.suffix = suffix

            def sdk_init(self, config):
                config.language += self.suffix
                return config

        hooks = SDKHooks()
        hooks.register_sdk_init_hook(Append("-one"))
        hooks.register_sdk_init_hook(Append("-two"))

        assert hooks.sdk_init(_sdk_config()).language == "python-one-two"

    def test_server_url_read_from_env(self, monkeypatch):
        monkeypatch.setenv("TEXTQL_SERVER_URL", "https://textql.internal.example.com")
        config = SDKHooks().sdk_init(_sdk_config())
        assert config.get_server_details()[0] == "https://textql.internal.example.com"

    def test_explicit_server_url_beats_env(self, monkeypatch):
        monkeypatch.setenv("TEXTQL_SERVER_URL", "https://textql.internal.example.com")
        config = SDKHooks().sdk_init(_sdk_config(server_url="https://explicit.example.com"))
        assert config.get_server_details()[0] == "https://explicit.example.com"

    def test_falls_back_to_generated_default(self, monkeypatch):
        monkeypatch.delenv("TEXTQL_SERVER_URL", raising=False)
        config = SDKHooks().sdk_init(_sdk_config())
        assert config.get_server_details()[0] == SERVERS[0]
