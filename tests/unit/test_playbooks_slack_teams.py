"""Unit tests for Playbooks Slack/Teams context operations:"""
from __future__ import annotations

import pytest

from textql_sdk import errors, models

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PB_PATH = "/textql.rpc.public.playbook.PlaybookService"


# --------------------------------------------------------------------------
# set_slack_channel_context_playbook
# --------------------------------------------------------------------------


def test_set_slack_channel_context_playbook_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.set_slack_channel_context_playbook(
        playbook_id="pb1", slack_channel_id="C123"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/SetSlackChannelContextPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1", "slackChannelId": "C123"}
    assert result.success is True


@pytest.mark.asyncio
async def test_set_slack_channel_context_playbook_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.playbooks.set_slack_channel_context_playbook_async(
        playbook_id="pb1", slack_channel_id="C123"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/SetSlackChannelContextPlaybook"
    assert result.success is True


def test_set_slack_channel_context_playbook_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.set_slack_channel_context_playbook(
            playbook_id="pb1", slack_channel_id="C123"
        )
    assert exc_info.value.status_code == 404


def test_set_slack_channel_context_playbook_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.set_slack_channel_context_playbook(
            playbook_id="pb1", slack_channel_id="C123"
        )
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# unset_slack_channel_context_playbook
# --------------------------------------------------------------------------


def test_unset_slack_channel_context_playbook_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.unset_slack_channel_context_playbook(
        slack_channel_id="C123"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/UnsetSlackChannelContextPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"slackChannelId": "C123"}
    assert result.success is True


@pytest.mark.asyncio
async def test_unset_slack_channel_context_playbook_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = await bundle.sdk.playbooks.unset_slack_channel_context_playbook_async(
        slack_channel_id="C123"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/UnsetSlackChannelContextPlaybook"
    assert result.success is False


def test_unset_slack_channel_context_playbook_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.unset_slack_channel_context_playbook(slack_channel_id="C123")
    assert exc_info.value.status_code == 404


def test_unset_slack_channel_context_playbook_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.unset_slack_channel_context_playbook(slack_channel_id="C123")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_slack_channel_context_playbooks (-> ListAllSlackChannelContextPlaybooks)
# --------------------------------------------------------------------------


def test_list_slack_channel_context_playbooks_sync_sends_correct_request(make_sdk):
    payload = {
        "mappings": [
            {"playbookId": "pb1", "slackChannelId": "C123"},
            {"playbookId": "pb2", "slackChannelId": "C456"},
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.list_slack_channel_context_playbooks(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/ListAllSlackChannelContextPlaybooks"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert len(result.mappings) == 2
    assert result.mappings[0].playbook_id == "pb1"
    assert result.mappings[0].slack_channel_id == "C123"


@pytest.mark.asyncio
async def test_list_slack_channel_context_playbooks_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"mappings": []}))

    result = await bundle.sdk.playbooks.list_slack_channel_context_playbooks_async(body={})

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/ListAllSlackChannelContextPlaybooks"
    assert result.mappings == []


def test_list_slack_channel_context_playbooks_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_slack_channel_context_playbooks(body={})
    assert exc_info.value.status_code == 400


def test_list_slack_channel_context_playbooks_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_slack_channel_context_playbooks(body={})
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_slack_channels_for_context
# --------------------------------------------------------------------------


def test_list_slack_channels_for_context_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"slackChannelIds": ["C123", "C456"]})
    )

    result = bundle.sdk.playbooks.list_slack_channels_for_context(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/ListSlackChannelsForContextPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.slack_channel_ids == ["C123", "C456"]


@pytest.mark.asyncio
async def test_list_slack_channels_for_context_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"slackChannelIds": []}))

    result = await bundle.sdk.playbooks.list_slack_channels_for_context_async(
        playbook_id="pb1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/ListSlackChannelsForContextPlaybook"
    assert result.slack_channel_ids == []


def test_list_slack_channels_for_context_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_slack_channels_for_context(playbook_id="missing")
    assert exc_info.value.status_code == 404


def test_list_slack_channels_for_context_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_slack_channels_for_context(playbook_id="pb1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# preview_slack_report
# --------------------------------------------------------------------------


def test_preview_slack_report_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.preview_slack_report(
        playbook_id="pb1",
        cell={"subject": "Weekly", "blocks": [{"text": {"content": "hi"}}]},
        chat_id="chat-1",
        slack_channel_id="C123",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/PreviewSlackReport"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["playbookId"] == "pb1"
    assert body["cell"]["subject"] == "Weekly"
    assert body["cell"]["blocks"] == [{"text": {"content": "hi"}}]
    assert body["chatId"] == "chat-1"
    assert body["slackChannelId"] == "C123"


@pytest.mark.asyncio
async def test_preview_slack_report_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.playbooks.preview_slack_report_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/PreviewSlackReport"
    assert bundle.transport.body_json() == {"playbookId": "pb1"}


def test_preview_slack_report_no_cell_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.playbooks.preview_slack_report(playbook_id="pb1")

    body = bundle.transport.body_json()
    assert "cell" not in body


def test_preview_slack_report_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.preview_slack_report(playbook_id="pb1")
    assert exc_info.value.status_code == 400


def test_preview_slack_report_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.preview_slack_report(playbook_id="pb1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# set_teams_channel_context
# --------------------------------------------------------------------------


def test_set_teams_channel_context_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.set_teams_channel_context(
        playbook_id="pb1", teams_channel_id="T123"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/SetTeamsChannelContextPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1", "teamsChannelId": "T123"}
    assert result.success is True


@pytest.mark.asyncio
async def test_set_teams_channel_context_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.playbooks.set_teams_channel_context_async(
        playbook_id="pb1", teams_channel_id="T123"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/SetTeamsChannelContextPlaybook"
    assert result.success is True


def test_set_teams_channel_context_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.set_teams_channel_context(
            playbook_id="pb1", teams_channel_id="T123"
        )
    assert exc_info.value.status_code == 404


def test_set_teams_channel_context_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.set_teams_channel_context(
            playbook_id="pb1", teams_channel_id="T123"
        )
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# unset_teams_channel_context
# --------------------------------------------------------------------------


def test_unset_teams_channel_context_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.unset_teams_channel_context(teams_channel_id="T123")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/UnsetTeamsChannelContextPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"teamsChannelId": "T123"}
    assert result.success is True


@pytest.mark.asyncio
async def test_unset_teams_channel_context_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = await bundle.sdk.playbooks.unset_teams_channel_context_async(
        teams_channel_id="T123"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/UnsetTeamsChannelContextPlaybook"
    assert result.success is False


def test_unset_teams_channel_context_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.unset_teams_channel_context(teams_channel_id="T123")
    assert exc_info.value.status_code == 404


def test_unset_teams_channel_context_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.unset_teams_channel_context(teams_channel_id="T123")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_teams_channels_for_context_playbook
# --------------------------------------------------------------------------


def test_list_teams_channels_for_context_playbook_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"teamsChannelIds": ["T123", "T456"]})
    )

    result = bundle.sdk.playbooks.list_teams_channels_for_context_playbook(
        playbook_id="pb1"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/ListTeamsChannelsForContextPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.teams_channel_ids == ["T123", "T456"]


@pytest.mark.asyncio
async def test_list_teams_channels_for_context_playbook_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"teamsChannelIds": []}))

    result = await bundle.sdk.playbooks.list_teams_channels_for_context_playbook_async(
        playbook_id="pb1"
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/ListTeamsChannelsForContextPlaybook"
    assert result.teams_channel_ids == []


def test_list_teams_channels_for_context_playbook_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_teams_channels_for_context_playbook(playbook_id="missing")
    assert exc_info.value.status_code == 404


def test_list_teams_channels_for_context_playbook_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_teams_channels_for_context_playbook(playbook_id="pb1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# list_all_teams_channel_context_playbooks
# --------------------------------------------------------------------------


def test_list_all_teams_channel_context_playbooks_sync_sends_correct_request(make_sdk):
    payload = {
        "mappings": [
            {"playbookId": "pb1", "teamsChannelId": "T123"},
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.list_all_teams_channel_context_playbooks(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/ListAllTeamsChannelContextPlaybooks"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert result.mappings[0].playbook_id == "pb1"
    assert result.mappings[0].teams_channel_id == "T123"


@pytest.mark.asyncio
async def test_list_all_teams_channel_context_playbooks_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"mappings": []}))

    result = await bundle.sdk.playbooks.list_all_teams_channel_context_playbooks_async(
        body={}
    )

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/ListAllTeamsChannelContextPlaybooks"
    assert result.mappings == []


def test_list_all_teams_channel_context_playbooks_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_all_teams_channel_context_playbooks(body={})
    assert exc_info.value.status_code == 400


def test_list_all_teams_channel_context_playbooks_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.list_all_teams_channel_context_playbooks(body={})
    assert exc_info.value.status_code == 500
