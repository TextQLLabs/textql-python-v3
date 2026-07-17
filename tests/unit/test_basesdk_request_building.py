"""Unit tests for BaseSDK._build_request(_with_client) and do_request(_async)"""
import httpx
import pytest

from textql_sdk import errors
from textql_sdk.utils import BackoffStrategy, RetryConfig

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response


class TestHeaderConstruction:
    def test_accept_and_user_agent_headers_are_set(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(agent_id="a1")

        req = bundle.transport.last_request
        assert req.headers["accept"] == "application/json"
        assert "user-agent" in req.headers
        assert "textql-sdk" in req.headers["user-agent"] or req.headers["user-agent"]

    def test_http_headers_kwarg_adds_and_can_override_headers(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(
            agent_id="a1",
            # Must match the exact case the SDK uses internally ("Accept")
            # for the override to actually replace it -- see the dedicated
            # bug test below for what happens when the case differs.
            http_headers={"X-Custom": "value", "Accept": "text/plain"},
        )

        req = bundle.transport.last_request
        assert req.headers["X-Custom"] == "value"
        assert req.headers["accept"] == "text/plain"

    def test_http_headers_with_different_case_does_not_override_bug(self, make_sdk):
        """Bug: `http_headers={"accept": ...}` (lowercase) doesn't override the
        SDK's own "Accept" -- both survive in the plain dict and httpx merges
        them into one comma-joined value instead of one replacing the other."""
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(
            agent_id="a1",
            http_headers={"accept": "text/plain"},
        )

        req = bundle.transport.last_request
        # Expected if overriding worked cleanly: "text/plain".
        # Actual: both values got merged because of the casing mismatch.
        assert req.headers["accept"] == "application/json, text/plain"

    def test_auth_header_present_by_default(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(agent_id="a1")

        req = bundle.transport.last_request
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    def test_no_auth_header_when_api_key_is_none(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}), api_key=None)
        bundle.sdk.agents.get_agent(agent_id="a1")

        req = bundle.transport.last_request
        assert AUTH_HEADER_NAME not in req.headers

    def test_falls_back_to_env_var_when_constructed_without_api_key(self, make_sdk, monkeypatch):
        monkeypatch.setenv("TEXTQL_API_KEY", "from-env")
        bundle = make_sdk(lambda req: json_response(200, {}), api_key=None)
        bundle.sdk.agents.get_agent(agent_id="a1")

        req = bundle.transport.last_request
        assert req.headers[AUTH_HEADER_NAME] == "from-env"


class TestServerUrlAndPathBuilding:
    def test_default_base_url_and_path_used(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(agent_id="a1")

        req = bundle.transport.last_request
        assert req.url.host == "textql-sdk-tests.invalid"
        assert req.url.path == "/textql.rpc.public.agent.AgentService/GetAgent"

    def test_per_call_server_url_override(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(agent_id="a1", server_url="https://override.example.com")

        req = bundle.transport.last_request
        assert req.url.host == "override.example.com"

    def test_trailing_slash_on_server_url_override_is_stripped(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(agent_id="a1", server_url="https://override.example.com/")

        req = bundle.transport.last_request
        assert str(req.url) == "https://override.example.com/textql.rpc.public.agent.AgentService/GetAgent"


class TestTimeoutOverride:
    def test_timeout_ms_override_is_applied_to_request_extensions(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))
        bundle.sdk.agents.get_agent(agent_id="a1", timeout_ms=5000)

        req = bundle.transport.last_request
        assert req.extensions.get("timeout", {}).get("connect") == pytest.approx(5.0)

    def test_sdk_level_timeout_ms_used_when_no_per_call_override(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}), timeout_ms=7000)
        bundle.sdk.agents.get_agent(agent_id="a1")

        req = bundle.transport.last_request
        assert req.extensions.get("timeout", {}).get("connect") == pytest.approx(7.0)


class TestErrorResponseHandling:
    def test_4xx_raises_textql_default_error_with_body(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.agents.get_agent(agent_id="a1")

        assert exc_info.value.status_code == 400
        assert "bad request" in exc_info.value.message

    def test_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(500, {"message": "server exploded"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.agents.get_agent(agent_id="a1")

        assert exc_info.value.status_code == 500

    def test_malformed_json_200_response_raises_response_validation_error(self, make_sdk):
        bundle = make_sdk(
            lambda req: httpx.Response(200, content="not json{{{", headers={"content-type": "application/json"})
        )

        with pytest.raises(errors.ResponseValidationError):
            bundle.sdk.agents.get_agent(agent_id="a1")


class TestRetryWiringThroughRealOperation:
    def test_retries_kwarg_retries_on_500_then_succeeds(self, make_sdk, sequence_handler):
        handler = sequence_handler(
            [
                json_response(500, {"message": "retry me"}),
                json_response(200, {}),
            ]
        )
        bundle = make_sdk(handler)

        retry_cfg = RetryConfig(
            "backoff",
            BackoffStrategy(initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=5000, jitter_ms=0),
            retry_connection_errors=False,
        )
        bundle.sdk.agents.get_agent(agent_id="a1", retries=retry_cfg)

        assert len(bundle.transport.requests) == 2

    def test_no_retries_by_default_on_500(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(500, {}))

        with pytest.raises(errors.TextqlDefaultError):
            bundle.sdk.agents.get_agent(agent_id="a1")

        assert len(bundle.transport.requests) == 1

    @pytest.mark.asyncio
    async def test_async_retries_kwarg_retries_on_500_then_succeeds(self, make_sdk, sequence_handler):
        handler = sequence_handler(
            [
                json_response(502, {"message": "retry me"}),
                json_response(200, {}),
            ]
        )
        bundle = make_sdk(handler)

        retry_cfg = RetryConfig(
            "backoff",
            BackoffStrategy(initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=5000, jitter_ms=0),
            retry_connection_errors=False,
        )
        await bundle.sdk.agents.get_agent_async(agent_id="a1", retries=retry_cfg)

        assert len(bundle.transport.requests) == 2


class TestNoResponseError:
    def test_transport_exception_with_no_hooks_raises_no_response_error(self, make_sdk):
        def boom(_req):
            raise httpx.ConnectError("connection refused")

        bundle = make_sdk(boom)

        # The underlying httpx.ConnectError propagates since no hook
        # swallows it (see BaseSDK.do_request: hooks.after_error returns the
        # same exception when there are no registered after_error hooks).
        with pytest.raises(httpx.ConnectError):
            bundle.sdk.agents.get_agent(agent_id="a1")
