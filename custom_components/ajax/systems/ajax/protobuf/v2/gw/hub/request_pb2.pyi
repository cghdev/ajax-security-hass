from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.protobuf.auth import auth_pb2 as _auth_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetHubForMigrationRequest(_message.Message):
    __slots__ = ("hub_id", "user_id", "user_role")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ROLE_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_role: _auth_pb2.UserRole
    hub_id: str
    def __init__(
        self,
        user_id: str | None = ...,
        user_role: _auth_pb2.UserRole | str | None = ...,
        hub_id: str | None = ...,
    ) -> None: ...
