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
from . import agent_pb2 as public_dot_agent__pb2

class AgentService(Protocol):

    async def create_agent(self, request: public_dot_agent__pb2.CreateAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.CreateAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_agent(self, request: public_dot_agent__pb2.UpdateAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.UpdateAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_agents(self, request: public_dot_agent__pb2.ListAgentsRequest, ctx: RequestContext) -> public_dot_agent__pb2.ListAgentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_agent(self, request: public_dot_agent__pb2.GetAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.GetAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_agent(self, request: public_dot_agent__pb2.DeleteAgentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def trigger_agent(self, request: public_dot_agent__pb2.TriggerAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.TriggerAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def trigger_agent_comment(self, request: public_dot_agent__pb2.TriggerAgentCommentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def duplicate_agent(self, request: public_dot_agent__pb2.DuplicateAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.DuplicateAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def seed_organization(self, request: public_dot_agent__pb2.SeedOrganizationRequest, ctx: RequestContext) -> public_dot_agent__pb2.SeedOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_agent_status(self, request: public_dot_agent__pb2.StreamAgentStatusRequest, ctx: RequestContext) -> AsyncIterator[public_dot_agent__pb2.AgentStatusUpdate]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_agent_runs(self, request: public_dot_agent__pb2.ListAgentRunsRequest, ctx: RequestContext) -> public_dot_agent__pb2.ListAgentRunsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_agent_run(self, request: public_dot_agent__pb2.GetAgentRunRequest, ctx: RequestContext) -> public_dot_agent__pb2.GetAgentRunResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_agent_runs_for_thing(self, request: public_dot_agent__pb2.ListAgentRunsForThingRequest, ctx: RequestContext) -> public_dot_agent__pb2.ListAgentRunsForThingResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def upload_agent_avatar(self, request: public_dot_agent__pb2.UploadAgentAvatarRequest, ctx: RequestContext) -> public_dot_agent__pb2.UploadAgentAvatarResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def reset_agent_avatar(self, request: public_dot_agent__pb2.ResetAgentAvatarRequest, ctx: RequestContext) -> public_dot_agent__pb2.ResetAgentAvatarResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AgentServiceASGIApplication(ConnectASGIApplication[AgentService]):

    def __init__(self, service: AgentService | AsyncGenerator[AgentService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.agent.AgentService/CreateAgent': Endpoint.unary(method=MethodInfo(name='CreateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.CreateAgentRequest, output=public_dot_agent__pb2.CreateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_agent), '/textql.rpc.public.agent.AgentService/UpdateAgent': Endpoint.unary(method=MethodInfo(name='UpdateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UpdateAgentRequest, output=public_dot_agent__pb2.UpdateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_agent), '/textql.rpc.public.agent.AgentService/ListAgents': Endpoint.unary(method=MethodInfo(name='ListAgents', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentsRequest, output=public_dot_agent__pb2.ListAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_agents), '/textql.rpc.public.agent.AgentService/GetAgent': Endpoint.unary(method=MethodInfo(name='GetAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRequest, output=public_dot_agent__pb2.GetAgentResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_agent), '/textql.rpc.public.agent.AgentService/DeleteAgent': Endpoint.unary(method=MethodInfo(name='DeleteAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DeleteAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_agent), '/textql.rpc.public.agent.AgentService/TriggerAgent': Endpoint.unary(method=MethodInfo(name='TriggerAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentRequest, output=public_dot_agent__pb2.TriggerAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.trigger_agent), '/textql.rpc.public.agent.AgentService/TriggerAgentComment': Endpoint.unary(method=MethodInfo(name='TriggerAgentComment', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.trigger_agent_comment), '/textql.rpc.public.agent.AgentService/DuplicateAgent': Endpoint.unary(method=MethodInfo(name='DuplicateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DuplicateAgentRequest, output=public_dot_agent__pb2.DuplicateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.duplicate_agent), '/textql.rpc.public.agent.AgentService/SeedOrganization': Endpoint.unary(method=MethodInfo(name='SeedOrganization', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.SeedOrganizationRequest, output=public_dot_agent__pb2.SeedOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.seed_organization), '/textql.rpc.public.agent.AgentService/StreamAgentStatus': Endpoint.server_stream(method=MethodInfo(name='StreamAgentStatus', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.StreamAgentStatusRequest, output=public_dot_agent__pb2.AgentStatusUpdate, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.stream_agent_status), '/textql.rpc.public.agent.AgentService/ListAgentRuns': Endpoint.unary(method=MethodInfo(name='ListAgentRuns', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsRequest, output=public_dot_agent__pb2.ListAgentRunsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_agent_runs), '/textql.rpc.public.agent.AgentService/GetAgentRun': Endpoint.unary(method=MethodInfo(name='GetAgentRun', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRunRequest, output=public_dot_agent__pb2.GetAgentRunResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_agent_run), '/textql.rpc.public.agent.AgentService/ListAgentRunsForThing': Endpoint.unary(method=MethodInfo(name='ListAgentRunsForThing', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsForThingRequest, output=public_dot_agent__pb2.ListAgentRunsForThingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_agent_runs_for_thing), '/textql.rpc.public.agent.AgentService/UploadAgentAvatar': Endpoint.unary(method=MethodInfo(name='UploadAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UploadAgentAvatarRequest, output=public_dot_agent__pb2.UploadAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.upload_agent_avatar), '/textql.rpc.public.agent.AgentService/ResetAgentAvatar': Endpoint.unary(method=MethodInfo(name='ResetAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ResetAgentAvatarRequest, output=public_dot_agent__pb2.ResetAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.reset_agent_avatar)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.agent.AgentService'

class AgentServiceClient(ConnectClient):

    async def create_agent(self, request: public_dot_agent__pb2.CreateAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.CreateAgentResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.CreateAgentRequest, output=public_dot_agent__pb2.CreateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_agent(self, request: public_dot_agent__pb2.UpdateAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.UpdateAgentResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UpdateAgentRequest, output=public_dot_agent__pb2.UpdateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_agents(self, request: public_dot_agent__pb2.ListAgentsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.ListAgentsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListAgents', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentsRequest, output=public_dot_agent__pb2.ListAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_agent(self, request: public_dot_agent__pb2.GetAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.GetAgentResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRequest, output=public_dot_agent__pb2.GetAgentResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def delete_agent(self, request: public_dot_agent__pb2.DeleteAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DeleteAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def trigger_agent(self, request: public_dot_agent__pb2.TriggerAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.TriggerAgentResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TriggerAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentRequest, output=public_dot_agent__pb2.TriggerAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def trigger_agent_comment(self, request: public_dot_agent__pb2.TriggerAgentCommentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='TriggerAgentComment', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def duplicate_agent(self, request: public_dot_agent__pb2.DuplicateAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.DuplicateAgentResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DuplicateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DuplicateAgentRequest, output=public_dot_agent__pb2.DuplicateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def seed_organization(self, request: public_dot_agent__pb2.SeedOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.SeedOrganizationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SeedOrganization', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.SeedOrganizationRequest, output=public_dot_agent__pb2.SeedOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_agent_status(self, request: public_dot_agent__pb2.StreamAgentStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> AsyncIterator[public_dot_agent__pb2.AgentStatusUpdate]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamAgentStatus', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.StreamAgentStatusRequest, output=public_dot_agent__pb2.AgentStatusUpdate, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_agent_runs(self, request: public_dot_agent__pb2.ListAgentRunsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.ListAgentRunsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListAgentRuns', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsRequest, output=public_dot_agent__pb2.ListAgentRunsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_agent_run(self, request: public_dot_agent__pb2.GetAgentRunRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.GetAgentRunResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetAgentRun', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRunRequest, output=public_dot_agent__pb2.GetAgentRunResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_agent_runs_for_thing(self, request: public_dot_agent__pb2.ListAgentRunsForThingRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.ListAgentRunsForThingResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListAgentRunsForThing', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsForThingRequest, output=public_dot_agent__pb2.ListAgentRunsForThingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def upload_agent_avatar(self, request: public_dot_agent__pb2.UploadAgentAvatarRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.UploadAgentAvatarResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UploadAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UploadAgentAvatarRequest, output=public_dot_agent__pb2.UploadAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def reset_agent_avatar(self, request: public_dot_agent__pb2.ResetAgentAvatarRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.ResetAgentAvatarResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ResetAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ResetAgentAvatarRequest, output=public_dot_agent__pb2.ResetAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class AgentServiceSync(Protocol):

    def create_agent(self, request: public_dot_agent__pb2.CreateAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.CreateAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_agent(self, request: public_dot_agent__pb2.UpdateAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.UpdateAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_agents(self, request: public_dot_agent__pb2.ListAgentsRequest, ctx: RequestContext) -> public_dot_agent__pb2.ListAgentsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_agent(self, request: public_dot_agent__pb2.GetAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.GetAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_agent(self, request: public_dot_agent__pb2.DeleteAgentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def trigger_agent(self, request: public_dot_agent__pb2.TriggerAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.TriggerAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def trigger_agent_comment(self, request: public_dot_agent__pb2.TriggerAgentCommentRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def duplicate_agent(self, request: public_dot_agent__pb2.DuplicateAgentRequest, ctx: RequestContext) -> public_dot_agent__pb2.DuplicateAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def seed_organization(self, request: public_dot_agent__pb2.SeedOrganizationRequest, ctx: RequestContext) -> public_dot_agent__pb2.SeedOrganizationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stream_agent_status(self, request: public_dot_agent__pb2.StreamAgentStatusRequest, ctx: RequestContext) -> Iterator[public_dot_agent__pb2.AgentStatusUpdate]:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_agent_runs(self, request: public_dot_agent__pb2.ListAgentRunsRequest, ctx: RequestContext) -> public_dot_agent__pb2.ListAgentRunsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_agent_run(self, request: public_dot_agent__pb2.GetAgentRunRequest, ctx: RequestContext) -> public_dot_agent__pb2.GetAgentRunResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_agent_runs_for_thing(self, request: public_dot_agent__pb2.ListAgentRunsForThingRequest, ctx: RequestContext) -> public_dot_agent__pb2.ListAgentRunsForThingResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def upload_agent_avatar(self, request: public_dot_agent__pb2.UploadAgentAvatarRequest, ctx: RequestContext) -> public_dot_agent__pb2.UploadAgentAvatarResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def reset_agent_avatar(self, request: public_dot_agent__pb2.ResetAgentAvatarRequest, ctx: RequestContext) -> public_dot_agent__pb2.ResetAgentAvatarResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class AgentServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: AgentServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.agent.AgentService/CreateAgent': EndpointSync.unary(method=MethodInfo(name='CreateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.CreateAgentRequest, output=public_dot_agent__pb2.CreateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_agent), '/textql.rpc.public.agent.AgentService/UpdateAgent': EndpointSync.unary(method=MethodInfo(name='UpdateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UpdateAgentRequest, output=public_dot_agent__pb2.UpdateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_agent), '/textql.rpc.public.agent.AgentService/ListAgents': EndpointSync.unary(method=MethodInfo(name='ListAgents', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentsRequest, output=public_dot_agent__pb2.ListAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_agents), '/textql.rpc.public.agent.AgentService/GetAgent': EndpointSync.unary(method=MethodInfo(name='GetAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRequest, output=public_dot_agent__pb2.GetAgentResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_agent), '/textql.rpc.public.agent.AgentService/DeleteAgent': EndpointSync.unary(method=MethodInfo(name='DeleteAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DeleteAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_agent), '/textql.rpc.public.agent.AgentService/TriggerAgent': EndpointSync.unary(method=MethodInfo(name='TriggerAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentRequest, output=public_dot_agent__pb2.TriggerAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.trigger_agent), '/textql.rpc.public.agent.AgentService/TriggerAgentComment': EndpointSync.unary(method=MethodInfo(name='TriggerAgentComment', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.trigger_agent_comment), '/textql.rpc.public.agent.AgentService/DuplicateAgent': EndpointSync.unary(method=MethodInfo(name='DuplicateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DuplicateAgentRequest, output=public_dot_agent__pb2.DuplicateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.duplicate_agent), '/textql.rpc.public.agent.AgentService/SeedOrganization': EndpointSync.unary(method=MethodInfo(name='SeedOrganization', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.SeedOrganizationRequest, output=public_dot_agent__pb2.SeedOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.seed_organization), '/textql.rpc.public.agent.AgentService/StreamAgentStatus': EndpointSync.server_stream(method=MethodInfo(name='StreamAgentStatus', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.StreamAgentStatusRequest, output=public_dot_agent__pb2.AgentStatusUpdate, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.stream_agent_status), '/textql.rpc.public.agent.AgentService/ListAgentRuns': EndpointSync.unary(method=MethodInfo(name='ListAgentRuns', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsRequest, output=public_dot_agent__pb2.ListAgentRunsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_agent_runs), '/textql.rpc.public.agent.AgentService/GetAgentRun': EndpointSync.unary(method=MethodInfo(name='GetAgentRun', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRunRequest, output=public_dot_agent__pb2.GetAgentRunResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_agent_run), '/textql.rpc.public.agent.AgentService/ListAgentRunsForThing': EndpointSync.unary(method=MethodInfo(name='ListAgentRunsForThing', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsForThingRequest, output=public_dot_agent__pb2.ListAgentRunsForThingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_agent_runs_for_thing), '/textql.rpc.public.agent.AgentService/UploadAgentAvatar': EndpointSync.unary(method=MethodInfo(name='UploadAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UploadAgentAvatarRequest, output=public_dot_agent__pb2.UploadAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.upload_agent_avatar), '/textql.rpc.public.agent.AgentService/ResetAgentAvatar': EndpointSync.unary(method=MethodInfo(name='ResetAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ResetAgentAvatarRequest, output=public_dot_agent__pb2.ResetAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.reset_agent_avatar)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.agent.AgentService'

class AgentServiceClientSync(ConnectClientSync):

    def create_agent(self, request: public_dot_agent__pb2.CreateAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.CreateAgentResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.CreateAgentRequest, output=public_dot_agent__pb2.CreateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_agent(self, request: public_dot_agent__pb2.UpdateAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.UpdateAgentResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UpdateAgentRequest, output=public_dot_agent__pb2.UpdateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_agents(self, request: public_dot_agent__pb2.ListAgentsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.ListAgentsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListAgents', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentsRequest, output=public_dot_agent__pb2.ListAgentsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_agent(self, request: public_dot_agent__pb2.GetAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.GetAgentResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRequest, output=public_dot_agent__pb2.GetAgentResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def delete_agent(self, request: public_dot_agent__pb2.DeleteAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DeleteAgentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def trigger_agent(self, request: public_dot_agent__pb2.TriggerAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.TriggerAgentResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TriggerAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentRequest, output=public_dot_agent__pb2.TriggerAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def trigger_agent_comment(self, request: public_dot_agent__pb2.TriggerAgentCommentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='TriggerAgentComment', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.TriggerAgentCommentRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def duplicate_agent(self, request: public_dot_agent__pb2.DuplicateAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.DuplicateAgentResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DuplicateAgent', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.DuplicateAgentRequest, output=public_dot_agent__pb2.DuplicateAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def seed_organization(self, request: public_dot_agent__pb2.SeedOrganizationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.SeedOrganizationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SeedOrganization', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.SeedOrganizationRequest, output=public_dot_agent__pb2.SeedOrganizationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def stream_agent_status(self, request: public_dot_agent__pb2.StreamAgentStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> Iterator[public_dot_agent__pb2.AgentStatusUpdate]:
        return self.execute_server_stream(request=request, method=MethodInfo(name='StreamAgentStatus', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.StreamAgentStatusRequest, output=public_dot_agent__pb2.AgentStatusUpdate, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_agent_runs(self, request: public_dot_agent__pb2.ListAgentRunsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.ListAgentRunsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListAgentRuns', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsRequest, output=public_dot_agent__pb2.ListAgentRunsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_agent_run(self, request: public_dot_agent__pb2.GetAgentRunRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.GetAgentRunResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetAgentRun', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.GetAgentRunRequest, output=public_dot_agent__pb2.GetAgentRunResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_agent_runs_for_thing(self, request: public_dot_agent__pb2.ListAgentRunsForThingRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_agent__pb2.ListAgentRunsForThingResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListAgentRunsForThing', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ListAgentRunsForThingRequest, output=public_dot_agent__pb2.ListAgentRunsForThingResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def upload_agent_avatar(self, request: public_dot_agent__pb2.UploadAgentAvatarRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.UploadAgentAvatarResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UploadAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.UploadAgentAvatarRequest, output=public_dot_agent__pb2.UploadAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def reset_agent_avatar(self, request: public_dot_agent__pb2.ResetAgentAvatarRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_agent__pb2.ResetAgentAvatarResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ResetAgentAvatar', service_name='textql.rpc.public.agent.AgentService', input=public_dot_agent__pb2.ResetAgentAvatarRequest, output=public_dot_agent__pb2.ResetAgentAvatarResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)