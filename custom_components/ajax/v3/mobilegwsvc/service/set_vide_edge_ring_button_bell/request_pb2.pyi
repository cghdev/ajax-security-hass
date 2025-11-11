from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeRingButtonBellRequest(_message.Message):
    __slots__ = ("ring_button_bell_enabled", "space_locator", "video_edge_id")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_BELL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    video_edge_id: str
    ring_button_bell_enabled: bool
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        video_edge_id: str | None = ...,
        ring_button_bell_enabled: bool = ...,
    ) -> None: ...
