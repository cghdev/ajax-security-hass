from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareUpdateStartedData(_message.Message):
    __slots__ = ("member_id", "member_user_name")
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    MEMBER_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    member_id: str
    member_user_name: str
    def __init__(
        self, member_id: str | None = ..., member_user_name: str | None = ...
    ) -> None: ...
