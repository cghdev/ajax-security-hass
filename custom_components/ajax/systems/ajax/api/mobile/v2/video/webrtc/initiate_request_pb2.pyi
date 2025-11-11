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
from systems.ajax.api.mobile.v2.common.video.webrtc import (
    ice_candidate_filters_pb2 as _ice_candidate_filters_pb2,
)
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

DESCRIPTOR: _descriptor.FileDescriptor

class InitiateWebRtcRequest(_message.Message):
    __slots__ = (
        "allow_large_rtp_packets",
        "ice_filters",
        "initial_streams",
        "space_locator",
        "video_edge_id",
    )
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    INITIAL_STREAMS_FIELD_NUMBER: _ClassVar[int]
    ICE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    ALLOW_LARGE_RTP_PACKETS_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    initial_streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
    ice_filters: _ice_candidate_filters_pb2.IceCandidateFilters
    allow_large_rtp_packets: bool
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        initial_streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...,
        ice_filters: _ice_candidate_filters_pb2.IceCandidateFilters
        | _Mapping
        | None = ...,
        allow_large_rtp_packets: bool = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class InitiateWebRtcResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("answer", "init", "new_ice_candidate", "offer")
        class WebRtcInit(_message.Message):
            __slots__ = ("ice_servers", "session_id", "streams")
            SESSION_ID_FIELD_NUMBER: _ClassVar[int]
            ICE_SERVERS_FIELD_NUMBER: _ClassVar[int]
            STREAMS_FIELD_NUMBER: _ClassVar[int]
            session_id: str
            ice_servers: _containers.RepeatedCompositeFieldContainer[
                _ice_server_pb2.IceServer
            ]
            streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
            def __init__(
                self,
                session_id: str | None = ...,
                ice_servers: _Iterable[_ice_server_pb2.IceServer | _Mapping]
                | None = ...,
                streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...,
            ) -> None: ...

        class WebRtcOffer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(
                self,
                session_description: _session_description_pb2.SessionDescription
                | _Mapping
                | None = ...,
            ) -> None: ...

        class WebRtcAnswer(_message.Message):
            __slots__ = ("session_description",)
            SESSION_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            session_description: _session_description_pb2.SessionDescription
            def __init__(
                self,
                session_description: _session_description_pb2.SessionDescription
                | _Mapping
                | None = ...,
            ) -> None: ...

        class WebRtcNewIceCandidate(_message.Message):
            __slots__ = ("candidate",)
            CANDIDATE_FIELD_NUMBER: _ClassVar[int]
            candidate: _ice_candidate_pb2.IceCandidate
            def __init__(
                self, candidate: _ice_candidate_pb2.IceCandidate | _Mapping | None = ...
            ) -> None: ...

        INIT_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        NEW_ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        init: InitiateWebRtcResponse.Success.WebRtcInit
        offer: InitiateWebRtcResponse.Success.WebRtcOffer
        new_ice_candidate: InitiateWebRtcResponse.Success.WebRtcNewIceCandidate
        answer: InitiateWebRtcResponse.Success.WebRtcAnswer
        def __init__(
            self,
            init: InitiateWebRtcResponse.Success.WebRtcInit | _Mapping | None = ...,
            offer: InitiateWebRtcResponse.Success.WebRtcOffer | _Mapping | None = ...,
            new_ice_candidate: InitiateWebRtcResponse.Success.WebRtcNewIceCandidate
            | _Mapping
            | None = ...,
            answer: InitiateWebRtcResponse.Success.WebRtcAnswer | _Mapping | None = ...,
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
        bad_request: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: InitiateWebRtcResponse.Success
    failure: InitiateWebRtcResponse.Failure
    def __init__(
        self,
        success: InitiateWebRtcResponse.Success | _Mapping | None = ...,
        failure: InitiateWebRtcResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
