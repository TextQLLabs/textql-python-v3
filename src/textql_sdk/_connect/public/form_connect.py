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
from . import form_pb2 as public_dot_form__pb2

class FormService(Protocol):

    async def get_form(self, request: public_dot_form__pb2.GetFormRequest, ctx: RequestContext) -> public_dot_form__pb2.GetFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_forms(self, request: public_dot_form__pb2.ListFormsRequest, ctx: RequestContext) -> public_dot_form__pb2.ListFormsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def prepare_form_edit(self, request: public_dot_form__pb2.PrepareFormEditRequest, ctx: RequestContext) -> public_dot_form__pb2.PrepareFormEditResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def validate_form(self, request: public_dot_form__pb2.ValidateFormRequest, ctx: RequestContext) -> public_dot_form__pb2.ValidateFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_form_data(self, request: public_dot_form__pb2.UpdateFormDataRequest, ctx: RequestContext) -> public_dot_form__pb2.UpdateFormDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def test_form(self, request: public_dot_form__pb2.TestFormRequest, ctx: RequestContext) -> public_dot_form__pb2.TestFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_form_test(self, request: public_dot_form__pb2.GetFormTestRequest, ctx: RequestContext) -> public_dot_form__pb2.GetFormTestResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def submit_form(self, request: public_dot_form__pb2.SubmitFormRequest, ctx: RequestContext) -> public_dot_form__pb2.SubmitFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_form_status(self, request: public_dot_form__pb2.SetFormStatusRequest, ctx: RequestContext) -> public_dot_form__pb2.SetFormStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def backup_form_revision(self, request: public_dot_form__pb2.BackupFormRevisionRequest, ctx: RequestContext) -> public_dot_form__pb2.BackupFormRevisionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class FormServiceASGIApplication(ConnectASGIApplication[FormService]):

    def __init__(self, service: FormService | AsyncGenerator[FormService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.form.FormService/GetForm': Endpoint.unary(method=MethodInfo(name='GetForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormRequest, output=public_dot_form__pb2.GetFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_form), '/textql.rpc.public.form.FormService/ListForms': Endpoint.unary(method=MethodInfo(name='ListForms', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ListFormsRequest, output=public_dot_form__pb2.ListFormsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_forms), '/textql.rpc.public.form.FormService/PrepareFormEdit': Endpoint.unary(method=MethodInfo(name='PrepareFormEdit', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.PrepareFormEditRequest, output=public_dot_form__pb2.PrepareFormEditResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.prepare_form_edit), '/textql.rpc.public.form.FormService/ValidateForm': Endpoint.unary(method=MethodInfo(name='ValidateForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ValidateFormRequest, output=public_dot_form__pb2.ValidateFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.validate_form), '/textql.rpc.public.form.FormService/UpdateFormData': Endpoint.unary(method=MethodInfo(name='UpdateFormData', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.UpdateFormDataRequest, output=public_dot_form__pb2.UpdateFormDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_form_data), '/textql.rpc.public.form.FormService/TestForm': Endpoint.unary(method=MethodInfo(name='TestForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.TestFormRequest, output=public_dot_form__pb2.TestFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.test_form), '/textql.rpc.public.form.FormService/GetFormTest': Endpoint.unary(method=MethodInfo(name='GetFormTest', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormTestRequest, output=public_dot_form__pb2.GetFormTestResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_form_test), '/textql.rpc.public.form.FormService/SubmitForm': Endpoint.unary(method=MethodInfo(name='SubmitForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SubmitFormRequest, output=public_dot_form__pb2.SubmitFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.submit_form), '/textql.rpc.public.form.FormService/SetFormStatus': Endpoint.unary(method=MethodInfo(name='SetFormStatus', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SetFormStatusRequest, output=public_dot_form__pb2.SetFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_form_status), '/textql.rpc.public.form.FormService/BackupFormRevision': Endpoint.unary(method=MethodInfo(name='BackupFormRevision', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.BackupFormRevisionRequest, output=public_dot_form__pb2.BackupFormRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.backup_form_revision)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.form.FormService'

class FormServiceClient(ConnectClient):

    async def get_form(self, request: public_dot_form__pb2.GetFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.GetFormResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormRequest, output=public_dot_form__pb2.GetFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def list_forms(self, request: public_dot_form__pb2.ListFormsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.ListFormsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListForms', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ListFormsRequest, output=public_dot_form__pb2.ListFormsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def prepare_form_edit(self, request: public_dot_form__pb2.PrepareFormEditRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.PrepareFormEditResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='PrepareFormEdit', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.PrepareFormEditRequest, output=public_dot_form__pb2.PrepareFormEditResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def validate_form(self, request: public_dot_form__pb2.ValidateFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.ValidateFormResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ValidateForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ValidateFormRequest, output=public_dot_form__pb2.ValidateFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_form_data(self, request: public_dot_form__pb2.UpdateFormDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.UpdateFormDataResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateFormData', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.UpdateFormDataRequest, output=public_dot_form__pb2.UpdateFormDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def test_form(self, request: public_dot_form__pb2.TestFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.TestFormResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.TestFormRequest, output=public_dot_form__pb2.TestFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_form_test(self, request: public_dot_form__pb2.GetFormTestRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.GetFormTestResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetFormTest', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormTestRequest, output=public_dot_form__pb2.GetFormTestResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def submit_form(self, request: public_dot_form__pb2.SubmitFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.SubmitFormResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SubmitForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SubmitFormRequest, output=public_dot_form__pb2.SubmitFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def set_form_status(self, request: public_dot_form__pb2.SetFormStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.SetFormStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetFormStatus', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SetFormStatusRequest, output=public_dot_form__pb2.SetFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def backup_form_revision(self, request: public_dot_form__pb2.BackupFormRevisionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.BackupFormRevisionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='BackupFormRevision', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.BackupFormRevisionRequest, output=public_dot_form__pb2.BackupFormRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class FormServiceSync(Protocol):

    def get_form(self, request: public_dot_form__pb2.GetFormRequest, ctx: RequestContext) -> public_dot_form__pb2.GetFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_forms(self, request: public_dot_form__pb2.ListFormsRequest, ctx: RequestContext) -> public_dot_form__pb2.ListFormsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def prepare_form_edit(self, request: public_dot_form__pb2.PrepareFormEditRequest, ctx: RequestContext) -> public_dot_form__pb2.PrepareFormEditResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def validate_form(self, request: public_dot_form__pb2.ValidateFormRequest, ctx: RequestContext) -> public_dot_form__pb2.ValidateFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_form_data(self, request: public_dot_form__pb2.UpdateFormDataRequest, ctx: RequestContext) -> public_dot_form__pb2.UpdateFormDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def test_form(self, request: public_dot_form__pb2.TestFormRequest, ctx: RequestContext) -> public_dot_form__pb2.TestFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_form_test(self, request: public_dot_form__pb2.GetFormTestRequest, ctx: RequestContext) -> public_dot_form__pb2.GetFormTestResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def submit_form(self, request: public_dot_form__pb2.SubmitFormRequest, ctx: RequestContext) -> public_dot_form__pb2.SubmitFormResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_form_status(self, request: public_dot_form__pb2.SetFormStatusRequest, ctx: RequestContext) -> public_dot_form__pb2.SetFormStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def backup_form_revision(self, request: public_dot_form__pb2.BackupFormRevisionRequest, ctx: RequestContext) -> public_dot_form__pb2.BackupFormRevisionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class FormServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: FormServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.form.FormService/GetForm': EndpointSync.unary(method=MethodInfo(name='GetForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormRequest, output=public_dot_form__pb2.GetFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_form), '/textql.rpc.public.form.FormService/ListForms': EndpointSync.unary(method=MethodInfo(name='ListForms', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ListFormsRequest, output=public_dot_form__pb2.ListFormsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_forms), '/textql.rpc.public.form.FormService/PrepareFormEdit': EndpointSync.unary(method=MethodInfo(name='PrepareFormEdit', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.PrepareFormEditRequest, output=public_dot_form__pb2.PrepareFormEditResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.prepare_form_edit), '/textql.rpc.public.form.FormService/ValidateForm': EndpointSync.unary(method=MethodInfo(name='ValidateForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ValidateFormRequest, output=public_dot_form__pb2.ValidateFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.validate_form), '/textql.rpc.public.form.FormService/UpdateFormData': EndpointSync.unary(method=MethodInfo(name='UpdateFormData', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.UpdateFormDataRequest, output=public_dot_form__pb2.UpdateFormDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_form_data), '/textql.rpc.public.form.FormService/TestForm': EndpointSync.unary(method=MethodInfo(name='TestForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.TestFormRequest, output=public_dot_form__pb2.TestFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.test_form), '/textql.rpc.public.form.FormService/GetFormTest': EndpointSync.unary(method=MethodInfo(name='GetFormTest', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormTestRequest, output=public_dot_form__pb2.GetFormTestResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_form_test), '/textql.rpc.public.form.FormService/SubmitForm': EndpointSync.unary(method=MethodInfo(name='SubmitForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SubmitFormRequest, output=public_dot_form__pb2.SubmitFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.submit_form), '/textql.rpc.public.form.FormService/SetFormStatus': EndpointSync.unary(method=MethodInfo(name='SetFormStatus', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SetFormStatusRequest, output=public_dot_form__pb2.SetFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_form_status), '/textql.rpc.public.form.FormService/BackupFormRevision': EndpointSync.unary(method=MethodInfo(name='BackupFormRevision', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.BackupFormRevisionRequest, output=public_dot_form__pb2.BackupFormRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.backup_form_revision)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.form.FormService'

class FormServiceClientSync(ConnectClientSync):

    def get_form(self, request: public_dot_form__pb2.GetFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.GetFormResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormRequest, output=public_dot_form__pb2.GetFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def list_forms(self, request: public_dot_form__pb2.ListFormsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.ListFormsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListForms', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ListFormsRequest, output=public_dot_form__pb2.ListFormsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def prepare_form_edit(self, request: public_dot_form__pb2.PrepareFormEditRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.PrepareFormEditResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='PrepareFormEdit', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.PrepareFormEditRequest, output=public_dot_form__pb2.PrepareFormEditResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def validate_form(self, request: public_dot_form__pb2.ValidateFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.ValidateFormResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ValidateForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.ValidateFormRequest, output=public_dot_form__pb2.ValidateFormResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_form_data(self, request: public_dot_form__pb2.UpdateFormDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.UpdateFormDataResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateFormData', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.UpdateFormDataRequest, output=public_dot_form__pb2.UpdateFormDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def test_form(self, request: public_dot_form__pb2.TestFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.TestFormResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.TestFormRequest, output=public_dot_form__pb2.TestFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_form_test(self, request: public_dot_form__pb2.GetFormTestRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_form__pb2.GetFormTestResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetFormTest', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.GetFormTestRequest, output=public_dot_form__pb2.GetFormTestResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def submit_form(self, request: public_dot_form__pb2.SubmitFormRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.SubmitFormResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SubmitForm', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SubmitFormRequest, output=public_dot_form__pb2.SubmitFormResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def set_form_status(self, request: public_dot_form__pb2.SetFormStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.SetFormStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SetFormStatus', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.SetFormStatusRequest, output=public_dot_form__pb2.SetFormStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def backup_form_revision(self, request: public_dot_form__pb2.BackupFormRevisionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_form__pb2.BackupFormRevisionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='BackupFormRevision', service_name='textql.rpc.public.form.FormService', input=public_dot_form__pb2.BackupFormRevisionRequest, output=public_dot_form__pb2.BackupFormRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)