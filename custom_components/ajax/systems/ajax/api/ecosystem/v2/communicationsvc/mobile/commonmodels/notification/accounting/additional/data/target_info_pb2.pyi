from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting.additional.data import (
    additional_target_info_pb2 as _additional_target_info_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class TargetInfo(_message.Message):
    __slots__ = ("additional_info", "id", "name", "room_name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    room_name: str
    additional_info: _additional_target_info_pb2.AdditionalTargetInfo
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        room_name: str | None = ...,
        additional_info: _additional_target_info_pb2.AdditionalTargetInfo
        | _Mapping
        | None = ...,
    ) -> None: ...
