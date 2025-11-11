from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class AlwaysActive(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALWAYS_ACTIVE_UNSPECIFIED: _ClassVar[AlwaysActive]
    ALWAYS_ACTIVE_DISABLED: _ClassVar[AlwaysActive]
    ALWAYS_ACTIVE_ENABLED: _ClassVar[AlwaysActive]

ALWAYS_ACTIVE_UNSPECIFIED: AlwaysActive
ALWAYS_ACTIVE_DISABLED: AlwaysActive
ALWAYS_ACTIVE_ENABLED: AlwaysActive
