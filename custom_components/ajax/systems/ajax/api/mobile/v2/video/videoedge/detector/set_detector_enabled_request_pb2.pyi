from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.detection import (
    detection_settings_pb2 as _detection_settings_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.channel.detection import (
    detector_locator_pb2 as _detector_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetDetectorEnabledRequest(_message.Message):
    __slots__ = (
        "detector_id",
        "detector_locator",
        "enabled",
        "space_locator",
        "video_edge_id",
    )
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    DETECTOR_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    detector_id: str
    enabled: bool
    space_locator: _space_locator_pb2.SpaceLocator
    detector_locator: _detector_locator_pb2.DetectorLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        detector_id: str | None = ...,
        enabled: bool = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        detector_locator: _detector_locator_pb2.DetectorLocator | _Mapping | None = ...,
    ) -> None: ...

class SetDetectorEnabledResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("settings",)
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        settings: _detection_settings_pb2.DetectionSettings
        def __init__(
            self,
            settings: _detection_settings_pb2.DetectionSettings | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "detector_not_found",
            "permission_denied",
            "space_armed",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        DETECTOR_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        detector_not_found: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            detector_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetDetectorEnabledResponse.Success
    failure: SetDetectorEnabledResponse.Failure
    def __init__(
        self,
        success: SetDetectorEnabledResponse.Success | _Mapping | None = ...,
        failure: SetDetectorEnabledResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
