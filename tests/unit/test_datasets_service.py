"""Unit tests for the Datasets service (sdk.datasets)."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, utils

BASE_PATH = "/textql.rpc.public.dataset.DatasetService"


# ---------------------------------------------------------------------------
# CreateFolder
# ---------------------------------------------------------------------------


def test_create_folder_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.datasets.create_folder(
        name="my-folder", parent_path=["a", "b"]
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateFolder"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["name"] == "my-folder"
    assert body["parentPath"] == ["a", "b"]
    assert result is not None


@pytest.mark.asyncio
async def test_create_folder_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.create_folder_async(name="folder-async")

    body = bundle.transport.body_json()
    assert body["name"] == "folder-async"
    assert "parentPath" not in body


def test_create_folder_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "bad folder"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.create_folder(name="x")

    assert exc_info.value.status_code == 422


# ---------------------------------------------------------------------------
# CreatePowerBIDataset
# ---------------------------------------------------------------------------


def test_create_power_bi_dataset_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"datasetId": "ds-1"}))

    bundle.sdk.datasets.create_power_bi_dataset(
        connector_id=5,
        name="pbi-dataset",
        workspace_id="ws-1",
        workspace_name="workspace one",
        reports=[{"id": "r1", "name": "Report 1"}],
        datasets=[{"id": "d1", "name": "Dataset 1"}],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreatePowerBIDataset"
    body = bundle.transport.body_json()
    assert body["connectorId"] == 5
    assert body["workspaceId"] == "ws-1"
    assert body["reports"] == [{"id": "r1", "name": "Report 1"}]
    assert body["datasets"] == [{"id": "d1", "name": "Dataset 1"}]


@pytest.mark.asyncio
async def test_create_power_bi_dataset_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.create_power_bi_dataset_async(name="pbi-async")

    body = bundle.transport.body_json()
    assert body["name"] == "pbi-async"
    assert "reports" not in body
    assert "datasets" not in body


# ---------------------------------------------------------------------------
# CreateTableauDataset
# ---------------------------------------------------------------------------


def test_create_tableau_dataset_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.create_tableau_dataset(
        connector_id=9,
        name="tableau-ds",
        project_id="proj-1",
        views=[{"id": "v1", "name": "View 1"}],
        datasources=[{"id": "ds1", "name": "Datasource 1"}],
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/CreateTableauDataset"
    body = bundle.transport.body_json()
    assert body["projectId"] == "proj-1"
    assert body["views"] == [{"id": "v1", "name": "View 1"}]
    assert body["datasources"] == [{"id": "ds1", "name": "Datasource 1"}]


@pytest.mark.asyncio
async def test_create_tableau_dataset_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.create_tableau_dataset_async(name="tab-async")

    body = bundle.transport.body_json()
    assert body["name"] == "tab-async"


def test_create_tableau_dataset_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.create_tableau_dataset(name="x")

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# CreateUploadPresignUrl / ProcessUploadPresignUrl (two-step upload flow)
# ---------------------------------------------------------------------------


def test_create_upload_presign_url_sync_full_fields(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "datasetId": "ds-42",
                "datasetVersion": 1,
                "presignUrl": "https://s3.example.com/upload?sig=abc",
            },
        )
    )

    result = bundle.sdk.datasets.create_upload_presign_url(
        type_="TYPE_TABULAR",
        file_name="data.csv",
        folder_path=["reports", "2024"],
        ephemeral=True,
        expires_in_days=30,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CreateUploadPresignUrl"
    body = bundle.transport.body_json()
    assert body["type"] == "TYPE_TABULAR"
    assert body["fileName"] == "data.csv"
    assert body["folderPath"] == ["reports", "2024"]
    assert body["ephemeral"] is True
    assert body["expiresInDays"] == 30

    assert result.dataset_id == "ds-42"
    assert result.dataset_version == 1
    assert result.presign_url == "https://s3.example.com/upload?sig=abc"


def test_create_upload_presign_url_expires_in_days_unset_omitted(make_sdk):
    """expires_in_days is OptionalNullable[int] = UNSET by default; when not
    passed, it must be omitted entirely from the serialized body (not sent as
    null)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.create_upload_presign_url(file_name="f.csv")

    body = bundle.transport.body_json()
    assert "expiresInDays" not in body


def test_create_upload_presign_url_expires_in_days_explicit_none_is_null(make_sdk):
    """When explicitly passed as None, the Nullable field must serialize as
    JSON null (distinct from omission)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.create_upload_presign_url(file_name="f.csv", expires_in_days=None)

    body = bundle.transport.body_json()
    assert "expiresInDays" in body
    assert body["expiresInDays"] is None


@pytest.mark.asyncio
async def test_create_upload_presign_url_async(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"presignUrl": "https://s3.example.com/x"})
    )

    result = await bundle.sdk.datasets.create_upload_presign_url_async(
        file_name="async.csv"
    )

    assert result.presign_url == "https://s3.example.com/x"


def test_process_upload_presign_url_sync(make_sdk):
    """Second step of the upload flow: after uploading to the presigned URL,
    the client tells the server the upload is complete."""
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "dataset": {
                    "tabularFile": {"category": "CATEGORY_UNKNOWN"},
                    "id": "ds-42",
                    "name": "data.csv",
                    "version": 1,
                }
            },
        )
    )

    result = bundle.sdk.datasets.process_upload_presign_url(
        dataset_id="ds-42", dataset_version=1
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/ProcessUploadPresignUrl"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-42"
    assert body["datasetVersion"] == 1
    assert result.dataset.id == "ds-42"
    assert result.dataset.name == "data.csv"


@pytest.mark.asyncio
async def test_process_upload_presign_url_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.process_upload_presign_url_async(
        dataset_id="ds-99", dataset_version=2
    )

    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-99"
    assert body["datasetVersion"] == 2


def test_upload_presign_flow_end_to_end(make_sdk):
    """Simulates the full two-step presigned-upload flow against a sequence of
    responses: first CreateUploadPresignUrl, then ProcessUploadPresignUrl."""
    responses = iter(
        [
            json_response(
                200,
                {
                    "datasetId": "ds-1",
                    "datasetVersion": 1,
                    "presignUrl": "https://s3.example.com/put",
                },
            ),
            json_response(
                200,
                {
                    "dataset": {
                        "tabularFile": {"category": "CATEGORY_UNKNOWN"},
                        "id": "ds-1",
                        "version": 1,
                    }
                },
            ),
        ]
    )
    bundle = make_sdk(lambda req: next(responses))

    presign = bundle.sdk.datasets.create_upload_presign_url(
        type_="TYPE_TABULAR", file_name="foo.csv"
    )
    assert presign.presign_url == "https://s3.example.com/put"

    processed = bundle.sdk.datasets.process_upload_presign_url(
        dataset_id=presign.dataset_id, dataset_version=presign.dataset_version
    )
    assert processed.dataset.id == "ds-1"

    assert len(bundle.transport.requests) == 2
    assert bundle.transport.requests[0].url.path == f"{BASE_PATH}/CreateUploadPresignUrl"
    assert (
        bundle.transport.requests[1].url.path == f"{BASE_PATH}/ProcessUploadPresignUrl"
    )


def test_create_upload_presign_url_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad type"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.create_upload_presign_url(file_name="f.csv")

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# Delete
# ---------------------------------------------------------------------------


def test_delete_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    bundle.sdk.datasets.delete(dataset_id="ds-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/DeleteDataset"
    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-1"


@pytest.mark.asyncio
async def test_delete_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.delete_async(dataset_id="ds-2")

    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-2"


def test_delete_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.delete(dataset_id="missing")

    assert exc_info.value.status_code == 404


def test_delete_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.delete(dataset_id="ds-1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Export
# ---------------------------------------------------------------------------


def test_export_sync_with_version_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.export(
        dataset_id="ds-1", preferred_format="FORMAT_CSV", version_id=3
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ExportDataset"
    body = bundle.transport.body_json()
    assert body["preferredFormat"] == "FORMAT_CSV"
    assert body["versionId"] == 3


def test_export_version_id_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.export(dataset_id="ds-1")

    body = bundle.transport.body_json()
    assert "versionId" not in body


def test_export_version_id_explicit_none(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.export(dataset_id="ds-1", version_id=None)

    body = bundle.transport.body_json()
    assert "versionId" in body
    assert body["versionId"] is None


@pytest.mark.asyncio
async def test_export_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.export_async(dataset_id="ds-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/ExportDataset"


# ---------------------------------------------------------------------------
# Fetch (GetDataset)
# ---------------------------------------------------------------------------


def test_fetch_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {"dataset": {"tabularFile": {"category": "CATEGORY_UNKNOWN"}, "id": "ds-1"}},
        )
    )

    result = bundle.sdk.datasets.fetch(dataset_id="ds-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetDataset"
    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-1"
    assert result.dataset.id == "ds-1"


@pytest.mark.asyncio
async def test_fetch_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.fetch_async(dataset_id="ds-2")

    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-2"


def test_fetch_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.fetch(dataset_id="ds-1")

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# GetStats
# ---------------------------------------------------------------------------


def test_get_stats_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get_stats(dataset_id="ds-1", version_id=2)

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetDatasetStats"
    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-1"
    assert body["versionId"] == 2


def test_get_stats_version_id_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get_stats(dataset_id="ds-1")

    body = bundle.transport.body_json()
    assert "versionId" not in body


@pytest.mark.asyncio
async def test_get_stats_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.get_stats_async(dataset_id="ds-1")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetDatasetStats"


# ---------------------------------------------------------------------------
# GetDatasetValues
# ---------------------------------------------------------------------------


def test_get_dataset_values_sync_all_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get_dataset_values(
        dataset_id="ds-1", version_id=1, limit=50, page=2, sheet=0
    )

    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-1"
    assert body["versionId"] == 1
    assert body["limit"] == 50
    assert body["page"] == 2
    assert body["sheet"] == 0


def test_get_dataset_values_optional_nullable_fields_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get_dataset_values(dataset_id="ds-1")

    body = bundle.transport.body_json()
    for key in ("versionId", "limit", "page", "sheet"):
        assert key not in body


def test_get_dataset_values_explicit_none_serializes_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get_dataset_values(dataset_id="ds-1", limit=None, page=None)

    body = bundle.transport.body_json()
    assert body["limit"] is None
    assert body["page"] is None
    assert "versionId" not in body
    assert "sheet" not in body


@pytest.mark.asyncio
async def test_get_dataset_values_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.get_dataset_values_async(dataset_id="ds-1", limit=10)

    body = bundle.transport.body_json()
    assert body["limit"] == 10


# ---------------------------------------------------------------------------
# Get (GetDatasets)
# ---------------------------------------------------------------------------


def test_get_sync_defaults(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"datasets": [], "totalCount": 0})
    )

    bundle.sdk.datasets.get()

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetDatasets"
    body = bundle.transport.body_json()
    # All fields are OptionalNullable/Optional and default to UNSET/None ->
    # nothing should be serialized.
    assert body == {}


def test_get_sync_with_filters(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get(
        types=["TYPE_TABULAR", "TYPE_DOCUMENT"],
        owner_only=True,
        include_subfolders=False,
        path="/reports",
        search_param="q1",
        sort="SORT_NAME_ASC" if False else None,  # keep sort untouched/None
        limit=25,
        cursor="cursor-abc",
    )

    body = bundle.transport.body_json()
    assert body["types"] == ["TYPE_TABULAR", "TYPE_DOCUMENT"]
    assert body["ownerOnly"] is True
    assert body["includeSubfolders"] is False
    assert body["path"] == "/reports"
    assert body["searchParam"] == "q1"
    assert body["limit"] == 25
    assert body["cursor"] == "cursor-abc"


def test_get_path_explicit_none_serializes_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get(path=None, cursor=None)

    body = bundle.transport.body_json()
    assert body["path"] is None
    assert body["cursor"] is None
    assert "searchParam" not in body
    assert "limit" not in body


@pytest.mark.asyncio
async def test_get_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.get_async(owner_only=True)

    body = bundle.transport.body_json()
    assert body["ownerOnly"] is True


# ---------------------------------------------------------------------------
# GetByIds
# ---------------------------------------------------------------------------


def test_get_by_ids_empty_list(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"datasets": []}))

    result = bundle.sdk.datasets.get_by_ids(dataset_ids=[])

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetDatasetsByIds"
    body = bundle.transport.body_json()
    assert body["datasetIds"] == []
    assert result.datasets == []


def test_get_by_ids_single_id(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "datasets": [
                    {
                        "tabularFile": {"category": "CATEGORY_UNKNOWN"},
                        "id": "ds-1",
                        "name": "one.csv",
                    }
                ]
            },
        )
    )

    result = bundle.sdk.datasets.get_by_ids(dataset_ids=["ds-1"])

    body = bundle.transport.body_json()
    assert body["datasetIds"] == ["ds-1"]
    assert len(result.datasets) == 1
    assert result.datasets[0].id == "ds-1"
    assert result.datasets[0].name == "one.csv"


def test_get_by_ids_many_ids(make_sdk):
    ids = [f"ds-{i}" for i in range(25)]
    bundle = make_sdk(lambda req: json_response(200, {"datasets": []}))

    bundle.sdk.datasets.get_by_ids(dataset_ids=ids)

    body = bundle.transport.body_json()
    assert body["datasetIds"] == ids
    assert len(body["datasetIds"]) == 25


def test_get_by_ids_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get_by_ids()

    body = bundle.transport.body_json()
    assert body == {}


@pytest.mark.asyncio
async def test_get_by_ids_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"datasets": []}))

    result = await bundle.sdk.datasets.get_by_ids_async(dataset_ids=["a", "b", "c"])

    body = bundle.transport.body_json()
    assert body["datasetIds"] == ["a", "b", "c"]
    assert result.datasets == []


def test_get_by_ids_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad ids"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.get_by_ids(dataset_ids=["x"])

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# GetFolders
# ---------------------------------------------------------------------------


def test_get_folders_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"folders": []}))

    bundle.sdk.datasets.get_folders(path="/reports")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/GetFolders"
    body = bundle.transport.body_json()
    assert body["path"] == "/reports"


@pytest.mark.asyncio
async def test_get_folders_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.get_folders_async(path="/x")

    body = bundle.transport.body_json()
    assert body["path"] == "/x"


def test_get_folders_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.get_folders(path="/")

    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# UpdateDataset
# ---------------------------------------------------------------------------


def test_update_dataset_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.update_dataset(dataset_id="ds-1", name="new name")

    req = bundle.transport.last_request
    assert req.url.path == f"{BASE_PATH}/UpdateDataset"
    body = bundle.transport.body_json()
    assert body["datasetId"] == "ds-1"
    assert body["name"] == "new name"


def test_update_dataset_name_unset_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.update_dataset(dataset_id="ds-1")

    body = bundle.transport.body_json()
    assert "name" not in body


def test_update_dataset_name_explicit_none_is_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.update_dataset(dataset_id="ds-1", name=None)

    body = bundle.transport.body_json()
    assert "name" in body
    assert body["name"] is None


@pytest.mark.asyncio
async def test_update_dataset_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.datasets.update_dataset_async(dataset_id="ds-1", name="renamed")

    body = bundle.transport.body_json()
    assert body["name"] == "renamed"


def test_update_dataset_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.datasets.update_dataset(dataset_id="ds-1", name="x")

    assert exc_info.value.status_code == 409


# ---------------------------------------------------------------------------
# retries / server_url / http_headers / timeout_ms overrides
# ---------------------------------------------------------------------------


def test_delete_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)

    result = bundle.sdk.datasets.delete(
        dataset_id="ds-1",
        retries=utils.RetryConfig(
            strategy="backoff",
            backoff=utils.BackoffStrategy(
                initial_interval=1,
                max_interval=5,
                exponent=1.0,
                max_elapsed_time=5000,
            ),
            retry_connection_errors=False,
        ),
    )

    assert len(bundle.transport.requests) == 2
    assert result is not None


@pytest.mark.asyncio
async def test_fetch_retries_on_500_then_succeeds_async(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {}),
        ]
    )
    bundle = make_sdk(handler)

    await bundle.sdk.datasets.fetch_async(
        dataset_id="ds-1",
        retries=utils.RetryConfig(
            strategy="backoff",
            backoff=utils.BackoffStrategy(
                initial_interval=1,
                max_interval=5,
                exponent=1.0,
                max_elapsed_time=5000,
            ),
            retry_connection_errors=False,
        ),
    )

    assert len(bundle.transport.requests) == 2


def test_get_stats_server_url_override(make_sdk):
    captured = {}

    def handler(req):
        captured["url"] = str(req.url)
        return json_response(200, {})

    bundle = make_sdk(handler)

    bundle.sdk.datasets.get_stats(
        dataset_id="ds-1", server_url="https://override.invalid"
    )

    assert captured["url"].startswith("https://override.invalid")


def test_delete_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.delete(
        dataset_id="ds-1", http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    # Auth header should still be present alongside custom headers.
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_get_timeout_ms_override_does_not_error(make_sdk):
    """timeout_ms is a per-call override; we can't easily observe the httpx
    timeout value through the mock transport, but we verify the call
    succeeds and doesn't raise when a custom timeout is supplied."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.datasets.get(timeout_ms=15000)

    assert len(bundle.transport.requests) == 1
