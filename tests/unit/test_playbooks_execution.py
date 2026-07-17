"""Unit tests for Playbooks execution operations: run, cancel_template_execution, batch runs, lineage."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PB_PATH = "/textql.rpc.public.playbook.PlaybookService"


# --------------------------------------------------------------------------
# run (RunPlaybook)
# --------------------------------------------------------------------------


def test_run_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-1"}))

    result = bundle.sdk.playbooks.run(
        playbook_id="pb1", dry_run=True, template_id="tmpl-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/RunPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {
        "playbookId": "pb1",
        "dryRun": True,
        "templateId": "tmpl-1",
    }
    assert result.chat_id == "chat-1"


@pytest.mark.asyncio
async def test_run_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-2"}))

    result = await bundle.sdk.playbooks.run_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/RunPlaybook"
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.chat_id == "chat-2"


def test_run_omits_unset_template_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.run(playbook_id="pb1", dry_run=False)

    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb1", "dryRun": False}
    assert "templateId" not in body


def test_run_explicit_null_template_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.run(playbook_id="pb1", template_id=None)

    body = bundle.transport.body_json()
    assert body["templateId"] is None


def test_run_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid playbook state"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.run(playbook_id="pb1")
    assert exc_info.value.status_code == 422


def test_run_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.run(playbook_id="pb1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_run_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.run_async(playbook_id="does-not-exist")
    assert exc_info.value.status_code == 404


@pytest.mark.asyncio
async def test_run_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.run_async(playbook_id="pb1")
    assert exc_info.value.status_code == 503


def test_run_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"chatId": "chat-1"}),
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
    result = bundle.sdk.playbooks.run(playbook_id="pb1", retries=retry_config)
    assert len(bundle.transport.requests) == 2
    assert result.chat_id == "chat-1"


def test_run_retries_exhausted_raises(make_sdk, sequence_handler):
    """When max_elapsed_time is exceeded, retry_with_backoff returns the last
    (still-erroring) response as-is, which then flows through the normal
    5xx handling in run() and raises TextqlDefaultError."""
    handler = sequence_handler(
        [
            json_response(500, {"message": "still failing"}),
            json_response(500, {"message": "still failing"}),
            json_response(500, {"message": "still failing"}),
        ]
    )
    bundle = make_sdk(handler)
    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1, max_interval=2, exponent=1.0, max_elapsed_time=1
        ),
        retry_connection_errors=False,
    )
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.run(playbook_id="pb1", retries=retry_config)
    assert exc_info.value.status_code == 500


def test_run_unicode_chat_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "チャット-🎯"}))
    result = bundle.sdk.playbooks.run(playbook_id="pb1")
    assert result.chat_id == "チャット-🎯"


def test_run_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-1"}))
    override_url = "https://override.invalid"

    bundle.sdk.playbooks.run(playbook_id="pb1", server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_run_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-1"}))

    bundle.sdk.playbooks.run(
        playbook_id="pb1", http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_run_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "chat-1"}))

    result = bundle.sdk.playbooks.run(playbook_id="pb1", timeout_ms=5000)

    assert result.chat_id == "chat-1"


# --------------------------------------------------------------------------
# cancel_template_execution
# --------------------------------------------------------------------------


def test_cancel_template_execution_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": True, "cancelledCount": 3})
    )

    result = bundle.sdk.playbooks.cancel_template_execution(
        template_header_id="hdr-1", playbook_id="pb1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/CancelTemplateExecution"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {
        "templateHeaderId": "hdr-1",
        "playbookId": "pb1",
    }
    assert result.success is True
    assert result.cancelled_count == 3


@pytest.mark.asyncio
async def test_cancel_template_execution_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = await bundle.sdk.playbooks.cancel_template_execution_async(
        template_header_id="hdr-1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/CancelTemplateExecution"
    assert result.success is False


def test_cancel_template_execution_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.cancel_template_execution(template_header_id="missing")
    assert exc_info.value.status_code == 404


def test_cancel_template_execution_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.cancel_template_execution(template_header_id="hdr-1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# get_batch_run
# --------------------------------------------------------------------------


def test_get_batch_run_sync_sends_correct_request(make_sdk):
    payload = {
        "batchRun": {
            "id": "batch-1",
            "playbookId": "pb1",
            "templateHeaderId": "hdr-1",
            "templateDataIds": ["tmpl-1", "tmpl-2"],
        }
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.get_batch_run(batch_run_id="batch-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetPlaybookBatchRun"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"batchRunId": "batch-1"}
    assert result.batch_run.id == "batch-1"
    assert result.batch_run.template_data_ids == ["tmpl-1", "tmpl-2"]


@pytest.mark.asyncio
async def test_get_batch_run_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"batchRun": {"id": "batch-2"}}))

    result = await bundle.sdk.playbooks.get_batch_run_async(batch_run_id="batch-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetPlaybookBatchRun"
    assert result.batch_run.id == "batch-2"


def test_get_batch_run_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_batch_run(batch_run_id="missing")
    assert exc_info.value.status_code == 404


def test_get_batch_run_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_batch_run(batch_run_id="batch-1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_batch_runs
# --------------------------------------------------------------------------


def test_list_batch_runs_sync_sends_correct_request(make_sdk):
    payload = {
        "batchRuns": [{"id": "batch-1"}, {"id": "batch-2"}],
        "totalCount": 2,
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.list_batch_runs(playbook_id="pb1", limit=10, offset=0)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/ListPlaybookBatchRuns"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {
        "playbookId": "pb1",
        "limit": 10,
        "offset": 0,
    }
    assert result.total_count == 2
    assert len(result.batch_runs) == 2


@pytest.mark.asyncio
async def test_list_batch_runs_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"batchRuns": []}))

    result = await bundle.sdk.playbooks.list_batch_runs_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/ListPlaybookBatchRuns"
    assert result.batch_runs == []


def test_list_batch_runs_omits_unset_nullable_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.list_batch_runs(playbook_id="pb1")

    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb1"}
    assert "limit" not in body
    assert "offset" not in body


def test_list_batch_runs_explicit_null_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.list_batch_runs(playbook_id="pb1", limit=None, offset=None)

    body = bundle.transport.body_json()
    assert body["limit"] is None
    assert body["offset"] is None


def test_list_batch_runs_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_batch_runs(playbook_id="pb1")
    assert exc_info.value.status_code == 400


def test_list_batch_runs_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_batch_runs(playbook_id="pb1")
    assert exc_info.value.status_code == 500


def test_list_batch_runs_empty_list(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"batchRuns": [], "totalCount": 0}))
    result = bundle.sdk.playbooks.list_batch_runs(playbook_id="pb1")
    assert result.batch_runs == []
    assert result.total_count == 0


# --------------------------------------------------------------------------
# get_playbook_lineage
# --------------------------------------------------------------------------


def test_get_playbook_lineage_sync_sends_correct_request(make_sdk):
    payload = {
        "parent": {"playbookId": "pb-parent", "name": "Parent", "status": "STATUS_ACTIVE"},
        "duplicates": [
            {"playbookId": "pb-dup-1", "name": "Dup 1"},
            {"playbookId": "pb-dup-2", "name": "Dup 2"},
        ],
        "originPlaybookId": "pb-origin",
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.get_playbook_lineage(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetPlaybookLineage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.parent.playbook_id == "pb-parent"
    assert len(result.duplicates) == 2
    assert result.duplicates[1].playbook_id == "pb-dup-2"
    assert result.origin_playbook_id == "pb-origin"


@pytest.mark.asyncio
async def test_get_playbook_lineage_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"duplicates": []}))

    result = await bundle.sdk.playbooks.get_playbook_lineage_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetPlaybookLineage"
    assert result.duplicates == []


def test_get_playbook_lineage_no_parent_no_duplicates(make_sdk):
    from textql_sdk.types import UNSET

    bundle = make_sdk(lambda req: json_response(200, {}))
    result = bundle.sdk.playbooks.get_playbook_lineage(playbook_id="pb1")
    assert result.parent is None
    assert result.duplicates is None
    # originPlaybookId is OptionalNullable(str): when the field is absent
    # from the response JSON entirely, it should remain UNSET (not coerced
    # to None) -- this distinguishes "field absent" from "field explicitly
    # null" for OptionalNullable fields.
    assert result.origin_playbook_id == UNSET


def test_get_playbook_lineage_origin_explicit_null(make_sdk):
    """originPlaybookId is OptionalNullable(str) -- when the API returns an
    explicit null it must round-trip to Python None (not UNSET)."""
    payload = {"originPlaybookId": None}
    bundle = make_sdk(lambda req: json_response(200, payload))
    result = bundle.sdk.playbooks.get_playbook_lineage(playbook_id="pb1")
    assert result.origin_playbook_id is None


def test_get_playbook_lineage_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_playbook_lineage(playbook_id="missing")
    assert exc_info.value.status_code == 404


def test_get_playbook_lineage_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_playbook_lineage(playbook_id="pb1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_get_playbook_lineage_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.get_playbook_lineage_async(playbook_id="pb1")
    assert exc_info.value.status_code == 502


def test_get_playbook_lineage_unicode_names(make_sdk):
    payload = {
        "parent": {"playbookId": "pb-parent", "name": "親プレイブック 🇯🇵"},
        "duplicates": [],
    }
    bundle = make_sdk(lambda req: json_response(200, payload))
    result = bundle.sdk.playbooks.get_playbook_lineage(playbook_id="pb1")
    assert result.parent.name == "親プレイブック 🇯🇵"


def test_get_playbook_lineage_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"duplicates": []}),
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
    result = bundle.sdk.playbooks.get_playbook_lineage(playbook_id="pb1", retries=retry_config)
    assert len(bundle.transport.requests) == 2
    assert result.duplicates == []
