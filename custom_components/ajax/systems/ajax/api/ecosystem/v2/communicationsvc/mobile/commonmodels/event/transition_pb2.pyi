from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class EventTransition(_message.Message):
    __slots__ = ("impulse", "recovered", "triggered")
    class Triggered(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Recovered(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Impulse(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    RECOVERED_FIELD_NUMBER: _ClassVar[int]
    IMPULSE_FIELD_NUMBER: _ClassVar[int]
    triggered: EventTransition.Triggered
    recovered: EventTransition.Recovered
    impulse: EventTransition.Impulse
    def __init__(
        self,
        triggered: EventTransition.Triggered | _Mapping | None = ...,
        recovered: EventTransition.Recovered | _Mapping | None = ...,
        impulse: EventTransition.Impulse | _Mapping | None = ...,
    ) -> None: ...
