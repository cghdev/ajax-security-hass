from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ImageUrls(_message.Message):
    __slots__ = ("base_path", "big", "medium", "small")
    SMALL_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_FIELD_NUMBER: _ClassVar[int]
    BIG_FIELD_NUMBER: _ClassVar[int]
    BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    small: _wrappers_pb2.StringValue
    medium: _wrappers_pb2.StringValue
    big: _wrappers_pb2.StringValue
    base_path: _wrappers_pb2.StringValue
    def __init__(
        self,
        small: _wrappers_pb2.StringValue | _Mapping | None = ...,
        medium: _wrappers_pb2.StringValue | _Mapping | None = ...,
        big: _wrappers_pb2.StringValue | _Mapping | None = ...,
        base_path: _wrappers_pb2.StringValue | _Mapping | None = ...,
    ) -> None: ...
