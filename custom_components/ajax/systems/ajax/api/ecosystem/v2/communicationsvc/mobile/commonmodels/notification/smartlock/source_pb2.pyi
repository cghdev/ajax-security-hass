from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.smartlock import (
    source_type_pb2 as _source_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockNotificationSource(_message.Message):
    __slots__ = ("id", "name", "room_hex_id", "room_name", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.SmartLockNotificationSourceType
    id: str
    name: str
    room_hex_id: str
    room_name: str
    def __init__(
        self,
        type: _source_type_pb2.SmartLockNotificationSourceType | str | None = ...,
        id: str | None = ...,
        name: str | None = ...,
        room_hex_id: str | None = ...,
        room_name: str | None = ...,
    ) -> None: ...
