from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.video.videoedge.archive import (
    calendar_pb2 as _calendar_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetChannelCalendarResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("calendar",)
        CALENDAR_FIELD_NUMBER: _ClassVar[int]
        calendar: _calendar_pb2.Calendar
        def __init__(
            self, calendar: _calendar_pb2.Calendar | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "permission_denied",
            "space_not_found",
            "video_edge_is_offline",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            channel_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetChannelCalendarResponse.Success
    failure: GetChannelCalendarResponse.Failure
    def __init__(
        self,
        success: GetChannelCalendarResponse.Success | _Mapping | None = ...,
        failure: GetChannelCalendarResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
