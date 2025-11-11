from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class AccelerometerSettings(_message.Message):
    __slots__ = ("accelerometer_types",)
    class AccelerometerTypeSettings(_message.Message):
        __slots__ = ("enabled", "movement", "shock")
        class Movement(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class Shock(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        ENABLED_FIELD_NUMBER: _ClassVar[int]
        MOVEMENT_FIELD_NUMBER: _ClassVar[int]
        SHOCK_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        movement: AccelerometerSettings.AccelerometerTypeSettings.Movement
        shock: AccelerometerSettings.AccelerometerTypeSettings.Shock
        def __init__(
            self,
            enabled: bool = ...,
            movement: AccelerometerSettings.AccelerometerTypeSettings.Movement
            | _Mapping
            | None = ...,
            shock: AccelerometerSettings.AccelerometerTypeSettings.Shock
            | _Mapping
            | None = ...,
        ) -> None: ...

    ACCELEROMETER_TYPES_FIELD_NUMBER: _ClassVar[int]
    accelerometer_types: _containers.RepeatedCompositeFieldContainer[
        AccelerometerSettings.AccelerometerTypeSettings
    ]
    def __init__(
        self,
        accelerometer_types: _Iterable[
            AccelerometerSettings.AccelerometerTypeSettings | _Mapping
        ]
        | None = ...,
    ) -> None: ...
