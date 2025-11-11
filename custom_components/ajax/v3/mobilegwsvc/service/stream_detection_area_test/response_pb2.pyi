from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamDetectionAreaTestResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[StreamDetectionAreaTestResponse.Success.State]
            STATE_IN_PROGRESS: _ClassVar[StreamDetectionAreaTestResponse.Success.State]
            STATE_READY: _ClassVar[StreamDetectionAreaTestResponse.Success.State]
            STATE_FAILED: _ClassVar[StreamDetectionAreaTestResponse.Success.State]

        STATE_UNSPECIFIED: StreamDetectionAreaTestResponse.Success.State
        STATE_IN_PROGRESS: StreamDetectionAreaTestResponse.Success.State
        STATE_READY: StreamDetectionAreaTestResponse.Success.State
        STATE_FAILED: StreamDetectionAreaTestResponse.Success.State
        class Snapshot(_message.Message):
            __slots__ = ("detection_area",)
            DETECTION_AREA_FIELD_NUMBER: _ClassVar[int]
            detection_area: StreamDetectionAreaTestResponse.Success.DetectionArea
            def __init__(
                self,
                detection_area: StreamDetectionAreaTestResponse.Success.DetectionArea
                | _Mapping
                | None = ...,
            ) -> None: ...

        class Update(_message.Message):
            __slots__ = ("detection_area",)
            DETECTION_AREA_FIELD_NUMBER: _ClassVar[int]
            detection_area: StreamDetectionAreaTestResponse.Success.DetectionArea
            def __init__(
                self,
                detection_area: StreamDetectionAreaTestResponse.Success.DetectionArea
                | _Mapping
                | None = ...,
            ) -> None: ...

        class DetectionArea(_message.Message):
            __slots__ = ("photo_info", "state")
            STATE_FIELD_NUMBER: _ClassVar[int]
            PHOTO_INFO_FIELD_NUMBER: _ClassVar[int]
            state: StreamDetectionAreaTestResponse.Success.State
            photo_info: StreamDetectionAreaTestResponse.Success.PhotoInfo
            def __init__(
                self,
                state: StreamDetectionAreaTestResponse.Success.State | str | None = ...,
                photo_info: StreamDetectionAreaTestResponse.Success.PhotoInfo
                | _Mapping
                | None = ...,
            ) -> None: ...

        class PhotoInfo(_message.Message):
            __slots__ = ("creation_time", "url")
            URL_FIELD_NUMBER: _ClassVar[int]
            CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
            url: str
            creation_time: _timestamp_pb2.Timestamp
            def __init__(
                self,
                url: str | None = ...,
                creation_time: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            ) -> None: ...

        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamDetectionAreaTestResponse.Success.Snapshot
        update: StreamDetectionAreaTestResponse.Success.Update
        def __init__(
            self,
            snapshot: StreamDetectionAreaTestResponse.Success.Snapshot
            | _Mapping
            | None = ...,
            update: StreamDetectionAreaTestResponse.Success.Update
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamDetectionAreaTestResponse.Success
    failure: StreamDetectionAreaTestResponse.Failure
    def __init__(
        self,
        success: StreamDetectionAreaTestResponse.Success | _Mapping | None = ...,
        failure: StreamDetectionAreaTestResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
