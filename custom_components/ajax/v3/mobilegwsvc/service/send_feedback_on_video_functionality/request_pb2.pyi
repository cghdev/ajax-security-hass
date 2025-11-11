from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SendFeedbackOnVideoFunctionalityRequest(_message.Message):
    __slots__ = ("detection_feedback_details", "space_locator", "text", "video_edge_id")
    class DetectionResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETECTION_RESULT_UNSPECIFIED: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionResult
        ]
        DETECTION_RESULT_MISSING: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionResult
        ]
        DETECTION_RESULT_VEHICLE: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionResult
        ]
        DETECTION_RESULT_ANIMAL: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionResult
        ]
        DETECTION_RESULT_HUMAN: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionResult
        ]

    DETECTION_RESULT_UNSPECIFIED: (
        SendFeedbackOnVideoFunctionalityRequest.DetectionResult
    )
    DETECTION_RESULT_MISSING: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
    DETECTION_RESULT_VEHICLE: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
    DETECTION_RESULT_ANIMAL: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
    DETECTION_RESULT_HUMAN: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
    class DetectionFeedbackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETECTION_FEEDBACK_TYPE_UNSPECIFIED: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
        ]
        DETECTION_FEEDBACK_TYPE_POSITIVE: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
        ]
        DETECTION_FEEDBACK_TYPE_NEGATIVE: _ClassVar[
            SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
        ]

    DETECTION_FEEDBACK_TYPE_UNSPECIFIED: (
        SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
    )
    DETECTION_FEEDBACK_TYPE_POSITIVE: (
        SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
    )
    DETECTION_FEEDBACK_TYPE_NEGATIVE: (
        SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
    )
    class DetectionFeedbackDetails(_message.Message):
        __slots__ = (
            "actual",
            "channel_id",
            "detection_feedback",
            "expected",
            "time_range",
            "timestamp",
            "video_source_type",
        )
        EXPECTED_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_FIELD_NUMBER: _ClassVar[int]
        DETECTION_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
        TIME_RANGE_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        VIDEO_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        expected: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
        actual: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
        detection_feedback: (
            SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
        )
        time_range: _types_pb2.TimestampRange
        channel_id: str
        timestamp: _timestamp_pb2.Timestamp
        video_source_type: _types_pb2.VideoSourceType
        def __init__(
            self,
            expected: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
            | str
            | None = ...,
            actual: SendFeedbackOnVideoFunctionalityRequest.DetectionResult
            | str
            | None = ...,
            detection_feedback: SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackType
            | str
            | None = ...,
            time_range: _types_pb2.TimestampRange | _Mapping | None = ...,
            channel_id: str | None = ...,
            timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            video_source_type: _types_pb2.VideoSourceType | str | None = ...,
        ) -> None: ...

    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    DETECTION_FEEDBACK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    space_locator: _space_locator_pb2.SpaceLocator
    text: str
    detection_feedback_details: (
        SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackDetails
    )
    def __init__(
        self,
        video_edge_id: str | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        text: str | None = ...,
        detection_feedback_details: SendFeedbackOnVideoFunctionalityRequest.DetectionFeedbackDetails
        | _Mapping
        | None = ...,
    ) -> None: ...
