from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayGroups(_message.Message):
    __slots__ = ("groups",)
    class Group(_message.Message):
        __slots__ = ("group_hex_id", "group_name")
        GROUP_HEX_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
        group_hex_id: str
        group_name: str
        def __init__(
            self, group_hex_id: str | None = ..., group_name: str | None = ...
        ) -> None: ...

    GROUPS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[DisplayGroups.Group]
    def __init__(
        self, groups: _Iterable[DisplayGroups.Group | _Mapping] | None = ...
    ) -> None: ...
