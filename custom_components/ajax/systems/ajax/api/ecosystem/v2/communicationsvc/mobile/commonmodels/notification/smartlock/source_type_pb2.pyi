from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class SmartLockNotificationSourceType(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = ()
    SMART_LOCK_NOTIFICATION_SOURCE_TYPE_UNSPECIFIED: _ClassVar[
        SmartLockNotificationSourceType
    ]
    SMART_LOCK: _ClassVar[SmartLockNotificationSourceType]

SMART_LOCK_NOTIFICATION_SOURCE_TYPE_UNSPECIFIED: SmartLockNotificationSourceType
SMART_LOCK: SmartLockNotificationSourceType
