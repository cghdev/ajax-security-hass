from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Leds(_message.Message):
    __slots__ = ("logo",)
    class LogoLed(_message.Message):
        __slots__ = ("brightness",)
        BRIGHTNESS_FIELD_NUMBER: _ClassVar[int]
        brightness: int
        def __init__(self, brightness: int | None = ...) -> None: ...

    LOGO_FIELD_NUMBER: _ClassVar[int]
    logo: Leds.LogoLed
    def __init__(self, logo: Leds.LogoLed | _Mapping | None = ...) -> None: ...
