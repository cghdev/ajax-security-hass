from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SelectedDevice(_message.Message):
    __slots__ = ("device_id", "is_selected", "object_type")
    DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    device_id: str
    object_type: _object_type_pb2.ObjectType
    is_selected: bool
    def __init__(
        self,
        device_id: str | None = ...,
        object_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
        is_selected: bool = ...,
    ) -> None: ...
