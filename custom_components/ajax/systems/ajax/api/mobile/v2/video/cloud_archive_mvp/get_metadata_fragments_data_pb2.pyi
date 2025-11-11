from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class CloudArchiveGetMetadataFragmentsDataRequest(_message.Message):
    __slots__ = ("entries", "session_id", "tag")
    class Entry(_message.Message):
        __slots__ = ("fragment_id",)
        FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
        fragment_id: int
        def __init__(self, fragment_id: int | None = ...) -> None: ...

    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    tag: str
    entries: _containers.RepeatedCompositeFieldContainer[
        CloudArchiveGetMetadataFragmentsDataRequest.Entry
    ]
    def __init__(
        self,
        session_id: str | None = ...,
        tag: str | None = ...,
        entries: _Iterable[CloudArchiveGetMetadataFragmentsDataRequest.Entry | _Mapping]
        | None = ...,
    ) -> None: ...
