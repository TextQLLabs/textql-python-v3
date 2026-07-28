# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
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
from . import scim_pb2 as public_dot_scim__pb2

class ScimService(Protocol):

    async def create_scim_token(self, request: public_dot_scim__pb2.CreateScimTokenRequest, ctx: RequestContext) -> public_dot_scim__pb2.CreateScimTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_scim_tokens(self, request: public_dot_scim__pb2.ListScimTokensRequest, ctx: RequestContext) -> public_dot_scim__pb2.ListScimTokensResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revoke_scim_token(self, request: public_dot_scim__pb2.RevokeScimTokenRequest, ctx: RequestContext) -> public_dot_scim__pb2.RevokeScimTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_scim_o_auth_client(self, request: public_dot_scim__pb2.CreateScimOAuthClientRequest, ctx: RequestContext) -> public_dot_scim__pb2.CreateScimOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_scim_o_auth_clients(self, request: public_dot_scim__pb2.ListScimOAuthClientsRequest, ctx: RequestContext) -> public_dot_scim__pb2.ListScimOAuthClientsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revoke_scim_o_auth_client(self, request: public_dot_scim__pb2.RevokeScimOAuthClientRequest, ctx: RequestContext) -> public_dot_scim__pb2.RevokeScimOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ScimServiceASGIApplication(ConnectASGIApplication[ScimService]):

    def __init__(self, service: ScimService | AsyncGenerator[ScimService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.scim.ScimService/CreateScimToken': Endpoint.unary(method=MethodInfo(name='CreateScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimTokenRequest, output=public_dot_scim__pb2.CreateScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_scim_token), '/textql.rpc.public.scim.ScimService/ListScimTokens': Endpoint.unary(method=MethodInfo(name='ListScimTokens', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimTokensRequest, output=public_dot_scim__pb2.ListScimTokensResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_scim_tokens), '/textql.rpc.public.scim.ScimService/RevokeScimToken': Endpoint.unary(method=MethodInfo(name='RevokeScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimTokenRequest, output=public_dot_scim__pb2.RevokeScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revoke_scim_token), '/textql.rpc.public.scim.ScimService/CreateScimOAuthClient': Endpoint.unary(method=MethodInfo(name='CreateScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimOAuthClientRequest, output=public_dot_scim__pb2.CreateScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_scim_o_auth_client), '/textql.rpc.public.scim.ScimService/ListScimOAuthClients': Endpoint.unary(method=MethodInfo(name='ListScimOAuthClients', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimOAuthClientsRequest, output=public_dot_scim__pb2.ListScimOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_scim_o_auth_clients), '/textql.rpc.public.scim.ScimService/RevokeScimOAuthClient': Endpoint.unary(method=MethodInfo(name='RevokeScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimOAuthClientRequest, output=public_dot_scim__pb2.RevokeScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revoke_scim_o_auth_client)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.scim.ScimService'

class ScimServiceClient(ConnectClient):

    async def create_scim_token(self, request: public_dot_scim__pb2.CreateScimTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.CreateScimTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimTokenRequest, output=public_dot_scim__pb2.CreateScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_scim_tokens(self, request: public_dot_scim__pb2.ListScimTokensRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_scim__pb2.ListScimTokensResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListScimTokens', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimTokensRequest, output=public_dot_scim__pb2.ListScimTokensResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def revoke_scim_token(self, request: public_dot_scim__pb2.RevokeScimTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.RevokeScimTokenResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevokeScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimTokenRequest, output=public_dot_scim__pb2.RevokeScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_scim_o_auth_client(self, request: public_dot_scim__pb2.CreateScimOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.CreateScimOAuthClientResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimOAuthClientRequest, output=public_dot_scim__pb2.CreateScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_scim_o_auth_clients(self, request: public_dot_scim__pb2.ListScimOAuthClientsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_scim__pb2.ListScimOAuthClientsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListScimOAuthClients', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimOAuthClientsRequest, output=public_dot_scim__pb2.ListScimOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def revoke_scim_o_auth_client(self, request: public_dot_scim__pb2.RevokeScimOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.RevokeScimOAuthClientResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevokeScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimOAuthClientRequest, output=public_dot_scim__pb2.RevokeScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class ScimServiceSync(Protocol):

    def create_scim_token(self, request: public_dot_scim__pb2.CreateScimTokenRequest, ctx: RequestContext) -> public_dot_scim__pb2.CreateScimTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_scim_tokens(self, request: public_dot_scim__pb2.ListScimTokensRequest, ctx: RequestContext) -> public_dot_scim__pb2.ListScimTokensResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revoke_scim_token(self, request: public_dot_scim__pb2.RevokeScimTokenRequest, ctx: RequestContext) -> public_dot_scim__pb2.RevokeScimTokenResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_scim_o_auth_client(self, request: public_dot_scim__pb2.CreateScimOAuthClientRequest, ctx: RequestContext) -> public_dot_scim__pb2.CreateScimOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_scim_o_auth_clients(self, request: public_dot_scim__pb2.ListScimOAuthClientsRequest, ctx: RequestContext) -> public_dot_scim__pb2.ListScimOAuthClientsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revoke_scim_o_auth_client(self, request: public_dot_scim__pb2.RevokeScimOAuthClientRequest, ctx: RequestContext) -> public_dot_scim__pb2.RevokeScimOAuthClientResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ScimServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ScimServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.scim.ScimService/CreateScimToken': EndpointSync.unary(method=MethodInfo(name='CreateScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimTokenRequest, output=public_dot_scim__pb2.CreateScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_scim_token), '/textql.rpc.public.scim.ScimService/ListScimTokens': EndpointSync.unary(method=MethodInfo(name='ListScimTokens', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimTokensRequest, output=public_dot_scim__pb2.ListScimTokensResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_scim_tokens), '/textql.rpc.public.scim.ScimService/RevokeScimToken': EndpointSync.unary(method=MethodInfo(name='RevokeScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimTokenRequest, output=public_dot_scim__pb2.RevokeScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revoke_scim_token), '/textql.rpc.public.scim.ScimService/CreateScimOAuthClient': EndpointSync.unary(method=MethodInfo(name='CreateScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimOAuthClientRequest, output=public_dot_scim__pb2.CreateScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_scim_o_auth_client), '/textql.rpc.public.scim.ScimService/ListScimOAuthClients': EndpointSync.unary(method=MethodInfo(name='ListScimOAuthClients', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimOAuthClientsRequest, output=public_dot_scim__pb2.ListScimOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_scim_o_auth_clients), '/textql.rpc.public.scim.ScimService/RevokeScimOAuthClient': EndpointSync.unary(method=MethodInfo(name='RevokeScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimOAuthClientRequest, output=public_dot_scim__pb2.RevokeScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revoke_scim_o_auth_client)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.scim.ScimService'

class ScimServiceClientSync(ConnectClientSync):

    def create_scim_token(self, request: public_dot_scim__pb2.CreateScimTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.CreateScimTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimTokenRequest, output=public_dot_scim__pb2.CreateScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_scim_tokens(self, request: public_dot_scim__pb2.ListScimTokensRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_scim__pb2.ListScimTokensResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListScimTokens', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimTokensRequest, output=public_dot_scim__pb2.ListScimTokensResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def revoke_scim_token(self, request: public_dot_scim__pb2.RevokeScimTokenRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.RevokeScimTokenResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevokeScimToken', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimTokenRequest, output=public_dot_scim__pb2.RevokeScimTokenResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_scim_o_auth_client(self, request: public_dot_scim__pb2.CreateScimOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.CreateScimOAuthClientResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.CreateScimOAuthClientRequest, output=public_dot_scim__pb2.CreateScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_scim_o_auth_clients(self, request: public_dot_scim__pb2.ListScimOAuthClientsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_scim__pb2.ListScimOAuthClientsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListScimOAuthClients', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.ListScimOAuthClientsRequest, output=public_dot_scim__pb2.ListScimOAuthClientsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def revoke_scim_o_auth_client(self, request: public_dot_scim__pb2.RevokeScimOAuthClientRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_scim__pb2.RevokeScimOAuthClientResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevokeScimOAuthClient', service_name='textql.rpc.public.scim.ScimService', input=public_dot_scim__pb2.RevokeScimOAuthClientRequest, output=public_dot_scim__pb2.RevokeScimOAuthClientResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)