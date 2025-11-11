from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class EjectVideoEdgeStorageDeviceRequest(_message.Message):
    __slots__ = ("space_id", "storage_device_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    storage_device_id: str
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        storage_device_id: str | None = ...,
    ) -> None: ...
