from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class PaidService(_message.Message):
    __slots__ = ("id", "name", "name_res_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_RES_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name_res_id: str
    name: str
    def __init__(
        self,
        id: str | None = ...,
        name_res_id: str | None = ...,
        name: str | None = ...,
    ) -> None: ...
