from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFacilityOnInstallationRequest(_message.Message):
    __slots__ = ("device_qr_code", "facility_name", "registration_number")
    FACILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    facility_name: str
    registration_number: str
    device_qr_code: str
    def __init__(
        self,
        facility_name: str | None = ...,
        registration_number: str | None = ...,
        device_qr_code: str | None = ...,
    ) -> None: ...
