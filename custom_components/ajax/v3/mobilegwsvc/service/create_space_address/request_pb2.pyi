from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space import (
    space_address_pb2 as _space_address_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CreateAddressRequest(_message.Message):
    __slots__ = ("address", "space_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    address: _space_address_pb2.SpaceAddress
    def __init__(
        self,
        space_id: str | None = ...,
        address: _space_address_pb2.SpaceAddress | _Mapping | None = ...,
    ) -> None: ...
