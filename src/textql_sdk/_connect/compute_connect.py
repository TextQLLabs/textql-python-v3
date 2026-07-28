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
from . import compute_pb2 as compute__pb2
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2

class ComputeService(Protocol):

    async def exec(self, request: compute__pb2.ExecRequest, ctx: RequestContext) -> compute__pb2.ExecResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def load_data(self, request: compute__pb2.LoadDataRequest, ctx: RequestContext) -> compute__pb2.LoadDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def load_files(self, request: compute__pb2.LoadFileRequest, ctx: RequestContext) -> compute__pb2.LoadDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_sandbox_status(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> compute__pb2.SandboxStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def refresh_sandbox(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def query_s_q_l(self, request: compute__pb2.QuerySQLRequest, ctx: RequestContext) -> compute__pb2.QuerySQLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ComputeServiceASGIApplication(ConnectASGIApplication[ComputeService]):

    def __init__(self, service: ComputeService | AsyncGenerator[ComputeService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.compute.ComputeService/Exec': Endpoint.unary(method=MethodInfo(name='Exec', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.ExecRequest, output=compute__pb2.ExecResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.exec), '/textql.rpc.compute.ComputeService/LoadData': Endpoint.unary(method=MethodInfo(name='LoadData', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadDataRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.load_data), '/textql.rpc.compute.ComputeService/LoadFiles': Endpoint.unary(method=MethodInfo(name='LoadFiles', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadFileRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.load_files), '/textql.rpc.compute.ComputeService/GetSandboxStatus': Endpoint.unary(method=MethodInfo(name='GetSandboxStatus', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=compute__pb2.SandboxStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_sandbox_status), '/textql.rpc.compute.ComputeService/RefreshSandbox': Endpoint.unary(method=MethodInfo(name='RefreshSandbox', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.refresh_sandbox), '/textql.rpc.compute.ComputeService/QuerySQL': Endpoint.unary(method=MethodInfo(name='QuerySQL', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.QuerySQLRequest, output=compute__pb2.QuerySQLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.query_s_q_l)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.compute.ComputeService'

class ComputeServiceClient(ConnectClient):

    async def exec(self, request: compute__pb2.ExecRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.ExecResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='Exec', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.ExecRequest, output=compute__pb2.ExecResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def load_data(self, request: compute__pb2.LoadDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.LoadDataResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='LoadData', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadDataRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def load_files(self, request: compute__pb2.LoadFileRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.LoadDataResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='LoadFiles', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadFileRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_sandbox_status(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.SandboxStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetSandboxStatus', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=compute__pb2.SandboxStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def refresh_sandbox(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='RefreshSandbox', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def query_s_q_l(self, request: compute__pb2.QuerySQLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.QuerySQLResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='QuerySQL', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.QuerySQLRequest, output=compute__pb2.QuerySQLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class ComputeServiceSync(Protocol):

    def exec(self, request: compute__pb2.ExecRequest, ctx: RequestContext) -> compute__pb2.ExecResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def load_data(self, request: compute__pb2.LoadDataRequest, ctx: RequestContext) -> compute__pb2.LoadDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def load_files(self, request: compute__pb2.LoadFileRequest, ctx: RequestContext) -> compute__pb2.LoadDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_sandbox_status(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> compute__pb2.SandboxStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def refresh_sandbox(self, request: google_dot_protobuf_dot_empty__pb2.Empty, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def query_s_q_l(self, request: compute__pb2.QuerySQLRequest, ctx: RequestContext) -> compute__pb2.QuerySQLResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class ComputeServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: ComputeServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.compute.ComputeService/Exec': EndpointSync.unary(method=MethodInfo(name='Exec', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.ExecRequest, output=compute__pb2.ExecResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.exec), '/textql.rpc.compute.ComputeService/LoadData': EndpointSync.unary(method=MethodInfo(name='LoadData', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadDataRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.load_data), '/textql.rpc.compute.ComputeService/LoadFiles': EndpointSync.unary(method=MethodInfo(name='LoadFiles', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadFileRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.load_files), '/textql.rpc.compute.ComputeService/GetSandboxStatus': EndpointSync.unary(method=MethodInfo(name='GetSandboxStatus', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=compute__pb2.SandboxStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_sandbox_status), '/textql.rpc.compute.ComputeService/RefreshSandbox': EndpointSync.unary(method=MethodInfo(name='RefreshSandbox', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.refresh_sandbox), '/textql.rpc.compute.ComputeService/QuerySQL': EndpointSync.unary(method=MethodInfo(name='QuerySQL', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.QuerySQLRequest, output=compute__pb2.QuerySQLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.query_s_q_l)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.compute.ComputeService'

class ComputeServiceClientSync(ConnectClientSync):

    def exec(self, request: compute__pb2.ExecRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.ExecResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='Exec', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.ExecRequest, output=compute__pb2.ExecResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def load_data(self, request: compute__pb2.LoadDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.LoadDataResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='LoadData', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadDataRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def load_files(self, request: compute__pb2.LoadFileRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.LoadDataResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='LoadFiles', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.LoadFileRequest, output=compute__pb2.LoadDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_sandbox_status(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.SandboxStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetSandboxStatus', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=compute__pb2.SandboxStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def refresh_sandbox(self, request: google_dot_protobuf_dot_empty__pb2.Empty, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='RefreshSandbox', service_name='textql.rpc.compute.ComputeService', input=google_dot_protobuf_dot_empty__pb2.Empty, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def query_s_q_l(self, request: compute__pb2.QuerySQLRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> compute__pb2.QuerySQLResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='QuerySQL', service_name='textql.rpc.compute.ComputeService', input=compute__pb2.QuerySQLRequest, output=compute__pb2.QuerySQLResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)