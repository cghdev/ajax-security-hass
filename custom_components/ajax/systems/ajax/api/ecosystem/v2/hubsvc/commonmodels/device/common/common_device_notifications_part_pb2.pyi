from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class CommonDeviceNotificationsPart(_message.Message):
    __slots__ = ("device_notifications",)
    class NotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFICATION_TYPE_UNSPECIFIED: _ClassVar[
            CommonDeviceNotificationsPart.NotificationType
        ]
        NOTIFICATION_TYPE_INCORRECT_DEVICE_INSTALLATION: _ClassVar[
            CommonDeviceNotificationsPart.NotificationType
        ]
        NOTIFICATION_TYPE_BATTERY_FAILED_CHARGE: _ClassVar[
            CommonDeviceNotificationsPart.NotificationType
        ]
        NOTIFICATION_TYPE_BATTERY_FAILED_LOAD_TEST: _ClassVar[
            CommonDeviceNotificationsPart.NotificationType
        ]

    NOTIFICATION_TYPE_UNSPECIFIED: CommonDeviceNotificationsPart.NotificationType
    NOTIFICATION_TYPE_INCORRECT_DEVICE_INSTALLATION: (
        CommonDeviceNotificationsPart.NotificationType
    )
    NOTIFICATION_TYPE_BATTERY_FAILED_CHARGE: (
        CommonDeviceNotificationsPart.NotificationType
    )
    NOTIFICATION_TYPE_BATTERY_FAILED_LOAD_TEST: (
        CommonDeviceNotificationsPart.NotificationType
    )
    class IsEnabled(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IS_ENABLED_UNSPECIFIED: _ClassVar[CommonDeviceNotificationsPart.IsEnabled]
        IS_ENABLED_DISABLED: _ClassVar[CommonDeviceNotificationsPart.IsEnabled]
        IS_ENABLED_ENABLED: _ClassVar[CommonDeviceNotificationsPart.IsEnabled]

    IS_ENABLED_UNSPECIFIED: CommonDeviceNotificationsPart.IsEnabled
    IS_ENABLED_DISABLED: CommonDeviceNotificationsPart.IsEnabled
    IS_ENABLED_ENABLED: CommonDeviceNotificationsPart.IsEnabled
    class DeviceNotificationsPartSettings(_message.Message):
        __slots__ = ("device_notifications",)
        DEVICE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
        device_notifications: _containers.RepeatedCompositeFieldContainer[
            CommonDeviceNotificationsPart.Notification
        ]
        def __init__(
            self,
            device_notifications: _Iterable[
                CommonDeviceNotificationsPart.Notification | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Notification(_message.Message):
        __slots__ = ("is_enabled", "notification_type")
        NOTIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        notification_type: CommonDeviceNotificationsPart.NotificationType
        is_enabled: CommonDeviceNotificationsPart.IsEnabled
        def __init__(
            self,
            notification_type: CommonDeviceNotificationsPart.NotificationType
            | str
            | None = ...,
            is_enabled: CommonDeviceNotificationsPart.IsEnabled | str | None = ...,
        ) -> None: ...

    DEVICE_NOTIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    device_notifications: _containers.RepeatedCompositeFieldContainer[
        CommonDeviceNotificationsPart.Notification
    ]
    def __init__(
        self,
        device_notifications: _Iterable[
            CommonDeviceNotificationsPart.Notification | _Mapping
        ]
        | None = ...,
    ) -> None: ...
