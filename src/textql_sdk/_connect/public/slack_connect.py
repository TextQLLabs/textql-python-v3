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
from . import slack_pb2 as public_dot_slack__pb2

class SlackService(Protocol):

    async def sync_workspace(self, request: public_dot_slack__pb2.SyncWorkspaceRequest, ctx: RequestContext) -> public_dot_slack__pb2.SyncWorkspaceResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.ListInstallationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.GetCurrentUserResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.ListChannelsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.ListUsersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_installation(self, request: public_dot_slack__pb2.DeleteInstallationRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_slack_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.CreateSlackUuidResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def handle_slack_o_auth_callback(self, request: public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, ctx: RequestContext) -> public_dot_slack__pb2.HandleSlackOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SlackServiceASGIApplication(ConnectASGIApplication[SlackService]):

    def __init__(self, service: SlackService | AsyncGenerator[SlackService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.slack.SlackService/SyncWorkspace': Endpoint.unary(method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.SyncWorkspaceRequest, output=public_dot_slack__pb2.SyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.sync_workspace), '/textql.rpc.public.slack.SlackService/ListInstallations': Endpoint.unary(method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_installations), '/textql.rpc.public.slack.SlackService/GetCurrentUser': Endpoint.unary(method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.GetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_current_user), '/textql.rpc.public.slack.SlackService/ListChannels': Endpoint.unary(method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_channels), '/textql.rpc.public.slack.SlackService/ListUsers': Endpoint.unary(method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_users), '/textql.rpc.public.slack.SlackService/DeleteInstallation': Endpoint.unary(method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.DeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_installation), '/textql.rpc.public.slack.SlackService/CreateSlackUuid': Endpoint.unary(method=MethodInfo(name='CreateSlackUuid', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.CreateSlackUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_slack_uuid), '/textql.rpc.public.slack.SlackService/HandleSlackOAuthCallback': Endpoint.unary(method=MethodInfo(name='HandleSlackOAuthCallback', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, output=public_dot_slack__pb2.HandleSlackOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.handle_slack_o_auth_callback)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.slack.SlackService'

class SlackServiceClient(ConnectClient):

    async def sync_workspace(self, request: public_dot_slack__pb2.SyncWorkspaceRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.SyncWorkspaceResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.SyncWorkspaceRequest, output=public_dot_slack__pb2.SyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.ListInstallationsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.GetCurrentUserResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.GetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.ListChannelsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.ListUsersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_installation(self, request: public_dot_slack__pb2.DeleteInstallationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.DeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_slack_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.CreateSlackUuidResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateSlackUuid', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.CreateSlackUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def handle_slack_o_auth_callback(self, request: public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.HandleSlackOAuthCallbackResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='HandleSlackOAuthCallback', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, output=public_dot_slack__pb2.HandleSlackOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SlackServiceSync(Protocol):

    def sync_workspace(self, request: public_dot_slack__pb2.SyncWorkspaceRequest, ctx: RequestContext) -> public_dot_slack__pb2.SyncWorkspaceResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.ListInstallationsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.GetCurrentUserResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.ListChannelsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.ListUsersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_installation(self, request: public_dot_slack__pb2.DeleteInstallationRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_slack_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> public_dot_slack__pb2.CreateSlackUuidResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def handle_slack_o_auth_callback(self, request: public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, ctx: RequestContext) -> public_dot_slack__pb2.HandleSlackOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SlackServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SlackServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.slack.SlackService/SyncWorkspace': EndpointSync.unary(method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.SyncWorkspaceRequest, output=public_dot_slack__pb2.SyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.sync_workspace), '/textql.rpc.public.slack.SlackService/ListInstallations': EndpointSync.unary(method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_installations), '/textql.rpc.public.slack.SlackService/GetCurrentUser': EndpointSync.unary(method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.GetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_current_user), '/textql.rpc.public.slack.SlackService/ListChannels': EndpointSync.unary(method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_channels), '/textql.rpc.public.slack.SlackService/ListUsers': EndpointSync.unary(method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_users), '/textql.rpc.public.slack.SlackService/DeleteInstallation': EndpointSync.unary(method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.DeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_installation), '/textql.rpc.public.slack.SlackService/CreateSlackUuid': EndpointSync.unary(method=MethodInfo(name='CreateSlackUuid', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.CreateSlackUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_slack_uuid), '/textql.rpc.public.slack.SlackService/HandleSlackOAuthCallback': EndpointSync.unary(method=MethodInfo(name='HandleSlackOAuthCallback', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, output=public_dot_slack__pb2.HandleSlackOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.handle_slack_o_auth_callback)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.slack.SlackService'

class SlackServiceClientSync(ConnectClientSync):

    def sync_workspace(self, request: public_dot_slack__pb2.SyncWorkspaceRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.SyncWorkspaceResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SyncWorkspace', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.SyncWorkspaceRequest, output=public_dot_slack__pb2.SyncWorkspaceResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_installations(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.ListInstallationsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListInstallations', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListInstallationsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_current_user(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.GetCurrentUserResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCurrentUser', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.GetCurrentUserResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_channels(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.ListChannelsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListChannels', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListChannelsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_users(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.ListUsersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListUsers', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.ListUsersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_installation(self, request: public_dot_slack__pb2.DeleteInstallationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteInstallation', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.DeleteInstallationRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_slack_uuid(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.CreateSlackUuidResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateSlackUuid', service_name='textql.rpc.public.slack.SlackService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=public_dot_slack__pb2.CreateSlackUuidResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def handle_slack_o_auth_callback(self, request: public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_slack__pb2.HandleSlackOAuthCallbackResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='HandleSlackOAuthCallback', service_name='textql.rpc.public.slack.SlackService', input=public_dot_slack__pb2.HandleSlackOAuthCallbackRequest, output=public_dot_slack__pb2.HandleSlackOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)