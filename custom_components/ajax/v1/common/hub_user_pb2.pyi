from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import group_permissions_pb2 as _group_permissions_pb2
from v1.common import image_urls_pb2 as _image_urls_pb2
from v1.common import notification_settings_pb2 as _notification_settings_pb2
from v1.common import permission_pb2 as _permission_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2
from v1.common import restore_permission_pb2 as _restore_permission_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class HubUser(_message.Message):
    __slots__ = (
        "email",
        "first_name",
        "group_permissions",
        "id",
        "image_urls",
        "last_name",
        "notification_settings",
        "permissions",
        "phone",
        "restore_permissions",
        "role",
        "user_index",
    )
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        USER: _ClassVar[HubUser.Role]
        PRO: _ClassVar[HubUser.Role]
        COMPANY: _ClassVar[HubUser.Role]

    USER: HubUser.Role
    PRO: HubUser.Role
    COMPANY: HubUser.Role
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    RESTORE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: str
    last_name: str
    email: _email_address_pb2.EmailAddress
    phone: _phone_number_pb2.PhoneNumber
    image_urls: _image_urls_pb2.ImageUrls
    role: HubUser.Role
    permissions: _containers.RepeatedScalarFieldContainer[_permission_pb2.Permission]
    restore_permissions: _containers.RepeatedScalarFieldContainer[
        _restore_permission_pb2.RestorePermission
    ]
    group_permissions: _containers.RepeatedCompositeFieldContainer[
        _group_permissions_pb2.GroupPermissions
    ]
    notification_settings: _notification_settings_pb2.NotificationSettings
    user_index: _wrappers_pb2.Int32Value
    def __init__(
        self,
        id: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        email: _email_address_pb2.EmailAddress | _Mapping | None = ...,
        phone: _phone_number_pb2.PhoneNumber | _Mapping | None = ...,
        image_urls: _image_urls_pb2.ImageUrls | _Mapping | None = ...,
        role: HubUser.Role | str | None = ...,
        permissions: _Iterable[_permission_pb2.Permission | str] | None = ...,
        restore_permissions: _Iterable[_restore_permission_pb2.RestorePermission | str]
        | None = ...,
        group_permissions: _Iterable[_group_permissions_pb2.GroupPermissions | _Mapping]
        | None = ...,
        notification_settings: _notification_settings_pb2.NotificationSettings
        | _Mapping
        | None = ...,
        user_index: _wrappers_pb2.Int32Value | _Mapping | None = ...,
    ) -> None: ...
