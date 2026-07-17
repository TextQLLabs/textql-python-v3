"""Unit tests for Playbooks CRUD operations: create_playbook, get, update, delete, duplicate, deactivate, deploy, fetch."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PB_PATH = "/textql.rpc.public.playbook.PlaybookService"


# --------------------------------------------------------------------------
# create_playbook
# --------------------------------------------------------------------------


def test_create_playbook_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb1"}}))

    result = bundle.sdk.playbooks.create_playbook(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/CreatePlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert result.playbook.id == "pb1"


@pytest.mark.asyncio
async def test_create_playbook_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb1"}}))

    result = await bundle.sdk.playbooks.create_playbook_async(body={})

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/CreatePlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert result.playbook.id == "pb1"


def test_create_playbook_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.create_playbook(body={})

    assert exc_info.value.status_code == 422


def test_create_playbook_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.create_playbook(body={})

    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_create_playbook_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "nope"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.create_playbook_async(body={})

    assert exc_info.value.status_code == 404


def test_create_playbook_unicode_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"playbook": {"id": "pb1", "name": "日本語 名前 🎉"}})
    )

    result = bundle.sdk.playbooks.create_playbook(body={})
    assert result.playbook.name == "日本語 名前 🎉"


# --------------------------------------------------------------------------
# get (GetPlaybooks - list)
# --------------------------------------------------------------------------


def test_get_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"playbooks": [{"id": "pb1"}], "totalCount": 1})
    )

    result = bundle.sdk.playbooks.get(
        member_only=True,
        limit=10,
        offset=0,
        search_term="foo",
        creator_member_id="mem-1",
        subscribed_first=True,
        only_subscribed=False,
        shared_with_me=True,
        include_shared_drafts=False,
        statuses=["STATUS_ACTIVE"],
        creator_member_ids=["mem-1", "mem-2"],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetPlaybooks"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["memberOnly"] is True
    assert body["limit"] == 10
    assert body["offset"] == 0
    assert body["searchTerm"] == "foo"
    assert body["creatorMemberId"] == "mem-1"
    assert body["subscribedFirst"] is True
    assert body["onlySubscribed"] is False
    assert body["sharedWithMe"] is True
    assert body["includeSharedDrafts"] is False
    assert body["statuses"] == ["STATUS_ACTIVE"]
    assert body["creatorMemberIds"] == ["mem-1", "mem-2"]
    assert len(result.playbooks) == 1
    assert result.playbooks[0].id == "pb1"
    assert result.total_count == 1


@pytest.mark.asyncio
async def test_get_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbooks": []}))

    result = await bundle.sdk.playbooks.get_async()

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetPlaybooks"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert result.playbooks == []


def test_get_omits_unset_nullable_fields(make_sdk):
    """search_term/creator_member_id/subscribed_first/only_subscribed/
    shared_with_me/include_shared_drafts are all OptionalNullable(UNSET) by
    default and should be omitted entirely."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.get()

    body = bundle.transport.body_json()
    assert body == {}
    for key in (
        "searchTerm",
        "creatorMemberId",
        "subscribedFirst",
        "onlySubscribed",
        "sharedWithMe",
        "includeSharedDrafts",
    ):
        assert key not in body


def test_get_explicit_null_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.get(search_term=None, only_subscribed=None)

    body = bundle.transport.body_json()
    assert body["searchTerm"] is None
    assert body["onlySubscribed"] is None


def test_get_empty_list_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbooks": []}))

    bundle.sdk.playbooks.get(statuses=[], creator_member_ids=[])

    body = bundle.transport.body_json()
    assert body["statuses"] == []
    assert body["creatorMemberIds"] == []


def test_get_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get()
    assert exc_info.value.status_code == 400


def test_get_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get()
    assert exc_info.value.status_code == 503


@pytest.mark.asyncio
async def test_get_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.get_async()
    assert exc_info.value.status_code == 403


# --------------------------------------------------------------------------
# update
# --------------------------------------------------------------------------


def test_update_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb1"}}))

    result = bundle.sdk.playbooks.update(
        playbook_id="pb1",
        name="New Name",
        prompt="do the thing",
        status="STATUS_ACTIVE",
        trigger_type="TRIGGER_TYPE_CRON",
        cron_string="0 0 * * *",
        dataset_ids={"items": ["ds1", "ds2"]},
        reference_report_id="report-1",
        email_addresses={"items": ["a@example.com"]},
        slack_channel_id="C123",
        max_concurrent_templates=5,
        auto_optimize_concurrency=True,
        chat_is_public=False,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/UpdatePlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["playbookId"] == "pb1"
    assert body["name"] == "New Name"
    assert body["prompt"] == "do the thing"
    assert body["status"] == "STATUS_ACTIVE"
    assert body["triggerType"] == "TRIGGER_TYPE_CRON"
    assert body["cronString"] == "0 0 * * *"
    assert body["datasetIds"] == {"items": ["ds1", "ds2"]}
    assert body["referenceReportId"] == "report-1"
    assert body["emailAddresses"] == {"items": ["a@example.com"]}
    assert body["slackChannelId"] == "C123"
    assert body["maxConcurrentTemplates"] == 5
    assert body["autoOptimizeConcurrency"] is True
    assert body["chatIsPublic"] is False
    assert result.playbook.id == "pb1"


@pytest.mark.asyncio
async def test_update_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb1"}}))

    result = await bundle.sdk.playbooks.update_async(playbook_id="pb1", name="Async Name")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/UpdatePlaybook"
    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb1", "name": "Async Name"}
    assert result.playbook.id == "pb1"


def test_update_omits_unset_nullable_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {}}))

    bundle.sdk.playbooks.update(playbook_id="pb1")

    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb1"}
    for key in (
        "name",
        "prompt",
        "cronString",
        "connectorId",
        "referenceReportId",
        "slackChannelId",
        "templateHeaderId",
        "maxConcurrentTemplates",
        "autoOptimizeConcurrency",
        "chatIsPublic",
        "recipientEmailColumn",
        "teamsChannelId",
    ):
        assert key not in body


def test_update_explicit_null_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {}}))

    bundle.sdk.playbooks.update(
        playbook_id="pb1",
        name=None,
        cron_string=None,
        max_concurrent_templates=None,
        chat_is_public=None,
    )

    body = bundle.transport.body_json()
    assert body["name"] is None
    assert body["cronString"] is None
    assert body["maxConcurrentTemplates"] is None
    assert body["chatIsPublic"] is None


def test_update_empty_string_lists(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {}}))

    bundle.sdk.playbooks.update(
        playbook_id="pb1",
        dataset_ids={"items": []},
        email_addresses={"items": []},
    )

    body = bundle.transport.body_json()
    assert body["datasetIds"] == {"items": []}
    assert body["emailAddresses"] == {"items": []}


def test_update_unicode_name(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb1"}}))

    bundle.sdk.playbooks.update(playbook_id="pb1", name="プレイブック 🚀")

    body = bundle.transport.body_json()
    assert body["name"] == "プレイブック 🚀"


def test_update_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.update(playbook_id="pb1")
    assert exc_info.value.status_code == 422


def test_update_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.update(playbook_id="pb1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_update_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.update_async(playbook_id="pb1")
    assert exc_info.value.status_code == 502


def test_update_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"playbook": {"id": "pb1"}}),
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

    result = bundle.sdk.playbooks.update(playbook_id="pb1", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result.playbook.id == "pb1"


# --------------------------------------------------------------------------
# delete
# --------------------------------------------------------------------------


def test_delete_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.delete(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/DeletePlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}


@pytest.mark.asyncio
async def test_delete_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.playbooks.delete_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/DeletePlaybook"
    assert bundle.transport.body_json() == {"playbookId": "pb1"}


def test_delete_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.delete(playbook_id="pb1")
    assert exc_info.value.status_code == 404


def test_delete_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.delete(playbook_id="pb1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# duplicate
# --------------------------------------------------------------------------


def test_duplicate_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb2"}}))

    result = bundle.sdk.playbooks.duplicate(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/DuplicatePlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.playbook.id == "pb2"


@pytest.mark.asyncio
async def test_duplicate_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb2"}}))

    result = await bundle.sdk.playbooks.duplicate_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/DuplicatePlaybook"
    assert result.playbook.id == "pb2"


def test_duplicate_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "conflict"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.duplicate(playbook_id="pb1")
    assert exc_info.value.status_code == 409


def test_duplicate_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.duplicate(playbook_id="pb1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_duplicate_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.duplicate_async(playbook_id="pb1")
    assert exc_info.value.status_code == 400


def test_duplicate_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(502, {"message": "transient"}),
            json_response(200, {"playbook": {"id": "pb2"}}),
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

    result = bundle.sdk.playbooks.duplicate(playbook_id="pb1", retries=retry_config)
    assert len(bundle.transport.requests) == 2
    assert result.playbook.id == "pb2"


def test_duplicate_unicode_name_in_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"playbook": {"id": "pb2", "name": "コピー 📋"}})
    )
    result = bundle.sdk.playbooks.duplicate(playbook_id="pb1")
    assert result.playbook.name == "コピー 📋"


# --------------------------------------------------------------------------
# deactivate
# --------------------------------------------------------------------------


def test_deactivate_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.deactivate(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/DeactivatePlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}


@pytest.mark.asyncio
async def test_deactivate_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.playbooks.deactivate_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/DeactivatePlaybook"
    assert bundle.transport.body_json() == {"playbookId": "pb1"}


def test_deactivate_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.deactivate(playbook_id="pb1")
    assert exc_info.value.status_code == 400


def test_deactivate_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.deactivate(playbook_id="pb1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# deploy
# --------------------------------------------------------------------------


def test_deploy_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"playbookId": "pb1", "deployedAt": "2024-01-01T00:00:00Z"}
        )
    )

    result = bundle.sdk.playbooks.deploy(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/DeployPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.playbook_id == "pb1"
    assert result.deployed_at is not None


@pytest.mark.asyncio
async def test_deploy_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbookId": "pb1"}))

    result = await bundle.sdk.playbooks.deploy_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/DeployPlaybook"
    assert result.playbook_id == "pb1"


def test_deploy_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid state"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.deploy(playbook_id="pb1")
    assert exc_info.value.status_code == 422


def test_deploy_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.deploy(playbook_id="pb1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_deploy_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.deploy_async(playbook_id="pb1")
    assert exc_info.value.status_code == 503


def test_deploy_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(429, {"message": "rate limited"}),
            json_response(200, {"playbookId": "pb1"}),
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

    result = bundle.sdk.playbooks.deploy(playbook_id="pb1", retries=retry_config)
    assert len(bundle.transport.requests) == 2
    assert result.playbook_id == "pb1"


# --------------------------------------------------------------------------
# fetch (GetPlaybook)
# --------------------------------------------------------------------------


def test_fetch_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"playbook": {"id": "pb1"}, "reports": []})
    )

    result = bundle.sdk.playbooks.fetch(playbook_id="pb1", limit=10, offset=5)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {
        "playbookId": "pb1",
        "limit": 10,
        "offset": 5,
    }
    assert result.playbook.id == "pb1"


@pytest.mark.asyncio
async def test_fetch_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"playbook": {"id": "pb1"}}))

    result = await bundle.sdk.playbooks.fetch_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetPlaybook"
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.playbook.id == "pb1"


def test_fetch_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.fetch(playbook_id="does-not-exist")
    assert exc_info.value.status_code == 404


def test_fetch_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.fetch(playbook_id="pb1")
    assert exc_info.value.status_code == 500


@pytest.mark.asyncio
async def test_fetch_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.playbooks.fetch_async(playbook_id="pb1")
    assert exc_info.value.status_code == 401


# --------------------------------------------------------------------------
# demo_playbook
# --------------------------------------------------------------------------


def test_demo_playbook_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.demo_playbook(
        chat_id="chat-1",
        person_name="Ada Lovelace",
        job_title="Engineer",
        target_email="ada@example.com",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/DemoPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {
        "chatId": "chat-1",
        "personName": "Ada Lovelace",
        "jobTitle": "Engineer",
        "targetEmail": "ada@example.com",
    }


@pytest.mark.asyncio
async def test_demo_playbook_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.playbooks.demo_playbook_async(person_name="Grace Hopper")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/DemoPlaybook"
    assert bundle.transport.body_json() == {"personName": "Grace Hopper"}


def test_demo_playbook_unicode(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.demo_playbook(person_name="山田太郎 🎌")

    body = bundle.transport.body_json()
    assert body["personName"] == "山田太郎 🎌"


def test_demo_playbook_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.demo_playbook()
    assert exc_info.value.status_code == 400


def test_demo_playbook_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.demo_playbook()
    assert exc_info.value.status_code == 500
