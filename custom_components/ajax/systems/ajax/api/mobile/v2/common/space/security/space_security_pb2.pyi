from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space.security import (
    space_security_mode_pb2 as _space_security_mode_pb2,
)
from systems.ajax.api.mobile.v2.common.space.security.group import (
    group_pb2 as _group_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceSecurity(_message.Message):
    __slots__ = ("groups", "mode")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
    mode: _space_security_mode_pb2.SpaceSecurityMode
    def __init__(
        self,
        groups: _Iterable[_group_pb2.Group | _Mapping] | None = ...,
        mode: _space_security_mode_pb2.SpaceSecurityMode | _Mapping | None = ...,
    ) -> None: ...
