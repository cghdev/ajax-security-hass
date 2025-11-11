from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class LightIndication(_message.Message):
    __slots__ = ("capabilities", "light_indication_settings")
    class Indication(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INDICATION_UNSPECIFIED: _ClassVar[LightIndication.Indication]
        INDICATION_OFF: _ClassVar[LightIndication.Indication]
        INDICATION_ARMED: _ClassVar[LightIndication.Indication]
        INDICATION_ALWAYS: _ClassVar[LightIndication.Indication]

    INDICATION_UNSPECIFIED: LightIndication.Indication
    INDICATION_OFF: LightIndication.Indication
    INDICATION_ARMED: LightIndication.Indication
    INDICATION_ALWAYS: LightIndication.Indication
    class ExternalLedMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_LED_MODE_UNSPECIFIED: _ClassVar[LightIndication.ExternalLedMode]
        EXTERNAL_LED_MODE_BLINK: _ClassVar[LightIndication.ExternalLedMode]
        EXTERNAL_LED_MODE_SHINE_CONSTANTLY: _ClassVar[LightIndication.ExternalLedMode]

    EXTERNAL_LED_MODE_UNSPECIFIED: LightIndication.ExternalLedMode
    EXTERNAL_LED_MODE_BLINK: LightIndication.ExternalLedMode
    EXTERNAL_LED_MODE_SHINE_CONSTANTLY: LightIndication.ExternalLedMode
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[LightIndication.Capability]
        CAPABILITY_NEW_ARM_MODE_INDICATION: _ClassVar[LightIndication.Capability]
        CAPABILITY_EXTERNAL_LED_INDICATION_TYPE: _ClassVar[LightIndication.Capability]

    CAPABILITY_UNSPECIFIED: LightIndication.Capability
    CAPABILITY_NEW_ARM_MODE_INDICATION: LightIndication.Capability
    CAPABILITY_EXTERNAL_LED_INDICATION_TYPE: LightIndication.Capability
    class LightIndicationSettings(_message.Message):
        __slots__ = ("external_led_mode", "light_indication")
        LIGHT_INDICATION_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_LED_MODE_FIELD_NUMBER: _ClassVar[int]
        light_indication: LightIndication.Indication
        external_led_mode: LightIndication.ExternalLedMode
        def __init__(
            self,
            light_indication: LightIndication.Indication | str | None = ...,
            external_led_mode: LightIndication.ExternalLedMode | str | None = ...,
        ) -> None: ...

    LIGHT_INDICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    light_indication_settings: LightIndication.LightIndicationSettings
    capabilities: _containers.RepeatedScalarFieldContainer[LightIndication.Capability]
    def __init__(
        self,
        light_indication_settings: LightIndication.LightIndicationSettings
        | _Mapping
        | None = ...,
        capabilities: _Iterable[LightIndication.Capability | str] | None = ...,
    ) -> None: ...
