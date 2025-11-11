from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v1.common import permission_pb2 as _permission_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class AccessRights(_message.Message):
    __slots__ = ("access_type", "expiration_seconds", "permissions")
    class AccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXPIRED: _ClassVar[AccessRights.AccessType]
        PERMANENT: _ClassVar[AccessRights.AccessType]
        VALID: _ClassVar[AccessRights.AccessType]

    EXPIRED: AccessRights.AccessType
    PERMANENT: AccessRights.AccessType
    VALID: AccessRights.AccessType
    EXPIRATION_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    expiration_seconds: int
    access_type: AccessRights.AccessType
    permissions: _containers.RepeatedScalarFieldContainer[_permission_pb2.Permission]
    def __init__(
        self,
        expiration_seconds: int | None = ...,
        access_type: AccessRights.AccessType | str | None = ...,
        permissions: _Iterable[_permission_pb2.Permission | str] | None = ...,
    ) -> None: ...
