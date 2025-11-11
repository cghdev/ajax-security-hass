from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class VideoEdgeChannelMediaDataInfo(_message.Message):
    __slots__ = ("allowed_member_ids", "channel_id")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    allowed_member_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(
        self,
        channel_id: str | None = ...,
        allowed_member_ids: _Iterable[str] | None = ...,
    ) -> None: ...
