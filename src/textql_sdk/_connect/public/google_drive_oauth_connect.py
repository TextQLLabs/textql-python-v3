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
from . import google_drive_oauth_pb2 as public_dot_google__drive__oauth__pb2

class GoogleDriveOAuthService(Protocol):

    async def exchange_google_drive_code(self, request: public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, ctx: RequestContext) -> public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class GoogleDriveOAuthServiceASGIApplication(ConnectASGIApplication[GoogleDriveOAuthService]):

    def __init__(self, service: GoogleDriveOAuthService | AsyncGenerator[GoogleDriveOAuthService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService/ExchangeGoogleDriveCode': Endpoint.unary(method=MethodInfo(name='ExchangeGoogleDriveCode', service_name='textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService', input=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, output=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exchange_google_drive_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService'

class GoogleDriveOAuthServiceClient(ConnectClient):

    async def exchange_google_drive_code(self, request: public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExchangeGoogleDriveCode', service_name='textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService', input=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, output=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class GoogleDriveOAuthServiceSync(Protocol):

    def exchange_google_drive_code(self, request: public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, ctx: RequestContext) -> public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class GoogleDriveOAuthServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: GoogleDriveOAuthServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService/ExchangeGoogleDriveCode': EndpointSync.unary(method=MethodInfo(name='ExchangeGoogleDriveCode', service_name='textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService', input=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, output=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exchange_google_drive_code)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService'

class GoogleDriveOAuthServiceClientSync(ConnectClientSync):

    def exchange_google_drive_code(self, request: public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExchangeGoogleDriveCode', service_name='textql.rpc.public.google_drive_oauth.GoogleDriveOAuthService', input=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeRequest, output=public_dot_google__drive__oauth__pb2.ExchangeGoogleDriveCodeResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)