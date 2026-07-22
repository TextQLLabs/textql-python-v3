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
from . import sandbox_capability_pb2 as public_dot_sandbox__capability__pb2

class SandboxCapabilityService(Protocol):

    async def execute_write(self, request: public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def state_op(self, request: public_dot_sandbox__capability__pb2.SandboxStateOpRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxStateOpResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def put_asset(self, request: public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxPutAssetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def send_notify(self, request: public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SandboxCapabilityServiceASGIApplication(ConnectASGIApplication[SandboxCapabilityService]):

    def __init__(self, service: SandboxCapabilityService | AsyncGenerator[SandboxCapabilityService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.sandbox_capability.SandboxCapabilityService/ExecuteWrite': Endpoint.unary(method=MethodInfo(name='ExecuteWrite', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, output=public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.execute_write), '/textql.rpc.public.sandbox_capability.SandboxCapabilityService/StateOp': Endpoint.unary(method=MethodInfo(name='StateOp', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxStateOpRequest, output=public_dot_sandbox__capability__pb2.SandboxStateOpResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.state_op), '/textql.rpc.public.sandbox_capability.SandboxCapabilityService/PutAsset': Endpoint.unary(method=MethodInfo(name='PutAsset', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, output=public_dot_sandbox__capability__pb2.SandboxPutAssetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.put_asset), '/textql.rpc.public.sandbox_capability.SandboxCapabilityService/SendNotify': Endpoint.unary(method=MethodInfo(name='SendNotify', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, output=public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.send_notify)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sandbox_capability.SandboxCapabilityService'

class SandboxCapabilityServiceClient(ConnectClient):

    async def execute_write(self, request: public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExecuteWrite', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, output=public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def state_op(self, request: public_dot_sandbox__capability__pb2.SandboxStateOpRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxStateOpResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='StateOp', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxStateOpRequest, output=public_dot_sandbox__capability__pb2.SandboxStateOpResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def put_asset(self, request: public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxPutAssetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='PutAsset', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, output=public_dot_sandbox__capability__pb2.SandboxPutAssetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def send_notify(self, request: public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SendNotify', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, output=public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SandboxCapabilityServiceSync(Protocol):

    def execute_write(self, request: public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def state_op(self, request: public_dot_sandbox__capability__pb2.SandboxStateOpRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxStateOpResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def put_asset(self, request: public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxPutAssetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def send_notify(self, request: public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, ctx: RequestContext) -> public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SandboxCapabilityServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SandboxCapabilityServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.sandbox_capability.SandboxCapabilityService/ExecuteWrite': EndpointSync.unary(method=MethodInfo(name='ExecuteWrite', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, output=public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.execute_write), '/textql.rpc.public.sandbox_capability.SandboxCapabilityService/StateOp': EndpointSync.unary(method=MethodInfo(name='StateOp', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxStateOpRequest, output=public_dot_sandbox__capability__pb2.SandboxStateOpResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.state_op), '/textql.rpc.public.sandbox_capability.SandboxCapabilityService/PutAsset': EndpointSync.unary(method=MethodInfo(name='PutAsset', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, output=public_dot_sandbox__capability__pb2.SandboxPutAssetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.put_asset), '/textql.rpc.public.sandbox_capability.SandboxCapabilityService/SendNotify': EndpointSync.unary(method=MethodInfo(name='SendNotify', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, output=public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.send_notify)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sandbox_capability.SandboxCapabilityService'

class SandboxCapabilityServiceClientSync(ConnectClientSync):

    def execute_write(self, request: public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExecuteWrite', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxExecuteWriteRequest, output=public_dot_sandbox__capability__pb2.SandboxExecuteWriteResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def state_op(self, request: public_dot_sandbox__capability__pb2.SandboxStateOpRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxStateOpResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='StateOp', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxStateOpRequest, output=public_dot_sandbox__capability__pb2.SandboxStateOpResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def put_asset(self, request: public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxPutAssetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='PutAsset', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxPutAssetRequest, output=public_dot_sandbox__capability__pb2.SandboxPutAssetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def send_notify(self, request: public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SendNotify', service_name='textql.rpc.public.sandbox_capability.SandboxCapabilityService', input=public_dot_sandbox__capability__pb2.SandboxSendNotifyRequest, output=public_dot_sandbox__capability__pb2.SandboxSendNotifyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)