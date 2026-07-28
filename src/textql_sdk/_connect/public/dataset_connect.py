# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
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
from . import dataset_pb2 as public_dot_dataset__pb2

class DatasetService(Protocol):

    async def create_folder(self, request: public_dot_dataset__pb2.CreateFolderRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreateFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_folders(self, request: public_dot_dataset__pb2.GetFoldersRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetFoldersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_upload_presign_url(self, request: public_dot_dataset__pb2.CreateUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreateUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def process_upload_presign_url(self, request: public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_dataset__pb2.ProcessUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_dataset(self, request: public_dot_dataset__pb2.GetDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_datasets(self, request: public_dot_dataset__pb2.GetDatasetsRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_datasets_by_ids(self, request: public_dot_dataset__pb2.GetDatasetsByIdsRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetsByIdsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_dataset(self, request: public_dot_dataset__pb2.UpdateDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.UpdateDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def export_dataset(self, request: public_dot_dataset__pb2.ExportDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.ExportDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_dataset_values(self, request: public_dot_dataset__pb2.GetDatasetValuesRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetValuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_dataset_stats(self, request: public_dot_dataset__pb2.GetDatasetStatsRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_tableau_dataset(self, request: public_dot_dataset__pb2.CreateTableauDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreateTableauDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_power_b_i_dataset(self, request: public_dot_dataset__pb2.CreatePowerBIDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreatePowerBIDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_dataset(self, request: public_dot_dataset__pb2.DeleteDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.DeleteDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class DatasetServiceASGIApplication(ConnectASGIApplication[DatasetService]):

    def __init__(self, service: DatasetService | AsyncGenerator[DatasetService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.dataset.DatasetService/CreateFolder': Endpoint.unary(method=MethodInfo(name='CreateFolder', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateFolderRequest, output=public_dot_dataset__pb2.CreateFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_folder), '/textql.rpc.public.dataset.DatasetService/GetFolders': Endpoint.unary(method=MethodInfo(name='GetFolders', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetFoldersRequest, output=public_dot_dataset__pb2.GetFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_folders), '/textql.rpc.public.dataset.DatasetService/CreateUploadPresignUrl': Endpoint.unary(method=MethodInfo(name='CreateUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateUploadPresignUrlRequest, output=public_dot_dataset__pb2.CreateUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_upload_presign_url), '/textql.rpc.public.dataset.DatasetService/ProcessUploadPresignUrl': Endpoint.unary(method=MethodInfo(name='ProcessUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, output=public_dot_dataset__pb2.ProcessUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.process_upload_presign_url), '/textql.rpc.public.dataset.DatasetService/GetDataset': Endpoint.unary(method=MethodInfo(name='GetDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetRequest, output=public_dot_dataset__pb2.GetDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_dataset), '/textql.rpc.public.dataset.DatasetService/GetDatasets': Endpoint.unary(method=MethodInfo(name='GetDatasets', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsRequest, output=public_dot_dataset__pb2.GetDatasetsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_datasets), '/textql.rpc.public.dataset.DatasetService/GetDatasetsByIds': Endpoint.unary(method=MethodInfo(name='GetDatasetsByIds', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsByIdsRequest, output=public_dot_dataset__pb2.GetDatasetsByIdsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_datasets_by_ids), '/textql.rpc.public.dataset.DatasetService/UpdateDataset': Endpoint.unary(method=MethodInfo(name='UpdateDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.UpdateDatasetRequest, output=public_dot_dataset__pb2.UpdateDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), function=svc.update_dataset), '/textql.rpc.public.dataset.DatasetService/ExportDataset': Endpoint.unary(method=MethodInfo(name='ExportDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ExportDatasetRequest, output=public_dot_dataset__pb2.ExportDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.export_dataset), '/textql.rpc.public.dataset.DatasetService/GetDatasetValues': Endpoint.unary(method=MethodInfo(name='GetDatasetValues', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetValuesRequest, output=public_dot_dataset__pb2.GetDatasetValuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_dataset_values), '/textql.rpc.public.dataset.DatasetService/GetDatasetStats': Endpoint.unary(method=MethodInfo(name='GetDatasetStats', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetStatsRequest, output=public_dot_dataset__pb2.GetDatasetStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_dataset_stats), '/textql.rpc.public.dataset.DatasetService/CreateTableauDataset': Endpoint.unary(method=MethodInfo(name='CreateTableauDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateTableauDatasetRequest, output=public_dot_dataset__pb2.CreateTableauDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_tableau_dataset), '/textql.rpc.public.dataset.DatasetService/CreatePowerBIDataset': Endpoint.unary(method=MethodInfo(name='CreatePowerBIDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreatePowerBIDatasetRequest, output=public_dot_dataset__pb2.CreatePowerBIDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_power_b_i_dataset), '/textql.rpc.public.dataset.DatasetService/DeleteDataset': Endpoint.unary(method=MethodInfo(name='DeleteDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.DeleteDatasetRequest, output=public_dot_dataset__pb2.DeleteDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), function=svc.delete_dataset)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.dataset.DatasetService'

class DatasetServiceClient(ConnectClient):

    async def create_folder(self, request: public_dot_dataset__pb2.CreateFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreateFolderResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateFolder', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateFolderRequest, output=public_dot_dataset__pb2.CreateFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_folders(self, request: public_dot_dataset__pb2.GetFoldersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetFoldersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetFolders', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetFoldersRequest, output=public_dot_dataset__pb2.GetFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def create_upload_presign_url(self, request: public_dot_dataset__pb2.CreateUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreateUploadPresignUrlResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateUploadPresignUrlRequest, output=public_dot_dataset__pb2.CreateUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def process_upload_presign_url(self, request: public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.ProcessUploadPresignUrlResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ProcessUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, output=public_dot_dataset__pb2.ProcessUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_dataset(self, request: public_dot_dataset__pb2.GetDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetRequest, output=public_dot_dataset__pb2.GetDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_datasets(self, request: public_dot_dataset__pb2.GetDatasetsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDatasets', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsRequest, output=public_dot_dataset__pb2.GetDatasetsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_datasets_by_ids(self, request: public_dot_dataset__pb2.GetDatasetsByIdsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetsByIdsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDatasetsByIds', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsByIdsRequest, output=public_dot_dataset__pb2.GetDatasetsByIdsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def update_dataset(self, request: public_dot_dataset__pb2.UpdateDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.UpdateDatasetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.UpdateDatasetRequest, output=public_dot_dataset__pb2.UpdateDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), headers=headers, timeout_ms=timeout_ms)

    async def export_dataset(self, request: public_dot_dataset__pb2.ExportDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.ExportDatasetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ExportDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ExportDatasetRequest, output=public_dot_dataset__pb2.ExportDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_dataset_values(self, request: public_dot_dataset__pb2.GetDatasetValuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetValuesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDatasetValues', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetValuesRequest, output=public_dot_dataset__pb2.GetDatasetValuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_dataset_stats(self, request: public_dot_dataset__pb2.GetDatasetStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetStatsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetDatasetStats', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetStatsRequest, output=public_dot_dataset__pb2.GetDatasetStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def create_tableau_dataset(self, request: public_dot_dataset__pb2.CreateTableauDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreateTableauDatasetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateTableauDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateTableauDatasetRequest, output=public_dot_dataset__pb2.CreateTableauDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_power_b_i_dataset(self, request: public_dot_dataset__pb2.CreatePowerBIDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreatePowerBIDatasetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreatePowerBIDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreatePowerBIDatasetRequest, output=public_dot_dataset__pb2.CreatePowerBIDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_dataset(self, request: public_dot_dataset__pb2.DeleteDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.DeleteDatasetResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.DeleteDatasetRequest, output=public_dot_dataset__pb2.DeleteDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), headers=headers, timeout_ms=timeout_ms)

class DatasetServiceSync(Protocol):

    def create_folder(self, request: public_dot_dataset__pb2.CreateFolderRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreateFolderResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_folders(self, request: public_dot_dataset__pb2.GetFoldersRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetFoldersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_upload_presign_url(self, request: public_dot_dataset__pb2.CreateUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreateUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def process_upload_presign_url(self, request: public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, ctx: RequestContext) -> public_dot_dataset__pb2.ProcessUploadPresignUrlResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_dataset(self, request: public_dot_dataset__pb2.GetDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_datasets(self, request: public_dot_dataset__pb2.GetDatasetsRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_datasets_by_ids(self, request: public_dot_dataset__pb2.GetDatasetsByIdsRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetsByIdsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_dataset(self, request: public_dot_dataset__pb2.UpdateDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.UpdateDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def export_dataset(self, request: public_dot_dataset__pb2.ExportDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.ExportDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_dataset_values(self, request: public_dot_dataset__pb2.GetDatasetValuesRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetValuesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_dataset_stats(self, request: public_dot_dataset__pb2.GetDatasetStatsRequest, ctx: RequestContext) -> public_dot_dataset__pb2.GetDatasetStatsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_tableau_dataset(self, request: public_dot_dataset__pb2.CreateTableauDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreateTableauDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_power_b_i_dataset(self, request: public_dot_dataset__pb2.CreatePowerBIDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.CreatePowerBIDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_dataset(self, request: public_dot_dataset__pb2.DeleteDatasetRequest, ctx: RequestContext) -> public_dot_dataset__pb2.DeleteDatasetResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class DatasetServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: DatasetServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.dataset.DatasetService/CreateFolder': EndpointSync.unary(method=MethodInfo(name='CreateFolder', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateFolderRequest, output=public_dot_dataset__pb2.CreateFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_folder), '/textql.rpc.public.dataset.DatasetService/GetFolders': EndpointSync.unary(method=MethodInfo(name='GetFolders', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetFoldersRequest, output=public_dot_dataset__pb2.GetFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_folders), '/textql.rpc.public.dataset.DatasetService/CreateUploadPresignUrl': EndpointSync.unary(method=MethodInfo(name='CreateUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateUploadPresignUrlRequest, output=public_dot_dataset__pb2.CreateUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_upload_presign_url), '/textql.rpc.public.dataset.DatasetService/ProcessUploadPresignUrl': EndpointSync.unary(method=MethodInfo(name='ProcessUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, output=public_dot_dataset__pb2.ProcessUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.process_upload_presign_url), '/textql.rpc.public.dataset.DatasetService/GetDataset': EndpointSync.unary(method=MethodInfo(name='GetDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetRequest, output=public_dot_dataset__pb2.GetDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_dataset), '/textql.rpc.public.dataset.DatasetService/GetDatasets': EndpointSync.unary(method=MethodInfo(name='GetDatasets', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsRequest, output=public_dot_dataset__pb2.GetDatasetsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_datasets), '/textql.rpc.public.dataset.DatasetService/GetDatasetsByIds': EndpointSync.unary(method=MethodInfo(name='GetDatasetsByIds', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsByIdsRequest, output=public_dot_dataset__pb2.GetDatasetsByIdsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_datasets_by_ids), '/textql.rpc.public.dataset.DatasetService/UpdateDataset': EndpointSync.unary(method=MethodInfo(name='UpdateDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.UpdateDatasetRequest, output=public_dot_dataset__pb2.UpdateDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), function=service.update_dataset), '/textql.rpc.public.dataset.DatasetService/ExportDataset': EndpointSync.unary(method=MethodInfo(name='ExportDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ExportDatasetRequest, output=public_dot_dataset__pb2.ExportDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.export_dataset), '/textql.rpc.public.dataset.DatasetService/GetDatasetValues': EndpointSync.unary(method=MethodInfo(name='GetDatasetValues', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetValuesRequest, output=public_dot_dataset__pb2.GetDatasetValuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_dataset_values), '/textql.rpc.public.dataset.DatasetService/GetDatasetStats': EndpointSync.unary(method=MethodInfo(name='GetDatasetStats', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetStatsRequest, output=public_dot_dataset__pb2.GetDatasetStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_dataset_stats), '/textql.rpc.public.dataset.DatasetService/CreateTableauDataset': EndpointSync.unary(method=MethodInfo(name='CreateTableauDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateTableauDatasetRequest, output=public_dot_dataset__pb2.CreateTableauDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_tableau_dataset), '/textql.rpc.public.dataset.DatasetService/CreatePowerBIDataset': EndpointSync.unary(method=MethodInfo(name='CreatePowerBIDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreatePowerBIDatasetRequest, output=public_dot_dataset__pb2.CreatePowerBIDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_power_b_i_dataset), '/textql.rpc.public.dataset.DatasetService/DeleteDataset': EndpointSync.unary(method=MethodInfo(name='DeleteDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.DeleteDatasetRequest, output=public_dot_dataset__pb2.DeleteDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), function=service.delete_dataset)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.dataset.DatasetService'

class DatasetServiceClientSync(ConnectClientSync):

    def create_folder(self, request: public_dot_dataset__pb2.CreateFolderRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreateFolderResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateFolder', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateFolderRequest, output=public_dot_dataset__pb2.CreateFolderResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_folders(self, request: public_dot_dataset__pb2.GetFoldersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetFoldersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetFolders', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetFoldersRequest, output=public_dot_dataset__pb2.GetFoldersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def create_upload_presign_url(self, request: public_dot_dataset__pb2.CreateUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreateUploadPresignUrlResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateUploadPresignUrlRequest, output=public_dot_dataset__pb2.CreateUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def process_upload_presign_url(self, request: public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.ProcessUploadPresignUrlResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ProcessUploadPresignUrl', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ProcessUploadPresignUrlRequest, output=public_dot_dataset__pb2.ProcessUploadPresignUrlResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_dataset(self, request: public_dot_dataset__pb2.GetDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetRequest, output=public_dot_dataset__pb2.GetDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_datasets(self, request: public_dot_dataset__pb2.GetDatasetsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDatasets', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsRequest, output=public_dot_dataset__pb2.GetDatasetsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_datasets_by_ids(self, request: public_dot_dataset__pb2.GetDatasetsByIdsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetsByIdsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDatasetsByIds', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetsByIdsRequest, output=public_dot_dataset__pb2.GetDatasetsByIdsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def update_dataset(self, request: public_dot_dataset__pb2.UpdateDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.UpdateDatasetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.UpdateDatasetRequest, output=public_dot_dataset__pb2.UpdateDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), headers=headers, timeout_ms=timeout_ms)

    def export_dataset(self, request: public_dot_dataset__pb2.ExportDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.ExportDatasetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ExportDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.ExportDatasetRequest, output=public_dot_dataset__pb2.ExportDatasetResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_dataset_values(self, request: public_dot_dataset__pb2.GetDatasetValuesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetValuesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDatasetValues', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetValuesRequest, output=public_dot_dataset__pb2.GetDatasetValuesResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_dataset_stats(self, request: public_dot_dataset__pb2.GetDatasetStatsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_dataset__pb2.GetDatasetStatsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetDatasetStats', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.GetDatasetStatsRequest, output=public_dot_dataset__pb2.GetDatasetStatsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def create_tableau_dataset(self, request: public_dot_dataset__pb2.CreateTableauDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreateTableauDatasetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateTableauDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreateTableauDatasetRequest, output=public_dot_dataset__pb2.CreateTableauDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_power_b_i_dataset(self, request: public_dot_dataset__pb2.CreatePowerBIDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.CreatePowerBIDatasetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreatePowerBIDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.CreatePowerBIDatasetRequest, output=public_dot_dataset__pb2.CreatePowerBIDatasetResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_dataset(self, request: public_dot_dataset__pb2.DeleteDatasetRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_dataset__pb2.DeleteDatasetResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteDataset', service_name='textql.rpc.public.dataset.DatasetService', input=public_dot_dataset__pb2.DeleteDatasetRequest, output=public_dot_dataset__pb2.DeleteDatasetResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), headers=headers, timeout_ms=timeout_ms)