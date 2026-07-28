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
from . import teams_pb2 as public_dot_teams__pb2

class TeamsService(Protocol):

    async def sync_workspace(self, request: public_dot_teams__pb2.TeamsSyncWorkspaceRequest, ctx: RequestContext) -> public_dot_teams__pb2.TeamsSyncWorkspaceResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsListInstallationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsGetCurrentUserResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsListChannelsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsListUsersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_installation(self, request: public_dot_teams__pb2.TeamsDeleteInstallationRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_teams_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.CreateTeamsUuidResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def handle_teams_o_auth_callback(self, request: public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, ctx: RequestContext) -> public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TeamsServiceASGIApplication(ConnectASGIApplication[TeamsService]):

    def __init__(self, service: TeamsService | AsyncGenerator[TeamsService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.teams.TeamsService/SyncWorkspace': Endpoint.unary(method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsSyncWorkspaceRequest, output=public_dot_teams__pb2.TeamsSyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.sync_workspace), '/textql.rpc.public.teams.TeamsService/ListInstallations': Endpoint.unary(method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_installations), '/textql.rpc.public.teams.TeamsService/GetCurrentUser': Endpoint.unary(method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsGetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_current_user), '/textql.rpc.public.teams.TeamsService/ListChannels': Endpoint.unary(method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_channels), '/textql.rpc.public.teams.TeamsService/ListUsers': Endpoint.unary(method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_users), '/textql.rpc.public.teams.TeamsService/DeleteInstallation': Endpoint.unary(method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsDeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_installation), '/textql.rpc.public.teams.TeamsService/CreateTeamsUuid': Endpoint.unary(method=MethodInfo(name='CreateTeamsUuid', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.CreateTeamsUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_teams_uuid), '/textql.rpc.public.teams.TeamsService/HandleTeamsOAuthCallback': Endpoint.unary(method=MethodInfo(name='HandleTeamsOAuthCallback', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, output=public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.handle_teams_o_auth_callback)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.teams.TeamsService'

class TeamsServiceClient(ConnectClient):

    async def sync_workspace(self, request: public_dot_teams__pb2.TeamsSyncWorkspaceRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsSyncWorkspaceResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsSyncWorkspaceRequest, output=public_dot_teams__pb2.TeamsSyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsListInstallationsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsGetCurrentUserResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsGetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsListChannelsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsListUsersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_installation(self, request: public_dot_teams__pb2.TeamsDeleteInstallationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsDeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_teams_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.CreateTeamsUuidResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateTeamsUuid', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.CreateTeamsUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def handle_teams_o_auth_callback(self, request: public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='HandleTeamsOAuthCallback', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, output=public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class TeamsServiceSync(Protocol):

    def sync_workspace(self, request: public_dot_teams__pb2.TeamsSyncWorkspaceRequest, ctx: RequestContext) -> public_dot_teams__pb2.TeamsSyncWorkspaceResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsListInstallationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsGetCurrentUserResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsListChannelsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.TeamsListUsersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_installation(self, request: public_dot_teams__pb2.TeamsDeleteInstallationRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_teams_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_teams__pb2.CreateTeamsUuidResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def handle_teams_o_auth_callback(self, request: public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, ctx: RequestContext) -> public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TeamsServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: TeamsServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.teams.TeamsService/SyncWorkspace': EndpointSync.unary(method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsSyncWorkspaceRequest, output=public_dot_teams__pb2.TeamsSyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.sync_workspace), '/textql.rpc.public.teams.TeamsService/ListInstallations': EndpointSync.unary(method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_installations), '/textql.rpc.public.teams.TeamsService/GetCurrentUser': EndpointSync.unary(method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsGetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_current_user), '/textql.rpc.public.teams.TeamsService/ListChannels': EndpointSync.unary(method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_channels), '/textql.rpc.public.teams.TeamsService/ListUsers': EndpointSync.unary(method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_users), '/textql.rpc.public.teams.TeamsService/DeleteInstallation': EndpointSync.unary(method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsDeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_installation), '/textql.rpc.public.teams.TeamsService/CreateTeamsUuid': EndpointSync.unary(method=MethodInfo(name='CreateTeamsUuid', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.CreateTeamsUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_teams_uuid), '/textql.rpc.public.teams.TeamsService/HandleTeamsOAuthCallback': EndpointSync.unary(method=MethodInfo(name='HandleTeamsOAuthCallback', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, output=public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.handle_teams_o_auth_callback)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.teams.TeamsService'

class TeamsServiceClientSync(ConnectClientSync):

    def sync_workspace(self, request: public_dot_teams__pb2.TeamsSyncWorkspaceRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsSyncWorkspaceResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsSyncWorkspaceRequest, output=public_dot_teams__pb2.TeamsSyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsListInstallationsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsGetCurrentUserResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsGetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsListChannelsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.TeamsListUsersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.TeamsListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_installation(self, request: public_dot_teams__pb2.TeamsDeleteInstallationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.TeamsDeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_teams_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.CreateTeamsUuidResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateTeamsUuid', service_name='textql.rpc.public.teams.TeamsService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_teams__pb2.CreateTeamsUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def handle_teams_o_auth_callback(self, request: public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='HandleTeamsOAuthCallback', service_name='textql.rpc.public.teams.TeamsService', input=public_dot_teams__pb2.HandleTeamsOAuthCallbackRequest, output=public_dot_teams__pb2.HandleTeamsOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)