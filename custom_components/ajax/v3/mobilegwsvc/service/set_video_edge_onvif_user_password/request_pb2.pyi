from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeOnvifUserPasswordRequest(_message.Message):
    __slots__ = ("password", "space_id", "username", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    username: str
    password: str
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        username: str | None = ...,
        password: str | None = ...,
    ) -> None: ...
