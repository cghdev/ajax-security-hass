from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space.security.group import (
    group_security_pb2 as _group_security_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GroupModeSpaceSecurity(_message.Message):
    __slots__ = ("groups", "night_mode_enabled")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[
        _group_security_pb2.GroupSecurity
    ]
    night_mode_enabled: bool
    def __init__(
        self,
        groups: _Iterable[_group_security_pb2.GroupSecurity | _Mapping] | None = ...,
        night_mode_enabled: bool = ...,
    ) -> None: ...
