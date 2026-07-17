"""Smoke tests for the shared mock-transport test harness itself (tests/conftest.py)."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response


def test_sync_request_is_recorded_with_auth_header(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.create(name="foo")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.agent.AgentService/CreateAgent"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["name"] == "foo"


@pytest.mark.asyncio
async def test_async_request_is_recorded_with_auth_header(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.agents.create_async(name="bar")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["name"] == "bar"


def test_error_response_raises_textql_default_error(make_sdk):
    from textql_sdk import errors

    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.get_agent(agent_id="does-not-exist")

    assert exc_info.value.status_code == 404
