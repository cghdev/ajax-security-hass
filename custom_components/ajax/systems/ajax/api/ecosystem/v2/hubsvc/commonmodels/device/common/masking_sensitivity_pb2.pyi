from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class MaskingSensitivity(_message.Message):
    __slots__ = ("available_sensitivities", "sensitivity")
    class Sensitivity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SENSITIVITY_UNSPECIFIED: _ClassVar[MaskingSensitivity.Sensitivity]
        SENSITIVITY_LOW: _ClassVar[MaskingSensitivity.Sensitivity]
        SENSITIVITY_NORMAL: _ClassVar[MaskingSensitivity.Sensitivity]
        SENSITIVITY_HIGH: _ClassVar[MaskingSensitivity.Sensitivity]

    SENSITIVITY_UNSPECIFIED: MaskingSensitivity.Sensitivity
    SENSITIVITY_LOW: MaskingSensitivity.Sensitivity
    SENSITIVITY_NORMAL: MaskingSensitivity.Sensitivity
    SENSITIVITY_HIGH: MaskingSensitivity.Sensitivity
    class MaskingSensitivitySettings(_message.Message):
        __slots__ = ("sensitivity",)
        SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
        sensitivity: MaskingSensitivity.Sensitivity
        def __init__(
            self, sensitivity: MaskingSensitivity.Sensitivity | str | None = ...
        ) -> None: ...

    SENSITIVITY_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_SENSITIVITIES_FIELD_NUMBER: _ClassVar[int]
    sensitivity: MaskingSensitivity.Sensitivity
    available_sensitivities: _containers.RepeatedScalarFieldContainer[
        MaskingSensitivity.Sensitivity
    ]
    def __init__(
        self,
        sensitivity: MaskingSensitivity.Sensitivity | str | None = ...,
        available_sensitivities: _Iterable[MaskingSensitivity.Sensitivity | str]
        | None = ...,
    ) -> None: ...
