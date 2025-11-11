from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import (
    archive_pb2 as _archive_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video import (
    duration_option_pb2 as _duration_option_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoCloudArchiveRecordSettingsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "allowed_cooldown_intervals",
            "allowed_record_modes",
            "allowed_recording_durations",
            "cooldown_interval",
            "detectors_disabled",
            "record_mode",
            "record_policy",
            "recording_duration",
        )
        RECORD_MODE_FIELD_NUMBER: _ClassVar[int]
        RECORD_POLICY_FIELD_NUMBER: _ClassVar[int]
        RECORDING_DURATION_FIELD_NUMBER: _ClassVar[int]
        COOLDOWN_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_RECORD_MODES_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_RECORDING_DURATIONS_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_COOLDOWN_INTERVALS_FIELD_NUMBER: _ClassVar[int]
        DETECTORS_DISABLED_FIELD_NUMBER: _ClassVar[int]
        record_mode: _archive_pb2.RecordMode
        record_policy: _archive_pb2.RecordPolicy
        recording_duration: _duration_option_pb2.DurationOption
        cooldown_interval: _duration_option_pb2.DurationOption
        allowed_record_modes: _containers.RepeatedScalarFieldContainer[
            _archive_pb2.RecordMode
        ]
        allowed_recording_durations: _containers.RepeatedScalarFieldContainer[
            _duration_option_pb2.DurationOption
        ]
        allowed_cooldown_intervals: _containers.RepeatedScalarFieldContainer[
            _duration_option_pb2.DurationOption
        ]
        detectors_disabled: bool
        def __init__(
            self,
            record_mode: _archive_pb2.RecordMode | str | None = ...,
            record_policy: _archive_pb2.RecordPolicy | str | None = ...,
            recording_duration: _duration_option_pb2.DurationOption | str | None = ...,
            cooldown_interval: _duration_option_pb2.DurationOption | str | None = ...,
            allowed_record_modes: _Iterable[_archive_pb2.RecordMode | str] | None = ...,
            allowed_recording_durations: _Iterable[
                _duration_option_pb2.DurationOption | str
            ]
            | None = ...,
            allowed_cooldown_intervals: _Iterable[
                _duration_option_pb2.DurationOption | str
            ]
            | None = ...,
            detectors_disabled: bool = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "cloud_archive_not_found",
            "permission_denied",
            "space_not_found",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CLOUD_ARCHIVE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        cloud_archive_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            channel_not_found: _response_pb2.Error | _Mapping | None = ...,
            cloud_archive_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoCloudArchiveRecordSettingsResponse.Success
    failure: GetVideoCloudArchiveRecordSettingsResponse.Failure
    def __init__(
        self,
        success: GetVideoCloudArchiveRecordSettingsResponse.Success
        | _Mapping
        | None = ...,
        failure: GetVideoCloudArchiveRecordSettingsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
