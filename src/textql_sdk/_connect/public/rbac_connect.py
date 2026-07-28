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
from . import rbac_pb2 as public_dot_rbac__pb2

class RBACService(Protocol):

    async def create_role(self, request: public_dot_rbac__pb2.CreateRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_role(self, request: public_dot_rbac__pb2.GetRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_roles(self, request: public_dot_rbac__pb2.ListRolesRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListRolesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_role(self, request: public_dot_rbac__pb2.UpdateRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_role(self, request: public_dot_rbac__pb2.DeleteRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.DeleteRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_permissions(self, request: public_dot_rbac__pb2.ListPermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListPermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_role_permissions(self, request: public_dot_rbac__pb2.GetRolePermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetRolePermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def assign_permission_to_role(self, request: public_dot_rbac__pb2.AssignPermissionToRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.AssignPermissionToRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def remove_permission_from_role(self, request: public_dot_rbac__pb2.RemovePermissionFromRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RemovePermissionFromRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def set_role_permissions(self, request: public_dot_rbac__pb2.SetRolePermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.SetRolePermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def assign_role_to_member(self, request: public_dot_rbac__pb2.AssignRoleToMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.AssignRoleToMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def remove_role_from_member(self, request: public_dot_rbac__pb2.RemoveRoleFromMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RemoveRoleFromMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_member_roles(self, request: public_dot_rbac__pb2.GetMemberRolesRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetMemberRolesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_current_member_roles_and_permissions(self, request: public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_group(self, request: public_dot_rbac__pb2.CreateGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_group(self, request: public_dot_rbac__pb2.GetGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_groups(self, request: public_dot_rbac__pb2.ListGroupsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListGroupsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_group(self, request: public_dot_rbac__pb2.UpdateGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_group(self, request: public_dot_rbac__pb2.DeleteGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.DeleteGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def add_group_member(self, request: public_dot_rbac__pb2.AddGroupMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.AddGroupMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def remove_group_member(self, request: public_dot_rbac__pb2.RemoveGroupMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RemoveGroupMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_member_groups(self, request: public_dot_rbac__pb2.GetMemberGroupsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetMemberGroupsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def share_object_with_group(self, request: public_dot_rbac__pb2.ShareObjectWithGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ShareObjectWithGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_group_connectors(self, request: public_dot_rbac__pb2.ListGroupConnectorsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListGroupConnectorsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def migrate_scim_group_mapping_to_group(self, request: public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def migrate_all_scim_group_mappings(self, request: public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revert_scim_group_mapping_to_role(self, request: public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def convert_role_to_group(self, request: public_dot_rbac__pb2.ConvertRoleToGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ConvertRoleToGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_scim_group_mappings(self, request: public_dot_rbac__pb2.ListScimGroupMappingsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListScimGroupMappingsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def share_object(self, request: public_dot_rbac__pb2.ShareObjectRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ShareObjectResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def share_object_with_role(self, request: public_dot_rbac__pb2.ShareObjectWithRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ShareObjectWithRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revoke_object_access(self, request: public_dot_rbac__pb2.RevokeObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RevokeObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_object_access(self, request: public_dot_rbac__pb2.GetObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def has_object_access(self, request: public_dot_rbac__pb2.HasObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.HasObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_object_visibility(self, request: public_dot_rbac__pb2.UpdateObjectVisibilityRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateObjectVisibilityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def update_object_access(self, request: public_dot_rbac__pb2.UpdateObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def generate_share_link(self, request: public_dot_rbac__pb2.GenerateShareLinkRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GenerateShareLinkResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def request_access(self, request: public_dot_rbac__pb2.RequestAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RequestAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_access_requests(self, request: public_dot_rbac__pb2.ListAccessRequestsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListAccessRequestsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def approve_access_request(self, request: public_dot_rbac__pb2.ApproveAccessRequestRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ApproveAccessRequestResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def reject_access_request(self, request: public_dot_rbac__pb2.RejectAccessRequestRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RejectAccessRequestResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_api_key(self, request: public_dot_rbac__pb2.CreateApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_api_keys(self, request: public_dot_rbac__pb2.ListApiKeysRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListApiKeysResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def revoke_api_key(self, request: public_dot_rbac__pb2.RevokeApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RevokeApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def rotate_api_key(self, request: public_dot_rbac__pb2.RotateApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RotateApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def get_embed_user_api_key(self, request: public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetEmbedUserApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def create_service_account(self, request: public_dot_rbac__pb2.CreateServiceAccountRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateServiceAccountResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def list_service_accounts(self, request: public_dot_rbac__pb2.ListServiceAccountsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListServiceAccountsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    async def delete_service_account(self, request: public_dot_rbac__pb2.DeleteServiceAccountRequest, ctx: RequestContext) -> public_dot_rbac__pb2.DeleteServiceAccountResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class RBACServiceASGIApplication(ConnectASGIApplication[RBACService]):

    def __init__(self, service: RBACService | AsyncGenerator[RBACService], *, interceptors: Iterable[Interceptor]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(service=service, endpoints=lambda svc: {'/textql.rpc.public.rbac.RBACService/CreateRole': Endpoint.unary(method=MethodInfo(name='CreateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateRoleRequest, output=public_dot_rbac__pb2.CreateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_role), '/textql.rpc.public.rbac.RBACService/GetRole': Endpoint.unary(method=MethodInfo(name='GetRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRoleRequest, output=public_dot_rbac__pb2.GetRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_role), '/textql.rpc.public.rbac.RBACService/ListRoles': Endpoint.unary(method=MethodInfo(name='ListRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListRolesRequest, output=public_dot_rbac__pb2.ListRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_roles), '/textql.rpc.public.rbac.RBACService/UpdateRole': Endpoint.unary(method=MethodInfo(name='UpdateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateRoleRequest, output=public_dot_rbac__pb2.UpdateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_role), '/textql.rpc.public.rbac.RBACService/DeleteRole': Endpoint.unary(method=MethodInfo(name='DeleteRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteRoleRequest, output=public_dot_rbac__pb2.DeleteRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_role), '/textql.rpc.public.rbac.RBACService/ListPermissions': Endpoint.unary(method=MethodInfo(name='ListPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListPermissionsRequest, output=public_dot_rbac__pb2.ListPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_permissions), '/textql.rpc.public.rbac.RBACService/GetRolePermissions': Endpoint.unary(method=MethodInfo(name='GetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRolePermissionsRequest, output=public_dot_rbac__pb2.GetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_role_permissions), '/textql.rpc.public.rbac.RBACService/AssignPermissionToRole': Endpoint.unary(method=MethodInfo(name='AssignPermissionToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignPermissionToRoleRequest, output=public_dot_rbac__pb2.AssignPermissionToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.assign_permission_to_role), '/textql.rpc.public.rbac.RBACService/RemovePermissionFromRole': Endpoint.unary(method=MethodInfo(name='RemovePermissionFromRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemovePermissionFromRoleRequest, output=public_dot_rbac__pb2.RemovePermissionFromRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.remove_permission_from_role), '/textql.rpc.public.rbac.RBACService/SetRolePermissions': Endpoint.unary(method=MethodInfo(name='SetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.SetRolePermissionsRequest, output=public_dot_rbac__pb2.SetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.set_role_permissions), '/textql.rpc.public.rbac.RBACService/AssignRoleToMember': Endpoint.unary(method=MethodInfo(name='AssignRoleToMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignRoleToMemberRequest, output=public_dot_rbac__pb2.AssignRoleToMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.assign_role_to_member), '/textql.rpc.public.rbac.RBACService/RemoveRoleFromMember': Endpoint.unary(method=MethodInfo(name='RemoveRoleFromMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveRoleFromMemberRequest, output=public_dot_rbac__pb2.RemoveRoleFromMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.remove_role_from_member), '/textql.rpc.public.rbac.RBACService/GetMemberRoles': Endpoint.unary(method=MethodInfo(name='GetMemberRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberRolesRequest, output=public_dot_rbac__pb2.GetMemberRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_member_roles), '/textql.rpc.public.rbac.RBACService/GetCurrentMemberRolesAndPermissions': Endpoint.unary(method=MethodInfo(name='GetCurrentMemberRolesAndPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, output=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_current_member_roles_and_permissions), '/textql.rpc.public.rbac.RBACService/CreateGroup': Endpoint.unary(method=MethodInfo(name='CreateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateGroupRequest, output=public_dot_rbac__pb2.CreateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_group), '/textql.rpc.public.rbac.RBACService/GetGroup': Endpoint.unary(method=MethodInfo(name='GetGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetGroupRequest, output=public_dot_rbac__pb2.GetGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_group), '/textql.rpc.public.rbac.RBACService/ListGroups': Endpoint.unary(method=MethodInfo(name='ListGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupsRequest, output=public_dot_rbac__pb2.ListGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_groups), '/textql.rpc.public.rbac.RBACService/UpdateGroup': Endpoint.unary(method=MethodInfo(name='UpdateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateGroupRequest, output=public_dot_rbac__pb2.UpdateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_group), '/textql.rpc.public.rbac.RBACService/DeleteGroup': Endpoint.unary(method=MethodInfo(name='DeleteGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteGroupRequest, output=public_dot_rbac__pb2.DeleteGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_group), '/textql.rpc.public.rbac.RBACService/AddGroupMember': Endpoint.unary(method=MethodInfo(name='AddGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AddGroupMemberRequest, output=public_dot_rbac__pb2.AddGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.add_group_member), '/textql.rpc.public.rbac.RBACService/RemoveGroupMember': Endpoint.unary(method=MethodInfo(name='RemoveGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveGroupMemberRequest, output=public_dot_rbac__pb2.RemoveGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.remove_group_member), '/textql.rpc.public.rbac.RBACService/GetMemberGroups': Endpoint.unary(method=MethodInfo(name='GetMemberGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberGroupsRequest, output=public_dot_rbac__pb2.GetMemberGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_member_groups), '/textql.rpc.public.rbac.RBACService/ShareObjectWithGroup': Endpoint.unary(method=MethodInfo(name='ShareObjectWithGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithGroupRequest, output=public_dot_rbac__pb2.ShareObjectWithGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.share_object_with_group), '/textql.rpc.public.rbac.RBACService/ListGroupConnectors': Endpoint.unary(method=MethodInfo(name='ListGroupConnectors', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupConnectorsRequest, output=public_dot_rbac__pb2.ListGroupConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_group_connectors), '/textql.rpc.public.rbac.RBACService/MigrateScimGroupMappingToGroup': Endpoint.unary(method=MethodInfo(name='MigrateScimGroupMappingToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, output=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.migrate_scim_group_mapping_to_group), '/textql.rpc.public.rbac.RBACService/MigrateAllScimGroupMappings': Endpoint.unary(method=MethodInfo(name='MigrateAllScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, output=public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.migrate_all_scim_group_mappings), '/textql.rpc.public.rbac.RBACService/RevertScimGroupMappingToRole': Endpoint.unary(method=MethodInfo(name='RevertScimGroupMappingToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, output=public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revert_scim_group_mapping_to_role), '/textql.rpc.public.rbac.RBACService/ConvertRoleToGroup': Endpoint.unary(method=MethodInfo(name='ConvertRoleToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ConvertRoleToGroupRequest, output=public_dot_rbac__pb2.ConvertRoleToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.convert_role_to_group), '/textql.rpc.public.rbac.RBACService/ListScimGroupMappings': Endpoint.unary(method=MethodInfo(name='ListScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListScimGroupMappingsRequest, output=public_dot_rbac__pb2.ListScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_scim_group_mappings), '/textql.rpc.public.rbac.RBACService/ShareObject': Endpoint.unary(method=MethodInfo(name='ShareObject', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectRequest, output=public_dot_rbac__pb2.ShareObjectResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.share_object), '/textql.rpc.public.rbac.RBACService/ShareObjectWithRole': Endpoint.unary(method=MethodInfo(name='ShareObjectWithRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithRoleRequest, output=public_dot_rbac__pb2.ShareObjectWithRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.share_object_with_role), '/textql.rpc.public.rbac.RBACService/RevokeObjectAccess': Endpoint.unary(method=MethodInfo(name='RevokeObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeObjectAccessRequest, output=public_dot_rbac__pb2.RevokeObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revoke_object_access), '/textql.rpc.public.rbac.RBACService/GetObjectAccess': Endpoint.unary(method=MethodInfo(name='GetObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetObjectAccessRequest, output=public_dot_rbac__pb2.GetObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_object_access), '/textql.rpc.public.rbac.RBACService/HasObjectAccess': Endpoint.unary(method=MethodInfo(name='HasObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.HasObjectAccessRequest, output=public_dot_rbac__pb2.HasObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.has_object_access), '/textql.rpc.public.rbac.RBACService/UpdateObjectVisibility': Endpoint.unary(method=MethodInfo(name='UpdateObjectVisibility', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectVisibilityRequest, output=public_dot_rbac__pb2.UpdateObjectVisibilityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_object_visibility), '/textql.rpc.public.rbac.RBACService/UpdateObjectAccess': Endpoint.unary(method=MethodInfo(name='UpdateObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectAccessRequest, output=public_dot_rbac__pb2.UpdateObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.update_object_access), '/textql.rpc.public.rbac.RBACService/GenerateShareLink': Endpoint.unary(method=MethodInfo(name='GenerateShareLink', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GenerateShareLinkRequest, output=public_dot_rbac__pb2.GenerateShareLinkResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.generate_share_link), '/textql.rpc.public.rbac.RBACService/RequestAccess': Endpoint.unary(method=MethodInfo(name='RequestAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RequestAccessRequest, output=public_dot_rbac__pb2.RequestAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.request_access), '/textql.rpc.public.rbac.RBACService/ListAccessRequests': Endpoint.unary(method=MethodInfo(name='ListAccessRequests', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListAccessRequestsRequest, output=public_dot_rbac__pb2.ListAccessRequestsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_access_requests), '/textql.rpc.public.rbac.RBACService/ApproveAccessRequest': Endpoint.unary(method=MethodInfo(name='ApproveAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ApproveAccessRequestRequest, output=public_dot_rbac__pb2.ApproveAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.approve_access_request), '/textql.rpc.public.rbac.RBACService/RejectAccessRequest': Endpoint.unary(method=MethodInfo(name='RejectAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RejectAccessRequestRequest, output=public_dot_rbac__pb2.RejectAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.reject_access_request), '/textql.rpc.public.rbac.RBACService/CreateApiKey': Endpoint.unary(method=MethodInfo(name='CreateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateApiKeyRequest, output=public_dot_rbac__pb2.CreateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_api_key), '/textql.rpc.public.rbac.RBACService/ListApiKeys': Endpoint.unary(method=MethodInfo(name='ListApiKeys', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListApiKeysRequest, output=public_dot_rbac__pb2.ListApiKeysResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_api_keys), '/textql.rpc.public.rbac.RBACService/RevokeApiKey': Endpoint.unary(method=MethodInfo(name='RevokeApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeApiKeyRequest, output=public_dot_rbac__pb2.RevokeApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.revoke_api_key), '/textql.rpc.public.rbac.RBACService/RotateApiKey': Endpoint.unary(method=MethodInfo(name='RotateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RotateApiKeyRequest, output=public_dot_rbac__pb2.RotateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.rotate_api_key), '/textql.rpc.public.rbac.RBACService/GetEmbedUserApiKey': Endpoint.unary(method=MethodInfo(name='GetEmbedUserApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, output=public_dot_rbac__pb2.GetEmbedUserApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.get_embed_user_api_key), '/textql.rpc.public.rbac.RBACService/CreateServiceAccount': Endpoint.unary(method=MethodInfo(name='CreateServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateServiceAccountRequest, output=public_dot_rbac__pb2.CreateServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.create_service_account), '/textql.rpc.public.rbac.RBACService/ListServiceAccounts': Endpoint.unary(method=MethodInfo(name='ListServiceAccounts', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListServiceAccountsRequest, output=public_dot_rbac__pb2.ListServiceAccountsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.list_service_accounts), '/textql.rpc.public.rbac.RBACService/DeleteServiceAccount': Endpoint.unary(method=MethodInfo(name='DeleteServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteServiceAccountRequest, output=public_dot_rbac__pb2.DeleteServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=svc.delete_service_account)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.rbac.RBACService'

class RBACServiceClient(ConnectClient):

    async def create_role(self, request: public_dot_rbac__pb2.CreateRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateRoleRequest, output=public_dot_rbac__pb2.CreateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_role(self, request: public_dot_rbac__pb2.GetRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRoleRequest, output=public_dot_rbac__pb2.GetRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_roles(self, request: public_dot_rbac__pb2.ListRolesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListRolesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListRolesRequest, output=public_dot_rbac__pb2.ListRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_role(self, request: public_dot_rbac__pb2.UpdateRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateRoleRequest, output=public_dot_rbac__pb2.UpdateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_role(self, request: public_dot_rbac__pb2.DeleteRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.DeleteRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteRoleRequest, output=public_dot_rbac__pb2.DeleteRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_permissions(self, request: public_dot_rbac__pb2.ListPermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListPermissionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListPermissionsRequest, output=public_dot_rbac__pb2.ListPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_role_permissions(self, request: public_dot_rbac__pb2.GetRolePermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetRolePermissionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRolePermissionsRequest, output=public_dot_rbac__pb2.GetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def assign_permission_to_role(self, request: public_dot_rbac__pb2.AssignPermissionToRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.AssignPermissionToRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AssignPermissionToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignPermissionToRoleRequest, output=public_dot_rbac__pb2.AssignPermissionToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def remove_permission_from_role(self, request: public_dot_rbac__pb2.RemovePermissionFromRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RemovePermissionFromRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RemovePermissionFromRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemovePermissionFromRoleRequest, output=public_dot_rbac__pb2.RemovePermissionFromRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def set_role_permissions(self, request: public_dot_rbac__pb2.SetRolePermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.SetRolePermissionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='SetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.SetRolePermissionsRequest, output=public_dot_rbac__pb2.SetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def assign_role_to_member(self, request: public_dot_rbac__pb2.AssignRoleToMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.AssignRoleToMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AssignRoleToMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignRoleToMemberRequest, output=public_dot_rbac__pb2.AssignRoleToMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def remove_role_from_member(self, request: public_dot_rbac__pb2.RemoveRoleFromMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RemoveRoleFromMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RemoveRoleFromMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveRoleFromMemberRequest, output=public_dot_rbac__pb2.RemoveRoleFromMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_member_roles(self, request: public_dot_rbac__pb2.GetMemberRolesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetMemberRolesResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMemberRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberRolesRequest, output=public_dot_rbac__pb2.GetMemberRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_current_member_roles_and_permissions(self, request: public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetCurrentMemberRolesAndPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, output=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_group(self, request: public_dot_rbac__pb2.CreateGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateGroupResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateGroupRequest, output=public_dot_rbac__pb2.CreateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_group(self, request: public_dot_rbac__pb2.GetGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetGroupResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetGroupRequest, output=public_dot_rbac__pb2.GetGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_groups(self, request: public_dot_rbac__pb2.ListGroupsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListGroupsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupsRequest, output=public_dot_rbac__pb2.ListGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_group(self, request: public_dot_rbac__pb2.UpdateGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateGroupResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateGroupRequest, output=public_dot_rbac__pb2.UpdateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_group(self, request: public_dot_rbac__pb2.DeleteGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.DeleteGroupResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteGroupRequest, output=public_dot_rbac__pb2.DeleteGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def add_group_member(self, request: public_dot_rbac__pb2.AddGroupMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.AddGroupMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='AddGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AddGroupMemberRequest, output=public_dot_rbac__pb2.AddGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def remove_group_member(self, request: public_dot_rbac__pb2.RemoveGroupMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RemoveGroupMemberResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RemoveGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveGroupMemberRequest, output=public_dot_rbac__pb2.RemoveGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_member_groups(self, request: public_dot_rbac__pb2.GetMemberGroupsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetMemberGroupsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetMemberGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberGroupsRequest, output=public_dot_rbac__pb2.GetMemberGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def share_object_with_group(self, request: public_dot_rbac__pb2.ShareObjectWithGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ShareObjectWithGroupResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ShareObjectWithGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithGroupRequest, output=public_dot_rbac__pb2.ShareObjectWithGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_group_connectors(self, request: public_dot_rbac__pb2.ListGroupConnectorsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListGroupConnectorsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListGroupConnectors', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupConnectorsRequest, output=public_dot_rbac__pb2.ListGroupConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def migrate_scim_group_mapping_to_group(self, request: public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='MigrateScimGroupMappingToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, output=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def migrate_all_scim_group_mappings(self, request: public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='MigrateAllScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, output=public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def revert_scim_group_mapping_to_role(self, request: public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevertScimGroupMappingToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, output=public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def convert_role_to_group(self, request: public_dot_rbac__pb2.ConvertRoleToGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ConvertRoleToGroupResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ConvertRoleToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ConvertRoleToGroupRequest, output=public_dot_rbac__pb2.ConvertRoleToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_scim_group_mappings(self, request: public_dot_rbac__pb2.ListScimGroupMappingsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListScimGroupMappingsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListScimGroupMappingsRequest, output=public_dot_rbac__pb2.ListScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def share_object(self, request: public_dot_rbac__pb2.ShareObjectRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ShareObjectResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ShareObject', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectRequest, output=public_dot_rbac__pb2.ShareObjectResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def share_object_with_role(self, request: public_dot_rbac__pb2.ShareObjectWithRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ShareObjectWithRoleResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ShareObjectWithRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithRoleRequest, output=public_dot_rbac__pb2.ShareObjectWithRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def revoke_object_access(self, request: public_dot_rbac__pb2.RevokeObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RevokeObjectAccessResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevokeObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeObjectAccessRequest, output=public_dot_rbac__pb2.RevokeObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_object_access(self, request: public_dot_rbac__pb2.GetObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetObjectAccessResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetObjectAccessRequest, output=public_dot_rbac__pb2.GetObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def has_object_access(self, request: public_dot_rbac__pb2.HasObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.HasObjectAccessResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='HasObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.HasObjectAccessRequest, output=public_dot_rbac__pb2.HasObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_object_visibility(self, request: public_dot_rbac__pb2.UpdateObjectVisibilityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateObjectVisibilityResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateObjectVisibility', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectVisibilityRequest, output=public_dot_rbac__pb2.UpdateObjectVisibilityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def update_object_access(self, request: public_dot_rbac__pb2.UpdateObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateObjectAccessResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='UpdateObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectAccessRequest, output=public_dot_rbac__pb2.UpdateObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def generate_share_link(self, request: public_dot_rbac__pb2.GenerateShareLinkRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GenerateShareLinkResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GenerateShareLink', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GenerateShareLinkRequest, output=public_dot_rbac__pb2.GenerateShareLinkResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def request_access(self, request: public_dot_rbac__pb2.RequestAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RequestAccessResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RequestAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RequestAccessRequest, output=public_dot_rbac__pb2.RequestAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_access_requests(self, request: public_dot_rbac__pb2.ListAccessRequestsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListAccessRequestsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListAccessRequests', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListAccessRequestsRequest, output=public_dot_rbac__pb2.ListAccessRequestsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def approve_access_request(self, request: public_dot_rbac__pb2.ApproveAccessRequestRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ApproveAccessRequestResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ApproveAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ApproveAccessRequestRequest, output=public_dot_rbac__pb2.ApproveAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def reject_access_request(self, request: public_dot_rbac__pb2.RejectAccessRequestRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RejectAccessRequestResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RejectAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RejectAccessRequestRequest, output=public_dot_rbac__pb2.RejectAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_api_key(self, request: public_dot_rbac__pb2.CreateApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateApiKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateApiKeyRequest, output=public_dot_rbac__pb2.CreateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_api_keys(self, request: public_dot_rbac__pb2.ListApiKeysRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListApiKeysResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListApiKeys', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListApiKeysRequest, output=public_dot_rbac__pb2.ListApiKeysResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def revoke_api_key(self, request: public_dot_rbac__pb2.RevokeApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RevokeApiKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RevokeApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeApiKeyRequest, output=public_dot_rbac__pb2.RevokeApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def rotate_api_key(self, request: public_dot_rbac__pb2.RotateApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RotateApiKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='RotateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RotateApiKeyRequest, output=public_dot_rbac__pb2.RotateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def get_embed_user_api_key(self, request: public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetEmbedUserApiKeyResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='GetEmbedUserApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, output=public_dot_rbac__pb2.GetEmbedUserApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def create_service_account(self, request: public_dot_rbac__pb2.CreateServiceAccountRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateServiceAccountResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='CreateServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateServiceAccountRequest, output=public_dot_rbac__pb2.CreateServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def list_service_accounts(self, request: public_dot_rbac__pb2.ListServiceAccountsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListServiceAccountsResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='ListServiceAccounts', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListServiceAccountsRequest, output=public_dot_rbac__pb2.ListServiceAccountsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    async def delete_service_account(self, request: public_dot_rbac__pb2.DeleteServiceAccountRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.DeleteServiceAccountResponse:
        return await self.execute_unary(request=request, method=MethodInfo(name='DeleteServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteServiceAccountRequest, output=public_dot_rbac__pb2.DeleteServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

class RBACServiceSync(Protocol):

    def create_role(self, request: public_dot_rbac__pb2.CreateRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_role(self, request: public_dot_rbac__pb2.GetRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_roles(self, request: public_dot_rbac__pb2.ListRolesRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListRolesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_role(self, request: public_dot_rbac__pb2.UpdateRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_role(self, request: public_dot_rbac__pb2.DeleteRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.DeleteRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_permissions(self, request: public_dot_rbac__pb2.ListPermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListPermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_role_permissions(self, request: public_dot_rbac__pb2.GetRolePermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetRolePermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def assign_permission_to_role(self, request: public_dot_rbac__pb2.AssignPermissionToRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.AssignPermissionToRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def remove_permission_from_role(self, request: public_dot_rbac__pb2.RemovePermissionFromRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RemovePermissionFromRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def set_role_permissions(self, request: public_dot_rbac__pb2.SetRolePermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.SetRolePermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def assign_role_to_member(self, request: public_dot_rbac__pb2.AssignRoleToMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.AssignRoleToMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def remove_role_from_member(self, request: public_dot_rbac__pb2.RemoveRoleFromMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RemoveRoleFromMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_member_roles(self, request: public_dot_rbac__pb2.GetMemberRolesRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetMemberRolesResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_current_member_roles_and_permissions(self, request: public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_group(self, request: public_dot_rbac__pb2.CreateGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_group(self, request: public_dot_rbac__pb2.GetGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_groups(self, request: public_dot_rbac__pb2.ListGroupsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListGroupsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_group(self, request: public_dot_rbac__pb2.UpdateGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_group(self, request: public_dot_rbac__pb2.DeleteGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.DeleteGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def add_group_member(self, request: public_dot_rbac__pb2.AddGroupMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.AddGroupMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def remove_group_member(self, request: public_dot_rbac__pb2.RemoveGroupMemberRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RemoveGroupMemberResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_member_groups(self, request: public_dot_rbac__pb2.GetMemberGroupsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetMemberGroupsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def share_object_with_group(self, request: public_dot_rbac__pb2.ShareObjectWithGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ShareObjectWithGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_group_connectors(self, request: public_dot_rbac__pb2.ListGroupConnectorsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListGroupConnectorsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def migrate_scim_group_mapping_to_group(self, request: public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def migrate_all_scim_group_mappings(self, request: public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revert_scim_group_mapping_to_role(self, request: public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def convert_role_to_group(self, request: public_dot_rbac__pb2.ConvertRoleToGroupRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ConvertRoleToGroupResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_scim_group_mappings(self, request: public_dot_rbac__pb2.ListScimGroupMappingsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListScimGroupMappingsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def share_object(self, request: public_dot_rbac__pb2.ShareObjectRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ShareObjectResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def share_object_with_role(self, request: public_dot_rbac__pb2.ShareObjectWithRoleRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ShareObjectWithRoleResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revoke_object_access(self, request: public_dot_rbac__pb2.RevokeObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RevokeObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_object_access(self, request: public_dot_rbac__pb2.GetObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def has_object_access(self, request: public_dot_rbac__pb2.HasObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.HasObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_object_visibility(self, request: public_dot_rbac__pb2.UpdateObjectVisibilityRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateObjectVisibilityResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def update_object_access(self, request: public_dot_rbac__pb2.UpdateObjectAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.UpdateObjectAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def generate_share_link(self, request: public_dot_rbac__pb2.GenerateShareLinkRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GenerateShareLinkResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def request_access(self, request: public_dot_rbac__pb2.RequestAccessRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RequestAccessResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_access_requests(self, request: public_dot_rbac__pb2.ListAccessRequestsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListAccessRequestsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def approve_access_request(self, request: public_dot_rbac__pb2.ApproveAccessRequestRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ApproveAccessRequestResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def reject_access_request(self, request: public_dot_rbac__pb2.RejectAccessRequestRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RejectAccessRequestResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_api_key(self, request: public_dot_rbac__pb2.CreateApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_api_keys(self, request: public_dot_rbac__pb2.ListApiKeysRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListApiKeysResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def revoke_api_key(self, request: public_dot_rbac__pb2.RevokeApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RevokeApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def rotate_api_key(self, request: public_dot_rbac__pb2.RotateApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.RotateApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def get_embed_user_api_key(self, request: public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, ctx: RequestContext) -> public_dot_rbac__pb2.GetEmbedUserApiKeyResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def create_service_account(self, request: public_dot_rbac__pb2.CreateServiceAccountRequest, ctx: RequestContext) -> public_dot_rbac__pb2.CreateServiceAccountResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def list_service_accounts(self, request: public_dot_rbac__pb2.ListServiceAccountsRequest, ctx: RequestContext) -> public_dot_rbac__pb2.ListServiceAccountsResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

    def delete_service_account(self, request: public_dot_rbac__pb2.DeleteServiceAccountRequest, ctx: RequestContext) -> public_dot_rbac__pb2.DeleteServiceAccountResponse:
        raise ConnectError(Code.UNIMPLEMENTED, 'Not implemented')

class RBACServiceWSGIApplication(ConnectWSGIApplication):

    def __init__(self, service: RBACServiceSync, interceptors: Iterable[InterceptorSync]=(), read_max_bytes: int | None=None, compressions: Iterable[Compression] | None=None) -> None:
        super().__init__(endpoints={'/textql.rpc.public.rbac.RBACService/CreateRole': EndpointSync.unary(method=MethodInfo(name='CreateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateRoleRequest, output=public_dot_rbac__pb2.CreateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_role), '/textql.rpc.public.rbac.RBACService/GetRole': EndpointSync.unary(method=MethodInfo(name='GetRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRoleRequest, output=public_dot_rbac__pb2.GetRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_role), '/textql.rpc.public.rbac.RBACService/ListRoles': EndpointSync.unary(method=MethodInfo(name='ListRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListRolesRequest, output=public_dot_rbac__pb2.ListRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_roles), '/textql.rpc.public.rbac.RBACService/UpdateRole': EndpointSync.unary(method=MethodInfo(name='UpdateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateRoleRequest, output=public_dot_rbac__pb2.UpdateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_role), '/textql.rpc.public.rbac.RBACService/DeleteRole': EndpointSync.unary(method=MethodInfo(name='DeleteRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteRoleRequest, output=public_dot_rbac__pb2.DeleteRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_role), '/textql.rpc.public.rbac.RBACService/ListPermissions': EndpointSync.unary(method=MethodInfo(name='ListPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListPermissionsRequest, output=public_dot_rbac__pb2.ListPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_permissions), '/textql.rpc.public.rbac.RBACService/GetRolePermissions': EndpointSync.unary(method=MethodInfo(name='GetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRolePermissionsRequest, output=public_dot_rbac__pb2.GetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_role_permissions), '/textql.rpc.public.rbac.RBACService/AssignPermissionToRole': EndpointSync.unary(method=MethodInfo(name='AssignPermissionToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignPermissionToRoleRequest, output=public_dot_rbac__pb2.AssignPermissionToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.assign_permission_to_role), '/textql.rpc.public.rbac.RBACService/RemovePermissionFromRole': EndpointSync.unary(method=MethodInfo(name='RemovePermissionFromRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemovePermissionFromRoleRequest, output=public_dot_rbac__pb2.RemovePermissionFromRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.remove_permission_from_role), '/textql.rpc.public.rbac.RBACService/SetRolePermissions': EndpointSync.unary(method=MethodInfo(name='SetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.SetRolePermissionsRequest, output=public_dot_rbac__pb2.SetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.set_role_permissions), '/textql.rpc.public.rbac.RBACService/AssignRoleToMember': EndpointSync.unary(method=MethodInfo(name='AssignRoleToMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignRoleToMemberRequest, output=public_dot_rbac__pb2.AssignRoleToMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.assign_role_to_member), '/textql.rpc.public.rbac.RBACService/RemoveRoleFromMember': EndpointSync.unary(method=MethodInfo(name='RemoveRoleFromMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveRoleFromMemberRequest, output=public_dot_rbac__pb2.RemoveRoleFromMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.remove_role_from_member), '/textql.rpc.public.rbac.RBACService/GetMemberRoles': EndpointSync.unary(method=MethodInfo(name='GetMemberRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberRolesRequest, output=public_dot_rbac__pb2.GetMemberRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_member_roles), '/textql.rpc.public.rbac.RBACService/GetCurrentMemberRolesAndPermissions': EndpointSync.unary(method=MethodInfo(name='GetCurrentMemberRolesAndPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, output=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_current_member_roles_and_permissions), '/textql.rpc.public.rbac.RBACService/CreateGroup': EndpointSync.unary(method=MethodInfo(name='CreateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateGroupRequest, output=public_dot_rbac__pb2.CreateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_group), '/textql.rpc.public.rbac.RBACService/GetGroup': EndpointSync.unary(method=MethodInfo(name='GetGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetGroupRequest, output=public_dot_rbac__pb2.GetGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_group), '/textql.rpc.public.rbac.RBACService/ListGroups': EndpointSync.unary(method=MethodInfo(name='ListGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupsRequest, output=public_dot_rbac__pb2.ListGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_groups), '/textql.rpc.public.rbac.RBACService/UpdateGroup': EndpointSync.unary(method=MethodInfo(name='UpdateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateGroupRequest, output=public_dot_rbac__pb2.UpdateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_group), '/textql.rpc.public.rbac.RBACService/DeleteGroup': EndpointSync.unary(method=MethodInfo(name='DeleteGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteGroupRequest, output=public_dot_rbac__pb2.DeleteGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_group), '/textql.rpc.public.rbac.RBACService/AddGroupMember': EndpointSync.unary(method=MethodInfo(name='AddGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AddGroupMemberRequest, output=public_dot_rbac__pb2.AddGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.add_group_member), '/textql.rpc.public.rbac.RBACService/RemoveGroupMember': EndpointSync.unary(method=MethodInfo(name='RemoveGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveGroupMemberRequest, output=public_dot_rbac__pb2.RemoveGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.remove_group_member), '/textql.rpc.public.rbac.RBACService/GetMemberGroups': EndpointSync.unary(method=MethodInfo(name='GetMemberGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberGroupsRequest, output=public_dot_rbac__pb2.GetMemberGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_member_groups), '/textql.rpc.public.rbac.RBACService/ShareObjectWithGroup': EndpointSync.unary(method=MethodInfo(name='ShareObjectWithGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithGroupRequest, output=public_dot_rbac__pb2.ShareObjectWithGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.share_object_with_group), '/textql.rpc.public.rbac.RBACService/ListGroupConnectors': EndpointSync.unary(method=MethodInfo(name='ListGroupConnectors', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupConnectorsRequest, output=public_dot_rbac__pb2.ListGroupConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_group_connectors), '/textql.rpc.public.rbac.RBACService/MigrateScimGroupMappingToGroup': EndpointSync.unary(method=MethodInfo(name='MigrateScimGroupMappingToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, output=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.migrate_scim_group_mapping_to_group), '/textql.rpc.public.rbac.RBACService/MigrateAllScimGroupMappings': EndpointSync.unary(method=MethodInfo(name='MigrateAllScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, output=public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.migrate_all_scim_group_mappings), '/textql.rpc.public.rbac.RBACService/RevertScimGroupMappingToRole': EndpointSync.unary(method=MethodInfo(name='RevertScimGroupMappingToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, output=public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revert_scim_group_mapping_to_role), '/textql.rpc.public.rbac.RBACService/ConvertRoleToGroup': EndpointSync.unary(method=MethodInfo(name='ConvertRoleToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ConvertRoleToGroupRequest, output=public_dot_rbac__pb2.ConvertRoleToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.convert_role_to_group), '/textql.rpc.public.rbac.RBACService/ListScimGroupMappings': EndpointSync.unary(method=MethodInfo(name='ListScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListScimGroupMappingsRequest, output=public_dot_rbac__pb2.ListScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_scim_group_mappings), '/textql.rpc.public.rbac.RBACService/ShareObject': EndpointSync.unary(method=MethodInfo(name='ShareObject', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectRequest, output=public_dot_rbac__pb2.ShareObjectResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.share_object), '/textql.rpc.public.rbac.RBACService/ShareObjectWithRole': EndpointSync.unary(method=MethodInfo(name='ShareObjectWithRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithRoleRequest, output=public_dot_rbac__pb2.ShareObjectWithRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.share_object_with_role), '/textql.rpc.public.rbac.RBACService/RevokeObjectAccess': EndpointSync.unary(method=MethodInfo(name='RevokeObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeObjectAccessRequest, output=public_dot_rbac__pb2.RevokeObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revoke_object_access), '/textql.rpc.public.rbac.RBACService/GetObjectAccess': EndpointSync.unary(method=MethodInfo(name='GetObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetObjectAccessRequest, output=public_dot_rbac__pb2.GetObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_object_access), '/textql.rpc.public.rbac.RBACService/HasObjectAccess': EndpointSync.unary(method=MethodInfo(name='HasObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.HasObjectAccessRequest, output=public_dot_rbac__pb2.HasObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.has_object_access), '/textql.rpc.public.rbac.RBACService/UpdateObjectVisibility': EndpointSync.unary(method=MethodInfo(name='UpdateObjectVisibility', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectVisibilityRequest, output=public_dot_rbac__pb2.UpdateObjectVisibilityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_object_visibility), '/textql.rpc.public.rbac.RBACService/UpdateObjectAccess': EndpointSync.unary(method=MethodInfo(name='UpdateObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectAccessRequest, output=public_dot_rbac__pb2.UpdateObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.update_object_access), '/textql.rpc.public.rbac.RBACService/GenerateShareLink': EndpointSync.unary(method=MethodInfo(name='GenerateShareLink', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GenerateShareLinkRequest, output=public_dot_rbac__pb2.GenerateShareLinkResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.generate_share_link), '/textql.rpc.public.rbac.RBACService/RequestAccess': EndpointSync.unary(method=MethodInfo(name='RequestAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RequestAccessRequest, output=public_dot_rbac__pb2.RequestAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.request_access), '/textql.rpc.public.rbac.RBACService/ListAccessRequests': EndpointSync.unary(method=MethodInfo(name='ListAccessRequests', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListAccessRequestsRequest, output=public_dot_rbac__pb2.ListAccessRequestsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_access_requests), '/textql.rpc.public.rbac.RBACService/ApproveAccessRequest': EndpointSync.unary(method=MethodInfo(name='ApproveAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ApproveAccessRequestRequest, output=public_dot_rbac__pb2.ApproveAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.approve_access_request), '/textql.rpc.public.rbac.RBACService/RejectAccessRequest': EndpointSync.unary(method=MethodInfo(name='RejectAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RejectAccessRequestRequest, output=public_dot_rbac__pb2.RejectAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.reject_access_request), '/textql.rpc.public.rbac.RBACService/CreateApiKey': EndpointSync.unary(method=MethodInfo(name='CreateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateApiKeyRequest, output=public_dot_rbac__pb2.CreateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_api_key), '/textql.rpc.public.rbac.RBACService/ListApiKeys': EndpointSync.unary(method=MethodInfo(name='ListApiKeys', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListApiKeysRequest, output=public_dot_rbac__pb2.ListApiKeysResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_api_keys), '/textql.rpc.public.rbac.RBACService/RevokeApiKey': EndpointSync.unary(method=MethodInfo(name='RevokeApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeApiKeyRequest, output=public_dot_rbac__pb2.RevokeApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.revoke_api_key), '/textql.rpc.public.rbac.RBACService/RotateApiKey': EndpointSync.unary(method=MethodInfo(name='RotateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RotateApiKeyRequest, output=public_dot_rbac__pb2.RotateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.rotate_api_key), '/textql.rpc.public.rbac.RBACService/GetEmbedUserApiKey': EndpointSync.unary(method=MethodInfo(name='GetEmbedUserApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, output=public_dot_rbac__pb2.GetEmbedUserApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.get_embed_user_api_key), '/textql.rpc.public.rbac.RBACService/CreateServiceAccount': EndpointSync.unary(method=MethodInfo(name='CreateServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateServiceAccountRequest, output=public_dot_rbac__pb2.CreateServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.create_service_account), '/textql.rpc.public.rbac.RBACService/ListServiceAccounts': EndpointSync.unary(method=MethodInfo(name='ListServiceAccounts', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListServiceAccountsRequest, output=public_dot_rbac__pb2.ListServiceAccountsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.list_service_accounts), '/textql.rpc.public.rbac.RBACService/DeleteServiceAccount': EndpointSync.unary(method=MethodInfo(name='DeleteServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteServiceAccountRequest, output=public_dot_rbac__pb2.DeleteServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), function=service.delete_service_account)}, interceptors=interceptors, read_max_bytes=read_max_bytes, compressions=compressions)

    @property
    def path(self) -> str:
        """Returns the URL path to mount the application to when serving multiple applications."""
        return '/textql.rpc.public.rbac.RBACService'

class RBACServiceClientSync(ConnectClientSync):

    def create_role(self, request: public_dot_rbac__pb2.CreateRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateRoleRequest, output=public_dot_rbac__pb2.CreateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_role(self, request: public_dot_rbac__pb2.GetRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRoleRequest, output=public_dot_rbac__pb2.GetRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_roles(self, request: public_dot_rbac__pb2.ListRolesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListRolesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListRolesRequest, output=public_dot_rbac__pb2.ListRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_role(self, request: public_dot_rbac__pb2.UpdateRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateRoleRequest, output=public_dot_rbac__pb2.UpdateRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_role(self, request: public_dot_rbac__pb2.DeleteRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.DeleteRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteRoleRequest, output=public_dot_rbac__pb2.DeleteRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_permissions(self, request: public_dot_rbac__pb2.ListPermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListPermissionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListPermissionsRequest, output=public_dot_rbac__pb2.ListPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_role_permissions(self, request: public_dot_rbac__pb2.GetRolePermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetRolePermissionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetRolePermissionsRequest, output=public_dot_rbac__pb2.GetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def assign_permission_to_role(self, request: public_dot_rbac__pb2.AssignPermissionToRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.AssignPermissionToRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AssignPermissionToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignPermissionToRoleRequest, output=public_dot_rbac__pb2.AssignPermissionToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def remove_permission_from_role(self, request: public_dot_rbac__pb2.RemovePermissionFromRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RemovePermissionFromRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RemovePermissionFromRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemovePermissionFromRoleRequest, output=public_dot_rbac__pb2.RemovePermissionFromRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def set_role_permissions(self, request: public_dot_rbac__pb2.SetRolePermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.SetRolePermissionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='SetRolePermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.SetRolePermissionsRequest, output=public_dot_rbac__pb2.SetRolePermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def assign_role_to_member(self, request: public_dot_rbac__pb2.AssignRoleToMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.AssignRoleToMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AssignRoleToMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AssignRoleToMemberRequest, output=public_dot_rbac__pb2.AssignRoleToMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def remove_role_from_member(self, request: public_dot_rbac__pb2.RemoveRoleFromMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RemoveRoleFromMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RemoveRoleFromMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveRoleFromMemberRequest, output=public_dot_rbac__pb2.RemoveRoleFromMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_member_roles(self, request: public_dot_rbac__pb2.GetMemberRolesRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetMemberRolesResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMemberRoles', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberRolesRequest, output=public_dot_rbac__pb2.GetMemberRolesResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_current_member_roles_and_permissions(self, request: public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetCurrentMemberRolesAndPermissions', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsRequest, output=public_dot_rbac__pb2.GetCurrentMemberRolesAndPermissionsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_group(self, request: public_dot_rbac__pb2.CreateGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateGroupResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateGroupRequest, output=public_dot_rbac__pb2.CreateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_group(self, request: public_dot_rbac__pb2.GetGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetGroupResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetGroupRequest, output=public_dot_rbac__pb2.GetGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_groups(self, request: public_dot_rbac__pb2.ListGroupsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListGroupsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupsRequest, output=public_dot_rbac__pb2.ListGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_group(self, request: public_dot_rbac__pb2.UpdateGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateGroupResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateGroupRequest, output=public_dot_rbac__pb2.UpdateGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_group(self, request: public_dot_rbac__pb2.DeleteGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.DeleteGroupResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteGroupRequest, output=public_dot_rbac__pb2.DeleteGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def add_group_member(self, request: public_dot_rbac__pb2.AddGroupMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.AddGroupMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='AddGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.AddGroupMemberRequest, output=public_dot_rbac__pb2.AddGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def remove_group_member(self, request: public_dot_rbac__pb2.RemoveGroupMemberRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RemoveGroupMemberResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RemoveGroupMember', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RemoveGroupMemberRequest, output=public_dot_rbac__pb2.RemoveGroupMemberResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_member_groups(self, request: public_dot_rbac__pb2.GetMemberGroupsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetMemberGroupsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetMemberGroups', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetMemberGroupsRequest, output=public_dot_rbac__pb2.GetMemberGroupsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def share_object_with_group(self, request: public_dot_rbac__pb2.ShareObjectWithGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ShareObjectWithGroupResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ShareObjectWithGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithGroupRequest, output=public_dot_rbac__pb2.ShareObjectWithGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_group_connectors(self, request: public_dot_rbac__pb2.ListGroupConnectorsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListGroupConnectorsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListGroupConnectors', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListGroupConnectorsRequest, output=public_dot_rbac__pb2.ListGroupConnectorsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def migrate_scim_group_mapping_to_group(self, request: public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='MigrateScimGroupMappingToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupRequest, output=public_dot_rbac__pb2.MigrateScimGroupMappingToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def migrate_all_scim_group_mappings(self, request: public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='MigrateAllScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.MigrateAllScimGroupMappingsRequest, output=public_dot_rbac__pb2.MigrateAllScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def revert_scim_group_mapping_to_role(self, request: public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevertScimGroupMappingToRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevertScimGroupMappingToRoleRequest, output=public_dot_rbac__pb2.RevertScimGroupMappingToRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def convert_role_to_group(self, request: public_dot_rbac__pb2.ConvertRoleToGroupRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ConvertRoleToGroupResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ConvertRoleToGroup', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ConvertRoleToGroupRequest, output=public_dot_rbac__pb2.ConvertRoleToGroupResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_scim_group_mappings(self, request: public_dot_rbac__pb2.ListScimGroupMappingsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListScimGroupMappingsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListScimGroupMappings', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListScimGroupMappingsRequest, output=public_dot_rbac__pb2.ListScimGroupMappingsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def share_object(self, request: public_dot_rbac__pb2.ShareObjectRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ShareObjectResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ShareObject', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectRequest, output=public_dot_rbac__pb2.ShareObjectResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def share_object_with_role(self, request: public_dot_rbac__pb2.ShareObjectWithRoleRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ShareObjectWithRoleResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ShareObjectWithRole', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ShareObjectWithRoleRequest, output=public_dot_rbac__pb2.ShareObjectWithRoleResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def revoke_object_access(self, request: public_dot_rbac__pb2.RevokeObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RevokeObjectAccessResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevokeObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeObjectAccessRequest, output=public_dot_rbac__pb2.RevokeObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_object_access(self, request: public_dot_rbac__pb2.GetObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetObjectAccessResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetObjectAccessRequest, output=public_dot_rbac__pb2.GetObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def has_object_access(self, request: public_dot_rbac__pb2.HasObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.HasObjectAccessResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='HasObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.HasObjectAccessRequest, output=public_dot_rbac__pb2.HasObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_object_visibility(self, request: public_dot_rbac__pb2.UpdateObjectVisibilityRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateObjectVisibilityResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateObjectVisibility', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectVisibilityRequest, output=public_dot_rbac__pb2.UpdateObjectVisibilityResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def update_object_access(self, request: public_dot_rbac__pb2.UpdateObjectAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.UpdateObjectAccessResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='UpdateObjectAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.UpdateObjectAccessRequest, output=public_dot_rbac__pb2.UpdateObjectAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def generate_share_link(self, request: public_dot_rbac__pb2.GenerateShareLinkRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GenerateShareLinkResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GenerateShareLink', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GenerateShareLinkRequest, output=public_dot_rbac__pb2.GenerateShareLinkResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def request_access(self, request: public_dot_rbac__pb2.RequestAccessRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RequestAccessResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RequestAccess', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RequestAccessRequest, output=public_dot_rbac__pb2.RequestAccessResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_access_requests(self, request: public_dot_rbac__pb2.ListAccessRequestsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListAccessRequestsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListAccessRequests', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListAccessRequestsRequest, output=public_dot_rbac__pb2.ListAccessRequestsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def approve_access_request(self, request: public_dot_rbac__pb2.ApproveAccessRequestRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ApproveAccessRequestResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ApproveAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ApproveAccessRequestRequest, output=public_dot_rbac__pb2.ApproveAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def reject_access_request(self, request: public_dot_rbac__pb2.RejectAccessRequestRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RejectAccessRequestResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RejectAccessRequest', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RejectAccessRequestRequest, output=public_dot_rbac__pb2.RejectAccessRequestResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_api_key(self, request: public_dot_rbac__pb2.CreateApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateApiKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateApiKeyRequest, output=public_dot_rbac__pb2.CreateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_api_keys(self, request: public_dot_rbac__pb2.ListApiKeysRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListApiKeysResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListApiKeys', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListApiKeysRequest, output=public_dot_rbac__pb2.ListApiKeysResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def revoke_api_key(self, request: public_dot_rbac__pb2.RevokeApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RevokeApiKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RevokeApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RevokeApiKeyRequest, output=public_dot_rbac__pb2.RevokeApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def rotate_api_key(self, request: public_dot_rbac__pb2.RotateApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.RotateApiKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='RotateApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.RotateApiKeyRequest, output=public_dot_rbac__pb2.RotateApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def get_embed_user_api_key(self, request: public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.GetEmbedUserApiKeyResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='GetEmbedUserApiKey', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.GetEmbedUserApiKeyRequest, output=public_dot_rbac__pb2.GetEmbedUserApiKeyResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def create_service_account(self, request: public_dot_rbac__pb2.CreateServiceAccountRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.CreateServiceAccountResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='CreateServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.CreateServiceAccountRequest, output=public_dot_rbac__pb2.CreateServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def list_service_accounts(self, request: public_dot_rbac__pb2.ListServiceAccountsRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.ListServiceAccountsResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='ListServiceAccounts', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.ListServiceAccountsRequest, output=public_dot_rbac__pb2.ListServiceAccountsResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)

    def delete_service_account(self, request: public_dot_rbac__pb2.DeleteServiceAccountRequest, *, headers: Headers | Mapping[str, str] | None=None, timeout_ms: int | None=None) -> public_dot_rbac__pb2.DeleteServiceAccountResponse:
        return self.execute_unary(request=request, method=MethodInfo(name='DeleteServiceAccount', service_name='textql.rpc.public.rbac.RBACService', input=public_dot_rbac__pb2.DeleteServiceAccountRequest, output=public_dot_rbac__pb2.DeleteServiceAccountResponse, idempotency_level=IdempotencyLevel.UNKNOWN), headers=headers, timeout_ms=timeout_ms)