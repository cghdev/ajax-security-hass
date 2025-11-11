from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalTamperPart(_message.Message):
    __slots__ = ("external_tamper_status",)
    class ExternalTamperStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_TAMPER_STATUS_UNSPECIFIED: _ClassVar[
            ExternalTamperPart.ExternalTamperStatus
        ]
        EXTERNAL_TAMPER_STATUS_NOT_CONNECTED: _ClassVar[
            ExternalTamperPart.ExternalTamperStatus
        ]
        EXTERNAL_TAMPER_STATUS_CONNECTED: _ClassVar[
            ExternalTamperPart.ExternalTamperStatus
        ]

    EXTERNAL_TAMPER_STATUS_UNSPECIFIED: ExternalTamperPart.ExternalTamperStatus
    EXTERNAL_TAMPER_STATUS_NOT_CONNECTED: ExternalTamperPart.ExternalTamperStatus
    EXTERNAL_TAMPER_STATUS_CONNECTED: ExternalTamperPart.ExternalTamperStatus
    EXTERNAL_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    external_tamper_status: ExternalTamperPart.ExternalTamperStatus
    def __init__(
        self,
        external_tamper_status: ExternalTamperPart.ExternalTamperStatus
        | str
        | None = ...,
    ) -> None: ...
