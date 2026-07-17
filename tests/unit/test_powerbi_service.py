"""Unit tests for the PowerBI service (sdk.powerbi)."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PATH_PREFIX = "/textql.rpc.public.powerbi.PowerBIService"


def assert_common(bundle, path_suffix: str, api_key: str = FAKE_API_KEY):
    """Assert method/path/auth-header invariants that apply to every call."""
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/{path_suffix}"
    assert req.headers[AUTH_HEADER_NAME] == api_key


# ---------------------------------------------------------------------------
# export_report_image
# ---------------------------------------------------------------------------
# NOTE: despite the name, ExportPowerBIReportImage returns a *JSON* response
# (models.TextqlRPCPublicPowerbiExportPowerBIReportImageResponse) with
# imageData/imageUrl string fields, matched via
# utils.match_response(http_res, "200", "application/json") in
# src/textql_sdk/powerbi_sdk.py -- it is NOT raw binary image bytes.


def test_export_report_image_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"imageData": "ZmFrZS1pbWFnZS1ieXRlcw==", "imageUrl": "https://example.invalid/img.png"}
        )
    )

    resp = bundle.sdk.powerbi.export_report_image(
        connector_id=1, workspace_id="ws-1", report_id="report-1"
    )

    assert_common(bundle, "ExportPowerBIReportImage")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["workspaceId"] == "ws-1"
    assert body["reportId"] == "report-1"
    assert resp.image_data == "ZmFrZS1pbWFnZS1ieXRlcw=="
    assert resp.image_url == "https://example.invalid/img.png"


async def test_export_report_image_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"imageData": "YXN5bmMtYnl0ZXM=", "imageUrl": "https://example.invalid/img2.png"})
    )

    resp = await bundle.sdk.powerbi.export_report_image_async(
        connector_id=2, workspace_id="ws-2", report_id="report-2"
    )

    assert_common(bundle, "ExportPowerBIReportImage")
    assert resp.image_data == "YXN5bmMtYnl0ZXM="


def test_export_report_image_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.export_report_image(report_id="missing")
    assert exc_info.value.status_code == 404


async def test_export_report_image_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.export_report_image_async(report_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# generate_embed_token
# ---------------------------------------------------------------------------


def test_generate_embed_token_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"token": "fake-embed-token-xyz", "tokenId": "tok-1", "expiration": "2030-01-01T00:00:00Z"}
        )
    )

    resp = bundle.sdk.powerbi.generate_embed_token(
        connector_id=1, workspace_id="ws-1", report_id="report-1", dataset_id="ds-1"
    )

    assert_common(bundle, "GeneratePowerBIEmbedToken")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["workspaceId"] == "ws-1"
    assert body["reportId"] == "report-1"
    assert body["datasetId"] == "ds-1"
    assert resp.token == "fake-embed-token-xyz"
    assert resp.token_id == "tok-1"


async def test_generate_embed_token_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"token": "fake-embed-token-async-abc"}))

    resp = await bundle.sdk.powerbi.generate_embed_token_async(
        connector_id=2, workspace_id="ws-2", report_id="report-2", dataset_id="ds-2"
    )

    assert_common(bundle, "GeneratePowerBIEmbedToken")
    assert resp.token == "fake-embed-token-async-abc"


def test_generate_embed_token_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.generate_embed_token(report_id="missing")
    assert exc_info.value.status_code == 404


async def test_generate_embed_token_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.generate_embed_token_async(report_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_dataset_preview
# ---------------------------------------------------------------------------


def test_get_dataset_preview_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"tablePreviews": [], "success": True})
    )

    resp = bundle.sdk.powerbi.get_dataset_preview(
        connector_id=1,
        workspace_id="ws-1",
        dataset_id="ds-1",
        dataset_name="My Dataset",
        limit=50,
    )

    assert_common(bundle, "GetPowerBIDatasetPreview")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["workspaceId"] == "ws-1"
    assert body["datasetId"] == "ds-1"
    assert body["datasetName"] == "My Dataset"
    assert body["limit"] == 50
    assert resp.success is True


async def test_get_dataset_preview_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))
    resp = await bundle.sdk.powerbi.get_dataset_preview_async(dataset_id="ds-2")
    assert_common(bundle, "GetPowerBIDatasetPreview")
    assert resp.success is False


def test_get_dataset_preview_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.get_dataset_preview(dataset_id="missing")
    assert exc_info.value.status_code == 404


async def test_get_dataset_preview_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.get_dataset_preview_async(dataset_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_synced_items
# ---------------------------------------------------------------------------


def test_get_synced_items_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "reports": [{"report": {"id": "r1"}, "workspaceId": "ws-1"}],
                "datasets": [{"dataset": {"id": "d1"}, "workspaceId": "ws-1"}],
            },
        )
    )

    resp = bundle.sdk.powerbi.get_synced_items(connector_id=7)

    assert_common(bundle, "GetSyncedPowerBIItems")
    assert bundle.transport.body_json()["connectorId"] == 7
    # TextqlRPCPublicPowerbiSyncedPowerBIReport/-Dataset wrap the underlying
    # report/dataset object plus sync metadata (workspace_id, synced_at).
    assert resp.reports[0].report.id == "r1"
    assert resp.reports[0].workspace_id == "ws-1"
    assert resp.datasets[0].dataset.id == "d1"


async def test_get_synced_items_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": [], "datasets": []}))
    resp = await bundle.sdk.powerbi.get_synced_items_async(connector_id=8)
    assert_common(bundle, "GetSyncedPowerBIItems")
    assert resp.reports == []


def test_get_synced_items_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.get_synced_items(connector_id=1)
    assert exc_info.value.status_code == 404


async def test_get_synced_items_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.get_synced_items_async(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list (ListPowerBIDatasets)
# ---------------------------------------------------------------------------


def test_list_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"datasets": [{"id": "ds-1", "name": "Sales"}]})
    )

    resp = bundle.sdk.powerbi.list(connector_id=1, workspace_id="ws-1")

    assert_common(bundle, "ListPowerBIDatasets")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["workspaceId"] == "ws-1"
    assert resp.datasets[0].id == "ds-1"


async def test_list_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"datasets": []}))
    resp = await bundle.sdk.powerbi.list_async(connector_id=2)
    assert_common(bundle, "ListPowerBIDatasets")
    assert resp.datasets == []


def test_list_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.list()
    assert exc_info.value.status_code == 404


async def test_list_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.list_async()
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_reports
# ---------------------------------------------------------------------------


def test_list_reports_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"reports": [{"id": "rep-1", "name": "Q1"}]})
    )

    resp = bundle.sdk.powerbi.list_reports(connector_id=1, workspace_id="ws-1")

    assert_common(bundle, "ListPowerBIReports")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["workspaceId"] == "ws-1"
    assert resp.reports[0].id == "rep-1"


async def test_list_reports_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"reports": []}))
    resp = await bundle.sdk.powerbi.list_reports_async(connector_id=2)
    assert_common(bundle, "ListPowerBIReports")
    assert resp.reports == []


def test_list_reports_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.list_reports()
    assert exc_info.value.status_code == 404


async def test_list_reports_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.list_reports_async()
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_workspaces
# ---------------------------------------------------------------------------


def test_list_workspaces_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"workspaces": [{"id": "ws-1", "name": "Marketing"}]})
    )

    resp = bundle.sdk.powerbi.list_workspaces(connector_id=1)

    assert_common(bundle, "ListPowerBIWorkspaces")
    assert bundle.transport.body_json()["connectorId"] == 1
    assert resp.workspaces[0].id == "ws-1"


async def test_list_workspaces_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"workspaces": []}))
    resp = await bundle.sdk.powerbi.list_workspaces_async(connector_id=2)
    assert_common(bundle, "ListPowerBIWorkspaces")
    assert resp.workspaces == []


def test_list_workspaces_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.list_workspaces()
    assert exc_info.value.status_code == 404


async def test_list_workspaces_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.list_workspaces_async()
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# sync_power_bi_items -- list serialization (reports/datasets), incl. empty list
# ---------------------------------------------------------------------------


def test_sync_power_bi_items_sync_with_lists(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "syncedReportIds": ["r1", "r2"],
                "syncedDatasetIds": ["d1"],
            },
        )
    )

    resp = bundle.sdk.powerbi.sync_power_bi_items(
        connector_id=1,
        workspace_id="ws-1",
        workspace_name="Marketing",
        reports=[{"id": "r1", "name": "Report One"}, {"id": "r2"}],
        datasets=[{"id": "d1", "name": "Dataset One"}],
    )

    assert_common(bundle, "SyncPowerBIItems")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["workspaceId"] == "ws-1"
    assert body["workspaceName"] == "Marketing"
    assert isinstance(body["reports"], list)
    assert len(body["reports"]) == 2
    assert body["reports"][0]["id"] == "r1"
    assert body["reports"][0]["name"] == "Report One"
    assert isinstance(body["datasets"], list)
    assert body["datasets"][0]["id"] == "d1"
    assert resp.success is True
    assert resp.synced_report_ids == ["r1", "r2"]
    assert resp.synced_dataset_ids == ["d1"]


def test_sync_power_bi_items_empty_lists(make_sdk):
    """Passing empty lists for reports/datasets should serialize as empty JSON
    arrays, not be omitted or become null."""
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.powerbi.sync_power_bi_items(
        connector_id=1,
        workspace_id="ws-1",
        reports=[],
        datasets=[],
    )

    body = bundle.transport.body_json()
    assert body["reports"] == []
    assert body["datasets"] == []


async def test_sync_power_bi_items_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    resp = await bundle.sdk.powerbi.sync_power_bi_items_async(
        connector_id=2, workspace_id="ws-2", reports=[], datasets=[]
    )

    assert_common(bundle, "SyncPowerBIItems")
    assert resp.success is True


def test_sync_power_bi_items_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.sync_power_bi_items(workspace_id="missing")
    assert exc_info.value.status_code == 404


async def test_sync_power_bi_items_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.sync_power_bi_items_async(workspace_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# test_connection -- OptionalNullable[int/str] fields
# ---------------------------------------------------------------------------


def test_test_connection_sync_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    resp = bundle.sdk.powerbi.test_connection(
        connector_id=1,
        tenant_id="tenant-1",
        client_id="client-1",
        client_secret="fake-test-secret-123",
    )

    assert_common(bundle, "TestPowerBIConnection")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["tenantId"] == "tenant-1"
    assert body["clientId"] == "client-1"
    assert body["clientSecret"] == "fake-test-secret-123"
    assert resp.success is True


def test_test_connection_unset_fields_omitted(make_sdk):
    """connector_id/tenant_id/client_id/client_secret are all
    OptionalNullable[...]=UNSET by default; omitting them should omit the keys
    entirely from the serialized body (per
    TextqlRPCPublicPowerbiTestPowerBIConnectionRequest.serialize_model)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.powerbi.test_connection()

    body = bundle.transport.body_json()
    assert "connectorId" not in body
    assert "tenantId" not in body
    assert "clientId" not in body
    assert "clientSecret" not in body


def test_test_connection_explicit_none_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.powerbi.test_connection(
        connector_id=None, tenant_id=None, client_id=None, client_secret=None
    )

    body = bundle.transport.body_json()
    assert "connectorId" in body
    assert body["connectorId"] is None
    assert "tenantId" in body
    assert body["tenantId"] is None
    assert "clientId" in body
    assert body["clientId"] is None
    assert "clientSecret" in body
    assert body["clientSecret"] is None


async def test_test_connection_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))
    resp = await bundle.sdk.powerbi.test_connection_async(client_secret="fake-test-secret-456")
    assert_common(bundle, "TestPowerBIConnection")
    assert resp.success is False


def test_test_connection_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.test_connection()
    assert exc_info.value.status_code == 404


async def test_test_connection_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.test_connection_async()
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# unsync_items -- list serialization (report_ids/dataset_ids), incl. empty list
# ---------------------------------------------------------------------------


def test_unsync_items_sync_with_lists(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    resp = bundle.sdk.powerbi.unsync_items(
        connector_id=1, report_ids=["r1", "r2"], dataset_ids=["d1"]
    )

    assert_common(bundle, "UnsyncPowerBIItems")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["reportIds"] == ["r1", "r2"]
    assert body["datasetIds"] == ["d1"]
    assert resp.success is True


def test_unsync_items_empty_lists(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.powerbi.unsync_items(connector_id=1, report_ids=[], dataset_ids=[])

    body = bundle.transport.body_json()
    assert body["reportIds"] == []
    assert body["datasetIds"] == []


async def test_unsync_items_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    resp = await bundle.sdk.powerbi.unsync_items_async(
        connector_id=2, report_ids=["r3"], dataset_ids=["d2"]
    )
    assert_common(bundle, "UnsyncPowerBIItems")
    assert resp.success is True


def test_unsync_items_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.powerbi.unsync_items()
    assert exc_info.value.status_code == 404


async def test_unsync_items_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.powerbi.unsync_items_async()
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# retries
# ---------------------------------------------------------------------------


def test_retries_backoff_retries_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "server error"}),
            json_response(200, {"workspaces": [{"id": "ws-1"}]}),
        ]
    )
    bundle = make_sdk(handler)

    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=False,
    )

    resp = bundle.sdk.powerbi.list_workspaces(retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.workspaces[0].id == "ws-1"


async def test_retries_backoff_retries_then_succeeds_async(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "server error"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)

    retry_config = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=False,
    )

    resp = await bundle.sdk.powerbi.test_connection_async(retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.success is True


# ---------------------------------------------------------------------------
# server_url / http_headers / timeout_ms per-call overrides
# ---------------------------------------------------------------------------


def test_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    override_url = "https://override.invalid"

    bundle.sdk.powerbi.list_workspaces(server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.powerbi.list_workspaces(http_headers={"X-Custom-Header": "custom-value"})

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.powerbi.list_workspaces(timeout_ms=5000)

    assert len(bundle.transport.requests) == 1
