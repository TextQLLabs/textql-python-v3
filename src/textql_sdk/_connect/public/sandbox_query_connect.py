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
from . import sandbox_query_pb2 as public_dot_sandbox__query__pb2

class SandboxQueryService(Protocol):

    async def execute_query(self, request: public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, ctx: RequestContext) -> public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SandboxQueryServiceASGIApplication(ConnectASGIApplication[SandboxQueryService]):

    def __init__(self, service: SandboxQueryService | AsyncGenerator[SandboxQueryService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.sandbox_query.SandboxQueryService/ExecuteQuery': Endpoint.unary(method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.sandbox_query.SandboxQueryService', input=public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, output=public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.execute_query)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sandbox_query.SandboxQueryService'

class SandboxQueryServiceClient(ConnectClient):

    async def execute_query(self, request: public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.sandbox_query.SandboxQueryService', input=public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, output=public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SandboxQueryServiceSync(Protocol):

    def execute_query(self, request: public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, ctx: RequestContext) -> public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SandboxQueryServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SandboxQueryServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.sandbox_query.SandboxQueryService/ExecuteQuery': EndpointSync.unary(method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.sandbox_query.SandboxQueryService', input=public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, output=public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.execute_query)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sandbox_query.SandboxQueryService'

class SandboxQueryServiceClientSync(ConnectClientSync):

    def execute_query(self, request: public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExecuteQuery', service_name='textql.rpc.public.sandbox_query.SandboxQueryService', input=public_dot_sandbox__query__pb2.SandboxExecuteQueryRequest, output=public_dot_sandbox__query__pb2.SandboxExecuteQueryResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)