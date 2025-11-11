from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub import image_urls_pb2 as _image_urls_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = (
        "agreement_version",
        "attached_company_id",
        "email",
        "first_name",
        "group_permissions",
        "hub_binding_role",
        "id",
        "image_id",
        "image_urls",
        "index",
        "keypad_prefix",
        "language",
        "notification_settings",
        "password_hash",
        "password_hash_duress",
        "permissions",
        "phone",
        "restore_permissions",
    )
    class HubBindingRole(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_ROLE_INFO: _ClassVar[User.HubBindingRole]
        USER: _ClassVar[User.HubBindingRole]
        MASTER: _ClassVar[User.HubBindingRole]
        PRO: _ClassVar[User.HubBindingRole]
        COMPANY: _ClassVar[User.HubBindingRole]

    NO_ROLE_INFO: User.HubBindingRole
    USER: User.HubBindingRole
    MASTER: User.HubBindingRole
    PRO: User.HubBindingRole
    COMPANY: User.HubBindingRole
    class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESERVED_0: _ClassVar[User.Permission]
        USER_DELETE: _ClassVar[User.Permission]
        USER_ADD: _ClassVar[User.Permission]
        USER_ROLE_UPDATE: _ClassVar[User.Permission]
        USER_PERMISSIONS_UPDATE: _ClassVar[User.Permission]
        USER_NOTIFICATION_SETTINGS_UPDATE: _ClassVar[User.Permission]
        RESERVED_6: _ClassVar[User.Permission]
        RESERVED_7: _ClassVar[User.Permission]
        ARM: _ClassVar[User.Permission]
        NIGHT_MODE: _ClassVar[User.Permission]
        DISARM: _ClassVar[User.Permission]
        PANIC: _ClassVar[User.Permission]
        ROOM_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        DEVICE_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        HUB_NET_SETTINGS_UPDATE: _ClassVar[User.Permission]
        HUB_OTHER_SETTINGS_UPDATE: _ClassVar[User.Permission]
        STATE_COMMANDS: _ClassVar[User.Permission]
        FIRMWARE_COMMANDS: _ClassVar[User.Permission]
        CAMERA_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        CAMERA_GET: _ClassVar[User.Permission]
        GROUP_ADD_UPDATE_DELETE: _ClassVar[User.Permission]
        EVENTS_GET: _ClassVar[User.Permission]
        GET: _ClassVar[User.Permission]
        SCENARIO: _ClassVar[User.Permission]
        CHIMES_UPDATE: _ClassVar[User.Permission]
        PRIVACY_ACCESS_SETTINGS: _ClassVar[User.Permission]
        RESERVED_26: _ClassVar[User.Permission]
        RESERVED_27: _ClassVar[User.Permission]
        RESERVED_28: _ClassVar[User.Permission]
        RESERVED_29: _ClassVar[User.Permission]
        RESERVED_30: _ClassVar[User.Permission]
        RESERVED_31: _ClassVar[User.Permission]

    RESERVED_0: User.Permission
    USER_DELETE: User.Permission
    USER_ADD: User.Permission
    USER_ROLE_UPDATE: User.Permission
    USER_PERMISSIONS_UPDATE: User.Permission
    USER_NOTIFICATION_SETTINGS_UPDATE: User.Permission
    RESERVED_6: User.Permission
    RESERVED_7: User.Permission
    ARM: User.Permission
    NIGHT_MODE: User.Permission
    DISARM: User.Permission
    PANIC: User.Permission
    ROOM_ADD_UPDATE_DELETE: User.Permission
    DEVICE_ADD_UPDATE_DELETE: User.Permission
    HUB_NET_SETTINGS_UPDATE: User.Permission
    HUB_OTHER_SETTINGS_UPDATE: User.Permission
    STATE_COMMANDS: User.Permission
    FIRMWARE_COMMANDS: User.Permission
    CAMERA_ADD_UPDATE_DELETE: User.Permission
    CAMERA_GET: User.Permission
    GROUP_ADD_UPDATE_DELETE: User.Permission
    EVENTS_GET: User.Permission
    GET: User.Permission
    SCENARIO: User.Permission
    CHIMES_UPDATE: User.Permission
    PRIVACY_ACCESS_SETTINGS: User.Permission
    RESERVED_26: User.Permission
    RESERVED_27: User.Permission
    RESERVED_28: User.Permission
    RESERVED_29: User.Permission
    RESERVED_30: User.Permission
    RESERVED_31: User.Permission
    class RestorePermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_RESTORE_PERMISSION_INFO: _ClassVar[User.RestorePermission]
        RESTORE_CONFIRMED_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_CONFIRMED_HU_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_UNCONFIRMED_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_UNCONFIRMED_HU_ALARMS: _ClassVar[User.RestorePermission]
        RESTORE_TAMPER_ACTIVATION: _ClassVar[User.RestorePermission]
        RESTORE_EXTERNAL_POWER_ACTIVATION: _ClassVar[User.RestorePermission]
        RESTORE_ATS_ACTIVATION: _ClassVar[User.RestorePermission]
        RESTORE_OTHER_FAULT_ACTIVATION: _ClassVar[User.RestorePermission]

    NO_RESTORE_PERMISSION_INFO: User.RestorePermission
    RESTORE_CONFIRMED_ALARMS: User.RestorePermission
    RESTORE_CONFIRMED_HU_ALARMS: User.RestorePermission
    RESTORE_UNCONFIRMED_ALARMS: User.RestorePermission
    RESTORE_UNCONFIRMED_HU_ALARMS: User.RestorePermission
    RESTORE_TAMPER_ACTIVATION: User.RestorePermission
    RESTORE_EXTERNAL_POWER_ACTIVATION: User.RestorePermission
    RESTORE_ATS_ACTIVATION: User.RestorePermission
    RESTORE_OTHER_FAULT_ACTIVATION: User.RestorePermission
    class NotificationSettings(_message.Message):
        __slots__ = ("alarms", "armings", "events", "malfunctions")
        class NotificationChannel(_message.Message):
            __slots__ = ()
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_NOTIFICATION_CHANNEL_INFO: _ClassVar[
                    User.NotificationSettings.NotificationChannel.Type
                ]
                PUSH: _ClassVar[User.NotificationSettings.NotificationChannel.Type]
                SMS: _ClassVar[User.NotificationSettings.NotificationChannel.Type]
                CALL: _ClassVar[User.NotificationSettings.NotificationChannel.Type]

            NO_NOTIFICATION_CHANNEL_INFO: (
                User.NotificationSettings.NotificationChannel.Type
            )
            PUSH: User.NotificationSettings.NotificationChannel.Type
            SMS: User.NotificationSettings.NotificationChannel.Type
            CALL: User.NotificationSettings.NotificationChannel.Type
            def __init__(self) -> None: ...

        class MessageNotificationChannel(_message.Message):
            __slots__ = ()
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                NO_MESSAGE_NOTIFICATION_CHANNEL_INFO: _ClassVar[
                    User.NotificationSettings.MessageNotificationChannel.Type
                ]
                PUSH: _ClassVar[
                    User.NotificationSettings.MessageNotificationChannel.Type
                ]
                SMS: _ClassVar[
                    User.NotificationSettings.MessageNotificationChannel.Type
                ]

            NO_MESSAGE_NOTIFICATION_CHANNEL_INFO: (
                User.NotificationSettings.MessageNotificationChannel.Type
            )
            PUSH: User.NotificationSettings.MessageNotificationChannel.Type
            SMS: User.NotificationSettings.MessageNotificationChannel.Type
            def __init__(self) -> None: ...

        ALARMS_FIELD_NUMBER: _ClassVar[int]
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        ARMINGS_FIELD_NUMBER: _ClassVar[int]
        alarms: _containers.RepeatedScalarFieldContainer[
            User.NotificationSettings.NotificationChannel.Type
        ]
        events: _containers.RepeatedScalarFieldContainer[
            User.NotificationSettings.MessageNotificationChannel.Type
        ]
        malfunctions: _containers.RepeatedScalarFieldContainer[
            User.NotificationSettings.MessageNotificationChannel.Type
        ]
        armings: _containers.RepeatedScalarFieldContainer[
            User.NotificationSettings.MessageNotificationChannel.Type
        ]
        def __init__(
            self,
            alarms: _Iterable[User.NotificationSettings.NotificationChannel.Type | str]
            | None = ...,
            events: _Iterable[
                User.NotificationSettings.MessageNotificationChannel.Type | str
            ]
            | None = ...,
            malfunctions: _Iterable[
                User.NotificationSettings.MessageNotificationChannel.Type | str
            ]
            | None = ...,
            armings: _Iterable[
                User.NotificationSettings.MessageNotificationChannel.Type | str
            ]
            | None = ...,
        ) -> None: ...

    class GroupPermissions(_message.Message):
        __slots__ = ("group_id", "permissions")
        class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_PERMISSION_INFO: _ClassVar[User.GroupPermissions.Permission]
            ARM: _ClassVar[User.GroupPermissions.Permission]
            DISARM: _ClassVar[User.GroupPermissions.Permission]

        NO_PERMISSION_INFO: User.GroupPermissions.Permission
        ARM: User.GroupPermissions.Permission
        DISARM: User.GroupPermissions.Permission
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        permissions: _containers.RepeatedScalarFieldContainer[
            User.GroupPermissions.Permission
        ]
        def __init__(
            self,
            group_id: str | None = ...,
            permissions: _Iterable[User.GroupPermissions.Permission | str] | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    ATTACHED_COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_BINDING_ROLE_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_HASH_DURESS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: str
    email: str
    phone: str
    language: str
    index: int
    agreement_version: int
    attached_company_id: str
    permissions: _containers.RepeatedScalarFieldContainer[User.Permission]
    hub_binding_role: User.HubBindingRole
    restore_permissions: _containers.RepeatedScalarFieldContainer[
        User.RestorePermission
    ]
    password_hash: str
    password_hash_duress: str
    image_id: str
    keypad_prefix: str
    image_urls: _image_urls_pb2.ImageUrls
    notification_settings: User.NotificationSettings
    group_permissions: _containers.RepeatedCompositeFieldContainer[
        User.GroupPermissions
    ]
    def __init__(
        self,
        id: str | None = ...,
        first_name: str | None = ...,
        email: str | None = ...,
        phone: str | None = ...,
        language: str | None = ...,
        index: int | None = ...,
        agreement_version: int | None = ...,
        attached_company_id: str | None = ...,
        permissions: _Iterable[User.Permission | str] | None = ...,
        hub_binding_role: User.HubBindingRole | str | None = ...,
        restore_permissions: _Iterable[User.RestorePermission | str] | None = ...,
        password_hash: str | None = ...,
        password_hash_duress: str | None = ...,
        image_id: str | None = ...,
        keypad_prefix: str | None = ...,
        image_urls: _image_urls_pb2.ImageUrls | _Mapping | None = ...,
        notification_settings: User.NotificationSettings | _Mapping | None = ...,
        group_permissions: _Iterable[User.GroupPermissions | _Mapping] | None = ...,
    ) -> None: ...
