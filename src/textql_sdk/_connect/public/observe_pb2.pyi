# pylint: skip-file
# mypy: ignore-errors
# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
import datetime
from ..google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import chat_pb2 as _chat_pb2
from ..public import warnings_pb2 as _warnings_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ThreadWarning(_message.Message):
    __slots__ = ('id', 'chat_id', 'warning_type', 'severity', 'detail', 'fix_chat_id', 'fix_patch_cell', 'fix_run_active', 'fix_status')
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    WARNING_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    DETAIL_FIELD_NUMBER: _ClassVar[int]
    FIX_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    FIX_PATCH_CELL_FIELD_NUMBER: _ClassVar[int]
    FIX_RUN_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FIX_STATUS_FIELD_NUMBER: _ClassVar[int]
    id: str
    chat_id: str
    warning_type: _warnings_pb2.ThreadWarningType
    severity: str
    detail: str
    fix_chat_id: str
    fix_patch_cell: _chat_pb2.Cell
    fix_run_active: bool
    fix_status: str

    def __init__(self, id: _Optional[str]=..., chat_id: _Optional[str]=..., warning_type: _Optional[_Union[_warnings_pb2.ThreadWarningType, str]]=..., severity: _Optional[str]=..., detail: _Optional[str]=..., fix_chat_id: _Optional[str]=..., fix_patch_cell: _Optional[_Union[_chat_pb2.Cell, _Mapping]]=..., fix_run_active: bool=..., fix_status: _Optional[str]=...) -> None:
        ...

class ThreadWarningList(_message.Message):
    __slots__ = ('warnings',)
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    warnings: _containers.RepeatedCompositeFieldContainer[ThreadWarning]

    def __init__(self, warnings: _Optional[_Iterable[_Union[ThreadWarning, _Mapping]]]=...) -> None:
        ...

class GetThreadWarningsRequest(_message.Message):
    __slots__ = ('chat_ids',)
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, chat_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetThreadWarningsResponse(_message.Message):
    __slots__ = ('warnings_by_chat', 'analyzed_chat_ids')

    class WarningsByChatEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ThreadWarningList

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ThreadWarningList, _Mapping]]=...) -> None:
            ...
    WARNINGS_BY_CHAT_FIELD_NUMBER: _ClassVar[int]
    ANALYZED_CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    warnings_by_chat: _containers.MessageMap[str, ThreadWarningList]
    analyzed_chat_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, warnings_by_chat: _Optional[_Mapping[str, ThreadWarningList]]=..., analyzed_chat_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class FixWarningRequest(_message.Message):
    __slots__ = ('warning_id',)
    WARNING_ID_FIELD_NUMBER: _ClassVar[int]
    warning_id: str

    def __init__(self, warning_id: _Optional[str]=...) -> None:
        ...

class FixWarningResponse(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class FixCheckRecordRequest(_message.Message):
    __slots__ = ('record_id',)
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    record_id: str

    def __init__(self, record_id: _Optional[str]=...) -> None:
        ...

class FixCheckRecordResponse(_message.Message):
    __slots__ = ('chat_id',)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str

    def __init__(self, chat_id: _Optional[str]=...) -> None:
        ...

class GetCheckRecordFixRequest(_message.Message):
    __slots__ = ('record_id',)
    RECORD_ID_FIELD_NUMBER: _ClassVar[int]
    record_id: str

    def __init__(self, record_id: _Optional[str]=...) -> None:
        ...

class GetCheckRecordFixResponse(_message.Message):
    __slots__ = ('fix_chat_id', 'fix_patch_cell', 'fix_run_active', 'fix_status')
    FIX_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    FIX_PATCH_CELL_FIELD_NUMBER: _ClassVar[int]
    FIX_RUN_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    FIX_STATUS_FIELD_NUMBER: _ClassVar[int]
    fix_chat_id: str
    fix_patch_cell: _chat_pb2.Cell
    fix_run_active: bool
    fix_status: str

    def __init__(self, fix_chat_id: _Optional[str]=..., fix_patch_cell: _Optional[_Union[_chat_pb2.Cell, _Mapping]]=..., fix_run_active: bool=..., fix_status: _Optional[str]=...) -> None:
        ...

class GetObservabilityStatsRequest(_message.Message):
    __slots__ = ('days', 'timezone')
    DAYS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    days: int
    timezone: str

    def __init__(self, days: _Optional[int]=..., timezone: _Optional[str]=...) -> None:
        ...

class GetObservabilityStatsResponse(_message.Message):
    __slots__ = ('summary', 'daily_volume', 'warning_distribution', 'warning_catalog', 'warning_daily_distribution', 'usage_heatmap')
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    DAILY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    WARNING_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    WARNING_CATALOG_FIELD_NUMBER: _ClassVar[int]
    WARNING_DAILY_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    USAGE_HEATMAP_FIELD_NUMBER: _ClassVar[int]
    summary: ObservabilitySummary
    daily_volume: _containers.RepeatedCompositeFieldContainer[DailyVolumePoint]
    warning_distribution: _containers.RepeatedCompositeFieldContainer[WarningTypeCount]
    warning_catalog: _containers.RepeatedCompositeFieldContainer[WarningTypeMeta]
    warning_daily_distribution: _containers.RepeatedCompositeFieldContainer[WarningTypeDailyCount]
    usage_heatmap: _containers.RepeatedCompositeFieldContainer[UsageHeatmapPoint]

    def __init__(self, summary: _Optional[_Union[ObservabilitySummary, _Mapping]]=..., daily_volume: _Optional[_Iterable[_Union[DailyVolumePoint, _Mapping]]]=..., warning_distribution: _Optional[_Iterable[_Union[WarningTypeCount, _Mapping]]]=..., warning_catalog: _Optional[_Iterable[_Union[WarningTypeMeta, _Mapping]]]=..., warning_daily_distribution: _Optional[_Iterable[_Union[WarningTypeDailyCount, _Mapping]]]=..., usage_heatmap: _Optional[_Iterable[_Union[UsageHeatmapPoint, _Mapping]]]=...) -> None:
        ...

class UsageHeatmapPoint(_message.Message):
    __slots__ = ('dow', 'hour', 'total')
    DOW_FIELD_NUMBER: _ClassVar[int]
    HOUR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    dow: int
    hour: int
    total: int

    def __init__(self, dow: _Optional[int]=..., hour: _Optional[int]=..., total: _Optional[int]=...) -> None:
        ...

class ObservabilitySummary(_message.Message):
    __slots__ = ('total_runs', 'total_threads', 'total_playbooks', 'total_warnings', 'warn_rate_pct', 'runs_delta_pct', 'threads_delta_pct', 'playbooks_delta_pct', 'warnings_delta_pct', 'runs_sparkline', 'threads_sparkline', 'playbooks_sparkline', 'warnings_sparkline', 'total_feed_agents', 'feed_agents_delta_pct', 'feed_agents_sparkline', 'total_slack', 'slack_delta_pct', 'slack_sparkline', 'total_teams', 'teams_delta_pct', 'teams_sparkline', 'total_positive', 'positive_delta_pct', 'positive_sparkline')
    TOTAL_RUNS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_THREADS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    WARN_RATE_PCT_FIELD_NUMBER: _ClassVar[int]
    RUNS_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    THREADS_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOKS_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    RUNS_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    THREADS_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOKS_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FEED_AGENTS_FIELD_NUMBER: _ClassVar[int]
    FEED_AGENTS_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    FEED_AGENTS_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SLACK_FIELD_NUMBER: _ClassVar[int]
    SLACK_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    SLACK_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TEAMS_FIELD_NUMBER: _ClassVar[int]
    TEAMS_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    TEAMS_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_POSITIVE_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_DELTA_PCT_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_SPARKLINE_FIELD_NUMBER: _ClassVar[int]
    total_runs: int
    total_threads: int
    total_playbooks: int
    total_warnings: int
    warn_rate_pct: int
    runs_delta_pct: int
    threads_delta_pct: int
    playbooks_delta_pct: int
    warnings_delta_pct: int
    runs_sparkline: _containers.RepeatedScalarFieldContainer[int]
    threads_sparkline: _containers.RepeatedScalarFieldContainer[int]
    playbooks_sparkline: _containers.RepeatedScalarFieldContainer[int]
    warnings_sparkline: _containers.RepeatedScalarFieldContainer[int]
    total_feed_agents: int
    feed_agents_delta_pct: int
    feed_agents_sparkline: _containers.RepeatedScalarFieldContainer[int]
    total_slack: int
    slack_delta_pct: int
    slack_sparkline: _containers.RepeatedScalarFieldContainer[int]
    total_teams: int
    teams_delta_pct: int
    teams_sparkline: _containers.RepeatedScalarFieldContainer[int]
    total_positive: int
    positive_delta_pct: int
    positive_sparkline: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, total_runs: _Optional[int]=..., total_threads: _Optional[int]=..., total_playbooks: _Optional[int]=..., total_warnings: _Optional[int]=..., warn_rate_pct: _Optional[int]=..., runs_delta_pct: _Optional[int]=..., threads_delta_pct: _Optional[int]=..., playbooks_delta_pct: _Optional[int]=..., warnings_delta_pct: _Optional[int]=..., runs_sparkline: _Optional[_Iterable[int]]=..., threads_sparkline: _Optional[_Iterable[int]]=..., playbooks_sparkline: _Optional[_Iterable[int]]=..., warnings_sparkline: _Optional[_Iterable[int]]=..., total_feed_agents: _Optional[int]=..., feed_agents_delta_pct: _Optional[int]=..., feed_agents_sparkline: _Optional[_Iterable[int]]=..., total_slack: _Optional[int]=..., slack_delta_pct: _Optional[int]=..., slack_sparkline: _Optional[_Iterable[int]]=..., total_teams: _Optional[int]=..., teams_delta_pct: _Optional[int]=..., teams_sparkline: _Optional[_Iterable[int]]=..., total_positive: _Optional[int]=..., positive_delta_pct: _Optional[int]=..., positive_sparkline: _Optional[_Iterable[int]]=...) -> None:
        ...

class DailyVolumePoint(_message.Message):
    __slots__ = ('date', 'threads', 'playbooks', 'feed_agents', 'slack', 'teams')
    DATE_FIELD_NUMBER: _ClassVar[int]
    THREADS_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOKS_FIELD_NUMBER: _ClassVar[int]
    FEED_AGENTS_FIELD_NUMBER: _ClassVar[int]
    SLACK_FIELD_NUMBER: _ClassVar[int]
    TEAMS_FIELD_NUMBER: _ClassVar[int]
    date: str
    threads: int
    playbooks: int
    feed_agents: int
    slack: int
    teams: int

    def __init__(self, date: _Optional[str]=..., threads: _Optional[int]=..., playbooks: _Optional[int]=..., feed_agents: _Optional[int]=..., slack: _Optional[int]=..., teams: _Optional[int]=...) -> None:
        ...

class WarningTypeCount(_message.Message):
    __slots__ = ('warning_type', 'total')
    WARNING_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    warning_type: _warnings_pb2.ThreadWarningType
    total: int

    def __init__(self, warning_type: _Optional[_Union[_warnings_pb2.ThreadWarningType, str]]=..., total: _Optional[int]=...) -> None:
        ...

class WarningTypeMeta(_message.Message):
    __slots__ = ('warning_type', 'category')
    WARNING_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    warning_type: _warnings_pb2.ThreadWarningType
    category: _warnings_pb2.WarningCategory

    def __init__(self, warning_type: _Optional[_Union[_warnings_pb2.ThreadWarningType, str]]=..., category: _Optional[_Union[_warnings_pb2.WarningCategory, str]]=...) -> None:
        ...

class WarningTypeDailyCount(_message.Message):
    __slots__ = ('date', 'warning_type', 'total')
    DATE_FIELD_NUMBER: _ClassVar[int]
    WARNING_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    date: str
    warning_type: _warnings_pb2.ThreadWarningType
    total: int

    def __init__(self, date: _Optional[str]=..., warning_type: _Optional[_Union[_warnings_pb2.ThreadWarningType, str]]=..., total: _Optional[int]=...) -> None:
        ...

class MemberSignalTrendPoint(_message.Message):
    __slots__ = ('member_id', 'bucket_start', 'positive', 'negative', 'analyzed')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    BUCKET_START_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_FIELD_NUMBER: _ClassVar[int]
    ANALYZED_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    bucket_start: str
    positive: int
    negative: int
    analyzed: int

    def __init__(self, member_id: _Optional[str]=..., bucket_start: _Optional[str]=..., positive: _Optional[int]=..., negative: _Optional[int]=..., analyzed: _Optional[int]=...) -> None:
        ...

class GetMemberSignalTrendRequest(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int

    def __init__(self, days: _Optional[int]=...) -> None:
        ...

class GetMemberSignalTrendResponse(_message.Message):
    __slots__ = ('points',)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[MemberSignalTrendPoint]

    def __init__(self, points: _Optional[_Iterable[_Union[MemberSignalTrendPoint, _Mapping]]]=...) -> None:
        ...

class GetBackfillPreviewRequest(_message.Message):
    __slots__ = ('days', 'org_id', 'redo_all_threads')
    DAYS_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REDO_ALL_THREADS_FIELD_NUMBER: _ClassVar[int]
    days: int
    org_id: str
    redo_all_threads: bool

    def __init__(self, days: _Optional[int]=..., org_id: _Optional[str]=..., redo_all_threads: bool=...) -> None:
        ...

class GetBackfillPreviewResponse(_message.Message):
    __slots__ = ('unanalyzed_count', 'org_name', 'eligible_thread_count')
    UNANALYZED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ORG_NAME_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    unanalyzed_count: int
    org_name: str
    eligible_thread_count: int

    def __init__(self, unanalyzed_count: _Optional[int]=..., org_name: _Optional[str]=..., eligible_thread_count: _Optional[int]=...) -> None:
        ...

class BackfillThreadWarningsRequest(_message.Message):
    __slots__ = ('days', 'concurrency', 'org_id', 'redo_all_threads')
    DAYS_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    REDO_ALL_THREADS_FIELD_NUMBER: _ClassVar[int]
    days: int
    concurrency: int
    org_id: str
    redo_all_threads: bool

    def __init__(self, days: _Optional[int]=..., concurrency: _Optional[int]=..., org_id: _Optional[str]=..., redo_all_threads: bool=...) -> None:
        ...

class BackfillThreadWarningsResponse(_message.Message):
    __slots__ = ('total_threads', 'already_running')
    TOTAL_THREADS_FIELD_NUMBER: _ClassVar[int]
    ALREADY_RUNNING_FIELD_NUMBER: _ClassVar[int]
    total_threads: int
    already_running: bool

    def __init__(self, total_threads: _Optional[int]=..., already_running: bool=...) -> None:
        ...

class GetBackfillStatusRequest(_message.Message):
    __slots__ = ('org_id',)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str

    def __init__(self, org_id: _Optional[str]=...) -> None:
        ...

class GetBackfillStatusResponse(_message.Message):
    __slots__ = ('running', 'total', 'processed', 'failed')
    RUNNING_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROCESSED_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    running: bool
    total: int
    processed: int
    failed: int

    def __init__(self, running: bool=..., total: _Optional[int]=..., processed: _Optional[int]=..., failed: _Optional[int]=...) -> None:
        ...

class GetBillingStatsRequest(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int

    def __init__(self, days: _Optional[int]=...) -> None:
        ...

class GetPlaybookBillingStatsRequest(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int

    def __init__(self, days: _Optional[int]=...) -> None:
        ...

class GetPlaybookBillingStatsResponse(_message.Message):
    __slots__ = ('playbook_stats', 'total_playbook_acu', 'unattributed_playbook_acu', 'total_playbook_count', 'acu_rate_per_1000_usd')
    PLAYBOOK_STATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PLAYBOOK_ACU_FIELD_NUMBER: _ClassVar[int]
    UNATTRIBUTED_PLAYBOOK_ACU_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PLAYBOOK_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACU_RATE_PER_1000_USD_FIELD_NUMBER: _ClassVar[int]
    playbook_stats: _containers.RepeatedCompositeFieldContainer[PlaybookBillingStat]
    total_playbook_acu: float
    unattributed_playbook_acu: float
    total_playbook_count: int
    acu_rate_per_1000_usd: float

    def __init__(self, playbook_stats: _Optional[_Iterable[_Union[PlaybookBillingStat, _Mapping]]]=..., total_playbook_acu: _Optional[float]=..., unattributed_playbook_acu: _Optional[float]=..., total_playbook_count: _Optional[int]=..., acu_rate_per_1000_usd: _Optional[float]=...) -> None:
        ...

class MemberBillingStat(_message.Message):
    __slots__ = ('member_id', 'member_name', 'email', 'total_acu', 'acu_by_category', 'acu_by_source', 'profile_image_url', 'thread_count', 'playbook_count', 'dashboard_count', 'agent_count', 'is_former_member', 'positive_signal_count', 'negative_signal_count', 'flagged_thread_count', 'analyzed_thread_count')

    class AcuByCategoryEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float

        def __init__(self, key: _Optional[str]=..., value: _Optional[float]=...) -> None:
            ...

    class AcuBySourceEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float

        def __init__(self, key: _Optional[str]=..., value: _Optional[float]=...) -> None:
            ...
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACU_FIELD_NUMBER: _ClassVar[int]
    ACU_BY_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    ACU_BY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_COUNT_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    AGENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_FORMER_MEMBER_FIELD_NUMBER: _ClassVar[int]
    POSITIVE_SIGNAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_SIGNAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLAGGED_THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    ANALYZED_THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    member_name: str
    email: str
    total_acu: float
    acu_by_category: _containers.ScalarMap[str, float]
    acu_by_source: _containers.ScalarMap[str, float]
    profile_image_url: str
    thread_count: int
    playbook_count: int
    dashboard_count: int
    agent_count: int
    is_former_member: bool
    positive_signal_count: int
    negative_signal_count: int
    flagged_thread_count: int
    analyzed_thread_count: int

    def __init__(self, member_id: _Optional[str]=..., member_name: _Optional[str]=..., email: _Optional[str]=..., total_acu: _Optional[float]=..., acu_by_category: _Optional[_Mapping[str, float]]=..., acu_by_source: _Optional[_Mapping[str, float]]=..., profile_image_url: _Optional[str]=..., thread_count: _Optional[int]=..., playbook_count: _Optional[int]=..., dashboard_count: _Optional[int]=..., agent_count: _Optional[int]=..., is_former_member: bool=..., positive_signal_count: _Optional[int]=..., negative_signal_count: _Optional[int]=..., flagged_thread_count: _Optional[int]=..., analyzed_thread_count: _Optional[int]=...) -> None:
        ...

class AgentBillingStat(_message.Message):
    __slots__ = ('agent_id', 'estimated_acu', 'is_internal')
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_ACU_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    agent_id: str
    estimated_acu: float
    is_internal: bool

    def __init__(self, agent_id: _Optional[str]=..., estimated_acu: _Optional[float]=..., is_internal: bool=...) -> None:
        ...

class PlaybookBillingStat(_message.Message):
    __slots__ = ('playbook_id', 'playbook_name', 'owner_id', 'owner_name', 'total_acu', 'llm_acu', 'compute_acu', 'run_count', 'is_internal', 'daily_run_counts', 'is_active')
    PLAYBOOK_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ACU_FIELD_NUMBER: _ClassVar[int]
    LLM_ACU_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ACU_FIELD_NUMBER: _ClassVar[int]
    RUN_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    DAILY_RUN_COUNTS_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    playbook_id: str
    playbook_name: str
    owner_id: str
    owner_name: str
    total_acu: float
    llm_acu: float
    compute_acu: float
    run_count: int
    is_internal: bool
    daily_run_counts: _containers.RepeatedScalarFieldContainer[int]
    is_active: bool

    def __init__(self, playbook_id: _Optional[str]=..., playbook_name: _Optional[str]=..., owner_id: _Optional[str]=..., owner_name: _Optional[str]=..., total_acu: _Optional[float]=..., llm_acu: _Optional[float]=..., compute_acu: _Optional[float]=..., run_count: _Optional[int]=..., is_internal: bool=..., daily_run_counts: _Optional[_Iterable[int]]=..., is_active: bool=...) -> None:
        ...

class DashboardBillingStat(_message.Message):
    __slots__ = ('dashboard_id', 'dashboard_name', 'owner_id', 'owner_name', 'compute_acu', 'refresh_count', 'is_internal', 'view_count', 'last_viewed_at', 'daily_view_counts', 'is_published')
    DASHBOARD_ID_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ACU_FIELD_NUMBER: _ClassVar[int]
    REFRESH_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_VIEWED_AT_FIELD_NUMBER: _ClassVar[int]
    DAILY_VIEW_COUNTS_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    dashboard_id: str
    dashboard_name: str
    owner_id: str
    owner_name: str
    compute_acu: float
    refresh_count: int
    is_internal: bool
    view_count: int
    last_viewed_at: _timestamp_pb2.Timestamp
    daily_view_counts: _containers.RepeatedScalarFieldContainer[int]
    is_published: bool

    def __init__(self, dashboard_id: _Optional[str]=..., dashboard_name: _Optional[str]=..., owner_id: _Optional[str]=..., owner_name: _Optional[str]=..., compute_acu: _Optional[float]=..., refresh_count: _Optional[int]=..., is_internal: bool=..., view_count: _Optional[int]=..., last_viewed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., daily_view_counts: _Optional[_Iterable[int]]=..., is_published: bool=...) -> None:
        ...

class AppBillingStat(_message.Message):
    __slots__ = ('app_id', 'app_name', 'owner_id', 'owner_name', 'compute_acu', 'refresh_count', 'is_internal', 'view_count', 'last_viewed_at', 'daily_view_counts', 'is_published')
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    APP_NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_ACU_FIELD_NUMBER: _ClassVar[int]
    REFRESH_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    VIEW_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_VIEWED_AT_FIELD_NUMBER: _ClassVar[int]
    DAILY_VIEW_COUNTS_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    app_id: str
    app_name: str
    owner_id: str
    owner_name: str
    compute_acu: float
    refresh_count: int
    is_internal: bool
    view_count: int
    last_viewed_at: _timestamp_pb2.Timestamp
    daily_view_counts: _containers.RepeatedScalarFieldContainer[int]
    is_published: bool

    def __init__(self, app_id: _Optional[str]=..., app_name: _Optional[str]=..., owner_id: _Optional[str]=..., owner_name: _Optional[str]=..., compute_acu: _Optional[float]=..., refresh_count: _Optional[int]=..., is_internal: bool=..., view_count: _Optional[int]=..., last_viewed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., daily_view_counts: _Optional[_Iterable[int]]=..., is_published: bool=...) -> None:
        ...

class GetBillingStatsResponse(_message.Message):
    __slots__ = ('member_stats', 'agent_stats', 'total_feed_acu', 'playbook_stats', 'dashboard_stats', 'total_playbook_acu', 'total_dashboard_acu', 'unattributed_feed_acu', 'unattributed_dashboard_acu', 'total_dashboard_count', 'total_playbook_count', 'unattributed_playbook_acu', 'app_stats', 'total_app_acu', 'unattributed_app_acu', 'total_app_count', 'acu_rate_per_1000_usd')
    MEMBER_STATS_FIELD_NUMBER: _ClassVar[int]
    AGENT_STATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FEED_ACU_FIELD_NUMBER: _ClassVar[int]
    PLAYBOOK_STATS_FIELD_NUMBER: _ClassVar[int]
    DASHBOARD_STATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PLAYBOOK_ACU_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DASHBOARD_ACU_FIELD_NUMBER: _ClassVar[int]
    UNATTRIBUTED_FEED_ACU_FIELD_NUMBER: _ClassVar[int]
    UNATTRIBUTED_DASHBOARD_ACU_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DASHBOARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PLAYBOOK_COUNT_FIELD_NUMBER: _ClassVar[int]
    UNATTRIBUTED_PLAYBOOK_ACU_FIELD_NUMBER: _ClassVar[int]
    APP_STATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_APP_ACU_FIELD_NUMBER: _ClassVar[int]
    UNATTRIBUTED_APP_ACU_FIELD_NUMBER: _ClassVar[int]
    TOTAL_APP_COUNT_FIELD_NUMBER: _ClassVar[int]
    ACU_RATE_PER_1000_USD_FIELD_NUMBER: _ClassVar[int]
    member_stats: _containers.RepeatedCompositeFieldContainer[MemberBillingStat]
    agent_stats: _containers.RepeatedCompositeFieldContainer[AgentBillingStat]
    total_feed_acu: float
    playbook_stats: _containers.RepeatedCompositeFieldContainer[PlaybookBillingStat]
    dashboard_stats: _containers.RepeatedCompositeFieldContainer[DashboardBillingStat]
    total_playbook_acu: float
    total_dashboard_acu: float
    unattributed_feed_acu: float
    unattributed_dashboard_acu: float
    total_dashboard_count: int
    total_playbook_count: int
    unattributed_playbook_acu: float
    app_stats: _containers.RepeatedCompositeFieldContainer[AppBillingStat]
    total_app_acu: float
    unattributed_app_acu: float
    total_app_count: int
    acu_rate_per_1000_usd: float

    def __init__(self, member_stats: _Optional[_Iterable[_Union[MemberBillingStat, _Mapping]]]=..., agent_stats: _Optional[_Iterable[_Union[AgentBillingStat, _Mapping]]]=..., total_feed_acu: _Optional[float]=..., playbook_stats: _Optional[_Iterable[_Union[PlaybookBillingStat, _Mapping]]]=..., dashboard_stats: _Optional[_Iterable[_Union[DashboardBillingStat, _Mapping]]]=..., total_playbook_acu: _Optional[float]=..., total_dashboard_acu: _Optional[float]=..., unattributed_feed_acu: _Optional[float]=..., unattributed_dashboard_acu: _Optional[float]=..., total_dashboard_count: _Optional[int]=..., total_playbook_count: _Optional[int]=..., unattributed_playbook_acu: _Optional[float]=..., app_stats: _Optional[_Iterable[_Union[AppBillingStat, _Mapping]]]=..., total_app_acu: _Optional[float]=..., unattributed_app_acu: _Optional[float]=..., total_app_count: _Optional[int]=..., acu_rate_per_1000_usd: _Optional[float]=...) -> None:
        ...

class GetActivePeopleStatsRequest(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int

    def __init__(self, days: _Optional[int]=...) -> None:
        ...

class GetActivePeopleStatsResponse(_message.Message):
    __slots__ = ('active_member_count', 'total_member_count')
    ACTIVE_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    active_member_count: int
    total_member_count: int

    def __init__(self, active_member_count: _Optional[int]=..., total_member_count: _Optional[int]=...) -> None:
        ...

class GetChatSourceStatsRequest(_message.Message):
    __slots__ = ('days', 'exclude_textql', 'member_id', 'start_date', 'end_date')
    DAYS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_TEXTQL_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    days: int
    exclude_textql: bool
    member_id: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp

    def __init__(self, days: _Optional[int]=..., exclude_textql: bool=..., member_id: _Optional[str]=..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ChatSourceCount(_message.Message):
    __slots__ = ('source', 'total')
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    source: _chat_pb2.ChatSource
    total: int

    def __init__(self, source: _Optional[_Union[_chat_pb2.ChatSource, str]]=..., total: _Optional[int]=...) -> None:
        ...

class MemberChatSourceStat(_message.Message):
    __slots__ = ('member_id', 'member_name', 'email', 'total', 'by_source')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    BY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    member_name: str
    email: str
    total: int
    by_source: _containers.RepeatedCompositeFieldContainer[ChatSourceCount]

    def __init__(self, member_id: _Optional[str]=..., member_name: _Optional[str]=..., email: _Optional[str]=..., total: _Optional[int]=..., by_source: _Optional[_Iterable[_Union[ChatSourceCount, _Mapping]]]=...) -> None:
        ...

class GetChatSourceStatsResponse(_message.Message):
    __slots__ = ('org_by_source', 'member_stats')
    ORG_BY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_STATS_FIELD_NUMBER: _ClassVar[int]
    org_by_source: _containers.RepeatedCompositeFieldContainer[ChatSourceCount]
    member_stats: _containers.RepeatedCompositeFieldContainer[MemberChatSourceStat]

    def __init__(self, org_by_source: _Optional[_Iterable[_Union[ChatSourceCount, _Mapping]]]=..., member_stats: _Optional[_Iterable[_Union[MemberChatSourceStat, _Mapping]]]=...) -> None:
        ...

class GetActivePeopleTrendRequest(_message.Message):
    __slots__ = ('days', 'start_date', 'end_date')
    DAYS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    days: int
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp

    def __init__(self, days: _Optional[int]=..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ActivePeoplePoint(_message.Message):
    __slots__ = ('bucket_start', 'returning', 'new_people')
    BUCKET_START_FIELD_NUMBER: _ClassVar[int]
    RETURNING_FIELD_NUMBER: _ClassVar[int]
    NEW_PEOPLE_FIELD_NUMBER: _ClassVar[int]
    bucket_start: str
    returning: int
    new_people: int

    def __init__(self, bucket_start: _Optional[str]=..., returning: _Optional[int]=..., new_people: _Optional[int]=...) -> None:
        ...

class GetActivePeopleTrendResponse(_message.Message):
    __slots__ = ('points', 'growth_pct', 'bucket_unit')
    POINTS_FIELD_NUMBER: _ClassVar[int]
    GROWTH_PCT_FIELD_NUMBER: _ClassVar[int]
    BUCKET_UNIT_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[ActivePeoplePoint]
    growth_pct: int
    bucket_unit: str

    def __init__(self, points: _Optional[_Iterable[_Union[ActivePeoplePoint, _Mapping]]]=..., growth_pct: _Optional[int]=..., bucket_unit: _Optional[str]=...) -> None:
        ...

class GetEngagementSpectrumRequest(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int

    def __init__(self, days: _Optional[int]=...) -> None:
        ...

class EngagementTierCount(_message.Message):
    __slots__ = ('tier', 'count')
    TIER_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    tier: str
    count: int

    def __init__(self, tier: _Optional[str]=..., count: _Optional[int]=...) -> None:
        ...

class GetEngagementSpectrumResponse(_message.Message):
    __slots__ = ('tiers', 'total_people')
    TIERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PEOPLE_FIELD_NUMBER: _ClassVar[int]
    tiers: _containers.RepeatedCompositeFieldContainer[EngagementTierCount]
    total_people: int

    def __init__(self, tiers: _Optional[_Iterable[_Union[EngagementTierCount, _Mapping]]]=..., total_people: _Optional[int]=...) -> None:
        ...

class GetAccessMethodStatsRequest(_message.Message):
    __slots__ = ('days', 'start_date', 'end_date')
    DAYS_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    days: int
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp

    def __init__(self, days: _Optional[int]=..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class AccessMethodCount(_message.Message):
    __slots__ = ('method', 'total')
    METHOD_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    method: str
    total: int

    def __init__(self, method: _Optional[str]=..., total: _Optional[int]=...) -> None:
        ...

class GetAccessMethodStatsResponse(_message.Message):
    __slots__ = ('methods',)
    METHODS_FIELD_NUMBER: _ClassVar[int]
    methods: _containers.RepeatedCompositeFieldContainer[AccessMethodCount]

    def __init__(self, methods: _Optional[_Iterable[_Union[AccessMethodCount, _Mapping]]]=...) -> None:
        ...

class GetMemberActivityRequest(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: int

    def __init__(self, days: _Optional[int]=...) -> None:
        ...

class MemberActivity(_message.Message):
    __slots__ = ('member_id', 'daily_activity', 'event_count', 'thread_count', 'last_active')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    DAILY_ACTIVITY_FIELD_NUMBER: _ClassVar[int]
    EVENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    daily_activity: _containers.RepeatedScalarFieldContainer[int]
    event_count: int
    thread_count: int
    last_active: _timestamp_pb2.Timestamp

    def __init__(self, member_id: _Optional[str]=..., daily_activity: _Optional[_Iterable[int]]=..., event_count: _Optional[int]=..., thread_count: _Optional[int]=..., last_active: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetMemberActivityResponse(_message.Message):
    __slots__ = ('members',)
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[MemberActivity]

    def __init__(self, members: _Optional[_Iterable[_Union[MemberActivity, _Mapping]]]=...) -> None:
        ...

class ExportObservabilityCsvRequest(_message.Message):
    __slots__ = ('tab', 'days')
    TAB_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    tab: str
    days: int

    def __init__(self, tab: _Optional[str]=..., days: _Optional[int]=...) -> None:
        ...

class ExportObservabilityCsvResponse(_message.Message):
    __slots__ = ('download_url',)
    DOWNLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    download_url: str

    def __init__(self, download_url: _Optional[str]=...) -> None:
        ...

class CustomTopic(_message.Message):
    __slots__ = ('id', 'name', 'user_prompt', 'covers', 'excludes', 'status', 'created_by_member_id', 'backfill_chat_id', 'backfill_status', 'backfill_error', 'created_at', 'tag_count', 'updated_at', 'created_by_email', 'daily_tag_counts', 'people_count')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    COVERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_STATUS_FIELD_NUMBER: _ClassVar[int]
    BACKFILL_ERROR_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    TAG_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DAILY_TAG_COUNTS_FIELD_NUMBER: _ClassVar[int]
    PEOPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    user_prompt: str
    covers: str
    excludes: str
    status: str
    created_by_member_id: str
    backfill_chat_id: str
    backfill_status: str
    backfill_error: str
    created_at: _timestamp_pb2.Timestamp
    tag_count: int
    updated_at: _timestamp_pb2.Timestamp
    created_by_email: str
    daily_tag_counts: _containers.RepeatedScalarFieldContainer[int]
    people_count: int

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=..., user_prompt: _Optional[str]=..., covers: _Optional[str]=..., excludes: _Optional[str]=..., status: _Optional[str]=..., created_by_member_id: _Optional[str]=..., backfill_chat_id: _Optional[str]=..., backfill_status: _Optional[str]=..., backfill_error: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., tag_count: _Optional[int]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., created_by_email: _Optional[str]=..., daily_tag_counts: _Optional[_Iterable[int]]=..., people_count: _Optional[int]=...) -> None:
        ...

class RefineTopicDraftRequest(_message.Message):
    __slots__ = ('prompt', 'examples', 'exclusions')
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIONS_FIELD_NUMBER: _ClassVar[int]
    prompt: str
    examples: _containers.RepeatedScalarFieldContainer[str]
    exclusions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, prompt: _Optional[str]=..., examples: _Optional[_Iterable[str]]=..., exclusions: _Optional[_Iterable[str]]=...) -> None:
        ...

class SimilarTopic(_message.Message):
    __slots__ = ('id', 'name')
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str

    def __init__(self, id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class RefineTopicDraftResponse(_message.Message):
    __slots__ = ('name', 'covers', 'excludes', 'vague', 'quality_hint', 'similar_topics')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COVERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    VAGUE_FIELD_NUMBER: _ClassVar[int]
    QUALITY_HINT_FIELD_NUMBER: _ClassVar[int]
    SIMILAR_TOPICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    covers: str
    excludes: str
    vague: bool
    quality_hint: str
    similar_topics: _containers.RepeatedCompositeFieldContainer[SimilarTopic]

    def __init__(self, name: _Optional[str]=..., covers: _Optional[str]=..., excludes: _Optional[str]=..., vague: bool=..., quality_hint: _Optional[str]=..., similar_topics: _Optional[_Iterable[_Union[SimilarTopic, _Mapping]]]=...) -> None:
        ...

class CreateCustomTopicRequest(_message.Message):
    __slots__ = ('name', 'user_prompt', 'covers', 'excludes')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    COVERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_prompt: str
    covers: str
    excludes: str

    def __init__(self, name: _Optional[str]=..., user_prompt: _Optional[str]=..., covers: _Optional[str]=..., excludes: _Optional[str]=...) -> None:
        ...

class CustomTopicResponse(_message.Message):
    __slots__ = ('topic',)
    TOPIC_FIELD_NUMBER: _ClassVar[int]
    topic: CustomTopic

    def __init__(self, topic: _Optional[_Union[CustomTopic, _Mapping]]=...) -> None:
        ...

class BackfillCustomTopicRequest(_message.Message):
    __slots__ = ('topic_id', 'start_date', 'end_date')
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    start_date: _timestamp_pb2.Timestamp
    end_date: _timestamp_pb2.Timestamp

    def __init__(self, topic_id: _Optional[str]=..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., end_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class BackfillCustomTopicResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetCustomTopicRequest(_message.Message):
    __slots__ = ('topic_id', 'trend_start', 'trend_end')
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    TREND_START_FIELD_NUMBER: _ClassVar[int]
    TREND_END_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    trend_start: _timestamp_pb2.Timestamp
    trend_end: _timestamp_pb2.Timestamp

    def __init__(self, topic_id: _Optional[str]=..., trend_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., trend_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListCustomTopicsRequest(_message.Message):
    __slots__ = ('trend_start', 'trend_end')
    TREND_START_FIELD_NUMBER: _ClassVar[int]
    TREND_END_FIELD_NUMBER: _ClassVar[int]
    trend_start: _timestamp_pb2.Timestamp
    trend_end: _timestamp_pb2.Timestamp

    def __init__(self, trend_start: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., trend_end: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListCustomTopicsResponse(_message.Message):
    __slots__ = ('topics',)
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[CustomTopic]

    def __init__(self, topics: _Optional[_Iterable[_Union[CustomTopic, _Mapping]]]=...) -> None:
        ...

class GetCustomTopicThreadsRequest(_message.Message):
    __slots__ = ('topic_id', 'verdict', 'page_token', 'page_size', 'member_id')
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    verdict: str
    page_token: str
    page_size: int
    member_id: str

    def __init__(self, topic_id: _Optional[str]=..., verdict: _Optional[str]=..., page_token: _Optional[str]=..., page_size: _Optional[int]=..., member_id: _Optional[str]=...) -> None:
        ...

class GetCustomTopicPeopleRequest(_message.Message):
    __slots__ = ('topic_id',)
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str

    def __init__(self, topic_id: _Optional[str]=...) -> None:
        ...

class CustomTopicPerson(_message.Message):
    __slots__ = ('member_id', 'name', 'email', 'thread_count')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    THREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    name: str
    email: str
    thread_count: int

    def __init__(self, member_id: _Optional[str]=..., name: _Optional[str]=..., email: _Optional[str]=..., thread_count: _Optional[int]=...) -> None:
        ...

class GetCustomTopicPeopleResponse(_message.Message):
    __slots__ = ('people',)
    PEOPLE_FIELD_NUMBER: _ClassVar[int]
    people: _containers.RepeatedCompositeFieldContainer[CustomTopicPerson]

    def __init__(self, people: _Optional[_Iterable[_Union[CustomTopicPerson, _Mapping]]]=...) -> None:
        ...

class GetChatTopicsRequest(_message.Message):
    __slots__ = ('chat_ids',)
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, chat_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class ChatTopicRef(_message.Message):
    __slots__ = ('topic_id', 'name')
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    name: str

    def __init__(self, topic_id: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class ChatTopicList(_message.Message):
    __slots__ = ('topics',)
    TOPICS_FIELD_NUMBER: _ClassVar[int]
    topics: _containers.RepeatedCompositeFieldContainer[ChatTopicRef]

    def __init__(self, topics: _Optional[_Iterable[_Union[ChatTopicRef, _Mapping]]]=...) -> None:
        ...

class GetChatTopicsResponse(_message.Message):
    __slots__ = ('topics_by_chat',)

    class TopicsByChatEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ChatTopicList

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ChatTopicList, _Mapping]]=...) -> None:
            ...
    TOPICS_BY_CHAT_FIELD_NUMBER: _ClassVar[int]
    topics_by_chat: _containers.MessageMap[str, ChatTopicList]

    def __init__(self, topics_by_chat: _Optional[_Mapping[str, ChatTopicList]]=...) -> None:
        ...

class CustomTopicThread(_message.Message):
    __slots__ = ('chat_id', 'title', 'member_id', 'tagged_by', 'tagged_at')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TAGGED_BY_FIELD_NUMBER: _ClassVar[int]
    TAGGED_AT_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    title: str
    member_id: str
    tagged_by: str
    tagged_at: _timestamp_pb2.Timestamp

    def __init__(self, chat_id: _Optional[str]=..., title: _Optional[str]=..., member_id: _Optional[str]=..., tagged_by: _Optional[str]=..., tagged_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetCustomTopicThreadsResponse(_message.Message):
    __slots__ = ('threads', 'next_page_token')
    THREADS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    threads: _containers.RepeatedCompositeFieldContainer[CustomTopicThread]
    next_page_token: str

    def __init__(self, threads: _Optional[_Iterable[_Union[CustomTopicThread, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateCustomTopicRequest(_message.Message):
    __slots__ = ('topic_id', 'name', 'covers', 'excludes')
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COVERS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDES_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    name: str
    covers: str
    excludes: str

    def __init__(self, topic_id: _Optional[str]=..., name: _Optional[str]=..., covers: _Optional[str]=..., excludes: _Optional[str]=...) -> None:
        ...

class SetTopicTagFeedbackRequest(_message.Message):
    __slots__ = ('topic_id', 'chat_id', 'excluded', 'reason')
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    topic_id: str
    chat_id: str
    excluded: bool
    reason: str

    def __init__(self, topic_id: _Optional[str]=..., chat_id: _Optional[str]=..., excluded: bool=..., reason: _Optional[str]=...) -> None:
        ...

class SetTopicTagFeedbackResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TopicLifecycleRequest(_message.Message):
    __slots__ = ('topic_id',)
    TOPIC_ID_FIELD_NUMBER: _ClassVar[int]
    topic_id: str

    def __init__(self, topic_id: _Optional[str]=...) -> None:
        ...

class TopicLifecycleResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...