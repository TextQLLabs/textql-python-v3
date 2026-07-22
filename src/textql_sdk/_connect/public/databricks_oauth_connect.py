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
from . import databricks_oauth_pb2 as public_dot_databricks__oauth__pb2

class DatabricksOAuthService(Protocol):

    async def get_databricks_o_auth_u_r_l(self, request: public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, ctx: RequestContext) -> public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_databricks_code(self, request: public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, ctx: RequestContext) -> public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class DatabricksOAuthServiceASGIApplication(ConnectASGIApplication[DatabricksOAuthService]):

    def __init__(self, service: DatabricksOAuthService | AsyncGenerator[DatabricksOAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.databricks_oauth.DatabricksOAuthService/GetDatabricksOAuthURL': Endpoint.unary(method=MethodInfo(name='GetDatabricksOAuthURL', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, output=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_databricks_o_auth_u_r_l), '/textql.rpc.public.databricks_oauth.DatabricksOAuthService/ExchangeDatabricksCode': Endpoint.unary(method=MethodInfo(name='ExchangeDatabricksCode', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, output=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_databricks_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.databricks_oauth.DatabricksOAuthService'

class DatabricksOAuthServiceClient(ConnectClient):

    async def get_databricks_o_auth_u_r_l(self, request: public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDatabricksOAuthURL', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, output=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_databricks_code(self, request: public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeDatabricksCode', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, output=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class DatabricksOAuthServiceSync(Protocol):

    def get_databricks_o_auth_u_r_l(self, request: public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, ctx: RequestContext) -> public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_databricks_code(self, request: public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, ctx: RequestContext) -> public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class DatabricksOAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: DatabricksOAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.databricks_oauth.DatabricksOAuthService/GetDatabricksOAuthURL': EndpointSync.unary(method=MethodInfo(name='GetDatabricksOAuthURL', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, output=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_databricks_o_auth_u_r_l), '/textql.rpc.public.databricks_oauth.DatabricksOAuthService/ExchangeDatabricksCode': EndpointSync.unary(method=MethodInfo(name='ExchangeDatabricksCode', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, output=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_databricks_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.databricks_oauth.DatabricksOAuthService'

class DatabricksOAuthServiceClientSync(ConnectClientSync):

    def get_databricks_o_auth_u_r_l(self, request: public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDatabricksOAuthURL', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLRequest, output=public_dot_databricks__oauth__pb2.GetDatabricksOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_databricks_code(self, request: public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeDatabricksCode', service_name='textql.rpc.public.databricks_oauth.DatabricksOAuthService', input=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeRequest, output=public_dot_databricks__oauth__pb2.ExchangeDatabricksCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)