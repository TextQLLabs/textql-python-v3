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
import google.protobuf.empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import engagement_pb2 as public_dot_engagement__pb2

class EngagementService(Protocol):

    async def record_engagement(self, request: public_dot_engagement__pb2.RecordEngagementRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class EngagementServiceASGIApplication(ConnectASGIApplication[EngagementService]):

    def __init__(self, service: EngagementService | AsyncGenerator[EngagementService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.engagement.EngagementService/RecordEngagement': Endpoint.unary(method=MethodInfo(name='RecordEngagement', service_name='textql.rpc.public.engagement.EngagementService', input=public_dot_engagement__pb2.RecordEngagementRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.record_engagement)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.engagement.EngagementService'

class EngagementServiceClient(ConnectClient):

    async def record_engagement(self, request: public_dot_engagement__pb2.RecordEngagementRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='RecordEngagement', service_name='textql.rpc.public.engagement.EngagementService', input=public_dot_engagement__pb2.RecordEngagementRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class EngagementServiceSync(Protocol):

    def record_engagement(self, request: public_dot_engagement__pb2.RecordEngagementRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class EngagementServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: EngagementServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.engagement.EngagementService/RecordEngagement': EndpointSync.unary(method=MethodInfo(name='RecordEngagement', service_name='textql.rpc.public.engagement.EngagementService', input=public_dot_engagement__pb2.RecordEngagementRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.record_engagement)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.engagement.EngagementService'

class EngagementServiceClientSync(ConnectClientSync):

    def record_engagement(self, request: public_dot_engagement__pb2.RecordEngagementRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='RecordEngagement', service_name='textql.rpc.public.engagement.EngagementService', input=public_dot_engagement__pb2.RecordEngagementRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)