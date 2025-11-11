from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class Initiator(_message.Message):
    __slots__ = ("id", "name", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNSPECIFIED: _ClassVar[Initiator.Type]
        TYPE_EXTERNAL_USER: _ClassVar[Initiator.Type]
        TYPE_SPACE_MEMBER: _ClassVar[Initiator.Type]
        TYPE_SCENARIO: _ClassVar[Initiator.Type]

    TYPE_UNSPECIFIED: Initiator.Type
    TYPE_EXTERNAL_USER: Initiator.Type
    TYPE_SPACE_MEMBER: Initiator.Type
    TYPE_SCENARIO: Initiator.Type
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: Initiator.Type
    name: str
    def __init__(
        self,
        id: str | None = ...,
        type: Initiator.Type | str | None = ...,
        name: str | None = ...,
    ) -> None: ...
