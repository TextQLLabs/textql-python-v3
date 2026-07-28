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
from . import checks_pb2 as public_dot_checks__pb2

class ChecksService(Protocol):

    async def list_checks(self, request: public_dot_checks__pb2.ListChecksRequest, ctx: RequestContext) -> public_dot_checks__pb2.ListChecksResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def run_checks(self, request: public_dot_checks__pb2.RunChecksRequest, ctx: RequestContext) -> public_dot_checks__pb2.RunChecksResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_check_results(self, request: public_dot_checks__pb2.GetCheckResultsRequest, ctx: RequestContext) -> public_dot_checks__pb2.GetCheckResultsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ChecksServiceASGIApplication(ConnectASGIApplication[ChecksService]):

    def __init__(self, service: ChecksService | AsyncGenerator[ChecksService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.checks.ChecksService/ListChecks': Endpoint.unary(method=MethodInfo(name='ListChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.ListChecksRequest, output=public_dot_checks__pb2.ListChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_checks), '/textql.rpc.public.checks.ChecksService/RunChecks': Endpoint.unary(method=MethodInfo(name='RunChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.RunChecksRequest, output=public_dot_checks__pb2.RunChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.run_checks), '/textql.rpc.public.checks.ChecksService/GetCheckResults': Endpoint.unary(method=MethodInfo(name='GetCheckResults', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.GetCheckResultsRequest, output=public_dot_checks__pb2.GetCheckResultsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_check_results)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.checks.ChecksService'

class ChecksServiceClient(ConnectClient):

    async def list_checks(self, request: public_dot_checks__pb2.ListChecksRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_checks__pb2.ListChecksResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.ListChecksRequest, output=public_dot_checks__pb2.ListChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def run_checks(self, request: public_dot_checks__pb2.RunChecksRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_checks__pb2.RunChecksResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RunChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.RunChecksRequest, output=public_dot_checks__pb2.RunChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_check_results(self, request: public_dot_checks__pb2.GetCheckResultsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_checks__pb2.GetCheckResultsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCheckResults', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.GetCheckResultsRequest, output=public_dot_checks__pb2.GetCheckResultsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class ChecksServiceSync(Protocol):

    def list_checks(self, request: public_dot_checks__pb2.ListChecksRequest, ctx: RequestContext) -> public_dot_checks__pb2.ListChecksResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def run_checks(self, request: public_dot_checks__pb2.RunChecksRequest, ctx: RequestContext) -> public_dot_checks__pb2.RunChecksResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_check_results(self, request: public_dot_checks__pb2.GetCheckResultsRequest, ctx: RequestContext) -> public_dot_checks__pb2.GetCheckResultsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ChecksServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ChecksServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.checks.ChecksService/ListChecks': EndpointSync.unary(method=MethodInfo(name='ListChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.ListChecksRequest, output=public_dot_checks__pb2.ListChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_checks), '/textql.rpc.public.checks.ChecksService/RunChecks': EndpointSync.unary(method=MethodInfo(name='RunChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.RunChecksRequest, output=public_dot_checks__pb2.RunChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.run_checks), '/textql.rpc.public.checks.ChecksService/GetCheckResults': EndpointSync.unary(method=MethodInfo(name='GetCheckResults', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.GetCheckResultsRequest, output=public_dot_checks__pb2.GetCheckResultsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_check_results)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.checks.ChecksService'

class ChecksServiceClientSync(ConnectClientSync):

    def list_checks(self, request: public_dot_checks__pb2.ListChecksRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_checks__pb2.ListChecksResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.ListChecksRequest, output=public_dot_checks__pb2.ListChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def run_checks(self, request: public_dot_checks__pb2.RunChecksRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_checks__pb2.RunChecksResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RunChecks', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.RunChecksRequest, output=public_dot_checks__pb2.RunChecksResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_check_results(self, request: public_dot_checks__pb2.GetCheckResultsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_checks__pb2.GetCheckResultsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCheckResults', service_name='textql.rpc.public.checks.ChecksService', input=public_dot_checks__pb2.GetCheckResultsRequest, output=public_dot_checks__pb2.GetCheckResultsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)