"""Unit tests for Chats CRUD operations: create_chat, get, get_all, update, delete, duplicate_chat, bookmark, unbookmark."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, FAKE_BASE_URL, json_response
from textql_sdk import errors, utils

BASE_PATH = "/textql.rpc.public.chat.ChatService"


# ---------------------------------------------------------------------------
# create_chat
# ---------------------------------------------------------------------------


class TestCreateChat:
    def test_sync_request_shape_and_response(self, make_sdk):
        payload = {"chat": {"id": "chat-1", "summary": "hello"}}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = bundle.sdk.chats.create_chat(message="hi there", model="MODEL_DEFAULT")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/CreateChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"message": "hi there", "model": "MODEL_DEFAULT"}

        assert result.chat.id == "chat-1"
        assert result.chat.summary == "hello"

    async def test_async_request_shape_and_response(self, make_sdk):
        payload = {"chat": {"id": "chat-2"}}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = await bundle.sdk.chats.create_chat_async(
            message="hi async", model="MODEL_DEFAULT"
        )

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/CreateChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"message": "hi async", "model": "MODEL_DEFAULT"}
        assert result.chat.id == "chat-2"

    def test_unset_optional_fields_omitted_from_body(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.create_chat()

        body = bundle.transport.body_json()
        # message, playbook_id, research, dashboard_mode, vllm_model_id,
        # fast_mode are all OptionalNullable[...] = UNSET by default and
        # should be entirely absent from the JSON body.
        for key in (
            "message",
            "playbookId",
            "research",
            "dashboardMode",
            "vllmModelId",
            "fastMode",
        ):
            assert key not in body
        assert body == {}

    def test_explicit_none_nullable_fields_serialize_as_null(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.create_chat(
            message=None,
            playbook_id=None,
            research=None,
            dashboard_mode=None,
            vllm_model_id=None,
            fast_mode=None,
        )

        body = bundle.transport.body_json()
        assert body == {
            "message": None,
            "playbookId": None,
            "research": None,
            "dashboardMode": None,
            "vllmModelId": None,
            "fastMode": None,
        }

    def test_explicit_values_serialize_with_alias(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.create_chat(
            message="msg",
            playbook_id="pb-1",
            research=True,
            dashboard_mode=False,
            vllm_model_id="vllm-1",
            fast_mode=True,
            model="MODEL_OPUS_4_5",
            methodology="METHODOLOGY_THOROUGH",
        )

        body = bundle.transport.body_json()
        assert body == {
            "message": "msg",
            "playbookId": "pb-1",
            "research": True,
            "dashboardMode": False,
            "vllmModelId": "vllm-1",
            "fastMode": True,
            "model": "MODEL_OPUS_4_5",
            "methodology": "METHODOLOGY_THOROUGH",
        }

    def test_sync_4xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.chats.create_chat(message="x")

        assert exc_info.value.status_code == 400

    def test_sync_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.chats.create_chat(message="x")

        assert exc_info.value.status_code == 500

    async def test_async_4xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            await bundle.sdk.chats.create_chat_async(message="x")

        assert exc_info.value.status_code == 403

    async def test_async_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            await bundle.sdk.chats.create_chat_async(message="x")

        assert exc_info.value.status_code == 503

    def test_retries_on_500_then_succeeds(self, make_sdk, sequence_handler):
        handler = sequence_handler(
            [
                json_response(500, {"message": "transient"}),
                json_response(200, {"chat": {"id": "chat-retried"}}),
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

        result = bundle.sdk.chats.create_chat(message="retry-me", retries=retries)

        assert len(bundle.transport.requests) == 2
        assert result.chat.id == "chat-retried"

    async def test_async_retries_on_500_then_succeeds(self, make_sdk, sequence_handler):
        handler = sequence_handler(
            [
                json_response(500, {"message": "transient"}),
                json_response(200, {"chat": {"id": "chat-retried-async"}}),
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

        result = await bundle.sdk.chats.create_chat_async(
            message="retry-me-async", retries=retries
        )

        assert len(bundle.transport.requests) == 2
        assert result.chat.id == "chat-retried-async"

    def test_server_url_override(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.create_chat(message="x", server_url=FAKE_BASE_URL)

        req = bundle.transport.last_request
        assert str(req.url).startswith(FAKE_BASE_URL)
        assert req.url.path == f"{BASE_PATH}/CreateChat"

    def test_http_headers_override(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.create_chat(message="x", http_headers={"X-Custom-Header": "abc"})

        req = bundle.transport.last_request
        assert req.headers["X-Custom-Header"] == "abc"

    def test_timeout_ms_override_does_not_crash(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        result = bundle.sdk.chats.create_chat(message="x", timeout_ms=15000)

        assert result.chat.id == "c"
        assert len(bundle.transport.requests) == 1


# ---------------------------------------------------------------------------
# get
# ---------------------------------------------------------------------------


class TestGet:
    def test_sync_request_shape_and_response(self, make_sdk):
        payload = {
            "chat": {"id": "chat-9"},
            "messages": [{"role": "user", "content": "hello"}],
            "assets": [],
        }
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = bundle.sdk.chats.get(chat_id="chat-9")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/GetChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-9"}

        assert result.chat.id == "chat-9"
        assert len(result.messages) == 1
        assert result.messages[0].role == "user"
        assert result.messages[0].content == "hello"
        assert result.assets == []

    async def test_async_request_shape_and_response(self, make_sdk):
        payload = {"chat": {"id": "chat-10"}}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = await bundle.sdk.chats.get_async(chat_id="chat-10")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/GetChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-10"}
        assert result.chat.id == "chat-10"

    def test_chat_id_unset_omits_field(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.get()

        body = bundle.transport.body_json()
        assert body == {}

    def test_sync_4xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.chats.get(chat_id="missing")

        assert exc_info.value.status_code == 404

    def test_sync_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.chats.get(chat_id="x")

        assert exc_info.value.status_code == 502

    async def test_async_4xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            await bundle.sdk.chats.get_async(chat_id="x")

        assert exc_info.value.status_code == 401

    async def test_async_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(504, {"message": "timeout"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            await bundle.sdk.chats.get_async(chat_id="x")

        assert exc_info.value.status_code == 504

    def test_retries_on_500_then_succeeds(self, make_sdk, sequence_handler):
        handler = sequence_handler(
            [
                json_response(500, {"message": "transient"}),
                json_response(200, {"chat": {"id": "chat-after-retry"}}),
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

        result = bundle.sdk.chats.get(chat_id="retry-target", retries=retries)

        assert len(bundle.transport.requests) == 2
        assert result.chat.id == "chat-after-retry"

    def test_server_url_and_headers_override(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.get(
            chat_id="c",
            server_url=FAKE_BASE_URL,
            http_headers={"X-Trace-Id": "trace-123"},
            timeout_ms=2000,
        )

        req = bundle.transport.last_request
        assert str(req.url).startswith(FAKE_BASE_URL)
        assert req.headers["X-Trace-Id"] == "trace-123"


# ---------------------------------------------------------------------------
# get_all
# ---------------------------------------------------------------------------


class TestGetAll:
    def test_sync_request_shape_and_response(self, make_sdk):
        payload = {
            "chats": [{"id": "c1"}, {"id": "c2"}],
            "totalCount": 2,
        }
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = bundle.sdk.chats.get_all(member_only=True, limit=10, offset=0)

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/GetChats"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"memberOnly": True, "limit": 10, "offset": 0}

        assert result.total_count == 2
        assert [c.id for c in result.chats] == ["c1", "c2"]

    async def test_async_request_shape_and_response(self, make_sdk):
        payload = {"chats": [], "totalCount": 0}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = await bundle.sdk.chats.get_all_async(member_only=False)

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/GetChats"

        body = bundle.transport.body_json()
        assert body == {"memberOnly": False}
        assert result.total_count == 0
        assert result.chats == []

    def test_no_kwargs_omits_all_optional_fields(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chats": [], "totalCount": 0}))

        bundle.sdk.chats.get_all()

        body = bundle.transport.body_json()
        assert body == {}

    def test_limit_zero_serializes_explicitly(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chats": [], "totalCount": 0}))

        bundle.sdk.chats.get_all(limit=0)

        body = bundle.transport.body_json()
        assert body == {"limit": 0}

    def test_large_limit_serializes(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chats": [], "totalCount": 0}))

        bundle.sdk.chats.get_all(limit=1_000_000)

        body = bundle.transport.body_json()
        assert body == {"limit": 1_000_000}

    def test_empty_search_term_serializes(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chats": [], "totalCount": 0}))

        bundle.sdk.chats.get_all(search_term="")

        body = bundle.transport.body_json()
        assert body == {"searchTerm": ""}

    def test_explicit_none_nullable_fields_serialize_as_null(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chats": [], "totalCount": 0}))

        bundle.sdk.chats.get_all(
            search_term=None,
            limit=None,
            offset=None,
            creator_member_id=None,
            bookmarked_only=None,
            exclude_batch_runs=None,
            exclude_unused_playbooks=None,
            has_thread_warning=None,
            shared_with_me=None,
            exclude_feed=None,
        )

        body = bundle.transport.body_json()
        assert body == {
            "searchTerm": None,
            "limit": None,
            "offset": None,
            "creatorMemberId": None,
            "bookmarkedOnly": None,
            "excludeBatchRuns": None,
            "excludeUnusedPlaybooks": None,
            "hasThreadWarning": None,
            "sharedWithMe": None,
            "excludeFeed": None,
        }

    def test_list_fields_serialize_correctly(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chats": [], "totalCount": 0}))

        bundle.sdk.chats.get_all(
            creator_member_ids=["m1", "m2"],
            sources=["CHAT_SOURCE_THREAD", "CHAT_SOURCE_AGENT"],
            thread_warning_types=["THREAD_WARNING_TYPE_SLOW_QUERY"],
            topic_ids=["topic-1"],
        )

        body = bundle.transport.body_json()
        assert body == {
            "creatorMemberIds": ["m1", "m2"],
            "sources": ["CHAT_SOURCE_THREAD", "CHAT_SOURCE_AGENT"],
            "threadWarningTypes": ["THREAD_WARNING_TYPE_SLOW_QUERY"],
            "topicIds": ["topic-1"],
        }

    def test_sort_and_date_filters_serialize(self, make_sdk):
        from datetime import datetime, timezone

        bundle = make_sdk(lambda req: json_response(200, {"chats": [], "totalCount": 0}))

        created_after = datetime(2024, 1, 1, tzinfo=timezone.utc)
        created_before = datetime(2024, 12, 31, tzinfo=timezone.utc)

        bundle.sdk.chats.get_all(
            sort_by="CHAT_SORT_FIELD_CREATED_AT",
            sort_direction="CHAT_SORT_DIRECTION_DESC",
            created_after=created_after,
            created_before=created_before,
            source="CHAT_SOURCE_PLAYBOOK",
        )

        body = bundle.transport.body_json()
        assert body["sortBy"] == "CHAT_SORT_FIELD_CREATED_AT"
        assert body["sortDirection"] == "CHAT_SORT_DIRECTION_DESC"
        assert body["source"] == "CHAT_SOURCE_PLAYBOOK"
        assert body["createdAfter"].startswith("2024-01-01")
        assert body["createdBefore"].startswith("2024-12-31")

    def test_response_unmarshals_full_chat_list(self, make_sdk):
        payload = {
            "chats": [
                {"id": "c1", "summary": "first"},
                {"id": "c2", "summary": "second"},
            ],
            "totalCount": 42,
        }
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = bundle.sdk.chats.get_all()

        assert result.total_count == 42
        assert result.chats[0].summary == "first"
        assert result.chats[1].summary == "second"


# ---------------------------------------------------------------------------
# update
# ---------------------------------------------------------------------------


class TestUpdate:
    def test_sync_request_shape_and_response(self, make_sdk):
        payload = {"chat": {"id": "chat-5", "summary": "updated summary"}}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = bundle.sdk.chats.update(
            chat_id="chat-5",
            research=True,
            summary="updated summary",
            dashboard_mode=True,
            methodology="METHODOLOGY_ADAPTIVE",
            fast_mode=False,
        )

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/UpdateChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {
            "chatId": "chat-5",
            "research": True,
            "summary": "updated summary",
            "dashboardMode": True,
            "methodology": "METHODOLOGY_ADAPTIVE",
            "fastMode": False,
        }

        assert result.chat.id == "chat-5"
        assert result.chat.summary == "updated summary"

    async def test_async_request_shape_and_response(self, make_sdk):
        payload = {"chat": {"id": "chat-6"}}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = await bundle.sdk.chats.update_async(
            chat_id="chat-6", summary="async summary"
        )

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/UpdateChat"

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-6", "summary": "async summary"}
        assert result.chat.id == "chat-6"

    def test_unset_fields_omitted(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.update(chat_id="c")

        body = bundle.transport.body_json()
        assert body == {"chatId": "c"}

    def test_explicit_none_nullable_fields_serialize_as_null(self, make_sdk):
        # research, summary, dashboard_mode, fast_mode are OptionalNullable and
        # marked nullable_fields in the model_serializer: an explicit None
        # should serialize as JSON null (not be dropped) because the field is
        # in __pydantic_fields_set__.
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.update(
            chat_id="c",
            research=None,
            summary=None,
            dashboard_mode=None,
            fast_mode=None,
        )

        body = bundle.transport.body_json()
        assert body == {
            "chatId": "c",
            "research": None,
            "summary": None,
            "dashboardMode": None,
            "fastMode": None,
        }

    def test_rich_summary_field_serializes_correctly(self, make_sdk):
        # "summary" is a plain nullable string field -- verify a longer,
        # structured string value round-trips through serialization intact.
        rich_summary = "Line 1\nLine 2 with \"quotes\" and a unicode dash — end."
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.update(chat_id="c", summary=rich_summary)

        body = bundle.transport.body_json()
        assert body["summary"] == rich_summary

    def test_sync_4xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(422, {"message": "invalid"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.chats.update(chat_id="c", summary="x")

        assert exc_info.value.status_code == 422

    async def test_async_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            await bundle.sdk.chats.update_async(chat_id="c", summary="x")

        assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# delete
# ---------------------------------------------------------------------------


class TestDelete:
    def test_sync_request_shape_and_response(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        result = bundle.sdk.chats.delete(chat_id="chat-to-delete")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/DeleteChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-to-delete"}

        # 200 response unmarshals to GoogleProtobufEmpty.
        assert result is not None

    async def test_async_request_shape_and_response(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        result = await bundle.sdk.chats.delete_async(chat_id="chat-to-delete-async")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/DeleteChat"

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-to-delete-async"}
        assert result is not None

    def test_chat_id_unset_omits_field(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        bundle.sdk.chats.delete()

        body = bundle.transport.body_json()
        assert body == {}

    def test_sync_4xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.chats.delete(chat_id="missing")

        assert exc_info.value.status_code == 404

    def test_sync_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            bundle.sdk.chats.delete(chat_id="x")

        assert exc_info.value.status_code == 500

    async def test_async_4xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            await bundle.sdk.chats.delete_async(chat_id="x")

        assert exc_info.value.status_code == 409

    async def test_async_5xx_raises_textql_default_error(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            await bundle.sdk.chats.delete_async(chat_id="x")

        assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# duplicate_chat
# ---------------------------------------------------------------------------


class TestDuplicateChat:
    def test_sync_request_shape_and_response(self, make_sdk):
        payload = {"chat": {"id": "chat-dup"}}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = bundle.sdk.chats.duplicate_chat(
            chat_id="chat-orig", only_if_different_owner=True
        )

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/DuplicateChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-orig", "onlyIfDifferentOwner": True}
        assert result.chat.id == "chat-dup"

    async def test_async_request_shape_and_response(self, make_sdk):
        payload = {"chat": {"id": "chat-dup-async"}}
        bundle = make_sdk(lambda req: json_response(200, payload))

        result = await bundle.sdk.chats.duplicate_chat_async(
            chat_id="chat-orig-async", only_if_different_owner=False
        )

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/DuplicateChat"

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-orig-async", "onlyIfDifferentOwner": False}
        assert result.chat.id == "chat-dup-async"

    def test_only_if_different_owner_unset_omitted(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.duplicate_chat(chat_id="c")

        body = bundle.transport.body_json()
        assert body == {"chatId": "c"}

    def test_only_if_different_owner_explicit_none_serializes_null(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {"chat": {"id": "c"}}))

        bundle.sdk.chats.duplicate_chat(chat_id="c", only_if_different_owner=None)

        body = bundle.transport.body_json()
        assert body == {"chatId": "c", "onlyIfDifferentOwner": None}


# ---------------------------------------------------------------------------
# bookmark
# ---------------------------------------------------------------------------


class TestBookmark:
    def test_sync_request_shape_and_response(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        result = bundle.sdk.chats.bookmark(chat_id="chat-to-bookmark")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/BookmarkChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-to-bookmark"}
        assert result is not None

    async def test_async_request_shape_and_response(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        result = await bundle.sdk.chats.bookmark_async(chat_id="chat-to-bookmark-async")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/BookmarkChat"

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-to-bookmark-async"}
        assert result is not None

    def test_chat_id_unset_omits_field(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        bundle.sdk.chats.bookmark()

        body = bundle.transport.body_json()
        assert body == {}


# ---------------------------------------------------------------------------
# unbookmark
# ---------------------------------------------------------------------------


class TestUnbookmark:
    def test_sync_request_shape_and_response(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        result = bundle.sdk.chats.unbookmark(chat_id="chat-to-unbookmark")

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/UnbookmarkChat"
        assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-to-unbookmark"}
        assert result is not None

    async def test_async_request_shape_and_response(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        result = await bundle.sdk.chats.unbookmark_async(
            chat_id="chat-to-unbookmark-async"
        )

        req = bundle.transport.last_request
        assert req.method == "POST"
        assert req.url.path == f"{BASE_PATH}/UnbookmarkChat"

        body = bundle.transport.body_json()
        assert body == {"chatId": "chat-to-unbookmark-async"}
        assert result is not None

    def test_chat_id_unset_omits_field(self, make_sdk):
        bundle = make_sdk(lambda req: json_response(200, {}))

        bundle.sdk.chats.unbookmark()

        body = bundle.transport.body_json()
        assert body == {}
