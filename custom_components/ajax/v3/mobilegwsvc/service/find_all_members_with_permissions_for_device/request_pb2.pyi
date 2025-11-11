from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.space.device import (
    smart_lock_id_pb2 as _smart_lock_id_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device import (
    video_channel_id_pb2 as _video_channel_id_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllMembersWithPermissionsForDeviceRequest(_message.Message):
    __slots__ = ("smart_lock_id", "space_id", "video_channel_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    smart_lock_id: _smart_lock_id_pb2.SmartLockId
    video_channel_id: _video_channel_id_pb2.VideoChannelId
    def __init__(
        self,
        space_id: str | None = ...,
        smart_lock_id: _smart_lock_id_pb2.SmartLockId | _Mapping | None = ...,
        video_channel_id: _video_channel_id_pb2.VideoChannelId | _Mapping | None = ...,
    ) -> None: ...
