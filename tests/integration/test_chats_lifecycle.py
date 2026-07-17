"""Integration tests: Chats lifecycle against a REAL TextQL API server."""
import pytest

pytestmark = pytest.mark.integration


class TestChatCreateSendHistory:
    def test_create_send_get_history_roundtrip(self, live_sdk, cleanup):
        chat = live_sdk.chats.create_chat(message="Hello from the SDK integration suite")
        assert chat.chat is not None
        chat_id = chat.chat.id
        cleanup.add(lambda: live_sdk.chats.delete(chat_id=chat_id))

        send_resp = live_sdk.chats.send(chat_id=chat_id, message="A follow-up message.")
        assert send_resp is not None

        history = live_sdk.chats.get_history(chat_id=chat_id)
        assert history is not None

    def test_get_returns_same_chat_created(self, live_sdk, cleanup):
        chat = live_sdk.chats.create_chat(message="test")
        chat_id = chat.chat.id
        cleanup.add(lambda: live_sdk.chats.delete(chat_id=chat_id))

        got = live_sdk.chats.get(chat_id=chat_id)
        assert got.chat is not None
        assert got.chat.id == chat_id

    def test_bookmark_and_unbookmark(self, live_sdk, cleanup):
        chat = live_sdk.chats.create_chat(message="test")
        chat_id = chat.chat.id
        cleanup.add(lambda: live_sdk.chats.delete(chat_id=chat_id))

        live_sdk.chats.bookmark(chat_id=chat_id)
        bookmarked = live_sdk.chats.get(chat_id=chat_id)
        assert getattr(bookmarked.chat, "is_bookmarked", None) in (True, None)

        live_sdk.chats.unbookmark(chat_id=chat_id)

    def test_duplicate_chat_creates_independent_copy(self, live_sdk, cleanup):
        original = live_sdk.chats.create_chat(message="original")
        original_id = original.chat.id
        cleanup.add(lambda: live_sdk.chats.delete(chat_id=original_id))

        dup = live_sdk.chats.duplicate_chat(chat_id=original_id)
        assert dup.chat is not None
        dup_id = dup.chat.id
        assert dup_id != original_id
        cleanup.add(lambda: live_sdk.chats.delete(chat_id=dup_id))

    @pytest.mark.asyncio
    async def test_async_create_and_send(self, live_sdk_async, cleanup):
        chat = await live_sdk_async.chats.create_chat_async(message="async test")
        chat_id = chat.chat.id
        cleanup.add(lambda: live_sdk_async.chats.delete(chat_id=chat_id))

        await live_sdk_async.chats.send_async(chat_id=chat_id, message="async follow-up")


class TestChatAttachments:
    def test_attach_dataset_and_dashboard_do_not_error(self, live_sdk, cleanup):
        pytest.skip(
            "requires a real dataset_id/dashboard_id from the target test org; "
            "set TEXTQL_TEST_DATASET_ID / TEXTQL_TEST_DASHBOARD_ID to enable"
        )


class TestChatQueryOneShot:
    def test_query_one_shot_returns_an_answer(self, live_sdk):
        resp = live_sdk.chats.query_one_shot(message="What is 2 + 2?")
        assert resp is not None

    def test_query_one_shot_rejects_empty_message_or_handles_gracefully(self, live_sdk):
        from textql_sdk import errors

        try:
            resp = live_sdk.chats.query_one_shot(message="")
            # If the server accepts it, at minimum it shouldn't 500.
            assert resp is not None
        except errors.TextqlDefaultError as e:
            assert e.status_code < 500


class TestChatErrorPaths:
    def test_get_nonexistent_chat_raises_client_error(self, live_sdk):
        from textql_sdk import errors

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.chats.get(chat_id="00000000-0000-0000-0000-000000000000")
        assert 400 <= exc_info.value.status_code < 500

    def test_send_to_nonexistent_chat_raises_client_error(self, live_sdk):
        from textql_sdk import errors

        with pytest.raises(errors.TextqlDefaultError) as exc_info:
            live_sdk.chats.send(chat_id="00000000-0000-0000-0000-000000000000", message="hi")
        assert 400 <= exc_info.value.status_code < 500
