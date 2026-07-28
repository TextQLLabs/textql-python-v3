# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
from collections.abc import AsyncGenerator, AsyncIterator, Iterable, Iterator, Mapping
from typing import Protocol
from connectrpc.client import ConnectClient, ConnectClientSync
from connectrpc.code import Code
from connectrpc.compression import Compression
from connectrpc.errors import ConnectError
from connectrpc.interceptor import Interceptor, InterceptorSync
from connectrpc.method import IdempotencyLevel, MethodInfo
from connectrpc.request import Headers, RequestContext
from connectrpc.server import ConnectASGIApplication, ConnectWSGIApplication, Endpoint, EndpointSync
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import chat_pb2 as public_dot_chat__pb2

class ChatService(Protocol):

    async def create_chat(self, request: public_dot_chat__pb2.CreateRequest, ctx: RequestContext) -> public_dot_chat__pb2.CreateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_chat(self, request: public_dot_chat__pb2.UpdateChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_chat(self, request: public_dot_chat__pb2.DeleteChatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def duplicate_chat(self, request: public_dot_chat__pb2.DuplicateChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.DuplicateChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def watch_chat(self, request: public_dot_chat__pb2.WatchChatRequest, ctx: RequestContext) -> AsyncIterator[public_dot_chat__pb2.WatchChatEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def poll_chat_events(self, request: public_dot_chat__pb2.PollChatEventsRequest, ctx: RequestContext) -> public_dot_chat__pb2.PollChatEventsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_chat(self, request: public_dot_chat__pb2.RunChatRequest, ctx: RequestContext) -> AsyncIterator[public_dot_chat__pb2.Cell]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def cancel_stream(self, request: public_dot_chat__pb2.CancelStreamRequest, ctx: RequestContext) -> public_dot_chat__pb2.CancelStreamResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def run_chat(self, request: public_dot_chat__pb2.RunChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.RunChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def send_message(self, request: public_dot_chat__pb2.SendRequest, ctx: RequestContext) -> public_dot_chat__pb2.SendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def check_health(self, request: public_dot_chat__pb2.CheckHealthRequest, ctx: RequestContext) -> public_dot_chat__pb2.CheckHealthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def rate_chat_cell(self, request: public_dot_chat__pb2.RateChatCellRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def attach_dataset(self, request: public_dot_chat__pb2.AttachDatasetRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def attach_dashboard(self, request: public_dot_chat__pb2.AttachDashboardRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def attach_app(self, request: public_dot_chat__pb2.AttachAppRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_chat_history(self, request: public_dot_chat__pb2.HistoryRequest, ctx: RequestContext) -> public_dot_chat__pb2.HistoryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_a_p_i_chat_answer(self, request: public_dot_chat__pb2.GetAPIChatAnswerRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetAPIChatAnswerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_chats(self, request: public_dot_chat__pb2.GetChatsRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_chat(self, request: public_dot_chat__pb2.GetChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_playbook_chats(self, request: public_dot_chat__pb2.GetPlaybookChatsRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetPlaybookChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_members_with_chats(self, request: public_dot_chat__pb2.GetMembersWithChatsRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetMembersWithChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_completion_parameters(self, request: public_dot_chat__pb2.GetCompletionParametersRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCompletionParametersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_completion_parameters_batch(self, request: public_dot_chat__pb2.GetCompletionParametersBatchRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCompletionParametersBatchResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_chat_execution_timing(self, request: public_dot_chat__pb2.GetChatExecutionTimingRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatExecutionTimingResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def check_chat_permissions(self, request: public_dot_chat__pb2.CheckChatPermissionsRequest, ctx: RequestContext) -> public_dot_chat__pb2.CheckChatPermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_llm_usage(self, request: public_dot_chat__pb2.GetLlmUsageRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetLlmUsageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def approve_context_prompt_change(self, request: public_dot_chat__pb2.ApproveContextPromptChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.ApproveContextPromptChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def reject_context_prompt_change(self, request: public_dot_chat__pb2.RejectContextPromptChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.RejectContextPromptChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def submit_context_prompt_change(self, request: public_dot_chat__pb2.SubmitContextPromptChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.SubmitContextPromptChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def submit_questions(self, request: public_dot_chat__pb2.SubmitQuestionsRequest, ctx: RequestContext) -> public_dot_chat__pb2.SubmitQuestionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def dismiss_questions(self, request: public_dot_chat__pb2.DismissQuestionsRequest, ctx: RequestContext) -> public_dot_chat__pb2.DismissQuestionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def submit_form_approval(self, request: public_dot_chat__pb2.SubmitFormApprovalRequest, ctx: RequestContext) -> public_dot_chat__pb2.SubmitFormApprovalResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def reject_form_approval(self, request: public_dot_chat__pb2.RejectFormApprovalRequest, ctx: RequestContext) -> public_dot_chat__pb2.RejectFormApprovalResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def dismiss_form_approval(self, request: public_dot_chat__pb2.DismissFormApprovalRequest, ctx: RequestContext) -> public_dot_chat__pb2.DismissFormApprovalResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def resume_chat_after_auth(self, request: public_dot_chat__pb2.ResumeChatAfterAuthRequest, ctx: RequestContext) -> public_dot_chat__pb2.ResumeChatAfterAuthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def grant_sandbox_o_auth_permission(self, request: public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, ctx: RequestContext) -> public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_cell_auth_status(self, request: public_dot_chat__pb2.GetCellAuthStatusRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCellAuthStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def approve_ontology_change(self, request: public_dot_chat__pb2.ApproveOntologyChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.ApproveOntologyChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def reject_ontology_change(self, request: public_dot_chat__pb2.RejectOntologyChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.RejectOntologyChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def query_one_shot(self, request: public_dot_chat__pb2.QueryOneShotRequest, ctx: RequestContext) -> public_dot_chat__pb2.QueryOneShotResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def check_streamlit_health(self, request: public_dot_chat__pb2.CheckStreamlitHealthRequest, ctx: RequestContext) -> public_dot_chat__pb2.CheckStreamlitHealthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_form_status(self, request: public_dot_chat__pb2.UpdateFormStatusRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateFormStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_form_fields(self, request: public_dot_chat__pb2.UpdateFormFieldsRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateFormFieldsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_form_validation_error(self, request: public_dot_chat__pb2.UpdateFormValidationErrorRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateFormValidationErrorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_form_submit_result(self, request: public_dot_chat__pb2.SetFormSubmitResultRequest, ctx: RequestContext) -> public_dot_chat__pb2.SetFormSubmitResultResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_cell(self, request: public_dot_chat__pb2.GetCellRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCellResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def bookmark_chat(self, request: public_dot_chat__pb2.BookmarkChatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def unbookmark_chat(self, request: public_dot_chat__pb2.UnbookmarkChatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def mark_chat_read(self, request: public_dot_chat__pb2.MarkChatReadRequest, ctx: RequestContext) -> public_dot_chat__pb2.MarkChatReadResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def mark_chat_unread(self, request: public_dot_chat__pb2.MarkChatUnreadRequest, ctx: RequestContext) -> public_dot_chat__pb2.MarkChatUnreadResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_chat_artifacts_summary(self, request: public_dot_chat__pb2.GetChatArtifactsSummaryRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatArtifactsSummaryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_artifact(self, request: public_dot_chat__pb2.GetArtifactRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetArtifactResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def attach_agent_to_chat(self, request: public_dot_chat__pb2.AttachAgentToChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachAgentToChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ChatServiceASGIApplication(ConnectASGIApplication[ChatService]):

    def __init__(self, service: ChatService | AsyncGenerator[ChatService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.chat.ChatService/CreateChat': Endpoint.unary(method=MethodInfo(name='CreateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CreateRequest, output=public_dot_chat__pb2.CreateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_chat), '/textql.rpc.public.chat.ChatService/UpdateChat': Endpoint.unary(method=MethodInfo(name='UpdateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateChatRequest, output=public_dot_chat__pb2.UpdateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_chat), '/textql.rpc.public.chat.ChatService/DeleteChat': Endpoint.unary(method=MethodInfo(name='DeleteChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DeleteChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_chat), '/textql.rpc.public.chat.ChatService/DuplicateChat': Endpoint.unary(method=MethodInfo(name='DuplicateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DuplicateChatRequest, output=public_dot_chat__pb2.DuplicateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.duplicate_chat), '/textql.rpc.public.chat.ChatService/WatchChat': Endpoint.server_stream(method=MethodInfo(name='WatchChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.WatchChatRequest, output=public_dot_chat__pb2.WatchChatEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.watch_chat), '/textql.rpc.public.chat.ChatService/PollChatEvents': Endpoint.unary(method=MethodInfo(name='PollChatEvents', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.PollChatEventsRequest, output=public_dot_chat__pb2.PollChatEventsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.poll_chat_events), '/textql.rpc.public.chat.ChatService/StreamChat': Endpoint.server_stream(method=MethodInfo(name='StreamChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.Cell, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.stream_chat), '/textql.rpc.public.chat.ChatService/CancelStream': Endpoint.unary(method=MethodInfo(name='CancelStream', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CancelStreamRequest, output=public_dot_chat__pb2.CancelStreamResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.cancel_stream), '/textql.rpc.public.chat.ChatService/RunChat': Endpoint.unary(method=MethodInfo(name='RunChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.RunChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.run_chat), '/textql.rpc.public.chat.ChatService/SendMessage': Endpoint.unary(method=MethodInfo(name='SendMessage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SendRequest, output=public_dot_chat__pb2.SendResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.send_message), '/textql.rpc.public.chat.ChatService/CheckHealth': Endpoint.unary(method=MethodInfo(name='CheckHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckHealthRequest, output=public_dot_chat__pb2.CheckHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.check_health), '/textql.rpc.public.chat.ChatService/RateChatCell': Endpoint.unary(method=MethodInfo(name='RateChatCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RateChatCellRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.rate_chat_cell), '/textql.rpc.public.chat.ChatService/AttachDataset': Endpoint.unary(method=MethodInfo(name='AttachDataset', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDatasetRequest, output=public_dot_chat__pb2.AttachDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.attach_dataset), '/textql.rpc.public.chat.ChatService/AttachDashboard': Endpoint.unary(method=MethodInfo(name='AttachDashboard', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDashboardRequest, output=public_dot_chat__pb2.AttachDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.attach_dashboard), '/textql.rpc.public.chat.ChatService/AttachApp': Endpoint.unary(method=MethodInfo(name='AttachApp', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAppRequest, output=public_dot_chat__pb2.AttachAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.attach_app), '/textql.rpc.public.chat.ChatService/GetChatHistory': Endpoint.unary(method=MethodInfo(name='GetChatHistory', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.HistoryRequest, output=public_dot_chat__pb2.HistoryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_chat_history), '/textql.rpc.public.chat.ChatService/GetAPIChatAnswer': Endpoint.unary(method=MethodInfo(name='GetAPIChatAnswer', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetAPIChatAnswerRequest, output=public_dot_chat__pb2.GetAPIChatAnswerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_a_p_i_chat_answer), '/textql.rpc.public.chat.ChatService/GetChats': Endpoint.unary(method=MethodInfo(name='GetChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatsRequest, output=public_dot_chat__pb2.GetChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_chats), '/textql.rpc.public.chat.ChatService/GetChat': Endpoint.unary(method=MethodInfo(name='GetChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatRequest, output=public_dot_chat__pb2.GetChatResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_chat), '/textql.rpc.public.chat.ChatService/GetPlaybookChats': Endpoint.unary(method=MethodInfo(name='GetPlaybookChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetPlaybookChatsRequest, output=public_dot_chat__pb2.GetPlaybookChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_playbook_chats), '/textql.rpc.public.chat.ChatService/GetMembersWithChats': Endpoint.unary(method=MethodInfo(name='GetMembersWithChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetMembersWithChatsRequest, output=public_dot_chat__pb2.GetMembersWithChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_members_with_chats), '/textql.rpc.public.chat.ChatService/GetCompletionParameters': Endpoint.unary(method=MethodInfo(name='GetCompletionParameters', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersRequest, output=public_dot_chat__pb2.GetCompletionParametersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_completion_parameters), '/textql.rpc.public.chat.ChatService/GetCompletionParametersBatch': Endpoint.unary(method=MethodInfo(name='GetCompletionParametersBatch', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersBatchRequest, output=public_dot_chat__pb2.GetCompletionParametersBatchResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_completion_parameters_batch), '/textql.rpc.public.chat.ChatService/GetChatExecutionTiming': Endpoint.unary(method=MethodInfo(name='GetChatExecutionTiming', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatExecutionTimingRequest, output=public_dot_chat__pb2.GetChatExecutionTimingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_chat_execution_timing), '/textql.rpc.public.chat.ChatService/CheckChatPermissions': Endpoint.unary(method=MethodInfo(name='CheckChatPermissions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckChatPermissionsRequest, output=public_dot_chat__pb2.CheckChatPermissionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.check_chat_permissions), '/textql.rpc.public.chat.ChatService/GetLlmUsage': Endpoint.unary(method=MethodInfo(name='GetLlmUsage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetLlmUsageRequest, output=public_dot_chat__pb2.GetLlmUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_llm_usage), '/textql.rpc.public.chat.ChatService/ApproveContextPromptChange': Endpoint.unary(method=MethodInfo(name='ApproveContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveContextPromptChangeRequest, output=public_dot_chat__pb2.ApproveContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.approve_context_prompt_change), '/textql.rpc.public.chat.ChatService/RejectContextPromptChange': Endpoint.unary(method=MethodInfo(name='RejectContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectContextPromptChangeRequest, output=public_dot_chat__pb2.RejectContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.reject_context_prompt_change), '/textql.rpc.public.chat.ChatService/SubmitContextPromptChange': Endpoint.unary(method=MethodInfo(name='SubmitContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitContextPromptChangeRequest, output=public_dot_chat__pb2.SubmitContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.submit_context_prompt_change), '/textql.rpc.public.chat.ChatService/SubmitQuestions': Endpoint.unary(method=MethodInfo(name='SubmitQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitQuestionsRequest, output=public_dot_chat__pb2.SubmitQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.submit_questions), '/textql.rpc.public.chat.ChatService/DismissQuestions': Endpoint.unary(method=MethodInfo(name='DismissQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissQuestionsRequest, output=public_dot_chat__pb2.DismissQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.dismiss_questions), '/textql.rpc.public.chat.ChatService/SubmitFormApproval': Endpoint.unary(method=MethodInfo(name='SubmitFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitFormApprovalRequest, output=public_dot_chat__pb2.SubmitFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.submit_form_approval), '/textql.rpc.public.chat.ChatService/RejectFormApproval': Endpoint.unary(method=MethodInfo(name='RejectFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectFormApprovalRequest, output=public_dot_chat__pb2.RejectFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.reject_form_approval), '/textql.rpc.public.chat.ChatService/DismissFormApproval': Endpoint.unary(method=MethodInfo(name='DismissFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissFormApprovalRequest, output=public_dot_chat__pb2.DismissFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.dismiss_form_approval), '/textql.rpc.public.chat.ChatService/ResumeChatAfterAuth': Endpoint.unary(method=MethodInfo(name='ResumeChatAfterAuth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ResumeChatAfterAuthRequest, output=public_dot_chat__pb2.ResumeChatAfterAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.resume_chat_after_auth), '/textql.rpc.public.chat.ChatService/GrantSandboxOAuthPermission': Endpoint.unary(method=MethodInfo(name='GrantSandboxOAuthPermission', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, output=public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.grant_sandbox_o_auth_permission), '/textql.rpc.public.chat.ChatService/GetCellAuthStatus': Endpoint.unary(method=MethodInfo(name='GetCellAuthStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellAuthStatusRequest, output=public_dot_chat__pb2.GetCellAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_cell_auth_status), '/textql.rpc.public.chat.ChatService/ApproveOntologyChange': Endpoint.unary(method=MethodInfo(name='ApproveOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveOntologyChangeRequest, output=public_dot_chat__pb2.ApproveOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.approve_ontology_change), '/textql.rpc.public.chat.ChatService/RejectOntologyChange': Endpoint.unary(method=MethodInfo(name='RejectOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectOntologyChangeRequest, output=public_dot_chat__pb2.RejectOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.reject_ontology_change), '/textql.rpc.public.chat.ChatService/QueryOneShot': Endpoint.unary(method=MethodInfo(name='QueryOneShot', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.QueryOneShotRequest, output=public_dot_chat__pb2.QueryOneShotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.query_one_shot), '/textql.rpc.public.chat.ChatService/CheckStreamlitHealth': Endpoint.unary(method=MethodInfo(name='CheckStreamlitHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckStreamlitHealthRequest, output=public_dot_chat__pb2.CheckStreamlitHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.check_streamlit_health), '/textql.rpc.public.chat.ChatService/UpdateFormStatus': Endpoint.unary(method=MethodInfo(name='UpdateFormStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormStatusRequest, output=public_dot_chat__pb2.UpdateFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_form_status), '/textql.rpc.public.chat.ChatService/UpdateFormFields': Endpoint.unary(method=MethodInfo(name='UpdateFormFields', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormFieldsRequest, output=public_dot_chat__pb2.UpdateFormFieldsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_form_fields), '/textql.rpc.public.chat.ChatService/UpdateFormValidationError': Endpoint.unary(method=MethodInfo(name='UpdateFormValidationError', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormValidationErrorRequest, output=public_dot_chat__pb2.UpdateFormValidationErrorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_form_validation_error), '/textql.rpc.public.chat.ChatService/SetFormSubmitResult': Endpoint.unary(method=MethodInfo(name='SetFormSubmitResult', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SetFormSubmitResultRequest, output=public_dot_chat__pb2.SetFormSubmitResultResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_form_submit_result), '/textql.rpc.public.chat.ChatService/GetCell': Endpoint.unary(method=MethodInfo(name='GetCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellRequest, output=public_dot_chat__pb2.GetCellResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_cell), '/textql.rpc.public.chat.ChatService/BookmarkChat': Endpoint.unary(method=MethodInfo(name='BookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.BookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.bookmark_chat), '/textql.rpc.public.chat.ChatService/UnbookmarkChat': Endpoint.unary(method=MethodInfo(name='UnbookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UnbookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.unbookmark_chat), '/textql.rpc.public.chat.ChatService/MarkChatRead': Endpoint.unary(method=MethodInfo(name='MarkChatRead', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatReadRequest, output=public_dot_chat__pb2.MarkChatReadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.mark_chat_read), '/textql.rpc.public.chat.ChatService/MarkChatUnread': Endpoint.unary(method=MethodInfo(name='MarkChatUnread', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatUnreadRequest, output=public_dot_chat__pb2.MarkChatUnreadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.mark_chat_unread), '/textql.rpc.public.chat.ChatService/GetChatArtifactsSummary': Endpoint.unary(method=MethodInfo(name='GetChatArtifactsSummary', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatArtifactsSummaryRequest, output=public_dot_chat__pb2.GetChatArtifactsSummaryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_chat_artifacts_summary), '/textql.rpc.public.chat.ChatService/GetArtifact': Endpoint.unary(method=MethodInfo(name='GetArtifact', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetArtifactRequest, output=public_dot_chat__pb2.GetArtifactResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_artifact), '/textql.rpc.public.chat.ChatService/AttachAgentToChat': Endpoint.unary(method=MethodInfo(name='AttachAgentToChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAgentToChatRequest, output=public_dot_chat__pb2.AttachAgentToChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.attach_agent_to_chat)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.chat.ChatService'

class ChatServiceClient(ConnectClient):

    async def create_chat(self, request: public_dot_chat__pb2.CreateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CreateResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CreateRequest, output=public_dot_chat__pb2.CreateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_chat(self, request: public_dot_chat__pb2.UpdateChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateChatResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateChatRequest, output=public_dot_chat__pb2.UpdateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_chat(self, request: public_dot_chat__pb2.DeleteChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DeleteChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def duplicate_chat(self, request: public_dot_chat__pb2.DuplicateChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.DuplicateChatResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DuplicateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DuplicateChatRequest, output=public_dot_chat__pb2.DuplicateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def watch_chat(self, request: public_dot_chat__pb2.WatchChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> AsyncIterator[public_dot_chat__pb2.WatchChatEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='WatchChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.WatchChatRequest, output=public_dot_chat__pb2.WatchChatEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def poll_chat_events(self, request: public_dot_chat__pb2.PollChatEventsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.PollChatEventsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='PollChatEvents', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.PollChatEventsRequest, output=public_dot_chat__pb2.PollChatEventsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_chat(self, request: public_dot_chat__pb2.RunChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> AsyncIterator[public_dot_chat__pb2.Cell]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.Cell, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def cancel_stream(self, request: public_dot_chat__pb2.CancelStreamRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CancelStreamResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CancelStream', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CancelStreamRequest, output=public_dot_chat__pb2.CancelStreamResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def run_chat(self, request: public_dot_chat__pb2.RunChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RunChatResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RunChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.RunChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def send_message(self, request: public_dot_chat__pb2.SendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SendResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SendMessage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SendRequest, output=public_dot_chat__pb2.SendResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def check_health(self, request: public_dot_chat__pb2.CheckHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CheckHealthResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CheckHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckHealthRequest, output=public_dot_chat__pb2.CheckHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def rate_chat_cell(self, request: public_dot_chat__pb2.RateChatCellRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='RateChatCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RateChatCellRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def attach_dataset(self, request: public_dot_chat__pb2.AttachDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachDatasetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AttachDataset', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDatasetRequest, output=public_dot_chat__pb2.AttachDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def attach_dashboard(self, request: public_dot_chat__pb2.AttachDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachDashboardResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AttachDashboard', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDashboardRequest, output=public_dot_chat__pb2.AttachDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def attach_app(self, request: public_dot_chat__pb2.AttachAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachAppResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AttachApp', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAppRequest, output=public_dot_chat__pb2.AttachAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_chat_history(self, request: public_dot_chat__pb2.HistoryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.HistoryResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetChatHistory', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.HistoryRequest, output=public_dot_chat__pb2.HistoryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_a_p_i_chat_answer(self, request: public_dot_chat__pb2.GetAPIChatAnswerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetAPIChatAnswerResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetAPIChatAnswer', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetAPIChatAnswerRequest, output=public_dot_chat__pb2.GetAPIChatAnswerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_chats(self, request: public_dot_chat__pb2.GetChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatsRequest, output=public_dot_chat__pb2.GetChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_chat(self, request: public_dot_chat__pb2.GetChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatRequest, output=public_dot_chat__pb2.GetChatResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_playbook_chats(self, request: public_dot_chat__pb2.GetPlaybookChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetPlaybookChatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetPlaybookChatsRequest, output=public_dot_chat__pb2.GetPlaybookChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_members_with_chats(self, request: public_dot_chat__pb2.GetMembersWithChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetMembersWithChatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetMembersWithChatsRequest, output=public_dot_chat__pb2.GetMembersWithChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_completion_parameters(self, request: public_dot_chat__pb2.GetCompletionParametersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCompletionParametersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCompletionParameters', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersRequest, output=public_dot_chat__pb2.GetCompletionParametersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_completion_parameters_batch(self, request: public_dot_chat__pb2.GetCompletionParametersBatchRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCompletionParametersBatchResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCompletionParametersBatch', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersBatchRequest, output=public_dot_chat__pb2.GetCompletionParametersBatchResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_chat_execution_timing(self, request: public_dot_chat__pb2.GetChatExecutionTimingRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatExecutionTimingResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetChatExecutionTiming', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatExecutionTimingRequest, output=public_dot_chat__pb2.GetChatExecutionTimingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def check_chat_permissions(self, request: public_dot_chat__pb2.CheckChatPermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.CheckChatPermissionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CheckChatPermissions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckChatPermissionsRequest, output=public_dot_chat__pb2.CheckChatPermissionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_llm_usage(self, request: public_dot_chat__pb2.GetLlmUsageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetLlmUsageResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetLlmUsage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetLlmUsageRequest, output=public_dot_chat__pb2.GetLlmUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def approve_context_prompt_change(self, request: public_dot_chat__pb2.ApproveContextPromptChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.ApproveContextPromptChangeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ApproveContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveContextPromptChangeRequest, output=public_dot_chat__pb2.ApproveContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def reject_context_prompt_change(self, request: public_dot_chat__pb2.RejectContextPromptChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RejectContextPromptChangeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RejectContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectContextPromptChangeRequest, output=public_dot_chat__pb2.RejectContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def submit_context_prompt_change(self, request: public_dot_chat__pb2.SubmitContextPromptChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SubmitContextPromptChangeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SubmitContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitContextPromptChangeRequest, output=public_dot_chat__pb2.SubmitContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def submit_questions(self, request: public_dot_chat__pb2.SubmitQuestionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SubmitQuestionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SubmitQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitQuestionsRequest, output=public_dot_chat__pb2.SubmitQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def dismiss_questions(self, request: public_dot_chat__pb2.DismissQuestionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.DismissQuestionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DismissQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissQuestionsRequest, output=public_dot_chat__pb2.DismissQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def submit_form_approval(self, request: public_dot_chat__pb2.SubmitFormApprovalRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SubmitFormApprovalResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SubmitFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitFormApprovalRequest, output=public_dot_chat__pb2.SubmitFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def reject_form_approval(self, request: public_dot_chat__pb2.RejectFormApprovalRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RejectFormApprovalResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RejectFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectFormApprovalRequest, output=public_dot_chat__pb2.RejectFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def dismiss_form_approval(self, request: public_dot_chat__pb2.DismissFormApprovalRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.DismissFormApprovalResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DismissFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissFormApprovalRequest, output=public_dot_chat__pb2.DismissFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def resume_chat_after_auth(self, request: public_dot_chat__pb2.ResumeChatAfterAuthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.ResumeChatAfterAuthResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ResumeChatAfterAuth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ResumeChatAfterAuthRequest, output=public_dot_chat__pb2.ResumeChatAfterAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def grant_sandbox_o_auth_permission(self, request: public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GrantSandboxOAuthPermission', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, output=public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_cell_auth_status(self, request: public_dot_chat__pb2.GetCellAuthStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCellAuthStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCellAuthStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellAuthStatusRequest, output=public_dot_chat__pb2.GetCellAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def approve_ontology_change(self, request: public_dot_chat__pb2.ApproveOntologyChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.ApproveOntologyChangeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ApproveOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveOntologyChangeRequest, output=public_dot_chat__pb2.ApproveOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def reject_ontology_change(self, request: public_dot_chat__pb2.RejectOntologyChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RejectOntologyChangeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RejectOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectOntologyChangeRequest, output=public_dot_chat__pb2.RejectOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def query_one_shot(self, request: public_dot_chat__pb2.QueryOneShotRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.QueryOneShotResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='QueryOneShot', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.QueryOneShotRequest, output=public_dot_chat__pb2.QueryOneShotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def check_streamlit_health(self, request: public_dot_chat__pb2.CheckStreamlitHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CheckStreamlitHealthResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CheckStreamlitHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckStreamlitHealthRequest, output=public_dot_chat__pb2.CheckStreamlitHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_form_status(self, request: public_dot_chat__pb2.UpdateFormStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateFormStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateFormStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormStatusRequest, output=public_dot_chat__pb2.UpdateFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_form_fields(self, request: public_dot_chat__pb2.UpdateFormFieldsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateFormFieldsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateFormFields', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormFieldsRequest, output=public_dot_chat__pb2.UpdateFormFieldsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_form_validation_error(self, request: public_dot_chat__pb2.UpdateFormValidationErrorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateFormValidationErrorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateFormValidationError', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormValidationErrorRequest, output=public_dot_chat__pb2.UpdateFormValidationErrorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def set_form_submit_result(self, request: public_dot_chat__pb2.SetFormSubmitResultRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SetFormSubmitResultResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetFormSubmitResult', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SetFormSubmitResultRequest, output=public_dot_chat__pb2.SetFormSubmitResultResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_cell(self, request: public_dot_chat__pb2.GetCellRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCellResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellRequest, output=public_dot_chat__pb2.GetCellResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def bookmark_chat(self, request: public_dot_chat__pb2.BookmarkChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='BookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.BookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def unbookmark_chat(self, request: public_dot_chat__pb2.UnbookmarkChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='UnbookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UnbookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def mark_chat_read(self, request: public_dot_chat__pb2.MarkChatReadRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.MarkChatReadResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='MarkChatRead', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatReadRequest, output=public_dot_chat__pb2.MarkChatReadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def mark_chat_unread(self, request: public_dot_chat__pb2.MarkChatUnreadRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.MarkChatUnreadResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='MarkChatUnread', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatUnreadRequest, output=public_dot_chat__pb2.MarkChatUnreadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_chat_artifacts_summary(self, request: public_dot_chat__pb2.GetChatArtifactsSummaryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatArtifactsSummaryResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetChatArtifactsSummary', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatArtifactsSummaryRequest, output=public_dot_chat__pb2.GetChatArtifactsSummaryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_artifact(self, request: public_dot_chat__pb2.GetArtifactRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetArtifactResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetArtifact', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetArtifactRequest, output=public_dot_chat__pb2.GetArtifactResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def attach_agent_to_chat(self, request: public_dot_chat__pb2.AttachAgentToChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachAgentToChatResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AttachAgentToChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAgentToChatRequest, output=public_dot_chat__pb2.AttachAgentToChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class ChatServiceSync(Protocol):

    def create_chat(self, request: public_dot_chat__pb2.CreateRequest, ctx: RequestContext) -> public_dot_chat__pb2.CreateResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_chat(self, request: public_dot_chat__pb2.UpdateChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_chat(self, request: public_dot_chat__pb2.DeleteChatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def duplicate_chat(self, request: public_dot_chat__pb2.DuplicateChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.DuplicateChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def watch_chat(self, request: public_dot_chat__pb2.WatchChatRequest, ctx: RequestContext) -> Iterator[public_dot_chat__pb2.WatchChatEvent]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def poll_chat_events(self, request: public_dot_chat__pb2.PollChatEventsRequest, ctx: RequestContext) -> public_dot_chat__pb2.PollChatEventsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_chat(self, request: public_dot_chat__pb2.RunChatRequest, ctx: RequestContext) -> Iterator[public_dot_chat__pb2.Cell]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def cancel_stream(self, request: public_dot_chat__pb2.CancelStreamRequest, ctx: RequestContext) -> public_dot_chat__pb2.CancelStreamResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def run_chat(self, request: public_dot_chat__pb2.RunChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.RunChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def send_message(self, request: public_dot_chat__pb2.SendRequest, ctx: RequestContext) -> public_dot_chat__pb2.SendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def check_health(self, request: public_dot_chat__pb2.CheckHealthRequest, ctx: RequestContext) -> public_dot_chat__pb2.CheckHealthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def rate_chat_cell(self, request: public_dot_chat__pb2.RateChatCellRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def attach_dataset(self, request: public_dot_chat__pb2.AttachDatasetRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def attach_dashboard(self, request: public_dot_chat__pb2.AttachDashboardRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachDashboardResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def attach_app(self, request: public_dot_chat__pb2.AttachAppRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachAppResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_chat_history(self, request: public_dot_chat__pb2.HistoryRequest, ctx: RequestContext) -> public_dot_chat__pb2.HistoryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_a_p_i_chat_answer(self, request: public_dot_chat__pb2.GetAPIChatAnswerRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetAPIChatAnswerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_chats(self, request: public_dot_chat__pb2.GetChatsRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_chat(self, request: public_dot_chat__pb2.GetChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_playbook_chats(self, request: public_dot_chat__pb2.GetPlaybookChatsRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetPlaybookChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_members_with_chats(self, request: public_dot_chat__pb2.GetMembersWithChatsRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetMembersWithChatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_completion_parameters(self, request: public_dot_chat__pb2.GetCompletionParametersRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCompletionParametersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_completion_parameters_batch(self, request: public_dot_chat__pb2.GetCompletionParametersBatchRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCompletionParametersBatchResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_chat_execution_timing(self, request: public_dot_chat__pb2.GetChatExecutionTimingRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatExecutionTimingResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def check_chat_permissions(self, request: public_dot_chat__pb2.CheckChatPermissionsRequest, ctx: RequestContext) -> public_dot_chat__pb2.CheckChatPermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_llm_usage(self, request: public_dot_chat__pb2.GetLlmUsageRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetLlmUsageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def approve_context_prompt_change(self, request: public_dot_chat__pb2.ApproveContextPromptChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.ApproveContextPromptChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def reject_context_prompt_change(self, request: public_dot_chat__pb2.RejectContextPromptChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.RejectContextPromptChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def submit_context_prompt_change(self, request: public_dot_chat__pb2.SubmitContextPromptChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.SubmitContextPromptChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def submit_questions(self, request: public_dot_chat__pb2.SubmitQuestionsRequest, ctx: RequestContext) -> public_dot_chat__pb2.SubmitQuestionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def dismiss_questions(self, request: public_dot_chat__pb2.DismissQuestionsRequest, ctx: RequestContext) -> public_dot_chat__pb2.DismissQuestionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def submit_form_approval(self, request: public_dot_chat__pb2.SubmitFormApprovalRequest, ctx: RequestContext) -> public_dot_chat__pb2.SubmitFormApprovalResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def reject_form_approval(self, request: public_dot_chat__pb2.RejectFormApprovalRequest, ctx: RequestContext) -> public_dot_chat__pb2.RejectFormApprovalResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def dismiss_form_approval(self, request: public_dot_chat__pb2.DismissFormApprovalRequest, ctx: RequestContext) -> public_dot_chat__pb2.DismissFormApprovalResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def resume_chat_after_auth(self, request: public_dot_chat__pb2.ResumeChatAfterAuthRequest, ctx: RequestContext) -> public_dot_chat__pb2.ResumeChatAfterAuthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def grant_sandbox_o_auth_permission(self, request: public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, ctx: RequestContext) -> public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_cell_auth_status(self, request: public_dot_chat__pb2.GetCellAuthStatusRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCellAuthStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def approve_ontology_change(self, request: public_dot_chat__pb2.ApproveOntologyChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.ApproveOntologyChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def reject_ontology_change(self, request: public_dot_chat__pb2.RejectOntologyChangeRequest, ctx: RequestContext) -> public_dot_chat__pb2.RejectOntologyChangeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def query_one_shot(self, request: public_dot_chat__pb2.QueryOneShotRequest, ctx: RequestContext) -> public_dot_chat__pb2.QueryOneShotResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def check_streamlit_health(self, request: public_dot_chat__pb2.CheckStreamlitHealthRequest, ctx: RequestContext) -> public_dot_chat__pb2.CheckStreamlitHealthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_form_status(self, request: public_dot_chat__pb2.UpdateFormStatusRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateFormStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_form_fields(self, request: public_dot_chat__pb2.UpdateFormFieldsRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateFormFieldsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_form_validation_error(self, request: public_dot_chat__pb2.UpdateFormValidationErrorRequest, ctx: RequestContext) -> public_dot_chat__pb2.UpdateFormValidationErrorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_form_submit_result(self, request: public_dot_chat__pb2.SetFormSubmitResultRequest, ctx: RequestContext) -> public_dot_chat__pb2.SetFormSubmitResultResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_cell(self, request: public_dot_chat__pb2.GetCellRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetCellResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def bookmark_chat(self, request: public_dot_chat__pb2.BookmarkChatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def unbookmark_chat(self, request: public_dot_chat__pb2.UnbookmarkChatRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def mark_chat_read(self, request: public_dot_chat__pb2.MarkChatReadRequest, ctx: RequestContext) -> public_dot_chat__pb2.MarkChatReadResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def mark_chat_unread(self, request: public_dot_chat__pb2.MarkChatUnreadRequest, ctx: RequestContext) -> public_dot_chat__pb2.MarkChatUnreadResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_chat_artifacts_summary(self, request: public_dot_chat__pb2.GetChatArtifactsSummaryRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetChatArtifactsSummaryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_artifact(self, request: public_dot_chat__pb2.GetArtifactRequest, ctx: RequestContext) -> public_dot_chat__pb2.GetArtifactResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def attach_agent_to_chat(self, request: public_dot_chat__pb2.AttachAgentToChatRequest, ctx: RequestContext) -> public_dot_chat__pb2.AttachAgentToChatResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ChatServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ChatServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.chat.ChatService/CreateChat': EndpointSync.unary(method=MethodInfo(name='CreateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CreateRequest, output=public_dot_chat__pb2.CreateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_chat), '/textql.rpc.public.chat.ChatService/UpdateChat': EndpointSync.unary(method=MethodInfo(name='UpdateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateChatRequest, output=public_dot_chat__pb2.UpdateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_chat), '/textql.rpc.public.chat.ChatService/DeleteChat': EndpointSync.unary(method=MethodInfo(name='DeleteChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DeleteChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_chat), '/textql.rpc.public.chat.ChatService/DuplicateChat': EndpointSync.unary(method=MethodInfo(name='DuplicateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DuplicateChatRequest, output=public_dot_chat__pb2.DuplicateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.duplicate_chat), '/textql.rpc.public.chat.ChatService/WatchChat': EndpointSync.server_stream(method=MethodInfo(name='WatchChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.WatchChatRequest, output=public_dot_chat__pb2.WatchChatEvent, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.watch_chat), '/textql.rpc.public.chat.ChatService/PollChatEvents': EndpointSync.unary(method=MethodInfo(name='PollChatEvents', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.PollChatEventsRequest, output=public_dot_chat__pb2.PollChatEventsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.poll_chat_events), '/textql.rpc.public.chat.ChatService/StreamChat': EndpointSync.server_stream(method=MethodInfo(name='StreamChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.Cell, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.stream_chat), '/textql.rpc.public.chat.ChatService/CancelStream': EndpointSync.unary(method=MethodInfo(name='CancelStream', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CancelStreamRequest, output=public_dot_chat__pb2.CancelStreamResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.cancel_stream), '/textql.rpc.public.chat.ChatService/RunChat': EndpointSync.unary(method=MethodInfo(name='RunChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.RunChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.run_chat), '/textql.rpc.public.chat.ChatService/SendMessage': EndpointSync.unary(method=MethodInfo(name='SendMessage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SendRequest, output=public_dot_chat__pb2.SendResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.send_message), '/textql.rpc.public.chat.ChatService/CheckHealth': EndpointSync.unary(method=MethodInfo(name='CheckHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckHealthRequest, output=public_dot_chat__pb2.CheckHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.check_health), '/textql.rpc.public.chat.ChatService/RateChatCell': EndpointSync.unary(method=MethodInfo(name='RateChatCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RateChatCellRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.rate_chat_cell), '/textql.rpc.public.chat.ChatService/AttachDataset': EndpointSync.unary(method=MethodInfo(name='AttachDataset', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDatasetRequest, output=public_dot_chat__pb2.AttachDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.attach_dataset), '/textql.rpc.public.chat.ChatService/AttachDashboard': EndpointSync.unary(method=MethodInfo(name='AttachDashboard', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDashboardRequest, output=public_dot_chat__pb2.AttachDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.attach_dashboard), '/textql.rpc.public.chat.ChatService/AttachApp': EndpointSync.unary(method=MethodInfo(name='AttachApp', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAppRequest, output=public_dot_chat__pb2.AttachAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.attach_app), '/textql.rpc.public.chat.ChatService/GetChatHistory': EndpointSync.unary(method=MethodInfo(name='GetChatHistory', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.HistoryRequest, output=public_dot_chat__pb2.HistoryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_chat_history), '/textql.rpc.public.chat.ChatService/GetAPIChatAnswer': EndpointSync.unary(method=MethodInfo(name='GetAPIChatAnswer', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetAPIChatAnswerRequest, output=public_dot_chat__pb2.GetAPIChatAnswerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_a_p_i_chat_answer), '/textql.rpc.public.chat.ChatService/GetChats': EndpointSync.unary(method=MethodInfo(name='GetChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatsRequest, output=public_dot_chat__pb2.GetChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_chats), '/textql.rpc.public.chat.ChatService/GetChat': EndpointSync.unary(method=MethodInfo(name='GetChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatRequest, output=public_dot_chat__pb2.GetChatResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_chat), '/textql.rpc.public.chat.ChatService/GetPlaybookChats': EndpointSync.unary(method=MethodInfo(name='GetPlaybookChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetPlaybookChatsRequest, output=public_dot_chat__pb2.GetPlaybookChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_playbook_chats), '/textql.rpc.public.chat.ChatService/GetMembersWithChats': EndpointSync.unary(method=MethodInfo(name='GetMembersWithChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetMembersWithChatsRequest, output=public_dot_chat__pb2.GetMembersWithChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_members_with_chats), '/textql.rpc.public.chat.ChatService/GetCompletionParameters': EndpointSync.unary(method=MethodInfo(name='GetCompletionParameters', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersRequest, output=public_dot_chat__pb2.GetCompletionParametersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_completion_parameters), '/textql.rpc.public.chat.ChatService/GetCompletionParametersBatch': EndpointSync.unary(method=MethodInfo(name='GetCompletionParametersBatch', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersBatchRequest, output=public_dot_chat__pb2.GetCompletionParametersBatchResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_completion_parameters_batch), '/textql.rpc.public.chat.ChatService/GetChatExecutionTiming': EndpointSync.unary(method=MethodInfo(name='GetChatExecutionTiming', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatExecutionTimingRequest, output=public_dot_chat__pb2.GetChatExecutionTimingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_chat_execution_timing), '/textql.rpc.public.chat.ChatService/CheckChatPermissions': EndpointSync.unary(method=MethodInfo(name='CheckChatPermissions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckChatPermissionsRequest, output=public_dot_chat__pb2.CheckChatPermissionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.check_chat_permissions), '/textql.rpc.public.chat.ChatService/GetLlmUsage': EndpointSync.unary(method=MethodInfo(name='GetLlmUsage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetLlmUsageRequest, output=public_dot_chat__pb2.GetLlmUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_llm_usage), '/textql.rpc.public.chat.ChatService/ApproveContextPromptChange': EndpointSync.unary(method=MethodInfo(name='ApproveContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveContextPromptChangeRequest, output=public_dot_chat__pb2.ApproveContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.approve_context_prompt_change), '/textql.rpc.public.chat.ChatService/RejectContextPromptChange': EndpointSync.unary(method=MethodInfo(name='RejectContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectContextPromptChangeRequest, output=public_dot_chat__pb2.RejectContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.reject_context_prompt_change), '/textql.rpc.public.chat.ChatService/SubmitContextPromptChange': EndpointSync.unary(method=MethodInfo(name='SubmitContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitContextPromptChangeRequest, output=public_dot_chat__pb2.SubmitContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.submit_context_prompt_change), '/textql.rpc.public.chat.ChatService/SubmitQuestions': EndpointSync.unary(method=MethodInfo(name='SubmitQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitQuestionsRequest, output=public_dot_chat__pb2.SubmitQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.submit_questions), '/textql.rpc.public.chat.ChatService/DismissQuestions': EndpointSync.unary(method=MethodInfo(name='DismissQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissQuestionsRequest, output=public_dot_chat__pb2.DismissQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.dismiss_questions), '/textql.rpc.public.chat.ChatService/SubmitFormApproval': EndpointSync.unary(method=MethodInfo(name='SubmitFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitFormApprovalRequest, output=public_dot_chat__pb2.SubmitFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.submit_form_approval), '/textql.rpc.public.chat.ChatService/RejectFormApproval': EndpointSync.unary(method=MethodInfo(name='RejectFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectFormApprovalRequest, output=public_dot_chat__pb2.RejectFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.reject_form_approval), '/textql.rpc.public.chat.ChatService/DismissFormApproval': EndpointSync.unary(method=MethodInfo(name='DismissFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissFormApprovalRequest, output=public_dot_chat__pb2.DismissFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.dismiss_form_approval), '/textql.rpc.public.chat.ChatService/ResumeChatAfterAuth': EndpointSync.unary(method=MethodInfo(name='ResumeChatAfterAuth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ResumeChatAfterAuthRequest, output=public_dot_chat__pb2.ResumeChatAfterAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.resume_chat_after_auth), '/textql.rpc.public.chat.ChatService/GrantSandboxOAuthPermission': EndpointSync.unary(method=MethodInfo(name='GrantSandboxOAuthPermission', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, output=public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.grant_sandbox_o_auth_permission), '/textql.rpc.public.chat.ChatService/GetCellAuthStatus': EndpointSync.unary(method=MethodInfo(name='GetCellAuthStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellAuthStatusRequest, output=public_dot_chat__pb2.GetCellAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_cell_auth_status), '/textql.rpc.public.chat.ChatService/ApproveOntologyChange': EndpointSync.unary(method=MethodInfo(name='ApproveOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveOntologyChangeRequest, output=public_dot_chat__pb2.ApproveOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.approve_ontology_change), '/textql.rpc.public.chat.ChatService/RejectOntologyChange': EndpointSync.unary(method=MethodInfo(name='RejectOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectOntologyChangeRequest, output=public_dot_chat__pb2.RejectOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.reject_ontology_change), '/textql.rpc.public.chat.ChatService/QueryOneShot': EndpointSync.unary(method=MethodInfo(name='QueryOneShot', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.QueryOneShotRequest, output=public_dot_chat__pb2.QueryOneShotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.query_one_shot), '/textql.rpc.public.chat.ChatService/CheckStreamlitHealth': EndpointSync.unary(method=MethodInfo(name='CheckStreamlitHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckStreamlitHealthRequest, output=public_dot_chat__pb2.CheckStreamlitHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.check_streamlit_health), '/textql.rpc.public.chat.ChatService/UpdateFormStatus': EndpointSync.unary(method=MethodInfo(name='UpdateFormStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormStatusRequest, output=public_dot_chat__pb2.UpdateFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_form_status), '/textql.rpc.public.chat.ChatService/UpdateFormFields': EndpointSync.unary(method=MethodInfo(name='UpdateFormFields', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormFieldsRequest, output=public_dot_chat__pb2.UpdateFormFieldsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_form_fields), '/textql.rpc.public.chat.ChatService/UpdateFormValidationError': EndpointSync.unary(method=MethodInfo(name='UpdateFormValidationError', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormValidationErrorRequest, output=public_dot_chat__pb2.UpdateFormValidationErrorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_form_validation_error), '/textql.rpc.public.chat.ChatService/SetFormSubmitResult': EndpointSync.unary(method=MethodInfo(name='SetFormSubmitResult', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SetFormSubmitResultRequest, output=public_dot_chat__pb2.SetFormSubmitResultResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_form_submit_result), '/textql.rpc.public.chat.ChatService/GetCell': EndpointSync.unary(method=MethodInfo(name='GetCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellRequest, output=public_dot_chat__pb2.GetCellResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_cell), '/textql.rpc.public.chat.ChatService/BookmarkChat': EndpointSync.unary(method=MethodInfo(name='BookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.BookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.bookmark_chat), '/textql.rpc.public.chat.ChatService/UnbookmarkChat': EndpointSync.unary(method=MethodInfo(name='UnbookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UnbookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.unbookmark_chat), '/textql.rpc.public.chat.ChatService/MarkChatRead': EndpointSync.unary(method=MethodInfo(name='MarkChatRead', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatReadRequest, output=public_dot_chat__pb2.MarkChatReadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.mark_chat_read), '/textql.rpc.public.chat.ChatService/MarkChatUnread': EndpointSync.unary(method=MethodInfo(name='MarkChatUnread', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatUnreadRequest, output=public_dot_chat__pb2.MarkChatUnreadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.mark_chat_unread), '/textql.rpc.public.chat.ChatService/GetChatArtifactsSummary': EndpointSync.unary(method=MethodInfo(name='GetChatArtifactsSummary', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatArtifactsSummaryRequest, output=public_dot_chat__pb2.GetChatArtifactsSummaryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_chat_artifacts_summary), '/textql.rpc.public.chat.ChatService/GetArtifact': EndpointSync.unary(method=MethodInfo(name='GetArtifact', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetArtifactRequest, output=public_dot_chat__pb2.GetArtifactResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_artifact), '/textql.rpc.public.chat.ChatService/AttachAgentToChat': EndpointSync.unary(method=MethodInfo(name='AttachAgentToChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAgentToChatRequest, output=public_dot_chat__pb2.AttachAgentToChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.attach_agent_to_chat)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.chat.ChatService'

class ChatServiceClientSync(ConnectClientSync):

    def create_chat(self, request: public_dot_chat__pb2.CreateRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CreateResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CreateRequest, output=public_dot_chat__pb2.CreateResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_chat(self, request: public_dot_chat__pb2.UpdateChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateChatResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateChatRequest, output=public_dot_chat__pb2.UpdateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_chat(self, request: public_dot_chat__pb2.DeleteChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DeleteChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def duplicate_chat(self, request: public_dot_chat__pb2.DuplicateChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.DuplicateChatResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DuplicateChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DuplicateChatRequest, output=public_dot_chat__pb2.DuplicateChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def watch_chat(self, request: public_dot_chat__pb2.WatchChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> Iterator[public_dot_chat__pb2.WatchChatEvent]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='WatchChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.WatchChatRequest, output=public_dot_chat__pb2.WatchChatEvent, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def poll_chat_events(self, request: public_dot_chat__pb2.PollChatEventsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.PollChatEventsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='PollChatEvents', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.PollChatEventsRequest, output=public_dot_chat__pb2.PollChatEventsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_chat(self, request: public_dot_chat__pb2.RunChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> Iterator[public_dot_chat__pb2.Cell]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.Cell, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def cancel_stream(self, request: public_dot_chat__pb2.CancelStreamRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CancelStreamResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CancelStream', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CancelStreamRequest, output=public_dot_chat__pb2.CancelStreamResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def run_chat(self, request: public_dot_chat__pb2.RunChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RunChatResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RunChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RunChatRequest, output=public_dot_chat__pb2.RunChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def send_message(self, request: public_dot_chat__pb2.SendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SendResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SendMessage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SendRequest, output=public_dot_chat__pb2.SendResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def check_health(self, request: public_dot_chat__pb2.CheckHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CheckHealthResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CheckHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckHealthRequest, output=public_dot_chat__pb2.CheckHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def rate_chat_cell(self, request: public_dot_chat__pb2.RateChatCellRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='RateChatCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RateChatCellRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def attach_dataset(self, request: public_dot_chat__pb2.AttachDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachDatasetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AttachDataset', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDatasetRequest, output=public_dot_chat__pb2.AttachDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def attach_dashboard(self, request: public_dot_chat__pb2.AttachDashboardRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachDashboardResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AttachDashboard', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachDashboardRequest, output=public_dot_chat__pb2.AttachDashboardResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def attach_app(self, request: public_dot_chat__pb2.AttachAppRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachAppResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AttachApp', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAppRequest, output=public_dot_chat__pb2.AttachAppResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_chat_history(self, request: public_dot_chat__pb2.HistoryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.HistoryResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetChatHistory', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.HistoryRequest, output=public_dot_chat__pb2.HistoryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_a_p_i_chat_answer(self, request: public_dot_chat__pb2.GetAPIChatAnswerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetAPIChatAnswerResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetAPIChatAnswer', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetAPIChatAnswerRequest, output=public_dot_chat__pb2.GetAPIChatAnswerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_chats(self, request: public_dot_chat__pb2.GetChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatsRequest, output=public_dot_chat__pb2.GetChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_chat(self, request: public_dot_chat__pb2.GetChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatRequest, output=public_dot_chat__pb2.GetChatResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_playbook_chats(self, request: public_dot_chat__pb2.GetPlaybookChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetPlaybookChatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetPlaybookChatsRequest, output=public_dot_chat__pb2.GetPlaybookChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_members_with_chats(self, request: public_dot_chat__pb2.GetMembersWithChatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetMembersWithChatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithChats', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetMembersWithChatsRequest, output=public_dot_chat__pb2.GetMembersWithChatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_completion_parameters(self, request: public_dot_chat__pb2.GetCompletionParametersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCompletionParametersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCompletionParameters', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersRequest, output=public_dot_chat__pb2.GetCompletionParametersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_completion_parameters_batch(self, request: public_dot_chat__pb2.GetCompletionParametersBatchRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCompletionParametersBatchResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCompletionParametersBatch', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCompletionParametersBatchRequest, output=public_dot_chat__pb2.GetCompletionParametersBatchResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_chat_execution_timing(self, request: public_dot_chat__pb2.GetChatExecutionTimingRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatExecutionTimingResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetChatExecutionTiming', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatExecutionTimingRequest, output=public_dot_chat__pb2.GetChatExecutionTimingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def check_chat_permissions(self, request: public_dot_chat__pb2.CheckChatPermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.CheckChatPermissionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CheckChatPermissions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckChatPermissionsRequest, output=public_dot_chat__pb2.CheckChatPermissionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_llm_usage(self, request: public_dot_chat__pb2.GetLlmUsageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetLlmUsageResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetLlmUsage', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetLlmUsageRequest, output=public_dot_chat__pb2.GetLlmUsageResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def approve_context_prompt_change(self, request: public_dot_chat__pb2.ApproveContextPromptChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.ApproveContextPromptChangeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ApproveContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveContextPromptChangeRequest, output=public_dot_chat__pb2.ApproveContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def reject_context_prompt_change(self, request: public_dot_chat__pb2.RejectContextPromptChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RejectContextPromptChangeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RejectContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectContextPromptChangeRequest, output=public_dot_chat__pb2.RejectContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def submit_context_prompt_change(self, request: public_dot_chat__pb2.SubmitContextPromptChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SubmitContextPromptChangeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SubmitContextPromptChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitContextPromptChangeRequest, output=public_dot_chat__pb2.SubmitContextPromptChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def submit_questions(self, request: public_dot_chat__pb2.SubmitQuestionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SubmitQuestionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SubmitQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitQuestionsRequest, output=public_dot_chat__pb2.SubmitQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def dismiss_questions(self, request: public_dot_chat__pb2.DismissQuestionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.DismissQuestionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DismissQuestions', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissQuestionsRequest, output=public_dot_chat__pb2.DismissQuestionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def submit_form_approval(self, request: public_dot_chat__pb2.SubmitFormApprovalRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SubmitFormApprovalResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SubmitFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SubmitFormApprovalRequest, output=public_dot_chat__pb2.SubmitFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def reject_form_approval(self, request: public_dot_chat__pb2.RejectFormApprovalRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RejectFormApprovalResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RejectFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectFormApprovalRequest, output=public_dot_chat__pb2.RejectFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def dismiss_form_approval(self, request: public_dot_chat__pb2.DismissFormApprovalRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.DismissFormApprovalResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DismissFormApproval', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.DismissFormApprovalRequest, output=public_dot_chat__pb2.DismissFormApprovalResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def resume_chat_after_auth(self, request: public_dot_chat__pb2.ResumeChatAfterAuthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.ResumeChatAfterAuthResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ResumeChatAfterAuth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ResumeChatAfterAuthRequest, output=public_dot_chat__pb2.ResumeChatAfterAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def grant_sandbox_o_auth_permission(self, request: public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GrantSandboxOAuthPermission', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GrantSandboxOAuthPermissionRequest, output=public_dot_chat__pb2.GrantSandboxOAuthPermissionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_cell_auth_status(self, request: public_dot_chat__pb2.GetCellAuthStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCellAuthStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCellAuthStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellAuthStatusRequest, output=public_dot_chat__pb2.GetCellAuthStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def approve_ontology_change(self, request: public_dot_chat__pb2.ApproveOntologyChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.ApproveOntologyChangeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ApproveOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.ApproveOntologyChangeRequest, output=public_dot_chat__pb2.ApproveOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def reject_ontology_change(self, request: public_dot_chat__pb2.RejectOntologyChangeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.RejectOntologyChangeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RejectOntologyChange', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.RejectOntologyChangeRequest, output=public_dot_chat__pb2.RejectOntologyChangeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def query_one_shot(self, request: public_dot_chat__pb2.QueryOneShotRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.QueryOneShotResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='QueryOneShot', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.QueryOneShotRequest, output=public_dot_chat__pb2.QueryOneShotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def check_streamlit_health(self, request: public_dot_chat__pb2.CheckStreamlitHealthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.CheckStreamlitHealthResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CheckStreamlitHealth', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.CheckStreamlitHealthRequest, output=public_dot_chat__pb2.CheckStreamlitHealthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_form_status(self, request: public_dot_chat__pb2.UpdateFormStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateFormStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateFormStatus', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormStatusRequest, output=public_dot_chat__pb2.UpdateFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_form_fields(self, request: public_dot_chat__pb2.UpdateFormFieldsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateFormFieldsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateFormFields', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormFieldsRequest, output=public_dot_chat__pb2.UpdateFormFieldsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_form_validation_error(self, request: public_dot_chat__pb2.UpdateFormValidationErrorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.UpdateFormValidationErrorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateFormValidationError', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UpdateFormValidationErrorRequest, output=public_dot_chat__pb2.UpdateFormValidationErrorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def set_form_submit_result(self, request: public_dot_chat__pb2.SetFormSubmitResultRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.SetFormSubmitResultResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SetFormSubmitResult', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.SetFormSubmitResultRequest, output=public_dot_chat__pb2.SetFormSubmitResultResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_cell(self, request: public_dot_chat__pb2.GetCellRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetCellResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCell', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetCellRequest, output=public_dot_chat__pb2.GetCellResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def bookmark_chat(self, request: public_dot_chat__pb2.BookmarkChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='BookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.BookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def unbookmark_chat(self, request: public_dot_chat__pb2.UnbookmarkChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='UnbookmarkChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.UnbookmarkChatRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def mark_chat_read(self, request: public_dot_chat__pb2.MarkChatReadRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.MarkChatReadResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='MarkChatRead', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatReadRequest, output=public_dot_chat__pb2.MarkChatReadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def mark_chat_unread(self, request: public_dot_chat__pb2.MarkChatUnreadRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.MarkChatUnreadResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='MarkChatUnread', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.MarkChatUnreadRequest, output=public_dot_chat__pb2.MarkChatUnreadResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_chat_artifacts_summary(self, request: public_dot_chat__pb2.GetChatArtifactsSummaryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetChatArtifactsSummaryResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetChatArtifactsSummary', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetChatArtifactsSummaryRequest, output=public_dot_chat__pb2.GetChatArtifactsSummaryResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_artifact(self, request: public_dot_chat__pb2.GetArtifactRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_chat__pb2.GetArtifactResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetArtifact', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.GetArtifactRequest, output=public_dot_chat__pb2.GetArtifactResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def attach_agent_to_chat(self, request: public_dot_chat__pb2.AttachAgentToChatRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_chat__pb2.AttachAgentToChatResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AttachAgentToChat', service_name='textql.rpc.public.chat.ChatService', input=public_dot_chat__pb2.AttachAgentToChatRequest, output=public_dot_chat__pb2.AttachAgentToChatResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)