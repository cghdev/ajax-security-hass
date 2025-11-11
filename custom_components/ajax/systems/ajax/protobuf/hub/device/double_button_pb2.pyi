from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub.device import common_device_pb2 as _common_device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DoubleButton(_message.Message):
    __slots__ = (
        "associated_user_id",
        "brightness",
        "common_part",
        "siren_triggers",
        "subtype",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SIREN_TRIGGER_INFO: _ClassVar[DoubleButton.SirenTrigger]
        SECURITY_BUTTON: _ClassVar[DoubleButton.SirenTrigger]

    NO_SIREN_TRIGGER_INFO: DoubleButton.SirenTrigger
    SECURITY_BUTTON: DoubleButton.SirenTrigger
    class Brightness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BRIGHTNESS_INFO: _ClassVar[DoubleButton.Brightness]
        OFF: _ClassVar[DoubleButton.Brightness]
        LOW: _ClassVar[DoubleButton.Brightness]
        HIGH: _ClassVar[DoubleButton.Brightness]

    NO_BRIGHTNESS_INFO: DoubleButton.Brightness
    OFF: DoubleButton.Brightness
    LOW: DoubleButton.Brightness
    HIGH: DoubleButton.Brightness
    class Subtype(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SUBTYPE: _ClassVar[DoubleButton.Subtype]

    NO_SUBTYPE: DoubleButton.Subtype
    COMMON_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    common_part: _common_device_pb2.CommonDevicePart
    siren_triggers: _containers.RepeatedScalarFieldContainer[DoubleButton.SirenTrigger]
    brightness: DoubleButton.Brightness
    associated_user_id: str
    subtype: DoubleButton.Subtype
    def __init__(
        self,
        common_part: _common_device_pb2.CommonDevicePart | _Mapping | None = ...,
        siren_triggers: _Iterable[DoubleButton.SirenTrigger | str] | None = ...,
        brightness: DoubleButton.Brightness | str | None = ...,
        associated_user_id: str | None = ...,
        subtype: DoubleButton.Subtype | str | None = ...,
    ) -> None: ...
