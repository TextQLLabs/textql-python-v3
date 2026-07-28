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
from . import sandbox_admin_pb2 as public_dot_sandbox__admin__pb2

class SandboxAdminService(Protocol):

    async def list_sandboxes(self, request: public_dot_sandbox__admin__pb2.ListSandboxesRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def stop_sandbox(self, request: public_dot_sandbox__admin__pb2.StopSandboxRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.StopSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def restart_sandbox(self, request: public_dot_sandbox__admin__pb2.RestartSandboxRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.RestartSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_sandbox(self, request: public_dot_sandbox__admin__pb2.GetSandboxRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.GetSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_sandbox_executions(self, request: public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_sandbox_files(self, request: public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxFilesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def read_sandbox_file(self, request: public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ReadSandboxFileResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_sandbox_egress(self, request: public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxEgressResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_sandbox_spend(self, request: public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxSpendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_sandbox_resources(self, request: public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SandboxAdminServiceASGIApplication(ConnectASGIApplication[SandboxAdminService]):

    def __init__(self, service: SandboxAdminService | AsyncGenerator[SandboxAdminService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxes': Endpoint.unary(method=MethodInfo(name='ListSandboxes', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_sandboxes), '/textql.rpc.public.sandbox_admin.SandboxAdminService/StopSandbox': Endpoint.unary(method=MethodInfo(name='StopSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.StopSandboxRequest, output=public_dot_sandbox__admin__pb2.StopSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.stop_sandbox), '/textql.rpc.public.sandbox_admin.SandboxAdminService/RestartSandbox': Endpoint.unary(method=MethodInfo(name='RestartSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.RestartSandboxRequest, output=public_dot_sandbox__admin__pb2.RestartSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.restart_sandbox), '/textql.rpc.public.sandbox_admin.SandboxAdminService/GetSandbox': Endpoint.unary(method=MethodInfo(name='GetSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.GetSandboxRequest, output=public_dot_sandbox__admin__pb2.GetSandboxResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_sandbox), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxExecutions': Endpoint.unary(method=MethodInfo(name='ListSandboxExecutions', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, output=public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_sandbox_executions), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxFiles': Endpoint.unary(method=MethodInfo(name='ListSandboxFiles', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxFilesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_sandbox_files), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ReadSandboxFile': Endpoint.unary(method=MethodInfo(name='ReadSandboxFile', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, output=public_dot_sandbox__admin__pb2.ReadSandboxFileResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.read_sandbox_file), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxEgress': Endpoint.unary(method=MethodInfo(name='ListSandboxEgress', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, output=public_dot_sandbox__admin__pb2.ListSandboxEgressResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_sandbox_egress), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxSpend': Endpoint.unary(method=MethodInfo(name='ListSandboxSpend', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, output=public_dot_sandbox__admin__pb2.ListSandboxSpendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_sandbox_spend), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxResources': Endpoint.unary(method=MethodInfo(name='ListSandboxResources', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_sandbox_resources)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sandbox_admin.SandboxAdminService'

class SandboxAdminServiceClient(ConnectClient):

    async def list_sandboxes(self, request: public_dot_sandbox__admin__pb2.ListSandboxesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListSandboxes', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def stop_sandbox(self, request: public_dot_sandbox__admin__pb2.StopSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__admin__pb2.StopSandboxResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='StopSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.StopSandboxRequest, output=public_dot_sandbox__admin__pb2.StopSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def restart_sandbox(self, request: public_dot_sandbox__admin__pb2.RestartSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__admin__pb2.RestartSandboxResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RestartSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.RestartSandboxRequest, output=public_dot_sandbox__admin__pb2.RestartSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_sandbox(self, request: public_dot_sandbox__admin__pb2.GetSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.GetSandboxResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.GetSandboxRequest, output=public_dot_sandbox__admin__pb2.GetSandboxResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_sandbox_executions(self, request: public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListSandboxExecutions', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, output=public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_sandbox_files(self, request: public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxFilesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListSandboxFiles', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxFilesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def read_sandbox_file(self, request: public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ReadSandboxFileResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ReadSandboxFile', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, output=public_dot_sandbox__admin__pb2.ReadSandboxFileResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_sandbox_egress(self, request: public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxEgressResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListSandboxEgress', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, output=public_dot_sandbox__admin__pb2.ListSandboxEgressResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_sandbox_spend(self, request: public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxSpendResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListSandboxSpend', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, output=public_dot_sandbox__admin__pb2.ListSandboxSpendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_sandbox_resources(self, request: public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListSandboxResources', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class SandboxAdminServiceSync(Protocol):

    def list_sandboxes(self, request: public_dot_sandbox__admin__pb2.ListSandboxesRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def stop_sandbox(self, request: public_dot_sandbox__admin__pb2.StopSandboxRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.StopSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def restart_sandbox(self, request: public_dot_sandbox__admin__pb2.RestartSandboxRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.RestartSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_sandbox(self, request: public_dot_sandbox__admin__pb2.GetSandboxRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.GetSandboxResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_sandbox_executions(self, request: public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_sandbox_files(self, request: public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxFilesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def read_sandbox_file(self, request: public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ReadSandboxFileResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_sandbox_egress(self, request: public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxEgressResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_sandbox_spend(self, request: public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxSpendResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_sandbox_resources(self, request: public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, ctx: RequestContext) -> public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SandboxAdminServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SandboxAdminServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxes': EndpointSync.unary(method=MethodInfo(name='ListSandboxes', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_sandboxes), '/textql.rpc.public.sandbox_admin.SandboxAdminService/StopSandbox': EndpointSync.unary(method=MethodInfo(name='StopSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.StopSandboxRequest, output=public_dot_sandbox__admin__pb2.StopSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.stop_sandbox), '/textql.rpc.public.sandbox_admin.SandboxAdminService/RestartSandbox': EndpointSync.unary(method=MethodInfo(name='RestartSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.RestartSandboxRequest, output=public_dot_sandbox__admin__pb2.RestartSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.restart_sandbox), '/textql.rpc.public.sandbox_admin.SandboxAdminService/GetSandbox': EndpointSync.unary(method=MethodInfo(name='GetSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.GetSandboxRequest, output=public_dot_sandbox__admin__pb2.GetSandboxResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_sandbox), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxExecutions': EndpointSync.unary(method=MethodInfo(name='ListSandboxExecutions', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, output=public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_sandbox_executions), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxFiles': EndpointSync.unary(method=MethodInfo(name='ListSandboxFiles', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxFilesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_sandbox_files), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ReadSandboxFile': EndpointSync.unary(method=MethodInfo(name='ReadSandboxFile', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, output=public_dot_sandbox__admin__pb2.ReadSandboxFileResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.read_sandbox_file), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxEgress': EndpointSync.unary(method=MethodInfo(name='ListSandboxEgress', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, output=public_dot_sandbox__admin__pb2.ListSandboxEgressResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_sandbox_egress), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxSpend': EndpointSync.unary(method=MethodInfo(name='ListSandboxSpend', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, output=public_dot_sandbox__admin__pb2.ListSandboxSpendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_sandbox_spend), '/textql.rpc.public.sandbox_admin.SandboxAdminService/ListSandboxResources': EndpointSync.unary(method=MethodInfo(name='ListSandboxResources', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_sandbox_resources)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sandbox_admin.SandboxAdminService'

class SandboxAdminServiceClientSync(ConnectClientSync):

    def list_sandboxes(self, request: public_dot_sandbox__admin__pb2.ListSandboxesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListSandboxes', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def stop_sandbox(self, request: public_dot_sandbox__admin__pb2.StopSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__admin__pb2.StopSandboxResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='StopSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.StopSandboxRequest, output=public_dot_sandbox__admin__pb2.StopSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def restart_sandbox(self, request: public_dot_sandbox__admin__pb2.RestartSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__admin__pb2.RestartSandboxResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RestartSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.RestartSandboxRequest, output=public_dot_sandbox__admin__pb2.RestartSandboxResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_sandbox(self, request: public_dot_sandbox__admin__pb2.GetSandboxRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.GetSandboxResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetSandbox', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.GetSandboxRequest, output=public_dot_sandbox__admin__pb2.GetSandboxResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_sandbox_executions(self, request: public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListSandboxExecutions', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxExecutionsRequest, output=public_dot_sandbox__admin__pb2.ListSandboxExecutionsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_sandbox_files(self, request: public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxFilesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListSandboxFiles', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxFilesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxFilesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def read_sandbox_file(self, request: public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ReadSandboxFileResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ReadSandboxFile', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ReadSandboxFileRequest, output=public_dot_sandbox__admin__pb2.ReadSandboxFileResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_sandbox_egress(self, request: public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxEgressResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListSandboxEgress', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxEgressRequest, output=public_dot_sandbox__admin__pb2.ListSandboxEgressResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_sandbox_spend(self, request: public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxSpendResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListSandboxSpend', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxSpendRequest, output=public_dot_sandbox__admin__pb2.ListSandboxSpendResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_sandbox_resources(self, request: public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListSandboxResources', service_name='textql.rpc.public.sandbox_admin.SandboxAdminService', input=public_dot_sandbox__admin__pb2.ListSandboxResourcesRequest, output=public_dot_sandbox__admin__pb2.ListSandboxResourcesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)