# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 6, 31, 1, '', 'public/metrics_export.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ..public import options_pb2 as public_dot_options__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bpublic/metrics_export.proto\x12 textql.rpc.public.metrics_export\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14public/options.proto"\xde\x03\n\x13MetricsExportConfig\x12-\n\x12prometheus_enabled\x18\x01 \x01(\x08R\x11prometheusEnabled\x12!\n\x0cotlp_enabled\x18\x02 \x01(\x08R\x0botlpEnabled\x12#\n\rotlp_endpoint\x18\x03 \x01(\tR\x0cotlpEndpoint\x12\'\n\x0cotlp_headers\x18\x04 \x01(\tB\x04\x88\xb5\x18\x01R\x0botlpHeaders\x12#\n\rotlp_protocol\x18\x05 \x01(\tR\x0cotlpProtocol\x122\n\x15push_interval_seconds\x18\x06 \x01(\x05R\x13pushIntervalSeconds\x12E\n\x0elast_pushed_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x0clastPushedAt\x88\x01\x01\x129\n\ncreated_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampR\tcreatedAt\x129\n\nupdated_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampR\tupdatedAtB\x11\n\x0f_last_pushed_at"\x98\x02\n\x1dConfigureMetricsExportRequest\x12-\n\x12prometheus_enabled\x18\x01 \x01(\x08R\x11prometheusEnabled\x12!\n\x0cotlp_enabled\x18\x02 \x01(\x08R\x0botlpEnabled\x12#\n\rotlp_endpoint\x18\x03 \x01(\tR\x0cotlpEndpoint\x12\'\n\x0cotlp_headers\x18\x04 \x01(\tB\x04\x88\xb5\x18\x01R\x0botlpHeaders\x12#\n\rotlp_protocol\x18\x05 \x01(\tR\x0cotlpProtocol\x122\n\x15push_interval_seconds\x18\x06 \x01(\x05R\x13pushIntervalSeconds"o\n\x1eConfigureMetricsExportResponse\x12M\n\x06config\x18\x01 \x01(\x0b25.textql.rpc.public.metrics_export.MetricsExportConfigR\x06config"\x1f\n\x1dGetMetricsExportConfigRequest"\x7f\n\x1eGetMetricsExportConfigResponse\x12R\n\x06config\x18\x01 \x01(\x0b25.textql.rpc.public.metrics_export.MetricsExportConfigH\x00R\x06config\x88\x01\x01B\t\n\x07_config""\n DeleteMetricsExportConfigRequest"#\n!DeleteMetricsExportConfigResponse"\x97\x01\n"TestMetricsExportConnectionRequest\x12#\n\rotlp_endpoint\x18\x01 \x01(\tR\x0cotlpEndpoint\x12\'\n\x0cotlp_headers\x18\x02 \x01(\tB\x04\x88\xb5\x18\x01R\x0botlpHeaders\x12#\n\rotlp_protocol\x18\x03 \x01(\tR\x0cotlpProtocol"d\n#TestMetricsExportConnectionResponse\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12#\n\rerror_message\x18\x02 \x01(\tR\x0cerrorMessage"\x1b\n\x19TriggerMetricsPushRequest":\n\x1aTriggerMetricsPushResponse\x12\x1c\n\ttriggered\x18\x01 \x01(\x08R\ttriggered2\xc8\x06\n\x14MetricsExportService\x12\x9d\x01\n\x16ConfigureMetricsExport\x12?.textql.rpc.public.metrics_export.ConfigureMetricsExportRequest\x1a@.textql.rpc.public.metrics_export.ConfigureMetricsExportResponse"\x00\x12\xa0\x01\n\x16GetMetricsExportConfig\x12?.textql.rpc.public.metrics_export.GetMetricsExportConfigRequest\x1a@.textql.rpc.public.metrics_export.GetMetricsExportConfigResponse"\x03\x90\x02\x01\x12\xa6\x01\n\x19DeleteMetricsExportConfig\x12B.textql.rpc.public.metrics_export.DeleteMetricsExportConfigRequest\x1aC.textql.rpc.public.metrics_export.DeleteMetricsExportConfigResponse"\x00\x12\xaf\x01\n\x1bTestMetricsExportConnection\x12D.textql.rpc.public.metrics_export.TestMetricsExportConnectionRequest\x1aE.textql.rpc.public.metrics_export.TestMetricsExportConnectionResponse"\x03\x90\x02\x01\x12\x91\x01\n\x12TriggerMetricsPush\x12;.textql.rpc.public.metrics_export.TriggerMetricsPushRequest\x1a<.textql.rpc.public.metrics_export.TriggerMetricsPushResponse"\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'public.metrics_export_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_METRICSEXPORTCONFIG'].fields_by_name['otlp_headers']._loaded_options = None
    _globals['_METRICSEXPORTCONFIG'].fields_by_name['otlp_headers']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_CONFIGUREMETRICSEXPORTREQUEST'].fields_by_name['otlp_headers']._loaded_options = None
    _globals['_CONFIGUREMETRICSEXPORTREQUEST'].fields_by_name['otlp_headers']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_TESTMETRICSEXPORTCONNECTIONREQUEST'].fields_by_name['otlp_headers']._loaded_options = None
    _globals['_TESTMETRICSEXPORTCONNECTIONREQUEST'].fields_by_name['otlp_headers']._serialized_options = b'\x88\xb5\x18\x01'
    _globals['_METRICSEXPORTSERVICE'].methods_by_name['GetMetricsExportConfig']._loaded_options = None
    _globals['_METRICSEXPORTSERVICE'].methods_by_name['GetMetricsExportConfig']._serialized_options = b'\x90\x02\x01'
    _globals['_METRICSEXPORTSERVICE'].methods_by_name['TestMetricsExportConnection']._loaded_options = None
    _globals['_METRICSEXPORTSERVICE'].methods_by_name['TestMetricsExportConnection']._serialized_options = b'\x90\x02\x01'
    _globals['_METRICSEXPORTCONFIG']._serialized_start = 121
    _globals['_METRICSEXPORTCONFIG']._serialized_end = 599
    _globals['_CONFIGUREMETRICSEXPORTREQUEST']._serialized_start = 602
    _globals['_CONFIGUREMETRICSEXPORTREQUEST']._serialized_end = 882
    _globals['_CONFIGUREMETRICSEXPORTRESPONSE']._serialized_start = 884
    _globals['_CONFIGUREMETRICSEXPORTRESPONSE']._serialized_end = 995
    _globals['_GETMETRICSEXPORTCONFIGREQUEST']._serialized_start = 997
    _globals['_GETMETRICSEXPORTCONFIGREQUEST']._serialized_end = 1028
    _globals['_GETMETRICSEXPORTCONFIGRESPONSE']._serialized_start = 1030
    _globals['_GETMETRICSEXPORTCONFIGRESPONSE']._serialized_end = 1157
    _globals['_DELETEMETRICSEXPORTCONFIGREQUEST']._serialized_start = 1159
    _globals['_DELETEMETRICSEXPORTCONFIGREQUEST']._serialized_end = 1193
    _globals['_DELETEMETRICSEXPORTCONFIGRESPONSE']._serialized_start = 1195
    _globals['_DELETEMETRICSEXPORTCONFIGRESPONSE']._serialized_end = 1230
    _globals['_TESTMETRICSEXPORTCONNECTIONREQUEST']._serialized_start = 1233
    _globals['_TESTMETRICSEXPORTCONNECTIONREQUEST']._serialized_end = 1384
    _globals['_TESTMETRICSEXPORTCONNECTIONRESPONSE']._serialized_start = 1386
    _globals['_TESTMETRICSEXPORTCONNECTIONRESPONSE']._serialized_end = 1486
    _globals['_TRIGGERMETRICSPUSHREQUEST']._serialized_start = 1488
    _globals['_TRIGGERMETRICSPUSHREQUEST']._serialized_end = 1515
    _globals['_TRIGGERMETRICSPUSHRESPONSE']._serialized_start = 1517
    _globals['_TRIGGERMETRICSPUSHRESPONSE']._serialized_end = 1575
    _globals['_METRICSEXPORTSERVICE']._serialized_start = 1578
    _globals['_METRICSEXPORTSERVICE']._serialized_end = 2418