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
from . import packages_pb2 as public_dot_packages__pb2

class OrgPackageService(Protocol):

    async def list_org_packages(self, request: public_dot_packages__pb2.ListOrgPackagesRequest, ctx: RequestContext) -> public_dot_packages__pb2.ListOrgPackagesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def install_org_package(self, request: public_dot_packages__pb2.InstallOrgPackageRequest, ctx: RequestContext) -> public_dot_packages__pb2.InstallOrgPackageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def remove_org_package(self, request: public_dot_packages__pb2.RemoveOrgPackageRequest, ctx: RequestContext) -> public_dot_packages__pb2.RemoveOrgPackageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_org_package_status(self, request: public_dot_packages__pb2.GetOrgPackageStatusRequest, ctx: RequestContext) -> public_dot_packages__pb2.GetOrgPackageStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def retry_install_org_package(self, request: public_dot_packages__pb2.RetryInstallOrgPackageRequest, ctx: RequestContext) -> public_dot_packages__pb2.RetryInstallOrgPackageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_org_package_version(self, request: public_dot_packages__pb2.UpdateOrgPackageVersionRequest, ctx: RequestContext) -> public_dot_packages__pb2.UpdateOrgPackageVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class OrgPackageServiceASGIApplication(ConnectASGIApplication[OrgPackageService]):

    def __init__(self, service: OrgPackageService | AsyncGenerator[OrgPackageService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.packages.OrgPackageService/ListOrgPackages': Endpoint.unary(method=MethodInfo(name='ListOrgPackages', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.ListOrgPackagesRequest, output=public_dot_packages__pb2.ListOrgPackagesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_org_packages), '/textql.rpc.public.packages.OrgPackageService/InstallOrgPackage': Endpoint.unary(method=MethodInfo(name='InstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.InstallOrgPackageRequest, output=public_dot_packages__pb2.InstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.install_org_package), '/textql.rpc.public.packages.OrgPackageService/RemoveOrgPackage': Endpoint.unary(method=MethodInfo(name='RemoveOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RemoveOrgPackageRequest, output=public_dot_packages__pb2.RemoveOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.remove_org_package), '/textql.rpc.public.packages.OrgPackageService/GetOrgPackageStatus': Endpoint.unary(method=MethodInfo(name='GetOrgPackageStatus', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.GetOrgPackageStatusRequest, output=public_dot_packages__pb2.GetOrgPackageStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_org_package_status), '/textql.rpc.public.packages.OrgPackageService/RetryInstallOrgPackage': Endpoint.unary(method=MethodInfo(name='RetryInstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RetryInstallOrgPackageRequest, output=public_dot_packages__pb2.RetryInstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.retry_install_org_package), '/textql.rpc.public.packages.OrgPackageService/UpdateOrgPackageVersion': Endpoint.unary(method=MethodInfo(name='UpdateOrgPackageVersion', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.UpdateOrgPackageVersionRequest, output=public_dot_packages__pb2.UpdateOrgPackageVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_org_package_version)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.packages.OrgPackageService'

class OrgPackageServiceClient(ConnectClient):

    async def list_org_packages(self, request: public_dot_packages__pb2.ListOrgPackagesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.ListOrgPackagesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListOrgPackages', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.ListOrgPackagesRequest, output=public_dot_packages__pb2.ListOrgPackagesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def install_org_package(self, request: public_dot_packages__pb2.InstallOrgPackageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.InstallOrgPackageResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='InstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.InstallOrgPackageRequest, output=public_dot_packages__pb2.InstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def remove_org_package(self, request: public_dot_packages__pb2.RemoveOrgPackageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.RemoveOrgPackageResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RemoveOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RemoveOrgPackageRequest, output=public_dot_packages__pb2.RemoveOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_org_package_status(self, request: public_dot_packages__pb2.GetOrgPackageStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.GetOrgPackageStatusResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetOrgPackageStatus', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.GetOrgPackageStatusRequest, output=public_dot_packages__pb2.GetOrgPackageStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def retry_install_org_package(self, request: public_dot_packages__pb2.RetryInstallOrgPackageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.RetryInstallOrgPackageResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RetryInstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RetryInstallOrgPackageRequest, output=public_dot_packages__pb2.RetryInstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_org_package_version(self, request: public_dot_packages__pb2.UpdateOrgPackageVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.UpdateOrgPackageVersionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgPackageVersion', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.UpdateOrgPackageVersionRequest, output=public_dot_packages__pb2.UpdateOrgPackageVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class OrgPackageServiceSync(Protocol):

    def list_org_packages(self, request: public_dot_packages__pb2.ListOrgPackagesRequest, ctx: RequestContext) -> public_dot_packages__pb2.ListOrgPackagesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def install_org_package(self, request: public_dot_packages__pb2.InstallOrgPackageRequest, ctx: RequestContext) -> public_dot_packages__pb2.InstallOrgPackageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def remove_org_package(self, request: public_dot_packages__pb2.RemoveOrgPackageRequest, ctx: RequestContext) -> public_dot_packages__pb2.RemoveOrgPackageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_org_package_status(self, request: public_dot_packages__pb2.GetOrgPackageStatusRequest, ctx: RequestContext) -> public_dot_packages__pb2.GetOrgPackageStatusResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def retry_install_org_package(self, request: public_dot_packages__pb2.RetryInstallOrgPackageRequest, ctx: RequestContext) -> public_dot_packages__pb2.RetryInstallOrgPackageResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_org_package_version(self, request: public_dot_packages__pb2.UpdateOrgPackageVersionRequest, ctx: RequestContext) -> public_dot_packages__pb2.UpdateOrgPackageVersionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class OrgPackageServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: OrgPackageServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.packages.OrgPackageService/ListOrgPackages': EndpointSync.unary(method=MethodInfo(name='ListOrgPackages', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.ListOrgPackagesRequest, output=public_dot_packages__pb2.ListOrgPackagesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_org_packages), '/textql.rpc.public.packages.OrgPackageService/InstallOrgPackage': EndpointSync.unary(method=MethodInfo(name='InstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.InstallOrgPackageRequest, output=public_dot_packages__pb2.InstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.install_org_package), '/textql.rpc.public.packages.OrgPackageService/RemoveOrgPackage': EndpointSync.unary(method=MethodInfo(name='RemoveOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RemoveOrgPackageRequest, output=public_dot_packages__pb2.RemoveOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.remove_org_package), '/textql.rpc.public.packages.OrgPackageService/GetOrgPackageStatus': EndpointSync.unary(method=MethodInfo(name='GetOrgPackageStatus', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.GetOrgPackageStatusRequest, output=public_dot_packages__pb2.GetOrgPackageStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_org_package_status), '/textql.rpc.public.packages.OrgPackageService/RetryInstallOrgPackage': EndpointSync.unary(method=MethodInfo(name='RetryInstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RetryInstallOrgPackageRequest, output=public_dot_packages__pb2.RetryInstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.retry_install_org_package), '/textql.rpc.public.packages.OrgPackageService/UpdateOrgPackageVersion': EndpointSync.unary(method=MethodInfo(name='UpdateOrgPackageVersion', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.UpdateOrgPackageVersionRequest, output=public_dot_packages__pb2.UpdateOrgPackageVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_org_package_version)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.packages.OrgPackageService'

class OrgPackageServiceClientSync(ConnectClientSync):

    def list_org_packages(self, request: public_dot_packages__pb2.ListOrgPackagesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.ListOrgPackagesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListOrgPackages', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.ListOrgPackagesRequest, output=public_dot_packages__pb2.ListOrgPackagesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def install_org_package(self, request: public_dot_packages__pb2.InstallOrgPackageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.InstallOrgPackageResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='InstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.InstallOrgPackageRequest, output=public_dot_packages__pb2.InstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def remove_org_package(self, request: public_dot_packages__pb2.RemoveOrgPackageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.RemoveOrgPackageResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RemoveOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RemoveOrgPackageRequest, output=public_dot_packages__pb2.RemoveOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_org_package_status(self, request: public_dot_packages__pb2.GetOrgPackageStatusRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.GetOrgPackageStatusResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetOrgPackageStatus', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.GetOrgPackageStatusRequest, output=public_dot_packages__pb2.GetOrgPackageStatusResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def retry_install_org_package(self, request: public_dot_packages__pb2.RetryInstallOrgPackageRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.RetryInstallOrgPackageResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RetryInstallOrgPackage', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.RetryInstallOrgPackageRequest, output=public_dot_packages__pb2.RetryInstallOrgPackageResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_org_package_version(self, request: public_dot_packages__pb2.UpdateOrgPackageVersionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_packages__pb2.UpdateOrgPackageVersionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateOrgPackageVersion', service_name='textql.rpc.public.packages.OrgPackageService', input=public_dot_packages__pb2.UpdateOrgPackageVersionRequest, output=public_dot_packages__pb2.UpdateOrgPackageVersionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)