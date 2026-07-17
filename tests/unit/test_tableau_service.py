"""Unit tests for the Tableau service (sdk.tableau)."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PATH_PREFIX = "/textql.rpc.public.tableau.TableauService"


def assert_common(bundle, path_suffix: str, api_key: str = FAKE_API_KEY):
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/{path_suffix}"
    assert req.headers[AUTH_HEADER_NAME] == api_key


# ---------------------------------------------------------------------------
# generate_embed_token
# ---------------------------------------------------------------------------


def test_generate_embed_token_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"token": "fake-embed-token-xyz", "embedUrl": "https://example.invalid/embed"}
        )
    )

    resp = bundle.sdk.tableau.generate_embed_token(connector_id=1, view_id="view-1")

    assert_common(bundle, "GenerateEmbedToken")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["viewId"] == "view-1"
    assert resp.token == "fake-embed-token-xyz"
    assert resp.embed_url == "https://example.invalid/embed"


async def test_generate_embed_token_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"token": "fake-embed-token-async"}))
    resp = await bundle.sdk.tableau.generate_embed_token_async(connector_id=2, view_id="view-2")
    assert_common(bundle, "GenerateEmbedToken")
    assert resp.token == "fake-embed-token-async"


def test_generate_embed_token_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.generate_embed_token(view_id="missing")
    assert exc_info.value.status_code == 404


async def test_generate_embed_token_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.generate_embed_token_async(view_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_collection_thumbnail
# ---------------------------------------------------------------------------
# NOTE: despite the name, GetCollectionThumbnail returns a *JSON* response
# (models.TextqlRPCPublicTableauGetCollectionThumbnailResponse) with a single
# imageUrl string field, matched via
# utils.match_response(http_res, "200", "application/json") in
# src/textql_sdk/tableau_sdk.py -- it is NOT raw binary image bytes.


def test_get_collection_thumbnail_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"imageUrl": "https://example.invalid/thumb.png"})
    )

    resp = bundle.sdk.tableau.get_collection_thumbnail(dataset_id="ds-1")

    assert_common(bundle, "GetCollectionThumbnail")
    assert bundle.transport.body_json()["datasetId"] == "ds-1"
    assert resp.image_url == "https://example.invalid/thumb.png"


async def test_get_collection_thumbnail_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"imageUrl": "https://example.invalid/t2.png"}))
    resp = await bundle.sdk.tableau.get_collection_thumbnail_async(dataset_id="ds-2")
    assert_common(bundle, "GetCollectionThumbnail")
    assert resp.image_url == "https://example.invalid/t2.png"


def test_get_collection_thumbnail_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.get_collection_thumbnail(dataset_id="missing")
    assert exc_info.value.status_code == 404


async def test_get_collection_thumbnail_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.get_collection_thumbnail_async(dataset_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_connected_app_status
# ---------------------------------------------------------------------------


def test_get_connected_app_status_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "configured": True,
                "appName": "TextQL App",
                "clientIdSuffix": "ab12",
                "secretIdSuffix": "cd34",
            },
        )
    )

    resp = bundle.sdk.tableau.get_connected_app_status(connector_id=1)

    assert_common(bundle, "GetConnectedAppStatus")
    assert bundle.transport.body_json()["connectorId"] == 1
    assert resp.configured is True
    assert resp.app_name == "TextQL App"


async def test_get_connected_app_status_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"configured": False}))
    resp = await bundle.sdk.tableau.get_connected_app_status_async(connector_id=2)
    assert_common(bundle, "GetConnectedAppStatus")
    assert resp.configured is False


def test_get_connected_app_status_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.get_connected_app_status(connector_id=1)
    assert exc_info.value.status_code == 404


async def test_get_connected_app_status_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.get_connected_app_status_async(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_starred_items
# ---------------------------------------------------------------------------


def test_get_starred_items_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"items": [{"itemId": "item-1"}]}))

    resp = bundle.sdk.tableau.get_starred_items(connector_id=1)

    assert_common(bundle, "GetStarredTableauItems")
    assert bundle.transport.body_json()["connectorId"] == 1
    assert len(resp.items) == 1


async def test_get_starred_items_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"items": []}))
    resp = await bundle.sdk.tableau.get_starred_items_async(connector_id=2)
    assert_common(bundle, "GetStarredTableauItems")
    assert resp.items == []


def test_get_starred_items_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.get_starred_items(connector_id=1)
    assert exc_info.value.status_code == 404


async def test_get_starred_items_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.get_starred_items_async(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_projects
# ---------------------------------------------------------------------------


def test_list_projects_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"projects": [{"id": "proj-1", "name": "Sales"}]})
    )

    resp = bundle.sdk.tableau.list_projects(connector_id=1)

    assert_common(bundle, "ListTableauProjects")
    assert bundle.transport.body_json()["connectorId"] == 1
    assert resp.projects[0].id == "proj-1"


async def test_list_projects_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"projects": []}))
    resp = await bundle.sdk.tableau.list_projects_async(connector_id=2)
    assert_common(bundle, "ListTableauProjects")
    assert resp.projects == []


def test_list_projects_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.list_projects(connector_id=1)
    assert exc_info.value.status_code == 404


async def test_list_projects_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.list_projects_async(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_tableau_datasources -- request body is a Union[ProjectID, WorkbookID]
# ---------------------------------------------------------------------------


def test_list_tableau_datasources_sync_with_project_id(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"datasources": [{"id": "ds-1"}]})
    )

    resp = bundle.sdk.tableau.list_tableau_datasources(
        body={"project_id": "proj-1", "connector_id": 1}
    )

    assert_common(bundle, "ListTableauDatasources")
    body = bundle.transport.body_json()
    assert body["projectId"] == "proj-1"
    assert body["connectorId"] == 1
    assert resp.datasources[0].id == "ds-1"


def test_list_tableau_datasources_sync_with_workbook_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"datasources": []}))

    bundle.sdk.tableau.list_tableau_datasources(body={"workbook_id": "wb-1"})

    body = bundle.transport.body_json()
    assert body["workbookId"] == "wb-1"


async def test_list_tableau_datasources_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"datasources": []}))
    resp = await bundle.sdk.tableau.list_tableau_datasources_async(
        body={"project_id": "proj-2"}
    )
    assert_common(bundle, "ListTableauDatasources")
    assert resp.datasources == []


def test_list_tableau_datasources_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.list_tableau_datasources(body={"project_id": "missing"})
    assert exc_info.value.status_code == 404


async def test_list_tableau_datasources_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.list_tableau_datasources_async(body={"project_id": "missing"})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_views
# ---------------------------------------------------------------------------


def test_list_views_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"views": [{"id": "view-1"}]}))

    resp = bundle.sdk.tableau.list_views(
        connector_id=1, workbook_id="wb-1", workbook_name="My Workbook"
    )

    assert_common(bundle, "ListTableauViews")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["workbookId"] == "wb-1"
    assert body["workbookName"] == "My Workbook"
    assert resp.views[0].id == "view-1"


async def test_list_views_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"views": []}))
    resp = await bundle.sdk.tableau.list_views_async(connector_id=2, workbook_id="wb-2")
    assert_common(bundle, "ListTableauViews")
    assert resp.views == []


def test_list_views_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.list_views(workbook_id="missing")
    assert exc_info.value.status_code == 404


async def test_list_views_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.list_views_async(workbook_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_workbooks
# ---------------------------------------------------------------------------


def test_list_workbooks_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"workbooks": [{"id": "wb-1"}]}))

    resp = bundle.sdk.tableau.list_workbooks(
        connector_id=1, project_id="proj-1", project_name="Marketing"
    )

    assert_common(bundle, "ListTableauWorkbooks")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["projectId"] == "proj-1"
    assert body["projectName"] == "Marketing"
    assert resp.workbooks[0].id == "wb-1"


async def test_list_workbooks_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"workbooks": []}))
    resp = await bundle.sdk.tableau.list_workbooks_async(connector_id=2, project_id="proj-2")
    assert_common(bundle, "ListTableauWorkbooks")
    assert resp.workbooks == []


def test_list_workbooks_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.list_workbooks(project_id="missing")
    assert exc_info.value.status_code == 404


async def test_list_workbooks_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.list_workbooks_async(project_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# refresh_collection
# ---------------------------------------------------------------------------


def test_refresh_collection_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"viewsCount": 3, "datasourcesCount": 1})
    )

    resp = bundle.sdk.tableau.refresh_collection(dataset_id="ds-1")

    assert_common(bundle, "RefreshTableauCollection")
    assert bundle.transport.body_json()["datasetId"] == "ds-1"
    assert resp.views_count == 3
    assert resp.datasources_count == 1


async def test_refresh_collection_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"viewsCount": 0}))
    resp = await bundle.sdk.tableau.refresh_collection_async(dataset_id="ds-2")
    assert_common(bundle, "RefreshTableauCollection")
    assert resp.views_count == 0


def test_refresh_collection_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.refresh_collection(dataset_id="missing")
    assert exc_info.value.status_code == 404


async def test_refresh_collection_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.refresh_collection_async(dataset_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# reset_connected_app
# ---------------------------------------------------------------------------


def test_reset_connected_app_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    resp = bundle.sdk.tableau.reset_connected_app(connector_id=1)

    assert_common(bundle, "ResetConnectedApp")
    assert bundle.transport.body_json()["connectorId"] == 1
    assert resp.success is True


async def test_reset_connected_app_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))
    resp = await bundle.sdk.tableau.reset_connected_app_async(connector_id=2)
    assert_common(bundle, "ResetConnectedApp")
    assert resp.success is False


def test_reset_connected_app_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.reset_connected_app(connector_id=1)
    assert exc_info.value.status_code == 404


async def test_reset_connected_app_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.reset_connected_app_async(connector_id=1)
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# star_item
# ---------------------------------------------------------------------------


def test_star_item_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    resp = bundle.sdk.tableau.star_item(
        connector_id=1,
        item_type="ITEM_TYPE_WORKBOOK",
        item_id="wb-1",
        item_name="My Workbook",
    )

    assert_common(bundle, "StarTableauItem")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["itemType"] == "ITEM_TYPE_WORKBOOK"
    assert body["itemId"] == "wb-1"
    assert body["itemName"] == "My Workbook"
    assert resp.success is True


async def test_star_item_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))
    resp = await bundle.sdk.tableau.star_item_async(
        connector_id=2, item_type="ITEM_TYPE_VIEW", item_id="view-1"
    )
    assert_common(bundle, "StarTableauItem")
    assert resp.success is False


def test_star_item_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.star_item(item_id="missing")
    assert exc_info.value.status_code == 404


async def test_star_item_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.star_item_async(item_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# test_tableau_connection -- OptionalNullable fields incl. pat_secret
# ---------------------------------------------------------------------------


def test_test_tableau_connection_sync_full_payload(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    resp = bundle.sdk.tableau.test_tableau_connection(
        connector_id=1,
        server_url_="https://tableau.example.invalid",
        site_name="my-site",
        pat_name="fake-pat-name",
        pat_secret="fake-pat-secret-123",
    )

    assert_common(bundle, "TestTableauConnection")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["serverUrl"] == "https://tableau.example.invalid"
    assert body["siteName"] == "my-site"
    assert body["patName"] == "fake-pat-name"
    assert body["patSecret"] == "fake-pat-secret-123"
    assert resp.success is True


def test_test_tableau_connection_unset_fields_omitted(make_sdk):
    """All fields are OptionalNullable[...]=UNSET by default; omitting them
    should omit the keys entirely (per
    TextqlRPCPublicTableauTestTableauConnectionRequest.serialize_model)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.tableau.test_tableau_connection()

    body = bundle.transport.body_json()
    for key in ("connectorId", "serverUrl", "siteName", "patName", "patSecret"):
        assert key not in body, f"expected {key!r} to be omitted when unset"


def test_test_tableau_connection_explicit_none_included_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.tableau.test_tableau_connection(
        connector_id=None,
        server_url_=None,
        site_name=None,
        pat_name=None,
        pat_secret=None,
    )

    body = bundle.transport.body_json()
    for key in ("connectorId", "serverUrl", "siteName", "patName", "patSecret"):
        assert key in body, f"expected {key!r} to be present (explicit None)"
        assert body[key] is None


async def test_test_tableau_connection_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))
    resp = await bundle.sdk.tableau.test_tableau_connection_async(
        pat_secret="fake-pat-secret-456"
    )
    assert_common(bundle, "TestTableauConnection")
    assert resp.success is False


def test_test_tableau_connection_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.test_tableau_connection()
    assert exc_info.value.status_code == 404


async def test_test_tableau_connection_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.test_tableau_connection_async()
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# unstar_tableau_item
# ---------------------------------------------------------------------------


def test_unstar_tableau_item_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    resp = bundle.sdk.tableau.unstar_tableau_item(
        connector_id=1, item_type="ITEM_TYPE_DATASOURCE", item_id="ds-1"
    )

    assert_common(bundle, "UnstarTableauItem")
    body = bundle.transport.body_json()
    assert body["connectorId"] == 1
    assert body["itemType"] == "ITEM_TYPE_DATASOURCE"
    assert body["itemId"] == "ds-1"
    assert resp.success is True


async def test_unstar_tableau_item_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))
    resp = await bundle.sdk.tableau.unstar_tableau_item_async(
        connector_id=2, item_type="ITEM_TYPE_PROJECT", item_id="proj-1"
    )
    assert_common(bundle, "UnstarTableauItem")
    assert resp.success is False


def test_unstar_tableau_item_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.tableau.unstar_tableau_item(item_id="missing")
    assert exc_info.value.status_code == 404


async def test_unstar_tableau_item_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.tableau.unstar_tableau_item_async(item_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# retries
# ---------------------------------------------------------------------------


def test_retries_backoff_retries_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "server error"}),
            json_response(200, {"projects": [{"id": "proj-1"}]}),
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

    resp = bundle.sdk.tableau.list_projects(retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.projects[0].id == "proj-1"


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

    resp = await bundle.sdk.tableau.reset_connected_app_async(retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.success is True


# ---------------------------------------------------------------------------
# server_url / http_headers / timeout_ms per-call overrides
# ---------------------------------------------------------------------------


def test_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    override_url = "https://override.invalid"

    bundle.sdk.tableau.list_projects(server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.tableau.list_projects(http_headers={"X-Custom-Header": "custom-value"})

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.tableau.list_projects(timeout_ms=5000)

    assert len(bundle.transport.requests) == 1
