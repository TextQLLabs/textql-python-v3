# pyright: reportInvalidTypeForm=false, reportAttributeAccessIssue=false
# pylint: skip-file
# mypy: ignore-errors
import datetime
from ..google.api import visibility_pb2 as _visibility_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from ..public import config_source_pb2 as _config_source_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PatchStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PATCH_STATUS_UNKNOWN: _ClassVar[PatchStatus]
    PATCH_STATUS_RESERVED: _ClassVar[PatchStatus]
    PATCH_STATUS_DRAFT: _ClassVar[PatchStatus]
    PATCH_STATUS_OPEN: _ClassVar[PatchStatus]
    PATCH_STATUS_APPROVED: _ClassVar[PatchStatus]
    PATCH_STATUS_DENIED: _ClassVar[PatchStatus]

class PatchLineOp(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PATCH_LINE_OP_CONTEXT: _ClassVar[PatchLineOp]
    PATCH_LINE_OP_DELETE: _ClassVar[PatchLineOp]
    PATCH_LINE_OP_ADD: _ClassVar[PatchLineOp]

class ConfigDiagnosticClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONFIG_DIAGNOSTIC_CLASS_UNSPECIFIED: _ClassVar[ConfigDiagnosticClass]
    CONFIG_DIAGNOSTIC_CLASS_EDIT_FIXABLE: _ClassVar[ConfigDiagnosticClass]
    CONFIG_DIAGNOSTIC_CLASS_ORG_STATE_FIXABLE: _ClassVar[ConfigDiagnosticClass]

class OntologyFileKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONTOLOGY_FILE_KIND_UNSPECIFIED: _ClassVar[OntologyFileKind]
    ONTOLOGY_FILE_KIND_TEXT: _ClassVar[OntologyFileKind]
    ONTOLOGY_FILE_KIND_PDF: _ClassVar[OntologyFileKind]
    ONTOLOGY_FILE_KIND_IMAGE: _ClassVar[OntologyFileKind]
    ONTOLOGY_FILE_KIND_ASSET: _ClassVar[OntologyFileKind]
    ONTOLOGY_FILE_KIND_TABULAR: _ClassVar[OntologyFileKind]

class OntologyHistoryChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONTOLOGY_HISTORY_CHANGE_TYPE_UNSPECIFIED: _ClassVar[OntologyHistoryChangeType]
    ONTOLOGY_HISTORY_CHANGE_TYPE_ADDED: _ClassVar[OntologyHistoryChangeType]
    ONTOLOGY_HISTORY_CHANGE_TYPE_MODIFIED: _ClassVar[OntologyHistoryChangeType]
    ONTOLOGY_HISTORY_CHANGE_TYPE_DELETED: _ClassVar[OntologyHistoryChangeType]
    ONTOLOGY_HISTORY_CHANGE_TYPE_RENAMED: _ClassVar[OntologyHistoryChangeType]

class OntologyPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONTOLOGY_PERMISSION_UNSPECIFIED: _ClassVar[OntologyPermission]
    ONTOLOGY_PERMISSION_EXECUTE: _ClassVar[OntologyPermission]
    ONTOLOGY_PERMISSION_READ: _ClassVar[OntologyPermission]
    ONTOLOGY_PERMISSION_READ_EXECUTE: _ClassVar[OntologyPermission]
    ONTOLOGY_PERMISSION_READ_WRITE: _ClassVar[OntologyPermission]
    ONTOLOGY_PERMISSION_READ_WRITE_EXECUTE: _ClassVar[OntologyPermission]

class OntologyMergeOutcome(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONTOLOGY_MERGE_OUTCOME_UNSPECIFIED: _ClassVar[OntologyMergeOutcome]
    ONTOLOGY_MERGE_OUTCOME_ALREADY_UP_TO_DATE: _ClassVar[OntologyMergeOutcome]
    ONTOLOGY_MERGE_OUTCOME_LOCAL_AHEAD: _ClassVar[OntologyMergeOutcome]
    ONTOLOGY_MERGE_OUTCOME_FAST_FORWARD: _ClassVar[OntologyMergeOutcome]
    ONTOLOGY_MERGE_OUTCOME_BOOTSTRAP_ADOPT: _ClassVar[OntologyMergeOutcome]
    ONTOLOGY_MERGE_OUTCOME_MERGE_REQUIRED: _ClassVar[OntologyMergeOutcome]
    ONTOLOGY_MERGE_OUTCOME_UNRELATED_HISTORIES: _ClassVar[OntologyMergeOutcome]

class RecoverOntologyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECOVER_ONTOLOGY_LEVEL_UNSPECIFIED: _ClassVar[RecoverOntologyLevel]
    RECOVER_ONTOLOGY_LEVEL_DISCARD_LOCAL: _ClassVar[RecoverOntologyLevel]
    RECOVER_ONTOLOGY_LEVEL_RESET_TO_REMOTE: _ClassVar[RecoverOntologyLevel]
    RECOVER_ONTOLOGY_LEVEL_RECLONE: _ClassVar[RecoverOntologyLevel]

class OntologySyncRunStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ONTOLOGY_SYNC_RUN_STATUS_UNSPECIFIED: _ClassVar[OntologySyncRunStatus]
    ONTOLOGY_SYNC_RUN_STATUS_IN_PROGRESS: _ClassVar[OntologySyncRunStatus]
    ONTOLOGY_SYNC_RUN_STATUS_SUCCEEDED: _ClassVar[OntologySyncRunStatus]
    ONTOLOGY_SYNC_RUN_STATUS_FAILED: _ClassVar[OntologySyncRunStatus]
    ONTOLOGY_SYNC_RUN_STATUS_CONFLICTS: _ClassVar[OntologySyncRunStatus]

class UsageOrderBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_BY_UNKNOWN: _ClassVar[UsageOrderBy]
    ORDER_BY_MOST_RECENTLY_USED: _ClassVar[UsageOrderBy]
    ORDER_BY_LEAST_RECENTLY_USED: _ClassVar[UsageOrderBy]
    ORDER_BY_MOST_FREQUENTLY_USED: _ClassVar[UsageOrderBy]
    ORDER_BY_LEAST_FREQUENTLY_USED: _ClassVar[UsageOrderBy]
PATCH_STATUS_UNKNOWN: PatchStatus
PATCH_STATUS_RESERVED: PatchStatus
PATCH_STATUS_DRAFT: PatchStatus
PATCH_STATUS_OPEN: PatchStatus
PATCH_STATUS_APPROVED: PatchStatus
PATCH_STATUS_DENIED: PatchStatus
PATCH_LINE_OP_CONTEXT: PatchLineOp
PATCH_LINE_OP_DELETE: PatchLineOp
PATCH_LINE_OP_ADD: PatchLineOp
CONFIG_DIAGNOSTIC_CLASS_UNSPECIFIED: ConfigDiagnosticClass
CONFIG_DIAGNOSTIC_CLASS_EDIT_FIXABLE: ConfigDiagnosticClass
CONFIG_DIAGNOSTIC_CLASS_ORG_STATE_FIXABLE: ConfigDiagnosticClass
ONTOLOGY_FILE_KIND_UNSPECIFIED: OntologyFileKind
ONTOLOGY_FILE_KIND_TEXT: OntologyFileKind
ONTOLOGY_FILE_KIND_PDF: OntologyFileKind
ONTOLOGY_FILE_KIND_IMAGE: OntologyFileKind
ONTOLOGY_FILE_KIND_ASSET: OntologyFileKind
ONTOLOGY_FILE_KIND_TABULAR: OntologyFileKind
ONTOLOGY_HISTORY_CHANGE_TYPE_UNSPECIFIED: OntologyHistoryChangeType
ONTOLOGY_HISTORY_CHANGE_TYPE_ADDED: OntologyHistoryChangeType
ONTOLOGY_HISTORY_CHANGE_TYPE_MODIFIED: OntologyHistoryChangeType
ONTOLOGY_HISTORY_CHANGE_TYPE_DELETED: OntologyHistoryChangeType
ONTOLOGY_HISTORY_CHANGE_TYPE_RENAMED: OntologyHistoryChangeType
ONTOLOGY_PERMISSION_UNSPECIFIED: OntologyPermission
ONTOLOGY_PERMISSION_EXECUTE: OntologyPermission
ONTOLOGY_PERMISSION_READ: OntologyPermission
ONTOLOGY_PERMISSION_READ_EXECUTE: OntologyPermission
ONTOLOGY_PERMISSION_READ_WRITE: OntologyPermission
ONTOLOGY_PERMISSION_READ_WRITE_EXECUTE: OntologyPermission
ONTOLOGY_MERGE_OUTCOME_UNSPECIFIED: OntologyMergeOutcome
ONTOLOGY_MERGE_OUTCOME_ALREADY_UP_TO_DATE: OntologyMergeOutcome
ONTOLOGY_MERGE_OUTCOME_LOCAL_AHEAD: OntologyMergeOutcome
ONTOLOGY_MERGE_OUTCOME_FAST_FORWARD: OntologyMergeOutcome
ONTOLOGY_MERGE_OUTCOME_BOOTSTRAP_ADOPT: OntologyMergeOutcome
ONTOLOGY_MERGE_OUTCOME_MERGE_REQUIRED: OntologyMergeOutcome
ONTOLOGY_MERGE_OUTCOME_UNRELATED_HISTORIES: OntologyMergeOutcome
RECOVER_ONTOLOGY_LEVEL_UNSPECIFIED: RecoverOntologyLevel
RECOVER_ONTOLOGY_LEVEL_DISCARD_LOCAL: RecoverOntologyLevel
RECOVER_ONTOLOGY_LEVEL_RESET_TO_REMOTE: RecoverOntologyLevel
RECOVER_ONTOLOGY_LEVEL_RECLONE: RecoverOntologyLevel
ONTOLOGY_SYNC_RUN_STATUS_UNSPECIFIED: OntologySyncRunStatus
ONTOLOGY_SYNC_RUN_STATUS_IN_PROGRESS: OntologySyncRunStatus
ONTOLOGY_SYNC_RUN_STATUS_SUCCEEDED: OntologySyncRunStatus
ONTOLOGY_SYNC_RUN_STATUS_FAILED: OntologySyncRunStatus
ONTOLOGY_SYNC_RUN_STATUS_CONFLICTS: OntologySyncRunStatus
ORDER_BY_UNKNOWN: UsageOrderBy
ORDER_BY_MOST_RECENTLY_USED: UsageOrderBy
ORDER_BY_LEAST_RECENTLY_USED: UsageOrderBy
ORDER_BY_MOST_FREQUENTLY_USED: UsageOrderBy
ORDER_BY_LEAST_FREQUENTLY_USED: UsageOrderBy

class Skill(_message.Message):
    __slots__ = ('trigger', 'name', 'description', 'path')
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    trigger: str
    name: str
    description: str
    path: str

    def __init__(self, trigger: _Optional[str]=..., name: _Optional[str]=..., description: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class ListSkillsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListSkillsResponse(_message.Message):
    __slots__ = ('skills',)
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    skills: _containers.RepeatedCompositeFieldContainer[Skill]

    def __init__(self, skills: _Optional[_Iterable[_Union[Skill, _Mapping]]]=...) -> None:
        ...

class PatchLine(_message.Message):
    __slots__ = ('op', 'line')
    OP_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    op: PatchLineOp
    line: str

    def __init__(self, op: _Optional[_Union[PatchLineOp, str]]=..., line: _Optional[str]=...) -> None:
        ...

class PatchHunk(_message.Message):
    __slots__ = ('comment', 'old_position', 'old_lines', 'new_position', 'new_lines', 'lines_added', 'lines_deleted', 'leading_context', 'trailing_context', 'lines')
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    OLD_POSITION_FIELD_NUMBER: _ClassVar[int]
    OLD_LINES_FIELD_NUMBER: _ClassVar[int]
    NEW_POSITION_FIELD_NUMBER: _ClassVar[int]
    NEW_LINES_FIELD_NUMBER: _ClassVar[int]
    LINES_ADDED_FIELD_NUMBER: _ClassVar[int]
    LINES_DELETED_FIELD_NUMBER: _ClassVar[int]
    LEADING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TRAILING_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    comment: str
    old_position: int
    old_lines: int
    new_position: int
    new_lines: int
    lines_added: int
    lines_deleted: int
    leading_context: int
    trailing_context: int
    lines: _containers.RepeatedCompositeFieldContainer[PatchLine]

    def __init__(self, comment: _Optional[str]=..., old_position: _Optional[int]=..., old_lines: _Optional[int]=..., new_position: _Optional[int]=..., new_lines: _Optional[int]=..., lines_added: _Optional[int]=..., lines_deleted: _Optional[int]=..., leading_context: _Optional[int]=..., trailing_context: _Optional[int]=..., lines: _Optional[_Iterable[_Union[PatchLine, _Mapping]]]=...) -> None:
        ...

class PatchDiff(_message.Message):
    __slots__ = ('name', 'old_path', 'new_path', 'hunks', 'additions', 'deletions', 'is_binary', 'is_new', 'is_copy', 'is_rename', 'is_delete', 'old_content', 'new_content')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OLD_PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    HUNKS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    DELETIONS_FIELD_NUMBER: _ClassVar[int]
    IS_BINARY_FIELD_NUMBER: _ClassVar[int]
    IS_NEW_FIELD_NUMBER: _ClassVar[int]
    IS_COPY_FIELD_NUMBER: _ClassVar[int]
    IS_RENAME_FIELD_NUMBER: _ClassVar[int]
    IS_DELETE_FIELD_NUMBER: _ClassVar[int]
    OLD_CONTENT_FIELD_NUMBER: _ClassVar[int]
    NEW_CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    old_path: str
    new_path: str
    hunks: _containers.RepeatedCompositeFieldContainer[PatchHunk]
    additions: int
    deletions: int
    is_binary: bool
    is_new: bool
    is_copy: bool
    is_rename: bool
    is_delete: bool
    old_content: str
    new_content: str

    def __init__(self, name: _Optional[str]=..., old_path: _Optional[str]=..., new_path: _Optional[str]=..., hunks: _Optional[_Iterable[_Union[PatchHunk, _Mapping]]]=..., additions: _Optional[int]=..., deletions: _Optional[int]=..., is_binary: bool=..., is_new: bool=..., is_copy: bool=..., is_rename: bool=..., is_delete: bool=..., old_content: _Optional[str]=..., new_content: _Optional[str]=...) -> None:
        ...

class Patch(_message.Message):
    __slots__ = ('id', 'number', 'author_id', 'title', 'description', 'chat_id', 'ai_generated', 'diffs', 'status', 'git_ref', 'revision', 'head_at_merge', 'reviewer_id', 'created_at', 'updated_at', 'author_email', 'author_name', 'approval_count', 'required_approvals', 'capabilities', 'code_owner_status', 'requested_reviewer_member_ids')
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    AI_GENERATED_FIELD_NUMBER: _ClassVar[int]
    DIFFS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    GIT_REF_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    HEAD_AT_MERGE_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    CODE_OWNER_STATUS_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_REVIEWER_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: int
    author_id: str
    title: str
    description: str
    chat_id: str
    ai_generated: bool
    diffs: _containers.RepeatedCompositeFieldContainer[PatchDiff]
    status: PatchStatus
    git_ref: str
    revision: int
    head_at_merge: str
    reviewer_id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    author_email: str
    author_name: str
    approval_count: int
    required_approvals: int
    capabilities: PatchCapabilities
    code_owner_status: _containers.RepeatedCompositeFieldContainer[PatchCodeownerStatus]
    requested_reviewer_member_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, id: _Optional[str]=..., number: _Optional[int]=..., author_id: _Optional[str]=..., title: _Optional[str]=..., description: _Optional[str]=..., chat_id: _Optional[str]=..., ai_generated: bool=..., diffs: _Optional[_Iterable[_Union[PatchDiff, _Mapping]]]=..., status: _Optional[_Union[PatchStatus, str]]=..., git_ref: _Optional[str]=..., revision: _Optional[int]=..., head_at_merge: _Optional[str]=..., reviewer_id: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., author_email: _Optional[str]=..., author_name: _Optional[str]=..., approval_count: _Optional[int]=..., required_approvals: _Optional[int]=..., capabilities: _Optional[_Union[PatchCapabilities, _Mapping]]=..., code_owner_status: _Optional[_Iterable[_Union[PatchCodeownerStatus, _Mapping]]]=..., requested_reviewer_member_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class PatchCodeownerStatus(_message.Message):
    __slots__ = ('pattern', 'owner_member_ids', 'require_approvals', 'approval_count', 'satisfied')
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    OWNER_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    SATISFIED_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    owner_member_ids: _containers.RepeatedScalarFieldContainer[str]
    require_approvals: int
    approval_count: int
    satisfied: bool

    def __init__(self, pattern: _Optional[str]=..., owner_member_ids: _Optional[_Iterable[str]]=..., require_approvals: _Optional[int]=..., approval_count: _Optional[int]=..., satisfied: bool=...) -> None:
        ...

class PatchCapabilities(_message.Message):
    __slots__ = ('can_approve', 'can_deny', 'can_restore', 'caller_approved', 'approve_requires_admin')
    CAN_APPROVE_FIELD_NUMBER: _ClassVar[int]
    CAN_DENY_FIELD_NUMBER: _ClassVar[int]
    CAN_RESTORE_FIELD_NUMBER: _ClassVar[int]
    CALLER_APPROVED_FIELD_NUMBER: _ClassVar[int]
    APPROVE_REQUIRES_ADMIN_FIELD_NUMBER: _ClassVar[int]
    can_approve: bool
    can_deny: bool
    can_restore: bool
    caller_approved: bool
    approve_requires_admin: bool

    def __init__(self, can_approve: bool=..., can_deny: bool=..., can_restore: bool=..., caller_approved: bool=..., approve_requires_admin: bool=...) -> None:
        ...

class ListPatchesRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'statuses', 'include_auto_approved')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STATUSES_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_AUTO_APPROVED_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    statuses: _containers.RepeatedScalarFieldContainer[PatchStatus]
    include_auto_approved: bool

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., statuses: _Optional[_Iterable[_Union[PatchStatus, str]]]=..., include_auto_approved: bool=...) -> None:
        ...

class PatchStatusCounts(_message.Message):
    __slots__ = ('open', 'draft_mine', 'approved', 'denied', 'open_mine')
    OPEN_FIELD_NUMBER: _ClassVar[int]
    DRAFT_MINE_FIELD_NUMBER: _ClassVar[int]
    APPROVED_FIELD_NUMBER: _ClassVar[int]
    DENIED_FIELD_NUMBER: _ClassVar[int]
    OPEN_MINE_FIELD_NUMBER: _ClassVar[int]
    open: int
    draft_mine: int
    approved: int
    denied: int
    open_mine: int

    def __init__(self, open: _Optional[int]=..., draft_mine: _Optional[int]=..., approved: _Optional[int]=..., denied: _Optional[int]=..., open_mine: _Optional[int]=...) -> None:
        ...

class ListPatchesResponse(_message.Message):
    __slots__ = ('patches', 'next_page_token', 'counts')
    PATCHES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    COUNTS_FIELD_NUMBER: _ClassVar[int]
    patches: _containers.RepeatedCompositeFieldContainer[Patch]
    next_page_token: str
    counts: PatchStatusCounts

    def __init__(self, patches: _Optional[_Iterable[_Union[Patch, _Mapping]]]=..., next_page_token: _Optional[str]=..., counts: _Optional[_Union[PatchStatusCounts, _Mapping]]=...) -> None:
        ...

class ApprovePatchRequest(_message.Message):
    __slots__ = ('patch_id', 'expected_git_ref')
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_GIT_REF_FIELD_NUMBER: _ClassVar[int]
    patch_id: str
    expected_git_ref: str

    def __init__(self, patch_id: _Optional[str]=..., expected_git_ref: _Optional[str]=...) -> None:
        ...

class ApprovePatchResponse(_message.Message):
    __slots__ = ('merged', 'approval_count', 'required_approvals', 'already_approved')
    MERGED_FIELD_NUMBER: _ClassVar[int]
    APPROVAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    ALREADY_APPROVED_FIELD_NUMBER: _ClassVar[int]
    merged: bool
    approval_count: int
    required_approvals: int
    already_approved: bool

    def __init__(self, merged: bool=..., approval_count: _Optional[int]=..., required_approvals: _Optional[int]=..., already_approved: bool=...) -> None:
        ...

class RequestPatchReviewRequest(_message.Message):
    __slots__ = ('patch_id', 'reviewer_member_id')
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEWER_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    patch_id: str
    reviewer_member_id: str

    def __init__(self, patch_id: _Optional[str]=..., reviewer_member_id: _Optional[str]=...) -> None:
        ...

class RequestPatchReviewResponse(_message.Message):
    __slots__ = ('sent',)
    SENT_FIELD_NUMBER: _ClassVar[int]
    sent: bool

    def __init__(self, sent: bool=...) -> None:
        ...

class ListPatchReviewersRequest(_message.Message):
    __slots__ = ('patch_id',)
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    patch_id: str

    def __init__(self, patch_id: _Optional[str]=...) -> None:
        ...

class PatchReviewer(_message.Message):
    __slots__ = ('member_id', 'name', 'email', 'profile_image_url', 'is_admin', 'is_code_owner')
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PROFILE_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    IS_CODE_OWNER_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    name: str
    email: str
    profile_image_url: str
    is_admin: bool
    is_code_owner: bool

    def __init__(self, member_id: _Optional[str]=..., name: _Optional[str]=..., email: _Optional[str]=..., profile_image_url: _Optional[str]=..., is_admin: bool=..., is_code_owner: bool=...) -> None:
        ...

class ListPatchReviewersResponse(_message.Message):
    __slots__ = ('reviewers',)
    REVIEWERS_FIELD_NUMBER: _ClassVar[int]
    reviewers: _containers.RepeatedCompositeFieldContainer[PatchReviewer]

    def __init__(self, reviewers: _Optional[_Iterable[_Union[PatchReviewer, _Mapping]]]=...) -> None:
        ...

class DenyPatchRequest(_message.Message):
    __slots__ = ('patch_id', 'expected_git_ref')
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_GIT_REF_FIELD_NUMBER: _ClassVar[int]
    patch_id: str
    expected_git_ref: str

    def __init__(self, patch_id: _Optional[str]=..., expected_git_ref: _Optional[str]=...) -> None:
        ...

class RestorePatchRequest(_message.Message):
    __slots__ = ('patch_id', 'expected_git_ref')
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_GIT_REF_FIELD_NUMBER: _ClassVar[int]
    patch_id: str
    expected_git_ref: str

    def __init__(self, patch_id: _Optional[str]=..., expected_git_ref: _Optional[str]=...) -> None:
        ...

class RevertPatchRequest(_message.Message):
    __slots__ = ('patch_id',)
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    patch_id: str

    def __init__(self, patch_id: _Optional[str]=...) -> None:
        ...

class RevertPatchResponse(_message.Message):
    __slots__ = ('revert_patch',)
    REVERT_PATCH_FIELD_NUMBER: _ClassVar[int]
    revert_patch: Patch

    def __init__(self, revert_patch: _Optional[_Union[Patch, _Mapping]]=...) -> None:
        ...

class SaveObjectAsConfigRequest(_message.Message):
    __slots__ = ('object_type', 'object_id')
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    object_type: str
    object_id: str

    def __init__(self, object_type: _Optional[str]=..., object_id: _Optional[str]=...) -> None:
        ...

class SaveObjectAsConfigResponse(_message.Message):
    __slots__ = ('patch', 'file_path')
    PATCH_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    patch: Patch
    file_path: str

    def __init__(self, patch: _Optional[_Union[Patch, _Mapping]]=..., file_path: _Optional[str]=...) -> None:
        ...

class SaveAllObjectsAsConfigRequest(_message.Message):
    __slots__ = ('object_type',)
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    object_type: str

    def __init__(self, object_type: _Optional[str]=...) -> None:
        ...

class SaveAllObjectsAsConfigResponse(_message.Message):
    __slots__ = ('patch', 'file_paths', 'skipped', 'already_managed_count')
    PATCH_FIELD_NUMBER: _ClassVar[int]
    FILE_PATHS_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    ALREADY_MANAGED_COUNT_FIELD_NUMBER: _ClassVar[int]
    patch: Patch
    file_paths: _containers.RepeatedScalarFieldContainer[str]
    skipped: _containers.RepeatedCompositeFieldContainer[SkippedConfigExport]
    already_managed_count: int

    def __init__(self, patch: _Optional[_Union[Patch, _Mapping]]=..., file_paths: _Optional[_Iterable[str]]=..., skipped: _Optional[_Iterable[_Union[SkippedConfigExport, _Mapping]]]=..., already_managed_count: _Optional[int]=...) -> None:
        ...

class SkippedConfigExport(_message.Message):
    __slots__ = ('object_id', 'object_name', 'reason')
    OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    object_id: str
    object_name: str
    reason: str

    def __init__(self, object_id: _Optional[str]=..., object_name: _Optional[str]=..., reason: _Optional[str]=...) -> None:
        ...

class GetConfigExportCapabilitiesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetConfigExportCapabilitiesResponse(_message.Message):
    __slots__ = ('object_types', 'can_create_patches')
    OBJECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    CAN_CREATE_PATCHES_FIELD_NUMBER: _ClassVar[int]
    object_types: _containers.RepeatedScalarFieldContainer[str]
    can_create_patches: bool

    def __init__(self, object_types: _Optional[_Iterable[str]]=..., can_create_patches: bool=...) -> None:
        ...

class GetPatchRequest(_message.Message):
    __slots__ = ('patch_id', 'revision')
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    patch_id: str
    revision: int

    def __init__(self, patch_id: _Optional[str]=..., revision: _Optional[int]=...) -> None:
        ...

class GetPatchByNumberRequest(_message.Message):
    __slots__ = ('number',)
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int

    def __init__(self, number: _Optional[int]=...) -> None:
        ...

class GetRawPatchRequest(_message.Message):
    __slots__ = ('patch_number',)
    PATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    patch_number: int

    def __init__(self, patch_number: _Optional[int]=...) -> None:
        ...

class GetRawPatchResponse(_message.Message):
    __slots__ = ('raw_patch',)
    RAW_PATCH_FIELD_NUMBER: _ClassVar[int]
    raw_patch: str

    def __init__(self, raw_patch: _Optional[str]=...) -> None:
        ...

class ValidateConfigRequest(_message.Message):
    __slots__ = ('patch_id',)
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    patch_id: str

    def __init__(self, patch_id: _Optional[str]=...) -> None:
        ...

class ConfigDiagnostic(_message.Message):
    __slots__ = ('path', 'message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    path: str
    message: str

    def __init__(self, path: _Optional[str]=..., message: _Optional[str]=..., **kwargs) -> None:
        ...

class ValidateConfigResponse(_message.Message):
    __slots__ = ('ok', 'diagnostics')
    OK_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTICS_FIELD_NUMBER: _ClassVar[int]
    ok: bool
    diagnostics: _containers.RepeatedCompositeFieldContainer[ConfigDiagnostic]

    def __init__(self, ok: bool=..., diagnostics: _Optional[_Iterable[_Union[ConfigDiagnostic, _Mapping]]]=...) -> None:
        ...

class GetPatchCapabilitiesRequest(_message.Message):
    __slots__ = ('patch_id',)
    PATCH_ID_FIELD_NUMBER: _ClassVar[int]
    patch_id: str

    def __init__(self, patch_id: _Optional[str]=...) -> None:
        ...

class GetPatchCapabilitiesResponse(_message.Message):
    __slots__ = ('capabilities', 'status')
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    capabilities: PatchCapabilities
    status: PatchStatus

    def __init__(self, capabilities: _Optional[_Union[PatchCapabilities, _Mapping]]=..., status: _Optional[_Union[PatchStatus, str]]=...) -> None:
        ...

class OntologyEntry(_message.Message):
    __slots__ = ('path', 'name', 'is_dir', 'size_bytes', 'updated_at', 'can_write', 'can_read', 'config_sync_status', 'config_object_id', 'config_sync_error')
    PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DIR_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CAN_WRITE_FIELD_NUMBER: _ClassVar[int]
    CAN_READ_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SYNC_STATUS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIG_SYNC_ERROR_FIELD_NUMBER: _ClassVar[int]
    path: str
    name: str
    is_dir: bool
    size_bytes: int
    updated_at: _timestamp_pb2.Timestamp
    can_write: bool
    can_read: bool
    config_sync_status: _config_source_pb2.ConfigSyncStatus
    config_object_id: str
    config_sync_error: str

    def __init__(self, path: _Optional[str]=..., name: _Optional[str]=..., is_dir: bool=..., size_bytes: _Optional[int]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., can_write: bool=..., can_read: bool=..., config_sync_status: _Optional[_Union[_config_source_pb2.ConfigSyncStatus, str]]=..., config_object_id: _Optional[str]=..., config_sync_error: _Optional[str]=...) -> None:
        ...

class OntologyFile(_message.Message):
    __slots__ = ('path', 'name', 'content', 'updated_at', 'can_write', 'kind', 'mime_type', 'size_bytes', 'binary_content')
    PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CAN_WRITE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BINARY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    name: str
    content: str
    updated_at: _timestamp_pb2.Timestamp
    can_write: bool
    kind: OntologyFileKind
    mime_type: str
    size_bytes: int
    binary_content: bytes

    def __init__(self, path: _Optional[str]=..., name: _Optional[str]=..., content: _Optional[str]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., can_write: bool=..., kind: _Optional[_Union[OntologyFileKind, str]]=..., mime_type: _Optional[str]=..., size_bytes: _Optional[int]=..., binary_content: _Optional[bytes]=...) -> None:
        ...

class OntologyHistoryChangedFile(_message.Message):
    __slots__ = ('path', 'previous_path', 'change_type')
    PATH_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PATH_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    path: str
    previous_path: str
    change_type: OntologyHistoryChangeType

    def __init__(self, path: _Optional[str]=..., previous_path: _Optional[str]=..., change_type: _Optional[_Union[OntologyHistoryChangeType, str]]=...) -> None:
        ...

class OntologyHistoryEntry(_message.Message):
    __slots__ = ('commit_id', 'committed_at', 'author_email', 'author_name', 'message', 'changed_files')
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMITTED_AT_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_NAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FILES_FIELD_NUMBER: _ClassVar[int]
    commit_id: str
    committed_at: _timestamp_pb2.Timestamp
    author_email: str
    author_name: str
    message: str
    changed_files: _containers.RepeatedCompositeFieldContainer[OntologyHistoryChangedFile]

    def __init__(self, commit_id: _Optional[str]=..., committed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., author_email: _Optional[str]=..., author_name: _Optional[str]=..., message: _Optional[str]=..., changed_files: _Optional[_Iterable[_Union[OntologyHistoryChangedFile, _Mapping]]]=...) -> None:
        ...

class AutoAttachEntry(_message.Message):
    __slots__ = ('path', 'connector_id', 'api_connector_ids', 'role_ids', 'connector_ids', 'match_no_connector', 'match_no_api_connector', 'match_all')
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    API_CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    CONNECTOR_IDS_FIELD_NUMBER: _ClassVar[int]
    MATCH_NO_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    MATCH_NO_API_CONNECTOR_FIELD_NUMBER: _ClassVar[int]
    MATCH_ALL_FIELD_NUMBER: _ClassVar[int]
    path: str
    connector_id: int
    api_connector_ids: _containers.RepeatedScalarFieldContainer[str]
    role_ids: _containers.RepeatedScalarFieldContainer[str]
    connector_ids: _containers.RepeatedScalarFieldContainer[int]
    match_no_connector: bool
    match_no_api_connector: bool
    match_all: bool

    def __init__(self, path: _Optional[str]=..., connector_id: _Optional[int]=..., api_connector_ids: _Optional[_Iterable[str]]=..., role_ids: _Optional[_Iterable[str]]=..., connector_ids: _Optional[_Iterable[int]]=..., match_no_connector: bool=..., match_no_api_connector: bool=..., match_all: bool=...) -> None:
        ...

class CodeownerEntry(_message.Message):
    __slots__ = ('pattern', 'owner_member_ids', 'area')
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    OWNER_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    AREA_FIELD_NUMBER: _ClassVar[int]
    pattern: str
    owner_member_ids: _containers.RepeatedScalarFieldContainer[str]
    area: str

    def __init__(self, pattern: _Optional[str]=..., owner_member_ids: _Optional[_Iterable[str]]=..., area: _Optional[str]=...) -> None:
        ...

class GoldenEntry(_message.Message):
    __slots__ = ('path', 'set_by_member_id', 'set_at')
    PATH_FIELD_NUMBER: _ClassVar[int]
    SET_BY_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    SET_AT_FIELD_NUMBER: _ClassVar[int]
    path: str
    set_by_member_id: str
    set_at: _timestamp_pb2.Timestamp

    def __init__(self, path: _Optional[str]=..., set_by_member_id: _Optional[str]=..., set_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class SetOntologyFileGoldenRequest(_message.Message):
    __slots__ = ('path', 'golden')
    PATH_FIELD_NUMBER: _ClassVar[int]
    GOLDEN_FIELD_NUMBER: _ClassVar[int]
    path: str
    golden: bool

    def __init__(self, path: _Optional[str]=..., golden: bool=...) -> None:
        ...

class SetOntologyFileGoldenResponse(_message.Message):
    __slots__ = ('golden',)
    GOLDEN_FIELD_NUMBER: _ClassVar[int]
    golden: _containers.RepeatedCompositeFieldContainer[GoldenEntry]

    def __init__(self, golden: _Optional[_Iterable[_Union[GoldenEntry, _Mapping]]]=...) -> None:
        ...

class ListGoldenFilesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListGoldenFilesResponse(_message.Message):
    __slots__ = ('golden',)
    GOLDEN_FIELD_NUMBER: _ClassVar[int]
    golden: _containers.RepeatedCompositeFieldContainer[GoldenEntry]

    def __init__(self, golden: _Optional[_Iterable[_Union[GoldenEntry, _Mapping]]]=...) -> None:
        ...

class OntologyAnaConfig(_message.Message):
    __slots__ = ('path', 'auto_attach', 'can_write', 'updated_at', 'codeowners')
    PATH_FIELD_NUMBER: _ClassVar[int]
    AUTO_ATTACH_FIELD_NUMBER: _ClassVar[int]
    CAN_WRITE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CODEOWNERS_FIELD_NUMBER: _ClassVar[int]
    path: str
    auto_attach: _containers.RepeatedCompositeFieldContainer[AutoAttachEntry]
    can_write: bool
    updated_at: _timestamp_pb2.Timestamp
    codeowners: _containers.RepeatedCompositeFieldContainer[CodeownerEntry]

    def __init__(self, path: _Optional[str]=..., auto_attach: _Optional[_Iterable[_Union[AutoAttachEntry, _Mapping]]]=..., can_write: bool=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., codeowners: _Optional[_Iterable[_Union[CodeownerEntry, _Mapping]]]=...) -> None:
        ...

class GetOntologyAnaConfigRequest(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class GetOntologyAnaConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: OntologyAnaConfig

    def __init__(self, config: _Optional[_Union[OntologyAnaConfig, _Mapping]]=...) -> None:
        ...

class UpsertOntologyAnaConfigRequest(_message.Message):
    __slots__ = ('path', 'auto_attach', 'commit_message', 'codeowners')
    PATH_FIELD_NUMBER: _ClassVar[int]
    AUTO_ATTACH_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CODEOWNERS_FIELD_NUMBER: _ClassVar[int]
    path: str
    auto_attach: _containers.RepeatedCompositeFieldContainer[AutoAttachEntry]
    commit_message: str
    codeowners: _containers.RepeatedCompositeFieldContainer[CodeownerEntry]

    def __init__(self, path: _Optional[str]=..., auto_attach: _Optional[_Iterable[_Union[AutoAttachEntry, _Mapping]]]=..., commit_message: _Optional[str]=..., codeowners: _Optional[_Iterable[_Union[CodeownerEntry, _Mapping]]]=...) -> None:
        ...

class UpsertOntologyAnaConfigResponse(_message.Message):
    __slots__ = ('config',)
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    config: OntologyAnaConfig

    def __init__(self, config: _Optional[_Union[OntologyAnaConfig, _Mapping]]=...) -> None:
        ...

class GetCodeownerCoverageRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetCodeownerCoverageResponse(_message.Message):
    __slots__ = ('total_files', 'covered_files', 'coverage_pct', 'uncovered_files')
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    COVERED_FILES_FIELD_NUMBER: _ClassVar[int]
    COVERAGE_PCT_FIELD_NUMBER: _ClassVar[int]
    UNCOVERED_FILES_FIELD_NUMBER: _ClassVar[int]
    total_files: int
    covered_files: int
    coverage_pct: float
    uncovered_files: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, total_files: _Optional[int]=..., covered_files: _Optional[int]=..., coverage_pct: _Optional[float]=..., uncovered_files: _Optional[_Iterable[str]]=...) -> None:
        ...

class OntologyOwnerEntry(_message.Message):
    __slots__ = ('role_id', 'permission')
    ROLE_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    role_id: str
    permission: OntologyPermission

    def __init__(self, role_id: _Optional[str]=..., permission: _Optional[_Union[OntologyPermission, str]]=...) -> None:
        ...

class OntologyOwners(_message.Message):
    __slots__ = ('path', 'entries', 'can_write', 'updated_at')
    PATH_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    CAN_WRITE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    path: str
    entries: _containers.RepeatedCompositeFieldContainer[OntologyOwnerEntry]
    can_write: bool
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, path: _Optional[str]=..., entries: _Optional[_Iterable[_Union[OntologyOwnerEntry, _Mapping]]]=..., can_write: bool=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListOntologyEntriesRequest(_message.Message):
    __slots__ = ('path', 'recursive', 'include_debug_files')
    PATH_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_DEBUG_FILES_FIELD_NUMBER: _ClassVar[int]
    path: str
    recursive: bool
    include_debug_files: bool

    def __init__(self, path: _Optional[str]=..., recursive: bool=..., include_debug_files: bool=...) -> None:
        ...

class ListOntologyEntriesResponse(_message.Message):
    __slots__ = ('entries',)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[OntologyEntry]

    def __init__(self, entries: _Optional[_Iterable[_Union[OntologyEntry, _Mapping]]]=...) -> None:
        ...

class GetOntologyFileRequest(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class GetOntologyFileResponse(_message.Message):
    __slots__ = ('file',)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: OntologyFile

    def __init__(self, file: _Optional[_Union[OntologyFile, _Mapping]]=...) -> None:
        ...

class CreateOntologyFileUploadUrlRequest(_message.Message):
    __slots__ = ('path', 'mime_type', 'size_bytes')
    PATH_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    path: str
    mime_type: str
    size_bytes: int

    def __init__(self, path: _Optional[str]=..., mime_type: _Optional[str]=..., size_bytes: _Optional[int]=...) -> None:
        ...

class CreateOntologyFileUploadUrlResponse(_message.Message):
    __slots__ = ('upload_url', 'upload_key')
    UPLOAD_URL_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_KEY_FIELD_NUMBER: _ClassVar[int]
    upload_url: str
    upload_key: str

    def __init__(self, upload_url: _Optional[str]=..., upload_key: _Optional[str]=...) -> None:
        ...

class FinalizeOntologyFileUploadRequest(_message.Message):
    __slots__ = ('path', 'upload_key', 'commit_message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_KEY_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    upload_key: str
    commit_message: str

    def __init__(self, path: _Optional[str]=..., upload_key: _Optional[str]=..., commit_message: _Optional[str]=...) -> None:
        ...

class FinalizeOntologyFileUploadResponse(_message.Message):
    __slots__ = ('file',)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: OntologyFile

    def __init__(self, file: _Optional[_Union[OntologyFile, _Mapping]]=...) -> None:
        ...

class ListOntologyHistoryRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'path')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    path: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class ListOntologyHistoryResponse(_message.Message):
    __slots__ = ('history', 'next_page_token')
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[OntologyHistoryEntry]
    next_page_token: str

    def __init__(self, history: _Optional[_Iterable[_Union[OntologyHistoryEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetOntologyHistoryFileDiffRequest(_message.Message):
    __slots__ = ('commit_id', 'path')
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    commit_id: str
    path: str

    def __init__(self, commit_id: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class GetOntologyHistoryFileDiffResponse(_message.Message):
    __slots__ = ('commit_id', 'path', 'previous_path', 'change_type', 'before_content', 'after_content', 'is_binary')
    COMMIT_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PATH_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BEFORE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    AFTER_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_BINARY_FIELD_NUMBER: _ClassVar[int]
    commit_id: str
    path: str
    previous_path: str
    change_type: OntologyHistoryChangeType
    before_content: str
    after_content: str
    is_binary: bool

    def __init__(self, commit_id: _Optional[str]=..., path: _Optional[str]=..., previous_path: _Optional[str]=..., change_type: _Optional[_Union[OntologyHistoryChangeType, str]]=..., before_content: _Optional[str]=..., after_content: _Optional[str]=..., is_binary: bool=...) -> None:
        ...

class UpsertOntologyFileRequest(_message.Message):
    __slots__ = ('path', 'content', 'commit_message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: str
    commit_message: str

    def __init__(self, path: _Optional[str]=..., content: _Optional[str]=..., commit_message: _Optional[str]=...) -> None:
        ...

class UpsertOntologyFileResponse(_message.Message):
    __slots__ = ('file',)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: OntologyFile

    def __init__(self, file: _Optional[_Union[OntologyFile, _Mapping]]=...) -> None:
        ...

class CreateOntologyDirectoryRequest(_message.Message):
    __slots__ = ('path', 'commit_message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    commit_message: str

    def __init__(self, path: _Optional[str]=..., commit_message: _Optional[str]=...) -> None:
        ...

class CreateOntologyDirectoryResponse(_message.Message):
    __slots__ = ('entry',)
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: OntologyEntry

    def __init__(self, entry: _Optional[_Union[OntologyEntry, _Mapping]]=...) -> None:
        ...

class DeleteOntologyDirectoryRequest(_message.Message):
    __slots__ = ('path', 'commit_message', 'recursive')
    PATH_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    path: str
    commit_message: str
    recursive: bool

    def __init__(self, path: _Optional[str]=..., commit_message: _Optional[str]=..., recursive: bool=...) -> None:
        ...

class RenameOntologyFileRequest(_message.Message):
    __slots__ = ('old_path', 'new_path', 'commit_message')
    OLD_PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    old_path: str
    new_path: str
    commit_message: str

    def __init__(self, old_path: _Optional[str]=..., new_path: _Optional[str]=..., commit_message: _Optional[str]=...) -> None:
        ...

class RenameOntologyFileResponse(_message.Message):
    __slots__ = ('file',)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: OntologyFile

    def __init__(self, file: _Optional[_Union[OntologyFile, _Mapping]]=...) -> None:
        ...

class DeleteOntologyFileRequest(_message.Message):
    __slots__ = ('path', 'commit_message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    commit_message: str

    def __init__(self, path: _Optional[str]=..., commit_message: _Optional[str]=...) -> None:
        ...

class GetOntologyOwnersRequest(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class GetOntologyOwnersResponse(_message.Message):
    __slots__ = ('owners',)
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    owners: OntologyOwners

    def __init__(self, owners: _Optional[_Union[OntologyOwners, _Mapping]]=...) -> None:
        ...

class GetEffectiveOntologyOwnersRequest(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class GetEffectiveOntologyOwnersResponse(_message.Message):
    __slots__ = ('path', 'entries')
    PATH_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    path: str
    entries: _containers.RepeatedCompositeFieldContainer[OntologyOwnerEntry]

    def __init__(self, path: _Optional[str]=..., entries: _Optional[_Iterable[_Union[OntologyOwnerEntry, _Mapping]]]=...) -> None:
        ...

class UpsertOntologyOwnersRequest(_message.Message):
    __slots__ = ('path', 'role_ids', 'permissions', 'commit_message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    role_ids: _containers.RepeatedScalarFieldContainer[str]
    permissions: _containers.RepeatedScalarFieldContainer[OntologyPermission]
    commit_message: str

    def __init__(self, path: _Optional[str]=..., role_ids: _Optional[_Iterable[str]]=..., permissions: _Optional[_Iterable[_Union[OntologyPermission, str]]]=..., commit_message: _Optional[str]=...) -> None:
        ...

class UpsertOntologyOwnersResponse(_message.Message):
    __slots__ = ('owners',)
    OWNERS_FIELD_NUMBER: _ClassVar[int]
    owners: OntologyOwners

    def __init__(self, owners: _Optional[_Union[OntologyOwners, _Mapping]]=...) -> None:
        ...

class DeleteOntologyOwnersRequest(_message.Message):
    __slots__ = ('path', 'role_ids', 'commit_message')
    PATH_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    path: str
    role_ids: _containers.RepeatedScalarFieldContainer[str]
    commit_message: str

    def __init__(self, path: _Optional[str]=..., role_ids: _Optional[_Iterable[str]]=..., commit_message: _Optional[str]=...) -> None:
        ...

class OntologyRemote(_message.Message):
    __slots__ = ('id', 'remote_url', 'auth_type', 'default_branch', 'created_at', 'updated_at', 'sync_enabled', 'sync_interval_minutes', 'last_synced_at', 'last_sync_error', 'signing_key_type', 'github_app_id', 'github_app_installation_id', 'has_conflicts', 'push_mode')
    ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SYNC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SYNC_INTERVAL_MINUTES_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNCED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_SYNC_ERROR_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    GITHUB_APP_ID_FIELD_NUMBER: _ClassVar[int]
    GITHUB_APP_INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    PUSH_MODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    remote_url: str
    auth_type: str
    default_branch: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    sync_enabled: bool
    sync_interval_minutes: int
    last_synced_at: _timestamp_pb2.Timestamp
    last_sync_error: str
    signing_key_type: str
    github_app_id: str
    github_app_installation_id: str
    has_conflicts: bool
    push_mode: str

    def __init__(self, id: _Optional[str]=..., remote_url: _Optional[str]=..., auth_type: _Optional[str]=..., default_branch: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., sync_enabled: bool=..., sync_interval_minutes: _Optional[int]=..., last_synced_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_sync_error: _Optional[str]=..., signing_key_type: _Optional[str]=..., github_app_id: _Optional[str]=..., github_app_installation_id: _Optional[str]=..., has_conflicts: bool=..., push_mode: _Optional[str]=...) -> None:
        ...

class GetOntologyRemoteRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetOntologyRemoteResponse(_message.Message):
    __slots__ = ('remote', 'hosted_github_app_available', 'hosted_github_app_slug')
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    HOSTED_GITHUB_APP_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    HOSTED_GITHUB_APP_SLUG_FIELD_NUMBER: _ClassVar[int]
    remote: OntologyRemote
    hosted_github_app_available: bool
    hosted_github_app_slug: str

    def __init__(self, remote: _Optional[_Union[OntologyRemote, _Mapping]]=..., hosted_github_app_available: bool=..., hosted_github_app_slug: _Optional[str]=...) -> None:
        ...

class ConfigureOntologyRemoteRequest(_message.Message):
    __slots__ = ('remote_url', 'auth_type', 'token', 'ssh_private_key', 'ssh_key_password', 'default_branch', 'github_app_id', 'github_app_installation_id', 'github_app_private_key', 'signing_key_type', 'signing_key', 'push_mode', 'use_hosted_github_app')
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    SSH_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SSH_KEY_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    GITHUB_APP_ID_FIELD_NUMBER: _ClassVar[int]
    GITHUB_APP_INSTALLATION_ID_FIELD_NUMBER: _ClassVar[int]
    GITHUB_APP_PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SIGNING_KEY_FIELD_NUMBER: _ClassVar[int]
    PUSH_MODE_FIELD_NUMBER: _ClassVar[int]
    USE_HOSTED_GITHUB_APP_FIELD_NUMBER: _ClassVar[int]
    remote_url: str
    auth_type: str
    token: str
    ssh_private_key: str
    ssh_key_password: str
    default_branch: str
    github_app_id: str
    github_app_installation_id: str
    github_app_private_key: str
    signing_key_type: str
    signing_key: str
    push_mode: str
    use_hosted_github_app: bool

    def __init__(self, remote_url: _Optional[str]=..., auth_type: _Optional[str]=..., token: _Optional[str]=..., ssh_private_key: _Optional[str]=..., ssh_key_password: _Optional[str]=..., default_branch: _Optional[str]=..., github_app_id: _Optional[str]=..., github_app_installation_id: _Optional[str]=..., github_app_private_key: _Optional[str]=..., signing_key_type: _Optional[str]=..., signing_key: _Optional[str]=..., push_mode: _Optional[str]=..., use_hosted_github_app: bool=...) -> None:
        ...

class ConfigureOntologyRemoteResponse(_message.Message):
    __slots__ = ('remote',)
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    remote: OntologyRemote

    def __init__(self, remote: _Optional[_Union[OntologyRemote, _Mapping]]=...) -> None:
        ...

class GetOntologyGithubOAuthURLRequest(_message.Message):
    __slots__ = ('state', 'code_challenge')
    STATE_FIELD_NUMBER: _ClassVar[int]
    CODE_CHALLENGE_FIELD_NUMBER: _ClassVar[int]
    state: str
    code_challenge: str

    def __init__(self, state: _Optional[str]=..., code_challenge: _Optional[str]=...) -> None:
        ...

class GetOntologyGithubOAuthURLResponse(_message.Message):
    __slots__ = ('authorize_url', 'install_url', 'available')
    AUTHORIZE_URL_FIELD_NUMBER: _ClassVar[int]
    INSTALL_URL_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    authorize_url: str
    install_url: str
    available: bool

    def __init__(self, authorize_url: _Optional[str]=..., install_url: _Optional[str]=..., available: bool=...) -> None:
        ...

class ExchangeOntologyGithubCodeRequest(_message.Message):
    __slots__ = ('code', 'state', 'code_verifier')
    CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CODE_VERIFIER_FIELD_NUMBER: _ClassVar[int]
    code: str
    state: str
    code_verifier: str

    def __init__(self, code: _Optional[str]=..., state: _Optional[str]=..., code_verifier: _Optional[str]=...) -> None:
        ...

class ExchangeOntologyGithubCodeResponse(_message.Message):
    __slots__ = ('success', 'installations')
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    INSTALLATIONS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    installations: _containers.RepeatedCompositeFieldContainer[GithubInstallation]

    def __init__(self, success: bool=..., installations: _Optional[_Iterable[_Union[GithubInstallation, _Mapping]]]=...) -> None:
        ...

class GithubInstallation(_message.Message):
    __slots__ = ('id', 'account', 'repos', 'repos_error')
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    REPOS_FIELD_NUMBER: _ClassVar[int]
    REPOS_ERROR_FIELD_NUMBER: _ClassVar[int]
    id: str
    account: str
    repos: _containers.RepeatedCompositeFieldContainer[GithubInstallationRepo]
    repos_error: str

    def __init__(self, id: _Optional[str]=..., account: _Optional[str]=..., repos: _Optional[_Iterable[_Union[GithubInstallationRepo, _Mapping]]]=..., repos_error: _Optional[str]=...) -> None:
        ...

class GithubInstallationRepo(_message.Message):
    __slots__ = ('full_name', 'clone_url', 'default_branch', 'private')
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    CLONE_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_FIELD_NUMBER: _ClassVar[int]
    full_name: str
    clone_url: str
    default_branch: str
    private: bool

    def __init__(self, full_name: _Optional[str]=..., clone_url: _Optional[str]=..., default_branch: _Optional[str]=..., private: bool=...) -> None:
        ...

class RemoveOntologyRemoteRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PushOntologyToRemoteRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PullOntologyFromRemoteRequest(_message.Message):
    __slots__ = ('acknowledge_unrelated_histories', 'expected_local_head_hash', 'expected_remote_head_hash')
    ACKNOWLEDGE_UNRELATED_HISTORIES_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_LOCAL_HEAD_HASH_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_REMOTE_HEAD_HASH_FIELD_NUMBER: _ClassVar[int]
    acknowledge_unrelated_histories: bool
    expected_local_head_hash: str
    expected_remote_head_hash: str

    def __init__(self, acknowledge_unrelated_histories: bool=..., expected_local_head_hash: _Optional[str]=..., expected_remote_head_hash: _Optional[str]=...) -> None:
        ...

class TriggerConfigDriftReconcileRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TriggerConfigDriftReconcileResponse(_message.Message):
    __slots__ = ('drifted',)
    DRIFTED_FIELD_NUMBER: _ClassVar[int]
    drifted: bool

    def __init__(self, drifted: bool=...) -> None:
        ...

class UnrelatedHistoriesDetail(_message.Message):
    __slots__ = ('local_head_hash', 'remote_head_hash', 'remote_addition_paths', 'conflict_paths')
    LOCAL_HEAD_HASH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HEAD_HASH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDITION_PATHS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_PATHS_FIELD_NUMBER: _ClassVar[int]
    local_head_hash: str
    remote_head_hash: str
    remote_addition_paths: _containers.RepeatedScalarFieldContainer[str]
    conflict_paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, local_head_hash: _Optional[str]=..., remote_head_hash: _Optional[str]=..., remote_addition_paths: _Optional[_Iterable[str]]=..., conflict_paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetOntologyMigrationStatusRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetOntologyMigrationStatusResponse(_message.Message):
    __slots__ = ('pending_legacy_context_count',)
    PENDING_LEGACY_CONTEXT_COUNT_FIELD_NUMBER: _ClassVar[int]
    pending_legacy_context_count: int

    def __init__(self, pending_legacy_context_count: _Optional[int]=...) -> None:
        ...

class PlanOntologyMergeRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PlanOntologyMergeResponse(_message.Message):
    __slots__ = ('outcome', 'local_head_hash', 'remote_head_hash', 'remote_addition_paths', 'conflict_paths')
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    LOCAL_HEAD_HASH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_HEAD_HASH_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ADDITION_PATHS_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_PATHS_FIELD_NUMBER: _ClassVar[int]
    outcome: OntologyMergeOutcome
    local_head_hash: str
    remote_head_hash: str
    remote_addition_paths: _containers.RepeatedScalarFieldContainer[str]
    conflict_paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, outcome: _Optional[_Union[OntologyMergeOutcome, str]]=..., local_head_hash: _Optional[str]=..., remote_head_hash: _Optional[str]=..., remote_addition_paths: _Optional[_Iterable[str]]=..., conflict_paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class PreviewOntologyPullFromRemoteRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RecoverOntologyRequest(_message.Message):
    __slots__ = ('level',)
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: RecoverOntologyLevel

    def __init__(self, level: _Optional[_Union[RecoverOntologyLevel, str]]=...) -> None:
        ...

class PreviewOntologyPullFolderRow(_message.Message):
    __slots__ = ('folder_path', 'file_count')
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    folder_path: str
    file_count: int

    def __init__(self, folder_path: _Optional[str]=..., file_count: _Optional[int]=...) -> None:
        ...

class PreviewOntologyPullFromRemoteResponse(_message.Message):
    __slots__ = ('total_files', 'top_level_folder_count', 'folder_rows', 'unrelated_histories', 'unrelated_histories_remote_additions', 'unrelated_histories_conflict_paths')
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    TOP_LEVEL_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
    FOLDER_ROWS_FIELD_NUMBER: _ClassVar[int]
    UNRELATED_HISTORIES_FIELD_NUMBER: _ClassVar[int]
    UNRELATED_HISTORIES_REMOTE_ADDITIONS_FIELD_NUMBER: _ClassVar[int]
    UNRELATED_HISTORIES_CONFLICT_PATHS_FIELD_NUMBER: _ClassVar[int]
    total_files: int
    top_level_folder_count: int
    folder_rows: _containers.RepeatedCompositeFieldContainer[PreviewOntologyPullFolderRow]
    unrelated_histories: bool
    unrelated_histories_remote_additions: _containers.RepeatedScalarFieldContainer[str]
    unrelated_histories_conflict_paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, total_files: _Optional[int]=..., top_level_folder_count: _Optional[int]=..., folder_rows: _Optional[_Iterable[_Union[PreviewOntologyPullFolderRow, _Mapping]]]=..., unrelated_histories: bool=..., unrelated_histories_remote_additions: _Optional[_Iterable[str]]=..., unrelated_histories_conflict_paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class UpdateOntologySyncConfigRequest(_message.Message):
    __slots__ = ('sync_enabled', 'sync_interval_minutes')
    SYNC_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SYNC_INTERVAL_MINUTES_FIELD_NUMBER: _ClassVar[int]
    sync_enabled: bool
    sync_interval_minutes: int

    def __init__(self, sync_enabled: bool=..., sync_interval_minutes: _Optional[int]=...) -> None:
        ...

class UpdateOntologySyncConfigResponse(_message.Message):
    __slots__ = ('remote',)
    REMOTE_FIELD_NUMBER: _ClassVar[int]
    remote: OntologyRemote

    def __init__(self, remote: _Optional[_Union[OntologyRemote, _Mapping]]=...) -> None:
        ...

class OntologySyncRun(_message.Message):
    __slots__ = ('id', 'remote_id', 'remote_url', 'default_branch', 'source', 'status', 'started_at', 'completed_at', 'error_message', 'conflict_count')
    ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_ID_FIELD_NUMBER: _ClassVar[int]
    REMOTE_URL_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STARTED_AT_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_AT_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CONFLICT_COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    remote_id: str
    remote_url: str
    default_branch: str
    source: str
    status: OntologySyncRunStatus
    started_at: _timestamp_pb2.Timestamp
    completed_at: _timestamp_pb2.Timestamp
    error_message: str
    conflict_count: int

    def __init__(self, id: _Optional[str]=..., remote_id: _Optional[str]=..., remote_url: _Optional[str]=..., default_branch: _Optional[str]=..., source: _Optional[str]=..., status: _Optional[_Union[OntologySyncRunStatus, str]]=..., started_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., completed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., error_message: _Optional[str]=..., conflict_count: _Optional[int]=...) -> None:
        ...

class ListOntologySyncRunsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOntologySyncRunsResponse(_message.Message):
    __slots__ = ('runs', 'next_page_token')
    RUNS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    runs: _containers.RepeatedCompositeFieldContainer[OntologySyncRun]
    next_page_token: str

    def __init__(self, runs: _Optional[_Iterable[_Union[OntologySyncRun, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class OntologySyncConflict(_message.Message):
    __slots__ = ('id', 'file_path', 'ours_content', 'theirs_content', 'base_content', 'created_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OURS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    THEIRS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    BASE_CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    file_path: str
    ours_content: str
    theirs_content: str
    base_content: str
    created_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., file_path: _Optional[str]=..., ours_content: _Optional[str]=..., theirs_content: _Optional[str]=..., base_content: _Optional[str]=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetOntologySyncConflictsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetOntologySyncConflictsResponse(_message.Message):
    __slots__ = ('conflicts',)
    CONFLICTS_FIELD_NUMBER: _ClassVar[int]
    conflicts: _containers.RepeatedCompositeFieldContainer[OntologySyncConflict]

    def __init__(self, conflicts: _Optional[_Iterable[_Union[OntologySyncConflict, _Mapping]]]=...) -> None:
        ...

class ResolveOntologySyncConflictRequest(_message.Message):
    __slots__ = ('conflict_id', 'resolved_content')
    CONFLICT_ID_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    conflict_id: str
    resolved_content: str

    def __init__(self, conflict_id: _Optional[str]=..., resolved_content: _Optional[str]=...) -> None:
        ...

class MigrateLegacyContextToOntologyRequest(_message.Message):
    __slots__ = ('dry_run', 'include_inactive')
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_INACTIVE_FIELD_NUMBER: _ClassVar[int]
    dry_run: bool
    include_inactive: bool

    def __init__(self, dry_run: bool=..., include_inactive: bool=...) -> None:
        ...

class MigratedLegacyContextPrompt(_message.Message):
    __slots__ = ('legacy_context_prompt_id', 'name', 'folder_path', 'file_path', 'created', 'skipped', 'skip_reason', 'is_public', 'auto_attach')
    LEGACY_CONTEXT_PROMPT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_FIELD_NUMBER: _ClassVar[int]
    AUTO_ATTACH_FIELD_NUMBER: _ClassVar[int]
    legacy_context_prompt_id: str
    name: str
    folder_path: str
    file_path: str
    created: bool
    skipped: bool
    skip_reason: str
    is_public: bool
    auto_attach: bool

    def __init__(self, legacy_context_prompt_id: _Optional[str]=..., name: _Optional[str]=..., folder_path: _Optional[str]=..., file_path: _Optional[str]=..., created: bool=..., skipped: bool=..., skip_reason: _Optional[str]=..., is_public: bool=..., auto_attach: bool=...) -> None:
        ...

class MigrateLegacyContextToOntologyResponse(_message.Message):
    __slots__ = ('prompts', 'created_count', 'skipped_count', 'total_legacy_count', 'dry_run')
    PROMPTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LEGACY_COUNT_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    prompts: _containers.RepeatedCompositeFieldContainer[MigratedLegacyContextPrompt]
    created_count: int
    skipped_count: int
    total_legacy_count: int
    dry_run: bool

    def __init__(self, prompts: _Optional[_Iterable[_Union[MigratedLegacyContextPrompt, _Mapping]]]=..., created_count: _Optional[int]=..., skipped_count: _Optional[int]=..., total_legacy_count: _Optional[int]=..., dry_run: bool=...) -> None:
        ...

class MigrateOntologyToOntologyRequest(_message.Message):
    __slots__ = ('ontology_ids', 'dry_run')
    ONTOLOGY_IDS_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    ontology_ids: _containers.RepeatedScalarFieldContainer[int]
    dry_run: bool

    def __init__(self, ontology_ids: _Optional[_Iterable[int]]=..., dry_run: bool=...) -> None:
        ...

class MigratedOntologyNoun(_message.Message):
    __slots__ = ('noun_id', 'noun_name', 'file_path', 'created', 'skipped', 'skip_reason')
    NOUN_ID_FIELD_NUMBER: _ClassVar[int]
    NOUN_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_FIELD_NUMBER: _ClassVar[int]
    SKIP_REASON_FIELD_NUMBER: _ClassVar[int]
    noun_id: str
    noun_name: str
    file_path: str
    created: bool
    skipped: bool
    skip_reason: str

    def __init__(self, noun_id: _Optional[str]=..., noun_name: _Optional[str]=..., file_path: _Optional[str]=..., created: bool=..., skipped: bool=..., skip_reason: _Optional[str]=...) -> None:
        ...

class MigrateOntologyToOntologyResult(_message.Message):
    __slots__ = ('ontology_id', 'ontology_name', 'folder_path', 'nouns', 'created_count', 'skipped_count', 'total_nouns')
    ONTOLOGY_ID_FIELD_NUMBER: _ClassVar[int]
    ONTOLOGY_NAME_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    NOUNS_FIELD_NUMBER: _ClassVar[int]
    CREATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NOUNS_FIELD_NUMBER: _ClassVar[int]
    ontology_id: int
    ontology_name: str
    folder_path: str
    nouns: _containers.RepeatedCompositeFieldContainer[MigratedOntologyNoun]
    created_count: int
    skipped_count: int
    total_nouns: int

    def __init__(self, ontology_id: _Optional[int]=..., ontology_name: _Optional[str]=..., folder_path: _Optional[str]=..., nouns: _Optional[_Iterable[_Union[MigratedOntologyNoun, _Mapping]]]=..., created_count: _Optional[int]=..., skipped_count: _Optional[int]=..., total_nouns: _Optional[int]=...) -> None:
        ...

class MigrateOntologyToOntologyResponse(_message.Message):
    __slots__ = ('results', 'total_created', 'total_skipped', 'dry_run')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CREATED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SKIPPED_FIELD_NUMBER: _ClassVar[int]
    DRY_RUN_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MigrateOntologyToOntologyResult]
    total_created: int
    total_skipped: int
    dry_run: bool

    def __init__(self, results: _Optional[_Iterable[_Union[MigrateOntologyToOntologyResult, _Mapping]]]=..., total_created: _Optional[int]=..., total_skipped: _Optional[int]=..., dry_run: bool=...) -> None:
        ...

class AddOntologySubmoduleRequest(_message.Message):
    __slots__ = ('url', 'path', 'branch')
    URL_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    url: str
    path: str
    branch: str

    def __init__(self, url: _Optional[str]=..., path: _Optional[str]=..., branch: _Optional[str]=...) -> None:
        ...

class AddOntologySubmoduleResponse(_message.Message):
    __slots__ = ('path', 'url', 'branch')
    PATH_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    path: str
    url: str
    branch: str

    def __init__(self, path: _Optional[str]=..., url: _Optional[str]=..., branch: _Optional[str]=...) -> None:
        ...

class RemoveOntologySubmoduleRequest(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class ListOntologySubmodulesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class OntologySubmodule(_message.Message):
    __slots__ = ('name', 'path', 'url', 'branch')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    url: str
    branch: str

    def __init__(self, name: _Optional[str]=..., path: _Optional[str]=..., url: _Optional[str]=..., branch: _Optional[str]=...) -> None:
        ...

class ListOntologySubmodulesResponse(_message.Message):
    __slots__ = ('submodules',)
    SUBMODULES_FIELD_NUMBER: _ClassVar[int]
    submodules: _containers.RepeatedCompositeFieldContainer[OntologySubmodule]

    def __init__(self, submodules: _Optional[_Iterable[_Union[OntologySubmodule, _Mapping]]]=...) -> None:
        ...

class ContextPatchAutoApproveRule(_message.Message):
    __slots__ = ('id', 'directory_path', 'always_auto_approve', 'role_ids', 'agent_ids', 'enabled', 'created_at', 'updated_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_AUTO_APPROVE_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    directory_path: str
    always_auto_approve: bool
    role_ids: _containers.RepeatedScalarFieldContainer[str]
    agent_ids: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., directory_path: _Optional[str]=..., always_auto_approve: bool=..., role_ids: _Optional[_Iterable[str]]=..., agent_ids: _Optional[_Iterable[str]]=..., enabled: bool=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ContextPatchAutoApproveRuleInput(_message.Message):
    __slots__ = ('directory_path', 'always_auto_approve', 'role_ids', 'agent_ids', 'enabled')
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_AUTO_APPROVE_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    AGENT_IDS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    directory_path: str
    always_auto_approve: bool
    role_ids: _containers.RepeatedScalarFieldContainer[str]
    agent_ids: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool

    def __init__(self, directory_path: _Optional[str]=..., always_auto_approve: bool=..., role_ids: _Optional[_Iterable[str]]=..., agent_ids: _Optional[_Iterable[str]]=..., enabled: bool=...) -> None:
        ...

class ListContextPatchAutoApproveRulesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListContextPatchAutoApproveRulesResponse(_message.Message):
    __slots__ = ('rules',)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[ContextPatchAutoApproveRule]

    def __init__(self, rules: _Optional[_Iterable[_Union[ContextPatchAutoApproveRule, _Mapping]]]=...) -> None:
        ...

class CreateContextPatchAutoApproveRuleRequest(_message.Message):
    __slots__ = ('rule',)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: ContextPatchAutoApproveRuleInput

    def __init__(self, rule: _Optional[_Union[ContextPatchAutoApproveRuleInput, _Mapping]]=...) -> None:
        ...

class CreateContextPatchAutoApproveRuleResponse(_message.Message):
    __slots__ = ('rule',)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: ContextPatchAutoApproveRule

    def __init__(self, rule: _Optional[_Union[ContextPatchAutoApproveRule, _Mapping]]=...) -> None:
        ...

class UpdateContextPatchAutoApproveRuleRequest(_message.Message):
    __slots__ = ('id', 'rule')
    ID_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    id: str
    rule: ContextPatchAutoApproveRuleInput

    def __init__(self, id: _Optional[str]=..., rule: _Optional[_Union[ContextPatchAutoApproveRuleInput, _Mapping]]=...) -> None:
        ...

class UpdateContextPatchAutoApproveRuleResponse(_message.Message):
    __slots__ = ('rule',)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: ContextPatchAutoApproveRule

    def __init__(self, rule: _Optional[_Union[ContextPatchAutoApproveRule, _Mapping]]=...) -> None:
        ...

class DeleteContextPatchAutoApproveRuleRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class ApprovalRule(_message.Message):
    __slots__ = ('id', 'directory_path', 'required_approvals', 'role_ids', 'enabled', 'created_at', 'updated_at')
    ID_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    id: str
    directory_path: str
    required_approvals: int
    role_ids: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp

    def __init__(self, id: _Optional[str]=..., directory_path: _Optional[str]=..., required_approvals: _Optional[int]=..., role_ids: _Optional[_Iterable[str]]=..., enabled: bool=..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ApprovalRuleInput(_message.Message):
    __slots__ = ('directory_path', 'required_approvals', 'role_ids', 'enabled')
    DIRECTORY_PATH_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_APPROVALS_FIELD_NUMBER: _ClassVar[int]
    ROLE_IDS_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    directory_path: str
    required_approvals: int
    role_ids: _containers.RepeatedScalarFieldContainer[str]
    enabled: bool

    def __init__(self, directory_path: _Optional[str]=..., required_approvals: _Optional[int]=..., role_ids: _Optional[_Iterable[str]]=..., enabled: bool=...) -> None:
        ...

class ListApprovalRulesRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ListApprovalRulesResponse(_message.Message):
    __slots__ = ('rules',)
    RULES_FIELD_NUMBER: _ClassVar[int]
    rules: _containers.RepeatedCompositeFieldContainer[ApprovalRule]

    def __init__(self, rules: _Optional[_Iterable[_Union[ApprovalRule, _Mapping]]]=...) -> None:
        ...

class CreateApprovalRuleRequest(_message.Message):
    __slots__ = ('rule',)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: ApprovalRuleInput

    def __init__(self, rule: _Optional[_Union[ApprovalRuleInput, _Mapping]]=...) -> None:
        ...

class CreateApprovalRuleResponse(_message.Message):
    __slots__ = ('rule',)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: ApprovalRule

    def __init__(self, rule: _Optional[_Union[ApprovalRule, _Mapping]]=...) -> None:
        ...

class UpdateApprovalRuleRequest(_message.Message):
    __slots__ = ('id', 'rule')
    ID_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    id: str
    rule: ApprovalRuleInput

    def __init__(self, id: _Optional[str]=..., rule: _Optional[_Union[ApprovalRuleInput, _Mapping]]=...) -> None:
        ...

class UpdateApprovalRuleResponse(_message.Message):
    __slots__ = ('rule',)
    RULE_FIELD_NUMBER: _ClassVar[int]
    rule: ApprovalRule

    def __init__(self, rule: _Optional[_Union[ApprovalRule, _Mapping]]=...) -> None:
        ...

class DeleteApprovalRuleRequest(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str

    def __init__(self, id: _Optional[str]=...) -> None:
        ...

class ListOntologyImportsRequest(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class OntologyImportEdge(_message.Message):
    __slots__ = ('source_path', 'target_path', 'alias')
    SOURCE_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    source_path: str
    target_path: str
    alias: str

    def __init__(self, source_path: _Optional[str]=..., target_path: _Optional[str]=..., alias: _Optional[str]=...) -> None:
        ...

class ListOntologyImportsResponse(_message.Message):
    __slots__ = ('imports',)
    IMPORTS_FIELD_NUMBER: _ClassVar[int]
    imports: _containers.RepeatedCompositeFieldContainer[OntologyImportEdge]

    def __init__(self, imports: _Optional[_Iterable[_Union[OntologyImportEdge, _Mapping]]]=...) -> None:
        ...

class GetFileUsageRequest(_message.Message):
    __slots__ = ('path_prefix', 'order', 'observation_period', 'page_cursor', 'page_size')
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    path_prefix: str
    order: UsageOrderBy
    observation_period: _duration_pb2.Duration
    page_cursor: str
    page_size: int

    def __init__(self, path_prefix: _Optional[str]=..., order: _Optional[_Union[UsageOrderBy, str]]=..., observation_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=..., page_cursor: _Optional[str]=..., page_size: _Optional[int]=...) -> None:
        ...

class FileUsage(_message.Message):
    __slots__ = ('file_path', 'average_tokens', 'average_query_time', 'hit_rate', 'num_errors', 'num_empties', 'chats_pulled', 'chats_used', 'last_pulled', 'last_run', 'last_used')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_QUERY_TIME_FIELD_NUMBER: _ClassVar[int]
    HIT_RATE_FIELD_NUMBER: _ClassVar[int]
    NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
    NUM_EMPTIES_FIELD_NUMBER: _ClassVar[int]
    CHATS_PULLED_FIELD_NUMBER: _ClassVar[int]
    CHATS_USED_FIELD_NUMBER: _ClassVar[int]
    LAST_PULLED_FIELD_NUMBER: _ClassVar[int]
    LAST_RUN_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    average_tokens: int
    average_query_time: _duration_pb2.Duration
    hit_rate: float
    num_errors: int
    num_empties: int
    chats_pulled: int
    chats_used: int
    last_pulled: _timestamp_pb2.Timestamp
    last_run: _timestamp_pb2.Timestamp
    last_used: _timestamp_pb2.Timestamp

    def __init__(self, file_path: _Optional[str]=..., average_tokens: _Optional[int]=..., average_query_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=..., hit_rate: _Optional[float]=..., num_errors: _Optional[int]=..., num_empties: _Optional[int]=..., chats_pulled: _Optional[int]=..., chats_used: _Optional[int]=..., last_pulled: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_run: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., last_used: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class GetFileUsageResponse(_message.Message):
    __slots__ = ('files', 'next_page_cursor')
    FILES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_CURSOR_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[FileUsage]
    next_page_cursor: str

    def __init__(self, files: _Optional[_Iterable[_Union[FileUsage, _Mapping]]]=..., next_page_cursor: _Optional[str]=...) -> None:
        ...

class GetOntologyUsageSummaryRequest(_message.Message):
    __slots__ = ('observation_period',)
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    observation_period: _duration_pb2.Duration

    def __init__(self, observation_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class GetOntologyUsageSummaryResponse(_message.Message):
    __slots__ = ('total_files', 'pulled_files', 'dead_files', 'avg_hit_rate', 'error_files', 'reclaimable_tokens')
    TOTAL_FILES_FIELD_NUMBER: _ClassVar[int]
    PULLED_FILES_FIELD_NUMBER: _ClassVar[int]
    DEAD_FILES_FIELD_NUMBER: _ClassVar[int]
    AVG_HIT_RATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FILES_FIELD_NUMBER: _ClassVar[int]
    RECLAIMABLE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    total_files: int
    pulled_files: int
    dead_files: int
    avg_hit_rate: float
    error_files: int
    reclaimable_tokens: int

    def __init__(self, total_files: _Optional[int]=..., pulled_files: _Optional[int]=..., dead_files: _Optional[int]=..., avg_hit_rate: _Optional[float]=..., error_files: _Optional[int]=..., reclaimable_tokens: _Optional[int]=...) -> None:
        ...

class ListOntologyFilesRequest(_message.Message):
    __slots__ = ('observation_period',)
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    observation_period: _duration_pb2.Duration

    def __init__(self, observation_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class ListOntologyFilesResponse(_message.Message):
    __slots__ = ('files',)
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[FileUsage]

    def __init__(self, files: _Optional[_Iterable[_Union[FileUsage, _Mapping]]]=...) -> None:
        ...

class Date(_message.Message):
    __slots__ = ('year', 'month', 'day')
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    year: int
    month: int
    day: int

    def __init__(self, year: _Optional[int]=..., month: _Optional[int]=..., day: _Optional[int]=...) -> None:
        ...

class DailyFileUsage(_message.Message):
    __slots__ = ('date', 'average_tokens', 'average_query_time', 'hit_rate', 'num_errors', 'num_empties', 'chats_pulled', 'chats_used')
    DATE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_TOKENS_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_QUERY_TIME_FIELD_NUMBER: _ClassVar[int]
    HIT_RATE_FIELD_NUMBER: _ClassVar[int]
    NUM_ERRORS_FIELD_NUMBER: _ClassVar[int]
    NUM_EMPTIES_FIELD_NUMBER: _ClassVar[int]
    CHATS_PULLED_FIELD_NUMBER: _ClassVar[int]
    CHATS_USED_FIELD_NUMBER: _ClassVar[int]
    date: Date
    average_tokens: int
    average_query_time: _duration_pb2.Duration
    hit_rate: float
    num_errors: int
    num_empties: int
    chats_pulled: int
    chats_used: int

    def __init__(self, date: _Optional[_Union[Date, _Mapping]]=..., average_tokens: _Optional[int]=..., average_query_time: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=..., hit_rate: _Optional[float]=..., num_errors: _Optional[int]=..., num_empties: _Optional[int]=..., chats_pulled: _Optional[int]=..., chats_used: _Optional[int]=...) -> None:
        ...

class GetUsageDetailsForFileRequest(_message.Message):
    __slots__ = ('file_path', 'observation_period')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    observation_period: _duration_pb2.Duration

    def __init__(self, file_path: _Optional[str]=..., observation_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class GetUsageDetailsForFileResponse(_message.Message):
    __slots__ = ('last_used', 'days')
    LAST_USED_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    last_used: _timestamp_pb2.Timestamp
    days: _containers.RepeatedCompositeFieldContainer[DailyFileUsage]

    def __init__(self, last_used: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., days: _Optional[_Iterable[_Union[DailyFileUsage, _Mapping]]]=...) -> None:
        ...

class ListChatsForFileRequest(_message.Message):
    __slots__ = ('file_path', 'observation_period', 'limit')
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    observation_period: _duration_pb2.Duration
    limit: int

    def __init__(self, file_path: _Optional[str]=..., observation_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=..., limit: _Optional[int]=...) -> None:
        ...

class FileChatUsage(_message.Message):
    __slots__ = ('chat_id', 'title', 'last_pulled', 'used')
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    LAST_PULLED_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    title: str
    last_pulled: _timestamp_pb2.Timestamp
    used: bool

    def __init__(self, chat_id: _Optional[str]=..., title: _Optional[str]=..., last_pulled: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]]=..., used: bool=...) -> None:
        ...

class ListChatsForFileResponse(_message.Message):
    __slots__ = ('chats',)
    CHATS_FIELD_NUMBER: _ClassVar[int]
    chats: _containers.RepeatedCompositeFieldContainer[FileChatUsage]

    def __init__(self, chats: _Optional[_Iterable[_Union[FileChatUsage, _Mapping]]]=...) -> None:
        ...

class GetFileUsageTimelineRequest(_message.Message):
    __slots__ = ('path_prefix', 'observation_period')
    PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    path_prefix: str
    observation_period: _duration_pb2.Duration

    def __init__(self, path_prefix: _Optional[str]=..., observation_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class GetFileUsageTimelineResponse(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: _containers.RepeatedCompositeFieldContainer[DailyFileUsage]

    def __init__(self, days: _Optional[_Iterable[_Union[DailyFileUsage, _Mapping]]]=...) -> None:
        ...

class GetOntologySizeTimelineRequest(_message.Message):
    __slots__ = ('observation_period',)
    OBSERVATION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    observation_period: _duration_pb2.Duration

    def __init__(self, observation_period: _Optional[_Union[datetime.timedelta, _duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class OntologySizeDay(_message.Message):
    __slots__ = ('date', 'total_bytes', 'file_count')
    DATE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BYTES_FIELD_NUMBER: _ClassVar[int]
    FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
    date: Date
    total_bytes: int
    file_count: int

    def __init__(self, date: _Optional[_Union[Date, _Mapping]]=..., total_bytes: _Optional[int]=..., file_count: _Optional[int]=...) -> None:
        ...

class GetOntologySizeTimelineResponse(_message.Message):
    __slots__ = ('days',)
    DAYS_FIELD_NUMBER: _ClassVar[int]
    days: _containers.RepeatedCompositeFieldContainer[OntologySizeDay]

    def __init__(self, days: _Optional[_Iterable[_Union[OntologySizeDay, _Mapping]]]=...) -> None:
        ...