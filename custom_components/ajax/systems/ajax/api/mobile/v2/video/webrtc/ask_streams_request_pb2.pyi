from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.webrtc import stream_pb2 as _stream_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AskWebRtcStreamsRequest(_message.Message):
    __slots__ = ("space_locator", "streams", "video_edge_id", "webrtc_session_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    WEBRTC_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STREAMS_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    webrtc_session_id: str
    streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        webrtc_session_id: str | None = ...,
        streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class AskWebRtcStreamsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("streams",)
        STREAMS_FIELD_NUMBER: _ClassVar[int]
        streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
        def __init__(
            self, streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "session_not_found",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SESSION_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        session_not_found: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            session_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AskWebRtcStreamsResponse.Success
    failure: AskWebRtcStreamsResponse.Failure
    def __init__(
        self,
        success: AskWebRtcStreamsResponse.Success | _Mapping | None = ...,
        failure: AskWebRtcStreamsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
