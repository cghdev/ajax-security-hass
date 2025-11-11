from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class HubUserType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_TYPE_UNSPECIFIED: _ClassVar[HubUserType]
    USER: _ClassVar[HubUserType]
    PRO: _ClassVar[HubUserType]
    COMPANY: _ClassVar[HubUserType]

USER_TYPE_UNSPECIFIED: HubUserType
USER: HubUserType
PRO: HubUserType
COMPANY: HubUserType
