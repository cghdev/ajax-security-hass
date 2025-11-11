from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class BatterySaveModeStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BATTERY_SAVE_MODE_STATUS_UNSPECIFIED: _ClassVar[BatterySaveModeStatus]
    BATTERY_SAVE_MODE_STATUS_NORMAL: _ClassVar[BatterySaveModeStatus]
    BATTERY_SAVE_MODE_STATUS_BATTERY_SAVING: _ClassVar[BatterySaveModeStatus]

BATTERY_SAVE_MODE_STATUS_UNSPECIFIED: BatterySaveModeStatus
BATTERY_SAVE_MODE_STATUS_NORMAL: BatterySaveModeStatus
BATTERY_SAVE_MODE_STATUS_BATTERY_SAVING: BatterySaveModeStatus
