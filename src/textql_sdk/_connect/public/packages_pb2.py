# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/packages.proto')
_sym_db = _symbol_database.Default()
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15public/packages.proto\x12\x1atextql.rpc.public.packages\x1a\x14public/options.proto"\xbb\x02\n\nOrgPackage\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12!\n\x0cpackage_name\x18\x03 \x01(\tR\x0bpackageName\x12\x18\n\x07version\x18\x04 \x01(\tR\x07version\x12+\n\x11installed_version\x18\x05 \x01(\tR\x10installedVersion\x12\x16\n\x06status\x18\x06 \x01(\tR\x06status\x12#\n\rerror_message\x18\x07 \x01(\tR\x0cerrorMessage\x12!\n\x0cinstalled_by\x18\x08 \x01(\tR\x0binstalledBy\x12\x1d\n\ncreated_at\x18\t \x01(\tR\tcreatedAt\x12\x1d\n\nupdated_at\x18\n \x01(\tR\tupdatedAt"/\n\x16ListOrgPackagesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId"]\n\x17ListOrgPackagesResponse\x12B\n\x08packages\x18\x01 \x03(\x0b2&.textql.rpc.public.packages.OrgPackageR\x08packages"n\n\x18InstallOrgPackageRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12!\n\x0cpackage_name\x18\x02 \x01(\tR\x0bpackageName\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version"]\n\x19InstallOrgPackageResponse\x12@\n\x07package\x18\x01 \x01(\x0b2&.textql.rpc.public.packages.OrgPackageR\x07package"O\n\x17RemoveOrgPackageRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\npackage_id\x18\x02 \x01(\tR\tpackageId"4\n\x18RemoveOrgPackageResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success"R\n\x1aGetOrgPackageStatusRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\npackage_id\x18\x02 \x01(\tR\tpackageId"_\n\x1bGetOrgPackageStatusResponse\x12@\n\x07package\x18\x01 \x01(\x0b2&.textql.rpc.public.packages.OrgPackageR\x07package"U\n\x1dRetryInstallOrgPackageRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\npackage_id\x18\x02 \x01(\tR\tpackageId"b\n\x1eRetryInstallOrgPackageResponse\x12@\n\x07package\x18\x01 \x01(\x0b2&.textql.rpc.public.packages.OrgPackageR\x07package"p\n\x1eUpdateOrgPackageVersionRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\npackage_id\x18\x02 \x01(\tR\tpackageId\x12\x18\n\x07version\x18\x03 \x01(\tR\x07version"c\n\x1fUpdateOrgPackageVersionResponse\x12@\n\x07package\x18\x01 \x01(\x0b2&.textql.rpc.public.packages.OrgPackageR\x07package2\xc1\x06\n\x11OrgPackageService\x12z\n\x0fListOrgPackages\x122.textql.rpc.public.packages.ListOrgPackagesRequest\x1a3.textql.rpc.public.packages.ListOrgPackagesResponse\x12\x80\x01\n\x11InstallOrgPackage\x124.textql.rpc.public.packages.InstallOrgPackageRequest\x1a5.textql.rpc.public.packages.InstallOrgPackageResponse\x12}\n\x10RemoveOrgPackage\x123.textql.rpc.public.packages.RemoveOrgPackageRequest\x1a4.textql.rpc.public.packages.RemoveOrgPackageResponse\x12\x86\x01\n\x13GetOrgPackageStatus\x126.textql.rpc.public.packages.GetOrgPackageStatusRequest\x1a7.textql.rpc.public.packages.GetOrgPackageStatusResponse\x12\x8f\x01\n\x16RetryInstallOrgPackage\x129.textql.rpc.public.packages.RetryInstallOrgPackageRequest\x1a:.textql.rpc.public.packages.RetryInstallOrgPackageResponse\x12\x92\x01\n\x17UpdateOrgPackageVersion\x12:.textql.rpc.public.packages.UpdateOrgPackageVersionRequest\x1a;.textql.rpc.public.packages.UpdateOrgPackageVersionResponseB\x0c\x92\xb5\x18\x08INTERNALb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.packages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\x92\xb5\x18\x08INTERNAL'
    _globals['_ORGPACKAGE']._serialized_start = 76
    _globals['_ORGPACKAGE']._serialized_end = 391
    _globals['_LISTORGPACKAGESREQUEST']._serialized_start = 393
    _globals['_LISTORGPACKAGESREQUEST']._serialized_end = 440
    _globals['_LISTORGPACKAGESRESPONSE']._serialized_start = 442
    _globals['_LISTORGPACKAGESRESPONSE']._serialized_end = 535
    _globals['_INSTALLORGPACKAGEREQUEST']._serialized_start = 537
    _globals['_INSTALLORGPACKAGEREQUEST']._serialized_end = 647
    _globals['_INSTALLORGPACKAGERESPONSE']._serialized_start = 649
    _globals['_INSTALLORGPACKAGERESPONSE']._serialized_end = 742
    _globals['_REMOVEORGPACKAGEREQUEST']._serialized_start = 744
    _globals['_REMOVEORGPACKAGEREQUEST']._serialized_end = 823
    _globals['_REMOVEORGPACKAGERESPONSE']._serialized_start = 825
    _globals['_REMOVEORGPACKAGERESPONSE']._serialized_end = 877
    _globals['_GETORGPACKAGESTATUSREQUEST']._serialized_start = 879
    _globals['_GETORGPACKAGESTATUSREQUEST']._serialized_end = 961
    _globals['_GETORGPACKAGESTATUSRESPONSE']._serialized_start = 963
    _globals['_GETORGPACKAGESTATUSRESPONSE']._serialized_end = 1058
    _globals['_RETRYINSTALLORGPACKAGEREQUEST']._serialized_start = 1060
    _globals['_RETRYINSTALLORGPACKAGEREQUEST']._serialized_end = 1145
    _globals['_RETRYINSTALLORGPACKAGERESPONSE']._serialized_start = 1147
    _globals['_RETRYINSTALLORGPACKAGERESPONSE']._serialized_end = 1245
    _globals['_UPDATEORGPACKAGEVERSIONREQUEST']._serialized_start = 1247
    _globals['_UPDATEORGPACKAGEVERSIONREQUEST']._serialized_end = 1359
    _globals['_UPDATEORGPACKAGEVERSIONRESPONSE']._serialized_start = 1361
    _globals['_UPDATEORGPACKAGEVERSIONRESPONSE']._serialized_end = 1460
    _globals['_ORGPACKAGESERVICE']._serialized_start = 1463
    _globals['_ORGPACKAGESERVICE']._serialized_end = 2296