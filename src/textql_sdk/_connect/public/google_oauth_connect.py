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
from . import google_oauth_pb2 as public_dot_google__oauth__pb2

class GoogleOAuthService(Protocol):

    async def initiate_google_o_auth_flow(self, request: public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, ctx: RequestContext) -> public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def exchange_google_code(self, request: public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, ctx: RequestContext) -> public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class GoogleOAuthServiceASGIApplication(ConnectASGIApplication[GoogleOAuthService]):

    def __init__(self, service: GoogleOAuthService | AsyncGenerator[GoogleOAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.google_oauth.GoogleOAuthService/InitiateGoogleOAuthFlow': Endpoint.unary(method=MethodInfo(name='InitiateGoogleOAuthFlow', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, output=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.initiate_google_o_auth_flow), '/textql.rpc.public.google_oauth.GoogleOAuthService/ExchangeGoogleCode': Endpoint.unary(method=MethodInfo(name='ExchangeGoogleCode', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, output=public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_google_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.google_oauth.GoogleOAuthService'

class GoogleOAuthServiceClient(ConnectClient):

    async def initiate_google_o_auth_flow(self, request: public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='InitiateGoogleOAuthFlow', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, output=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def exchange_google_code(self, request: public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeGoogleCode', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, output=public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class GoogleOAuthServiceSync(Protocol):

    def initiate_google_o_auth_flow(self, request: public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, ctx: RequestContext) -> public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def exchange_google_code(self, request: public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, ctx: RequestContext) -> public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class GoogleOAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: GoogleOAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.google_oauth.GoogleOAuthService/InitiateGoogleOAuthFlow': EndpointSync.unary(method=MethodInfo(name='InitiateGoogleOAuthFlow', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, output=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.initiate_google_o_auth_flow), '/textql.rpc.public.google_oauth.GoogleOAuthService/ExchangeGoogleCode': EndpointSync.unary(method=MethodInfo(name='ExchangeGoogleCode', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, output=public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_google_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.google_oauth.GoogleOAuthService'

class GoogleOAuthServiceClientSync(ConnectClientSync):

    def initiate_google_o_auth_flow(self, request: public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='InitiateGoogleOAuthFlow', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowRequest, output=public_dot_google__oauth__pb2.InitiateGoogleOAuthFlowResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def exchange_google_code(self, request: public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeGoogleCode', service_name='textql.rpc.public.google_oauth.GoogleOAuthService', input=public_dot_google__oauth__pb2.ExchangeGoogleCodeRequest, output=public_dot_google__oauth__pb2.ExchangeGoogleCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)