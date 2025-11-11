from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class FacilitySearchRequest(_message.Message):
    __slots__ = ("limit", "offset", "search_phrase")
    SEARCH_PHRASE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    search_phrase: str
    limit: int
    offset: int
    def __init__(
        self,
        search_phrase: str | None = ...,
        limit: int | None = ...,
        offset: int | None = ...,
    ) -> None: ...
