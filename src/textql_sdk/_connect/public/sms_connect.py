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
from . import sms_pb2 as public_dot_sms__pb2

class SmsService(Protocol):

    async def start_phone_verification(self, request: public_dot_sms__pb2.StartPhoneVerificationRequest, ctx: RequestContext) -> public_dot_sms__pb2.StartPhoneVerificationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def confirm_phone_verification(self, request: public_dot_sms__pb2.ConfirmPhoneVerificationRequest, ctx: RequestContext) -> public_dot_sms__pb2.ConfirmPhoneVerificationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_sms_agent(self, request: public_dot_sms__pb2.SetSmsAgentRequest, ctx: RequestContext) -> public_dot_sms__pb2.SetSmsAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def remove_phone(self, request: public_dot_sms__pb2.RemovePhoneRequest, ctx: RequestContext) -> public_dot_sms__pb2.RemovePhoneResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SmsServiceASGIApplication(ConnectASGIApplication[SmsService]):

    def __init__(self, service: SmsService | AsyncGenerator[SmsService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.sms.SmsService/StartPhoneVerification': Endpoint.unary(method=MethodInfo(name='StartPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.StartPhoneVerificationRequest, output=public_dot_sms__pb2.StartPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.start_phone_verification), '/textql.rpc.public.sms.SmsService/ConfirmPhoneVerification': Endpoint.unary(method=MethodInfo(name='ConfirmPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.ConfirmPhoneVerificationRequest, output=public_dot_sms__pb2.ConfirmPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.confirm_phone_verification), '/textql.rpc.public.sms.SmsService/SetSmsAgent': Endpoint.unary(method=MethodInfo(name='SetSmsAgent', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.SetSmsAgentRequest, output=public_dot_sms__pb2.SetSmsAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_sms_agent), '/textql.rpc.public.sms.SmsService/RemovePhone': Endpoint.unary(method=MethodInfo(name='RemovePhone', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.RemovePhoneRequest, output=public_dot_sms__pb2.RemovePhoneResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.remove_phone)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sms.SmsService'

class SmsServiceClient(ConnectClient):

    async def start_phone_verification(self, request: public_dot_sms__pb2.StartPhoneVerificationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.StartPhoneVerificationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='StartPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.StartPhoneVerificationRequest, output=public_dot_sms__pb2.StartPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def confirm_phone_verification(self, request: public_dot_sms__pb2.ConfirmPhoneVerificationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.ConfirmPhoneVerificationResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ConfirmPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.ConfirmPhoneVerificationRequest, output=public_dot_sms__pb2.ConfirmPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def set_sms_agent(self, request: public_dot_sms__pb2.SetSmsAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.SetSmsAgentResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetSmsAgent', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.SetSmsAgentRequest, output=public_dot_sms__pb2.SetSmsAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def remove_phone(self, request: public_dot_sms__pb2.RemovePhoneRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.RemovePhoneResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RemovePhone', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.RemovePhoneRequest, output=public_dot_sms__pb2.RemovePhoneResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SmsServiceSync(Protocol):

    def start_phone_verification(self, request: public_dot_sms__pb2.StartPhoneVerificationRequest, ctx: RequestContext) -> public_dot_sms__pb2.StartPhoneVerificationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def confirm_phone_verification(self, request: public_dot_sms__pb2.ConfirmPhoneVerificationRequest, ctx: RequestContext) -> public_dot_sms__pb2.ConfirmPhoneVerificationResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_sms_agent(self, request: public_dot_sms__pb2.SetSmsAgentRequest, ctx: RequestContext) -> public_dot_sms__pb2.SetSmsAgentResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def remove_phone(self, request: public_dot_sms__pb2.RemovePhoneRequest, ctx: RequestContext) -> public_dot_sms__pb2.RemovePhoneResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SmsServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SmsServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.sms.SmsService/StartPhoneVerification': EndpointSync.unary(method=MethodInfo(name='StartPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.StartPhoneVerificationRequest, output=public_dot_sms__pb2.StartPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.start_phone_verification), '/textql.rpc.public.sms.SmsService/ConfirmPhoneVerification': EndpointSync.unary(method=MethodInfo(name='ConfirmPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.ConfirmPhoneVerificationRequest, output=public_dot_sms__pb2.ConfirmPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.confirm_phone_verification), '/textql.rpc.public.sms.SmsService/SetSmsAgent': EndpointSync.unary(method=MethodInfo(name='SetSmsAgent', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.SetSmsAgentRequest, output=public_dot_sms__pb2.SetSmsAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_sms_agent), '/textql.rpc.public.sms.SmsService/RemovePhone': EndpointSync.unary(method=MethodInfo(name='RemovePhone', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.RemovePhoneRequest, output=public_dot_sms__pb2.RemovePhoneResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.remove_phone)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.sms.SmsService'

class SmsServiceClientSync(ConnectClientSync):

    def start_phone_verification(self, request: public_dot_sms__pb2.StartPhoneVerificationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.StartPhoneVerificationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='StartPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.StartPhoneVerificationRequest, output=public_dot_sms__pb2.StartPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def confirm_phone_verification(self, request: public_dot_sms__pb2.ConfirmPhoneVerificationRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.ConfirmPhoneVerificationResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ConfirmPhoneVerification', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.ConfirmPhoneVerificationRequest, output=public_dot_sms__pb2.ConfirmPhoneVerificationResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def set_sms_agent(self, request: public_dot_sms__pb2.SetSmsAgentRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.SetSmsAgentResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SetSmsAgent', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.SetSmsAgentRequest, output=public_dot_sms__pb2.SetSmsAgentResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def remove_phone(self, request: public_dot_sms__pb2.RemovePhoneRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_sms__pb2.RemovePhoneResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RemovePhone', service_name='textql.rpc.public.sms.SmsService', input=public_dot_sms__pb2.RemovePhoneRequest, output=public_dot_sms__pb2.RemovePhoneResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)