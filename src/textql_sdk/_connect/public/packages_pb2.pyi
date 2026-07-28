# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OrgPackage(_message.Message):
    __slots__ = ('id', 'org_id', 'package_name', 'version', 'installed_version', 'status', 'error_message', 'installed_by', 'created_at', 'updated_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_BY_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    package_name: str
    version: str
    installed_version: str
    status: str
    error_message: str
    installed_by: str
    created_at: str
    updated_at: str

    def __init__(self, id: _Optional[str]=..., org_id: _Optional[str]=..., package_name: _Optional[str]=..., version: _Optional[str]=..., installed_version: _Optional[str]=..., status: _Optional[str]=..., error_message: _Optional[str]=..., installed_by: _Optional[str]=..., created_at: _Optional[str]=..., updated_at: _Optional[str]=...) -> None:
        ...

class ListOrgPackagesRequest(_message.Message):
    __slots__ = ('org_id',)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str

    def __init__(self, org_id: _Optional[str]=...) -> None:
        ...

class ListOrgPackagesResponse(_message.Message):
    __slots__ = ('packages',)
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.RepeatedCompositeFieldContainer[OrgPackage]

    def __init__(self, packages: _Optional[_Iterable[_Union[OrgPackage, _Mapping]]]=...) -> None:
        ...

class InstallOrgPackageRequest(_message.Message):
    __slots__ = ('org_id', 'package_name', 'version')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    package_name: str
    version: str

    def __init__(self, org_id: _Optional[str]=..., package_name: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class InstallOrgPackageResponse(_message.Message):
    __slots__ = ('package',)
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    package: OrgPackage

    def __init__(self, package: _Optional[_Union[OrgPackage, _Mapping]]=...) -> None:
        ...

class RemoveOrgPackageRequest(_message.Message):
    __slots__ = ('org_id', 'package_id')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    package_id: str

    def __init__(self, org_id: _Optional[str]=..., package_id: _Optional[str]=...) -> None:
        ...

class RemoveOrgPackageResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class GetOrgPackageStatusRequest(_message.Message):
    __slots__ = ('org_id', 'package_id')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    package_id: str

    def __init__(self, org_id: _Optional[str]=..., package_id: _Optional[str]=...) -> None:
        ...

class GetOrgPackageStatusResponse(_message.Message):
    __slots__ = ('package',)
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    package: OrgPackage

    def __init__(self, package: _Optional[_Union[OrgPackage, _Mapping]]=...) -> None:
        ...

class RetryInstallOrgPackageRequest(_message.Message):
    __slots__ = ('org_id', 'package_id')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    package_id: str

    def __init__(self, org_id: _Optional[str]=..., package_id: _Optional[str]=...) -> None:
        ...

class RetryInstallOrgPackageResponse(_message.Message):
    __slots__ = ('package',)
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    package: OrgPackage

    def __init__(self, package: _Optional[_Union[OrgPackage, _Mapping]]=...) -> None:
        ...

class UpdateOrgPackageVersionRequest(_message.Message):
    __slots__ = ('org_id', 'package_id', 'version')
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    package_id: str
    version: str

    def __init__(self, org_id: _Optional[str]=..., package_id: _Optional[str]=..., version: _Optional[str]=...) -> None:
        ...

class UpdateOrgPackageVersionResponse(_message.Message):
    __slots__ = ('package',)
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    package: OrgPackage

    def __init__(self, package: _Optional[_Union[OrgPackage, _Mapping]]=...) -> None:
        ...