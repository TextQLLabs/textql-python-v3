import pyqwest
import pytest

from textql_sdk._connect.public.agent_pb2 import (
    GetAgentRequest,
    StreamAgentStatusRequest,
)
from textql_sdk._version import __user_agent__, __version__
from textql_sdk.streaming import create_streaming_client, create_streaming_client_sync
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("user_agent", [None, "customer-application/2.0"])
@pytest.mark.parametrize("rpc_prefix", ["", "/rpc/public"])
@pytest.mark.parametrize("sdk_marker", [None, "stale-client/0.0"])
async def test_sdk_origin_header_on_transport(
    make_sdk, asynchronous, user_agent, rpc_prefix, sdk_marker
):
    bundle = make_sdk(lambda req: json_response(200, {}))
    headers = {
        "X-TextQL-Client": "customer-application",
        "X-TextQL-Client-Version": "2.0",
        "X-TextQL-Agent": "customer-agent",
    }
    if user_agent is not None:
        headers["user-agent"] = user_agent
    request_headers = dict(headers)
    if sdk_marker is not None:
        request_headers["x-textql-sdk"] = sdk_marker

    operation = (
        bundle.sdk.agents.get_agent_async
        if asynchronous
        else bundle.sdk.agents.get_agent
    )
    result = operation(
        agent_id="a1",
        server_url=f"https://textql-sdk-tests.invalid{rpc_prefix}",
        http_headers=request_headers,
    )
    if asynchronous:
        await result

    request = bundle.transport.last_request
    assert request.headers["X-TextQL-SDK"] == f"python/{__version__}"
    assert request.headers["User-Agent"] == (user_agent or __user_agent__)
    for name, value in headers.items():
        assert request.headers[name] == value
    assert request.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert (
        request.url.path == "/rpc/public/textql.rpc.public.agent.AgentService/GetAgent"
    )
    assert bundle.transport.body_json() == {"agentId": "a1"}


class RecordingConnectTransport:
    def __init__(self):
        self.requests = []

    async def execute(self, request):
        self.requests.append(request)
        streaming = request.url.endswith("/StreamAgentStatus")
        return pyqwest.Response(
            status=200,
            headers=pyqwest.Headers(
                {
                    "content-type": (
                        "application/connect+proto"
                        if streaming
                        else "application/proto"
                    )
                }
            ),
            content=b"\x02\x00\x00\x00\x02{}" if streaming else b"",
        )

    def execute_sync(self, request):
        self.requests.append(request)
        streaming = request.url.endswith("/StreamAgentStatus")
        return pyqwest.SyncResponse(
            status=200,
            headers=pyqwest.Headers(
                {
                    "content-type": (
                        "application/connect+proto"
                        if streaming
                        else "application/proto"
                    )
                }
            ),
            content=b"\x02\x00\x00\x00\x02{}" if streaming else b"",
        )


@pytest.mark.asyncio
@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("streaming", [False, True])
@pytest.mark.parametrize("sdk_marker", [None, "stale-client/0.0"])
async def test_connect_sdk_origin_header_on_transport(
    asynchronous, streaming, sdk_marker
):
    transport = RecordingConnectTransport()
    headers = {
        "X-TextQL-Client": "customer-application",
        "X-TextQL-Client-Version": "2.0",
        "X-TextQL-Agent": "customer-agent",
        "user-agent": "customer-application/2.0",
    }
    request_headers = dict(headers)
    if sdk_marker is not None:
        request_headers["x-textql-sdk"] = sdk_marker
    if asynchronous:
        client = create_streaming_client(
            api_key=FAKE_API_KEY,
            server_url="https://textql-sdk-tests.invalid",
            http_client=pyqwest.Client(transport),
        )
        if streaming:
            messages = [
                message
                async for message in client.agents.stream_agent_status(
                    StreamAgentStatusRequest(), headers=request_headers
                )
            ]
            assert messages == []
        else:
            await client.agents.get_agent(
                GetAgentRequest(agent_id="a1"), headers=request_headers
            )
    else:
        client = create_streaming_client_sync(
            api_key=FAKE_API_KEY,
            server_url="https://textql-sdk-tests.invalid",
            http_client=pyqwest.SyncClient(transport),
        )
        if streaming:
            assert (
                list(
                    client.agents.stream_agent_status(
                        StreamAgentStatusRequest(), headers=request_headers
                    )
                )
                == []
            )
        else:
            client.agents.get_agent(
                GetAgentRequest(agent_id="a1"), headers=request_headers
            )

    assert len(transport.requests) == 1
    request = transport.requests[0]
    assert request.headers["X-TextQL-SDK"] == f"python/{__version__}"
    for name, value in headers.items():
        assert request.headers[name] == value
    assert request.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    operation = "StreamAgentStatus" if streaming else "GetAgent"
    assert request.url == (
        f"https://textql-sdk-tests.invalid/rpc/public/textql.rpc.public.agent.AgentService/{operation}"
    )
