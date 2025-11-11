from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class GroupAssociation(_message.Message):
    __slots__ = ("capabilities", "group_associated")
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[GroupAssociation.Capability]
        CAPABILITY_GROUP_ASSOCIATED: _ClassVar[GroupAssociation.Capability]

    CAPABILITY_UNSPECIFIED: GroupAssociation.Capability
    CAPABILITY_GROUP_ASSOCIATED: GroupAssociation.Capability
    class GroupsAssociated(_message.Message):
        __slots__ = ("all", "group_associated")
        class All(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        GROUP_ASSOCIATED_FIELD_NUMBER: _ClassVar[int]
        ALL_FIELD_NUMBER: _ClassVar[int]
        group_associated: str
        all: GroupAssociation.GroupsAssociated.All
        def __init__(
            self,
            group_associated: str | None = ...,
            all: GroupAssociation.GroupsAssociated.All | _Mapping | None = ...,
        ) -> None: ...

    class GroupAssociationSettings(_message.Message):
        __slots__ = ("group_associated",)
        GROUP_ASSOCIATED_FIELD_NUMBER: _ClassVar[int]
        group_associated: GroupAssociation.GroupsAssociated
        def __init__(
            self,
            group_associated: GroupAssociation.GroupsAssociated | _Mapping | None = ...,
        ) -> None: ...

    GROUP_ASSOCIATED_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    group_associated: GroupAssociation.GroupsAssociated
    capabilities: _containers.RepeatedScalarFieldContainer[GroupAssociation.Capability]
    def __init__(
        self,
        group_associated: GroupAssociation.GroupsAssociated | _Mapping | None = ...,
        capabilities: _Iterable[GroupAssociation.Capability | str] | None = ...,
    ) -> None: ...
