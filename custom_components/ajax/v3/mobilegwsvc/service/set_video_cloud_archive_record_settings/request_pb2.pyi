from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import (
    archive_pb2 as _archive_pb2,
)
from v3.mobilegwsvc.commonmodels.video import (
    duration_option_pb2 as _duration_option_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoCloudArchiveRecordSettingsRequest(_message.Message):
    __slots__ = (
        "channel_id",
        "cooldown_interval",
        "record_mode",
        "record_policy",
        "recording_duration",
        "space_id",
        "video_edge_id",
    )
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
    RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
    RECORDING_DURATION_FIELD_NUMBER: _ClassVar[int]
    COOLDOWN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    channel_id: str
    record_mode: _archive_pb2.RecordMode
    record_policy: _archive_pb2.RecordPolicy
    recording_duration: _duration_option_pb2.DurationOption
    cooldown_interval: _duration_option_pb2.DurationOption
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        channel_id: str | None = ...,
        record_mode: _archive_pb2.RecordMode | str | None = ...,
        record_policy: _archive_pb2.RecordPolicy | str | None = ...,
        recording_duration: _duration_option_pb2.DurationOption | str | None = ...,
        cooldown_interval: _duration_option_pb2.DurationOption | str | None = ...,
    ) -> None: ...
