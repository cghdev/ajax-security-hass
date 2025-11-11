from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.accounting import (
    service_state_pb2 as _service_state_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.about import (
    about_pb2 as _about_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdge(_message.Message):
    __slots__ = (
        "channels",
        "id",
        "non_zombie_channels_count",
        "room_id",
        "service_state",
        "type",
    )
    class Channel(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: str | None = ...) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    NON_ZOMBIE_CHANNELS_COUNT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    room_id: str
    non_zombie_channels_count: int
    type: _about_pb2.About.Type
    channels: _containers.RepeatedCompositeFieldContainer[VideoEdge.Channel]
    service_state: _service_state_pb2.ServiceState
    def __init__(
        self,
        id: str | None = ...,
        room_id: str | None = ...,
        non_zombie_channels_count: int | None = ...,
        type: _about_pb2.About.Type | str | None = ...,
        channels: _Iterable[VideoEdge.Channel | _Mapping] | None = ...,
        service_state: _service_state_pb2.ServiceState | str | None = ...,
    ) -> None: ...
