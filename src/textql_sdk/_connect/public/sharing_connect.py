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
from . import sharing_pb2 as public_dot_sharing__pb2

class SharingService(Protocol):

    async def create_share(self, request: public_dot_sharing__pb2.CreateShareRequest, ctx: RequestContext) -> public_dot_sharing__pb2.CreateShareResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_share(self, request: public_dot_sharing__pb2.GetShareRequest, ctx: RequestContext) -> public_dot_sharing__pb2.GetShareResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def resolve_share_for_caller(self, request: public_dot_sharing__pb2.ResolveShareForCallerRequest, ctx: RequestContext) -> public_dot_sharing__pb2.ResolveShareForCallerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SharingServiceASGIApplication(ConnectASGIApplication[SharingService]):

    def __init__(self, service: SharingService | AsyncGenerator[SharingService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.sharing.SharingService/CreateShare': Endpoint.unary(method=MethodInfo(name='CreateShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.CreateShareRequest, output=public_dot_sharing__pb2.CreateShareResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_share), '/textql.rpc.public.sharing.SharingService/GetShare': Endpoint.unary(method=MethodInfo(name='GetShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.GetShareRequest, output=public_dot_sharing__pb2.GetShareResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_share), '/textql.rpc.public.sharing.SharingService/ResolveShareForCaller': Endpoint.unary(method=MethodInfo(name='ResolveShareForCaller', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.ResolveShareForCallerRequest, output=public_dot_sharing__pb2.ResolveShareForCallerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.resolve_share_for_caller)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sharing.SharingService'

class SharingServiceClient(ConnectClient):

    async def create_share(self, request: public_dot_sharing__pb2.CreateShareRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sharing__pb2.CreateShareResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.CreateShareRequest, output=public_dot_sharing__pb2.CreateShareResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_share(self, request: public_dot_sharing__pb2.GetShareRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sharing__pb2.GetShareResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.GetShareRequest, output=public_dot_sharing__pb2.GetShareResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def resolve_share_for_caller(self, request: public_dot_sharing__pb2.ResolveShareForCallerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sharing__pb2.ResolveShareForCallerResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ResolveShareForCaller', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.ResolveShareForCallerRequest, output=public_dot_sharing__pb2.ResolveShareForCallerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class SharingPreviewService(Protocol):

    async def get_share_preview(self, request: public_dot_sharing__pb2.GetSharePreviewRequest, ctx: RequestContext) -> public_dot_sharing__pb2.GetSharePreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SharingPreviewServiceASGIApplication(ConnectASGIApplication[SharingPreviewService]):

    def __init__(self, service: SharingPreviewService | AsyncGenerator[SharingPreviewService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.sharing.SharingPreviewService/GetSharePreview': Endpoint.unary(method=MethodInfo(name='GetSharePreview', service_name='textql.rpc.public.sharing.SharingPreviewService', input=public_dot_sharing__pb2.GetSharePreviewRequest, output=public_dot_sharing__pb2.GetSharePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_share_preview)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sharing.SharingPreviewService'

class SharingPreviewServiceClient(ConnectClient):

    async def get_share_preview(self, request: public_dot_sharing__pb2.GetSharePreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sharing__pb2.GetSharePreviewResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetSharePreview', service_name='textql.rpc.public.sharing.SharingPreviewService', input=public_dot_sharing__pb2.GetSharePreviewRequest, output=public_dot_sharing__pb2.GetSharePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class SharingServiceSync(Protocol):

    def create_share(self, request: public_dot_sharing__pb2.CreateShareRequest, ctx: RequestContext) -> public_dot_sharing__pb2.CreateShareResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_share(self, request: public_dot_sharing__pb2.GetShareRequest, ctx: RequestContext) -> public_dot_sharing__pb2.GetShareResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def resolve_share_for_caller(self, request: public_dot_sharing__pb2.ResolveShareForCallerRequest, ctx: RequestContext) -> public_dot_sharing__pb2.ResolveShareForCallerResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SharingServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SharingServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.sharing.SharingService/CreateShare': EndpointSync.unary(method=MethodInfo(name='CreateShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.CreateShareRequest, output=public_dot_sharing__pb2.CreateShareResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_share), '/textql.rpc.public.sharing.SharingService/GetShare': EndpointSync.unary(method=MethodInfo(name='GetShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.GetShareRequest, output=public_dot_sharing__pb2.GetShareResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_share), '/textql.rpc.public.sharing.SharingService/ResolveShareForCaller': EndpointSync.unary(method=MethodInfo(name='ResolveShareForCaller', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.ResolveShareForCallerRequest, output=public_dot_sharing__pb2.ResolveShareForCallerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.resolve_share_for_caller)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sharing.SharingService'

class SharingServiceClientSync(ConnectClientSync):

    def create_share(self, request: public_dot_sharing__pb2.CreateShareRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sharing__pb2.CreateShareResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.CreateShareRequest, output=public_dot_sharing__pb2.CreateShareResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_share(self, request: public_dot_sharing__pb2.GetShareRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sharing__pb2.GetShareResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetShare', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.GetShareRequest, output=public_dot_sharing__pb2.GetShareResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def resolve_share_for_caller(self, request: public_dot_sharing__pb2.ResolveShareForCallerRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sharing__pb2.ResolveShareForCallerResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ResolveShareForCaller', service_name='textql.rpc.public.sharing.SharingService', input=public_dot_sharing__pb2.ResolveShareForCallerRequest, output=public_dot_sharing__pb2.ResolveShareForCallerResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

class SharingPreviewServiceSync(Protocol):

    def get_share_preview(self, request: public_dot_sharing__pb2.GetSharePreviewRequest, ctx: RequestContext) -> public_dot_sharing__pb2.GetSharePreviewResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SharingPreviewServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SharingPreviewServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.sharing.SharingPreviewService/GetSharePreview': EndpointSync.unary(method=MethodInfo(name='GetSharePreview', service_name='textql.rpc.public.sharing.SharingPreviewService', input=public_dot_sharing__pb2.GetSharePreviewRequest, output=public_dot_sharing__pb2.GetSharePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_share_preview)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sharing.SharingPreviewService'

class SharingPreviewServiceClientSync(ConnectClientSync):

    def get_share_preview(self, request: public_dot_sharing__pb2.GetSharePreviewRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_sharing__pb2.GetSharePreviewResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetSharePreview', service_name='textql.rpc.public.sharing.SharingPreviewService', input=public_dot_sharing__pb2.GetSharePreviewRequest, output=public_dot_sharing__pb2.GetSharePreviewResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)