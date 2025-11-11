from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class ImageChunk(_message.Message):
    __slots__ = ("data_chunk", "last_chunk")
    class DataChunk(_message.Message):
        __slots__ = ("bytes",)
        BYTES_FIELD_NUMBER: _ClassVar[int]
        bytes: bytes
        def __init__(self, bytes: bytes | None = ...) -> None: ...

    class LastChunk(_message.Message):
        __slots__ = ("file_name", "metadata")
        class MetadataEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: str | None = ..., value: str | None = ...
            ) -> None: ...

        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        METADATA_FIELD_NUMBER: _ClassVar[int]
        file_name: str
        metadata: _containers.ScalarMap[str, str]
        def __init__(
            self, file_name: str | None = ..., metadata: _Mapping[str, str] | None = ...
        ) -> None: ...

    DATA_CHUNK_FIELD_NUMBER: _ClassVar[int]
    LAST_CHUNK_FIELD_NUMBER: _ClassVar[int]
    data_chunk: ImageChunk.DataChunk
    last_chunk: ImageChunk.LastChunk
    def __init__(
        self,
        data_chunk: ImageChunk.DataChunk | _Mapping | None = ...,
        last_chunk: ImageChunk.LastChunk | _Mapping | None = ...,
    ) -> None: ...
