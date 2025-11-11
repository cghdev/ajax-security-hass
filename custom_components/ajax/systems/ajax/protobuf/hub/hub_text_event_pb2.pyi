from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class HubTextEvent(_message.Message):
    __slots__ = ("parameter",)
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    parameter: _containers.RepeatedCompositeFieldContainer[HubParameter]
    def __init__(
        self, parameter: _Iterable[HubParameter | _Mapping] | None = ...
    ) -> None: ...

class HubParameter(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    def __init__(self, name: str | None = ..., value: str | None = ...) -> None: ...
