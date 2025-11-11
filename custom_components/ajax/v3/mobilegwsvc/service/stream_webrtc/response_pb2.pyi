from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video.webrtc import (
    ice_candidate_pb2 as _ice_candidate_pb2,
)
from systems.ajax.api.mobile.v2.common.video.webrtc import (
    ice_server_pb2 as _ice_server_pb2,
)
from systems.ajax.api.mobile.v2.common.video.webrtc import (
    session_description_pb2 as _session_description_pb2,
)
from systems.ajax.api.mobile.v2.common.video.webrtc import stream_pb2 as _stream_pb2
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamWebrtcResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = (
            "answer",
            "ask_streams_response",
            "init",
            "new_ice_candidate",
            "offer",
        )
        class Init(_message.Message):
            __slots__ = ("ice_servers", "streams")
            ICE_SERVERS_FIELD_NUMBER: _ClassVar[int]
            STREAMS_FIELD_NUMBER: _ClassVar[int]
            ice_servers: _containers.RepeatedCompositeFieldContainer[
                _ice_server_pb2.IceServer
            ]
            streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
            def __init__(
                self,
                ice_servers: _Iterable[_ice_server_pb2.IceServer | _Mapping]
                | None = ...,
                streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...,
            ) -> None: ...

        class AskStreamsResponse(_message.Message):
            __slots__ = ("failure", "success")
            class AskStreamsSuccess(_message.Message):
                __slots__ = ("streams",)
                STREAMS_FIELD_NUMBER: _ClassVar[int]
                streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
                def __init__(
                    self, streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...
                ) -> None: ...

            class AskStreamsFailure(_message.Message):
                __slots__ = (
                    "bad_request",
                    "permission_denied",
                    "video_edge_is_offline",
                    "video_edge_not_found",
                )
                BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
                VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
                PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
                VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
                bad_request: _response_pb2.Error
                video_edge_not_found: _response_pb2.Error
                permission_denied: _response_pb2.Error
                video_edge_is_offline: _response_pb2.Error
                def __init__(
                    self,
                    bad_request: _response_pb2.Error | _Mapping | None = ...,
                    video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
                    permission_denied: _response_pb2.Error | _Mapping | None = ...,
                    video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
                ) -> None: ...

            SUCCESS_FIELD_NUMBER: _ClassVar[int]
            FAILURE_FIELD_NUMBER: _ClassVar[int]
            success: StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsSuccess
            failure: StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsFailure
            def __init__(
                self,
                success: StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsSuccess
                | _Mapping
                | None = ...,
                failure: StreamWebrtcResponse.Success.AskStreamsResponse.AskStreamsFailure
                | _Mapping
                | None = ...,
            ) -> None: ...

        class NewIceCandidate(_message.Message):
            __slots__ = ("candidate",)
            CANDIDATE_FIELD_NUMBER: _ClassVar[int]
            candidate: _ice_candidate_pb2.IceCandidate
            def __init__(
                self, candidate: _ice_candidate_pb2.IceCandidate | _Mapping | None = ...
            ) -> None: ...

        class Offer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(
                self,
                session_description: _session_description_pb2.SessionDescription
                | _Mapping
                | None = ...,
            ) -> None: ...

        class Answer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(
                self,
                session_description: _session_description_pb2.SessionDescription
                | _Mapping
                | None = ...,
            ) -> None: ...

        INIT_FIELD_NUMBER: _ClassVar[int]
        ASK_STREAMS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        NEW_ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        init: StreamWebrtcResponse.Success.Init
        ask_streams_response: StreamWebrtcResponse.Success.AskStreamsResponse
        new_ice_candidate: StreamWebrtcResponse.Success.NewIceCandidate
        offer: StreamWebrtcResponse.Success.Offer
        answer: StreamWebrtcResponse.Success.Answer
        def __init__(
            self,
            init: StreamWebrtcResponse.Success.Init | _Mapping | None = ...,
            ask_streams_response: StreamWebrtcResponse.Success.AskStreamsResponse
            | _Mapping
            | None = ...,
            new_ice_candidate: StreamWebrtcResponse.Success.NewIceCandidate
            | _Mapping
            | None = ...,
            offer: StreamWebrtcResponse.Success.Offer | _Mapping | None = ...,
            answer: StreamWebrtcResponse.Success.Answer | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamWebrtcResponse.Success
    failure: StreamWebrtcResponse.Failure
    def __init__(
        self,
        success: StreamWebrtcResponse.Success | _Mapping | None = ...,
        failure: StreamWebrtcResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
