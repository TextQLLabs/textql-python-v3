"""Unit tests for Playbooks attachment operations: attach/remove dashboard and dataset."""
from __future__ import annotations

import pytest

from textql_sdk import errors, models, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PB_PATH = "/textql.rpc.public.playbook.PlaybookService"


# --------------------------------------------------------------------------
# attach_dashboard
# --------------------------------------------------------------------------


def test_attach_dashboard_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"dashboard": {"id": "dash-1", "name": "Dash"}})
    )

    result = bundle.sdk.playbooks.attach_dashboard(
        playbook_id="pb1", dashboard_id="dash-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/AttachDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1", "dashboardId": "dash-1"}
    assert result.dashboard.id == "dash-1"
    assert result.dashboard.name == "Dash"


@pytest.mark.asyncio
async def test_attach_dashboard_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {"id": "dash-2"}}))

    result = await bundle.sdk.playbooks.attach_dashboard_async(
        playbook_id="pb1", dashboard_id="dash-2"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/AttachDashboard"
    assert result.dashboard.id == "dash-2"


def test_attach_dashboard_omits_none_fields_not_passed(make_sdk):
    """playbook_id/dashboard_id default to None (Optional, not
    OptionalNullable) -- when omitted the fields should still not appear."""
    bundle = make_sdk(lambda req: json_response(200, {"dashboard": {}}))

    bundle.sdk.playbooks.attach_dashboard()

    body = bundle.transport.body_json()
    assert body == {}


def test_attach_dashboard_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.attach_dashboard(playbook_id="pb1", dashboard_id="missing")
    assert exc_info.value.status_code == 404


def test_attach_dashboard_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.attach_dashboard(playbook_id="pb1", dashboard_id="dash-1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_attach_dashboard_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.attach_dashboard_async(
            playbook_id="pb1", dashboard_id="dash-1"
        )
    assert exc_info.value.status_code == 400


def test_attach_dashboard_unicode_name(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"dashboard": {"id": "dash-1", "name": "ダッシュ 📊"}})
    )
    result = bundle.sdk.playbooks.attach_dashboard(playbook_id="pb1", dashboard_id="dash-1")
    assert result.dashboard.name == "ダッシュ 📊"


def test_attach_dashboard_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"dashboard": {"id": "dash-1"}}),
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
    result = bundle.sdk.playbooks.attach_dashboard(
        playbook_id="pb1", dashboard_id="dash-1", retries=retry_config
    )
    assert len(bundle.transport.requests) == 2
    assert result.dashboard.id == "dash-1"


# --------------------------------------------------------------------------
# attach_dataset
# --------------------------------------------------------------------------


def test_attach_dataset_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"dataset": {"document": {}, "id": "ds-1", "name": "My Dataset"}}
        )
    )

    result = bundle.sdk.playbooks.attach_dataset(playbook_id="pb1", dataset_id="ds-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/AttachDataset"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1", "datasetId": "ds-1"}
    assert isinstance(result.dataset, models.Document)
    assert result.dataset.id == "ds-1"
    assert result.dataset.name == "My Dataset"


@pytest.mark.asyncio
async def test_attach_dataset_async_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"dataset": {"document": {}, "id": "ds-2"}})
    )

    result = await bundle.sdk.playbooks.attach_dataset_async(
        playbook_id="pb1", dataset_id="ds-2"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/AttachDataset"
    assert result.dataset.id == "ds-2"


def test_attach_dataset_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.attach_dataset(playbook_id="pb1", dataset_id="missing")
    assert exc_info.value.status_code == 404


def test_attach_dataset_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.attach_dataset(playbook_id="pb1", dataset_id="ds-1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_attach_dataset_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.attach_dataset_async(
            playbook_id="pb1", dataset_id="ds-1"
        )
    assert exc_info.value.status_code == 503


def test_attach_dataset_empty_playbook_id_string(make_sdk):
    """Edge case: empty string is a valid (falsy but present) value and must
    still be serialized, not omitted."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.attach_dataset(playbook_id="", dataset_id="ds-1")

    body = bundle.transport.body_json()
    assert body["playbookId"] == ""
    assert body["datasetId"] == "ds-1"


def test_attach_dataset_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(502, {"message": "transient"}),
            json_response(200, {"dataset": {"document": {}, "id": "ds-1"}}),
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
    result = bundle.sdk.playbooks.attach_dataset(
        playbook_id="pb1", dataset_id="ds-1", retries=retry_config
    )
    assert len(bundle.transport.requests) == 2
    assert result.dataset.id == "ds-1"


# --------------------------------------------------------------------------
# remove_dashboard
# --------------------------------------------------------------------------


def test_remove_dashboard_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.remove_dashboard(
        playbook_id="pb1", dashboard_id="dash-1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/RemoveDashboard"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1", "dashboardId": "dash-1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_remove_dashboard_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = await bundle.sdk.playbooks.remove_dashboard_async(
        playbook_id="pb1", dashboard_id="dash-1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/RemoveDashboard"
    assert result.success is False


def test_remove_dashboard_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.remove_dashboard(playbook_id="pb1", dashboard_id="missing")
    assert exc_info.value.status_code == 404


def test_remove_dashboard_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.remove_dashboard(playbook_id="pb1", dashboard_id="dash-1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# remove_dataset
# --------------------------------------------------------------------------


def test_remove_dataset_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.remove_dataset(playbook_id="pb1", dataset_id="ds-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/RemoveDataset"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1", "datasetId": "ds-1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_remove_dataset_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.playbooks.remove_dataset_async(
        playbook_id="pb1", dataset_id="ds-1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/RemoveDataset"
    assert result.success is True


def test_remove_dataset_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.remove_dataset(playbook_id="pb1", dataset_id="missing")
    assert exc_info.value.status_code == 404


def test_remove_dataset_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.remove_dataset(playbook_id="pb1", dataset_id="ds-1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_remove_dataset_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.remove_dataset_async(
            playbook_id="pb1", dataset_id="ds-1"
        )
    assert exc_info.value.status_code == 500
