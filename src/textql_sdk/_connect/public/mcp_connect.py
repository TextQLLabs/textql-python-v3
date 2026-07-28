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
from . import mcp_pb2 as public_dot_mcp__pb2

class MCPService(Protocol):

    async def get_m_c_p_servers(self, request: public_dot_mcp__pb2.GetMCPServersRequest, ctx: RequestContext) -> public_dot_mcp__pb2.GetMCPServersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def upsert_m_c_p_servers(self, request: public_dot_mcp__pb2.UpsertMCPServersRequest, ctx: RequestContext) -> public_dot_mcp__pb2.UpsertMCPServersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_m_c_p_server(self, request: public_dot_mcp__pb2.DeleteMCPServerRequest, ctx: RequestContext) -> public_dot_mcp__pb2.DeleteMCPServerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def toggle_m_c_p_server(self, request: public_dot_mcp__pb2.ToggleMCPServerRequest, ctx: RequestContext) -> public_dot_mcp__pb2.ToggleMCPServerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def clear_o_auth_token(self, request: public_dot_mcp__pb2.ClearOAuthTokenRequest, ctx: RequestContext) -> public_dot_mcp__pb2.ClearOAuthTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def initiate_o_auth_flow(self, request: public_dot_mcp__pb2.InitiateOAuthFlowRequest, ctx: RequestContext) -> public_dot_mcp__pb2.InitiateOAuthFlowResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def handle_o_auth_callback(self, request: public_dot_mcp__pb2.HandleOAuthCallbackRequest, ctx: RequestContext) -> public_dot_mcp__pb2.HandleOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class MCPServiceASGIApplication(ConnectASGIApplication[MCPService]):

    def __init__(self, service: MCPService | AsyncGenerator[MCPService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.mcp.MCPService/GetMCPServers': Endpoint.unary(method=MethodInfo(name='GetMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.GetMCPServersRequest, output=public_dot_mcp__pb2.GetMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_m_c_p_servers), '/textql.rpc.public.mcp.MCPService/UpsertMCPServers': Endpoint.unary(method=MethodInfo(name='UpsertMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.UpsertMCPServersRequest, output=public_dot_mcp__pb2.UpsertMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.upsert_m_c_p_servers), '/textql.rpc.public.mcp.MCPService/DeleteMCPServer': Endpoint.unary(method=MethodInfo(name='DeleteMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.DeleteMCPServerRequest, output=public_dot_mcp__pb2.DeleteMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_m_c_p_server), '/textql.rpc.public.mcp.MCPService/ToggleMCPServer': Endpoint.unary(method=MethodInfo(name='ToggleMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ToggleMCPServerRequest, output=public_dot_mcp__pb2.ToggleMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.toggle_m_c_p_server), '/textql.rpc.public.mcp.MCPService/ClearOAuthToken': Endpoint.unary(method=MethodInfo(name='ClearOAuthToken', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ClearOAuthTokenRequest, output=public_dot_mcp__pb2.ClearOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.clear_o_auth_token), '/textql.rpc.public.mcp.MCPService/InitiateOAuthFlow': Endpoint.unary(method=MethodInfo(name='InitiateOAuthFlow', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.InitiateOAuthFlowRequest, output=public_dot_mcp__pb2.InitiateOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.initiate_o_auth_flow), '/textql.rpc.public.mcp.MCPService/HandleOAuthCallback': Endpoint.unary(method=MethodInfo(name='HandleOAuthCallback', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.HandleOAuthCallbackRequest, output=public_dot_mcp__pb2.HandleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.handle_o_auth_callback)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.mcp.MCPService'

class MCPServiceClient(ConnectClient):

    async def get_m_c_p_servers(self, request: public_dot_mcp__pb2.GetMCPServersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.GetMCPServersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.GetMCPServersRequest, output=public_dot_mcp__pb2.GetMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def upsert_m_c_p_servers(self, request: public_dot_mcp__pb2.UpsertMCPServersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.UpsertMCPServersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpsertMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.UpsertMCPServersRequest, output=public_dot_mcp__pb2.UpsertMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_m_c_p_server(self, request: public_dot_mcp__pb2.DeleteMCPServerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.DeleteMCPServerResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.DeleteMCPServerRequest, output=public_dot_mcp__pb2.DeleteMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def toggle_m_c_p_server(self, request: public_dot_mcp__pb2.ToggleMCPServerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.ToggleMCPServerResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ToggleMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ToggleMCPServerRequest, output=public_dot_mcp__pb2.ToggleMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def clear_o_auth_token(self, request: public_dot_mcp__pb2.ClearOAuthTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.ClearOAuthTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ClearOAuthToken', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ClearOAuthTokenRequest, output=public_dot_mcp__pb2.ClearOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def initiate_o_auth_flow(self, request: public_dot_mcp__pb2.InitiateOAuthFlowRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.InitiateOAuthFlowResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='InitiateOAuthFlow', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.InitiateOAuthFlowRequest, output=public_dot_mcp__pb2.InitiateOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def handle_o_auth_callback(self, request: public_dot_mcp__pb2.HandleOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.HandleOAuthCallbackResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='HandleOAuthCallback', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.HandleOAuthCallbackRequest, output=public_dot_mcp__pb2.HandleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class MCPServiceSync(Protocol):

    def get_m_c_p_servers(self, request: public_dot_mcp__pb2.GetMCPServersRequest, ctx: RequestContext) -> public_dot_mcp__pb2.GetMCPServersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def upsert_m_c_p_servers(self, request: public_dot_mcp__pb2.UpsertMCPServersRequest, ctx: RequestContext) -> public_dot_mcp__pb2.UpsertMCPServersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_m_c_p_server(self, request: public_dot_mcp__pb2.DeleteMCPServerRequest, ctx: RequestContext) -> public_dot_mcp__pb2.DeleteMCPServerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def toggle_m_c_p_server(self, request: public_dot_mcp__pb2.ToggleMCPServerRequest, ctx: RequestContext) -> public_dot_mcp__pb2.ToggleMCPServerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def clear_o_auth_token(self, request: public_dot_mcp__pb2.ClearOAuthTokenRequest, ctx: RequestContext) -> public_dot_mcp__pb2.ClearOAuthTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def initiate_o_auth_flow(self, request: public_dot_mcp__pb2.InitiateOAuthFlowRequest, ctx: RequestContext) -> public_dot_mcp__pb2.InitiateOAuthFlowResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def handle_o_auth_callback(self, request: public_dot_mcp__pb2.HandleOAuthCallbackRequest, ctx: RequestContext) -> public_dot_mcp__pb2.HandleOAuthCallbackResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class MCPServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: MCPServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.mcp.MCPService/GetMCPServers': EndpointSync.unary(method=MethodInfo(name='GetMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.GetMCPServersRequest, output=public_dot_mcp__pb2.GetMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_m_c_p_servers), '/textql.rpc.public.mcp.MCPService/UpsertMCPServers': EndpointSync.unary(method=MethodInfo(name='UpsertMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.UpsertMCPServersRequest, output=public_dot_mcp__pb2.UpsertMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.upsert_m_c_p_servers), '/textql.rpc.public.mcp.MCPService/DeleteMCPServer': EndpointSync.unary(method=MethodInfo(name='DeleteMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.DeleteMCPServerRequest, output=public_dot_mcp__pb2.DeleteMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_m_c_p_server), '/textql.rpc.public.mcp.MCPService/ToggleMCPServer': EndpointSync.unary(method=MethodInfo(name='ToggleMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ToggleMCPServerRequest, output=public_dot_mcp__pb2.ToggleMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.toggle_m_c_p_server), '/textql.rpc.public.mcp.MCPService/ClearOAuthToken': EndpointSync.unary(method=MethodInfo(name='ClearOAuthToken', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ClearOAuthTokenRequest, output=public_dot_mcp__pb2.ClearOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.clear_o_auth_token), '/textql.rpc.public.mcp.MCPService/InitiateOAuthFlow': EndpointSync.unary(method=MethodInfo(name='InitiateOAuthFlow', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.InitiateOAuthFlowRequest, output=public_dot_mcp__pb2.InitiateOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.initiate_o_auth_flow), '/textql.rpc.public.mcp.MCPService/HandleOAuthCallback': EndpointSync.unary(method=MethodInfo(name='HandleOAuthCallback', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.HandleOAuthCallbackRequest, output=public_dot_mcp__pb2.HandleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.handle_o_auth_callback)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.mcp.MCPService'

class MCPServiceClientSync(ConnectClientSync):

    def get_m_c_p_servers(self, request: public_dot_mcp__pb2.GetMCPServersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.GetMCPServersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.GetMCPServersRequest, output=public_dot_mcp__pb2.GetMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def upsert_m_c_p_servers(self, request: public_dot_mcp__pb2.UpsertMCPServersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.UpsertMCPServersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpsertMCPServers', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.UpsertMCPServersRequest, output=public_dot_mcp__pb2.UpsertMCPServersResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_m_c_p_server(self, request: public_dot_mcp__pb2.DeleteMCPServerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.DeleteMCPServerResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.DeleteMCPServerRequest, output=public_dot_mcp__pb2.DeleteMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def toggle_m_c_p_server(self, request: public_dot_mcp__pb2.ToggleMCPServerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.ToggleMCPServerResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ToggleMCPServer', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ToggleMCPServerRequest, output=public_dot_mcp__pb2.ToggleMCPServerResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def clear_o_auth_token(self, request: public_dot_mcp__pb2.ClearOAuthTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.ClearOAuthTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ClearOAuthToken', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.ClearOAuthTokenRequest, output=public_dot_mcp__pb2.ClearOAuthTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def initiate_o_auth_flow(self, request: public_dot_mcp__pb2.InitiateOAuthFlowRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.InitiateOAuthFlowResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='InitiateOAuthFlow', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.InitiateOAuthFlowRequest, output=public_dot_mcp__pb2.InitiateOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def handle_o_auth_callback(self, request: public_dot_mcp__pb2.HandleOAuthCallbackRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_mcp__pb2.HandleOAuthCallbackResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='HandleOAuthCallback', service_name='textql.rpc.public.mcp.MCPService', input=public_dot_mcp__pb2.HandleOAuthCallbackRequest, output=public_dot_mcp__pb2.HandleOAuthCallbackResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)