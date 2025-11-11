from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NO_NOTIFICATION_CHANNEL_INFO: _ClassVar[NotificationChannel]
    PUSH: _ClassVar[NotificationChannel]
    SMS: _ClassVar[NotificationChannel]
    CALL: _ClassVar[NotificationChannel]

NO_NOTIFICATION_CHANNEL_INFO: NotificationChannel
PUSH: NotificationChannel
SMS: NotificationChannel
CALL: NotificationChannel
