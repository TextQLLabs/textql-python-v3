"""Unit tests for the 9 library "config" operations on ``sdk.libraries``."""
from __future__ import annotations

from datetime import timedelta

import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors

URL_PREFIX = "/textql.rpc.public.patches.LibraryService"


# ---------------------------------------------------------------------------
# save_as_config / save_as_config_async
# ---------------------------------------------------------------------------


def test_save_as_config_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"patch": {"id": "patch-1"}, "filePath": "playbooks/foo.yaml"}
        )
    )

    result = bundle.sdk.libraries.save_as_config(
        object_type="playbook", object_id="obj-123"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/SaveObjectAsConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"objectType": "playbook", "objectId": "obj-123"}

    assert result.patch.id == "patch-1"
    assert result.file_path == "playbooks/foo.yaml"


@pytest.mark.asyncio
async def test_save_as_config_async_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"patch": {"id": "patch-2"}, "filePath": "playbooks/bar.yaml"}
        )
    )

    result = await bundle.sdk.libraries.save_as_config_async(
        object_type="playbook", object_id="obj-456"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/SaveObjectAsConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"objectType": "playbook", "objectId": "obj-456"}

    assert result.patch.id == "patch-2"
    assert result.file_path == "playbooks/bar.yaml"


def test_save_as_config_omitted_fields_absent_from_body(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.save_as_config()

    body = bundle.transport.body_json()
    assert body == {}


def test_save_as_config_unicode_and_empty_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.save_as_config(object_type="é中文 \U0001f600", object_id="")

    body = bundle.transport.body_json()
    assert body == {"objectType": "é中文 \U0001f600", "objectId": ""}


@pytest.mark.parametrize("status_code", [400, 404, 422, 500, 503])
def test_save_as_config_error_raises_textql_default_error(make_sdk, status_code):
    bundle = make_sdk(lambda req: json_response(status_code, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.save_as_config(object_type="playbook", object_id="x")

    assert exc_info.value.status_code == status_code


@pytest.mark.asyncio
async def test_save_as_config_async_error_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.save_as_config_async(
            object_type="playbook", object_id="x"
        )

    assert exc_info.value.status_code == 404


def test_save_as_config_large_payload(make_sdk):
    large_id = "x" * 50_000
    bundle = make_sdk(lambda req: json_response(200, {"filePath": "p"}))

    bundle.sdk.libraries.save_as_config(object_type="playbook", object_id=large_id)

    body = bundle.transport.body_json()
    assert body["objectId"] == large_id
    assert len(body["objectId"]) == 50_000


# ---------------------------------------------------------------------------
# save_all_objects_as_config / save_all_objects_as_config_async
# ---------------------------------------------------------------------------


def test_save_all_objects_as_config_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "patch": {"id": "patch-9"},
                "filePaths": ["a.yaml", "b.yaml"],
                "skipped": [{"objectId": "z", "reason": "unsupported"}],
                "alreadyManagedCount": 3,
            },
        )
    )

    result = bundle.sdk.libraries.save_all_objects_as_config(object_type="playbook")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/SaveAllObjectsAsConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"objectType": "playbook"}

    assert result.patch.id == "patch-9"
    assert result.file_paths == ["a.yaml", "b.yaml"]
    assert result.already_managed_count == 3


@pytest.mark.asyncio
async def test_save_all_objects_as_config_async_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"filePaths": ["c.yaml"], "alreadyManagedCount": 0}
        )
    )

    result = await bundle.sdk.libraries.save_all_objects_as_config_async(
        object_type="dashboard"
    )

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"objectType": "dashboard"}
    assert result.file_paths == ["c.yaml"]


def test_save_all_objects_as_config_omitted_field_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.save_all_objects_as_config()

    body = bundle.transport.body_json()
    assert body == {}


def test_save_all_objects_as_config_unicode_object_type(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.save_all_objects_as_config(object_type="ümläut ☃")

    body = bundle.transport.body_json()
    assert body == {"objectType": "ümläut ☃"}


@pytest.mark.parametrize("status_code", [400, 403, 500, 502])
def test_save_all_objects_as_config_error_raises(make_sdk, status_code):
    bundle = make_sdk(lambda req: json_response(status_code, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.save_all_objects_as_config(object_type="playbook")

    assert exc_info.value.status_code == status_code


@pytest.mark.asyncio
async def test_save_all_objects_as_config_async_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.save_all_objects_as_config_async(
            object_type="playbook"
        )

    assert exc_info.value.status_code == 500


def test_save_all_objects_as_config_large_file_paths_list(make_sdk):
    many_paths = [f"folder/file_{i}.yaml" for i in range(2000)]
    bundle = make_sdk(
        lambda req: json_response(200, {"filePaths": many_paths, "alreadyManagedCount": 0})
    )

    result = bundle.sdk.libraries.save_all_objects_as_config(object_type="playbook")

    assert len(result.file_paths) == 2000
    assert result.file_paths[-1] == "folder/file_1999.yaml"


# ---------------------------------------------------------------------------
# validate_config / validate_config_async
# ---------------------------------------------------------------------------


def test_validate_config_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "ok": False,
                "diagnostics": [
                    {"path": "a.yaml", "message": "bad ref", "class": "CALLER_FIXABLE"}
                ],
            },
        )
    )

    result = bundle.sdk.libraries.validate_config(patch_id="patch-abc")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/ValidateConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-abc"}

    assert result.ok is False
    assert result.diagnostics[0].path == "a.yaml"


@pytest.mark.asyncio
async def test_validate_config_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"ok": True}))

    result = await bundle.sdk.libraries.validate_config_async(patch_id="patch-xyz")

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"patchId": "patch-xyz"}
    assert result.ok is True


def test_validate_config_omitted_patch_id_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"ok": True}))

    bundle.sdk.libraries.validate_config()

    body = bundle.transport.body_json()
    assert body == {}


def test_validate_config_empty_string_patch_id_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"ok": True}))

    bundle.sdk.libraries.validate_config(patch_id="")

    body = bundle.transport.body_json()
    # empty string is not None, so it IS included (only None is omitted).
    assert body == {"patchId": ""}


def test_validate_config_unicode_patch_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"ok": True}))

    unicode_id = "patch-日本語-\U0001f680"
    bundle.sdk.libraries.validate_config(patch_id=unicode_id)

    body = bundle.transport.body_json()
    assert body == {"patchId": unicode_id}


@pytest.mark.parametrize("status_code", [400, 404, 422, 500, 503])
def test_validate_config_error_raises_textql_default_error(make_sdk, status_code):
    bundle = make_sdk(lambda req: json_response(status_code, {"message": "invalid"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.validate_config(patch_id="patch-abc")

    assert exc_info.value.status_code == status_code


@pytest.mark.asyncio
async def test_validate_config_async_error_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "invalid"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.validate_config_async(patch_id="patch-abc")

    assert exc_info.value.status_code == 400


def test_validate_config_large_diagnostics_payload(make_sdk):
    diagnostics = [
        {"path": f"file_{i}.yaml", "message": "issue " + ("z" * 200), "class": "CALLER_FIXABLE"}
        for i in range(500)
    ]
    bundle = make_sdk(
        lambda req: json_response(200, {"ok": False, "diagnostics": diagnostics})
    )

    result = bundle.sdk.libraries.validate_config(patch_id="p")

    assert result.ok is False
    assert len(result.diagnostics) == 500
    assert result.diagnostics[0].path == "file_0.yaml"


def test_validate_config_large_patch_id_string(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"ok": True}))

    huge_patch_id = "p-" + ("a" * 20_000)
    bundle.sdk.libraries.validate_config(patch_id=huge_patch_id)

    body = bundle.transport.body_json()
    assert body["patchId"] == huge_patch_id


# ---------------------------------------------------------------------------
# get_config_export_capabilities / get_config_export_capabilities_async
# ---------------------------------------------------------------------------


def test_get_config_export_capabilities_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"objectTypes": ["playbook", "dashboard"], "canCreatePatches": True}
        )
    )

    result = bundle.sdk.libraries.get_config_export_capabilities(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/GetConfigExportCapabilities"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {}

    assert result.object_types == ["playbook", "dashboard"]
    assert result.can_create_patches is True


@pytest.mark.asyncio
async def test_get_config_export_capabilities_async_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"objectTypes": [], "canCreatePatches": False})
    )

    result = await bundle.sdk.libraries.get_config_export_capabilities_async(body={})

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {}
    assert result.can_create_patches is False


@pytest.mark.parametrize("status_code", [400, 401, 500])
def test_get_config_export_capabilities_error_raises(make_sdk, status_code):
    bundle = make_sdk(lambda req: json_response(status_code, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.get_config_export_capabilities(body={})

    assert exc_info.value.status_code == status_code


# ---------------------------------------------------------------------------
# upsert_ana_config / upsert_ana_config_async
# ---------------------------------------------------------------------------


def test_upsert_ana_config_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "config": {
                    "path": "ana/config.yaml",
                    "canWrite": True,
                }
            },
        )
    )

    result = bundle.sdk.libraries.upsert_ana_config(
        path="ana/config.yaml",
        auto_attach=[{"path": "foo", "matchAll": True}],
        commit_message="update config",
        codeowners=[{"pattern": "*.yaml", "ownerMemberIds": ["u1"]}],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/UpsertLibraryAnaConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["path"] == "ana/config.yaml"
    assert body["commitMessage"] == "update config"
    assert body["autoAttach"] == [{"path": "foo", "matchAll": True}]
    assert body["codeowners"] == [{"pattern": "*.yaml", "ownerMemberIds": ["u1"]}]

    assert result.config.path == "ana/config.yaml"
    assert result.config.can_write is True


@pytest.mark.asyncio
async def test_upsert_ana_config_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"path": "p2"}}))

    result = await bundle.sdk.libraries.upsert_ana_config_async(
        path="p2", commit_message="msg"
    )

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"path": "p2", "commitMessage": "msg"}
    assert result.config.path == "p2"


def test_upsert_ana_config_commit_message_omitted_absent(make_sdk):
    """commit_message: OptionalNullable[str] = UNSET -- if not passed, the
    field must be absent from the JSON body entirely (not present as null).
    """
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_ana_config(path="p")

    body = bundle.transport.body_json()
    assert body == {"path": "p"}
    assert "commitMessage" not in body


def test_upsert_ana_config_commit_message_explicit_value_present(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_ana_config(path="p", commit_message="hello world")

    body = bundle.transport.body_json()
    assert body["commitMessage"] == "hello world"


def test_upsert_ana_config_commit_message_explicit_none_is_json_null(make_sdk):
    """Passing commit_message=None explicitly (distinct from omission/UNSET)
    must serialize the field as an explicit JSON null, per the nullable_fields
    + __pydantic_fields_set__ logic in
    textql_rpc_public_patches_upsertlibraryanaconfigrequest.py.
    """
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_ana_config(path="p", commit_message=None)

    body = bundle.transport.body_json()
    assert "commitMessage" in body
    assert body["commitMessage"] is None


def test_upsert_ana_config_unicode_and_empty_string_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_ana_config(
        path="", commit_message="éèê 你好 \U0001f4a5"
    )

    body = bundle.transport.body_json()
    assert body["path"] == ""
    assert body["commitMessage"] == "éèê 你好 \U0001f4a5"


@pytest.mark.parametrize("status_code", [400, 403, 409, 500])
def test_upsert_ana_config_error_raises(make_sdk, status_code):
    bundle = make_sdk(lambda req: json_response(status_code, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.upsert_ana_config(path="p")

    assert exc_info.value.status_code == status_code


@pytest.mark.asyncio
async def test_upsert_ana_config_async_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.upsert_ana_config_async(path="p")

    assert exc_info.value.status_code == 422


def test_upsert_ana_config_large_codeowners_list(make_sdk):
    many_owners = [
        {"pattern": f"pattern_{i}/*", "ownerMemberIds": [f"user_{i}"]}
        for i in range(1000)
    ]
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.upsert_ana_config(path="p", codeowners=many_owners)

    body = bundle.transport.body_json()
    assert len(body["codeowners"]) == 1000
    assert body["codeowners"][-1]["pattern"] == "pattern_999/*"


# ---------------------------------------------------------------------------
# get_ana_config / get_ana_config_async
# ---------------------------------------------------------------------------


def test_get_ana_config_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"config": {"path": "ana/config.yaml"}})
    )

    result = bundle.sdk.libraries.get_ana_config(path="ana/config.yaml")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/GetLibraryAnaConfig"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"path": "ana/config.yaml"}

    assert result.config.path == "ana/config.yaml"


@pytest.mark.asyncio
async def test_get_ana_config_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"config": {"path": "p"}}))

    result = await bundle.sdk.libraries.get_ana_config_async(path="p")

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"path": "p"}
    assert result.config.path == "p"


def test_get_ana_config_omitted_path_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_ana_config()

    body = bundle.transport.body_json()
    assert body == {}


def test_get_ana_config_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.get_ana_config(path="missing")

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# migrate_legacy_context / migrate_legacy_context_async
# ---------------------------------------------------------------------------


def test_migrate_legacy_context_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "createdCount": 2,
                "skippedCount": 1,
                "totalLegacyCount": 3,
                "dryRun": False,
            },
        )
    )

    result = bundle.sdk.libraries.migrate_legacy_context(
        dry_run=False, include_inactive=True
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/MigrateLegacyContextToLibrary"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"dryRun": False, "includeInactive": True}

    assert result.created_count == 2
    assert result.skipped_count == 1
    assert result.dry_run is False


@pytest.mark.asyncio
async def test_migrate_legacy_context_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"dryRun": True}))

    result = await bundle.sdk.libraries.migrate_legacy_context_async(dry_run=True)

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"dryRun": True}
    assert result.dry_run is True


def test_migrate_legacy_context_both_omitted_absent(make_sdk):
    """dry_run and include_inactive are OptionalNullable[bool] = UNSET; if not
    passed, neither key should appear in the serialized JSON body at all.
    """
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.migrate_legacy_context()

    body = bundle.transport.body_json()
    assert body == {}


def test_migrate_legacy_context_explicit_none_serializes_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.migrate_legacy_context(dry_run=None, include_inactive=None)

    body = bundle.transport.body_json()
    assert "dryRun" in body and body["dryRun"] is None
    assert "includeInactive" in body and body["includeInactive"] is None


def test_migrate_legacy_context_one_explicit_one_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.migrate_legacy_context(dry_run=True)

    body = bundle.transport.body_json()
    assert body == {"dryRun": True}
    assert "includeInactive" not in body


def test_migrate_legacy_context_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.migrate_legacy_context(dry_run=True)

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_migrate_legacy_context_async_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.migrate_legacy_context_async(dry_run=True)

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# migrate_ontology / migrate_ontology_async
# ---------------------------------------------------------------------------


def test_migrate_ontology_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "results": [
                    {
                        "ontologyId": 1,
                        "ontologyName": "Sales",
                        "folderPath": "ontologies/sales",
                        "createdCount": 5,
                        "skippedCount": 0,
                        "totalNouns": 5,
                    }
                ],
                "totalCreated": 5,
                "totalSkipped": 0,
                "dryRun": False,
            },
        )
    )

    result = bundle.sdk.libraries.migrate_ontology(ontology_ids=[1, 2, 3], dry_run=False)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/MigrateOntologyToLibrary"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"ontologyIds": [1, 2, 3], "dryRun": False}

    assert result.total_created == 5
    assert result.results[0].ontology_name == "Sales"


@pytest.mark.asyncio
async def test_migrate_ontology_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalCreated": 0, "dryRun": True}))

    result = await bundle.sdk.libraries.migrate_ontology_async(
        ontology_ids=[42], dry_run=True
    )

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"ontologyIds": [42], "dryRun": True}
    assert result.dry_run is True


def test_migrate_ontology_omitted_fields_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.migrate_ontology()

    body = bundle.transport.body_json()
    assert body == {}


def test_migrate_ontology_dry_run_explicit_none_is_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.migrate_ontology(ontology_ids=[1], dry_run=None)

    body = bundle.transport.body_json()
    assert body["ontologyIds"] == [1]
    assert "dryRun" in body
    assert body["dryRun"] is None


def test_migrate_ontology_empty_ontology_ids_list(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.migrate_ontology(ontology_ids=[])

    body = bundle.transport.body_json()
    # empty list is not None, so it's included per the not-optional-omit rule.
    assert body == {"ontologyIds": []}


def test_migrate_ontology_large_ontology_ids_list(make_sdk):
    ids = list(range(10_000))
    bundle = make_sdk(lambda req: json_response(200, {"totalCreated": 0}))

    bundle.sdk.libraries.migrate_ontology(ontology_ids=ids)

    body = bundle.transport.body_json()
    assert len(body["ontologyIds"]) == 10_000
    assert body["ontologyIds"][-1] == 9999


def test_migrate_ontology_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.migrate_ontology(ontology_ids=[1])

    assert exc_info.value.status_code == 403


@pytest.mark.asyncio
async def test_migrate_ontology_async_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.migrate_ontology_async(ontology_ids=[1])

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_ontology_usage_summary / get_ontology_usage_summary_async
# ---------------------------------------------------------------------------


def test_get_ontology_usage_summary_sync_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "totalFiles": 100,
                "pulledFiles": 80,
                "deadFiles": 20,
                "avgHitRate": 0.75,
                "errorFiles": 2,
                "reclaimableTokens": 4096,
            },
        )
    )

    result = bundle.sdk.libraries.get_ontology_usage_summary(
        observation_period=timedelta(days=3, minutes=10)
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{URL_PREFIX}/GetOntologyUsageSummary"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    # timedelta serializes via pydantic's default ISO-8601 duration encoding.
    assert body == {"observationPeriod": "P3DT10M"}

    assert result.total_files == 100
    assert result.dead_files == 20
    assert result.reclaimable_tokens == 4096


@pytest.mark.asyncio
async def test_get_ontology_usage_summary_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalFiles": 5}))

    result = await bundle.sdk.libraries.get_ontology_usage_summary_async(
        observation_period=timedelta(seconds=90)
    )

    req = bundle.transport.last_request
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"observationPeriod": "PT1M30S"}
    assert result.total_files == 5


def test_get_ontology_usage_summary_omitted_period_absent(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.libraries.get_ontology_usage_summary()

    body = bundle.transport.body_json()
    assert body == {}


def test_get_ontology_usage_summary_reclaimable_tokens_as_string(make_sdk):
    """reclaimable_tokens is Union[int, str] per the generated model -- verify
    the string variant unmarshals correctly too.
    """
    bundle = make_sdk(
        lambda req: json_response(200, {"reclaimableTokens": "not-a-number"})
    )

    result = bundle.sdk.libraries.get_ontology_usage_summary()

    assert result.reclaimable_tokens == "not-a-number"


def test_get_ontology_usage_summary_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.libraries.get_ontology_usage_summary()

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_get_ontology_usage_summary_async_error_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.libraries.get_ontology_usage_summary_async()

    assert exc_info.value.status_code == 400
