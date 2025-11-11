from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.detection import (
    line_crossing_rule_pb2 as _line_crossing_rule_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoEdgeLineCrossingSettingsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "enabled_object_classes",
            "max_rules_count",
            "object_detector_mask",
            "rules",
        )
        RULES_FIELD_NUMBER: _ClassVar[int]
        ENABLED_OBJECT_CLASSES_FIELD_NUMBER: _ClassVar[int]
        OBJECT_DETECTOR_MASK_FIELD_NUMBER: _ClassVar[int]
        MAX_RULES_COUNT_FIELD_NUMBER: _ClassVar[int]
        rules: _containers.RepeatedCompositeFieldContainer[
            _line_crossing_rule_pb2.LineCrossingRule
        ]
        enabled_object_classes: _containers.RepeatedScalarFieldContainer[
            _types_pb2.ObjectClass
        ]
        object_detector_mask: _types_pb2.Mask
        max_rules_count: int
        def __init__(
            self,
            rules: _Iterable[_line_crossing_rule_pb2.LineCrossingRule | _Mapping]
            | None = ...,
            enabled_object_classes: _Iterable[_types_pb2.ObjectClass | str]
            | None = ...,
            object_detector_mask: _types_pb2.Mask | _Mapping | None = ...,
            max_rules_count: int | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "line_crossing_settings_not_found",
            "permission_denied",
            "space_not_found",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        LINE_CROSSING_SETTINGS_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        line_crossing_settings_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            channel_not_found: _response_pb2.Error | _Mapping | None = ...,
            line_crossing_settings_not_found: _response_pb2.Error
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoEdgeLineCrossingSettingsResponse.Success
    failure: GetVideoEdgeLineCrossingSettingsResponse.Failure
    def __init__(
        self,
        success: GetVideoEdgeLineCrossingSettingsResponse.Success
        | _Mapping
        | None = ...,
        failure: GetVideoEdgeLineCrossingSettingsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
