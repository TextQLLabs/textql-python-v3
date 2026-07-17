"""Unit tests for the Chats service "attach" operations (sdk.chats):"""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors


# ---------------------------------------------------------------------------
# attach_agent / attach_agent_async
# ---------------------------------------------------------------------------


def test_attach_agent_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"chat": {"id": "chat-1"}})
    )

    result = bundle.sdk.chats.attach_agent(chat_id="chat-1", agent_id="agent-1")

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/AttachAgentToChat"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1", "agentId": "agent-1"}

    assert result.chat is not None
    assert result.chat.id == "chat-1"


async def test_attach_agent_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"chat": {"id": "chat-async-1"}})
    )

    result = await bundle.sdk.chats.attach_agent_async(
        chat_id="chat-async-1", agent_id="agent-async-1"
    )

    assert len(bundle.transport.requests) == 1
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/AttachAgentToChat"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-async-1", "agentId": "agent-async-1"}

    assert result.chat is not None
    assert result.chat.id == "chat-async-1"


def test_attach_agent_omits_unset_fields(make_sdk):
    # Neither chat_id nor agent_id passed -> both are None at the model level,
    # and per TextqlRPCPublicChatAttachAgentToChatRequest.serialize_model both
    # "chatId" and "agentId" are in `optional_fields`, so a None value causes
    # the key to be omitted entirely (not serialized as JSON null).
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.attach_agent()

    body = bundle.transport.body_json()
    assert body == {}


def test_attach_agent_partial_kwargs_only_includes_passed_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.attach_agent(chat_id="only-chat")

    body = bundle.transport.body_json()
    assert body == {"chatId": "only-chat"}
    assert "agentId" not in body


# ---------------------------------------------------------------------------
# attach_app / attach_app_async
# ---------------------------------------------------------------------------


def test_attach_app_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"app": {"id": "app-1", "name": "My App"}})
    )

    result = bundle.sdk.chats.attach_app(chat_id="chat-2", app_id="app-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/AttachApp"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2", "appId": "app-1"}

    assert result.app is not None
    assert result.app.id == "app-1"
    assert result.app.name == "My App"
    # cell wasn't present in the payload -> optional field defaults to None
    assert result.cell is None


async def test_attach_app_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"app": {"id": "app-async-1"}})
    )

    result = await bundle.sdk.chats.attach_app_async(
        chat_id="chat-async-2", app_id="app-async-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/AttachApp"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-async-2", "appId": "app-async-1"}

    assert result.app is not None
    assert result.app.id == "app-async-1"


def test_attach_app_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.attach_app()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# attach_dashboard / attach_dashboard_async
# ---------------------------------------------------------------------------


def test_attach_dashboard_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"dashboard": {"id": "dash-1", "name": "My Dashboard"}}
        )
    )

    result = bundle.sdk.chats.attach_dashboard(
        chat_id="chat-3", dashboard_id="dash-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/AttachDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-3", "dashboardId": "dash-1"}

    assert result.dashboard is not None
    assert result.dashboard.id == "dash-1"
    assert result.dashboard.name == "My Dashboard"
    assert result.cell is None


async def test_attach_dashboard_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"dashboard": {"id": "dash-async-1"}})
    )

    result = await bundle.sdk.chats.attach_dashboard_async(
        chat_id="chat-async-3", dashboard_id="dash-async-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/AttachDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-async-3", "dashboardId": "dash-async-1"}

    assert result.dashboard is not None
    assert result.dashboard.id == "dash-async-1"


def test_attach_dashboard_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.attach_dashboard()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# attach_dataset / attach_dataset_async
# ---------------------------------------------------------------------------


def test_attach_dataset_sync_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.chats.attach_dataset(chat_id="chat-4", dataset_id="ds-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/AttachDataset"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-4", "datasetId": "ds-1"}

    # Both `cell` and `dataset` are optional and were omitted from the
    # response payload, so they should unmarshal to None rather than error.
    assert result.cell is None
    assert result.dataset is None


async def test_attach_dataset_async_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.chats.attach_dataset_async(
        chat_id="chat-async-4", dataset_id="ds-async-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/AttachDataset"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-async-4", "datasetId": "ds-async-1"}

    assert result.cell is None
    assert result.dataset is None


def test_attach_dataset_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.attach_dataset()

    body = bundle.transport.body_json()
    assert body == {}


def test_attach_dataset_partial_kwargs_only_includes_passed_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.attach_dataset(dataset_id="only-dataset")

    body = bundle.transport.body_json()
    assert body == {"datasetId": "only-dataset"}
    assert "chatId" not in body


# --- error handling -----------------------------------------------------


def test_attach_dataset_sync_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(404, {"message": "chat not found"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.attach_dataset(chat_id="missing-chat", dataset_id="ds-1")

    assert exc_info.value.status_code == 404


def test_attach_dataset_sync_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(500, {"message": "internal error"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.attach_dataset(chat_id="chat-5", dataset_id="ds-1")

    assert exc_info.value.status_code == 500


async def test_attach_dataset_async_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(400, {"message": "bad request"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.attach_dataset_async(
            chat_id="chat-6", dataset_id="ds-1"
        )

    assert exc_info.value.status_code == 400


async def test_attach_dataset_async_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(503, {"message": "service unavailable"})
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.attach_dataset_async(
            chat_id="chat-7", dataset_id="ds-1"
        )

    assert exc_info.value.status_code == 503
