"""Unit tests for miscellaneous Observability operations."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response
from textql_sdk import errors, utils

OBS_PATH = "/textql.rpc.public.observe.ObservabilityService"


# ---------------------------------------------------------------------------
# backfill_thread_warnings / backfill_thread_warnings_async
# ---------------------------------------------------------------------------


def test_backfill_thread_warnings_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalThreads": 10, "alreadyRunning": False}))

    result = bundle.sdk.observability.backfill_thread_warnings(days=7, concurrency=4)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/BackfillThreadWarnings"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"days": 7, "concurrency": 4}
    assert result.total_threads == 10
    assert result.already_running is False


def test_backfill_thread_warnings_org_id_unset_is_omitted(make_sdk):
    """org_id is OptionalNullable[str]; when left UNSET (the default) it must
    not appear in the serialized JSON body at all -- per
    TextqlRPCPublicObserveBackfillThreadWarningsRequest.serialize_model."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.backfill_thread_warnings(days=7)

    body = bundle.transport.body_json()
    assert "orgId" not in body


def test_backfill_thread_warnings_org_id_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.backfill_thread_warnings(days=7, org_id="org-42")

    body = bundle.transport.body_json()
    assert body["orgId"] == "org-42"


def test_backfill_thread_warnings_org_id_explicit_none_serializes_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.backfill_thread_warnings(days=7, org_id=None)

    body = bundle.transport.body_json()
    assert body["orgId"] is None


def test_backfill_thread_warnings_redo_all_threads(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.backfill_thread_warnings(days=7, redo_all_threads=True)

    body = bundle.transport.body_json()
    assert body["redoAllThreads"] is True


@pytest.mark.asyncio
async def test_backfill_thread_warnings_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalThreads": 5}))

    result = await bundle.sdk.observability.backfill_thread_warnings_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/BackfillThreadWarnings"
    assert result.total_threads == 5


def test_backfill_thread_warnings_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.backfill_thread_warnings(days=1)

    assert exc_info.value.status_code == 400


def test_backfill_thread_warnings_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.backfill_thread_warnings(days=1)

    assert exc_info.value.status_code == 500


# export_csv / export_csv_async: despite the name, the SDK expects a JSON
# envelope with a `download_url` field, not raw text/csv (see bug test below).


def test_export_csv_basic_json_envelope(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"downloadUrl": "https://files.example.com/export.csv"})
    )

    result = bundle.sdk.observability.export_csv(tab="topics", days=30)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/ExportObservabilityCsv"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"tab": "topics", "days": 30}
    assert result.download_url == "https://files.example.com/export.csv"


def test_export_csv_raw_text_csv_response_is_not_matched(make_sdk):
    """Bug/quirk: a real text/csv 200 response has no matching branch in
    export_csv(), so it raises TextqlDefaultError despite the call succeeding."""
    bundle = make_sdk(
        lambda req: text_response(200, "col1,col2\nval1,val2\n", content_type="text/csv")
    )

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.export_csv(tab="topics", days=30)

    assert "Unexpected response received" in str(exc_info.value)


@pytest.mark.asyncio
async def test_export_csv_async_basic_json_envelope(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"downloadUrl": "https://files.example.com/async.csv"})
    )

    result = await bundle.sdk.observability.export_csv_async(tab="threads", days=7)

    req = bundle.transport.last_request
    assert req.url.path == f"{OBS_PATH}/ExportObservabilityCsv"
    body = bundle.transport.body_json()
    assert body == {"tab": "threads", "days": 7}
    assert result.download_url == "https://files.example.com/async.csv"


def test_export_csv_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad tab"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.export_csv(tab="bad", days=1)

    assert exc_info.value.status_code == 400


def test_export_csv_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.export_csv(tab="topics", days=1)

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# fix_check_record / fix_check_record_async
# ---------------------------------------------------------------------------


def test_fix_check_record_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-fix-1"}))

    result = bundle.sdk.observability.fix_check_record(record_id="record-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/FixCheckRecord"
    body = bundle.transport.body_json()
    assert body == {"recordId": "record-1"}
    assert result.chat_id == "chat-fix-1"


@pytest.mark.asyncio
async def test_fix_check_record_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-fix-2"}))

    result = await bundle.sdk.observability.fix_check_record_async(record_id="record-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/FixCheckRecord"
    assert result.chat_id == "chat-fix-2"


def test_fix_check_record_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.fix_check_record(record_id="missing")

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# fix_warning / fix_warning_async
# ---------------------------------------------------------------------------


def test_fix_warning_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-warn-1"}))

    result = bundle.sdk.observability.fix_warning(warning_id="warning-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/FixWarning"
    body = bundle.transport.body_json()
    assert body == {"warningId": "warning-1"}
    assert result.chat_id == "chat-warn-1"


@pytest.mark.asyncio
async def test_fix_warning_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-warn-2"}))

    result = await bundle.sdk.observability.fix_warning_async(warning_id="warning-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/FixWarning"
    assert result.chat_id == "chat-warn-2"


def test_fix_warning_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.fix_warning(warning_id="x")

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# get_backfill_preview / get_backfill_preview_async
# ---------------------------------------------------------------------------


def test_get_backfill_preview_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"unanalyzedCount": 100, "orgName": "Acme", "eligibleThreadCount": 80}
        )
    )

    result = bundle.sdk.observability.get_backfill_preview(days=30)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetBackfillPreview"
    body = bundle.transport.body_json()
    assert body == {"days": 30}
    assert result.unanalyzed_count == 100
    assert result.org_name == "Acme"
    assert result.eligible_thread_count == 80


def test_get_backfill_preview_org_id_unset_is_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.get_backfill_preview(days=30)

    body = bundle.transport.body_json()
    assert "orgId" not in body


def test_get_backfill_preview_org_id_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.get_backfill_preview(days=30, org_id="org-1")

    body = bundle.transport.body_json()
    assert body["orgId"] == "org-1"


@pytest.mark.asyncio
async def test_get_backfill_preview_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"unanalyzedCount": 5}))

    result = await bundle.sdk.observability.get_backfill_preview_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetBackfillPreview"
    assert result.unanalyzed_count == 5


def test_get_backfill_preview_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_backfill_preview(days=1)

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# get_backfill_status / get_backfill_status_async
# ---------------------------------------------------------------------------


def test_get_backfill_status_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"running": True, "total": 100, "processed": 40, "failed": 2})
    )

    result = bundle.sdk.observability.get_backfill_status()

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetBackfillStatus"
    body = bundle.transport.body_json()
    assert body == {}
    assert result.running is True
    assert result.total == 100
    assert result.processed == 40
    assert result.failed == 2


def test_get_backfill_status_org_id_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.get_backfill_status(org_id="org-99")

    body = bundle.transport.body_json()
    assert body["orgId"] == "org-99"


def test_get_backfill_status_org_id_unset_is_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.get_backfill_status()

    body = bundle.transport.body_json()
    assert "orgId" not in body


@pytest.mark.asyncio
async def test_get_backfill_status_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"running": False}))

    result = await bundle.sdk.observability.get_backfill_status_async()

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetBackfillStatus"
    assert result.running is False


def test_get_backfill_status_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_backfill_status()

    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# get_check_record_fix / get_check_record_fix_async
# ---------------------------------------------------------------------------


def test_get_check_record_fix_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"fixChatId": "chat-1", "fixRunActive": True})
    )

    result = bundle.sdk.observability.get_check_record_fix(record_id="record-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetCheckRecordFix"
    body = bundle.transport.body_json()
    assert body == {"recordId": "record-1"}
    assert result.fix_chat_id == "chat-1"
    assert result.fix_run_active is True


@pytest.mark.asyncio
async def test_get_check_record_fix_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"fixRunActive": False}))

    result = await bundle.sdk.observability.get_check_record_fix_async(record_id="record-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetCheckRecordFix"
    assert result.fix_run_active is False


def test_get_check_record_fix_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_check_record_fix(record_id="missing")

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# get_thread_warnings / get_thread_warnings_async
# ---------------------------------------------------------------------------


def test_get_thread_warnings_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"warningsByChat": {}, "analyzedChatIds": ["chat-1"]})
    )

    result = bundle.sdk.observability.get_thread_warnings(chat_ids=["chat-1"])

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetThreadWarnings"
    body = bundle.transport.body_json()
    assert body == {"chatIds": ["chat-1"]}
    assert result.warnings_by_chat == {}
    assert result.analyzed_chat_ids == ["chat-1"]


@pytest.mark.asyncio
async def test_get_thread_warnings_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"analyzedChatIds": []}))

    result = await bundle.sdk.observability.get_thread_warnings_async(chat_ids=["chat-2"])

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetThreadWarnings"
    assert result.analyzed_chat_ids == []


def test_get_thread_warnings_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_thread_warnings(chat_ids=["x"])

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# refine_draft / refine_draft_async
# ---------------------------------------------------------------------------


def test_refine_draft_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"name": "Billing", "covers": "billing stuff", "excludes": "", "vague": False}
        )
    )

    result = bundle.sdk.observability.refine_draft(
        prompt="topic about billing",
        examples=["example one", "example two"],
        exclusions=["not this"],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/RefineTopicDraft"
    body = bundle.transport.body_json()
    assert body == {
        "prompt": "topic about billing",
        "examples": ["example one", "example two"],
        "exclusions": ["not this"],
    }
    assert result.name == "Billing"
    assert result.vague is False


@pytest.mark.asyncio
async def test_refine_draft_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"name": "Async Topic"}))

    result = await bundle.sdk.observability.refine_draft_async(prompt="async prompt")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/RefineTopicDraft"
    assert result.name == "Async Topic"


def test_refine_draft_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad prompt"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.refine_draft(prompt="x")

    assert exc_info.value.status_code == 400


def test_refine_draft_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.refine_draft(prompt="x")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# set_topic_tag_feedback / set_topic_tag_feedback_async
# ---------------------------------------------------------------------------


def test_set_topic_tag_feedback_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.observability.set_topic_tag_feedback(
        topic_id="topic-1", chat_id="chat-1", excluded=True, reason="not relevant"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/SetTopicTagFeedback"
    body = bundle.transport.body_json()
    assert body == {
        "topicId": "topic-1",
        "chatId": "chat-1",
        "excluded": True,
        "reason": "not relevant",
    }
    assert result is not None


@pytest.mark.asyncio
async def test_set_topic_tag_feedback_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.observability.set_topic_tag_feedback_async(
        topic_id="topic-2", chat_id="chat-2", excluded=False
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{OBS_PATH}/SetTopicTagFeedback"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-2", "chatId": "chat-2", "excluded": False}
    assert result is not None


def test_set_topic_tag_feedback_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.set_topic_tag_feedback(
            topic_id="x", chat_id="y", excluded=True
        )

    assert exc_info.value.status_code == 400


def test_set_topic_tag_feedback_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.set_topic_tag_feedback(
            topic_id="x", chat_id="y", excluded=True
        )

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Retry, server_url, and http_headers overrides (representative subset)
# ---------------------------------------------------------------------------


def test_fix_warning_retries_backoff_eventually_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"chatId": "chat-retry"}),
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

    result = bundle.sdk.observability.fix_warning(warning_id="warning-retry", retries=retries)

    assert len(bundle.transport.requests) == 2
    assert result.chat_id == "chat-retry"


@pytest.mark.asyncio
async def test_export_csv_async_retries_backoff_eventually_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(503, {"message": "temporary failure"}),
            json_response(200, {"downloadUrl": "https://files.example.com/retry.csv"}),
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

    result = await bundle.sdk.observability.export_csv_async(
        tab="topics", days=7, retries=retries
    )

    assert len(bundle.transport.requests) == 2
    assert result.download_url == "https://files.example.com/retry.csv"


def test_get_backfill_status_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    override_url = "https://override.invalid"
    bundle.sdk.observability.get_backfill_status(server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_refine_draft_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.refine_draft(
        prompt="x", http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_get_thread_warnings_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.observability.get_thread_warnings(
        chat_ids=["chat-1"], timeout_ms=5000
    )

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetThreadWarnings"
    assert result is not None
