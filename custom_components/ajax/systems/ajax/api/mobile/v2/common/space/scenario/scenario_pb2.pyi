from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.space.scenario.action import (
    action_pb2 as _action_pb2,
)
from systems.ajax.api.mobile.v2.common.space.scenario.trigger import (
    trigger_pb2 as _trigger_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Scenario(_message.Message):
    __slots__ = ("cases", "enabled", "id", "name")
    class Case(_message.Message):
        __slots__ = ("action", "trigger")
        TRIGGER_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        trigger: _trigger_pb2.Trigger
        action: _action_pb2.Action
        def __init__(
            self,
            trigger: _trigger_pb2.Trigger | _Mapping | None = ...,
            action: _action_pb2.Action | _Mapping | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CASES_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    enabled: bool
    cases: _containers.RepeatedCompositeFieldContainer[Scenario.Case]
    def __init__(
        self,
        id: str | None = ...,
        name: str | None = ...,
        enabled: bool = ...,
        cases: _Iterable[Scenario.Case | _Mapping] | None = ...,
    ) -> None: ...
