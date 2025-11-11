from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1.common import user_pb2 as _user_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class UserStreamChangesResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _user_pb2.User | _Mapping | None = ...) -> None: ...
