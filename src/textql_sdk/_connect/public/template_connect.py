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
from . import template_pb2 as public_dot_template__pb2

class TemplateService(Protocol):

    async def create_playbook_template_header(self, request: public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_playbook_template_header(self, request: public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_playbook_template_header(self, request: public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_playbook_template_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_playbook_template_headers(self, request: public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, ctx: RequestContext) -> public_dot_template__pb2.ListPlaybookTemplateHeadersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_playbook_template_data(self, request: public_dot_template__pb2.CreatePlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.CreatePlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_playbook_template_data(self, request: public_dot_template__pb2.GetPlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_playbook_template_data_by_header(self, request: public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_playbook_template_data_with_batch_status(self, request: public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def search_playbook_template_data(self, request: public_dot_template__pb2.SearchPlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.SearchPlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_playbook_template_data(self, request: public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.UpdatePlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_playbook_template_data(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_playbook_template_data_by_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_template_from_c_s_v(self, request: public_dot_template__pb2.CreateTemplateFromCSVRequest, ctx: RequestContext) -> public_dot_template__pb2.CreateTemplateFromCSVResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_template_from_x_l_s_x(self, request: public_dot_template__pb2.CreateTemplateFromXLSXRequest, ctx: RequestContext) -> public_dot_template__pb2.CreateTemplateFromXLSXResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TemplateServiceASGIApplication(ConnectASGIApplication[TemplateService]):

    def __init__(self, service: TemplateService | AsyncGenerator[TemplateService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.template.TemplateService/CreatePlaybookTemplateHeader': Endpoint.unary(method=MethodInfo(name='CreatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_playbook_template_header), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateHeader': Endpoint.unary(method=MethodInfo(name='GetPlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_playbook_template_header), '/textql.rpc.public.template.TemplateService/UpdatePlaybookTemplateHeader': Endpoint.unary(method=MethodInfo(name='UpdatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_playbook_template_header), '/textql.rpc.public.template.TemplateService/DeletePlaybookTemplateHeader': Endpoint.unary(method=MethodInfo(name='DeletePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_playbook_template_header), '/textql.rpc.public.template.TemplateService/ListPlaybookTemplateHeaders': Endpoint.unary(method=MethodInfo(name='ListPlaybookTemplateHeaders', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, output=public_dot_template__pb2.ListPlaybookTemplateHeadersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_playbook_template_headers), '/textql.rpc.public.template.TemplateService/CreatePlaybookTemplateData': Endpoint.unary(method=MethodInfo(name='CreatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateDataRequest, output=public_dot_template__pb2.CreatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_playbook_template_data), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateData': Endpoint.unary(method=MethodInfo(name='GetPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_playbook_template_data), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateDataByHeader': Endpoint.unary(method=MethodInfo(name='GetPlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_playbook_template_data_by_header), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateDataWithBatchStatus': Endpoint.unary(method=MethodInfo(name='GetPlaybookTemplateDataWithBatchStatus', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_playbook_template_data_with_batch_status), '/textql.rpc.public.template.TemplateService/SearchPlaybookTemplateData': Endpoint.unary(method=MethodInfo(name='SearchPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.SearchPlaybookTemplateDataRequest, output=public_dot_template__pb2.SearchPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.search_playbook_template_data), '/textql.rpc.public.template.TemplateService/UpdatePlaybookTemplateData': Endpoint.unary(method=MethodInfo(name='UpdatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_playbook_template_data), '/textql.rpc.public.template.TemplateService/DeletePlaybookTemplateData': Endpoint.unary(method=MethodInfo(name='DeletePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_playbook_template_data), '/textql.rpc.public.template.TemplateService/DeletePlaybookTemplateDataByHeader': Endpoint.unary(method=MethodInfo(name='DeletePlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_playbook_template_data_by_header), '/textql.rpc.public.template.TemplateService/CreateTemplateFromCSV': Endpoint.unary(method=MethodInfo(name='CreateTemplateFromCSV', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromCSVRequest, output=public_dot_template__pb2.CreateTemplateFromCSVResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_template_from_c_s_v), '/textql.rpc.public.template.TemplateService/CreateTemplateFromXLSX': Endpoint.unary(method=MethodInfo(name='CreateTemplateFromXLSX', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromXLSXRequest, output=public_dot_template__pb2.CreateTemplateFromXLSXResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_template_from_x_l_s_x)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.template.TemplateService'

class TemplateServiceClient(ConnectClient):

    async def create_playbook_template_header(self, request: public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_playbook_template_header(self, request: public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateHeaderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_playbook_template_header(self, request: public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_playbook_template_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeletePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_playbook_template_headers(self, request: public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.ListPlaybookTemplateHeadersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListPlaybookTemplateHeaders', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, output=public_dot_template__pb2.ListPlaybookTemplateHeadersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def create_playbook_template_data(self, request: public_dot_template__pb2.CreatePlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreatePlaybookTemplateDataResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateDataRequest, output=public_dot_template__pb2.CreatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_playbook_template_data(self, request: public_dot_template__pb2.GetPlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateDataResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_playbook_template_data_by_header(self, request: public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_playbook_template_data_with_batch_status(self, request: public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateDataWithBatchStatus', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def search_playbook_template_data(self, request: public_dot_template__pb2.SearchPlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.SearchPlaybookTemplateDataResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SearchPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.SearchPlaybookTemplateDataRequest, output=public_dot_template__pb2.SearchPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_playbook_template_data(self, request: public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.UpdatePlaybookTemplateDataResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_playbook_template_data(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeletePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_playbook_template_data_by_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeletePlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_template_from_c_s_v(self, request: public_dot_template__pb2.CreateTemplateFromCSVRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreateTemplateFromCSVResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateTemplateFromCSV', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromCSVRequest, output=public_dot_template__pb2.CreateTemplateFromCSVResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_template_from_x_l_s_x(self, request: public_dot_template__pb2.CreateTemplateFromXLSXRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreateTemplateFromXLSXResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateTemplateFromXLSX', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromXLSXRequest, output=public_dot_template__pb2.CreateTemplateFromXLSXResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class TemplateServiceSync(Protocol):

    def create_playbook_template_header(self, request: public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_playbook_template_header(self, request: public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_playbook_template_header(self, request: public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_playbook_template_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_playbook_template_headers(self, request: public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, ctx: RequestContext) -> public_dot_template__pb2.ListPlaybookTemplateHeadersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_playbook_template_data(self, request: public_dot_template__pb2.CreatePlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.CreatePlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_playbook_template_data(self, request: public_dot_template__pb2.GetPlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_playbook_template_data_by_header(self, request: public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_playbook_template_data_with_batch_status(self, request: public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, ctx: RequestContext) -> public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def search_playbook_template_data(self, request: public_dot_template__pb2.SearchPlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.SearchPlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_playbook_template_data(self, request: public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, ctx: RequestContext) -> public_dot_template__pb2.UpdatePlaybookTemplateDataResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_playbook_template_data(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_playbook_template_data_by_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, ctx: RequestContext) -> google_dot_protobuf_dot_empty__pb2.Empty:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_template_from_c_s_v(self, request: public_dot_template__pb2.CreateTemplateFromCSVRequest, ctx: RequestContext) -> public_dot_template__pb2.CreateTemplateFromCSVResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_template_from_x_l_s_x(self, request: public_dot_template__pb2.CreateTemplateFromXLSXRequest, ctx: RequestContext) -> public_dot_template__pb2.CreateTemplateFromXLSXResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class TemplateServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: TemplateServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.template.TemplateService/CreatePlaybookTemplateHeader': EndpointSync.unary(method=MethodInfo(name='CreatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_playbook_template_header), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateHeader': EndpointSync.unary(method=MethodInfo(name='GetPlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_playbook_template_header), '/textql.rpc.public.template.TemplateService/UpdatePlaybookTemplateHeader': EndpointSync.unary(method=MethodInfo(name='UpdatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_playbook_template_header), '/textql.rpc.public.template.TemplateService/DeletePlaybookTemplateHeader': EndpointSync.unary(method=MethodInfo(name='DeletePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_playbook_template_header), '/textql.rpc.public.template.TemplateService/ListPlaybookTemplateHeaders': EndpointSync.unary(method=MethodInfo(name='ListPlaybookTemplateHeaders', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, output=public_dot_template__pb2.ListPlaybookTemplateHeadersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_playbook_template_headers), '/textql.rpc.public.template.TemplateService/CreatePlaybookTemplateData': EndpointSync.unary(method=MethodInfo(name='CreatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateDataRequest, output=public_dot_template__pb2.CreatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_playbook_template_data), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateData': EndpointSync.unary(method=MethodInfo(name='GetPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_playbook_template_data), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateDataByHeader': EndpointSync.unary(method=MethodInfo(name='GetPlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_playbook_template_data_by_header), '/textql.rpc.public.template.TemplateService/GetPlaybookTemplateDataWithBatchStatus': EndpointSync.unary(method=MethodInfo(name='GetPlaybookTemplateDataWithBatchStatus', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_playbook_template_data_with_batch_status), '/textql.rpc.public.template.TemplateService/SearchPlaybookTemplateData': EndpointSync.unary(method=MethodInfo(name='SearchPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.SearchPlaybookTemplateDataRequest, output=public_dot_template__pb2.SearchPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.search_playbook_template_data), '/textql.rpc.public.template.TemplateService/UpdatePlaybookTemplateData': EndpointSync.unary(method=MethodInfo(name='UpdatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_playbook_template_data), '/textql.rpc.public.template.TemplateService/DeletePlaybookTemplateData': EndpointSync.unary(method=MethodInfo(name='DeletePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_playbook_template_data), '/textql.rpc.public.template.TemplateService/DeletePlaybookTemplateDataByHeader': EndpointSync.unary(method=MethodInfo(name='DeletePlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_playbook_template_data_by_header), '/textql.rpc.public.template.TemplateService/CreateTemplateFromCSV': EndpointSync.unary(method=MethodInfo(name='CreateTemplateFromCSV', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromCSVRequest, output=public_dot_template__pb2.CreateTemplateFromCSVResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_template_from_c_s_v), '/textql.rpc.public.template.TemplateService/CreateTemplateFromXLSX': EndpointSync.unary(method=MethodInfo(name='CreateTemplateFromXLSX', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromXLSXRequest, output=public_dot_template__pb2.CreateTemplateFromXLSXResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_template_from_x_l_s_x)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.template.TemplateService'

class TemplateServiceClientSync(ConnectClientSync):

    def create_playbook_template_header(self, request: public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.CreatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_playbook_template_header(self, request: public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateHeaderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_playbook_template_header(self, request: public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdatePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateHeaderRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateHeaderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_playbook_template_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeletePlaybookTemplateHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_playbook_template_headers(self, request: public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.ListPlaybookTemplateHeadersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListPlaybookTemplateHeaders', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.ListPlaybookTemplateHeadersRequest, output=public_dot_template__pb2.ListPlaybookTemplateHeadersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def create_playbook_template_data(self, request: public_dot_template__pb2.CreatePlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreatePlaybookTemplateDataResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreatePlaybookTemplateDataRequest, output=public_dot_template__pb2.CreatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_playbook_template_data(self, request: public_dot_template__pb2.GetPlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateDataResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_playbook_template_data_by_header(self, request: public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataByHeaderResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_playbook_template_data_with_batch_status(self, request: public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetPlaybookTemplateDataWithBatchStatus', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusRequest, output=public_dot_template__pb2.GetPlaybookTemplateDataWithBatchStatusResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def search_playbook_template_data(self, request: public_dot_template__pb2.SearchPlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_template__pb2.SearchPlaybookTemplateDataResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SearchPlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.SearchPlaybookTemplateDataRequest, output=public_dot_template__pb2.SearchPlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_playbook_template_data(self, request: public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.UpdatePlaybookTemplateDataResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdatePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.UpdatePlaybookTemplateDataRequest, output=public_dot_template__pb2.UpdatePlaybookTemplateDataResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_playbook_template_data(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeletePlaybookTemplateData', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_playbook_template_data_by_header(self, request: public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> google_dot_protobuf_dot_empty__pb2.Empty:
        return self.execute_unary(request=request, method=MethodInfo(name='DeletePlaybookTemplateDataByHeader', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.DeletePlaybookTemplateDataByHeaderRequest, output=google_dot_protobuf_dot_empty__pb2.Empty, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_template_from_c_s_v(self, request: public_dot_template__pb2.CreateTemplateFromCSVRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreateTemplateFromCSVResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateTemplateFromCSV', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromCSVRequest, output=public_dot_template__pb2.CreateTemplateFromCSVResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_template_from_x_l_s_x(self, request: public_dot_template__pb2.CreateTemplateFromXLSXRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_template__pb2.CreateTemplateFromXLSXResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateTemplateFromXLSX', service_name='textql.rpc.public.template.TemplateService', input=public_dot_template__pb2.CreateTemplateFromXLSXRequest, output=public_dot_template__pb2.CreateTemplateFromXLSXResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)