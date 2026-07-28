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
from . import textable_pb2 as textable__pb2

class TextableService(Protocol):

    async def load_to_sandbox(self, request: textable__pb2.LoadToSandboxRequest, ctx: RequestContext) -> textable__pb2.LoadToSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def query_textable(self, request: textable__pb2.QueryTextableRequest, ctx: RequestContext) -> textable__pb2.QueryTextableResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def retrieve_stats(self, request: textable__pb2.RetrieveStatsRequest, ctx: RequestContext) -> textable__pb2.StatsResult:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def check_textable(self, request: textable__pb2.CheckTextableRequest, ctx: RequestContext) -> textable__pb2.CheckTextableResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TextableServiceASGIApplication(ConnectASGIApplication[TextableService]):

    def __init__(self, service: TextableService | AsyncGenerator[TextableService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.textable.TextableService/LoadToSandbox': Endpoint.unary(method=MethodInfo(name='LoadToSandbox', service_name='textql.rpc.textable.TextableService', input=textable__pb2.LoadToSandboxRequest, output=textable__pb2.LoadToSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.load_to_sandbox), '/textql.rpc.textable.TextableService/QueryTextable': Endpoint.unary(method=MethodInfo(name='QueryTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.QueryTextableRequest, output=textable__pb2.QueryTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.query_textable), '/textql.rpc.textable.TextableService/RetrieveStats': Endpoint.unary(method=MethodInfo(name='RetrieveStats', service_name='textql.rpc.textable.TextableService', input=textable__pb2.RetrieveStatsRequest, output=textable__pb2.StatsResult, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.retrieve_stats), '/textql.rpc.textable.TextableService/CheckTextable': Endpoint.unary(method=MethodInfo(name='CheckTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.CheckTextableRequest, output=textable__pb2.CheckTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.check_textable)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.textable.TextableService'

class TextableServiceClient(ConnectClient):

    async def load_to_sandbox(self, request: textable__pb2.LoadToSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.LoadToSandboxResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='LoadToSandbox', service_name='textql.rpc.textable.TextableService', input=textable__pb2.LoadToSandboxRequest, output=textable__pb2.LoadToSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def query_textable(self, request: textable__pb2.QueryTextableRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.QueryTextableResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='QueryTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.QueryTextableRequest, output=textable__pb2.QueryTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def retrieve_stats(self, request: textable__pb2.RetrieveStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.StatsResult:
        return await self.execute_unary(request=request, method=MethodInfo(name='RetrieveStats', service_name='textql.rpc.textable.TextableService', input=textable__pb2.RetrieveStatsRequest, output=textable__pb2.StatsResult, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def check_textable(self, request: textable__pb2.CheckTextableRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.CheckTextableResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CheckTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.CheckTextableRequest, output=textable__pb2.CheckTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class TextableServiceSync(Protocol):

    def load_to_sandbox(self, request: textable__pb2.LoadToSandboxRequest, ctx: RequestContext) -> textable__pb2.LoadToSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def query_textable(self, request: textable__pb2.QueryTextableRequest, ctx: RequestContext) -> textable__pb2.QueryTextableResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def retrieve_stats(self, request: textable__pb2.RetrieveStatsRequest, ctx: RequestContext) -> textable__pb2.StatsResult:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def check_textable(self, request: textable__pb2.CheckTextableRequest, ctx: RequestContext) -> textable__pb2.CheckTextableResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TextableServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: TextableServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.textable.TextableService/LoadToSandbox': EndpointSync.unary(method=MethodInfo(name='LoadToSandbox', service_name='textql.rpc.textable.TextableService', input=textable__pb2.LoadToSandboxRequest, output=textable__pb2.LoadToSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.load_to_sandbox), '/textql.rpc.textable.TextableService/QueryTextable': EndpointSync.unary(method=MethodInfo(name='QueryTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.QueryTextableRequest, output=textable__pb2.QueryTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.query_textable), '/textql.rpc.textable.TextableService/RetrieveStats': EndpointSync.unary(method=MethodInfo(name='RetrieveStats', service_name='textql.rpc.textable.TextableService', input=textable__pb2.RetrieveStatsRequest, output=textable__pb2.StatsResult, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.retrieve_stats), '/textql.rpc.textable.TextableService/CheckTextable': EndpointSync.unary(method=MethodInfo(name='CheckTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.CheckTextableRequest, output=textable__pb2.CheckTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.check_textable)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.textable.TextableService'

class TextableServiceClientSync(ConnectClientSync):

    def load_to_sandbox(self, request: textable__pb2.LoadToSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.LoadToSandboxResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='LoadToSandbox', service_name='textql.rpc.textable.TextableService', input=textable__pb2.LoadToSandboxRequest, output=textable__pb2.LoadToSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def query_textable(self, request: textable__pb2.QueryTextableRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.QueryTextableResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='QueryTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.QueryTextableRequest, output=textable__pb2.QueryTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def retrieve_stats(self, request: textable__pb2.RetrieveStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.StatsResult:
        return self.execute_unary(request=request, method=MethodInfo(name='RetrieveStats', service_name='textql.rpc.textable.TextableService', input=textable__pb2.RetrieveStatsRequest, output=textable__pb2.StatsResult, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def check_textable(self, request: textable__pb2.CheckTextableRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> textable__pb2.CheckTextableResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CheckTextable', service_name='textql.rpc.textable.TextableService', input=textable__pb2.CheckTextableRequest, output=textable__pb2.CheckTextableResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)