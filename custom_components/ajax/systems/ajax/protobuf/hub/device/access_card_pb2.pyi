from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AccessCard(_message.Message):
    __slots__ = (
        "app_id",
        "associated_user_id",
        "attribute",
        "card_UID",
        "card_enabled",
        "card_key_seed",
        "card_record",
        "device_index",
        "full_arm",
        "group_permissions",
        "id",
        "name",
        "perimeter_arm",
    )
    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WHITE: _ClassVar[AccessCard.Color]
        BLACK: _ClassVar[AccessCard.Color]

    WHITE: AccessCard.Color
    BLACK: AccessCard.Color
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CARD: _ClassVar[AccessCard.Type]
        TAG: _ClassVar[AccessCard.Type]

    CARD: AccessCard.Type
    TAG: AccessCard.Type
    class GroupPermissions(_message.Message):
        __slots__ = ("group_id", "permissions")
        class Permission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NO_PERMISSION_INFO: _ClassVar[AccessCard.GroupPermissions.Permission]
            ARM: _ClassVar[AccessCard.GroupPermissions.Permission]
            DISARM: _ClassVar[AccessCard.GroupPermissions.Permission]

        NO_PERMISSION_INFO: AccessCard.GroupPermissions.Permission
        ARM: AccessCard.GroupPermissions.Permission
        DISARM: AccessCard.GroupPermissions.Permission
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
        group_id: str
        permissions: _containers.RepeatedScalarFieldContainer[
            AccessCard.GroupPermissions.Permission
        ]
        def __init__(
            self,
            group_id: str | None = ...,
            permissions: _Iterable[AccessCard.GroupPermissions.Permission | str]
            | None = ...,
        ) -> None: ...

    class Attribute(_message.Message):
        __slots__ = ("color", "type")
        COLOR_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        color: AccessCard.Color
        type: AccessCard.Type
        def __init__(
            self,
            color: AccessCard.Color | str | None = ...,
            type: AccessCard.Type | str | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CARD_RECORD_FIELD_NUMBER: _ClassVar[int]
    CARD_UID_FIELD_NUMBER: _ClassVar[int]
    CARD_KEY_SEED_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    PERIMETER_ARM_FIELD_NUMBER: _ClassVar[int]
    FULL_ARM_FIELD_NUMBER: _ClassVar[int]
    CARD_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    card_record: int
    card_UID: int
    card_key_seed: int
    app_id: int
    group_permissions: _containers.RepeatedCompositeFieldContainer[
        AccessCard.GroupPermissions
    ]
    associated_user_id: str
    device_index: int
    perimeter_arm: bool
    full_arm: bool
    card_enabled: bool
    attribute: AccessCard.Attribute
    def __init__(
        self,
        id: str | None = ...,
        name: _name_pb2.Name | _Mapping | None = ...,
        card_record: int | None = ...,
        card_UID: int | None = ...,
        card_key_seed: int | None = ...,
        app_id: int | None = ...,
        group_permissions: _Iterable[AccessCard.GroupPermissions | _Mapping]
        | None = ...,
        associated_user_id: str | None = ...,
        device_index: int | None = ...,
        perimeter_arm: bool = ...,
        full_arm: bool = ...,
        card_enabled: bool = ...,
        attribute: AccessCard.Attribute | _Mapping | None = ...,
    ) -> None: ...
