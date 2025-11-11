from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class LightDesignPart(_message.Message):
    __slots__ = ("led_brightness_level", "led_brightness_limits")
    class LightDesignPartSettings(_message.Message):
        __slots__ = ("led_brightness_level",)
        LED_BRIGHTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
        led_brightness_level: int
        def __init__(self, led_brightness_level: int | None = ...) -> None: ...

    class LedBrightnessLimits(_message.Message):
        __slots__ = ("max", "min")
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        min: int
        max: int
        def __init__(self, min: int | None = ..., max: int | None = ...) -> None: ...

    LED_BRIGHTNESS_LEVEL_FIELD_NUMBER: _ClassVar[int]
    LED_BRIGHTNESS_LIMITS_FIELD_NUMBER: _ClassVar[int]
    led_brightness_level: int
    led_brightness_limits: LightDesignPart.LedBrightnessLimits
    def __init__(
        self,
        led_brightness_level: int | None = ...,
        led_brightness_limits: LightDesignPart.LedBrightnessLimits
        | _Mapping
        | None = ...,
    ) -> None: ...
