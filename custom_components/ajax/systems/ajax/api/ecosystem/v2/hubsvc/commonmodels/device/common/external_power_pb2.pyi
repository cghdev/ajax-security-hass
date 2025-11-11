from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalPower(_message.Message):
    __slots__ = ("external_power_mode",)
    class ExternalPowerMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_POWER_MODE_UNSPECIFIED: _ClassVar[ExternalPower.ExternalPowerMode]
        EXTERNAL_POWER_MODE_CONNECTED: _ClassVar[ExternalPower.ExternalPowerMode]
        EXTERNAL_POWER_MODE_DISCONNECTED: _ClassVar[ExternalPower.ExternalPowerMode]

    EXTERNAL_POWER_MODE_UNSPECIFIED: ExternalPower.ExternalPowerMode
    EXTERNAL_POWER_MODE_CONNECTED: ExternalPower.ExternalPowerMode
    EXTERNAL_POWER_MODE_DISCONNECTED: ExternalPower.ExternalPowerMode
    EXTERNAL_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    external_power_mode: ExternalPower.ExternalPowerMode
    def __init__(
        self, external_power_mode: ExternalPower.ExternalPowerMode | str | None = ...
    ) -> None: ...
