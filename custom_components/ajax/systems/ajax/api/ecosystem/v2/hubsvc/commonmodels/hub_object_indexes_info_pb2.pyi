from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class HubObjectIndexesInfo(_message.Message):
    __slots__ = ("range",)
    class Range(_message.Message):
        __slots__ = ("max_index", "min_index")
        MIN_INDEX_FIELD_NUMBER: _ClassVar[int]
        MAX_INDEX_FIELD_NUMBER: _ClassVar[int]
        min_index: int
        max_index: int
        def __init__(
            self, min_index: int | None = ..., max_index: int | None = ...
        ) -> None: ...

    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: HubObjectIndexesInfo.Range
    def __init__(
        self, range: HubObjectIndexesInfo.Range | _Mapping | None = ...
    ) -> None: ...
