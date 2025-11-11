from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeArmingStateAction(_message.Message):
    __slots__ = ("action_type", "targets")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[ChangeArmingStateAction.ActionType]
        ACTION_TYPE_DISARM: _ClassVar[ChangeArmingStateAction.ActionType]
        ACTION_TYPE_ARM: _ClassVar[ChangeArmingStateAction.ActionType]

    ACTION_TYPE_UNSPECIFIED: ChangeArmingStateAction.ActionType
    ACTION_TYPE_DISARM: ChangeArmingStateAction.ActionType
    ACTION_TYPE_ARM: ChangeArmingStateAction.ActionType
    class Target(_message.Message):
        __slots__ = ("group", "space")
        class Space(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class Group(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: str
            def __init__(self, id: str | None = ...) -> None: ...

        SPACE_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        space: ChangeArmingStateAction.Target.Space
        group: ChangeArmingStateAction.Target.Group
        def __init__(
            self,
            space: ChangeArmingStateAction.Target.Space | _Mapping | None = ...,
            group: ChangeArmingStateAction.Target.Group | _Mapping | None = ...,
        ) -> None: ...

    TARGETS_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    targets: _containers.RepeatedCompositeFieldContainer[ChangeArmingStateAction.Target]
    action_type: ChangeArmingStateAction.ActionType
    def __init__(
        self,
        targets: _Iterable[ChangeArmingStateAction.Target | _Mapping] | None = ...,
        action_type: ChangeArmingStateAction.ActionType | str | None = ...,
    ) -> None: ...
