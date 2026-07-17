"""Unit tests for Observability stats/reporting operations."""
from datetime import datetime, timezone

import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, utils

OBS_PATH = "/textql.rpc.public.observe.ObservabilityService"


# ---------------------------------------------------------------------------
# get_access_method_stats / get_access_method_stats_async
# ---------------------------------------------------------------------------


def test_get_access_method_stats_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"methods": [{"method": "api", "total": 5}]}))

    result = bundle.sdk.observability.get_access_method_stats(days=7)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetAccessMethodStats"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"days": 7}
    assert result.methods[0].total == 5


def test_get_access_method_stats_with_dates(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    start = datetime(2024, 5, 1, tzinfo=timezone.utc)
    end = datetime(2024, 5, 31, tzinfo=timezone.utc)
    bundle.sdk.observability.get_access_method_stats(days=30, start_date=start, end_date=end)

    body = bundle.transport.body_json()
    assert body["startDate"] == "2024-05-01T00:00:00Z"
    assert body["endDate"] == "2024-05-31T00:00:00Z"


@pytest.mark.asyncio
async def test_get_access_method_stats_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"methods": []}))

    result = await bundle.sdk.observability.get_access_method_stats_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetAccessMethodStats"
    assert result.methods == []


def test_get_access_method_stats_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_access_method_stats(days=1)

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# get_active_people_stats / get_active_people_stats_async
# ---------------------------------------------------------------------------


def test_get_active_people_stats_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"activeMemberCount": 42, "totalMemberCount": 100}))

    result = bundle.sdk.observability.get_active_people_stats(days=14)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetActivePeopleStats"
    body = bundle.transport.body_json()
    assert body == {"days": 14}
    assert result.active_member_count == 42
    assert result.total_member_count == 100


@pytest.mark.asyncio
async def test_get_active_people_stats_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"activeMemberCount": 10}))

    result = await bundle.sdk.observability.get_active_people_stats_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetActivePeopleStats"
    assert result.active_member_count == 10


def test_get_active_people_stats_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_active_people_stats(days=1)

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_active_people_trend / get_active_people_trend_async
# ---------------------------------------------------------------------------


def test_get_active_people_trend_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"points": []}))

    result = bundle.sdk.observability.get_active_people_trend(days=30)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetActivePeopleTrend"
    body = bundle.transport.body_json()
    assert body == {"days": 30}
    assert result.points == []


def test_get_active_people_trend_with_dates(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"points": []}))

    start = datetime(2024, 1, 1, tzinfo=timezone.utc)
    end = datetime(2024, 1, 31, tzinfo=timezone.utc)
    bundle.sdk.observability.get_active_people_trend(days=30, start_date=start, end_date=end)

    body = bundle.transport.body_json()
    assert body["startDate"] == "2024-01-01T00:00:00Z"
    assert body["endDate"] == "2024-01-31T00:00:00Z"


@pytest.mark.asyncio
async def test_get_active_people_trend_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"points": []}))

    result = await bundle.sdk.observability.get_active_people_trend_async(days=7)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetActivePeopleTrend"
    assert result.points == []


def test_get_active_people_trend_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_active_people_trend(days=1)

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# get_billing_stats / get_billing_stats_async
# ---------------------------------------------------------------------------


def test_get_billing_stats_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalFeedAcu": 12.5}))

    result = bundle.sdk.observability.get_billing_stats(days=30)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetBillingStats"
    body = bundle.transport.body_json()
    assert body == {"days": 30}
    assert result.total_feed_acu == 12.5


@pytest.mark.asyncio
async def test_get_billing_stats_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"totalAppAcu": 1.0}))

    result = await bundle.sdk.observability.get_billing_stats_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetBillingStats"
    assert result.total_app_acu == 1.0


def test_get_billing_stats_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_billing_stats(days=1)

    assert exc_info.value.status_code == 401


def test_get_billing_stats_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_billing_stats(days=1)

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# get_chat_source_stats / get_chat_source_stats_async
# ---------------------------------------------------------------------------


def test_get_chat_source_stats_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"orgBySource": []}))

    result = bundle.sdk.observability.get_chat_source_stats(days=7)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetChatSourceStats"
    body = bundle.transport.body_json()
    assert body == {"days": 7}
    assert result.org_by_source == []


def test_get_chat_source_stats_member_id_unset_is_omitted(make_sdk):
    """member_id is OptionalNullable[str]; when left UNSET (the default) it
    must not appear in the serialized JSON body at all."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.get_chat_source_stats(days=7)

    body = bundle.transport.body_json()
    assert "memberId" not in body


def test_get_chat_source_stats_member_id_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.get_chat_source_stats(days=7, member_id="member-42")

    body = bundle.transport.body_json()
    assert body["memberId"] == "member-42"


def test_get_chat_source_stats_member_id_explicit_none_serializes_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.get_chat_source_stats(days=7, member_id=None)

    body = bundle.transport.body_json()
    assert body["memberId"] is None


def test_get_chat_source_stats_with_dates(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    start = datetime(2024, 4, 1, tzinfo=timezone.utc)
    end = datetime(2024, 4, 30, tzinfo=timezone.utc)
    bundle.sdk.observability.get_chat_source_stats(days=30, start_date=start, end_date=end)

    body = bundle.transport.body_json()
    assert body["startDate"] == "2024-04-01T00:00:00Z"
    assert body["endDate"] == "2024-04-30T00:00:00Z"


@pytest.mark.asyncio
async def test_get_chat_source_stats_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"orgBySource": []}))

    result = await bundle.sdk.observability.get_chat_source_stats_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetChatSourceStats"
    assert result.org_by_source == []


def test_get_chat_source_stats_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_chat_source_stats(days=1)

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# get_chat_topics / get_chat_topics_async
# ---------------------------------------------------------------------------


def test_get_chat_topics_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicsByChat": {}}))

    result = bundle.sdk.observability.get_chat_topics(chat_ids=["chat-1", "chat-2"])

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetChatTopics"
    body = bundle.transport.body_json()
    assert body == {"chatIds": ["chat-1", "chat-2"]}
    assert result.topics_by_chat == {}


@pytest.mark.asyncio
async def test_get_chat_topics_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicsByChat": {}}))

    result = await bundle.sdk.observability.get_chat_topics_async(chat_ids=["chat-9"])

    req = bundle.transport.last_request
    assert req.url.path == f"{OBS_PATH}/GetChatTopics"
    body = bundle.transport.body_json()
    assert body == {"chatIds": ["chat-9"]}
    assert result.topics_by_chat == {}


def test_get_chat_topics_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_chat_topics(chat_ids=["x"])

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# get_engagement_spectrum / get_engagement_spectrum_async
# ---------------------------------------------------------------------------


def test_get_engagement_spectrum_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"tiers": []}))

    result = bundle.sdk.observability.get_engagement_spectrum(days=7)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetEngagementSpectrum"
    body = bundle.transport.body_json()
    assert body == {"days": 7}
    assert result.tiers == []


@pytest.mark.asyncio
async def test_get_engagement_spectrum_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"tiers": []}))

    result = await bundle.sdk.observability.get_engagement_spectrum_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetEngagementSpectrum"
    assert result.tiers == []


def test_get_engagement_spectrum_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_engagement_spectrum(days=1)

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# get_member_activity / get_member_activity_async
# ---------------------------------------------------------------------------


def test_get_member_activity_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))

    result = bundle.sdk.observability.get_member_activity(days=7)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetMemberActivity"
    body = bundle.transport.body_json()
    assert body == {"days": 7}
    assert result.members == []


@pytest.mark.asyncio
async def test_get_member_activity_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))

    result = await bundle.sdk.observability.get_member_activity_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetMemberActivity"
    assert result.members == []


def test_get_member_activity_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_member_activity(days=1)

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# get_observability_stats / get_observability_stats_async
# ---------------------------------------------------------------------------


def test_get_observability_stats_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"summary": {}}))

    result = bundle.sdk.observability.get_observability_stats(days=7)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetObservabilityStats"
    body = bundle.transport.body_json()
    assert body == {"days": 7}
    assert result.summary is not None


@pytest.mark.asyncio
async def test_get_observability_stats_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"summary": {}}))

    result = await bundle.sdk.observability.get_observability_stats_async(days=1)

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetObservabilityStats"
    assert result.summary is not None


def test_get_observability_stats_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_observability_stats(days=1)

    assert exc_info.value.status_code == 400


def test_get_observability_stats_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_observability_stats(days=1)

    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# Retry, server_url, and http_headers overrides (representative subset)
# ---------------------------------------------------------------------------


def test_get_billing_stats_retries_backoff_eventually_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"totalFeedAcu": 99.0}),
        ]
    )
    bundle = make_sdk(handler)

    retries = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=True,
    )

    result = bundle.sdk.observability.get_billing_stats(days=30, retries=retries)

    assert len(bundle.transport.requests) == 2
    assert result.total_feed_acu == 99.0


@pytest.mark.asyncio
async def test_get_active_people_trend_async_retries_backoff_eventually_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(429, {"message": "rate limited"}),
            json_response(200, {"points": []}),
        ]
    )
    bundle = make_sdk(handler)

    retries = utils.RetryConfig(
        strategy="backoff",
        backoff=utils.BackoffStrategy(
            initial_interval=1,
            max_interval=5,
            exponent=1.0,
            max_elapsed_time=5000,
        ),
        retry_connection_errors=True,
    )

    result = await bundle.sdk.observability.get_active_people_trend_async(
        days=7, retries=retries
    )

    assert len(bundle.transport.requests) == 2
    assert result.points == []


def test_get_observability_stats_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"summary": {}}))

    override_url = "https://override.invalid"
    bundle.sdk.observability.get_observability_stats(days=1, server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_get_member_activity_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"members": []}))

    bundle.sdk.observability.get_member_activity(
        days=1, http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
