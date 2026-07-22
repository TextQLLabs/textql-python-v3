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
from . import snowflake_oauth_pb2 as public_dot_snowflake__oauth__pb2

class SnowflakeOAuthService(Protocol):

    async def get_snowflake_o_auth_u_r_l(self, request: public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, ctx: RequestContext) -> public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_snowflake_code(self, request: public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, ctx: RequestContext) -> public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SnowflakeOAuthServiceASGIApplication(ConnectASGIApplication[SnowflakeOAuthService]):

    def __init__(self, service: SnowflakeOAuthService | AsyncGenerator[SnowflakeOAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.snowflake_oauth.SnowflakeOAuthService/GetSnowflakeOAuthURL': Endpoint.unary(method=MethodInfo(name='GetSnowflakeOAuthURL', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, output=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_snowflake_o_auth_u_r_l), '/textql.rpc.public.snowflake_oauth.SnowflakeOAuthService/ExchangeSnowflakeCode': Endpoint.unary(method=MethodInfo(name='ExchangeSnowflakeCode', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, output=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_snowflake_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.snowflake_oauth.SnowflakeOAuthService'

class SnowflakeOAuthServiceClient(ConnectClient):

    async def get_snowflake_o_auth_u_r_l(self, request: public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetSnowflakeOAuthURL', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, output=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_snowflake_code(self, request: public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeSnowflakeCode', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, output=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SnowflakeOAuthServiceSync(Protocol):

    def get_snowflake_o_auth_u_r_l(self, request: public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, ctx: RequestContext) -> public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_snowflake_code(self, request: public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, ctx: RequestContext) -> public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SnowflakeOAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SnowflakeOAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.snowflake_oauth.SnowflakeOAuthService/GetSnowflakeOAuthURL': EndpointSync.unary(method=MethodInfo(name='GetSnowflakeOAuthURL', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, output=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_snowflake_o_auth_u_r_l), '/textql.rpc.public.snowflake_oauth.SnowflakeOAuthService/ExchangeSnowflakeCode': EndpointSync.unary(method=MethodInfo(name='ExchangeSnowflakeCode', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, output=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_snowflake_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.snowflake_oauth.SnowflakeOAuthService'

class SnowflakeOAuthServiceClientSync(ConnectClientSync):

    def get_snowflake_o_auth_u_r_l(self, request: public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetSnowflakeOAuthURL', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLRequest, output=public_dot_snowflake__oauth__pb2.GetSnowflakeOAuthURLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_snowflake_code(self, request: public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeSnowflakeCode', service_name='textql.rpc.public.snowflake_oauth.SnowflakeOAuthService', input=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeRequest, output=public_dot_snowflake__oauth__pb2.ExchangeSnowflakeCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)