"""Unit tests for Textql.__init__, lazy sub-SDK loading, and context-manager lifecycle."""
import httpx
import pytest

from textql_sdk import Textql, models
from textql_sdk.sdkconfiguration import SERVERS


class TestConstructorDefaults:
    def test_default_server_url_is_used_when_none_given(self):
        sdk = Textql(api_key="k")
        try:
            url, _vars = sdk.sdk_configuration.get_server_details()
            assert url == SERVERS[0]
        finally:
            sdk.__exit__(None, None, None)

    def test_explicit_server_url_overrides_default(self):
        sdk = Textql(api_key="k", server_url="https://custom.example.com/")
        try:
            url, _vars = sdk.sdk_configuration.get_server_details()
            # trailing slash is stripped by remove_suffix
            assert url == "https://custom.example.com"
        finally:
            sdk.__exit__(None, None, None)

    def test_server_url_with_url_params_is_templated(self):
        sdk = Textql(
            api_key="k",
            server_url="https://{tenant}.example.com",
            url_params={"tenant": "acme"},
        )
        try:
            url, _vars = sdk.sdk_configuration.get_server_details()
            assert url == "https://acme.example.com"
        finally:
            sdk.__exit__(None, None, None)

    def test_default_clients_are_created_when_not_supplied(self):
        sdk = Textql(api_key="k")
        try:
            assert isinstance(sdk.sdk_configuration.client, httpx.Client)
            assert isinstance(sdk.sdk_configuration.async_client, httpx.AsyncClient)
            assert sdk.sdk_configuration.client_supplied is False
            assert sdk.sdk_configuration.async_client_supplied is False
        finally:
            sdk.__exit__(None, None, None)

    def test_supplied_clients_are_marked_as_supplied(self):
        client = httpx.Client()
        async_client = httpx.AsyncClient()
        sdk = Textql(api_key="k", client=client, async_client=async_client)
        try:
            assert sdk.sdk_configuration.client is client
            assert sdk.sdk_configuration.async_client is async_client
            assert sdk.sdk_configuration.client_supplied is True
            assert sdk.sdk_configuration.async_client_supplied is True
        finally:
            sdk.__exit__(None, None, None)
            client.close()


class TestApiKeyHandling:
    def test_string_api_key_produces_security_model(self):
        sdk = Textql(api_key="literal-key")
        try:
            assert isinstance(sdk.sdk_configuration.security, models.Security)
            assert sdk.sdk_configuration.security.api_key == "literal-key"
        finally:
            sdk.__exit__(None, None, None)

    def test_none_api_key_produces_no_security(self):
        sdk = Textql(api_key=None)
        try:
            assert sdk.sdk_configuration.security is None
        finally:
            sdk.__exit__(None, None, None)

    def test_callable_api_key_is_wrapped_lazily(self):
        calls = {"n": 0}

        def supplier():
            calls["n"] += 1
            return f"dynamic-{calls['n']}"

        sdk = Textql(api_key=supplier)
        try:
            security_factory = sdk.sdk_configuration.security
            assert callable(security_factory)
            assert calls["n"] == 0  # not called yet, only wrapped

            first = security_factory()
            second = security_factory()
            assert isinstance(first, models.Security)
            assert first.api_key == "dynamic-1"
            assert second.api_key == "dynamic-2"
        finally:
            sdk.__exit__(None, None, None)


class TestLazySubSdkLoading:
    def test_accessing_agents_lazily_imports_and_caches_instance(self):
        sdk = Textql(api_key="k")
        try:
            from textql_sdk.agents import Agents

            first = sdk.agents
            assert isinstance(first, Agents)
            # Second access should return the exact same cached instance
            # (set via setattr in __getattr__), not re-import/re-instantiate.
            second = sdk.agents
            assert first is second
        finally:
            sdk.__exit__(None, None, None)

    def test_all_documented_sub_sdks_are_reachable(self):
        sdk = Textql(api_key="k")
        try:
            for attr in sdk._sub_sdk_map:
                instance = getattr(sdk, attr)
                assert instance is not None
                assert instance.sdk_configuration is sdk.sdk_configuration
        finally:
            sdk.__exit__(None, None, None)

    def test_unknown_attribute_raises_attribute_error(self):
        sdk = Textql(api_key="k")
        try:
            with pytest.raises(AttributeError):
                sdk.totally_not_a_real_attribute
        finally:
            sdk.__exit__(None, None, None)

    def test_dir_includes_lazy_sub_sdk_names(self):
        sdk = Textql(api_key="k")
        try:
            names = dir(sdk)
            assert "agents" in names
            assert "chats" in names
            assert "rbac" in names
        finally:
            sdk.__exit__(None, None, None)


class TestContextManagerLifecycle:
    def test_sync_context_manager_closes_owned_client_on_exit(self):
        with Textql(api_key="k") as sdk:
            client = sdk.sdk_configuration.client
            assert not client.is_closed
        assert client.is_closed
        assert sdk.sdk_configuration.client is None

    def test_sync_context_manager_does_not_close_supplied_client(self):
        client = httpx.Client()
        with Textql(api_key="k", client=client) as sdk:
            pass
        assert not client.is_closed
        assert sdk.sdk_configuration.client is None
        client.close()

    @pytest.mark.asyncio
    async def test_async_context_manager_closes_owned_async_client_on_exit(self):
        async with Textql(api_key="k") as sdk:
            async_client = sdk.sdk_configuration.async_client
            assert not async_client.is_closed
        assert async_client.is_closed
        assert sdk.sdk_configuration.async_client is None

        # Clean up the leftover sync client this constructor also created.
        if sdk.sdk_configuration.client is not None:
            sdk.sdk_configuration.client.close()


class TestRetryAndTimeoutConfigPassthrough:
    def test_timeout_ms_is_stored_on_configuration(self):
        sdk = Textql(api_key="k", timeout_ms=1234)
        try:
            assert sdk.sdk_configuration.timeout_ms == 1234
        finally:
            sdk.__exit__(None, None, None)

    def test_retry_config_is_stored_on_configuration(self):
        from textql_sdk.utils import BackoffStrategy, RetryConfig

        cfg = RetryConfig(
            "backoff",
            BackoffStrategy(initial_interval=1, max_interval=2, exponent=1.0, max_elapsed_time=10),
            retry_connection_errors=True,
        )
        sdk = Textql(api_key="k", retry_config=cfg)
        try:
            assert sdk.sdk_configuration.retry_config is cfg
        finally:
            sdk.__exit__(None, None, None)


class TestClientProtocolAssertion:
    def test_invalid_client_object_raises_assertion_error(self):
        class NotAClient:
            pass

        with pytest.raises(AssertionError):
            Textql(api_key="k", client=NotAClient())
