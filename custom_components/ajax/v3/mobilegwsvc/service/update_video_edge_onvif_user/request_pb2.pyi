from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video.videoedge.onvif import (
    onvif_user_pb2 as _onvif_user_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateVideoEdgeOnvifUserRequest(_message.Message):
    __slots__ = ("new_username", "role", "space_id", "username", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NEW_USERNAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    username: str
    new_username: str
    role: _onvif_user_pb2.OnvifUser.OnvifUserRole
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        username: str | None = ...,
        new_username: str | None = ...,
        role: _onvif_user_pb2.OnvifUser.OnvifUserRole | str | None = ...,
    ) -> None: ...
