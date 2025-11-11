from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class FastTamper(_message.Message):
    __slots__ = ("capabilities", "fast_tamper_status")
    class FastTamperStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAST_TAMPER_STATUS_UNSPECIFIED: _ClassVar[FastTamper.FastTamperStatus]
        FAST_TAMPER_STATUS_DISABLED: _ClassVar[FastTamper.FastTamperStatus]
        FAST_TAMPER_STATUS_ENABLED: _ClassVar[FastTamper.FastTamperStatus]

    FAST_TAMPER_STATUS_UNSPECIFIED: FastTamper.FastTamperStatus
    FAST_TAMPER_STATUS_DISABLED: FastTamper.FastTamperStatus
    FAST_TAMPER_STATUS_ENABLED: FastTamper.FastTamperStatus
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[FastTamper.Capability]
        CAPABILITY_FAST_TAMPER: _ClassVar[FastTamper.Capability]

    CAPABILITY_UNSPECIFIED: FastTamper.Capability
    CAPABILITY_FAST_TAMPER: FastTamper.Capability
    FAST_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    fast_tamper_status: FastTamper.FastTamperStatus
    capabilities: _containers.RepeatedScalarFieldContainer[FastTamper.Capability]
    def __init__(
        self,
        fast_tamper_status: FastTamper.FastTamperStatus | str | None = ...,
        capabilities: _Iterable[FastTamper.Capability | str] | None = ...,
    ) -> None: ...
