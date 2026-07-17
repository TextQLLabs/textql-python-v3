"""Unit tests for the Slack service (sdk.slack)."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils
from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PATH_PREFIX = "/textql.rpc.public.slack.SlackService"


def assert_common(bundle, path_suffix: str, api_key: str = FAKE_API_KEY):
    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PATH_PREFIX}/{path_suffix}"
    assert req.headers[AUTH_HEADER_NAME] == api_key


# ---------------------------------------------------------------------------
# create_uuid
# ---------------------------------------------------------------------------


def test_create_uuid_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"uuid": "uuid-1"}))

    resp = bundle.sdk.slack.create_uuid(body={})

    assert_common(bundle, "CreateSlackUuid")
    assert resp.uuid == "uuid-1"


async def test_create_uuid_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"uuid": "uuid-2"}))
    resp = await bundle.sdk.slack.create_uuid_async(body={})
    assert_common(bundle, "CreateSlackUuid")
    assert resp.uuid == "uuid-2"


def test_create_uuid_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.create_uuid(body={})
    assert exc_info.value.status_code == 404


async def test_create_uuid_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.create_uuid_async(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# delete_installation
# ---------------------------------------------------------------------------


def test_delete_installation_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    resp = bundle.sdk.slack.delete_installation(team_id="team-1")

    assert_common(bundle, "DeleteInstallation")
    assert bundle.transport.body_json()["teamId"] == "team-1"
    assert resp is not None


async def test_delete_installation_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    resp = await bundle.sdk.slack.delete_installation_async(team_id="team-2")
    assert_common(bundle, "DeleteInstallation")
    assert resp is not None


def test_delete_installation_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.delete_installation(team_id="missing")
    assert exc_info.value.status_code == 404


async def test_delete_installation_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.delete_installation_async(team_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_current_user
# ---------------------------------------------------------------------------


def test_get_current_user_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"user": {"id": "user-1", "name": "Alice"}})
    )

    resp = bundle.sdk.slack.get_current_user(body={})

    assert_common(bundle, "GetCurrentUser")
    assert resp.user.id == "user-1"


async def test_get_current_user_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"user": {"id": "user-2"}}))
    resp = await bundle.sdk.slack.get_current_user_async(body={})
    assert_common(bundle, "GetCurrentUser")
    assert resp.user.id == "user-2"


def test_get_current_user_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.get_current_user(body={})
    assert exc_info.value.status_code == 404


async def test_get_current_user_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.get_current_user_async(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# handle_o_auth_callback -- code/state placed in the JSON request BODY (not
# query params), per TextqlRPCPublicSlackHandleSlackOAuthCallbackRequest usage
# in src/textql_sdk/slack.py.
# ---------------------------------------------------------------------------


def test_handle_o_auth_callback_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"success": True, "teamId": "team-1"})
    )

    resp = bundle.sdk.slack.handle_o_auth_callback(
        code="fake-oauth-code-123", state="fake-oauth-state-abc"
    )

    assert_common(bundle, "HandleSlackOAuthCallback")
    body = bundle.transport.body_json()
    assert body["code"] == "fake-oauth-code-123"
    assert body["state"] == "fake-oauth-state-abc"
    # code/state must NOT be sent as query params
    assert "code" not in bundle.transport.last_request.url.params
    assert "state" not in bundle.transport.last_request.url.params
    assert resp.success is True
    assert resp.team_id == "team-1"


async def test_handle_o_auth_callback_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    resp = await bundle.sdk.slack.handle_o_auth_callback_async(
        code="fake-oauth-code-456", state="fake-oauth-state-def"
    )
    assert_common(bundle, "HandleSlackOAuthCallback")
    body = bundle.transport.body_json()
    assert body["code"] == "fake-oauth-code-456"
    assert body["state"] == "fake-oauth-state-def"
    assert resp.success is True


def test_handle_o_auth_callback_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.handle_o_auth_callback(code="fake-oauth-code", state="fake-state")
    assert exc_info.value.status_code == 404


async def test_handle_o_auth_callback_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.handle_o_auth_callback_async(
            code="fake-oauth-code", state="fake-state"
        )
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_channels
# ---------------------------------------------------------------------------


def test_list_channels_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"channels": [{"id": "chan-1", "name": "general"}]})
    )

    resp = bundle.sdk.slack.list_channels(body={})

    assert_common(bundle, "ListChannels")
    assert len(resp.channels) == 1


async def test_list_channels_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"channels": []}))
    resp = await bundle.sdk.slack.list_channels_async(body={})
    assert_common(bundle, "ListChannels")
    assert resp.channels == []


def test_list_channels_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.list_channels(body={})
    assert exc_info.value.status_code == 404


async def test_list_channels_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.list_channels_async(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_installations
# ---------------------------------------------------------------------------


def test_list_installations_sync(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"installations": [{"teamId": "team-1"}]})
    )

    resp = bundle.sdk.slack.list_installations(body={})

    assert_common(bundle, "ListInstallations")
    assert len(resp.installations) == 1


async def test_list_installations_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"installations": []}))
    resp = await bundle.sdk.slack.list_installations_async(body={})
    assert_common(bundle, "ListInstallations")
    assert resp.installations == []


def test_list_installations_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.list_installations(body={})
    assert exc_info.value.status_code == 404


async def test_list_installations_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.list_installations_async(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_users
# ---------------------------------------------------------------------------


def test_list_users_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"users": [{"id": "user-1"}]}))

    resp = bundle.sdk.slack.list_users(body={})

    assert_common(bundle, "ListUsers")
    assert len(resp.users) == 1


async def test_list_users_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"users": []}))
    resp = await bundle.sdk.slack.list_users_async(body={})
    assert_common(bundle, "ListUsers")
    assert resp.users == []


def test_list_users_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.list_users(body={})
    assert exc_info.value.status_code == 404


async def test_list_users_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.list_users_async(body={})
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# sync_workspace
# ---------------------------------------------------------------------------
# NOTE: SyncWorkspace takes a single `team_id: Optional[str]`, NOT a list of
# workspace ids -- confirmed by reading src/textql_sdk/slack.py's
# `sync_workspace` signature and its
# `TextqlRPCPublicSlackSyncWorkspaceRequest(team_id=team_id)` body construction.


def test_sync_workspace_sync(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"queued": True, "message": "ok"}))

    resp = bundle.sdk.slack.sync_workspace(team_id="team-1")

    assert_common(bundle, "SyncWorkspace")
    assert bundle.transport.body_json()["teamId"] == "team-1"
    assert resp.queued is True
    assert resp.message == "ok"


def test_sync_workspace_unset_team_id_omitted(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    bundle.sdk.slack.sync_workspace()
    body = bundle.transport.body_json()
    assert body is None or "teamId" not in body


async def test_sync_workspace_async(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"queued": False}))
    resp = await bundle.sdk.slack.sync_workspace_async(team_id="team-2")
    assert_common(bundle, "SyncWorkspace")
    assert resp.queued is False


def test_sync_workspace_404_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.slack.sync_workspace(team_id="missing")
    assert exc_info.value.status_code == 404


async def test_sync_workspace_async_500_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.slack.sync_workspace_async(team_id="missing")
    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# retries
# ---------------------------------------------------------------------------


def test_retries_backoff_retries_then_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "server error"}),
            json_response(200, {"queued": True}),
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

    resp = bundle.sdk.slack.sync_workspace(team_id="team-1", retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.queued is True


async def test_retries_backoff_retries_then_succeeds_async(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "server error"}),
            json_response(200, {"uuid": "uuid-1"}),
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

    resp = await bundle.sdk.slack.create_uuid_async(body={}, retries=retry_config)

    assert len(bundle.transport.requests) == 2
    assert resp.uuid == "uuid-1"


# ---------------------------------------------------------------------------
# server_url / http_headers / timeout_ms per-call overrides
# ---------------------------------------------------------------------------


def test_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))
    override_url = "https://override.invalid"

    bundle.sdk.slack.sync_workspace(team_id="team-1", server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.slack.sync_workspace(
        team_id="team-1", http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.slack.sync_workspace(team_id="team-1", timeout_ms=5000)

    assert len(bundle.transport.requests) == 1
