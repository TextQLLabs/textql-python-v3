"""Unit tests for the Chats service (sdk.chats) miscellaneous RPCs."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors, models


BASE_PATH = "/textql.rpc.public.chat.ChatService"


# ---------------------------------------------------------------------------
# check_health
# ---------------------------------------------------------------------------


def test_check_health_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.check_health(model="MODEL_SONNET_4_5", functional=True)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CheckHealth"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"model": "MODEL_SONNET_4_5", "functional": True}


async def test_check_health_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.check_health_async(model="MODEL_HAIKU_3", functional=False)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CheckHealth"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"model": "MODEL_HAIKU_3", "functional": False}


def test_check_health_sync_unmarshals_200_response(make_sdk):
    payload = {
        "llmStatus": "STATUS_HEALTHY",
        "webStatus": "STATUS_MINOR",
        "sandboxStatus": "STATUS_CRITICAL",
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.check_health()

    assert isinstance(result, models.TextqlRPCPublicChatCheckHealthResponse)
    assert result.llm_status == "STATUS_HEALTHY"
    assert result.web_status == "STATUS_MINOR"
    assert result.sandbox_status == "STATUS_CRITICAL"


async def test_check_health_async_unmarshals_200_response(make_sdk):
    payload = {"llmStatus": "STATUS_HEALTHY"}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.check_health_async()

    assert isinstance(result, models.TextqlRPCPublicChatCheckHealthResponse)
    assert result.llm_status == "STATUS_HEALTHY"


def test_check_health_functional_unset_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.check_health()

    body = bundle.transport.body_json()
    assert "functional" not in body
    assert "model" not in body


def test_check_health_functional_explicit_value_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.check_health(functional=True)

    body = bundle.transport.body_json()
    assert body["functional"] is True


def test_check_health_functional_explicit_none_serializes_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.check_health(functional=None)

    body = bundle.transport.body_json()
    assert "functional" in body
    assert body["functional"] is None


def test_check_health_sync_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.check_health()

    assert exc_info.value.status_code == 404


def test_check_health_sync_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "boom"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.check_health()

    assert exc_info.value.status_code == 500


async def test_check_health_async_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.check_health_async()

    assert exc_info.value.status_code == 400


async def test_check_health_async_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "unavailable"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.check_health_async()

    assert exc_info.value.status_code == 503


# ---------------------------------------------------------------------------
# check_permissions
# ---------------------------------------------------------------------------


def test_check_permissions_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.check_permissions(chat_id="chat-123")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CheckChatPermissions"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-123"}


async def test_check_permissions_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.check_permissions_async(chat_id="chat-456")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CheckChatPermissions"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-456"}


def test_check_permissions_chat_id_unset_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.check_permissions()

    body = bundle.transport.body_json()
    assert body == {}


def test_check_permissions_sync_unmarshals_200_response(make_sdk):
    payload = {
        "hasWritePermission": True,
        "hasReadPermission": True,
        "connectorIds": [1, 2, 3],
        "ontologyIds": [9],
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.check_permissions(chat_id="chat-123")

    assert isinstance(result, models.TextqlRPCPublicChatCheckChatPermissionsResponse)
    assert result.has_write_permission is True
    assert result.has_read_permission is True
    assert result.connector_ids == [1, 2, 3]
    assert result.ontology_ids == [9]


async def test_check_permissions_async_unmarshals_200_response(make_sdk):
    payload = {"hasWritePermission": False, "hasReadPermission": True}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.check_permissions_async(chat_id="chat-456")

    assert isinstance(result, models.TextqlRPCPublicChatCheckChatPermissionsResponse)
    assert result.has_write_permission is False
    assert result.has_read_permission is True


# ---------------------------------------------------------------------------
# check_streamlit_health
# ---------------------------------------------------------------------------


def test_check_streamlit_health_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.check_streamlit_health(chat_id="chat-1", cell_id="cell-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CheckStreamlitHealth"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1", "cellId": "cell-1"}


async def test_check_streamlit_health_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.check_streamlit_health_async(
        chat_id="chat-2", cell_id="cell-2"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/CheckStreamlitHealth"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2", "cellId": "cell-2"}


def test_check_streamlit_health_sync_unmarshals_200_response(make_sdk):
    payload = {
        "status": "STREAMLIT_HEALTH_STATUS_HEALTHY",
        "embedUrl": "https://example.invalid/embed",
        "streamlitUrl": "worker-1:8501",
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.check_streamlit_health(chat_id="chat-1", cell_id="cell-1")

    assert isinstance(
        result, models.TextqlRPCPublicChatCheckStreamlitHealthResponse
    )
    assert result.status == "STREAMLIT_HEALTH_STATUS_HEALTHY"
    assert result.embed_url == "https://example.invalid/embed"
    assert result.streamlit_url == "worker-1:8501"


async def test_check_streamlit_health_async_unmarshals_200_response(make_sdk):
    payload = {"status": "STREAMLIT_HEALTH_STATUS_STARTING"}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.check_streamlit_health_async(
        chat_id="chat-2", cell_id="cell-2"
    )

    assert result.status == "STREAMLIT_HEALTH_STATUS_STARTING"


# ---------------------------------------------------------------------------
# get_artifact
# ---------------------------------------------------------------------------


def test_get_artifact_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"streamlit": {"embedUrl": "https://x"}})
    )

    bundle.sdk.chats.get_artifact(artifact_id="artifact-1", chat_id="chat-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetArtifact"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"artifactId": "artifact-1", "chatId": "chat-1"}


async def test_get_artifact_async_sends_correct_request(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(200, {"streamlit": {"embedUrl": "https://x"}})
    )

    await bundle.sdk.chats.get_artifact_async(artifact_id="artifact-2", chat_id="chat-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetArtifact"
    body = bundle.transport.body_json()
    assert body == {"artifactId": "artifact-2", "chatId": "chat-2"}


def test_get_artifact_sync_unmarshals_200_response(make_sdk):
    payload = {
        "streamlit": {"embedUrl": "https://example.invalid/embed"},
        "id": "cell-1",
        "name": "My Artifact",
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_artifact(artifact_id="artifact-1", chat_id="chat-1")

    assert isinstance(result, models.Streamlit)
    assert result.id == "cell-1"
    assert result.name == "My Artifact"
    assert result.streamlit.embed_url == "https://example.invalid/embed"


async def test_get_artifact_async_unmarshals_200_response(make_sdk):
    payload = {"streamlit": {"embedUrl": "https://example.invalid/embed2"}}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_artifact_async(
        artifact_id="artifact-2", chat_id="chat-2"
    )

    assert isinstance(result, models.Streamlit)
    assert result.streamlit.embed_url == "https://example.invalid/embed2"


# ---------------------------------------------------------------------------
# get_artifacts_summary
# ---------------------------------------------------------------------------


def test_get_artifacts_summary_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_artifacts_summary(chat_id="chat-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetChatArtifactsSummary"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1"}


async def test_get_artifacts_summary_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.get_artifacts_summary_async(chat_id="chat-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetChatArtifactsSummary"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2"}


def test_get_artifacts_summary_sync_unmarshals_200_response(make_sdk):
    payload = {"artifacts": [{"id": "a1"}, {"id": "a2"}]}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_artifacts_summary(chat_id="chat-1")

    assert isinstance(
        result, models.TextqlRPCPublicChatGetChatArtifactsSummaryResponse
    )
    assert len(result.artifacts) == 2


async def test_get_artifacts_summary_async_unmarshals_200_response(make_sdk):
    payload = {"artifacts": []}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_artifacts_summary_async(chat_id="chat-2")

    assert result.artifacts == []


# ---------------------------------------------------------------------------
# get_chat_execution_timing
# ---------------------------------------------------------------------------


def test_get_chat_execution_timing_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_chat_execution_timing(chat_id="chat-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetChatExecutionTiming"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1"}


async def test_get_chat_execution_timing_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.get_chat_execution_timing_async(chat_id="chat-2")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetChatExecutionTiming"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2"}


def test_get_chat_execution_timing_sync_unmarshals_200_response(make_sdk):
    payload = {
        "totalExecutionMs": 1234,
        "totalWarehouseMs": "500",
        "totalEgressMs": 10,
        "totalOverheadMs": 5,
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_chat_execution_timing(chat_id="chat-1")

    assert isinstance(
        result, models.TextqlRPCPublicChatGetChatExecutionTimingResponse
    )
    assert result.total_execution_ms == 1234
    assert result.total_warehouse_ms == "500"


async def test_get_chat_execution_timing_async_unmarshals_200_response(make_sdk):
    payload = {"totalExecutionMs": 42}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_chat_execution_timing_async(chat_id="chat-2")

    assert result.total_execution_ms == 42


# ---------------------------------------------------------------------------
# get_completion_parameters
# ---------------------------------------------------------------------------


def test_get_completion_parameters_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_completion_parameters(chat_id="chat-1", cell_id="cell-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetCompletionParameters"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1", "cellId": "cell-1"}


async def test_get_completion_parameters_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.get_completion_parameters_async(
        chat_id="chat-2", cell_id="cell-2"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetCompletionParameters"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2", "cellId": "cell-2"}


def test_get_completion_parameters_sync_unmarshals_200_response(make_sdk):
    payload = {
        "params": {
            "memberId": "member-1",
            "llmModel": "MODEL_SONNET_4_5",
            "llmProvider": "anthropic",
        }
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_completion_parameters(
        chat_id="chat-1", cell_id="cell-1"
    )

    assert isinstance(
        result, models.TextqlRPCPublicChatGetCompletionParametersResponse
    )
    assert result.params.member_id == "member-1"
    assert result.params.llm_model == "MODEL_SONNET_4_5"
    assert result.params.llm_provider == "anthropic"


async def test_get_completion_parameters_async_unmarshals_200_response(make_sdk):
    payload = {"params": {"memberId": "member-2"}}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_completion_parameters_async(
        chat_id="chat-2", cell_id="cell-2"
    )

    assert result.params.member_id == "member-2"


# ---------------------------------------------------------------------------
# get_completion_parameters_batch
# ---------------------------------------------------------------------------


def test_get_completion_parameters_batch_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_completion_parameters_batch(
        chat_id="chat-1", cell_ids=["cell-1", "cell-2"]
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetCompletionParametersBatch"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1", "cellIds": ["cell-1", "cell-2"]}


async def test_get_completion_parameters_batch_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.get_completion_parameters_batch_async(
        chat_id="chat-2", cell_ids=["cell-3"]
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetCompletionParametersBatch"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2", "cellIds": ["cell-3"]}


def test_get_completion_parameters_batch_cell_ids_unset_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_completion_parameters_batch(chat_id="chat-1")

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1"}
    assert "cellIds" not in body


def test_get_completion_parameters_batch_cell_ids_empty_list_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_completion_parameters_batch(chat_id="chat-1", cell_ids=[])

    body = bundle.transport.body_json()
    assert body["cellIds"] == []


def test_get_completion_parameters_batch_cell_ids_one_item(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_completion_parameters_batch(
        chat_id="chat-1", cell_ids=["only-cell"]
    )

    body = bundle.transport.body_json()
    assert body["cellIds"] == ["only-cell"]


def test_get_completion_parameters_batch_cell_ids_multiple_items(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_completion_parameters_batch(
        chat_id="chat-1", cell_ids=["cell-a", "cell-b", "cell-c"]
    )

    body = bundle.transport.body_json()
    assert body["cellIds"] == ["cell-a", "cell-b", "cell-c"]


def test_get_completion_parameters_batch_sync_unmarshals_200_response(make_sdk):
    payload = {
        "paramsByCellId": {
            "cell-1": {"memberId": "member-1", "llmModel": "MODEL_SONNET_4_5"},
            "cell-2": {"memberId": "member-2", "llmModel": "MODEL_HAIKU_3"},
        }
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_completion_parameters_batch(
        chat_id="chat-1", cell_ids=["cell-1", "cell-2"]
    )

    assert isinstance(
        result, models.TextqlRPCPublicChatGetCompletionParametersBatchResponse
    )
    assert set(result.params_by_cell_id.keys()) == {"cell-1", "cell-2"}
    assert result.params_by_cell_id["cell-1"].member_id == "member-1"
    assert result.params_by_cell_id["cell-2"].llm_model == "MODEL_HAIKU_3"


async def test_get_completion_parameters_batch_async_unmarshals_200_response(make_sdk):
    payload = {"paramsByCellId": {}}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_completion_parameters_batch_async(
        chat_id="chat-2", cell_ids=[]
    )

    assert result.params_by_cell_id == {}


# ---------------------------------------------------------------------------
# get_llm_usage
# ---------------------------------------------------------------------------


def test_get_llm_usage_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_llm_usage(chat_id="chat-1", include_costs=True)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetLlmUsage"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1", "includeCosts": True}


async def test_get_llm_usage_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.get_llm_usage_async(chat_id="chat-2", include_costs=False)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetLlmUsage"
    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-2", "includeCosts": False}


def test_get_llm_usage_include_costs_unset_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_llm_usage(chat_id="chat-1")

    body = bundle.transport.body_json()
    assert body == {"chatId": "chat-1"}


def test_get_llm_usage_sync_unmarshals_200_response(make_sdk):
    payload = {
        "usage": [{"model": "MODEL_SONNET_4_5"}],
        "contextWindowUsed": 0.42,
        "estimatedCost": 1.23,
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_llm_usage(chat_id="chat-1", include_costs=True)

    assert isinstance(result, models.TextqlRPCPublicChatGetLlmUsageResponse)
    assert result.context_window_used == 0.42
    assert result.estimated_cost == 1.23
    assert len(result.usage) == 1


async def test_get_llm_usage_async_unmarshals_200_response(make_sdk):
    payload = {"contextWindowUsed": 0.1}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_llm_usage_async(chat_id="chat-2")

    assert result.context_window_used == 0.1


# ---------------------------------------------------------------------------
# get_members_with_chats
# ---------------------------------------------------------------------------


def test_get_members_with_chats_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_members_with_chats(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetMembersWithChats"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {}


async def test_get_members_with_chats_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.get_members_with_chats_async(body={})

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetMembersWithChats"
    body = bundle.transport.body_json()
    assert body == {}


def test_get_members_with_chats_sync_unmarshals_200_response(make_sdk):
    payload = {
        "members": [
            {"memberId": "m1", "memberEmail": "a@example.invalid"},
            {"memberId": "m2", "memberName": "Bob"},
        ]
    }
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_members_with_chats(body={})

    assert isinstance(
        result, models.TextqlRPCPublicChatGetMembersWithChatsResponse
    )
    assert len(result.members) == 2
    assert result.members[0].member_id == "m1"
    assert result.members[0].member_email == "a@example.invalid"
    assert result.members[1].member_name == "Bob"


async def test_get_members_with_chats_async_unmarshals_200_response(make_sdk):
    payload = {"members": []}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_members_with_chats_async(body={})

    assert result.members == []


# ---------------------------------------------------------------------------
# get_playbook_chats
# ---------------------------------------------------------------------------


def test_get_playbook_chats_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_playbook_chats(playbook_id="pb-1", limit=10, skip=0)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetPlaybookChats"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb-1", "limit": 10, "skip": 0}


async def test_get_playbook_chats_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.get_playbook_chats_async(playbook_id="pb-2", limit=5, skip=1)

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/GetPlaybookChats"
    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb-2", "limit": 5, "skip": 1}


def test_get_playbook_chats_limit_and_skip_unset_omit_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_playbook_chats(playbook_id="pb-1")

    body = bundle.transport.body_json()
    assert body == {"playbookId": "pb-1"}
    assert "limit" not in body
    assert "skip" not in body


def test_get_playbook_chats_limit_explicit_value_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_playbook_chats(playbook_id="pb-1", limit=25)

    body = bundle.transport.body_json()
    assert body["limit"] == 25
    assert "skip" not in body


def test_get_playbook_chats_limit_explicit_none_serializes_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_playbook_chats(playbook_id="pb-1", limit=None)

    body = bundle.transport.body_json()
    assert "limit" in body
    assert body["limit"] is None


def test_get_playbook_chats_skip_explicit_none_serializes_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.get_playbook_chats(playbook_id="pb-1", skip=None)

    body = bundle.transport.body_json()
    assert "skip" in body
    assert body["skip"] is None


def test_get_playbook_chats_sync_unmarshals_200_response(make_sdk):
    payload = {"chats": [{"id": "chat-1", "orgId": "org-1"}, {"id": "chat-2"}]}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = bundle.sdk.chats.get_playbook_chats(playbook_id="pb-1")

    assert isinstance(result, models.TextqlRPCPublicChatGetPlaybookChatsResponse)
    assert len(result.chats) == 2
    assert result.chats[0].id == "chat-1"
    assert result.chats[0].org_id == "org-1"


async def test_get_playbook_chats_async_unmarshals_200_response(make_sdk):
    payload = {"chats": []}
    bundle = make_sdk(lambda req: json_response(200, payload))

    result = await bundle.sdk.chats.get_playbook_chats_async(playbook_id="pb-2")

    assert result.chats == []


# ---------------------------------------------------------------------------
# rate_cell
# ---------------------------------------------------------------------------


def test_rate_cell_sync_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.rate_cell(
        chat_id="chat-1",
        cell_id="cell-1",
        rating="CELL_RATING_UP",
        reason="great answer",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RateChatCell"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY
    body = bundle.transport.body_json()
    assert body == {
        "chatId": "chat-1",
        "cellId": "cell-1",
        "rating": "CELL_RATING_UP",
        "reason": "great answer",
    }


async def test_rate_cell_async_sends_correct_request(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    await bundle.sdk.chats.rate_cell_async(
        chat_id="chat-2",
        cell_id="cell-2",
        rating="CELL_RATING_DOWN",
        reason="not helpful",
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == f"{BASE_PATH}/RateChatCell"
    body = bundle.transport.body_json()
    assert body == {
        "chatId": "chat-2",
        "cellId": "cell-2",
        "rating": "CELL_RATING_DOWN",
        "reason": "not helpful",
    }


def test_rate_cell_reason_unset_omits_field(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.rate_cell(chat_id="chat-1", cell_id="cell-1", rating="CELL_RATING_UP")

    body = bundle.transport.body_json()
    assert "reason" not in body
    assert body == {"chatId": "chat-1", "cellId": "cell-1", "rating": "CELL_RATING_UP"}


def test_rate_cell_reason_explicit_value_included(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.rate_cell(
        chat_id="chat-1", cell_id="cell-1", reason="explicit reason"
    )

    body = bundle.transport.body_json()
    assert body["reason"] == "explicit reason"


def test_rate_cell_reason_explicit_none_serializes_as_null(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.rate_cell(chat_id="chat-1", cell_id="cell-1", reason=None)

    body = bundle.transport.body_json()
    assert "reason" in body
    assert body["reason"] is None


def test_rate_cell_sync_unmarshals_200_empty_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = bundle.sdk.chats.rate_cell(
        chat_id="chat-1", cell_id="cell-1", rating="CELL_RATING_UP"
    )

    assert isinstance(result, models.GoogleProtobufEmpty)


async def test_rate_cell_async_unmarshals_200_empty_response(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    result = await bundle.sdk.chats.rate_cell_async(
        chat_id="chat-2", cell_id="cell-2", rating="CELL_RATING_DOWN"
    )

    assert isinstance(result, models.GoogleProtobufEmpty)


def test_rate_cell_sync_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid rating"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.rate_cell(chat_id="chat-1", cell_id="cell-1")

    assert exc_info.value.status_code == 422


def test_rate_cell_sync_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.rate_cell(chat_id="chat-1", cell_id="cell-1")

    assert exc_info.value.status_code == 502


async def test_rate_cell_async_4xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.rate_cell_async(chat_id="chat-2", cell_id="cell-2")

    assert exc_info.value.status_code == 403


async def test_rate_cell_async_5xx_raises_textql_default_error(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "server error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.rate_cell_async(chat_id="chat-2", cell_id="cell-2")

    assert exc_info.value.status_code == 500
