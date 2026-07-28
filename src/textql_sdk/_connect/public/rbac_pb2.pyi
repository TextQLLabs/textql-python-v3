# pylint: skip-file
# mypy: ignore-errors
import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from ..public import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ApiKeyScope(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    API_KEY_SCOPE_UNSPECIFIED: _ClassVar[ApiKeyScope]
    API_KEY_SCOPE_ALL: _ClassVar[ApiKeyScope]
    API_KEY_SCOPE_PERSONAL: _ClassVar[ApiKeyScope]
    API_KEY_SCOPE_SERVICE_ACCOUNTS: _ClassVar[ApiKeyScope]

class ApiKeySortField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    API_KEY_SORT_FIELD_UNSPECIFIED: _ClassVar[ApiKeySortField]
    API_KEY_SORT_FIELD_CREATED_AT: _ClassVar[ApiKeySortField]
    API_KEY_SORT_FIELD_EXPIRES_AT: _ClassVar[ApiKeySortField]
    API_KEY_SORT_FIELD_NAME: _ClassVar[ApiKeySortField]

class ApiKeyStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    API_KEY_STATUS_UNSPECIFIED: _ClassVar[ApiKeyStatus]
    API_KEY_STATUS_ACTIVE: _ClassVar[ApiKeyStatus]
    API_KEY_STATUS_EXPIRED: _ClassVar[ApiKeyStatus]
    API_KEY_STATUS_REVOKED: _ClassVar[ApiKeyStatus]
API_KEY_SCOPE_UNSPECIFIED: ApiKeyScope
API_KEY_SCOPE_ALL: ApiKeyScope
API_KEY_SCOPE_PERSONAL: ApiKeyScope
API_KEY_SCOPE_SERVICE_ACCOUNTS: ApiKeyScope
API_KEY_SORT_FIELD_UNSPECIFIED: ApiKeySortField
API_KEY_SORT_FIELD_CREATED_AT: ApiKeySortField
API_KEY_SORT_FIELD_EXPIRES_AT: ApiKeySortField
API_KEY_SORT_FIELD_NAME: ApiKeySortField
API_KEY_STATUS_UNSPECIFIED: ApiKeyStatus
API_KEY_STATUS_ACTIVE: ApiKeyStatus
API_KEY_STATUS_EXPIRED: ApiKeyStatus
API_KEY_STATUS_REVOKED: ApiKeyStatus

class Role(_message.Message):
    __slots__ = ('id', 'org_id', 'name', 'description', 'is_system', 'created_at', 'updated_at', 'default_model_id', 'allowed_model_ids', 'allow_model_choice', 'is_scim_managed')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MODEL_CHOICE_FIELD_NUMBER: _ClassVar[int]
    IS_SCIM_MANAGED_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    name: str
    description: str
    is_system: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    default_model_id: int
    allowed_model_ids: _containers.RepeatedScalarFieldContainer[int]
    allow_model_choice: bool
    is_scim_managed: bool

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., is_system: bool=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., default_model_id: _Optional[int]=..., allowed_model_ids: _Optional[_Iterable[int]]=..., allow_model_choice: bool=..., is_scim_managed: bool=...) -> None:
        ...

class Permission(_message.Message):
    __slots__ = ('id', 'resource', 'action', 'description', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    resource: str
    action: str
    description: str
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., resource: _Optional[str]=..., action: _Optional[str]=..., description: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ObjectAccess(_message.Message):
    __slots__ = ('id', 'org_id', 'object_type', 'object_id', 'created_by', 'is_public', 'member_id', 'role_id', 'access_type', 'granted_by', 'expires_at', 'created_at', 'updated_at', 'group_id')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    GRANTED_BY_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    object_type: str
    object_id: str
    created_by: str
    is_public: bool
    member_id: str
    role_id: str
    access_type: str
    granted_by: str
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    group_id: str

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., object_type: _Optional[str]=..., object_id: _Optional[str]=..., created_by: _Optional[str]=..., is_public: bool=..., member_id: _Optional[str]=..., role_id: _Optional[str]=..., access_type: _Optional[str]=..., granted_by: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., group_id: _Optional[str]=...) -> None:
        ...

class Group(_message.Message):
    __slots__ = ('id', 'org_id', 'name', 'description', 'is_system', 'created_at', 'updated_at', 'is_scim_managed', 'member_count', 'connector_count')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    IS_SCIM_MANAGED_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    name: str
    description: str
    is_system: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    is_scim_managed: bool
    member_count: int
    connector_count: int

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., is_system: bool=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., is_scim_managed: bool=..., member_count: _Optional[int]=..., connector_count: _Optional[int]=...) -> None:
        ...

class CreateRoleRequest(_message.Message):
    __slots__ = ('name', 'description')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class CreateRoleResponse(_message.Message):
    __slots__ = ('role',)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role

    def __init__(self, role: _Optional[_Union[Role, _Mapping]]=...) -> None:
        ...

class GetRoleRequest(_message.Message):
    __slots__ = ('role_id',)
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: str

    def __init__(self, role_id: _Optional[str]=...) -> None:
        ...

class GetRoleResponse(_message.Message):
    __slots__ = ('role',)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role

    def __init__(self, role: _Optional[_Union[Role, _Mapping]]=...) -> None:
        ...

class ListRolesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListRolesResponse(_message.Message):
    __slots__ = ('roles',)
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]

    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]]=...) -> None:
        ...

class UpdateRoleRequest(_message.Message):
    __slots__ = ('role_id', 'name', 'description', 'default_model_id', 'allowed_model_ids', 'allow_model_choice', 'clear_allowed_model_ids')
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MODEL_CHOICE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_ALLOWED_MODEL_IDS_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    name: str
    description: str
    default_model_id: _wrappers_pb2.Int32Value
    allowed_model_ids: _containers.RepeatedScalarFieldContainer[int]
    allow_model_choice: _wrappers_pb2.BoolValue
    clear_allowed_model_ids: bool

    def __init__(self, role_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., default_model_id: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]]=..., allowed_model_ids: _Optional[_Iterable[int]]=..., allow_model_choice: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]]=..., clear_allowed_model_ids: bool=...) -> None:
        ...

class UpdateRoleResponse(_message.Message):
    __slots__ = ('role',)
    ROLE_FIELD_NUMBER: _ClassVar[int]
    role: Role

    def __init__(self, role: _Optional[_Union[Role, _Mapping]]=...) -> None:
        ...

class DeleteRoleRequest(_message.Message):
    __slots__ = ('role_id',)
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: str

    def __init__(self, role_id: _Optional[str]=...) -> None:
        ...

class DeleteRoleResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class ListPermissionsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListPermissionsResponse(_message.Message):
    __slots__ = ('permissions',)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]

    def __init__(self, permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]]=...) -> None:
        ...

class GetRolePermissionsRequest(_message.Message):
    __slots__ = ('role_id',)
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: str

    def __init__(self, role_id: _Optional[str]=...) -> None:
        ...

class GetRolePermissionsResponse(_message.Message):
    __slots__ = ('permissions',)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]

    def __init__(self, permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]]=...) -> None:
        ...

class AssignPermissionToRoleRequest(_message.Message):
    __slots__ = ('role_id', 'permission_id')
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    permission_id: str

    def __init__(self, role_id: _Optional[str]=..., permission_id: _Optional[str]=...) -> None:
        ...

class AssignPermissionToRoleResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class RemovePermissionFromRoleRequest(_message.Message):
    __slots__ = ('role_id', 'permission_id')
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ID_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    permission_id: str

    def __init__(self, role_id: _Optional[str]=..., permission_id: _Optional[str]=...) -> None:
        ...

class RemovePermissionFromRoleResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class SetRolePermissionsRequest(_message.Message):
    __slots__ = ('role_id', 'add_permission_ids', 'remove_permission_ids')
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ADD_PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVE_PERMISSION_IDS_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    add_permission_ids: _containers.RepeatedScalarFieldContainer[str]
    remove_permission_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, role_id: _Optional[str]=..., add_permission_ids: _Optional[_Iterable[str]]=..., remove_permission_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class SetRolePermissionsResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class AssignRoleToMemberRequest(_message.Message):
    __slots__ = ('member_id', 'role_id')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    role_id: str

    def __init__(self, member_id: _Optional[str]=..., role_id: _Optional[str]=...) -> None:
        ...

class AssignRoleToMemberResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class RemoveRoleFromMemberRequest(_message.Message):
    __slots__ = ('member_id', 'role_id')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    role_id: str

    def __init__(self, member_id: _Optional[str]=..., role_id: _Optional[str]=...) -> None:
        ...

class RemoveRoleFromMemberResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GetMemberRolesRequest(_message.Message):
    __slots__ = ('member_ids',)
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    member_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, member_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMemberRolesResponse(_message.Message):
    __slots__ = ('member_roles',)

    class MemberRolesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MemberRoles

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[MemberRoles, _Mapping]]=...) -> None:
            ...
    MEMBER_ROLES_FIELD_NUMBER: _ClassVar[int]
    member_roles: _containers.MessageMap[str, MemberRoles]

    def __init__(self, member_roles: _Optional[_Mapping[str, MemberRoles]]=...) -> None:
        ...

class MemberRoles(_message.Message):
    __slots__ = ('roles',)
    ROLES_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]

    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]]=...) -> None:
        ...

class GetCurrentMemberRolesAndPermissionsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetCurrentMemberRolesAndPermissionsResponse(_message.Message):
    __slots__ = ('roles', 'permissions')
    ROLES_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    roles: _containers.RepeatedCompositeFieldContainer[Role]
    permissions: _containers.RepeatedCompositeFieldContainer[Permission]

    def __init__(self, roles: _Optional[_Iterable[_Union[Role, _Mapping]]]=..., permissions: _Optional[_Iterable[_Union[Permission, _Mapping]]]=...) -> None:
        ...

class ShareObjectRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'member_id', 'access_type', 'expires_at', 'is_public')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    member_id: str
    access_type: str
    expires_at: _timestamp_pb2.Timestamp
    is_public: bool

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., member_id: _Optional[str]=..., access_type: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., is_public: bool=...) -> None:
        ...

class ShareObjectResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class ShareObjectWithRoleRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'role_id', 'access_type', 'expires_at', 'is_public')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    role_id: str
    access_type: str
    expires_at: _timestamp_pb2.Timestamp
    is_public: bool

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., role_id: _Optional[str]=..., access_type: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., is_public: bool=...) -> None:
        ...

class ShareObjectWithRoleResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class RevokeObjectAccessRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'member_id', 'role_id', 'group_id')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    member_id: str
    role_id: str
    group_id: str

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., member_id: _Optional[str]=..., role_id: _Optional[str]=..., group_id: _Optional[str]=...) -> None:
        ...

class RevokeObjectAccessResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GetObjectAccessRequest(_message.Message):
    __slots__ = ('object_type', 'object_id')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=...) -> None:
        ...

class GetObjectAccessResponse(_message.Message):
    __slots__ = ('access_entries',)
    ACCESS_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    access_entries: _containers.RepeatedCompositeFieldContainer[ObjectAccess]

    def __init__(self, access_entries: _Optional[_Iterable[_Union[ObjectAccess, _Mapping]]]=...) -> None:
        ...

class HasObjectAccessRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'member_id', 'role_id', 'group_id')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    member_id: str
    role_id: str
    group_id: str

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., member_id: _Optional[str]=..., role_id: _Optional[str]=..., group_id: _Optional[str]=...) -> None:
        ...

class HasObjectAccessResponse(_message.Message):
    __slots__ = ('has_access',)
    HAS_ACCESS_FIELD_NUMBER: _ClassVar[int]
    has_access: bool

    def __init__(self, has_access: bool=...) -> None:
        ...

class UpdateObjectVisibilityRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'is_public')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    is_public: bool

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., is_public: bool=...) -> None:
        ...

class UpdateObjectVisibilityResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class UpdateObjectAccessRequest(_message.Message):
    __slots__ = ('access_id', 'access_type', 'expires_at')
    ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    access_id: str
    access_type: str
    expires_at: _timestamp_pb2.Timestamp

    def __init__(self, access_id: _Optional[str]=..., access_type: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpdateObjectAccessResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GenerateShareLinkRequest(_message.Message):
    __slots__ = ('object_type', 'object_id')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=...) -> None:
        ...

class GenerateShareLinkResponse(_message.Message):
    __slots__ = ('share_link',)
    SHARE_LINK_FIELD_NUMBER: _ClassVar[int]
    share_link: str

    def __init__(self, share_link: _Optional[str]=...) -> None:
        ...

class AccessRequest(_message.Message):
    __slots__ = ('id', 'org_id', 'object_type', 'object_id', 'member_id', 'requested_access_type', 'justification', 'request_message', 'status', 'reviewed_by', 'rejection_reason', 'created_at', 'updated_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_BY_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    object_type: str
    object_id: str
    member_id: str
    requested_access_type: str
    justification: str
    request_message: str
    status: str
    reviewed_by: str
    rejection_reason: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., object_type: _Optional[str]=..., object_id: _Optional[str]=..., member_id: _Optional[str]=..., requested_access_type: _Optional[str]=..., justification: _Optional[str]=..., request_message: _Optional[str]=..., status: _Optional[str]=..., reviewed_by: _Optional[str]=..., rejection_reason: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class RequestAccessRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'requested_access_type', 'justification', 'request_message')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    JUSTIFICATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    requested_access_type: str
    justification: str
    request_message: str

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., requested_access_type: _Optional[str]=..., justification: _Optional[str]=..., request_message: _Optional[str]=...) -> None:
        ...

class RequestAccessResponse(_message.Message):
    __slots__ = ('success', 'request_id')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    request_id: str

    def __init__(self, success: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class ListAccessRequestsRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'status')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    status: str

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., status: _Optional[str]=...) -> None:
        ...

class ListAccessRequestsResponse(_message.Message):
    __slots__ = ('requests',)
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    requests: _containers.RepeatedCompositeFieldContainer[AccessRequest]

    def __init__(self, requests: _Optional[_Iterable[_Union[AccessRequest, _Mapping]]]=...) -> None:
        ...

class ApproveAccessRequestRequest(_message.Message):
    __slots__ = ('request_id',)
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    request_id: str

    def __init__(self, request_id: _Optional[str]=...) -> None:
        ...

class ApproveAccessRequestResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class RejectAccessRequestRequest(_message.Message):
    __slots__ = ('request_id', 'rejection_reason')
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    rejection_reason: str

    def __init__(self, request_id: _Optional[str]=..., rejection_reason: _Optional[str]=...) -> None:
        ...

class RejectAccessRequestResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class CreateGroupRequest(_message.Message):
    __slots__ = ('name', 'description', 'member_ids')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    member_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., member_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateGroupResponse(_message.Message):
    __slots__ = ('group',)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: Group

    def __init__(self, group: _Optional[_Union[Group, _Mapping]]=...) -> None:
        ...

class GetGroupRequest(_message.Message):
    __slots__ = ('group_id',)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str

    def __init__(self, group_id: _Optional[str]=...) -> None:
        ...

class GetGroupResponse(_message.Message):
    __slots__ = ('group', 'member_ids')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    group: Group
    member_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, group: _Optional[_Union[Group, _Mapping]]=..., member_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class ListGroupsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListGroupsResponse(_message.Message):
    __slots__ = ('groups',)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]

    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]]=...) -> None:
        ...

class UpdateGroupRequest(_message.Message):
    __slots__ = ('group_id', 'name', 'description')
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    name: str
    description: str

    def __init__(self, group_id: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class UpdateGroupResponse(_message.Message):
    __slots__ = ('group',)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: Group

    def __init__(self, group: _Optional[_Union[Group, _Mapping]]=...) -> None:
        ...

class DeleteGroupRequest(_message.Message):
    __slots__ = ('group_id',)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str

    def __init__(self, group_id: _Optional[str]=...) -> None:
        ...

class DeleteGroupResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class AddGroupMemberRequest(_message.Message):
    __slots__ = ('group_id', 'member_id')
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    member_id: str

    def __init__(self, group_id: _Optional[str]=..., member_id: _Optional[str]=...) -> None:
        ...

class AddGroupMemberResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class RemoveGroupMemberRequest(_message.Message):
    __slots__ = ('group_id', 'member_id')
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    member_id: str

    def __init__(self, group_id: _Optional[str]=..., member_id: _Optional[str]=...) -> None:
        ...

class RemoveGroupMemberResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GetMemberGroupsRequest(_message.Message):
    __slots__ = ('member_ids',)
    MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    member_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, member_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetMemberGroupsResponse(_message.Message):
    __slots__ = ('member_groups',)

    class MemberGroupsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: MemberGroups

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[MemberGroups, _Mapping]]=...) -> None:
            ...
    MEMBER_GROUPS_FIELD_NUMBER: _ClassVar[int]
    member_groups: _containers.MessageMap[str, MemberGroups]

    def __init__(self, member_groups: _Optional[_Mapping[str, MemberGroups]]=...) -> None:
        ...

class MemberGroups(_message.Message):
    __slots__ = ('groups',)
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[Group]

    def __init__(self, groups: _Optional[_Iterable[_Union[Group, _Mapping]]]=...) -> None:
        ...

class ShareObjectWithGroupRequest(_message.Message):
    __slots__ = ('object_type', 'object_id', 'group_id', 'access_type', 'expires_at', 'is_public')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str
    group_id: str
    access_type: str
    expires_at: _timestamp_pb2.Timestamp
    is_public: bool

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=..., group_id: _Optional[str]=..., access_type: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., is_public: bool=...) -> None:
        ...

class ShareObjectWithGroupResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class ListGroupConnectorsRequest(_message.Message):
    __slots__ = ('group_id',)
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    group_id: str

    def __init__(self, group_id: _Optional[str]=...) -> None:
        ...

class GroupConnectorAccess(_message.Message):
    __slots__ = ('access_id', 'connector_id', 'connector_name', 'access_type')
    ACCESS_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_NAME_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    access_id: str
    connector_id: str
    connector_name: str
    access_type: str

    def __init__(self, access_id: _Optional[str]=..., connector_id: _Optional[str]=..., connector_name: _Optional[str]=..., access_type: _Optional[str]=...) -> None:
        ...

class ListGroupConnectorsResponse(_message.Message):
    __slots__ = ('connectors',)
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    connectors: _containers.RepeatedCompositeFieldContainer[GroupConnectorAccess]

    def __init__(self, connectors: _Optional[_Iterable[_Union[GroupConnectorAccess, _Mapping]]]=...) -> None:
        ...

class MigrateScimGroupMappingToGroupRequest(_message.Message):
    __slots__ = ('mapping_id',)
    MAPPING_ID_FIELD_NUMBER: _ClassVar[int]
    mapping_id: str

    def __init__(self, mapping_id: _Optional[str]=...) -> None:
        ...

class MigrateScimGroupMappingToGroupResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MigrateAllScimGroupMappingsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MigrateAllScimGroupMappingsResponse(_message.Message):
    __slots__ = ('migrated_mapping_count',)
    MIGRATED_MAPPING_COUNT_FIELD_NUMBER: _ClassVar[int]
    migrated_mapping_count: int

    def __init__(self, migrated_mapping_count: _Optional[int]=...) -> None:
        ...

class ConvertRoleToGroupRequest(_message.Message):
    __slots__ = ('role_id', 'drop_permissions')
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    DROP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    drop_permissions: bool

    def __init__(self, role_id: _Optional[str]=..., drop_permissions: bool=...) -> None:
        ...

class ConvertRoleToGroupResponse(_message.Message):
    __slots__ = ('group_id', 'migrated_member_count')
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    MIGRATED_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    group_id: str
    migrated_member_count: int

    def __init__(self, group_id: _Optional[str]=..., migrated_member_count: _Optional[int]=...) -> None:
        ...

class ListScimGroupMappingsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ScimGroupMappingSummary(_message.Message):
    __slots__ = ('id', 'display_name', 'external_id', 'role_id', 'role_name', 'group_id', 'group_name', 'target_mode', 'is_system')
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_SYSTEM_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    external_id: str
    role_id: str
    role_name: str
    group_id: str
    group_name: str
    target_mode: str
    is_system: bool

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., external_id: _Optional[str]=..., role_id: _Optional[str]=..., role_name: _Optional[str]=..., group_id: _Optional[str]=..., group_name: _Optional[str]=..., target_mode: _Optional[str]=..., is_system: bool=...) -> None:
        ...

class RevertScimGroupMappingToRoleRequest(_message.Message):
    __slots__ = ('mapping_id',)
    MAPPING_ID_FIELD_NUMBER: _ClassVar[int]
    mapping_id: str

    def __init__(self, mapping_id: _Optional[str]=...) -> None:
        ...

class RevertScimGroupMappingToRoleResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class ListScimGroupMappingsResponse(_message.Message):
    __slots__ = ('mappings',)
    MAPPINGS_FIELD_NUMBER: _ClassVar[int]
    mappings: _containers.RepeatedCompositeFieldContainer[ScimGroupMappingSummary]

    def __init__(self, mappings: _Optional[_Iterable[_Union[ScimGroupMappingSummary, _Mapping]]]=...) -> None:
        ...

class ApiKey(_message.Message):
    __slots__ = ('id', 'member_id', 'client_id', 'created_at', 'api_key_short', 'assumed_roles', 'name', 'expires_at', 'revoked_at', 'status', 'owner_display_name', 'owner_email', 'suppress_superadmin')
    ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SHORT_FIELD_NUMBER: _ClassVar[int]
    ASSUMED_ROLES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_AT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OWNER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_SUPERADMIN_FIELD_NUMBER: _ClassVar[int]
    id: str
    member_id: str
    client_id: str
    created_at: _timestamp_pb2.Timestamp
    api_key_short: str
    assumed_roles: _containers.RepeatedScalarFieldContainer[str]
    name: str
    expires_at: _timestamp_pb2.Timestamp
    revoked_at: _timestamp_pb2.Timestamp
    status: ApiKeyStatus
    owner_display_name: str
    owner_email: str
    suppress_superadmin: bool

    def __init__(self, id: _Optional[str]=..., member_id: _Optional[str]=..., client_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., api_key_short: _Optional[str]=..., assumed_roles: _Optional[_Iterable[str]]=..., name: _Optional[str]=..., expires_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., revoked_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., status: _Optional[_Union[ApiKeyStatus, str]]=..., owner_display_name: _Optional[str]=..., owner_email: _Optional[str]=..., suppress_superadmin: bool=...) -> None:
        ...

class CreateApiKeyRequest(_message.Message):
    __slots__ = ('expiry_seconds', 'assumed_roles', 'inherit_all_roles', 'name', 'target_member_id', 'client_id', 'suppress_superadmin')
    EXPIRY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ASSUMED_ROLES_FIELD_NUMBER: _ClassVar[int]
    INHERIT_ALL_ROLES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_SUPERADMIN_FIELD_NUMBER: _ClassVar[int]
    expiry_seconds: int
    assumed_roles: _containers.RepeatedScalarFieldContainer[str]
    inherit_all_roles: bool
    name: str
    target_member_id: str
    client_id: str
    suppress_superadmin: bool

    def __init__(self, expiry_seconds: _Optional[int]=..., assumed_roles: _Optional[_Iterable[str]]=..., inherit_all_roles: bool=..., name: _Optional[str]=..., target_member_id: _Optional[str]=..., client_id: _Optional[str]=..., suppress_superadmin: bool=...) -> None:
        ...

class CreateApiKeyResponse(_message.Message):
    __slots__ = ('api_key', 'api_key_secret', 'api_key_hash')
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SECRET_FIELD_NUMBER: _ClassVar[int]
    API_KEY_HASH_FIELD_NUMBER: _ClassVar[int]
    api_key: ApiKey
    api_key_secret: str
    api_key_hash: str

    def __init__(self, api_key: _Optional[_Union[ApiKey, _Mapping]]=..., api_key_secret: _Optional[str]=..., api_key_hash: _Optional[str]=...) -> None:
        ...

class ListApiKeysRequest(_message.Message):
    __slots__ = ('scope', 'service_account_member_id', 'include_revoked', 'search_term', 'sort_by', 'sort_direction', 'page_size', 'page_token')
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_REVOKED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    SORT_BY_FIELD_NUMBER: _ClassVar[int]
    SORT_DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    scope: ApiKeyScope
    service_account_member_id: str
    include_revoked: bool
    search_term: str
    sort_by: ApiKeySortField
    sort_direction: _common_pb2.SortDirection
    page_size: int
    page_token: str

    def __init__(self, scope: _Optional[_Union[ApiKeyScope, str]]=..., service_account_member_id: _Optional[str]=..., include_revoked: bool=..., search_term: _Optional[str]=..., sort_by: _Optional[_Union[ApiKeySortField, str]]=..., sort_direction: _Optional[_Union[_common_pb2.SortDirection, str]]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListApiKeysResponse(_message.Message):
    __slots__ = ('api_keys', 'next_page_token')
    API_KEYS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    api_keys: _containers.RepeatedCompositeFieldContainer[ApiKey]
    next_page_token: str

    def __init__(self, api_keys: _Optional[_Iterable[_Union[ApiKey, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RevokeApiKeyRequest(_message.Message):
    __slots__ = ('api_key_id',)
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    api_key_id: str

    def __init__(self, api_key_id: _Optional[str]=...) -> None:
        ...

class RevokeApiKeyResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class RotateApiKeyRequest(_message.Message):
    __slots__ = ('api_key_id',)
    API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    api_key_id: str

    def __init__(self, api_key_id: _Optional[str]=...) -> None:
        ...

class RotateApiKeyResponse(_message.Message):
    __slots__ = ('api_key', 'api_key_secret', 'revoked_api_key_id')
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SECRET_FIELD_NUMBER: _ClassVar[int]
    REVOKED_API_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    api_key: ApiKey
    api_key_secret: str
    revoked_api_key_id: str

    def __init__(self, api_key: _Optional[_Union[ApiKey, _Mapping]]=..., api_key_secret: _Optional[str]=..., revoked_api_key_id: _Optional[str]=...) -> None:
        ...

class GetEmbedUserApiKeyRequest(_message.Message):
    __slots__ = ('member_id',)
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str

    def __init__(self, member_id: _Optional[str]=...) -> None:
        ...

class GetEmbedUserApiKeyResponse(_message.Message):
    __slots__ = ('api_key_base64', 'api_key_short', 'service_account_email')
    API_KEY_BASE64_FIELD_NUMBER: _ClassVar[int]
    API_KEY_SHORT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    api_key_base64: str
    api_key_short: str
    service_account_email: str

    def __init__(self, api_key_base64: _Optional[str]=..., api_key_short: _Optional[str]=..., service_account_email: _Optional[str]=...) -> None:
        ...

class CreateServiceAccountRequest(_message.Message):
    __slots__ = ('name', 'description', 'owner_member_id', 'role_ids')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    owner_member_id: str
    role_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., owner_member_id: _Optional[str]=..., role_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateServiceAccountResponse(_message.Message):
    __slots__ = ('member_id', 'email')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    email: str

    def __init__(self, member_id: _Optional[str]=..., email: _Optional[str]=...) -> None:
        ...

class ServiceAccount(_message.Message):
    __slots__ = ('member_id', 'email', 'display_name', 'description', 'owner_member_id', 'created_at', 'agent_id')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    email: str
    display_name: str
    description: str
    owner_member_id: str
    created_at: _timestamp_pb2.Timestamp
    agent_id: str

    def __init__(self, member_id: _Optional[str]=..., email: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., owner_member_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., agent_id: _Optional[str]=...) -> None:
        ...

class ListServiceAccountsRequest(_message.Message):
    __slots__ = ('search_term', 'page_size', 'page_token')
    SEARCH_TERM_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_term: str
    page_size: int
    page_token: str

    def __init__(self, search_term: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListServiceAccountsResponse(_message.Message):
    __slots__ = ('service_accounts', 'next_page_token')
    SERVICE_ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    service_accounts: _containers.RepeatedCompositeFieldContainer[ServiceAccount]
    next_page_token: str

    def __init__(self, service_accounts: _Optional[_Iterable[_Union[ServiceAccount, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteServiceAccountRequest(_message.Message):
    __slots__ = ('member_id',)
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    member_id: str

    def __init__(self, member_id: _Optional[str]=...) -> None:
        ...

class DeleteServiceAccountResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...