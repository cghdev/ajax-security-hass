from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Pagination(_message.Message):
    __slots__ = ("forward_exclusive_pagination_token",)
    FORWARD_EXCLUSIVE_PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    forward_exclusive_pagination_token: str
    def __init__(
        self, forward_exclusive_pagination_token: str | None = ...
    ) -> None: ...
