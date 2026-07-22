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
from . import communications_pb2 as public_dot_communications__pb2

class CommunicationsService(Protocol):

    async def send_email(self, request: public_dot_communications__pb2.SendEmailRequest, ctx: RequestContext) -> public_dot_communications__pb2.SendEmailResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def upload_feedback_screenshot(self, request: public_dot_communications__pb2.UploadFeedbackScreenshotRequest, ctx: RequestContext) -> public_dot_communications__pb2.UploadFeedbackScreenshotResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class CommunicationsServiceASGIApplication(ConnectASGIApplication[CommunicationsService]):

    def __init__(self, service: CommunicationsService | AsyncGenerator[CommunicationsService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.communications.CommunicationsService/SendEmail': Endpoint.unary(method=MethodInfo(name='SendEmail', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.SendEmailRequest, output=public_dot_communications__pb2.SendEmailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.send_email), '/textql.rpc.public.communications.CommunicationsService/UploadFeedbackScreenshot': Endpoint.unary(method=MethodInfo(name='UploadFeedbackScreenshot', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.UploadFeedbackScreenshotRequest, output=public_dot_communications__pb2.UploadFeedbackScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.upload_feedback_screenshot)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.communications.CommunicationsService'

class CommunicationsServiceClient(ConnectClient):

    async def send_email(self, request: public_dot_communications__pb2.SendEmailRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_communications__pb2.SendEmailResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SendEmail', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.SendEmailRequest, output=public_dot_communications__pb2.SendEmailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def upload_feedback_screenshot(self, request: public_dot_communications__pb2.UploadFeedbackScreenshotRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_communications__pb2.UploadFeedbackScreenshotResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UploadFeedbackScreenshot', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.UploadFeedbackScreenshotRequest, output=public_dot_communications__pb2.UploadFeedbackScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class CommunicationsServiceSync(Protocol):

    def send_email(self, request: public_dot_communications__pb2.SendEmailRequest, ctx: RequestContext) -> public_dot_communications__pb2.SendEmailResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def upload_feedback_screenshot(self, request: public_dot_communications__pb2.UploadFeedbackScreenshotRequest, ctx: RequestContext) -> public_dot_communications__pb2.UploadFeedbackScreenshotResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class CommunicationsServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: CommunicationsServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.communications.CommunicationsService/SendEmail': EndpointSync.unary(method=MethodInfo(name='SendEmail', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.SendEmailRequest, output=public_dot_communications__pb2.SendEmailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.send_email), '/textql.rpc.public.communications.CommunicationsService/UploadFeedbackScreenshot': EndpointSync.unary(method=MethodInfo(name='UploadFeedbackScreenshot', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.UploadFeedbackScreenshotRequest, output=public_dot_communications__pb2.UploadFeedbackScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.upload_feedback_screenshot)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.communications.CommunicationsService'

class CommunicationsServiceClientSync(ConnectClientSync):

    def send_email(self, request: public_dot_communications__pb2.SendEmailRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_communications__pb2.SendEmailResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SendEmail', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.SendEmailRequest, output=public_dot_communications__pb2.SendEmailResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def upload_feedback_screenshot(self, request: public_dot_communications__pb2.UploadFeedbackScreenshotRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_communications__pb2.UploadFeedbackScreenshotResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UploadFeedbackScreenshot', service_name='textql.rpc.public.communications.CommunicationsService', input=public_dot_communications__pb2.UploadFeedbackScreenshotRequest, output=public_dot_communications__pb2.UploadFeedbackScreenshotResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)