from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.hub.user import (
    hub_user_type_pb2 as _hub_user_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubUser(_message.Message):
    __slots__ = ("id", "role")
    ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    id: str
    role: _hub_user_type_pb2.HubUserType
    def __init__(
        self,
        id: str | None = ...,
        role: _hub_user_type_pb2.HubUserType | str | None = ...,
    ) -> None: ...
