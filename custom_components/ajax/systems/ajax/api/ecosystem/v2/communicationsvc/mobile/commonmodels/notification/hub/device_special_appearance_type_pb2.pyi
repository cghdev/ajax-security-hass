from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceSpecialAppearanceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEVICE_SPECIAL_APPEARANCE_TYPE_UNSPECIFIED: _ClassVar[DeviceSpecialAppearanceType]
    DEVICE_SPECIAL_APPEARANCE_TYPE_UK: _ClassVar[DeviceSpecialAppearanceType]

DEVICE_SPECIAL_APPEARANCE_TYPE_UNSPECIFIED: DeviceSpecialAppearanceType
DEVICE_SPECIAL_APPEARANCE_TYPE_UK: DeviceSpecialAppearanceType
