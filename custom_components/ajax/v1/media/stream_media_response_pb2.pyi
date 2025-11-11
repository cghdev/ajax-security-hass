from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.media import media_pb2 as _media_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamMediaResponse(_message.Message):
    __slots__ = ("media",)
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    media: _containers.RepeatedCompositeFieldContainer[_media_pb2.Media]
    def __init__(
        self, media: _Iterable[_media_pb2.Media | _Mapping] | None = ...
    ) -> None: ...
