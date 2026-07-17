"""Unit tests for Playbooks report operations: get_report_by_id, get_reports, favoriting, previews."""
from __future__ import annotations

import pytest

from textql_sdk import errors, models, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PB_PATH = "/textql.rpc.public.playbook.PlaybookService"


def _report_with_blocks():
    """A report payload with 4 distinct report-block union variants."""
    return {
        "id": "report-1",
        "playbookId": "pb1",
        "subject": "Weekly Digest",
        "blocks": [
            {"hero": {"imageUrl": "https://example.com/hero.png", "imageAlt": "hero"}},
            {"text": {"heading": "Intro", "content": "Body content"}},
            {"image": {"imageUrl": "https://example.com/chart.png", "variant": "IMAGE_VARIANT_FULL_WIDTH"}},
            {"card": {"blocks": [{"text": {"heading": "Nested", "content": "nested content"}}]}},
        ],
    }


# --------------------------------------------------------------------------
# get_report_by_id
# --------------------------------------------------------------------------


def test_get_report_by_id_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"report": _report_with_blocks()}))

    result = bundle.sdk.playbooks.get_report_by_id(report_id="report-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetReportById"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"reportId": "report-1"}
    assert result.report.id == "report-1"


@pytest.mark.asyncio
async def test_get_report_by_id_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"report": {"id": "report-1"}}))

    result = await bundle.sdk.playbooks.get_report_by_id_async(report_id="report-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetReportById"
    assert result.report.id == "report-1"


def test_get_report_by_id_union_blocks_unmarshal_correctly(make_sdk):
    """Hunt for oneof/union unmarshaling bugs: each block variant must
    unmarshal to the correct Python model type with correct field values."""
    bundle = make_sdk(lambda req: json_response(200, {"report": _report_with_blocks()}))

    result = bundle.sdk.playbooks.get_report_by_id(report_id="report-1")
    blocks = result.report.blocks
    assert len(blocks) == 4

    hero_block = blocks[0]
    assert isinstance(hero_block, models.Hero)
    assert hero_block.hero.image_url == "https://example.com/hero.png"
    assert hero_block.hero.image_alt == "hero"

    text_block = blocks[1]
    assert isinstance(text_block, models.Text)
    assert text_block.text.heading == "Intro"
    assert text_block.text.content == "Body content"

    image_block = blocks[2]
    assert isinstance(image_block, models.Image)
    assert image_block.image.image_url == "https://example.com/chart.png"

    card_block = blocks[3]
    assert isinstance(card_block, models.Card1)
    assert len(card_block.card.blocks) == 1
    nested = card_block.card.blocks[0]
    assert isinstance(nested, models.Text)
    assert nested.text.heading == "Nested"


def test_get_report_by_id_additional_union_variants(make_sdk):
    """Cover divider, image_text, list, spacer block variants as well."""
    payload = {
        "report": {
            "id": "report-2",
            "blocks": [
                {"divider": {}},
                {"imageText": {"imageUrl": "https://example.com/x.png", "heading": "caption"}},
                {"list": {"items": ["a", "b", "c"]}},
                {"spacer": {}},
            ],
        }
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.get_report_by_id(report_id="report-2")
    blocks = result.report.blocks
    assert len(blocks) == 4
    assert isinstance(blocks[0], models.Divider)
    assert isinstance(blocks[1], models.ImageText)
    assert isinstance(blocks[2], models.ListT)
    assert isinstance(blocks[3], models.Spacer)


def test_get_report_by_id_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_report_by_id(report_id="missing")
    assert exc_info.value.status_code == 404


def test_get_report_by_id_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_report_by_id(report_id="r1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_get_report_by_id_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.get_report_by_id_async(report_id="r1")
    assert exc_info.value.status_code == 502


def test_get_report_by_id_unicode_content(make_sdk):
    payload = {
        "report": {
            "id": "r1",
            "subject": "報告書 📊",
            "blocks": [{"text": {"heading": "見出し", "content": "内容 テスト"}}],
        }
    }
    bundle = make_sdk(lambda req: json_response(200, payload))
    result = bundle.sdk.playbooks.get_report_by_id(report_id="r1")
    assert result.report.subject == "報告書 📊"
    assert result.report.blocks[0].text.heading == "見出し"


# --------------------------------------------------------------------------
# get_reports (GetPlaybookReports)
# --------------------------------------------------------------------------


def test_get_reports_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"reports": [_report_with_blocks()], "totalCount": 1}
        )
    )

    result = bundle.sdk.playbooks.get_reports(
        playbook_id="pb1",
        limit=10,
        offset=0,
        chat_id="chat-1",
        template_data_id="tmpl-1",
        batch_run_id="batch-1",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetPlaybookReports"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "playbookId": "pb1",
        "limit": 10,
        "offset": 0,
        "chatId": "chat-1",
        "templateDataId": "tmpl-1",
        "batchRunId": "batch-1",
    }
    assert result.total_count == 1
    assert result.reports[0].id == "report-1"


@pytest.mark.asyncio
async def test_get_reports_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))

    result = await bundle.sdk.playbooks.get_reports_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetPlaybookReports"
    assert result.reports == []


def test_get_reports_omits_unset_nullable_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))

    bundle.sdk.playbooks.get_reports(playbook_id="pb1")

    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb1"}
    for key in ("chatId", "templateDataId", "batchRunId"):
        assert key not in body


def test_get_reports_explicit_null_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))

    bundle.sdk.playbooks.get_reports(
        playbook_id="pb1", chat_id=None, template_data_id=None, batch_run_id=None
    )

    body = bundle.transport.body_json()
    assert body["chatId"] is None
    assert body["templateDataId"] is None
    assert body["batchRunId"] is None


def test_get_reports_union_blocks_multiple_reports(make_sdk):
    payload = {
        "reports": [
            {"id": "r1", "blocks": [{"hero": {"imageUrl": "u1"}}]},
            {"id": "r2", "blocks": [{"text": {"content": "hi"}}]},
            {"id": "r3", "blocks": [{"card": {"blocks": [{"spacer": {}}]}}]},
        ],
        "totalCount": 3,
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.get_reports(playbook_id="pb1")
    assert len(result.reports) == 3
    assert isinstance(result.reports[0].blocks[0], models.Hero)
    assert isinstance(result.reports[1].blocks[0], models.Text)
    assert isinstance(result.reports[2].blocks[0], models.Card1)
    assert isinstance(result.reports[2].blocks[0].card.blocks[0], models.Spacer)


def test_get_reports_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_reports(playbook_id="pb1")
    assert exc_info.value.status_code == 400


def test_get_reports_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_reports(playbook_id="pb1")
    assert exc_info.value.status_code == 500


def test_get_reports_empty_list_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": [], "totalCount": 0}))
    result = bundle.sdk.playbooks.get_reports(playbook_id="pb1")
    assert result.reports == []
    assert result.total_count == 0


def test_get_reports_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(503, {"message": "transient"}),
            json_response(200, {"reports": []}),
        ]
    )
    bundle = make_sdk(handler)
    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=5000
        ),
        retry_connection_errors=False,
    )
    result = bundle.sdk.playbooks.get_reports(playbook_id="pb1", retries=retry_config)
    assert len(bundle.transport.requests) == 2
    assert result.reports == []


# --------------------------------------------------------------------------
# get_reports_with_filters
# --------------------------------------------------------------------------


def test_get_reports_with_filters_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": [_report_with_blocks()]}))

    result = bundle.sdk.playbooks.get_reports_with_filters(
        filters={
            "playbook_ids": ["pb1", "pb2"],
            "search_term": "revenue",
            "sort_by": "createdAt",
            "sort_direction": "SORT_DIRECTION_DESC",
            "limit": 25,
            "offset": 0,
            "only_subscribed": True,
            "include_header": True,
            "chat_id": "chat-1",
        }
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetReportsWithFilters"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["filters"]["playbookIds"] == ["pb1", "pb2"]
    assert body["filters"]["searchTerm"] == "revenue"
    assert body["filters"]["sortBy"] == "createdAt"
    assert body["filters"]["sortDirection"] == "SORT_DIRECTION_DESC"
    assert body["filters"]["limit"] == 25
    assert body["filters"]["onlySubscribed"] is True
    assert body["filters"]["includeHeader"] is True
    assert body["filters"]["chatId"] == "chat-1"
    assert result.reports[0].id == "report-1"


@pytest.mark.asyncio
async def test_get_reports_with_filters_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))

    result = await bundle.sdk.playbooks.get_reports_with_filters_async(
        filters={"playbook_ids": ["pb1"]}
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetReportsWithFilters"
    body = bundle.transport.body_json()
    assert body["filters"]["playbookIds"] == ["pb1"]
    assert result.reports == []


def test_get_reports_with_filters_no_filters_omits_body_key(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))

    bundle.sdk.playbooks.get_reports_with_filters()

    body = bundle.transport.body_json()
    assert body == {}


def test_get_reports_with_filters_nullable_fields_explicit_null(make_sdk):
    """search_term/limit/offset/only_subscribed/chat_id are OptionalNullable
    inside TextqlRPCPublicPlaybookReportFilters -- explicit None must
    serialize as null when explicitly set."""
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))

    bundle.sdk.playbooks.get_reports_with_filters(
        filters={"search_term": None, "limit": None, "chat_id": None}
    )

    body = bundle.transport.body_json()
    assert body["filters"]["searchTerm"] is None
    assert body["filters"]["limit"] is None
    assert body["filters"]["chatId"] is None


def test_get_reports_with_filters_empty_playbook_ids_list(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))

    bundle.sdk.playbooks.get_reports_with_filters(filters={"playbook_ids": []})

    body = bundle.transport.body_json()
    assert body["filters"]["playbookIds"] == []


def test_get_reports_with_filters_union_blocks(make_sdk):
    payload = {
        "reports": [
            {"id": "r1", "blocks": [{"hero": {"imageUrl": "h1"}}, {"divider": {}}]},
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))
    result = bundle.sdk.playbooks.get_reports_with_filters(filters={"playbook_ids": ["pb1"]})
    assert isinstance(result.reports[0].blocks[0], models.Hero)
    assert isinstance(result.reports[0].blocks[1], models.Divider)


def test_get_reports_with_filters_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_reports_with_filters()
    assert exc_info.value.status_code == 400


def test_get_reports_with_filters_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_reports_with_filters()
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_get_reports_with_filters_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.get_reports_with_filters_async()
    assert exc_info.value.status_code == 422


def test_get_reports_with_filters_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"reports": []}),
        ]
    )
    bundle = make_sdk(handler)
    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=5000
        ),
        retry_connection_errors=False,
    )
    result = bundle.sdk.playbooks.get_reports_with_filters(retries=retry_config)
    assert len(bundle.transport.requests) == 2
    assert result.reports == []


# --------------------------------------------------------------------------
# get_chat_reports_summary
# --------------------------------------------------------------------------


def test_get_chat_reports_summary_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"summaries": []}))

    bundle.sdk.playbooks.get_chat_reports_summary(chat_id="chat-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetChatReportsSummary"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"chatId": "chat-1"}


@pytest.mark.asyncio
async def test_get_chat_reports_summary_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"summaries": []}))

    await bundle.sdk.playbooks.get_chat_reports_summary_async(chat_id="chat-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetChatReportsSummary"
    assert bundle.transport.body_json() == {"chatId": "chat-1"}


def test_get_chat_reports_summary_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_chat_reports_summary(chat_id="missing")
    assert exc_info.value.status_code == 404


def test_get_chat_reports_summary_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_chat_reports_summary(chat_id="chat-1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# get_playbook_reports_batch
# --------------------------------------------------------------------------


def test_get_playbook_reports_batch_sync_sends_correct_request(make_sdk):
    payload = {
        "templateDataReports": [
            {
                "templateDataId": "tmpl-1",
                "reports": [_report_with_blocks()],
                "totalCount": 1,
            }
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.get_playbook_reports_batch(
        playbook_id="pb1",
        template_data_ids=["tmpl-1", "tmpl-2"],
        limit_per_template=5,
        batch_run_id="batch-1",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetPlaybookReportsBatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "playbookId": "pb1",
        "templateDataIds": ["tmpl-1", "tmpl-2"],
        "limitPerTemplate": 5,
        "batchRunId": "batch-1",
    }
    assert result.template_data_reports[0].template_data_id == "tmpl-1"
    assert result.template_data_reports[0].reports[0].id == "report-1"


@pytest.mark.asyncio
async def test_get_playbook_reports_batch_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"templateDataReports": []}))

    result = await bundle.sdk.playbooks.get_playbook_reports_batch_async(
        playbook_id="pb1", template_data_ids=[]
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetPlaybookReportsBatch"
    body = bundle.transport.body_json()
    assert body["templateDataIds"] == []
    assert result.template_data_reports == []


def test_get_playbook_reports_batch_omits_unset_batch_run_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.get_playbook_reports_batch(playbook_id="pb1")

    body = bundle.transport.body_json()
    assert "batchRunId" not in body


def test_get_playbook_reports_batch_explicit_null_batch_run_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.get_playbook_reports_batch(playbook_id="pb1", batch_run_id=None)

    body = bundle.transport.body_json()
    assert body["batchRunId"] is None


def test_get_playbook_reports_batch_union_blocks(make_sdk):
    payload = {
        "templateDataReports": [
            {
                "templateDataId": "tmpl-1",
                "reports": [
                    {"id": "r1", "blocks": [{"imageText": {"imageUrl": "u", "heading": "t"}}]},
                    {"id": "r2", "blocks": [{"list": {"items": ["x"]}}]},
                ],
            }
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))
    result = bundle.sdk.playbooks.get_playbook_reports_batch(
        playbook_id="pb1", template_data_ids=["tmpl-1"]
    )
    reports = result.template_data_reports[0].reports
    assert isinstance(reports[0].blocks[0], models.ImageText)
    assert isinstance(reports[1].blocks[0], models.ListT)


def test_get_playbook_reports_batch_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_playbook_reports_batch(playbook_id="pb1")
    assert exc_info.value.status_code == 400


def test_get_playbook_reports_batch_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_playbook_reports_batch(playbook_id="pb1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_get_playbook_reports_batch_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.get_playbook_reports_batch_async(playbook_id="pb1")
    assert exc_info.value.status_code == 503


def test_get_playbook_reports_batch_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"templateDataReports": []}),
        ]
    )
    bundle = make_sdk(handler)
    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=5000
        ),
        retry_connection_errors=False,
    )
    result = bundle.sdk.playbooks.get_playbook_reports_batch(
        playbook_id="pb1", retries=retry_config
    )
    assert len(bundle.transport.requests) == 2
    assert result.template_data_reports == []


# --------------------------------------------------------------------------
# favorite_report
# --------------------------------------------------------------------------


def test_favorite_report_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.favorite_report(playbook_id="pb1", report_id="report-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/FavoriteReport"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1", "reportId": "report-1"}


@pytest.mark.asyncio
async def test_favorite_report_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.playbooks.favorite_report_async(playbook_id="pb1", report_id="report-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/FavoriteReport"
    assert bundle.transport.body_json() == {"playbookId": "pb1", "reportId": "report-1"}


def test_favorite_report_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.favorite_report(playbook_id="pb1", report_id="missing")
    assert exc_info.value.status_code == 404


def test_favorite_report_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.favorite_report(playbook_id="pb1", report_id="report-1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# mark_report_as_read
# --------------------------------------------------------------------------


def test_mark_report_as_read_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.mark_report_as_read(report_id="report-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/MarkReportAsRead"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"reportId": "report-1"}


@pytest.mark.asyncio
async def test_mark_report_as_read_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.playbooks.mark_report_as_read_async(report_id="report-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/MarkReportAsRead"
    assert bundle.transport.body_json() == {"reportId": "report-1"}


def test_mark_report_as_read_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.mark_report_as_read(report_id="missing")
    assert exc_info.value.status_code == 404


def test_mark_report_as_read_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.mark_report_as_read(report_id="report-1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# get_playbooks_previews
# --------------------------------------------------------------------------


def test_get_playbooks_previews_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbooks": [{"id": "pb1"}]}))

    result = bundle.sdk.playbooks.get_playbooks_previews(
        only_subscribed=True, status_filter="STATUS_ACTIVE"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetPlaybooksPreviews"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {
        "onlySubscribed": True,
        "statusFilter": "STATUS_ACTIVE",
    }
    assert result.playbooks[0].id == "pb1"


@pytest.mark.asyncio
async def test_get_playbooks_previews_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbooks": []}))

    result = await bundle.sdk.playbooks.get_playbooks_previews_async()

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetPlaybooksPreviews"
    assert result.playbooks == []


def test_get_playbooks_previews_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_playbooks_previews()
    assert exc_info.value.status_code == 400


def test_get_playbooks_previews_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_playbooks_previews()
    assert exc_info.value.status_code == 500
