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
from . import microsoft365_oauth_pb2 as public_dot_microsoft365__oauth__pb2

class Microsoft365OAuthService(Protocol):

    async def exchange_microsoft365_code(self, request: public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, ctx: RequestContext) -> public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class Microsoft365OAuthServiceASGIApplication(ConnectASGIApplication[Microsoft365OAuthService]):

    def __init__(self, service: Microsoft365OAuthService | AsyncGenerator[Microsoft365OAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService/ExchangeMicrosoft365Code': Endpoint.unary(method=MethodInfo(name='ExchangeMicrosoft365Code', service_name='textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService', input=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, output=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_microsoft365_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService'

class Microsoft365OAuthServiceClient(ConnectClient):

    async def exchange_microsoft365_code(self, request: public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeMicrosoft365Code', service_name='textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService', input=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, output=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class Microsoft365OAuthServiceSync(Protocol):

    def exchange_microsoft365_code(self, request: public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, ctx: RequestContext) -> public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class Microsoft365OAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: Microsoft365OAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService/ExchangeMicrosoft365Code': EndpointSync.unary(method=MethodInfo(name='ExchangeMicrosoft365Code', service_name='textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService', input=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, output=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_microsoft365_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService'

class Microsoft365OAuthServiceClientSync(ConnectClientSync):

    def exchange_microsoft365_code(self, request: public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeMicrosoft365Code', service_name='textql.rpc.public.microsoft365_oauth.Microsoft365OAuthService', input=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeRequest, output=public_dot_microsoft365__oauth__pb2.ExchangeMicrosoft365CodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)