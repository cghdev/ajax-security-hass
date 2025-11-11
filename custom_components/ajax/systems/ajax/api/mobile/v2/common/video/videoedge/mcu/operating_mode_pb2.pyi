from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class OperatingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPERATING_MODE_UNSPECIFIED: _ClassVar[OperatingMode]
    OPERATING_MODE_SMART_HOME: _ClassVar[OperatingMode]
    OPERATING_MODE_INTRUSION: _ClassVar[OperatingMode]

OPERATING_MODE_UNSPECIFIED: OperatingMode
OPERATING_MODE_SMART_HOME: OperatingMode
OPERATING_MODE_INTRUSION: OperatingMode
