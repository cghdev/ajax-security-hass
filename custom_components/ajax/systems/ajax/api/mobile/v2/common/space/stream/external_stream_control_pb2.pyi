from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space.stream import (
    stream_identifier_pb2 as _stream_identifier_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalStreamControl(_message.Message):
    __slots__ = ("stream_identifier",)
    STREAM_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    stream_identifier: _stream_identifier_pb2.StreamIdentifier
    def __init__(
        self,
        stream_identifier: _stream_identifier_pb2.StreamIdentifier | str | None = ...,
    ) -> None: ...
