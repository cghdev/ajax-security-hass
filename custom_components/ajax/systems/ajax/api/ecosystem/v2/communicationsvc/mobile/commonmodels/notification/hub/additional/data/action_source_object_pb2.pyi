from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    source_type_pb2 as _source_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ActionSourceObject(_message.Message):
    __slots__ = ("hex_id", "object_name", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_NAME_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.HubNotificationSourceType
    hex_id: str
    object_name: str
    def __init__(
        self,
        type: _source_type_pb2.HubNotificationSourceType | str | None = ...,
        hex_id: str | None = ...,
        object_name: str | None = ...,
    ) -> None: ...
