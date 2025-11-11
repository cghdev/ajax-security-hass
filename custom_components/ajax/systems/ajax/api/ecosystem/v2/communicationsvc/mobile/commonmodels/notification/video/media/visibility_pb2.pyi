from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class VideoMediaVisibility(_message.Message):
    __slots__ = ("allowed_for_everyone", "whitelist")
    class Whitelist(_message.Message):
        __slots__ = ("allowed_member_ids",)
        ALLOWED_MEMBER_IDS_FIELD_NUMBER: _ClassVar[int]
        allowed_member_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, allowed_member_ids: _Iterable[str] | None = ...) -> None: ...

    class AllowedForEveryone(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    WHITELIST_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FOR_EVERYONE_FIELD_NUMBER: _ClassVar[int]
    whitelist: VideoMediaVisibility.Whitelist
    allowed_for_everyone: VideoMediaVisibility.AllowedForEveryone
    def __init__(
        self,
        whitelist: VideoMediaVisibility.Whitelist | _Mapping | None = ...,
        allowed_for_everyone: VideoMediaVisibility.AllowedForEveryone
        | _Mapping
        | None = ...,
    ) -> None: ...
