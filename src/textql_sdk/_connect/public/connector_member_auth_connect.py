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
from . import connector_member_auth_pb2 as public_dot_connector__member__auth__pb2

class ConnectorMemberAuthService(Protocol):

    async def authenticate_member_for_connector(self, request: public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, ctx: RequestContext) -> public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_and_store_member_auth(self, request: public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, ctx: RequestContext) -> public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_member_connector_auth_status(self, request: public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, ctx: RequestContext) -> public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ConnectorMemberAuthServiceASGIApplication(ConnectASGIApplication[ConnectorMemberAuthService]):

    def __init__(self, service: ConnectorMemberAuthService | AsyncGenerator[ConnectorMemberAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService/AuthenticateMemberForConnector': Endpoint.unary(method=MethodInfo(name='AuthenticateMemberForConnector', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, output=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.authenticate_member_for_connector), '/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService/ExchangeAndStoreMemberAuth': Endpoint.unary(method=MethodInfo(name='ExchangeAndStoreMemberAuth', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, output=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_and_store_member_auth), '/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService/GetMemberConnectorAuthStatus': Endpoint.unary(method=MethodInfo(name='GetMemberConnectorAuthStatus', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, output=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_member_connector_auth_status)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService'

class ConnectorMemberAuthServiceClient(ConnectClient):

    async def authenticate_member_for_connector(self, request: public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AuthenticateMemberForConnector', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, output=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_and_store_member_auth(self, request: public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeAndStoreMemberAuth', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, output=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_member_connector_auth_status(self, request: public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMemberConnectorAuthStatus', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, output=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class ConnectorMemberAuthServiceSync(Protocol):

    def authenticate_member_for_connector(self, request: public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, ctx: RequestContext) -> public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_and_store_member_auth(self, request: public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, ctx: RequestContext) -> public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_member_connector_auth_status(self, request: public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, ctx: RequestContext) -> public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ConnectorMemberAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ConnectorMemberAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService/AuthenticateMemberForConnector': EndpointSync.unary(method=MethodInfo(name='AuthenticateMemberForConnector', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, output=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.authenticate_member_for_connector), '/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService/ExchangeAndStoreMemberAuth': EndpointSync.unary(method=MethodInfo(name='ExchangeAndStoreMemberAuth', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, output=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_and_store_member_auth), '/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService/GetMemberConnectorAuthStatus': EndpointSync.unary(method=MethodInfo(name='GetMemberConnectorAuthStatus', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, output=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_member_connector_auth_status)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.connector_member_auth.ConnectorMemberAuthService'

class ConnectorMemberAuthServiceClientSync(ConnectClientSync):

    def authenticate_member_for_connector(self, request: public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AuthenticateMemberForConnector', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorRequest, output=public_dot_connector__member__auth__pb2.AuthenticateMemberForConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_and_store_member_auth(self, request: public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeAndStoreMemberAuth', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthRequest, output=public_dot_connector__member__auth__pb2.ExchangeAndStoreMemberAuthResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_member_connector_auth_status(self, request: public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMemberConnectorAuthStatus', service_name='textql.rpc.public.connector_member_auth.ConnectorMemberAuthService', input=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusRequest, output=public_dot_connector__member__auth__pb2.GetMemberConnectorAuthStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)