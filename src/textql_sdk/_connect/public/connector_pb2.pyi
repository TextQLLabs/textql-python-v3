# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import options_pb2 as _options_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ConnectorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONNECTOR_TYPE_UNSPECIFIED: _ClassVar[ConnectorType]
    REDSHIFT: _ClassVar[ConnectorType]
    SNOWFLAKE: _ClassVar[ConnectorType]
    BIGQUERY: _ClassVar[ConnectorType]
    AZURE_SYNAPSE: _ClassVar[ConnectorType]
    AURORA: _ClassVar[ConnectorType]
    TABLEAU: _ClassVar[ConnectorType]
    DATABRICKS: _ClassVar[ConnectorType]
    SUPABASE: _ClassVar[ConnectorType]
    POSTGRES: _ClassVar[ConnectorType]
    MOTHERDUCK: _ClassVar[ConnectorType]
    CLICKHOUSE: _ClassVar[ConnectorType]
    MYSQL: _ClassVar[ConnectorType]
    ATHENA: _ClassVar[ConnectorType]
    GOOGLE_DRIVE: _ClassVar[ConnectorType]
    POWERBI: _ClassVar[ConnectorType]
    SQL_SERVER: _ClassVar[ConnectorType]
    MICROSOFT_365: _ClassVar[ConnectorType]
    SAP_HANA: _ClassVar[ConnectorType]
    ORACLE: _ClassVar[ConnectorType]
    GMAIL: _ClassVar[ConnectorType]
    ANA_INTERNAL: _ClassVar[ConnectorType]
    TRINO: _ClassVar[ConnectorType]
    GOOGLE_CALENDAR: _ClassVar[ConnectorType]
    GOOGLE: _ClassVar[ConnectorType]
    DREMIO: _ClassVar[ConnectorType]
    EXASOL: _ClassVar[ConnectorType]
    FIREBOLT: _ClassVar[ConnectorType]
    KDB: _ClassVar[ConnectorType]
    MONGODB: _ClassVar[ConnectorType]

class FeatureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEATURE_TYPE_UNSPECIFIED: _ClassVar[FeatureType]
    FEATURE_TYPE_REPORT: _ClassVar[FeatureType]
    FEATURE_TYPE_PLAYBOOK: _ClassVar[FeatureType]
    FEATURE_TYPE_DASHBOARD: _ClassVar[FeatureType]
    FEATURE_TYPE_DATA_APP: _ClassVar[FeatureType]
    FEATURE_TYPE_AGENT: _ClassVar[FeatureType]
CONNECTOR_TYPE_UNSPECIFIED: ConnectorType
REDSHIFT: ConnectorType
SNOWFLAKE: ConnectorType
BIGQUERY: ConnectorType
AZURE_SYNAPSE: ConnectorType
AURORA: ConnectorType
TABLEAU: ConnectorType
DATABRICKS: ConnectorType
SUPABASE: ConnectorType
POSTGRES: ConnectorType
MOTHERDUCK: ConnectorType
CLICKHOUSE: ConnectorType
MYSQL: ConnectorType
ATHENA: ConnectorType
GOOGLE_DRIVE: ConnectorType
POWERBI: ConnectorType
SQL_SERVER: ConnectorType
MICROSOFT_365: ConnectorType
SAP_HANA: ConnectorType
ORACLE: ConnectorType
GMAIL: ConnectorType
ANA_INTERNAL: ConnectorType
TRINO: ConnectorType
GOOGLE_CALENDAR: ConnectorType
GOOGLE: ConnectorType
DREMIO: ConnectorType
EXASOL: ConnectorType
FIREBOLT: ConnectorType
KDB: ConnectorType
MONGODB: ConnectorType
FEATURE_TYPE_UNSPECIFIED: FeatureType
FEATURE_TYPE_REPORT: FeatureType
FEATURE_TYPE_PLAYBOOK: FeatureType
FEATURE_TYPE_DASHBOARD: FeatureType
FEATURE_TYPE_DATA_APP: FeatureType
FEATURE_TYPE_AGENT: FeatureType

class ConnectorConfig(_message.Message):
    __slots__ = ('connector_type', 'name', 'redshift', 'snowflake', 'bigquery', 'azure_synapse', 'tableau', 'aurora', 'databricks', 'motherduck', 'clickhouse', 'mysql', 'athena', 'google_drive', 'powerbi', 'postgres', 'supabase', 'sql_server', 'microsoft_365', 'sap_hana', 'oracle', 'gmail', 'trino', 'google_calendar', 'google', 'dremio', 'exasol', 'firebolt', 'kdb', 'mongodb', 'auth_strategy')
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REDSHIFT_FIELD_NUMBER: _ClassVar[int]
    SNOWFLAKE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_FIELD_NUMBER: _ClassVar[int]
    AZURE_SYNAPSE_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_FIELD_NUMBER: _ClassVar[int]
    AURORA_FIELD_NUMBER: _ClassVar[int]
    DATABRICKS_FIELD_NUMBER: _ClassVar[int]
    MOTHERDUCK_FIELD_NUMBER: _ClassVar[int]
    CLICKHOUSE_FIELD_NUMBER: _ClassVar[int]
    MYSQL_FIELD_NUMBER: _ClassVar[int]
    ATHENA_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_FIELD_NUMBER: _ClassVar[int]
    POWERBI_FIELD_NUMBER: _ClassVar[int]
    POSTGRES_FIELD_NUMBER: _ClassVar[int]
    SUPABASE_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT_365_FIELD_NUMBER: _ClassVar[int]
    SAP_HANA_FIELD_NUMBER: _ClassVar[int]
    ORACLE_FIELD_NUMBER: _ClassVar[int]
    GMAIL_FIELD_NUMBER: _ClassVar[int]
    TRINO_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CALENDAR_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_FIELD_NUMBER: _ClassVar[int]
    DREMIO_FIELD_NUMBER: _ClassVar[int]
    EXASOL_FIELD_NUMBER: _ClassVar[int]
    FIREBOLT_FIELD_NUMBER: _ClassVar[int]
    KDB_FIELD_NUMBER: _ClassVar[int]
    MONGODB_FIELD_NUMBER: _ClassVar[int]
    AUTH_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    connector_type: ConnectorType
    name: str
    redshift: RedshiftMetadata
    snowflake: SnowflakeMetadata
    bigquery: BigQueryMetadata
    azure_synapse: AzureSynapseMetadata
    tableau: TableauMetadata
    aurora: AuroraMetadata
    databricks: DatabricksMetadata
    motherduck: MotherduckMetadata
    clickhouse: ClickHouseMetadata
    mysql: MYSQLMetadata
    athena: AthenaMetadata
    google_drive: GoogleDriveMetadata
    powerbi: PowerBIMetadata
    postgres: PostgresMetadata
    supabase: SupabaseMetadata
    sql_server: SQLServerMetadata
    microsoft_365: Microsoft365Metadata
    sap_hana: SAPHanaMetadata
    oracle: OracleMetadata
    gmail: GmailMetadata
    trino: TrinoMetadata
    google_calendar: GoogleCalendarMetadata
    google: GoogleMetadata
    dremio: DremioMetadata
    exasol: ExasolMetadata
    firebolt: FireboltMetadata
    kdb: KdbMetadata
    mongodb: MongoDBMetadata
    auth_strategy: str

    def __init__(self, connector_type: _Optional[_Union[ConnectorType, str]]=..., name: _Optional[str]=..., redshift: _Optional[_Union[RedshiftMetadata, _Mapping]]=..., snowflake: _Optional[_Union[SnowflakeMetadata, _Mapping]]=..., bigquery: _Optional[_Union[BigQueryMetadata, _Mapping]]=..., azure_synapse: _Optional[_Union[AzureSynapseMetadata, _Mapping]]=..., tableau: _Optional[_Union[TableauMetadata, _Mapping]]=..., aurora: _Optional[_Union[AuroraMetadata, _Mapping]]=..., databricks: _Optional[_Union[DatabricksMetadata, _Mapping]]=..., motherduck: _Optional[_Union[MotherduckMetadata, _Mapping]]=..., clickhouse: _Optional[_Union[ClickHouseMetadata, _Mapping]]=..., mysql: _Optional[_Union[MYSQLMetadata, _Mapping]]=..., athena: _Optional[_Union[AthenaMetadata, _Mapping]]=..., google_drive: _Optional[_Union[GoogleDriveMetadata, _Mapping]]=..., powerbi: _Optional[_Union[PowerBIMetadata, _Mapping]]=..., postgres: _Optional[_Union[PostgresMetadata, _Mapping]]=..., supabase: _Optional[_Union[SupabaseMetadata, _Mapping]]=..., sql_server: _Optional[_Union[SQLServerMetadata, _Mapping]]=..., microsoft_365: _Optional[_Union[Microsoft365Metadata, _Mapping]]=..., sap_hana: _Optional[_Union[SAPHanaMetadata, _Mapping]]=..., oracle: _Optional[_Union[OracleMetadata, _Mapping]]=..., gmail: _Optional[_Union[GmailMetadata, _Mapping]]=..., trino: _Optional[_Union[TrinoMetadata, _Mapping]]=..., google_calendar: _Optional[_Union[GoogleCalendarMetadata, _Mapping]]=..., google: _Optional[_Union[GoogleMetadata, _Mapping]]=..., dremio: _Optional[_Union[DremioMetadata, _Mapping]]=..., exasol: _Optional[_Union[ExasolMetadata, _Mapping]]=..., firebolt: _Optional[_Union[FireboltMetadata, _Mapping]]=..., kdb: _Optional[_Union[KdbMetadata, _Mapping]]=..., mongodb: _Optional[_Union[MongoDBMetadata, _Mapping]]=..., auth_strategy: _Optional[str]=...) -> None:
        ...

class RedshiftMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schemas', 'dialect', 'ssl_mode', 'auth_type', 'role_arn', 'region', 'cluster_id', 'group_federation', 'aws_access_key_id', 'aws_secret_access_key')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_FEDERATION_FIELD_NUMBER: _ClassVar[int]
    AWS_ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
    AWS_SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schemas: _containers.RepeatedScalarFieldContainer[str]
    dialect: str
    ssl_mode: bool
    auth_type: str
    role_arn: str
    region: str
    cluster_id: str
    group_federation: bool
    aws_access_key_id: str
    aws_secret_access_key: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schemas: _Optional[_Iterable[str]]=..., dialect: _Optional[str]=..., ssl_mode: bool=..., auth_type: _Optional[str]=..., role_arn: _Optional[str]=..., region: _Optional[str]=..., cluster_id: _Optional[str]=..., group_federation: bool=..., aws_access_key_id: _Optional[str]=..., aws_secret_access_key: _Optional[str]=...) -> None:
        ...

class PostgresMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schemas', 'dialect', 'ssl_mode', 'ssh_tunnel_enabled', 'ssh_host', 'ssh_port', 'ssh_user', 'ssh_private_key', 'ssh_host_public_key', 'secrets_manager_secret_arn', 'secrets_manager_role_arn', 'secrets_manager_external_id')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    SSH_TUNNEL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SSH_HOST_FIELD_NUMBER: _ClassVar[int]
    SSH_PORT_FIELD_NUMBER: _ClassVar[int]
    SSH_USER_FIELD_NUMBER: _ClassVar[int]
    SSH_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SSH_HOST_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRETS_MANAGER_SECRET_ARN_FIELD_NUMBER: _ClassVar[int]
    SECRETS_MANAGER_ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
    SECRETS_MANAGER_EXTERNAL_ID_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schemas: _containers.RepeatedScalarFieldContainer[str]
    dialect: str
    ssl_mode: bool
    ssh_tunnel_enabled: bool
    ssh_host: str
    ssh_port: int
    ssh_user: str
    ssh_private_key: str
    ssh_host_public_key: str
    secrets_manager_secret_arn: str
    secrets_manager_role_arn: str
    secrets_manager_external_id: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schemas: _Optional[_Iterable[str]]=..., dialect: _Optional[str]=..., ssl_mode: bool=..., ssh_tunnel_enabled: bool=..., ssh_host: _Optional[str]=..., ssh_port: _Optional[int]=..., ssh_user: _Optional[str]=..., ssh_private_key: _Optional[str]=..., ssh_host_public_key: _Optional[str]=..., secrets_manager_secret_arn: _Optional[str]=..., secrets_manager_role_arn: _Optional[str]=..., secrets_manager_external_id: _Optional[str]=...) -> None:
        ...

class KdbMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'tls', 'ssh_tunnel_enabled', 'ssh_host', 'ssh_port', 'ssh_user', 'ssh_private_key', 'ssh_host_public_key')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    SSH_TUNNEL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SSH_HOST_FIELD_NUMBER: _ClassVar[int]
    SSH_PORT_FIELD_NUMBER: _ClassVar[int]
    SSH_USER_FIELD_NUMBER: _ClassVar[int]
    SSH_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SSH_HOST_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    tls: bool
    ssh_tunnel_enabled: bool
    ssh_host: str
    ssh_port: int
    ssh_user: str
    ssh_private_key: str
    ssh_host_public_key: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., tls: bool=..., ssh_tunnel_enabled: bool=..., ssh_host: _Optional[str]=..., ssh_port: _Optional[int]=..., ssh_user: _Optional[str]=..., ssh_private_key: _Optional[str]=..., ssh_host_public_key: _Optional[str]=...) -> None:
        ...

class MongoDBMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'auth_source', 'tls', 'srv')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    AUTH_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TLS_FIELD_NUMBER: _ClassVar[int]
    SRV_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    auth_source: str
    tls: bool
    srv: bool

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., auth_source: _Optional[str]=..., tls: bool=..., srv: bool=...) -> None:
        ...

class SupabaseMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schemas', 'dialect', 'ssl_mode')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schemas: _containers.RepeatedScalarFieldContainer[str]
    dialect: str
    ssl_mode: bool

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schemas: _Optional[_Iterable[str]]=..., dialect: _Optional[str]=..., ssl_mode: bool=...) -> None:
        ...

class SnowflakeMetadata(_message.Message):
    __slots__ = ('username', 'password', 'private_key', 'private_key_passphrase', 'role', 'schema', 'locator', 'database', 'warehouse', 'oauth_access_token', 'oauth_refresh_token', 'oauth_client_id', 'oauth_client_secret', 'enable_sso_auth', 'token_exchange_endpoint', 'token_exchange_audience', 'token_exchange_scope')
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_PASSPHRASE_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    LOCATOR_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    WAREHOUSE_FIELD_NUMBER: _ClassVar[int]
    OAUTH_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OAUTH_REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    OAUTH_CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    ENABLE_SSO_AUTH_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXCHANGE_ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXCHANGE_AUDIENCE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXCHANGE_SCOPE_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    private_key: str
    private_key_passphrase: str
    role: str
    schema: str
    locator: str
    database: str
    warehouse: str
    oauth_access_token: str
    oauth_refresh_token: str
    oauth_client_id: str
    oauth_client_secret: str
    enable_sso_auth: bool
    token_exchange_endpoint: str
    token_exchange_audience: str
    token_exchange_scope: str

    def __init__(self, username: _Optional[str]=..., password: _Optional[str]=..., private_key: _Optional[str]=..., private_key_passphrase: _Optional[str]=..., role: _Optional[str]=..., schema: _Optional[str]=..., locator: _Optional[str]=..., database: _Optional[str]=..., warehouse: _Optional[str]=..., oauth_access_token: _Optional[str]=..., oauth_refresh_token: _Optional[str]=..., oauth_client_id: _Optional[str]=..., oauth_client_secret: _Optional[str]=..., enable_sso_auth: bool=..., token_exchange_endpoint: _Optional[str]=..., token_exchange_audience: _Optional[str]=..., token_exchange_scope: _Optional[str]=...) -> None:
        ...

class BigQueryMetadata(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'service_account_key', 'region_qualifier')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_KEY_FIELD_NUMBER: _ClassVar[int]
    REGION_QUALIFIER_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    service_account_key: str
    region_qualifier: str

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., service_account_key: _Optional[str]=..., region_qualifier: _Optional[str]=...) -> None:
        ...

class AzureSynapseMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schema', 'auth_type', 'client_id', 'client_secret', 'tenant_id')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schema: str
    auth_type: str
    client_id: str
    client_secret: str
    tenant_id: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schema: _Optional[str]=..., auth_type: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., tenant_id: _Optional[str]=...) -> None:
        ...

class AuroraMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schema', 'dialect', 'ssl_mode', 'aurora_auth')

    class AuroraAuth(_message.Message):
        __slots__ = ('iam_auth', 'cluster_id', 'region')
        IAM_AUTH_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_ID_FIELD_NUMBER: _ClassVar[int]
        REGION_FIELD_NUMBER: _ClassVar[int]
        iam_auth: bool
        cluster_id: str
        region: str

        def __init__(self, iam_auth: bool=..., cluster_id: _Optional[str]=..., region: _Optional[str]=...) -> None:
            ...
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    AURORA_AUTH_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schema: str
    dialect: str
    ssl_mode: bool
    aurora_auth: AuroraMetadata.AuroraAuth

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schema: _Optional[str]=..., dialect: _Optional[str]=..., ssl_mode: bool=..., aurora_auth: _Optional[_Union[AuroraMetadata.AuroraAuth, _Mapping]]=...) -> None:
        ...

class MYSQLMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schema', 'ssl_mode')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schema: str
    ssl_mode: bool

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schema: _Optional[str]=..., ssl_mode: bool=...) -> None:
        ...

class SQLServerMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schema', 'ssl_mode', 'auth_type', 'krb5_realm', 'krb5_config', 'krb5_keytab', 'krb5_spn', 'client_cert', 'client_key', 'tenant_id', 'client_id', 'client_secret')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    KRB5_REALM_FIELD_NUMBER: _ClassVar[int]
    KRB5_CONFIG_FIELD_NUMBER: _ClassVar[int]
    KRB5_KEYTAB_FIELD_NUMBER: _ClassVar[int]
    KRB5_SPN_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CERT_FIELD_NUMBER: _ClassVar[int]
    CLIENT_KEY_FIELD_NUMBER: _ClassVar[int]
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schema: str
    ssl_mode: bool
    auth_type: str
    krb5_realm: str
    krb5_config: str
    krb5_keytab: str
    krb5_spn: str
    client_cert: str
    client_key: str
    tenant_id: str
    client_id: str
    client_secret: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schema: _Optional[str]=..., ssl_mode: bool=..., auth_type: _Optional[str]=..., krb5_realm: _Optional[str]=..., krb5_config: _Optional[str]=..., krb5_keytab: _Optional[str]=..., krb5_spn: _Optional[str]=..., client_cert: _Optional[str]=..., client_key: _Optional[str]=..., tenant_id: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=...) -> None:
        ...

class TableauMetadata(_message.Message):
    __slots__ = ('server_url', 'site_name', 'pat_name', 'pat_secret', 'connected_app_client_id', 'connected_app_secret_id', 'connected_app_secret_value')
    SERVER_URL_FIELD_NUMBER: _ClassVar[int]
    SITE_NAME_FIELD_NUMBER: _ClassVar[int]
    PAT_NAME_FIELD_NUMBER: _ClassVar[int]
    PAT_SECRET_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_APP_CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_APP_SECRET_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_APP_SECRET_VALUE_FIELD_NUMBER: _ClassVar[int]
    server_url: str
    site_name: str
    pat_name: str
    pat_secret: str
    connected_app_client_id: str
    connected_app_secret_id: str
    connected_app_secret_value: str

    def __init__(self, server_url: _Optional[str]=..., site_name: _Optional[str]=..., pat_name: _Optional[str]=..., pat_secret: _Optional[str]=..., connected_app_client_id: _Optional[str]=..., connected_app_secret_id: _Optional[str]=..., connected_app_secret_value: _Optional[str]=...) -> None:
        ...

class PowerBIMetadata(_message.Message):
    __slots__ = ('tenant_id', 'client_id', 'client_secret', 'object_id', 'roles')
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    client_id: str
    client_secret: str
    object_id: str
    roles: str

    def __init__(self, tenant_id: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., object_id: _Optional[str]=..., roles: _Optional[str]=...) -> None:
        ...

class DatabricksMetadata(_message.Message):
    __slots__ = ('host', 'http_path', 'port', 'databricks_auth', 'catalog', 'schema', 'enable_token_exchange')

    class DatabricksAuth(_message.Message):
        __slots__ = ('pat', 'client_credentials', 'oauth_u2m')

        class PersonalAccessToken(_message.Message):
            __slots__ = ('token',)
            TOKEN_FIELD_NUMBER: _ClassVar[int]
            token: str

            def __init__(self, token: _Optional[str]=...) -> None:
                ...

        class ClientCredentials(_message.Message):
            __slots__ = ('client_id', 'client_secret')
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
            client_id: str
            client_secret: str

            def __init__(self, client_id: _Optional[str]=..., client_secret: _Optional[str]=...) -> None:
                ...

        class OAuthU2M(_message.Message):
            __slots__ = ('client_id', 'client_secret')
            CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
            CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
            client_id: str
            client_secret: str

            def __init__(self, client_id: _Optional[str]=..., client_secret: _Optional[str]=...) -> None:
                ...
        PAT_FIELD_NUMBER: _ClassVar[int]
        CLIENT_CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
        OAUTH_U2M_FIELD_NUMBER: _ClassVar[int]
        pat: DatabricksMetadata.DatabricksAuth.PersonalAccessToken
        client_credentials: DatabricksMetadata.DatabricksAuth.ClientCredentials
        oauth_u2m: DatabricksMetadata.DatabricksAuth.OAuthU2M

        def __init__(self, pat: _Optional[_Union[DatabricksMetadata.DatabricksAuth.PersonalAccessToken, _Mapping]]=..., client_credentials: _Optional[_Union[DatabricksMetadata.DatabricksAuth.ClientCredentials, _Mapping]]=..., oauth_u2m: _Optional[_Union[DatabricksMetadata.DatabricksAuth.OAuthU2M, _Mapping]]=...) -> None:
            ...
    HOST_FIELD_NUMBER: _ClassVar[int]
    HTTP_PATH_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    DATABRICKS_AUTH_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_TOKEN_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    host: str
    http_path: str
    port: int
    databricks_auth: DatabricksMetadata.DatabricksAuth
    catalog: str
    schema: str
    enable_token_exchange: bool

    def __init__(self, host: _Optional[str]=..., http_path: _Optional[str]=..., port: _Optional[int]=..., databricks_auth: _Optional[_Union[DatabricksMetadata.DatabricksAuth, _Mapping]]=..., catalog: _Optional[str]=..., schema: _Optional[str]=..., enable_token_exchange: bool=...) -> None:
        ...

class MotherduckMetadata(_message.Message):
    __slots__ = ('token',)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str

    def __init__(self, token: _Optional[str]=...) -> None:
        ...

class ClickHouseMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'use_ssl', 'protocol')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    USE_SSL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    use_ssl: bool
    protocol: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., use_ssl: bool=..., protocol: _Optional[str]=...) -> None:
        ...

class AthenaMetadata(_message.Message):
    __slots__ = ('region', 'database', 'workgroup', 's3_output_location', 'athena_auth', 'catalog')

    class AthenaAuth(_message.Message):
        __slots__ = ('access_key', 'iam_role')

        class AccessKeyCredentials(_message.Message):
            __slots__ = ('access_key_id', 'secret_access_key')
            ACCESS_KEY_ID_FIELD_NUMBER: _ClassVar[int]
            SECRET_ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
            access_key_id: str
            secret_access_key: str

            def __init__(self, access_key_id: _Optional[str]=..., secret_access_key: _Optional[str]=...) -> None:
                ...

        class IAMRoleCredentials(_message.Message):
            __slots__ = ('role_arn', 'session_name')
            ROLE_ARN_FIELD_NUMBER: _ClassVar[int]
            SESSION_NAME_FIELD_NUMBER: _ClassVar[int]
            role_arn: str
            session_name: str

            def __init__(self, role_arn: _Optional[str]=..., session_name: _Optional[str]=...) -> None:
                ...
        ACCESS_KEY_FIELD_NUMBER: _ClassVar[int]
        IAM_ROLE_FIELD_NUMBER: _ClassVar[int]
        access_key: AthenaMetadata.AthenaAuth.AccessKeyCredentials
        iam_role: AthenaMetadata.AthenaAuth.IAMRoleCredentials

        def __init__(self, access_key: _Optional[_Union[AthenaMetadata.AthenaAuth.AccessKeyCredentials, _Mapping]]=..., iam_role: _Optional[_Union[AthenaMetadata.AthenaAuth.IAMRoleCredentials, _Mapping]]=...) -> None:
            ...
    REGION_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    WORKGROUP_FIELD_NUMBER: _ClassVar[int]
    S3_OUTPUT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ATHENA_AUTH_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    region: str
    database: str
    workgroup: str
    s3_output_location: str
    athena_auth: AthenaMetadata.AthenaAuth
    catalog: str

    def __init__(self, region: _Optional[str]=..., database: _Optional[str]=..., workgroup: _Optional[str]=..., s3_output_location: _Optional[str]=..., athena_auth: _Optional[_Union[AthenaMetadata.AthenaAuth, _Mapping]]=..., catalog: _Optional[str]=...) -> None:
        ...

class GoogleDriveMetadata(_message.Message):
    __slots__ = ('access_token', 'refresh_token', 'member_id')
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    member_id: str

    def __init__(self, access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., member_id: _Optional[str]=...) -> None:
        ...

class GmailMetadata(_message.Message):
    __slots__ = ('access_token', 'refresh_token', 'member_id', 'metadata_only')
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    member_id: str
    metadata_only: bool

    def __init__(self, access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., member_id: _Optional[str]=..., metadata_only: bool=...) -> None:
        ...

class GoogleCalendarMetadata(_message.Message):
    __slots__ = ('access_token', 'refresh_token', 'member_id', 'metadata_only')
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    member_id: str
    metadata_only: bool

    def __init__(self, access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., member_id: _Optional[str]=..., metadata_only: bool=...) -> None:
        ...

class GoogleMetadata(_message.Message):
    __slots__ = ('access_token', 'refresh_token', 'member_id', 'gmail_enabled', 'calendar_enabled', 'metadata_only', 'drive_enabled', 'token_expiry')
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    GMAIL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CALENDAR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    DRIVE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    refresh_token: str
    member_id: str
    gmail_enabled: bool
    calendar_enabled: bool
    metadata_only: bool
    drive_enabled: bool
    token_expiry: str

    def __init__(self, access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., member_id: _Optional[str]=..., gmail_enabled: bool=..., calendar_enabled: bool=..., metadata_only: bool=..., drive_enabled: bool=..., token_expiry: _Optional[str]=...) -> None:
        ...

class Microsoft365Metadata(_message.Message):
    __slots__ = ('tenant_id', 'client_id', 'client_secret', 'access_token', 'refresh_token', 'member_id', 'token_expiry', 'metadata_only', 'scopes')
    TENANT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TOKEN_EXPIRY_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    tenant_id: str
    client_id: str
    client_secret: str
    access_token: str
    refresh_token: str
    member_id: str
    token_expiry: str
    metadata_only: bool
    scopes: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, tenant_id: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., access_token: _Optional[str]=..., refresh_token: _Optional[str]=..., member_id: _Optional[str]=..., token_expiry: _Optional[str]=..., metadata_only: bool=..., scopes: _Optional[_Iterable[str]]=...) -> None:
        ...

class SAPHanaMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schemas', 'dialect', 'ssl_mode', 'sap_hana_cloud')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    SAP_HANA_CLOUD_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schemas: _containers.RepeatedScalarFieldContainer[str]
    dialect: str
    ssl_mode: bool
    sap_hana_cloud: bool

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schemas: _Optional[_Iterable[str]]=..., dialect: _Optional[str]=..., ssl_mode: bool=..., sap_hana_cloud: bool=...) -> None:
        ...

class OracleMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'service_name', 'dialect', 'ssl_mode', 'connection_type', 'sid', 'connect_string', 'wallet_zip', 'wallet_password', 'tns_alias')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    DIALECT_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SID_FIELD_NUMBER: _ClassVar[int]
    CONNECT_STRING_FIELD_NUMBER: _ClassVar[int]
    WALLET_ZIP_FIELD_NUMBER: _ClassVar[int]
    WALLET_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TNS_ALIAS_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    service_name: str
    dialect: str
    ssl_mode: bool
    connection_type: str
    sid: str
    connect_string: str
    wallet_zip: str
    wallet_password: str
    tns_alias: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., service_name: _Optional[str]=..., dialect: _Optional[str]=..., ssl_mode: bool=..., connection_type: _Optional[str]=..., sid: _Optional[str]=..., connect_string: _Optional[str]=..., wallet_zip: _Optional[str]=..., wallet_password: _Optional[str]=..., tns_alias: _Optional[str]=...) -> None:
        ...

class TrinoMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'catalog', 'schema', 'ssl_mode', 'access_token', 'skip_tls_verify')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SKIP_TLS_VERIFY_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    catalog: str
    schema: str
    ssl_mode: bool
    access_token: str
    skip_tls_verify: bool

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., catalog: _Optional[str]=..., schema: _Optional[str]=..., ssl_mode: bool=..., access_token: _Optional[str]=..., skip_tls_verify: bool=...) -> None:
        ...

class DremioMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'token', 'project_id', 'spaces', 'ssl_mode')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    token: str
    project_id: str
    spaces: _containers.RepeatedScalarFieldContainer[str]
    ssl_mode: bool

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., token: _Optional[str]=..., project_id: _Optional[str]=..., spaces: _Optional[_Iterable[str]]=..., ssl_mode: bool=...) -> None:
        ...

class ExasolMetadata(_message.Message):
    __slots__ = ('host', 'port', 'user', 'password', 'database', 'schemas', 'ssl_mode', 'access_token')
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    SSL_MODE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    host: str
    port: int
    user: str
    password: str
    database: str
    schemas: _containers.RepeatedScalarFieldContainer[str]
    ssl_mode: bool
    access_token: str

    def __init__(self, host: _Optional[str]=..., port: _Optional[int]=..., user: _Optional[str]=..., password: _Optional[str]=..., database: _Optional[str]=..., schemas: _Optional[_Iterable[str]]=..., ssl_mode: bool=..., access_token: _Optional[str]=...) -> None:
        ...

class FireboltMetadata(_message.Message):
    __slots__ = ('account_name', 'database', 'engine_name', 'client_id', 'client_secret', 'schemas')
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    ENGINE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
    SCHEMAS_FIELD_NUMBER: _ClassVar[int]
    account_name: str
    database: str
    engine_name: str
    client_id: str
    client_secret: str
    schemas: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, account_name: _Optional[str]=..., database: _Optional[str]=..., engine_name: _Optional[str]=..., client_id: _Optional[str]=..., client_secret: _Optional[str]=..., schemas: _Optional[_Iterable[str]]=...) -> None:
        ...

class Connector(_message.Message):
    __slots__ = ('id', 'name', 'connector_type', 'member_id', 'created_at', 'redshift_metadata', 'snowflake_metadata', 'bigquery_metadata', 'azure_synapse_metadata', 'tableau_metadata', 'aurora_metadata', 'databricks_metadata', 'motherduck_metadata', 'clickhouse_metadata', 'mysql_metadata', 'athena_metadata', 'google_drive_metadata', 'powerbi_metadata', 'postgres_metadata', 'supabase_metadata', 'sql_server_metadata', 'microsoft_365_metadata', 'sap_hana_metadata', 'oracle_metadata', 'gmail_metadata', 'trino_metadata', 'google_calendar_metadata', 'google_metadata', 'dremio_metadata', 'exasol_metadata', 'firebolt_metadata', 'kdb_metadata', 'mongodb_metadata', 'is_example', 'allow_sql_write_operations', 'auth_strategy', 'authenticated_by_member_id', 'member_authenticated', 'member_auth_username', 'include_db_session_metadata', 'is_public')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REDSHIFT_METADATA_FIELD_NUMBER: _ClassVar[int]
    SNOWFLAKE_METADATA_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_METADATA_FIELD_NUMBER: _ClassVar[int]
    AZURE_SYNAPSE_METADATA_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_METADATA_FIELD_NUMBER: _ClassVar[int]
    AURORA_METADATA_FIELD_NUMBER: _ClassVar[int]
    DATABRICKS_METADATA_FIELD_NUMBER: _ClassVar[int]
    MOTHERDUCK_METADATA_FIELD_NUMBER: _ClassVar[int]
    CLICKHOUSE_METADATA_FIELD_NUMBER: _ClassVar[int]
    MYSQL_METADATA_FIELD_NUMBER: _ClassVar[int]
    ATHENA_METADATA_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_DRIVE_METADATA_FIELD_NUMBER: _ClassVar[int]
    POWERBI_METADATA_FIELD_NUMBER: _ClassVar[int]
    POSTGRES_METADATA_FIELD_NUMBER: _ClassVar[int]
    SUPABASE_METADATA_FIELD_NUMBER: _ClassVar[int]
    SQL_SERVER_METADATA_FIELD_NUMBER: _ClassVar[int]
    MICROSOFT_365_METADATA_FIELD_NUMBER: _ClassVar[int]
    SAP_HANA_METADATA_FIELD_NUMBER: _ClassVar[int]
    ORACLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    GMAIL_METADATA_FIELD_NUMBER: _ClassVar[int]
    TRINO_METADATA_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_CALENDAR_METADATA_FIELD_NUMBER: _ClassVar[int]
    GOOGLE_METADATA_FIELD_NUMBER: _ClassVar[int]
    DREMIO_METADATA_FIELD_NUMBER: _ClassVar[int]
    EXASOL_METADATA_FIELD_NUMBER: _ClassVar[int]
    FIREBOLT_METADATA_FIELD_NUMBER: _ClassVar[int]
    KDB_METADATA_FIELD_NUMBER: _ClassVar[int]
    MONGODB_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SQL_WRITE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    AUTH_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    AUTHENTICATED_BY_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AUTHENTICATED_FIELD_NUMBER: _ClassVar[int]
    MEMBER_AUTH_USERNAME_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DB_SESSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    connector_type: ConnectorType
    member_id: str
    created_at: _timestamp_pb2.Timestamp
    redshift_metadata: RedshiftMetadata
    snowflake_metadata: SnowflakeMetadata
    bigquery_metadata: BigQueryMetadata
    azure_synapse_metadata: AzureSynapseMetadata
    tableau_metadata: TableauMetadata
    aurora_metadata: AuroraMetadata
    databricks_metadata: DatabricksMetadata
    motherduck_metadata: MotherduckMetadata
    clickhouse_metadata: ClickHouseMetadata
    mysql_metadata: MYSQLMetadata
    athena_metadata: AthenaMetadata
    google_drive_metadata: GoogleDriveMetadata
    powerbi_metadata: PowerBIMetadata
    postgres_metadata: PostgresMetadata
    supabase_metadata: SupabaseMetadata
    sql_server_metadata: SQLServerMetadata
    microsoft_365_metadata: Microsoft365Metadata
    sap_hana_metadata: SAPHanaMetadata
    oracle_metadata: OracleMetadata
    gmail_metadata: GmailMetadata
    trino_metadata: TrinoMetadata
    google_calendar_metadata: GoogleCalendarMetadata
    google_metadata: GoogleMetadata
    dremio_metadata: DremioMetadata
    exasol_metadata: ExasolMetadata
    firebolt_metadata: FireboltMetadata
    kdb_metadata: KdbMetadata
    mongodb_metadata: MongoDBMetadata
    is_example: bool
    allow_sql_write_operations: bool
    auth_strategy: str
    authenticated_by_member_id: str
    member_authenticated: bool
    member_auth_username: str
    include_db_session_metadata: bool
    is_public: bool

    def __init__(self, id: _Optional[int]=..., name: _Optional[str]=..., connector_type: _Optional[_Union[ConnectorType, str]]=..., member_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., redshift_metadata: _Optional[_Union[RedshiftMetadata, _Mapping]]=..., snowflake_metadata: _Optional[_Union[SnowflakeMetadata, _Mapping]]=..., bigquery_metadata: _Optional[_Union[BigQueryMetadata, _Mapping]]=..., azure_synapse_metadata: _Optional[_Union[AzureSynapseMetadata, _Mapping]]=..., tableau_metadata: _Optional[_Union[TableauMetadata, _Mapping]]=..., aurora_metadata: _Optional[_Union[AuroraMetadata, _Mapping]]=..., databricks_metadata: _Optional[_Union[DatabricksMetadata, _Mapping]]=..., motherduck_metadata: _Optional[_Union[MotherduckMetadata, _Mapping]]=..., clickhouse_metadata: _Optional[_Union[ClickHouseMetadata, _Mapping]]=..., mysql_metadata: _Optional[_Union[MYSQLMetadata, _Mapping]]=..., athena_metadata: _Optional[_Union[AthenaMetadata, _Mapping]]=..., google_drive_metadata: _Optional[_Union[GoogleDriveMetadata, _Mapping]]=..., powerbi_metadata: _Optional[_Union[PowerBIMetadata, _Mapping]]=..., postgres_metadata: _Optional[_Union[PostgresMetadata, _Mapping]]=..., supabase_metadata: _Optional[_Union[SupabaseMetadata, _Mapping]]=..., sql_server_metadata: _Optional[_Union[SQLServerMetadata, _Mapping]]=..., microsoft_365_metadata: _Optional[_Union[Microsoft365Metadata, _Mapping]]=..., sap_hana_metadata: _Optional[_Union[SAPHanaMetadata, _Mapping]]=..., oracle_metadata: _Optional[_Union[OracleMetadata, _Mapping]]=..., gmail_metadata: _Optional[_Union[GmailMetadata, _Mapping]]=..., trino_metadata: _Optional[_Union[TrinoMetadata, _Mapping]]=..., google_calendar_metadata: _Optional[_Union[GoogleCalendarMetadata, _Mapping]]=..., google_metadata: _Optional[_Union[GoogleMetadata, _Mapping]]=..., dremio_metadata: _Optional[_Union[DremioMetadata, _Mapping]]=..., exasol_metadata: _Optional[_Union[ExasolMetadata, _Mapping]]=..., firebolt_metadata: _Optional[_Union[FireboltMetadata, _Mapping]]=..., kdb_metadata: _Optional[_Union[KdbMetadata, _Mapping]]=..., mongodb_metadata: _Optional[_Union[MongoDBMetadata, _Mapping]]=..., is_example: bool=..., allow_sql_write_operations: bool=..., auth_strategy: _Optional[str]=..., authenticated_by_member_id: _Optional[str]=..., member_authenticated: bool=..., member_auth_username: _Optional[str]=..., include_db_session_metadata: bool=..., is_public: bool=...) -> None:
        ...

class ConnectorAccessGrant(_message.Message):
    __slots__ = ('member_id', 'role_id', 'group_id', 'access_type')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    role_id: str
    group_id: str
    access_type: str

    def __init__(self, member_id: _Optional[str]=..., role_id: _Optional[str]=..., group_id: _Optional[str]=..., access_type: _Optional[str]=...) -> None:
        ...

class ConnectorAccessConfig(_message.Message):
    __slots__ = ('is_public', 'grants')
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    GRANTS_FIELD_NUMBER: _ClassVar[int]
    is_public: bool
    grants: _containers.RepeatedCompositeFieldContainer[ConnectorAccessGrant]

    def __init__(self, is_public: bool=..., grants: _Optional[_Iterable[_Union[ConnectorAccessGrant, _Mapping]]]=...) -> None:
        ...

class CreateConnectorRequest(_message.Message):
    __slots__ = ('config', 'allow_sql_write_operations', 'include_db_session_metadata', 'access')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SQL_WRITE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DB_SESSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    config: ConnectorConfig
    allow_sql_write_operations: bool
    include_db_session_metadata: bool
    access: ConnectorAccessConfig

    def __init__(self, config: _Optional[_Union[ConnectorConfig, _Mapping]]=..., allow_sql_write_operations: bool=..., include_db_session_metadata: bool=..., access: _Optional[_Union[ConnectorAccessConfig, _Mapping]]=...) -> None:
        ...

class CreateConnectorResponse(_message.Message):
    __slots__ = ('connector_id', 'name', 'connector_type')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_TYPE_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    name: str
    connector_type: ConnectorType

    def __init__(self, connector_id: _Optional[int]=..., name: _Optional[str]=..., connector_type: _Optional[_Union[ConnectorType, str]]=...) -> None:
        ...

class UpdateConnectorRequest(_message.Message):
    __slots__ = ('connector_id', 'config', 'allow_sql_write_operations', 'include_db_session_metadata')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    ALLOW_SQL_WRITE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DB_SESSION_METADATA_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    config: ConnectorConfig
    allow_sql_write_operations: bool
    include_db_session_metadata: bool

    def __init__(self, connector_id: _Optional[int]=..., config: _Optional[_Union[ConnectorConfig, _Mapping]]=..., allow_sql_write_operations: bool=..., include_db_session_metadata: bool=...) -> None:
        ...

class UpdateConnectorResponse(_message.Message):
    __slots__ = ('connector',)
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    connector: Connector

    def __init__(self, connector: _Optional[_Union[Connector, _Mapping]]=...) -> None:
        ...

class GetConnectorRequest(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class GetConnectorResponse(_message.Message):
    __slots__ = ('connector',)
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    connector: Connector

    def __init__(self, connector: _Optional[_Union[Connector, _Mapping]]=...) -> None:
        ...

class GetConnectorsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetConnectorsResponse(_message.Message):
    __slots__ = ('connectors',)
    CONNECTORS_FIELD_NUMBER: _ClassVar[int]
    connectors: _containers.RepeatedCompositeFieldContainer[Connector]

    def __init__(self, connectors: _Optional[_Iterable[_Union[Connector, _Mapping]]]=...) -> None:
        ...

class DeleteConnectorRequest(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class DeleteConnectorResponse(_message.Message):
    __slots__ = ('success',)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool

    def __init__(self, success: bool=...) -> None:
        ...

class TestConnectorRequest(_message.Message):
    __slots__ = ('config', 'connector_id')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    config: ConnectorConfig
    connector_id: str

    def __init__(self, config: _Optional[_Union[ConnectorConfig, _Mapping]]=..., connector_id: _Optional[str]=...) -> None:
        ...

class TestConnectorResponse(_message.Message):
    __slots__ = ('success', 'error')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    error: str

    def __init__(self, success: bool=..., error: _Optional[str]=...) -> None:
        ...

class DuplicateConnectorRequest(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class DuplicateConnectorResponse(_message.Message):
    __slots__ = ('connector',)
    CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    connector: Connector

    def __init__(self, connector: _Optional[_Union[Connector, _Mapping]]=...) -> None:
        ...

class QueryResult(_message.Message):
    __slots__ = ('arrow_data', 'total_rows')
    ARROW_DATA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ROWS_FIELD_NUMBER: _ClassVar[int]
    arrow_data: bytes
    total_rows: int

    def __init__(self, arrow_data: _Optional[bytes]=..., total_rows: _Optional[int]=...) -> None:
        ...

class PrimaryKeyMetadata(_message.Message):
    __slots__ = ('columns', 'descriptions')
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    columns: _containers.RepeatedScalarFieldContainer[str]
    descriptions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, columns: _Optional[_Iterable[str]]=..., descriptions: _Optional[_Iterable[str]]=...) -> None:
        ...

class ConnectorTable(_message.Message):
    __slots__ = ('table_database', 'table_schema', 'table_name', 'preview', 'primary_keys', 'table_type')
    TABLE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_KEYS_FIELD_NUMBER: _ClassVar[int]
    TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
    table_database: str
    table_schema: str
    table_name: str
    preview: QueryResult
    primary_keys: _containers.RepeatedCompositeFieldContainer[PrimaryKeyMetadata]
    table_type: str

    def __init__(self, table_database: _Optional[str]=..., table_schema: _Optional[str]=..., table_name: _Optional[str]=..., preview: _Optional[_Union[QueryResult, _Mapping]]=..., primary_keys: _Optional[_Iterable[_Union[PrimaryKeyMetadata, _Mapping]]]=..., table_type: _Optional[str]=...) -> None:
        ...

class ListConnectorTablesRequest(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class ListConnectorTablesResponse(_message.Message):
    __slots__ = ('tables', 'error')
    TABLES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedCompositeFieldContainer[ConnectorTable]
    error: str

    def __init__(self, tables: _Optional[_Iterable[_Union[ConnectorTable, _Mapping]]]=..., error: _Optional[str]=...) -> None:
        ...

class RetryTableRequest(_message.Message):
    __slots__ = ('connector_id', 'table_database', 'table_schema', 'table_name')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    table_database: str
    table_schema: str
    table_name: str

    def __init__(self, connector_id: _Optional[int]=..., table_database: _Optional[str]=..., table_schema: _Optional[str]=..., table_name: _Optional[str]=...) -> None:
        ...

class GetTablePreviewRequest(_message.Message):
    __slots__ = ('connector_id', 'table_database', 'table_schema', 'table_name', 'limit')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_DATABASE_FIELD_NUMBER: _ClassVar[int]
    TABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    TABLE_NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    table_database: str
    table_schema: str
    table_name: str
    limit: int

    def __init__(self, connector_id: _Optional[int]=..., table_database: _Optional[str]=..., table_schema: _Optional[str]=..., table_name: _Optional[str]=..., limit: _Optional[int]=...) -> None:
        ...

class GetTablePreviewResponse(_message.Message):
    __slots__ = ('arrow_data', 'success', 'error_message')
    ARROW_DATA_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    arrow_data: bytes
    success: bool
    error_message: str

    def __init__(self, arrow_data: _Optional[bytes]=..., success: bool=..., error_message: _Optional[str]=...) -> None:
        ...

class ExecuteQueryRequest(_message.Message):
    __slots__ = ('connector_id', 'query', 'limit')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    query: str
    limit: int

    def __init__(self, connector_id: _Optional[int]=..., query: _Optional[str]=..., limit: _Optional[int]=...) -> None:
        ...

class ExecuteQueryResponse(_message.Message):
    __slots__ = ('arrow_data', 'success', 'error_message')
    ARROW_DATA_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    arrow_data: bytes
    success: bool
    error_message: str

    def __init__(self, arrow_data: _Optional[bytes]=..., success: bool=..., error_message: _Optional[str]=...) -> None:
        ...

class GetExampleQueriesRequest(_message.Message):
    __slots__ = ('connector_contexts', 'feature_filter')
    CONNECTOR_CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    FEATURE_FILTER_FIELD_NUMBER: _ClassVar[int]
    connector_contexts: _containers.RepeatedCompositeFieldContainer[ConnectorContext]
    feature_filter: FeatureType

    def __init__(self, connector_contexts: _Optional[_Iterable[_Union[ConnectorContext, _Mapping]]]=..., feature_filter: _Optional[_Union[FeatureType, str]]=...) -> None:
        ...

class ConnectorContext(_message.Message):
    __slots__ = ('connector_id', 'tableau', 'powerbi')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    TABLEAU_FIELD_NUMBER: _ClassVar[int]
    POWERBI_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    tableau: TableauConnectorContext
    powerbi: PowerBIConnectorContext

    def __init__(self, connector_id: _Optional[int]=..., tableau: _Optional[_Union[TableauConnectorContext, _Mapping]]=..., powerbi: _Optional[_Union[PowerBIConnectorContext, _Mapping]]=...) -> None:
        ...

class TableauConnectorContext(_message.Message):
    __slots__ = ('collection_ids',)
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    collection_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, collection_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class PowerBIConnectorContext(_message.Message):
    __slots__ = ('report_ids', 'dataset_ids', 'collection_ids')
    REPORT_IDS_FIELD_NUMBER: _ClassVar[int]
    DATASET_IDS_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_IDS_FIELD_NUMBER: _ClassVar[int]
    report_ids: _containers.RepeatedScalarFieldContainer[str]
    dataset_ids: _containers.RepeatedScalarFieldContainer[str]
    collection_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, report_ids: _Optional[_Iterable[str]]=..., dataset_ids: _Optional[_Iterable[str]]=..., collection_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class MessageSegment(_message.Message):
    __slots__ = ('content', 'feature_type')
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    content: str
    feature_type: FeatureType

    def __init__(self, content: _Optional[str]=..., feature_type: _Optional[_Union[FeatureType, str]]=...) -> None:
        ...

class ExampleQuery(_message.Message):
    __slots__ = ('id', 'label', 'message', 'is_multi_source', 'required_connector_ids', 'category', 'segments', 'required_features', 'source_context')
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    IS_MULTI_SOURCE_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    message: str
    is_multi_source: bool
    required_connector_ids: _containers.RepeatedScalarFieldContainer[int]
    category: str
    segments: _containers.RepeatedCompositeFieldContainer[MessageSegment]
    required_features: _containers.RepeatedScalarFieldContainer[FeatureType]
    source_context: ConnectorContext

    def __init__(self, id: _Optional[str]=..., label: _Optional[str]=..., message: _Optional[str]=..., is_multi_source: bool=..., required_connector_ids: _Optional[_Iterable[int]]=..., category: _Optional[str]=..., segments: _Optional[_Iterable[_Union[MessageSegment, _Mapping]]]=..., required_features: _Optional[_Iterable[_Union[FeatureType, str]]]=..., source_context: _Optional[_Union[ConnectorContext, _Mapping]]=...) -> None:
        ...

class GetExampleQueriesResponse(_message.Message):
    __slots__ = ('examples',)
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[ExampleQuery]

    def __init__(self, examples: _Optional[_Iterable[_Union[ExampleQuery, _Mapping]]]=...) -> None:
        ...

class ConnectorStatEntry(_message.Message):
    __slots__ = ('connector_id', 'query_count', 'error_rate', 'avg_query_time_ms', 'unique_users', 'last_queried_at', 'table_count')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_RATE_FIELD_NUMBER: _ClassVar[int]
    AVG_QUERY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_USERS_FIELD_NUMBER: _ClassVar[int]
    LAST_QUERIED_AT_FIELD_NUMBER: _ClassVar[int]
    TABLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    query_count: int
    error_rate: float
    avg_query_time_ms: int
    unique_users: int
    last_queried_at: _timestamp_pb2.Timestamp
    table_count: int

    def __init__(self, connector_id: _Optional[int]=..., query_count: _Optional[int]=..., error_rate: _Optional[float]=..., avg_query_time_ms: _Optional[int]=..., unique_users: _Optional[int]=..., last_queried_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., table_count: _Optional[int]=...) -> None:
        ...

class GetConnectorStatsRequest(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int

    def __init__(self, days: _Optional[int]=...) -> None:
        ...

class GetConnectorStatsResponse(_message.Message):
    __slots__ = ('stats',)
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: _containers.RepeatedCompositeFieldContainer[ConnectorStatEntry]

    def __init__(self, stats: _Optional[_Iterable[_Union[ConnectorStatEntry, _Mapping]]]=...) -> None:
        ...

class ListQueryTemplatesRequest(_message.Message):
    __slots__ = ('connector_id', 'limit', 'offset', 'days')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    limit: int
    offset: int
    days: int

    def __init__(self, connector_id: _Optional[int]=..., limit: _Optional[int]=..., offset: _Optional[int]=..., days: _Optional[int]=...) -> None:
        ...

class ListQueryTemplatesResponse(_message.Message):
    __slots__ = ('templates', 'total_count')
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[QueryTemplate]
    total_count: int

    def __init__(self, templates: _Optional[_Iterable[_Union[QueryTemplate, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class QueryTemplate(_message.Message):
    __slots__ = ('template_id', 'normalized_sql', 'tables', 'joins', 'event_count', 'first_seen', 'last_seen', 'cte_refs', 'avg_runtime_ms')
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    NORMALIZED_SQL_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    JOINS_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    FIRST_SEEN_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    CTE_REFS_FIELD_NUMBER: _ClassVar[int]
    AVG_RUNTIME_MS_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    normalized_sql: str
    tables: _containers.RepeatedScalarFieldContainer[str]
    joins: _containers.RepeatedCompositeFieldContainer[QueryJoinInfo]
    event_count: int
    first_seen: _timestamp_pb2.Timestamp
    last_seen: _timestamp_pb2.Timestamp
    cte_refs: _containers.RepeatedCompositeFieldContainer[QueryTemplateCteRef]
    avg_runtime_ms: int

    def __init__(self, template_id: _Optional[str]=..., normalized_sql: _Optional[str]=..., tables: _Optional[_Iterable[str]]=..., joins: _Optional[_Iterable[_Union[QueryJoinInfo, _Mapping]]]=..., event_count: _Optional[int]=..., first_seen: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_seen: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., cte_refs: _Optional[_Iterable[_Union[QueryTemplateCteRef, _Mapping]]]=..., avg_runtime_ms: _Optional[int]=...) -> None:
        ...

class QueryTemplateCteRef(_message.Message):
    __slots__ = ('template_id', 'cte_name')
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    CTE_NAME_FIELD_NUMBER: _ClassVar[int]
    template_id: str
    cte_name: str

    def __init__(self, template_id: _Optional[str]=..., cte_name: _Optional[str]=...) -> None:
        ...

class QueryJoinInfo(_message.Message):
    __slots__ = ('tables', 'join_type')
    TABLES_FIELD_NUMBER: _ClassVar[int]
    JOIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    tables: _containers.RepeatedScalarFieldContainer[str]
    join_type: str

    def __init__(self, tables: _Optional[_Iterable[str]]=..., join_type: _Optional[str]=...) -> None:
        ...

class GetConnectorUsageRequest(_message.Message):
    __slots__ = ('connector_id', 'days')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    days: int

    def __init__(self, connector_id: _Optional[int]=..., days: _Optional[int]=...) -> None:
        ...

class GetConnectorUsageResponse(_message.Message):
    __slots__ = ('daily_volume', 'top_users', 'total_queries', 'daily_execution_ms')
    DAILY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOP_USERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_QUERIES_FIELD_NUMBER: _ClassVar[int]
    DAILY_EXECUTION_MS_FIELD_NUMBER: _ClassVar[int]
    daily_volume: _containers.RepeatedCompositeFieldContainer[DailyQueryCount]
    top_users: _containers.RepeatedCompositeFieldContainer[TopUser]
    total_queries: int
    daily_execution_ms: _containers.RepeatedCompositeFieldContainer[DailyDuration]

    def __init__(self, daily_volume: _Optional[_Iterable[_Union[DailyQueryCount, _Mapping]]]=..., top_users: _Optional[_Iterable[_Union[TopUser, _Mapping]]]=..., total_queries: _Optional[int]=..., daily_execution_ms: _Optional[_Iterable[_Union[DailyDuration, _Mapping]]]=...) -> None:
        ...

class DailyQueryCount(_message.Message):
    __slots__ = ('date', 'count')
    DATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    date: str
    count: int

    def __init__(self, date: _Optional[str]=..., count: _Optional[int]=...) -> None:
        ...

class DailyDuration(_message.Message):
    __slots__ = ('date', 'total_ms')
    DATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MS_FIELD_NUMBER: _ClassVar[int]
    date: str
    total_ms: int

    def __init__(self, date: _Optional[str]=..., total_ms: _Optional[int]=...) -> None:
        ...

class TopUser(_message.Message):
    __slots__ = ('member_id', 'display_name', 'email', 'query_count', 'chat_count', 'picture_url')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    QUERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHAT_COUNT_FIELD_NUMBER: _ClassVar[int]
    PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    display_name: str
    email: str
    query_count: int
    chat_count: int
    picture_url: str

    def __init__(self, member_id: _Optional[str]=..., display_name: _Optional[str]=..., email: _Optional[str]=..., query_count: _Optional[int]=..., chat_count: _Optional[int]=..., picture_url: _Optional[str]=...) -> None:
        ...

class GetConnectorChatsRequest(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class GetConnectorChatsResponse(_message.Message):
    __slots__ = ('stats', 'chats')
    STATS_FIELD_NUMBER: _ClassVar[int]
    CHATS_FIELD_NUMBER: _ClassVar[int]
    stats: ConnectorChatStats
    chats: _containers.RepeatedCompositeFieldContainer[ConnectorChat]

    def __init__(self, stats: _Optional[_Union[ConnectorChatStats, _Mapping]]=..., chats: _Optional[_Iterable[_Union[ConnectorChat, _Mapping]]]=...) -> None:
        ...

class ConnectorChatStats(_message.Message):
    __slots__ = ('chats_this_week', 'chats_last_week', 'active_users', 'active_users_last_week', 'avg_queries_per_chat', 'total_chats')
    CHATS_THIS_WEEK_FIELD_NUMBER: _ClassVar[int]
    CHATS_LAST_WEEK_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_USERS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_USERS_LAST_WEEK_FIELD_NUMBER: _ClassVar[int]
    AVG_QUERIES_PER_CHAT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CHATS_FIELD_NUMBER: _ClassVar[int]
    chats_this_week: int
    chats_last_week: int
    active_users: int
    active_users_last_week: int
    avg_queries_per_chat: float
    total_chats: int

    def __init__(self, chats_this_week: _Optional[int]=..., chats_last_week: _Optional[int]=..., active_users: _Optional[int]=..., active_users_last_week: _Optional[int]=..., avg_queries_per_chat: _Optional[float]=..., total_chats: _Optional[int]=...) -> None:
        ...

class ConnectorChat(_message.Message):
    __slots__ = ('chat_id', 'summary', 'member_id', 'display_name', 'email', 'query_count', 'last_activity', 'tables', 'picture_url')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    QUERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    summary: str
    member_id: str
    display_name: str
    email: str
    query_count: int
    last_activity: _timestamp_pb2.Timestamp
    tables: _containers.RepeatedScalarFieldContainer[str]
    picture_url: str

    def __init__(self, chat_id: _Optional[str]=..., summary: _Optional[str]=..., member_id: _Optional[str]=..., display_name: _Optional[str]=..., email: _Optional[str]=..., query_count: _Optional[int]=..., last_activity: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., tables: _Optional[_Iterable[str]]=..., picture_url: _Optional[str]=...) -> None:
        ...

class GetConnectorCellDurationsRequest(_message.Message):
    __slots__ = ('connector_id', 'days', 'limit', 'offset')
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    connector_id: int
    days: int
    limit: int
    offset: int

    def __init__(self, connector_id: _Optional[int]=..., days: _Optional[int]=..., limit: _Optional[int]=..., offset: _Optional[int]=...) -> None:
        ...

class GetConnectorCellDurationsResponse(_message.Message):
    __slots__ = ('cells', 'total_count')
    CELLS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    cells: _containers.RepeatedCompositeFieldContainer[ConnectorCellDuration]
    total_count: int

    def __init__(self, cells: _Optional[_Iterable[_Union[ConnectorCellDuration, _Mapping]]]=..., total_count: _Optional[int]=...) -> None:
        ...

class ConnectorCellDuration(_message.Message):
    __slots__ = ('cell_id', 'chat_id', 'duration_ms', 'has_duration', 'started_at', 'created_at', 'execution_error', 'member_id')
    CELL_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    HAS_DURATION_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_ERROR_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    cell_id: str
    chat_id: str
    duration_ms: int
    has_duration: bool
    started_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    execution_error: str
    member_id: str

    def __init__(self, cell_id: _Optional[str]=..., chat_id: _Optional[str]=..., duration_ms: _Optional[int]=..., has_duration: bool=..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., execution_error: _Optional[str]=..., member_id: _Optional[str]=...) -> None:
        ...

class GetConnectorDashboardsRequest(_message.Message):
    __slots__ = ('connector_id',)
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    connector_id: int

    def __init__(self, connector_id: _Optional[int]=...) -> None:
        ...

class GetConnectorDashboardsResponse(_message.Message):
    __slots__ = ('stats', 'dashboards')
    STATS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    stats: ConnectorDashboardStats
    dashboards: _containers.RepeatedCompositeFieldContainer[ConnectorDashboard]

    def __init__(self, stats: _Optional[_Union[ConnectorDashboardStats, _Mapping]]=..., dashboards: _Optional[_Iterable[_Union[ConnectorDashboard, _Mapping]]]=...) -> None:
        ...

class ConnectorDashboardStats(_message.Message):
    __slots__ = ('dashboards_this_week', 'dashboards_last_week', 'active_users', 'active_users_last_week', 'avg_queries_per_dashboard', 'total_dashboards')
    DASHBOARDS_THIS_WEEK_FIELD_NUMBER: _ClassVar[int]
    DASHBOARDS_LAST_WEEK_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_USERS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_USERS_LAST_WEEK_FIELD_NUMBER: _ClassVar[int]
    AVG_QUERIES_PER_DASHBOARD_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DASHBOARDS_FIELD_NUMBER: _ClassVar[int]
    dashboards_this_week: int
    dashboards_last_week: int
    active_users: int
    active_users_last_week: int
    avg_queries_per_dashboard: float
    total_dashboards: int

    def __init__(self, dashboards_this_week: _Optional[int]=..., dashboards_last_week: _Optional[int]=..., active_users: _Optional[int]=..., active_users_last_week: _Optional[int]=..., avg_queries_per_dashboard: _Optional[float]=..., total_dashboards: _Optional[int]=...) -> None:
        ...

class ConnectorDashboard(_message.Message):
    __slots__ = ('dashboard_id', 'name', 'member_id', 'display_name', 'email', 'query_count', 'last_activity', 'tables', 'picture_url')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    QUERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    TABLES_FIELD_NUMBER: _ClassVar[int]
    PICTURE_URL_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    name: str
    member_id: str
    display_name: str
    email: str
    query_count: int
    last_activity: _timestamp_pb2.Timestamp
    tables: _containers.RepeatedScalarFieldContainer[str]
    picture_url: str

    def __init__(self, dashboard_id: _Optional[str]=..., name: _Optional[str]=..., member_id: _Optional[str]=..., display_name: _Optional[str]=..., email: _Optional[str]=..., query_count: _Optional[int]=..., last_activity: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., tables: _Optional[_Iterable[str]]=..., picture_url: _Optional[str]=...) -> None:
        ...