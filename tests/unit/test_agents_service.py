"""Unit tests for sdk.agents (AgentService) covering all 13 operations."""
from __future__ import annotations

import httpx
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response, text_response
from textql_sdk import errors, utils

PATH_PREFIX = "/textql.rpc.public.agent.AgentService"


# ---------------------------------------------------------------------------
# CreateAgent
# ---------------------------------------------------------------------------


def test_create_sync_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "a1", "name": "foo"}, "chatId": "c1"}))

    result = bundle.sdk.agents.create(
        name="foo",
        prompt="do things",
        slack_dm_user_ids=["u1", "u2"],
        posting_frequency_crons=["0 * * * *"],
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/CreateAgent"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "foo"
    assert body["prompt"] == "do things"
    assert body["slackDmUserIds"] == ["u1", "u2"]
    assert isinstance(body["slackDmUserIds"], list)
    assert body["postingFrequencyCrons"] == ["0 * * * *"]

    assert result.agent.id == "a1"
    assert result.agent.name == "foo"
    assert result.chat_id == "c1"


async def test_create_async_builds_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "a2", "name": "bar"}, "chatId": "c2"}))

    result = await bundle.sdk.agents.create_async(name="bar", channel_ids=["ch1", "ch2"])

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/CreateAgent"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body["name"] == "bar"
    assert body["channelIds"] == ["ch1", "ch2"]

    assert result.agent.id == "a2"
    assert result.chat_id == "c2"


def test_create_optional_nullable_unset_omits_fields(make_sdk):
    """Leaving slack_channel_id/fast_mode/is_stateful/teams_channel_id at their
    UNSET default must omit them from the serialized body entirely."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.create(name="foo")

    body = bundle.transport.body_json()
    assert "slackChannelId" not in body
    assert "fastMode" not in body
    assert "isStateful" not in body
    assert "teamsChannelId" not in body


def test_create_optional_nullable_explicit_none_serializes_null(make_sdk):
    """Explicitly passing None for a Nullable field is tracked in
    __pydantic_fields_set__ so the custom model_serializer includes it as
    JSON null (see serialize_model in
    textql_rpc_public_agent_createagentrequest.py)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.create(name="foo", slack_channel_id=None, fast_mode=None, is_stateful=None)

    body = bundle.transport.body_json()
    assert body["slackChannelId"] is None
    assert body["fastMode"] is None
    assert body["isStateful"] is None


def test_create_optional_nullable_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.create(
        name="foo",
        slack_channel_id="C123",
        fast_mode=True,
        is_stateful=False,
        teams_channel_id="T456",
    )

    body = bundle.transport.body_json()
    assert body["slackChannelId"] == "C123"
    assert body["fastMode"] is True
    assert body["isStateful"] is False
    assert body["teamsChannelId"] == "T456"


def test_create_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "agent not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.create(name="foo")

    assert exc_info.value.status_code == 404
    assert "agent not found" in str(exc_info.value)


async def test_create_async_error_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.create_async(name="foo")

    assert exc_info.value.status_code == 400
    assert "bad request" in str(exc_info.value)


def test_create_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "internal error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.create(name="foo")

    assert exc_info.value.status_code == 500
    assert "internal error" in str(exc_info.value)


async def test_create_async_error_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.create_async(name="foo")

    assert exc_info.value.status_code == 503
    assert "unavailable" in str(exc_info.value)


# ---------------------------------------------------------------------------
# DeleteAgent
# ---------------------------------------------------------------------------


def test_delete_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.delete(agent_id="a1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/DeleteAgent"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"


async def test_delete_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.agents.delete_async(agent_id="a2")

    req = bundle.transport.last_request
    assert req.url.path == f"{PATH_PREFIX}/DeleteAgent"
    body = bundle.transport.body_json()
    assert body["agentId"] == "a2"


def test_delete_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.delete(agent_id="missing")

    assert exc_info.value.status_code == 404
    assert "not found" in str(exc_info.value)


async def test_delete_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.delete_async(agent_id="a1")

    assert exc_info.value.status_code == 502
    assert "bad gateway" in str(exc_info.value)


# ---------------------------------------------------------------------------
# DuplicateAgent
# ---------------------------------------------------------------------------


def test_duplicate_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "dup1", "name": "copy"}}))

    result = bundle.sdk.agents.duplicate(agent_id="a1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/DuplicateAgent"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"
    assert result.agent.id == "dup1"
    assert result.agent.name == "copy"


async def test_duplicate_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "dup2", "name": "copy2"}}))

    result = await bundle.sdk.agents.duplicate_async(agent_id="a2")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/DuplicateAgent"
    assert result.agent.id == "dup2"


def test_duplicate_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.duplicate(agent_id="a1")

    assert exc_info.value.status_code == 403
    assert "forbidden" in str(exc_info.value)


async def test_duplicate_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.duplicate_async(agent_id="a1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# GetAgent
# ---------------------------------------------------------------------------


def test_get_agent_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "a1", "name": "n", "isActive": True}}))

    result = bundle.sdk.agents.get_agent(agent_id="a1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/GetAgent"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"
    assert result.agent.id == "a1"
    assert result.agent.is_active is True


async def test_get_agent_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "a9"}}))

    result = await bundle.sdk.agents.get_agent_async(agent_id="a9")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/GetAgent"
    assert result.agent.id == "a9"


def test_get_agent_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no agent"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.get_agent(agent_id="does-not-exist")

    assert exc_info.value.status_code == 404
    assert "no agent" in str(exc_info.value)


async def test_get_agent_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.get_agent_async(agent_id="a1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# GetAgentRun
# ---------------------------------------------------------------------------


def test_get_run_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"run": {"id": "r1", "agentId": "a1", "status": "success"}}))

    result = bundle.sdk.agents.get_run(run_id="r1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/GetAgentRun"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["runId"] == "r1"
    assert result.run.id == "r1"
    assert result.run.status == "success"


async def test_get_run_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"run": {"id": "r2"}}))

    result = await bundle.sdk.agents.get_run_async(run_id="r2")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/GetAgentRun"
    assert result.run.id == "r2"


def test_get_run_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no run"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.get_run(run_id="missing")

    assert exc_info.value.status_code == 404


async def test_get_run_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(504, {"message": "timeout upstream"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.get_run_async(run_id="r1")

    assert exc_info.value.status_code == 504


# ---------------------------------------------------------------------------
# ListAgentRuns
# ---------------------------------------------------------------------------


def test_list_runs_sync_with_optional_nullable_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"runs": [{"id": "r1"}, {"id": "r2"}]}))

    result = bundle.sdk.agents.list_runs(
        agent_id="a1",
        trigger_source="webhook",
        status="success",
        limit=10,
        offset=5,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListAgentRuns"
    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"
    assert body["triggerSource"] == "webhook"
    assert body["status"] == "success"
    assert body["limit"] == 10
    assert body["offset"] == 5
    assert len(result.runs) == 2
    assert result.runs[0].id == "r1"


async def test_list_runs_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"runs": []}))

    result = await bundle.sdk.agents.list_runs_async(agent_id="a1")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ListAgentRuns"
    assert result.runs == []


def test_list_runs_optional_nullable_unset_omits_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.list_runs(agent_id="a1")

    body = bundle.transport.body_json()
    assert "triggerSource" not in body
    assert "status" not in body


def test_list_runs_optional_nullable_explicit_none(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.list_runs(agent_id="a1", trigger_source=None, status=None)

    body = bundle.transport.body_json()
    assert body["triggerSource"] is None
    assert body["status"] is None


def test_list_runs_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad filter"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.list_runs(agent_id="a1")

    assert exc_info.value.status_code == 400


async def test_list_runs_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.list_runs_async(agent_id="a1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ListAgents
# ---------------------------------------------------------------------------


def test_list_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agents": [{"id": "a1"}, {"id": "a2"}]}))

    result = bundle.sdk.agents.list(include_inactive=True, include_all_org=False, days=7)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ListAgents"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body["includeInactive"] is True
    assert body["includeAllOrg"] is False
    assert body["days"] == 7
    assert len(result.agents) == 2


async def test_list_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agents": []}))

    result = await bundle.sdk.agents.list_async()

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ListAgents"
    assert result.agents == []


def test_list_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.list()

    assert exc_info.value.status_code == 401
    assert "unauthorized" in str(exc_info.value)


async def test_list_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.list_async()

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# ResetAgentAvatar
# ---------------------------------------------------------------------------


def test_reset_agent_avatar_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"profileImageUrl": "https://example.com/a.png"}))

    result = bundle.sdk.agents.reset_agent_avatar(agent_id="a1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/ResetAgentAvatar"
    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"
    assert result.profile_image_url == "https://example.com/a.png"


async def test_reset_agent_avatar_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"profileImageUrl": "u"}))

    result = await bundle.sdk.agents.reset_agent_avatar_async(agent_id="a1")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/ResetAgentAvatar"
    assert result.profile_image_url == "u"


def test_reset_agent_avatar_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no agent"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.reset_agent_avatar(agent_id="missing")

    assert exc_info.value.status_code == 404


async def test_reset_agent_avatar_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.reset_agent_avatar_async(agent_id="a1")

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# TriggerAgent
# ---------------------------------------------------------------------------


def test_trigger_agent_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "c1"}))

    result = bundle.sdk.agents.trigger_agent(agent_id="a1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/TriggerAgent"
    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"
    assert result.chat_id == "c1"


async def test_trigger_agent_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"chatId": "c2"}))

    result = await bundle.sdk.agents.trigger_agent_async(agent_id="a2")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/TriggerAgent"
    assert result.chat_id == "c2"


def test_trigger_agent_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(409, {"message": "already running"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.trigger_agent(agent_id="a1")

    assert exc_info.value.status_code == 409
    assert "already running" in str(exc_info.value)


async def test_trigger_agent_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.trigger_agent_async(agent_id="a1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# UpdateAgent
# ---------------------------------------------------------------------------


def test_update_sync_full_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "a1", "name": "new-name"}, "chatId": "c1"}))

    result = bundle.sdk.agents.update(
        agent_id="a1",
        name="new-name",
        is_active=True,
        email_recipient_member_ids=["m1", "m2"],
        update_email_recipients=True,
        channel_ids=["c1", "c2"],
        update_channel_ids=False,
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/UpdateAgent"
    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"
    assert body["name"] == "new-name"
    assert body["isActive"] is True
    assert body["emailRecipientMemberIds"] == ["m1", "m2"]
    assert body["updateEmailRecipients"] is True
    assert body["channelIds"] == ["c1", "c2"]
    assert body["updateChannelIds"] is False
    assert result.agent.name == "new-name"


async def test_update_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"agent": {"id": "a1"}}))

    result = await bundle.sdk.agents.update_async(agent_id="a1", name="renamed")

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/UpdateAgent"
    assert result.agent.id == "a1"


def test_update_optional_nullable_unset_omits_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.update(agent_id="a1")

    body = bundle.transport.body_json()
    assert "slackChannelId" not in body
    assert "fastMode" not in body
    assert "isStateful" not in body
    assert "teamsChannelId" not in body
    assert "updateEmailRecipients" not in body
    assert "updateChannelIds" not in body


def test_update_optional_nullable_explicit_none(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.update(
        agent_id="a1",
        slack_channel_id=None,
        fast_mode=None,
        is_stateful=None,
        teams_channel_id=None,
        update_email_recipients=None,
        update_channel_ids=None,
    )

    body = bundle.transport.body_json()
    assert body["slackChannelId"] is None
    assert body["fastMode"] is None
    assert body["isStateful"] is None
    assert body["teamsChannelId"] is None
    assert body["updateEmailRecipients"] is None
    assert body["updateChannelIds"] is None


def test_update_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "no agent"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.update(agent_id="missing")

    assert exc_info.value.status_code == 404


async def test_update_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.update_async(agent_id="a1")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# UploadAgentAvatar
#
# NB: image_data/file_name are plain Optional[str] fields (see
# src/textql_sdk/models/textql_rpc_public_agent_uploadagentavatarrequest.py)
# and the operation is serialized with media type "json" (agents.py calls
# utils.serialize_request_body(request.body, False, False, "json", ...)), so
# this is a plain JSON request, NOT a multipart/form-data upload -- despite
# the "upload" name. image_data is presumably base64-encoded image bytes as a
# string, passed as a regular JSON string field.
# ---------------------------------------------------------------------------


def test_upload_agent_avatar_sync_is_plain_json_not_multipart(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"profileImageUrl": "https://example.com/x.png"}))

    result = bundle.sdk.agents.upload_agent_avatar(
        agent_id="a1", image_data="ZmFrZS1pbWFnZS1ieXRlcw==", file_name="avatar.png"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/UploadAgentAvatar"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    # Confirm this is JSON, not multipart.
    assert req.headers["content-type"].startswith("application/json")

    body = bundle.transport.body_json()
    assert body["agentId"] == "a1"
    assert body["imageData"] == "ZmFrZS1pbWFnZS1ieXRlcw=="
    assert body["fileName"] == "avatar.png"
    assert result.profile_image_url == "https://example.com/x.png"


async def test_upload_agent_avatar_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"profileImageUrl": "u"}))

    result = await bundle.sdk.agents.upload_agent_avatar_async(
        agent_id="a1", image_data="data", file_name="f.png"
    )

    assert bundle.transport.last_request.url.path == f"{PATH_PREFIX}/UploadAgentAvatar"
    assert result.profile_image_url == "u"


def test_upload_agent_avatar_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(413, {"message": "file too large"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.agents.upload_agent_avatar(agent_id="a1", image_data="d", file_name="f.png")

    assert exc_info.value.status_code == 413
    assert "file too large" in str(exc_info.value)


async def test_upload_agent_avatar_async_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "err"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.agents.upload_agent_avatar_async(agent_id="a1", image_data="d", file_name="f.png")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Cross-cutting behavior: retries, server_url override, http_headers,
# timeout_ms.
# ---------------------------------------------------------------------------


def test_retries_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"agent": {"id": "a1"}}),
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

    result = bundle.sdk.agents.create(name="foo", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result.agent.id == "a1"


async def test_retries_async_on_500_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"agent": {"id": "a2"}}),
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

    result = await bundle.sdk.agents.create_async(name="foo", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert result.agent.id == "a2"


def test_server_url_override_changes_host(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    override_url = "https://overridden.invalid"
    bundle.sdk.agents.create(name="foo", server_url=override_url)

    req = bundle.transport.last_request
    assert req.url.scheme == "https"
    assert req.url.host == "overridden.invalid"


async def test_server_url_override_changes_host_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    override_url = "https://overridden-async.invalid"
    await bundle.sdk.agents.create_async(name="foo", server_url=override_url)

    req = bundle.transport.last_request
    assert req.url.host == "overridden-async.invalid"


def test_http_headers_passthrough(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.create(name="foo", http_headers={"X-Custom-Header": "hello"})

    req = bundle.transport.last_request
    assert req.headers["x-custom-header"] == "hello"


async def test_http_headers_passthrough_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.agents.create_async(name="foo", http_headers={"X-Custom-Header": "world"})

    req = bundle.transport.last_request
    assert req.headers["x-custom-header"] == "world"


def test_timeout_ms_override_reflected_on_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.agents.create(name="foo", timeout_ms=1234)

    req = bundle.transport.last_request
    timeout_ext = req.extensions.get("timeout")
    assert timeout_ext is not None
    # httpx converts the float-seconds timeout into a dict of connect/read/etc
    # keys; 1234ms == 1.234s.
    assert timeout_ext.get("read") == pytest.approx(1.234)


async def test_timeout_ms_override_reflected_on_request_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.agents.create_async(name="foo", timeout_ms=2000)

    req = bundle.transport.last_request
    timeout_ext = req.extensions.get("timeout")
    assert timeout_ext is not None
    assert timeout_ext.get("read") == pytest.approx(2.0)
