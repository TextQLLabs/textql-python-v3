"""Unit tests for miscellaneous Playbooks operations: subscriptions, members, active-subscribed count."""
from __future__ import annotations

import pytest

from textql_sdk import errors, utils

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response

PB_PATH = "/textql.rpc.public.playbook.PlaybookService"


# --------------------------------------------------------------------------
# get_active_subscribed_count
# --------------------------------------------------------------------------


def test_get_active_subscribed_count_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"count": 42}))

    result = bundle.sdk.playbooks.get_active_subscribed_count(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetActiveSubscribedPlaybooksCount"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert result.count == 42


@pytest.mark.asyncio
async def test_get_active_subscribed_count_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"count": 7}))

    result = await bundle.sdk.playbooks.get_active_subscribed_count_async(body={})

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetActiveSubscribedPlaybooksCount"
    assert result.count == 7


def test_get_active_subscribed_count_zero(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"count": 0}))
    result = bundle.sdk.playbooks.get_active_subscribed_count(body={})
    assert result.count == 0


def test_get_active_subscribed_count_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_active_subscribed_count(body={})
    assert exc_info.value.status_code == 400


def test_get_active_subscribed_count_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_active_subscribed_count(body={})
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# get_members_with
# --------------------------------------------------------------------------


def test_get_members_with_sync_sends_correct_request(make_sdk):
    payload = {
        "members": [
            {"memberId": "mem-1", "memberEmail": "a@example.com", "memberName": "Alice"},
            {"memberId": "mem-2"},
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.playbooks.get_members_with(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/GetMembersWithPlaybooks"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {}
    assert len(result.members) == 2
    assert result.members[0].member_id == "mem-1"
    assert result.members[0].member_email == "a@example.com"
    assert result.members[0].member_name == "Alice"


@pytest.mark.asyncio
async def test_get_members_with_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))

    result = await bundle.sdk.playbooks.get_members_with_async(body={})

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/GetMembersWithPlaybooks"
    assert result.members == []


def test_get_members_with_unicode_names(make_sdk):
    payload = {"members": [{"memberId": "m1", "memberName": "田中太郎 👤"}]}
    bundle = make_sdk(lambda req: json_response(200, payload))
    result = bundle.sdk.playbooks.get_members_with(body={})
    assert result.members[0].member_name == "田中太郎 👤"


def test_get_members_with_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_members_with(body={})
    assert exc_info.value.status_code == 403


def test_get_members_with_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.get_members_with(body={})
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# subscribe
# --------------------------------------------------------------------------


def test_subscribe_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.subscribe(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/SubscribeToPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_subscribe_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.playbooks.subscribe_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/SubscribeToPlaybook"
    assert result.success is True


def test_subscribe_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.subscribe(playbook_id="missing")
    assert exc_info.value.status_code == 404


def test_subscribe_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.subscribe(playbook_id="pb1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# unsubscribe
# --------------------------------------------------------------------------


def test_unsubscribe_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.unsubscribe(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{PB_PATH}/UnsubscribeFromPlaybook"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    assert bundle.transport.body_json() == {"playbookId": "pb1"}
    assert result.success is True


@pytest.mark.asyncio
async def test_unsubscribe_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": False}))

    result = await bundle.sdk.playbooks.unsubscribe_async(playbook_id="pb1")

    req = bundle.transport.last_request
    assert req.url.path == f"{PB_PATH}/UnsubscribeFromPlaybook"
    assert result.success is False


def test_unsubscribe_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.unsubscribe(playbook_id="missing")
    assert exc_info.value.status_code == 404


def test_unsubscribe_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))
    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.playbooks.unsubscribe(playbook_id="pb1")
    assert exc_info.value.status_code == 500


# --------------------------------------------------------------------------
# retries / server_url / http_headers / timeout_ms overrides
# (cross-cutting SDK behavior, exercised on a representative sample of ops)
# --------------------------------------------------------------------------


def _tiny_retry_config():
    return utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1, max_interval=5, exponent=1.0, max_elapsed_time=5000
        ),
        retry_connection_errors=False,
    )


def test_subscribe_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "transient"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)

    result = bundle.sdk.playbooks.subscribe(playbook_id="pb1", retries=_tiny_retry_config())

    assert len(bundle.transport.requests) == 2
    assert result.success is True


@pytest.mark.asyncio
async def test_unsubscribe_async_retries_backoff_then_success(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(502, {"message": "transient"}),
            json_response(200, {"success": True}),
        ]
    )
    bundle = make_sdk(handler)

    result = await bundle.sdk.playbooks.unsubscribe_async(
        playbook_id="pb1", retries=_tiny_retry_config()
    )

    assert len(bundle.transport.requests) == 2
    assert result.success is True


def test_get_members_with_retries_exhausted_raises(make_sdk, sequence_handler):
    """max_elapsed_time is exceeded before a successful response arrives --
    the last erroring response is surfaced and get_members_with() raises."""
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
        bundle.sdk.playbooks.get_members_with(body={}, retries=retry_config)

    assert exc_info.value.status_code == 500


def test_subscribe_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    override_url = "https://override.invalid"

    bundle.sdk.playbooks.subscribe(playbook_id="pb1", server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)
    assert req.url.path == f"{PB_PATH}/SubscribeToPlaybook"


@pytest.mark.asyncio
async def test_unsubscribe_async_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))
    override_url = "https://override-async.invalid"

    await bundle.sdk.playbooks.unsubscribe_async(playbook_id="pb1", server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_get_active_subscribed_count_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"count": 1}))

    bundle.sdk.playbooks.get_active_subscribed_count(
        body={}, http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_get_members_with_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))

    bundle.sdk.playbooks.get_members_with(
        body={}, http_headers={"X-Trace-Id": "trace-123"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Trace-Id"] == "trace-123"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY


def test_subscribe_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = bundle.sdk.playbooks.subscribe(playbook_id="pb1", timeout_ms=2500)

    assert result.success is True


@pytest.mark.asyncio
async def test_unsubscribe_async_timeout_ms_override_does_not_break_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"success": True}))

    result = await bundle.sdk.playbooks.unsubscribe_async(playbook_id="pb1", timeout_ms=2500)

    assert result.success is True
