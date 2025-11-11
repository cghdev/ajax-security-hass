from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video.videoedge.localuser import (
    local_user_permissions_pb2 as _local_user_permissions_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateVideoEdgeLocalUserRequest(_message.Message):
    __slots__ = ("name", "new_name", "permissions", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    name: str
    new_name: str
    permissions: _local_user_permissions_pb2.LocalUserPermissions
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        name: str | None = ...,
        new_name: str | None = ...,
        permissions: _local_user_permissions_pb2.LocalUserPermissions
        | _Mapping
        | None = ...,
    ) -> None: ...
