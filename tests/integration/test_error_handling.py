"""Integration tests specifically targeting error handling / edge-of-contract behavior against a REAL TextQL API server: bad auth, malformed input, timeouts."""
import os

import httpx
import pytest

from textql_sdk import Textql, errors

pytestmark = pytest.mark.integration


class TestAuthenticationFailures:
    def test_invalid_api_key_raises_client_error_not_500(self, live_server_config):
        _valid_key, server_url = live_server_config
        with Textql(api_key="definitely-not-a-real-api-key", server_url=server_url) as sdk:
            with pytest.raises(errors.TextqlDefaultError) as exc_info:
                sdk.agents.list()
            # An invalid credential should be a 401/403, not a 500 -- if the
            # server 500s on bad auth, that's a real bug worth reporting.
            assert exc_info.value.status_code in (401, 403), (
                f"expected 401/403 for invalid API key, got {exc_info.value.status_code}: "
                f"{exc_info.value.message}"
            )

    def test_empty_api_key_raises_client_error(self, live_server_config):
        _valid_key, server_url = live_server_config
        with Textql(api_key="", server_url=server_url) as sdk:
            with pytest.raises(errors.TextqlDefaultError) as exc_info:
                sdk.agents.list()
            assert exc_info.value.status_code in (400, 401, 403)

    def test_no_api_key_at_all_raises_client_error(self, live_server_config):
        _valid_key, server_url = live_server_config
        with Textql(api_key=None, server_url=server_url) as sdk:
            with pytest.raises(errors.TextqlDefaultError) as exc_info:
                sdk.agents.list()
            assert exc_info.value.status_code in (400, 401, 403)


class TestMalformedRequests:
    def test_extremely_long_string_field_is_rejected_cleanly_or_accepted(self, live_sdk, cleanup):
        """A multi-megabyte name field should either be rejected with a
        clean 4xx (payload/field too large) or accepted -- what it must NOT
        do is crash the server (5xx) or hang past the client timeout."""
        huge_name = "x" * 5_000_000  # 5MB
        try:
            resp = live_sdk.agents.create(name=huge_name, prompt="test")
            if resp.agent is not None:
                cleanup.add(lambda: live_sdk.agents.delete(agent_id=resp.agent.id))
        except errors.TextqlDefaultError as e:
            assert e.status_code < 500, (
                f"a large-but-plausible payload should not 500, got {e.status_code}"
            )

    def test_unicode_and_control_characters_in_text_fields(self, live_sdk, cleanup):
        tricky_name = "Test 🎉 名前 \x00\x01 ‮ RTL-override"
        resp = live_sdk.agents.create(name=tricky_name, prompt="test")
        agent_id = resp.agent.id
        cleanup.add(lambda: live_sdk.agents.delete(agent_id=agent_id))

        got = live_sdk.agents.get_agent(agent_id=agent_id)
        # Round-trip should preserve the string exactly (or the server may
        # legitimately strip null bytes/control chars -- either is fine, a
        # *silent* mangling of ordinary unicode like emoji/CJK would not be).
        assert "🎉" in (got.agent.name or "")
        assert "名前" in (got.agent.name or "")

    def test_null_byte_in_query_string_does_not_crash_server(self, live_sdk, existing_connector_id=None):
        pytest.skip("requires TEXTQL_TEST_CONNECTOR_ID -- see test_connectors_lifecycle.py")


class TestClientSideTimeouts:
    def test_absurdly_low_timeout_ms_raises_a_catchable_timeout_error(self, live_server_config):
        """A 1ms timeout against any real network call should be impossible
        to satisfy -- confirms the SDK surfaces httpx's timeout exception
        rather than hanging indefinitely or raising something uncatchable.
        """
        api_key, server_url = live_server_config
        with Textql(api_key=api_key, server_url=server_url) as sdk:
            with pytest.raises((httpx.TimeoutException, errors.TextqlError)):
                sdk.agents.list(timeout_ms=1)


class TestConnectionRobustness:
    def test_unreachable_server_url_raises_connect_error(self, live_server_config):
        api_key, _server_url = live_server_config
        with Textql(api_key=api_key, server_url="http://127.0.0.1:1") as sdk:
            with pytest.raises(httpx.ConnectError):
                sdk.agents.list()

    def test_nonexistent_domain_raises_connect_error(self, live_server_config):
        api_key, _server_url = live_server_config
        with Textql(api_key=api_key, server_url="https://this-domain-should-not-exist-textql-test.invalid") as sdk:
            with pytest.raises(httpx.ConnectError):
                sdk.agents.list()
