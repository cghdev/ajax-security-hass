from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.common import permission_pb2 as _permission_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class InstallersCompanyPermissionsResponse(_message.Message):
    __slots__ = ("permissions",)
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedScalarFieldContainer[_permission_pb2.Permission]
    def __init__(
        self, permissions: _Iterable[_permission_pb2.Permission | str] | None = ...
    ) -> None: ...
