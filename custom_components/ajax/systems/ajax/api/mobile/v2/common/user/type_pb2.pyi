from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class UserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[UserType]
    USER: _ClassVar[UserType]
    PRO: _ClassVar[UserType]
    COMPANY: _ClassVar[UserType]

NONE: UserType
USER: UserType
PRO: UserType
COMPANY: UserType
