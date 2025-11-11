from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
import datetime
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2
from systems.ajax.api.mobile.v2.common.video.webrtc import (
    ice_candidate_filters_pb2 as _ice_candidate_filters_pb2,
)
from systems.ajax.api.mobile.v2.common.video.webrtc import (
    ice_candidate_pb2 as _ice_candidate_pb2,
)
from systems.ajax.api.mobile.v2.common.video.webrtc import (
    session_description_pb2 as _session_description_pb2,
)
from systems.ajax.api.mobile.v2.common.video.webrtc import stream_pb2 as _stream_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamWebrtcRequest(_message.Message):
    __slots__ = (
        "answer",
        "ask_streams",
        "init",
        "new_ice_candidate",
        "offer",
        "peer_connection_established",
    )
    class Init(_message.Message):
        __slots__ = (
            "allow_large_rtp_packets",
            "ice_filters",
            "initial_streams",
            "space_locator",
            "video_edge_id",
        )
        SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        INITIAL_STREAMS_FIELD_NUMBER: _ClassVar[int]
        ICE_FILTERS_FIELD_NUMBER: _ClassVar[int]
        ALLOW_LARGE_RTP_PACKETS_FIELD_NUMBER: _ClassVar[int]
        space_locator: _space_locator_pb2.SpaceLocator
        video_edge_id: str
        initial_streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
        ice_filters: _ice_candidate_filters_pb2.IceCandidateFilters
        allow_large_rtp_packets: bool
        def __init__(
            self,
            space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
            video_edge_id: str | None = ...,
            initial_streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...,
            ice_filters: _ice_candidate_filters_pb2.IceCandidateFilters
            | _Mapping
            | None = ...,
            allow_large_rtp_packets: bool = ...,
        ) -> None: ...

    class AskStreams(_message.Message):
        __slots__ = ("streams",)
        STREAMS_FIELD_NUMBER: _ClassVar[int]
        streams: _containers.RepeatedCompositeFieldContainer[_stream_pb2.Stream]
        def __init__(
            self, streams: _Iterable[_stream_pb2.Stream | _Mapping] | None = ...
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

    class PeerConnectionEstablished(_message.Message):
        __slots__ = (
            "ice_candidate_type",
            "latency",
            "network_technology_type",
            "transport_protocol_type",
        )
        LATENCY_FIELD_NUMBER: _ClassVar[int]
        NETWORK_TECHNOLOGY_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_PROTOCOL_TYPE_FIELD_NUMBER: _ClassVar[int]
        ICE_CANDIDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        latency: _duration_pb2.Duration
        network_technology_type: _types_pb2.NetworkTechnologyType
        transport_protocol_type: _types_pb2.TransportProtocolType
        ice_candidate_type: _types_pb2.IceCandidateType
        def __init__(
            self,
            latency: datetime.timedelta
            | _duration_pb2.Duration
            | _Mapping
            | None = ...,
            network_technology_type: _types_pb2.NetworkTechnologyType
            | str
            | None = ...,
            transport_protocol_type: _types_pb2.TransportProtocolType
            | str
            | None = ...,
            ice_candidate_type: _types_pb2.IceCandidateType | str | None = ...,
        ) -> None: ...

    INIT_FIELD_NUMBER: _ClassVar[int]
    ASK_STREAMS_FIELD_NUMBER: _ClassVar[int]
    NEW_ICE_CANDIDATE_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    PEER_CONNECTION_ESTABLISHED_FIELD_NUMBER: _ClassVar[int]
    init: StreamWebrtcRequest.Init
    ask_streams: StreamWebrtcRequest.AskStreams
    new_ice_candidate: StreamWebrtcRequest.NewIceCandidate
    offer: StreamWebrtcRequest.Offer
    answer: StreamWebrtcRequest.Answer
    peer_connection_established: StreamWebrtcRequest.PeerConnectionEstablished
    def __init__(
        self,
        init: StreamWebrtcRequest.Init | _Mapping | None = ...,
        ask_streams: StreamWebrtcRequest.AskStreams | _Mapping | None = ...,
        new_ice_candidate: StreamWebrtcRequest.NewIceCandidate | _Mapping | None = ...,
        offer: StreamWebrtcRequest.Offer | _Mapping | None = ...,
        answer: StreamWebrtcRequest.Answer | _Mapping | None = ...,
        peer_connection_established: StreamWebrtcRequest.PeerConnectionEstablished
        | _Mapping
        | None = ...,
    ) -> None: ...
