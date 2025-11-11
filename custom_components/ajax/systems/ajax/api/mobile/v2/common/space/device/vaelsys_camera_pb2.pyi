from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class VaelsysCamera(_message.Message):
    __slots__ = ("id", "name", "vaelsys_camera_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    VAELSYS_CAMERA_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    vaelsys_camera_id: str
    name: str
    def __init__(
        self,
        id: str | None = ...,
        vaelsys_camera_id: str | None = ...,
        name: str | None = ...,
    ) -> None: ...
