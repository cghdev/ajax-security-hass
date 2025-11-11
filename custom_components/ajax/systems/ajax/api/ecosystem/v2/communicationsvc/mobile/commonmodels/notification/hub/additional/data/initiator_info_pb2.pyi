from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    source_type_pb2 as _source_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatorInfo(_message.Message):
    __slots__ = ("device_color", "hex_id", "name", "room_id", "room_name", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.HubNotificationSourceType
    hex_id: str
    name: str
    room_name: str
    room_id: str
    device_color: _device_color_pb2.DeviceColor
    def __init__(
        self,
        type: _source_type_pb2.HubNotificationSourceType | str | None = ...,
        hex_id: str | None = ...,
        name: str | None = ...,
        room_name: str | None = ...,
        room_id: str | None = ...,
        device_color: _device_color_pb2.DeviceColor | str | None = ...,
    ) -> None: ...
