"""Unit tests for Chats ontology/context-prompt-change approval operations."""
import pytest

from tests.conftest import AUTH_HEADER_NAME, FAKE_API_KEY, json_response
from textql_sdk import errors


# ---------------------------------------------------------------------------
# approve_context_prompt_change
# ---------------------------------------------------------------------------


def test_approve_context_prompt_change_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "approved",
                "status": "STATUS_APPLIED",
                "resumed": True,
                "resumeError": "",
            },
        )
    )

    result = bundle.sdk.chats.approve_context_prompt_change(
        cell_id="cell-123", edited_context="new context text"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/ApproveContextPromptChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-123", "editedContext": "new context text"}

    assert result.success is True
    assert result.message == "approved"
    assert result.status == "STATUS_APPLIED"
    assert result.resumed is True
    assert result.resume_error == ""


async def test_approve_context_prompt_change_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "approved async",
                "status": "STATUS_APPLIED",
                "resumed": False,
            },
        )
    )

    result = await bundle.sdk.chats.approve_context_prompt_change_async(
        cell_id="cell-async-1", edited_context="edited async"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/ApproveContextPromptChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-async-1", "editedContext": "edited async"}

    assert result.success is True
    assert result.message == "approved async"
    assert result.resumed is False


def test_approve_context_prompt_change_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.approve_context_prompt_change()

    body = bundle.transport.body_json()
    # Both cell_id and edited_context default to None (unset) and the
    # model_serializer omits keys whose value is None when the field is in
    # `optional_fields`, so the JSON body should be empty.
    assert body == {}


def test_approve_context_prompt_change_only_cell_id_set(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.approve_context_prompt_change(cell_id="only-cell")

    body = bundle.transport.body_json()
    assert body == {"cellId": "only-cell"}


# ---------------------------------------------------------------------------
# reject_context_prompt_change
# ---------------------------------------------------------------------------


def test_reject_context_prompt_change_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "rejected",
                "status": "STATUS_REJECTED",
                "resumed": True,
            },
        )
    )

    result = bundle.sdk.chats.reject_context_prompt_change(cell_id="cell-reject-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/RejectContextPromptChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-reject-1"}

    assert result.success is True
    assert result.status == "STATUS_REJECTED"


async def test_reject_context_prompt_change_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": False,
                "message": "could not reject",
                "status": "STATUS_PENDING",
            },
        )
    )

    result = await bundle.sdk.chats.reject_context_prompt_change_async(
        cell_id="cell-reject-async"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/RejectContextPromptChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "cell-reject-async"}

    assert result.success is False
    assert result.status == "STATUS_PENDING"


def test_reject_context_prompt_change_omits_unset_cell_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.reject_context_prompt_change()

    body = bundle.transport.body_json()
    assert body == {}


# ---------------------------------------------------------------------------
# submit_context_prompt_change
# ---------------------------------------------------------------------------


def test_submit_context_prompt_change_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "submitted",
                "status": "STATUS_DRAFT",
                "resumed": False,
                "resumeError": "none",
            },
        )
    )

    result = bundle.sdk.chats.submit_context_prompt_change(
        cell_id="cell-submit-1", edited_context="proposed new context body"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/SubmitContextPromptChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "cellId": "cell-submit-1",
        "editedContext": "proposed new context body",
    }

    assert result.success is True
    assert result.message == "submitted"
    assert result.status == "STATUS_DRAFT"
    assert result.resumed is False
    assert result.resume_error == "none"


async def test_submit_context_prompt_change_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "submitted async",
                "status": "STATUS_PENDING",
            },
        )
    )

    result = await bundle.sdk.chats.submit_context_prompt_change_async(
        cell_id="cell-submit-async", edited_context="edited context payload"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path
        == "/textql.rpc.public.chat.ChatService/SubmitContextPromptChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {
        "cellId": "cell-submit-async",
        "editedContext": "edited context payload",
    }

    assert result.success is True
    assert result.status == "STATUS_PENDING"


def test_submit_context_prompt_change_omits_unset_fields(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.submit_context_prompt_change()

    body = bundle.transport.body_json()
    assert body == {}


def test_submit_context_prompt_change_only_edited_context_set(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.submit_context_prompt_change(edited_context="context only")

    body = bundle.transport.body_json()
    assert body == {"editedContext": "context only"}


def test_submit_context_prompt_change_sync_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(422, {"message": "invalid cell"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.submit_context_prompt_change(
            cell_id="bad-cell", edited_context="x"
        )

    assert exc_info.value.status_code == 422


def test_submit_context_prompt_change_sync_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(503, {"message": "server error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.submit_context_prompt_change(
            cell_id="cell-1", edited_context="x"
        )

    assert exc_info.value.status_code == 503


async def test_submit_context_prompt_change_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(404, {"message": "not found"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.submit_context_prompt_change_async(
            cell_id="missing-cell", edited_context="x"
        )

    assert exc_info.value.status_code == 404


async def test_submit_context_prompt_change_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(500, {"message": "internal error"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.submit_context_prompt_change_async(
            cell_id="cell-1", edited_context="x"
        )

    assert exc_info.value.status_code == 500


# ---------------------------------------------------------------------------
# approve_ontology_change
# ---------------------------------------------------------------------------


def test_approve_ontology_change_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "ontology change approved",
                "resumed": True,
                "resumeError": "",
            },
        )
    )

    result = bundle.sdk.chats.approve_ontology_change(cell_id="ontology-cell-1")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path == "/textql.rpc.public.chat.ChatService/ApproveOntologyChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "ontology-cell-1"}

    assert result.success is True
    assert result.message == "ontology change approved"
    assert result.resumed is True
    assert result.resume_error == ""


async def test_approve_ontology_change_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "approved async",
                "resumed": False,
            },
        )
    )

    result = await bundle.sdk.chats.approve_ontology_change_async(
        cell_id="ontology-cell-async"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert (
        req.url.path == "/textql.rpc.public.chat.ChatService/ApproveOntologyChange"
    )
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "ontology-cell-async"}

    assert result.success is True
    assert result.resumed is False


def test_approve_ontology_change_omits_unset_cell_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.approve_ontology_change()

    body = bundle.transport.body_json()
    assert body == {}


def test_approve_ontology_change_sync_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(400, {"message": "bad request"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.approve_ontology_change(cell_id="bad-cell")

    assert exc_info.value.status_code == 400


def test_approve_ontology_change_sync_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(502, {"message": "bad gateway"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        bundle.sdk.chats.approve_ontology_change(cell_id="cell-1")

    assert exc_info.value.status_code == 502


async def test_approve_ontology_change_async_4xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(403, {"message": "forbidden"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.approve_ontology_change_async(cell_id="cell-1")

    assert exc_info.value.status_code == 403


async def test_approve_ontology_change_async_5xx_raises(make_sdk):
    bundle = make_sdk(lambda req: json_response(504, {"message": "gateway timeout"}))

    with pytest.raises(errors.TextqlDefaultError) as exc_info:
        await bundle.sdk.chats.approve_ontology_change_async(cell_id="cell-1")

    assert exc_info.value.status_code == 504


# ---------------------------------------------------------------------------
# reject_ontology_change
# ---------------------------------------------------------------------------


def test_reject_ontology_change_sync_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": True,
                "message": "ontology change rejected",
                "resumed": True,
            },
        )
    )

    result = bundle.sdk.chats.reject_ontology_change(cell_id="ontology-cell-reject")

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/RejectOntologyChange"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "ontology-cell-reject"}

    assert result.success is True
    assert result.message == "ontology change rejected"
    assert result.resumed is True


async def test_reject_ontology_change_async_request_and_response(make_sdk):
    bundle = make_sdk(
        lambda req: json_response(
            200,
            {
                "success": False,
                "message": "rejection failed",
                "resumeError": "could not resume",
            },
        )
    )

    result = await bundle.sdk.chats.reject_ontology_change_async(
        cell_id="ontology-cell-reject-async"
    )

    req = bundle.transport.last_request
    assert req.method == "POST"
    assert req.url.path == "/textql.rpc.public.chat.ChatService/RejectOntologyChange"
    assert req.headers[AUTH_HEADER_NAME] == FAKE_API_KEY

    body = bundle.transport.body_json()
    assert body == {"cellId": "ontology-cell-reject-async"}

    assert result.success is False
    assert result.resume_error == "could not resume"


def test_reject_ontology_change_omits_unset_cell_id(make_sdk):
    bundle = make_sdk(lambda req: json_response(200, {}))

    bundle.sdk.chats.reject_ontology_change()

    body = bundle.transport.body_json()
    assert body == {}
