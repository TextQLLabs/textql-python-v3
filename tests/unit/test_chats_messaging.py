"""Unit tests for the Chats service (sdk.chats) messaging/streaming operations."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response
from textql_sdk import errors, utils

CHAT_PATH = "/textql.rpc.public.chat.ChatService"


# ---------------------------------------------------------------------------
# send / send_async
# ---------------------------------------------------------------------------


def test_send_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cellId": "cell-123"}))

    result = bundle.sdk.chats.send(chat_id="chat-1", message="hello there")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/SendMessage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1", "message": "hello there"}

    assert result.cell_id == "cell-123"


async def test_send_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cellId": "cell-async-1"}))

    result = await bundle.sdk.chats.send_async(chat_id="chat-2", message="hi")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/SendMessage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2", "message": "hi"}
    assert result.cell_id == "cell-async-1"


def test_send_rich_payload_image_urls_and_message_id_and_steering(make_sdk):
    """Exercise image_urls (plain list), message_id (OptionalNullable, explicit
    value), and steering (OptionalNullable[bool], explicit True)."""
    bundle = make_sdk(lambda req: json_response(200, {"cellId": "c-9"}))

    bundle.sdk.chats.send(
        chat_id="chat-9",
        message="look at these",
        image_urls=["https://example.com/a.png", "https://example.com/b.jpg"],
        message_id="msg-abc",
        steering=True,
    )

    body = bundle.transport.body_json()
    assert body == {
        "chatId": "chat-9",
        "message": "look at these",
        "imageUrls": ["https://example.com/a.png", "https://example.com/b.jpg"],
        "messageId": "msg-abc",
        "steering": True,
    }


def test_send_message_id_and_steering_unset_are_omitted(make_sdk):
    """When message_id/steering are left UNSET (the default), they must not
    appear in the serialized JSON body at all."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.send(chat_id="chat-10", message="plain")

    body = bundle.transport.body_json()
    assert "messageId" not in body
    assert "steering" not in body
    assert body == {"chatId": "chat-10", "message": "plain"}


def test_send_message_id_explicit_none_serializes_to_null(make_sdk):
    """message_id is OptionalNullable[str]; explicitly passing None (as opposed
    to leaving it UNSET) must serialize to JSON null, per
    TextqlRPCPublicChatSendRequest.serialize_model's nullable_fields handling."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.send(chat_id="chat-11", message="x", message_id=None, steering=None)

    body = bundle.transport.body_json()
    assert body["messageId"] is None
    assert body["steering"] is None
    assert body["chatId"] == "chat-11"


def test_send_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.send(chat_id="chat-x", message="oops")

    assert exc_info.value.status_code == 400


def test_send_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.send(chat_id="chat-x", message="oops")

    assert exc_info.value.status_code == 503


async def test_send_async_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.send_async(chat_id="chat-x", message="oops")

    assert exc_info.value.status_code == 404


async def test_send_async_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.send_async(chat_id="chat-x", message="oops")

    assert exc_info.value.status_code == 500


def test_send_retries_backoff_eventually_succeeds(make_sdk, sequence_handler):
    """500 then 200 -- verify the SDK's own retry machinery (utils.RetryConfig)
    retries on 5XX and eventually returns the successful response."""
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"cellId": "cell-retry-ok"}),
        ]
    )
    bundle = make_sdk(handler)

    retries = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=True,
    )

    result = bundle.sdk.chats.send(
        chat_id="chat-retry",
        message="retry me",
        retries=retries,
    )

    assert len(bundle.transport.requests) == 2
    assert result.cell_id == "cell-retry-ok"


async def test_send_async_retries_backoff_eventually_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(502, {"message": "temporary failure"}),
            json_response(200, {"cellId": "cell-retry-ok-async"}),
        ]
    )
    bundle = make_sdk(handler)

    retries = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=True,
    )

    result = await bundle.sdk.chats.send_async(
        chat_id="chat-retry-async",
        message="retry me",
        retries=retries,
    )

    assert len(bundle.transport.requests) == 2
    assert result.cell_id == "cell-retry-ok-async"


# ---------------------------------------------------------------------------
# run / run_async
# ---------------------------------------------------------------------------


def test_run_basic_request_and_response(make_sdk):
    # TextqlRPCPublicChatCell is a oneof; each cell must be wrapped under its
    # variant key (e.g. "textCell") per textql_rpc_public_chat_cell.py.
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "cells": [
                    {"id": "cell-1", "textCell": {"content": "hello"}},
                    {"id": "cell-2", "textCell": {"content": "world"}},
                ]
            },
        )
    )

    result = bundle.sdk.chats.run(chat_id="chat-run-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/RunChat"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-run-1"}

    assert len(result.cells) == 2
    assert result.cells[0].id == "cell-1"


async def test_run_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    result = await bundle.sdk.chats.run_async(chat_id="chat-run-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/RunChat"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-run-2"}
    assert result.cells == []


def test_run_rich_payload_all_optionalnullable_fields_explicit(make_sdk):
    """research, fast_mode (OptionalNullable[bool]) and
    latest_complete_cell_id (OptionalNullable[str]) explicitly set, plus
    model (plain Optional str enum)."""
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.run(
        chat_id="chat-run-3",
        latest_complete_cell_id="cell-prev",
        research=True,
        model="MODEL_SONNET_4_5",
        fast_mode=False,
    )

    body = bundle.transport.body_json()
    assert body == {
        "chatId": "chat-run-3",
        "latestCompleteCellId": "cell-prev",
        "research": True,
        "model": "MODEL_SONNET_4_5",
        "fastMode": False,
    }


def test_run_optionalnullable_fields_explicit_none_serialize_to_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.run(
        chat_id="chat-run-4",
        latest_complete_cell_id=None,
        research=None,
        fast_mode=None,
    )

    body = bundle.transport.body_json()
    assert body["latestCompleteCellId"] is None
    assert body["research"] is None
    assert body["fastMode"] is None


def test_run_optionalnullable_fields_unset_are_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.run(chat_id="chat-run-5")

    body = bundle.transport.body_json()
    assert "latestCompleteCellId" not in body
    assert "research" not in body
    assert "fastMode" not in body
    assert "model" not in body
    assert body == {"chatId": "chat-run-5"}


def test_run_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.run(chat_id="chat-run-err")

    assert exc_info.value.status_code == 422


def test_run_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(504, {"message": "timeout"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.run(chat_id="chat-run-err")

    assert exc_info.value.status_code == 504


async def test_run_async_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.run_async(chat_id="chat-run-err")

    assert exc_info.value.status_code == 401


async def test_run_async_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.run_async(chat_id="chat-run-err")

    assert exc_info.value.status_code == 502


def test_run_per_call_overrides_server_url_headers_timeout(make_sdk):
    """server_url / http_headers / timeout_ms per-call overrides for run()."""
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.run(
        chat_id="chat-override",
        server_url="https://override.invalid",
        http_headers={"X-Custom-Header": "custom-value"},
        timeout_ms=12345,
    )

    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override.invalid")
    assert req.headers["X-Custom-Header"] == "custom-value"
    # Auth header should still be present alongside the custom header.
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


async def test_run_async_per_call_overrides_server_url_headers_timeout(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    await bundle.sdk.chats.run_async(
        chat_id="chat-override-async",
        server_url="https://override-async.invalid",
        http_headers={"X-Custom-Header": "custom-value-async"},
        timeout_ms=6789,
    )

    req = bundle.transport.last_request
    assert str(req.url).startswith("https://override-async.invalid")
    assert req.headers["X-Custom-Header"] == "custom-value-async"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


# ---------------------------------------------------------------------------
# query_one_shot / query_one_shot_async
# ---------------------------------------------------------------------------


def test_query_one_shot_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"chatId": "chat-qos-1", "answer": "42", "cells": []}
        )
    )

    result = bundle.sdk.chats.query_one_shot(question="what is the answer?")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/QueryOneShot"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"question": "what is the answer?"}

    assert result.chat_id == "chat-qos-1"
    assert result.answer == "42"


async def test_query_one_shot_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"answer": "async-answer"}))

    result = await bundle.sdk.chats.query_one_shot_async(question="q?")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/QueryOneShot"
    body = bundle.transport.body_json()
    assert body == {"question": "q?"}
    assert result.answer == "async-answer"


def test_query_one_shot_rich_payload_with_paradigm_dict_and_chat_id(make_sdk):
    """paradigm accepts a dict (TypedDict) that goes through
    utils.get_pydantic_model; chat_id is OptionalNullable[str] explicit."""
    bundle = make_sdk(lambda req: json_response(200, {"answer": "ok"}))

    bundle.sdk.chats.query_one_shot(
        question="rich question",
        paradigm={"type": "TYPE_SQL", "version": 2},
        model="MODEL_OPUS_4_5",
        chat_id="chat-existing",
    )

    body = bundle.transport.body_json()
    assert body == {
        "question": "rich question",
        "paradigm": {"type": "TYPE_SQL", "version": 2},
        "model": "MODEL_OPUS_4_5",
        "chatId": "chat-existing",
    }


def test_query_one_shot_chat_id_explicit_none_serializes_to_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"answer": "ok"}))

    bundle.sdk.chats.query_one_shot(question="q", chat_id=None)

    body = bundle.transport.body_json()
    assert body["chatId"] is None


def test_query_one_shot_chat_id_unset_is_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"answer": "ok"}))

    bundle.sdk.chats.query_one_shot(question="q")

    body = bundle.transport.body_json()
    assert "chatId" not in body
    assert body == {"question": "q"}


def test_query_one_shot_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.query_one_shot(question="q")

    assert exc_info.value.status_code == 400


def test_query_one_shot_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.query_one_shot(question="q")

    assert exc_info.value.status_code == 500


async def test_query_one_shot_async_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.query_one_shot_async(question="q")

    assert exc_info.value.status_code == 403


async def test_query_one_shot_async_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.query_one_shot_async(question="q")

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# get_api_answer / get_api_answer_async
# ---------------------------------------------------------------------------


def test_get_api_answer_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"answer": "final answer", "complete": True})
    )

    result = bundle.sdk.chats.get_api_answer(chat_id="chat-ans-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/GetAPIChatAnswer"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-ans-1"}

    assert result.answer == "final answer"
    assert result.complete is True
    assert result.error is None


async def test_get_api_answer_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"answer": "", "complete": False, "error": "still running"}
        )
    )

    result = await bundle.sdk.chats.get_api_answer_async(chat_id="chat-ans-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/GetAPIChatAnswer"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-ans-2"}
    assert result.complete is False
    assert result.error == "still running"


def test_get_api_answer_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "chat missing"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.get_api_answer(chat_id="missing-chat")

    assert exc_info.value.status_code == 404


def test_get_api_answer_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.get_api_answer(chat_id="missing-chat")

    assert exc_info.value.status_code == 500


async def test_get_api_answer_async_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.get_api_answer_async(chat_id="chat-x")

    assert exc_info.value.status_code == 400


async def test_get_api_answer_async_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.get_api_answer_async(chat_id="chat-x")

    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# get_history / get_history_async
# ---------------------------------------------------------------------------


def test_get_history_basic_request_and_response(make_sdk):
    # TextqlRPCPublicChatCell is a oneof; wrap under the "textCell" variant.
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "cells": [
                    {"id": "c1", "textCell": {"content": "a"}},
                    {"id": "c2", "textCell": {"content": "b"}},
                ],
                "hasMore": True,
            },
        )
    )

    result = bundle.sdk.chats.get_history(chat_id="chat-hist-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/GetChatHistory"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-hist-1"}

    assert len(result.cells) == 2
    assert result.has_more is True


async def test_get_history_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": [], "hasMore": False}))

    result = await bundle.sdk.chats.get_history_async(chat_id="chat-hist-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/GetChatHistory"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-hist-2"}
    assert result.has_more is False


def test_get_history_limit_and_skip_unset_are_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.get_history(chat_id="chat-hist-3")

    body = bundle.transport.body_json()
    assert "limit" not in body
    assert "skip" not in body


def test_get_history_explicit_cursor_like_skip_and_limit_values(make_sdk):
    """limit/skip act as this endpoint's pagination controls (there is no
    separate 'cursor' param on GetChatHistory -- pagination is skip/limit
    based, per TextqlRPCPublicChatHistoryRequest)."""
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.get_history(chat_id="chat-hist-4", limit=25, skip=10)

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-hist-4", "limit": 25, "skip": 10}


def test_get_history_limit_zero_is_distinct_from_unset(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.get_history(chat_id="chat-hist-5", limit=0)

    body = bundle.transport.body_json()
    assert body["limit"] == 0
    assert "skip" not in body


def test_get_history_limit_very_large_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    huge_limit = 2**31 - 1
    bundle.sdk.chats.get_history(chat_id="chat-hist-6", limit=huge_limit)

    body = bundle.transport.body_json()
    assert body["limit"] == huge_limit


def test_get_history_limit_and_skip_explicit_none_serialize_to_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.get_history(chat_id="chat-hist-7", limit=None, skip=None)

    body = bundle.transport.body_json()
    assert body["limit"] is None
    assert body["skip"] is None


def test_get_history_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.get_history(chat_id="chat-x")

    assert exc_info.value.status_code == 400


def test_get_history_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.get_history(chat_id="chat-x")

    assert exc_info.value.status_code == 500


async def test_get_history_async_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.get_history_async(chat_id="chat-x")

    assert exc_info.value.status_code == 404


async def test_get_history_async_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.get_history_async(chat_id="chat-x")

    assert exc_info.value.status_code == 500


def test_get_history_per_call_overrides_server_url_headers_timeout(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    bundle.sdk.chats.get_history(
        chat_id="chat-hist-override",
        server_url="https://history-override.invalid",
        http_headers={"X-History-Header": "abc"},
        timeout_ms=999,
    )

    req = bundle.transport.last_request
    assert str(req.url).startswith("https://history-override.invalid")
    assert req.headers["X-History-Header"] == "abc"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


async def test_get_history_async_per_call_overrides_server_url_headers_timeout(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"cells": []}))

    await bundle.sdk.chats.get_history_async(
        chat_id="chat-hist-override-async",
        server_url="https://history-override-async.invalid",
        http_headers={"X-History-Header": "xyz"},
        timeout_ms=999,
    )

    req = bundle.transport.last_request
    assert str(req.url).startswith("https://history-override-async.invalid")
    assert req.headers["X-History-Header"] == "xyz"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


# ---------------------------------------------------------------------------
# poll_events / poll_events_async
# ---------------------------------------------------------------------------


def test_poll_events_basic_request_and_response(make_sdk):
    # TextqlRPCPublicChatWatchChatEvent is a oneof; wrap under the "cell"
    # variant, whose payload is itself the TextqlRPCPublicChatCell oneof.
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "events": [
                    {"cell": {"id": "c1", "textCell": {"content": "hi"}}}
                ],
                "cursor": "cursor-out-1",
                "running": True,
                "generation": 7,
            },
        )
    )

    result = bundle.sdk.chats.poll_events(chat_id="chat-poll-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/PollChatEvents"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-poll-1"}

    assert result.cursor == "cursor-out-1"
    assert result.running is True
    assert result.generation == 7
    assert len(result.events) == 1


async def test_poll_events_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"events": [], "cursor": "", "running": False})
    )

    result = await bundle.sdk.chats.poll_events_async(chat_id="chat-poll-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/PollChatEvents"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-poll-2"}
    assert result.events == []
    assert result.running is False


def test_poll_events_resume_cursor_unset_is_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"events": []}))

    bundle.sdk.chats.poll_events(chat_id="chat-poll-3")

    body = bundle.transport.body_json()
    assert "resumeCursor" not in body
    assert body == {"chatId": "chat-poll-3"}


def test_poll_events_resume_cursor_explicit_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"events": []}))

    bundle.sdk.chats.poll_events(chat_id="chat-poll-4", resume_cursor="cursor-abc-123")

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-poll-4", "resumeCursor": "cursor-abc-123"}


def test_poll_events_resume_cursor_empty_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"events": []}))

    bundle.sdk.chats.poll_events(chat_id="chat-poll-5", resume_cursor="")

    body = bundle.transport.body_json()
    assert body["resumeCursor"] == ""


def test_poll_events_resume_cursor_explicit_none_serializes_to_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"events": []}))

    bundle.sdk.chats.poll_events(chat_id="chat-poll-6", resume_cursor=None)

    body = bundle.transport.body_json()
    assert body["resumeCursor"] is None


def test_poll_events_min_generation_union_int_variant(make_sdk):
    """min_generation is Union[int, str] (MinGeneration TypeAliasType) --
    exercise the int variant."""
    bundle = make_sdk(lambda req: json_response(200, {"events": []}))

    bundle.sdk.chats.poll_events(chat_id="chat-poll-7", min_generation=42)

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-poll-7", "minGeneration": 42}


def test_poll_events_min_generation_union_str_variant(make_sdk):
    """Exercise the str variant of the min_generation union."""
    bundle = make_sdk(lambda req: json_response(200, {"events": []}))

    bundle.sdk.chats.poll_events(chat_id="chat-poll-8", min_generation="gen-token-xyz")

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-poll-8", "minGeneration": "gen-token-xyz"}


def test_poll_events_response_generation_union_str_variant_roundtrips(make_sdk):
    """The response's `generation` field is also Union[int, str]; verify the
    str variant round-trips through unmarshaling correctly."""
    bundle = make_sdk(
        lambda req: json_response(200, {"events": [], "generation": "gen-str-9"})
    )

    result = bundle.sdk.chats.poll_events(chat_id="chat-poll-9")

    assert result.generation == "gen-str-9"


def test_poll_events_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.poll_events(chat_id="chat-x")

    assert exc_info.value.status_code == 400


def test_poll_events_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.poll_events(chat_id="chat-x")

    assert exc_info.value.status_code == 500


async def test_poll_events_async_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(429, {"message": "rate limited"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.poll_events_async(chat_id="chat-x")

    assert exc_info.value.status_code == 429


async def test_poll_events_async_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.poll_events_async(chat_id="chat-x")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# cancel_stream / cancel_stream_async
# ---------------------------------------------------------------------------


def test_cancel_stream_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"exists": True}))

    result = bundle.sdk.chats.cancel_stream(chat_id="chat-cancel-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/CancelStream"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-cancel-1"}
    assert result.exists is True


async def test_cancel_stream_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"exists": False}))

    result = await bundle.sdk.chats.cancel_stream_async(chat_id="chat-cancel-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/CancelStream"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-cancel-2"}
    assert result.exists is False


def test_cancel_stream_error_response_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no such stream"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.cancel_stream(chat_id="missing")

    assert exc_info.value.status_code == 404


async def test_cancel_stream_async_error_response_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.cancel_stream_async(chat_id="missing")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# dismiss_questions / dismiss_questions_async
# ---------------------------------------------------------------------------


def test_dismiss_questions_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": True, "status": "QUESTIONS_STATUS_ANSWERED"})
    )

    result = bundle.sdk.chats.dismiss_questions(cell_id="cell-dq-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/DismissQuestions"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-dq-1"}

    assert result.success is True
    assert result.status == "QUESTIONS_STATUS_ANSWERED"


async def test_dismiss_questions_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = await bundle.sdk.chats.dismiss_questions_async(cell_id="cell-dq-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/DismissQuestions"
    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-dq-2"}
    assert result.success is False


def test_dismiss_questions_rich_payload_answers_list_of_dicts(make_sdk):
    """answers is a list of TextqlRPCPublicCellsQuestionAnswer objects, each
    with `selected` (list[str]), `custom` (OptionalNullable[str]), `inputs`
    (list[str]), `provided` (list[bool]). Build two distinct answer variants
    -- one multi-select, one free-text "Other" -- to exercise the nested list
    serialization contract."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.chats.dismiss_questions(
        cell_id="cell-dq-3",
        answers=[
            {
                "selected": ["OptionA", "OptionB"],
                "inputs": ["value-1"],
                "provided": [True],
            },
            {
                "selected": [],
                "custom": "my custom free text answer",
                "inputs": ["", "value-2"],
                "provided": [False, True],
            },
        ],
    )

    body = bundle.transport.body_json()
    assert body == {
        "cellId": "cell-dq-3",
        "answers": [
            {
                "selected": ["OptionA", "OptionB"],
                "inputs": ["value-1"],
                "provided": [True],
            },
            {
                "selected": [],
                "custom": "my custom free text answer",
                "inputs": ["", "value-2"],
                "provided": [False, True],
            },
        ],
    }


def test_dismiss_questions_answer_custom_explicit_none_serializes_to_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.chats.dismiss_questions(
        cell_id="cell-dq-4",
        answers=[{"selected": ["A"], "custom": None}],
    )

    body = bundle.transport.body_json()
    assert body["answers"][0]["custom"] is None


def test_dismiss_questions_answer_custom_unset_is_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.chats.dismiss_questions(
        cell_id="cell-dq-5",
        answers=[{"selected": ["A"]}],
    )

    body = bundle.transport.body_json()
    assert "custom" not in body["answers"][0]


def test_dismiss_questions_answers_unset_is_omitted_entirely(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.chats.dismiss_questions(cell_id="cell-dq-6")

    body = bundle.transport.body_json()
    assert "answers" not in body
    assert body == {"cellId": "cell-dq-6"}


def test_dismiss_questions_error_response_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.dismiss_questions(cell_id="cell-x")

    assert exc_info.value.status_code == 400


async def test_dismiss_questions_async_error_response_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.dismiss_questions_async(cell_id="cell-x")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# submit_questions / submit_questions_async
# ---------------------------------------------------------------------------


def test_submit_questions_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "status": "QUESTIONS_STATUS_ANSWERED",
                "resumed": True,
                "resumeError": "",
            },
        )
    )

    result = bundle.sdk.chats.submit_questions(cell_id="cell-sq-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{CHAT_PATH}/SubmitQuestions"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-sq-1"}

    assert result.success is True
    assert result.resumed is True
    assert result.resume_error == ""


async def test_submit_questions_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"success": False, "resumed": False, "resumeError": "agent gone"}
        )
    )

    result = await bundle.sdk.chats.submit_questions_async(cell_id="cell-sq-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{CHAT_PATH}/SubmitQuestions"
    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-sq-2"}
    assert result.resume_error == "agent gone"


def test_submit_questions_rich_payload_two_answer_variants(make_sdk):
    """Same nested answers contract as dismiss_questions; exercise both a
    multi-select variant and a free-text/"Other" variant together."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.chats.submit_questions(
        cell_id="cell-sq-3",
        answers=[
            {"selected": ["Yes"], "inputs": [], "provided": []},
            {"selected": ["Other"], "custom": "a free-form answer", "inputs": ["secret"], "provided": [True]},
        ],
    )

    body = bundle.transport.body_json()
    assert body["answers"][0] == {"selected": ["Yes"], "inputs": [], "provided": []}
    assert body["answers"][1] == {
        "selected": ["Other"],
        "custom": "a free-form answer",
        "inputs": ["secret"],
        "provided": [True],
    }


def test_submit_questions_answers_unset_is_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.chats.submit_questions(cell_id="cell-sq-4")

    body = bundle.transport.body_json()
    assert "answers" not in body


def test_submit_questions_error_response_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.submit_questions(cell_id="cell-x")

    assert exc_info.value.status_code == 400


async def test_submit_questions_async_error_response_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.submit_questions_async(cell_id="cell-x")

    assert exc_info.value.status_code == 500
