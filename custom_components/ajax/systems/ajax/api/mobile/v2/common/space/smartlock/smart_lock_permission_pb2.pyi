from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SMART_LOCK_PERMISSION_UNSPECIFIED: _ClassVar[SmartLockPermission]
    SMART_LOCK_PERMISSION_MANAGE_LOCK: _ClassVar[SmartLockPermission]

SMART_LOCK_PERMISSION_UNSPECIFIED: SmartLockPermission
SMART_LOCK_PERMISSION_MANAGE_LOCK: SmartLockPermission
