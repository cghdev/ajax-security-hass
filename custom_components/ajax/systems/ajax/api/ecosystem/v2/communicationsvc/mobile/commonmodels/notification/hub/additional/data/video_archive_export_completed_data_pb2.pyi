from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import (
    visibility_pb2 as _visibility_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoArchiveExportCompletedData(_message.Message):
    __slots__ = (
        "channel_id",
        "channel_name",
        "export_failed_metadata",
        "export_id",
        "export_prepared_metadata",
        "member_id",
        "member_user_name",
        "visibility",
    )
    class ExportPreparedMetadata(_message.Message):
        __slots__ = ("expires_at",)
        EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
        expires_at: _timestamp_pb2.Timestamp
        def __init__(
            self, expires_at: _timestamp_pb2.Timestamp | _Mapping | None = ...
        ) -> None: ...

    class ExportFailedMetadata(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPORT_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    EXPORT_PREPARED_METADATA_FIELD_NUMBER: _ClassVar[int]
    EXPORT_FAILED_METADATA_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    channel_name: str
    export_id: str
    member_id: str
    member_user_name: str
    visibility: _visibility_pb2.MediaVisibility
    export_prepared_metadata: VideoArchiveExportCompletedData.ExportPreparedMetadata
    export_failed_metadata: VideoArchiveExportCompletedData.ExportFailedMetadata
    def __init__(
        self,
        channel_id: str | None = ...,
        channel_name: str | None = ...,
        export_id: str | None = ...,
        member_id: str | None = ...,
        member_user_name: str | None = ...,
        visibility: _visibility_pb2.MediaVisibility | _Mapping | None = ...,
        export_prepared_metadata: VideoArchiveExportCompletedData.ExportPreparedMetadata
        | _Mapping
        | None = ...,
        export_failed_metadata: VideoArchiveExportCompletedData.ExportFailedMetadata
        | _Mapping
        | None = ...,
    ) -> None: ...
