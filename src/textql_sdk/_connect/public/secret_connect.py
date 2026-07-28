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
from . import secret_pb2 as public_dot_secret__pb2

class SecretService(Protocol):

    async def list_secrets(self, request: public_dot_secret__pb2.ListSecretsRequest, ctx: RequestContext) -> public_dot_secret__pb2.ListSecretsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_members_with_secrets(self, request: public_dot_secret__pb2.GetMembersWithSecretsRequest, ctx: RequestContext) -> public_dot_secret__pb2.GetMembersWithSecretsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def put_secret(self, request: public_dot_secret__pb2.PutSecretRequest, ctx: RequestContext) -> public_dot_secret__pb2.PutSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_secret(self, request: public_dot_secret__pb2.UpdateSecretRequest, ctx: RequestContext) -> public_dot_secret__pb2.UpdateSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_secret(self, request: public_dot_secret__pb2.DeleteSecretRequest, ctx: RequestContext) -> public_dot_secret__pb2.DeleteSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_api_revision(self, request: public_dot_secret__pb2.CreateApiRevisionRequest, ctx: RequestContext) -> public_dot_secret__pb2.CreateApiRevisionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def upsert_api_access_key(self, request: public_dot_secret__pb2.UpsertApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.UpsertApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_api_revision(self, request: public_dot_secret__pb2.DeleteApiRevisionRequest, ctx: RequestContext) -> public_dot_secret__pb2.DeleteApiRevisionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_api_access_keys(self, request: public_dot_secret__pb2.ListApiAccessKeysRequest, ctx: RequestContext) -> public_dot_secret__pb2.ListApiAccessKeysResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_api_access_key(self, request: public_dot_secret__pb2.GetApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.GetApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_api_access_key(self, request: public_dot_secret__pb2.DeleteApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.DeleteApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_api_providers(self, request: public_dot_secret__pb2.ListApiProvidersRequest, ctx: RequestContext) -> public_dot_secret__pb2.ListApiProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def test_api_access_key(self, request: public_dot_secret__pb2.TestApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.TestApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def migrate_secret_to_api_connector(self, request: public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, ctx: RequestContext) -> public_dot_secret__pb2.MigrateSecretToApiConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SecretServiceASGIApplication(ConnectASGIApplication[SecretService]):

    def __init__(self, service: SecretService | AsyncGenerator[SecretService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.secret.SecretService/ListSecrets': Endpoint.unary(method=MethodInfo(name='ListSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListSecretsRequest, output=public_dot_secret__pb2.ListSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_secrets), '/textql.rpc.public.secret.SecretService/GetMembersWithSecrets': Endpoint.unary(method=MethodInfo(name='GetMembersWithSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetMembersWithSecretsRequest, output=public_dot_secret__pb2.GetMembersWithSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_members_with_secrets), '/textql.rpc.public.secret.SecretService/PutSecret': Endpoint.unary(method=MethodInfo(name='PutSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.PutSecretRequest, output=public_dot_secret__pb2.PutSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.put_secret), '/textql.rpc.public.secret.SecretService/UpdateSecret': Endpoint.unary(method=MethodInfo(name='UpdateSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpdateSecretRequest, output=public_dot_secret__pb2.UpdateSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_secret), '/textql.rpc.public.secret.SecretService/DeleteSecret': Endpoint.unary(method=MethodInfo(name='DeleteSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteSecretRequest, output=public_dot_secret__pb2.DeleteSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_secret), '/textql.rpc.public.secret.SecretService/CreateApiRevision': Endpoint.unary(method=MethodInfo(name='CreateApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.CreateApiRevisionRequest, output=public_dot_secret__pb2.CreateApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_api_revision), '/textql.rpc.public.secret.SecretService/UpsertApiAccessKey': Endpoint.unary(method=MethodInfo(name='UpsertApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpsertApiAccessKeyRequest, output=public_dot_secret__pb2.UpsertApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.upsert_api_access_key), '/textql.rpc.public.secret.SecretService/DeleteApiRevision': Endpoint.unary(method=MethodInfo(name='DeleteApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiRevisionRequest, output=public_dot_secret__pb2.DeleteApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_api_revision), '/textql.rpc.public.secret.SecretService/ListApiAccessKeys': Endpoint.unary(method=MethodInfo(name='ListApiAccessKeys', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiAccessKeysRequest, output=public_dot_secret__pb2.ListApiAccessKeysResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_api_access_keys), '/textql.rpc.public.secret.SecretService/GetApiAccessKey': Endpoint.unary(method=MethodInfo(name='GetApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetApiAccessKeyRequest, output=public_dot_secret__pb2.GetApiAccessKeyResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.get_api_access_key), '/textql.rpc.public.secret.SecretService/DeleteApiAccessKey': Endpoint.unary(method=MethodInfo(name='DeleteApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiAccessKeyRequest, output=public_dot_secret__pb2.DeleteApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_api_access_key), '/textql.rpc.public.secret.SecretService/ListApiProviders': Endpoint.unary(method=MethodInfo(name='ListApiProviders', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiProvidersRequest, output=public_dot_secret__pb2.ListApiProvidersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=svc.list_api_providers), '/textql.rpc.public.secret.SecretService/TestApiAccessKey': Endpoint.unary(method=MethodInfo(name='TestApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.TestApiAccessKeyRequest, output=public_dot_secret__pb2.TestApiAccessKeyResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), function=svc.test_api_access_key), '/textql.rpc.public.secret.SecretService/MigrateSecretToApiConnector': Endpoint.unary(method=MethodInfo(name='MigrateSecretToApiConnector', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, output=public_dot_secret__pb2.MigrateSecretToApiConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.migrate_secret_to_api_connector)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.secret.SecretService'

class SecretServiceClient(ConnectClient):

    async def list_secrets(self, request: public_dot_secret__pb2.ListSecretsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.ListSecretsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListSecretsRequest, output=public_dot_secret__pb2.ListSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_members_with_secrets(self, request: public_dot_secret__pb2.GetMembersWithSecretsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.GetMembersWithSecretsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetMembersWithSecretsRequest, output=public_dot_secret__pb2.GetMembersWithSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def put_secret(self, request: public_dot_secret__pb2.PutSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.PutSecretResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='PutSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.PutSecretRequest, output=public_dot_secret__pb2.PutSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_secret(self, request: public_dot_secret__pb2.UpdateSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.UpdateSecretResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpdateSecretRequest, output=public_dot_secret__pb2.UpdateSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_secret(self, request: public_dot_secret__pb2.DeleteSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.DeleteSecretResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteSecretRequest, output=public_dot_secret__pb2.DeleteSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_api_revision(self, request: public_dot_secret__pb2.CreateApiRevisionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.CreateApiRevisionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.CreateApiRevisionRequest, output=public_dot_secret__pb2.CreateApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def upsert_api_access_key(self, request: public_dot_secret__pb2.UpsertApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.UpsertApiAccessKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpsertApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpsertApiAccessKeyRequest, output=public_dot_secret__pb2.UpsertApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_api_revision(self, request: public_dot_secret__pb2.DeleteApiRevisionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.DeleteApiRevisionResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiRevisionRequest, output=public_dot_secret__pb2.DeleteApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_api_access_keys(self, request: public_dot_secret__pb2.ListApiAccessKeysRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.ListApiAccessKeysResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListApiAccessKeys', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiAccessKeysRequest, output=public_dot_secret__pb2.ListApiAccessKeysResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def get_api_access_key(self, request: public_dot_secret__pb2.GetApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.GetApiAccessKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetApiAccessKeyRequest, output=public_dot_secret__pb2.GetApiAccessKeyResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def delete_api_access_key(self, request: public_dot_secret__pb2.DeleteApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.DeleteApiAccessKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiAccessKeyRequest, output=public_dot_secret__pb2.DeleteApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_api_providers(self, request: public_dot_secret__pb2.ListApiProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.ListApiProvidersResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListApiProviders', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiProvidersRequest, output=public_dot_secret__pb2.ListApiProvidersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    async def test_api_access_key(self, request: public_dot_secret__pb2.TestApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.TestApiAccessKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='TestApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.TestApiAccessKeyRequest, output=public_dot_secret__pb2.TestApiAccessKeyResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), headers=headers, timeout_ms=timeout_ms)

    async def migrate_secret_to_api_connector(self, request: public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.MigrateSecretToApiConnectorResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='MigrateSecretToApiConnector', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, output=public_dot_secret__pb2.MigrateSecretToApiConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class SecretServiceSync(Protocol):

    def list_secrets(self, request: public_dot_secret__pb2.ListSecretsRequest, ctx: RequestContext) -> public_dot_secret__pb2.ListSecretsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_members_with_secrets(self, request: public_dot_secret__pb2.GetMembersWithSecretsRequest, ctx: RequestContext) -> public_dot_secret__pb2.GetMembersWithSecretsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def put_secret(self, request: public_dot_secret__pb2.PutSecretRequest, ctx: RequestContext) -> public_dot_secret__pb2.PutSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_secret(self, request: public_dot_secret__pb2.UpdateSecretRequest, ctx: RequestContext) -> public_dot_secret__pb2.UpdateSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_secret(self, request: public_dot_secret__pb2.DeleteSecretRequest, ctx: RequestContext) -> public_dot_secret__pb2.DeleteSecretResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_api_revision(self, request: public_dot_secret__pb2.CreateApiRevisionRequest, ctx: RequestContext) -> public_dot_secret__pb2.CreateApiRevisionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def upsert_api_access_key(self, request: public_dot_secret__pb2.UpsertApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.UpsertApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_api_revision(self, request: public_dot_secret__pb2.DeleteApiRevisionRequest, ctx: RequestContext) -> public_dot_secret__pb2.DeleteApiRevisionResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_api_access_keys(self, request: public_dot_secret__pb2.ListApiAccessKeysRequest, ctx: RequestContext) -> public_dot_secret__pb2.ListApiAccessKeysResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_api_access_key(self, request: public_dot_secret__pb2.GetApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.GetApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_api_access_key(self, request: public_dot_secret__pb2.DeleteApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.DeleteApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_api_providers(self, request: public_dot_secret__pb2.ListApiProvidersRequest, ctx: RequestContext) -> public_dot_secret__pb2.ListApiProvidersResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def test_api_access_key(self, request: public_dot_secret__pb2.TestApiAccessKeyRequest, ctx: RequestContext) -> public_dot_secret__pb2.TestApiAccessKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def migrate_secret_to_api_connector(self, request: public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, ctx: RequestContext) -> public_dot_secret__pb2.MigrateSecretToApiConnectorResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class SecretServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: SecretServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.secret.SecretService/ListSecrets': EndpointSync.unary(method=MethodInfo(name='ListSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListSecretsRequest, output=public_dot_secret__pb2.ListSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_secrets), '/textql.rpc.public.secret.SecretService/GetMembersWithSecrets': EndpointSync.unary(method=MethodInfo(name='GetMembersWithSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetMembersWithSecretsRequest, output=public_dot_secret__pb2.GetMembersWithSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_members_with_secrets), '/textql.rpc.public.secret.SecretService/PutSecret': EndpointSync.unary(method=MethodInfo(name='PutSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.PutSecretRequest, output=public_dot_secret__pb2.PutSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.put_secret), '/textql.rpc.public.secret.SecretService/UpdateSecret': EndpointSync.unary(method=MethodInfo(name='UpdateSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpdateSecretRequest, output=public_dot_secret__pb2.UpdateSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_secret), '/textql.rpc.public.secret.SecretService/DeleteSecret': EndpointSync.unary(method=MethodInfo(name='DeleteSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteSecretRequest, output=public_dot_secret__pb2.DeleteSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_secret), '/textql.rpc.public.secret.SecretService/CreateApiRevision': EndpointSync.unary(method=MethodInfo(name='CreateApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.CreateApiRevisionRequest, output=public_dot_secret__pb2.CreateApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_api_revision), '/textql.rpc.public.secret.SecretService/UpsertApiAccessKey': EndpointSync.unary(method=MethodInfo(name='UpsertApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpsertApiAccessKeyRequest, output=public_dot_secret__pb2.UpsertApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.upsert_api_access_key), '/textql.rpc.public.secret.SecretService/DeleteApiRevision': EndpointSync.unary(method=MethodInfo(name='DeleteApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiRevisionRequest, output=public_dot_secret__pb2.DeleteApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_api_revision), '/textql.rpc.public.secret.SecretService/ListApiAccessKeys': EndpointSync.unary(method=MethodInfo(name='ListApiAccessKeys', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiAccessKeysRequest, output=public_dot_secret__pb2.ListApiAccessKeysResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_api_access_keys), '/textql.rpc.public.secret.SecretService/GetApiAccessKey': EndpointSync.unary(method=MethodInfo(name='GetApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetApiAccessKeyRequest, output=public_dot_secret__pb2.GetApiAccessKeyResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.get_api_access_key), '/textql.rpc.public.secret.SecretService/DeleteApiAccessKey': EndpointSync.unary(method=MethodInfo(name='DeleteApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiAccessKeyRequest, output=public_dot_secret__pb2.DeleteApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_api_access_key), '/textql.rpc.public.secret.SecretService/ListApiProviders': EndpointSync.unary(method=MethodInfo(name='ListApiProviders', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiProvidersRequest, output=public_dot_secret__pb2.ListApiProvidersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), function=service.list_api_providers), '/textql.rpc.public.secret.SecretService/TestApiAccessKey': EndpointSync.unary(method=MethodInfo(name='TestApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.TestApiAccessKeyRequest, output=public_dot_secret__pb2.TestApiAccessKeyResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), function=service.test_api_access_key), '/textql.rpc.public.secret.SecretService/MigrateSecretToApiConnector': EndpointSync.unary(method=MethodInfo(name='MigrateSecretToApiConnector', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, output=public_dot_secret__pb2.MigrateSecretToApiConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.migrate_secret_to_api_connector)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.secret.SecretService'

class SecretServiceClientSync(ConnectClientSync):

    def list_secrets(self, request: public_dot_secret__pb2.ListSecretsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.ListSecretsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListSecretsRequest, output=public_dot_secret__pb2.ListSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_members_with_secrets(self, request: public_dot_secret__pb2.GetMembersWithSecretsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.GetMembersWithSecretsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMembersWithSecrets', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetMembersWithSecretsRequest, output=public_dot_secret__pb2.GetMembersWithSecretsResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def put_secret(self, request: public_dot_secret__pb2.PutSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.PutSecretResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='PutSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.PutSecretRequest, output=public_dot_secret__pb2.PutSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_secret(self, request: public_dot_secret__pb2.UpdateSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.UpdateSecretResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpdateSecretRequest, output=public_dot_secret__pb2.UpdateSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_secret(self, request: public_dot_secret__pb2.DeleteSecretRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.DeleteSecretResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteSecret', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteSecretRequest, output=public_dot_secret__pb2.DeleteSecretResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_api_revision(self, request: public_dot_secret__pb2.CreateApiRevisionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.CreateApiRevisionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.CreateApiRevisionRequest, output=public_dot_secret__pb2.CreateApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def upsert_api_access_key(self, request: public_dot_secret__pb2.UpsertApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.UpsertApiAccessKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpsertApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.UpsertApiAccessKeyRequest, output=public_dot_secret__pb2.UpsertApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_api_revision(self, request: public_dot_secret__pb2.DeleteApiRevisionRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.DeleteApiRevisionResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteApiRevision', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiRevisionRequest, output=public_dot_secret__pb2.DeleteApiRevisionResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_api_access_keys(self, request: public_dot_secret__pb2.ListApiAccessKeysRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.ListApiAccessKeysResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListApiAccessKeys', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiAccessKeysRequest, output=public_dot_secret__pb2.ListApiAccessKeysResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def get_api_access_key(self, request: public_dot_secret__pb2.GetApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.GetApiAccessKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.GetApiAccessKeyRequest, output=public_dot_secret__pb2.GetApiAccessKeyResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def delete_api_access_key(self, request: public_dot_secret__pb2.DeleteApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.DeleteApiAccessKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.DeleteApiAccessKeyRequest, output=public_dot_secret__pb2.DeleteApiAccessKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_api_providers(self, request: public_dot_secret__pb2.ListApiProvidersRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None, use_get: bool=False) -> public_dot_secret__pb2.ListApiProvidersResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListApiProviders', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.ListApiProvidersRequest, output=public_dot_secret__pb2.ListApiProvidersResponse, idempotency_level=IdempotencyLevel.NO_SIDE_EFFECTS), headers=headers, timeout_ms=timeout_ms, use_get=use_get)

    def test_api_access_key(self, request: public_dot_secret__pb2.TestApiAccessKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.TestApiAccessKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='TestApiAccessKey', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.TestApiAccessKeyRequest, output=public_dot_secret__pb2.TestApiAccessKeyResponse, idempotency_level=IdempotencyLevel.IDEMPOTENT), headers=headers, timeout_ms=timeout_ms)

    def migrate_secret_to_api_connector(self, request: public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_secret__pb2.MigrateSecretToApiConnectorResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='MigrateSecretToApiConnector', service_name='textql.rpc.public.secret.SecretService', input=public_dot_secret__pb2.MigrateSecretToApiConnectorRequest, output=public_dot_secret__pb2.MigrateSecretToApiConnectorResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)