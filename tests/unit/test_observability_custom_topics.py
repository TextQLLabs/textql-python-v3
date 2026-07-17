"""Unit tests for Observability custom-topic operations."""
from datetime import datetime, timezone

import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, utils

OBS_PATH = "/textql.rpc.public.observe.ObservabilityService"


# ---------------------------------------------------------------------------
# activate_custom_topic / activate_custom_topic_async
# ---------------------------------------------------------------------------


def test_activate_custom_topic_basic_request_and_response(make_sdk):
    # TextqlRPCPublicObserveTopicLifecycleResponse is an empty response model
    # (no fields) -- see
    # models/textql_rpc_public_observe_topiclifecycleresponse.py. Any extra
    # keys in the JSON payload are simply ignored by unmarshaling.
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-1", "status": "active"}))

    result = bundle.sdk.observability.activate_custom_topic(topic_id="topic-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/ActivateCustomTopic"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1"}
    assert result is not None


@pytest.mark.asyncio
async def test_activate_custom_topic_async_basic_request_and_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-2", "status": "active"}))

    result = await bundle.sdk.observability.activate_custom_topic_async(topic_id="topic-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/ActivateCustomTopic"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-2"}
    assert result is not None


def test_activate_custom_topic_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.activate_custom_topic(topic_id="missing")

    assert exc_info.value.status_code == 404


def test_activate_custom_topic_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.activate_custom_topic(topic_id="x")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# backfill_custom_topic / backfill_custom_topic_async
# ---------------------------------------------------------------------------


def test_backfill_custom_topic_basic_request_and_response(make_sdk):
    # TextqlRPCPublicObserveBackfillCustomTopicResponse is also an empty
    # response model -- see
    # models/textql_rpc_public_observe_backfillcustomtopicresponse.py.
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-1", "backfillStatus": "running"}))

    result = bundle.sdk.observability.backfill_custom_topic(topic_id="topic-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/BackfillCustomTopic"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1"}
    assert result is not None


def test_backfill_custom_topic_with_dates_serializes_rfc3339_z(make_sdk):
    """start_date/end_date are datetime fields; verify the exact wire format
    produced by pydantic's mode="json" dump: ISO 8601 with a trailing 'Z'
    (see utils/values.py:_val_to_string and marshal_json, which use
    model_dump(mode="json") under the hood via serialize_request_body)."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    start = datetime(2024, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
    end = datetime(2024, 1, 31, 23, 59, 59, tzinfo=timezone.utc)

    bundle.sdk.observability.backfill_custom_topic(
        topic_id="topic-9", start_date=start, end_date=end
    )

    body = bundle.transport.body_json()
    assert body["startDate"] == "2024-01-01T00:00:00Z"
    assert body["endDate"] == "2024-01-31T23:59:59Z"


def test_backfill_custom_topic_with_microseconds(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    start = datetime(2024, 6, 15, 10, 30, 0, 123456, tzinfo=timezone.utc)
    bundle.sdk.observability.backfill_custom_topic(topic_id="topic-9", start_date=start)

    body = bundle.transport.body_json()
    assert body["startDate"] == "2024-06-15T10:30:00.123456Z"


@pytest.mark.asyncio
async def test_backfill_custom_topic_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-2"}))

    result = await bundle.sdk.observability.backfill_custom_topic_async(topic_id="topic-2")

    req = bundle.transport.last_request
    assert req.url.path == f"{OBS_PATH}/BackfillCustomTopic"
    assert result is not None


def test_backfill_custom_topic_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.backfill_custom_topic(topic_id="x")

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# create_custom_topic / create_custom_topic_async
# ---------------------------------------------------------------------------


def test_create_custom_topic_basic_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200, {"topic": {"id": "topic-new", "name": "Billing Complaints"}}
        )
    )

    result = bundle.sdk.observability.create_custom_topic(
        name="Billing Complaints",
        user_prompt="Threads about billing issues",
        covers="billing, invoices, refunds",
        excludes="general questions",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/CreateCustomTopic"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "name": "Billing Complaints",
        "userPrompt": "Threads about billing issues",
        "covers": "billing, invoices, refunds",
        "excludes": "general questions",
    }
    assert result.topic.id == "topic-new"
    assert result.topic.name == "Billing Complaints"


@pytest.mark.asyncio
async def test_create_custom_topic_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topic": {"id": "topic-async"}}))

    result = await bundle.sdk.observability.create_custom_topic_async(name="Async Topic")

    req = bundle.transport.last_request
    assert req.url.path == f"{OBS_PATH}/CreateCustomTopic"
    body = bundle.transport.body_json()
    assert body == {"name": "Async Topic"}
    assert result.topic.id == "topic-async"


def test_create_custom_topic_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.create_custom_topic(name="Bad")

    assert exc_info.value.status_code == 422


def test_create_custom_topic_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.create_custom_topic(name="Bad")

    assert exc_info.value.status_code == 502


# ---------------------------------------------------------------------------
# deactivate_custom_topic / deactivate_custom_topic_async
# ---------------------------------------------------------------------------


def test_deactivate_custom_topic_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-1", "status": "inactive"}))

    result = bundle.sdk.observability.deactivate_custom_topic(topic_id="topic-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/DeactivateCustomTopic"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1"}
    assert result is not None


@pytest.mark.asyncio
async def test_deactivate_custom_topic_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-2", "status": "inactive"}))

    result = await bundle.sdk.observability.deactivate_custom_topic_async(topic_id="topic-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/DeactivateCustomTopic"
    assert result is not None


def test_deactivate_custom_topic_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.deactivate_custom_topic(topic_id="x")

    assert exc_info.value.status_code == 403


# ---------------------------------------------------------------------------
# delete_custom_topic / delete_custom_topic_async
# ---------------------------------------------------------------------------


def test_delete_custom_topic_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-1", "status": "deleted"}))

    result = bundle.sdk.observability.delete_custom_topic(topic_id="topic-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/DeleteCustomTopic"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1"}
    assert result is not None


@pytest.mark.asyncio
async def test_delete_custom_topic_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topicId": "topic-2"}))

    result = await bundle.sdk.observability.delete_custom_topic_async(topic_id="topic-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/DeleteCustomTopic"
    assert result is not None


def test_delete_custom_topic_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.delete_custom_topic(topic_id="x")

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# get_custom_topic / get_custom_topic_async
# ---------------------------------------------------------------------------


def test_get_custom_topic_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topic": {"id": "topic-1", "name": "Foo"}}))

    result = bundle.sdk.observability.get_custom_topic(topic_id="topic-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetCustomTopic"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1"}
    assert result.topic.name == "Foo"


def test_get_custom_topic_with_trend_window(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topic": {"id": "topic-1"}}))

    start = datetime(2024, 2, 1, tzinfo=timezone.utc)
    end = datetime(2024, 2, 29, tzinfo=timezone.utc)
    bundle.sdk.observability.get_custom_topic(
        topic_id="topic-1", trend_start=start, trend_end=end
    )

    body = bundle.transport.body_json()
    assert body["trendStart"] == "2024-02-01T00:00:00Z"
    assert body["trendEnd"] == "2024-02-29T00:00:00Z"


@pytest.mark.asyncio
async def test_get_custom_topic_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topic": {"id": "topic-2"}}))

    result = await bundle.sdk.observability.get_custom_topic_async(topic_id="topic-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetCustomTopic"
    assert result.topic.id == "topic-2"


def test_get_custom_topic_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_custom_topic(topic_id="missing")

    assert exc_info.value.status_code == 404


# ---------------------------------------------------------------------------
# get_custom_topic_people / get_custom_topic_people_async
# ---------------------------------------------------------------------------


def test_get_custom_topic_people_basic(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"people": [{"memberId": "m-1", "threadCount": 3}]})
    )

    result = bundle.sdk.observability.get_custom_topic_people(topic_id="topic-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetCustomTopicPeople"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1"}
    assert result.people[0].member_id == "m-1"


@pytest.mark.asyncio
async def test_get_custom_topic_people_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"people": []}))

    result = await bundle.sdk.observability.get_custom_topic_people_async(topic_id="topic-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetCustomTopicPeople"
    assert result.people == []


def test_get_custom_topic_people_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_custom_topic_people(topic_id="x")

    assert exc_info.value.status_code == 400


# ---------------------------------------------------------------------------
# get_custom_topic_threads / get_custom_topic_threads_async
# ---------------------------------------------------------------------------


def test_get_custom_topic_threads_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"threads": [], "nextPageToken": ""}))

    result = bundle.sdk.observability.get_custom_topic_threads(topic_id="topic-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/GetCustomTopicThreads"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1"}
    assert result.threads == []


def test_get_custom_topic_threads_all_kwargs(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"threads": []}))

    bundle.sdk.observability.get_custom_topic_threads(
        topic_id="topic-1",
        verdict="tagged",
        page_token="tok-1",
        page_size=25,
        member_id="m-1",
    )

    body = bundle.transport.body_json()
    assert body == {
        "topicId": "topic-1",
        "verdict": "tagged",
        "pageToken": "tok-1",
        "pageSize": 25,
        "memberId": "m-1",
    }


@pytest.mark.asyncio
async def test_get_custom_topic_threads_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"threads": []}))

    result = await bundle.sdk.observability.get_custom_topic_threads_async(topic_id="topic-2")

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/GetCustomTopicThreads"
    assert result.threads == []


def test_get_custom_topic_threads_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.get_custom_topic_threads(topic_id="x")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# list_custom_topics / list_custom_topics_async
# ---------------------------------------------------------------------------


def test_list_custom_topics_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topics": [{"id": "t1"}, {"id": "t2"}]}))

    result = bundle.sdk.observability.list_custom_topics()

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/ListCustomTopics"
    body = bundle.transport.body_json()
    assert body == {}
    assert len(result.topics) == 2


def test_list_custom_topics_with_trend_window(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topics": []}))

    start = datetime(2024, 3, 1, 12, 0, 0, tzinfo=timezone.utc)
    end = datetime(2024, 3, 31, 12, 0, 0, tzinfo=timezone.utc)
    bundle.sdk.observability.list_custom_topics(trend_start=start, trend_end=end)

    body = bundle.transport.body_json()
    assert body["trendStart"] == "2024-03-01T12:00:00Z"
    assert body["trendEnd"] == "2024-03-31T12:00:00Z"


@pytest.mark.asyncio
async def test_list_custom_topics_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topics": []}))

    result = await bundle.sdk.observability.list_custom_topics_async()

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/ListCustomTopics"
    assert result.topics == []


def test_list_custom_topics_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(401, {"message": "unauthorized"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.list_custom_topics()

    assert exc_info.value.status_code == 401


# ---------------------------------------------------------------------------
# update_custom_topic / update_custom_topic_async
# ---------------------------------------------------------------------------


def test_update_custom_topic_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topic": {"id": "topic-1", "name": "New Name"}}))

    result = bundle.sdk.observability.update_custom_topic(topic_id="topic-1", name="New Name")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{OBS_PATH}/UpdateCustomTopic"
    body = bundle.transport.body_json()
    assert body == {"topicId": "topic-1", "name": "New Name"}
    assert result.topic.name == "New Name"


def test_update_custom_topic_covers_excludes_unset_are_omitted(make_sdk):
    """covers/excludes are OptionalNullable[str]; when left UNSET (the
    default) they must not appear in the serialized JSON body at all --
    per TextqlRPCPublicObserveUpdateCustomTopicRequest.serialize_model."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.update_custom_topic(topic_id="topic-1", name="X")

    body = bundle.transport.body_json()
    assert "covers" not in body
    assert "excludes" not in body


def test_update_custom_topic_covers_excludes_explicit_value(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.update_custom_topic(
        topic_id="topic-1", name="X", covers="new covers text", excludes="new excludes text"
    )

    body = bundle.transport.body_json()
    assert body["covers"] == "new covers text"
    assert body["excludes"] == "new excludes text"


def test_update_custom_topic_covers_excludes_explicit_none_serializes_null(make_sdk):
    """Explicitly passing None (as opposed to leaving UNSET) for a
    Nullable field must serialize to JSON null."""
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.observability.update_custom_topic(
        topic_id="topic-1", name="X", covers=None, excludes=None
    )

    body = bundle.transport.body_json()
    assert body["covers"] is None
    assert body["excludes"] is None


@pytest.mark.asyncio
async def test_update_custom_topic_async_basic(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topic": {"id": "topic-2"}}))

    result = await bundle.sdk.observability.update_custom_topic_async(
        topic_id="topic-2", name="Y"
    )

    assert bundle.transport.last_request.url.path == f"{OBS_PATH}/UpdateCustomTopic"
    assert result.topic.id == "topic-2"


def test_update_custom_topic_error_4xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.update_custom_topic(topic_id="x", name="y")

    assert exc_info.value.status_code == 400


def test_update_custom_topic_error_5xx(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.observability.update_custom_topic(topic_id="x", name="y")

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# Retry, server_url, and http_headers overrides (representative subset)
# ---------------------------------------------------------------------------


def test_activate_custom_topic_retries_backoff_eventually_succeeds(make_sdk, sequence_handler):
    handler = sequence_handler(
        [
            json_response(500, {"message": "temporary failure"}),
            json_response(200, {"topicId": "topic-retry", "status": "active"}),
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

    result = bundle.sdk.observability.activate_custom_topic(
        topic_id="topic-retry", retries=retries
    )

    assert len(bundle.transport.requests) == 2
    assert result is not None


@pytest.mark.asyncio
async def test_create_custom_topic_async_retries_backoff_eventually_succeeds(
    make_sdk, sequence_handler
):
    handler = sequence_handler(
        [
            json_response(503, {"message": "temporary failure"}),
            json_response(200, {"topic": {"id": "topic-retry-async"}}),
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

    result = await bundle.sdk.observability.create_custom_topic_async(
        name="Retry Topic", retries=retries
    )

    assert len(bundle.transport.requests) == 2
    assert result.topic.id == "topic-retry-async"


def test_get_custom_topic_server_url_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topic": {"id": "topic-1"}}))

    override_url = "https://override.invalid"
    bundle.sdk.observability.get_custom_topic(topic_id="topic-1", server_url=override_url)

    req = bundle.transport.last_request
    assert str(req.url).startswith(override_url)


def test_list_custom_topics_http_headers_override(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {"topics": []}))

    bundle.sdk.observability.list_custom_topics(
        http_headers={"X-Custom-Header": "custom-value"}
    )

    req = bundle.transport.last_request
    assert req.headers["X-Custom-Header"] == "custom-value"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
