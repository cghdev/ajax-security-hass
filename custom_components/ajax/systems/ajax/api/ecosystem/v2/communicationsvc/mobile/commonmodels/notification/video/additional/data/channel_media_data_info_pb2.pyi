from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelMediaDataInfo(_message.Message):
    __slots__ = ("allowed_member_ids", "channel_id", "channel_name", "num_frames")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    NUM_FRAMES_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    allowed_member_ids: _containers.RepeatedScalarFieldContainer[str]
    channel_name: str
    num_frames: int
    def __init__(
        self,
        channel_id: str | None = ...,
        allowed_member_ids: _Iterable[str] | None = ...,
        channel_name: str | None = ...,
        num_frames: int | None = ...,
    ) -> None: ...
