from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class TemporaryVideoAccessDeniedForCompanyData(_message.Message):
    __slots__ = ("company_email", "company_id", "company_name", "request_id")
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    company_id: str
    company_name: str
    company_email: str
    request_id: str
    def __init__(
        self,
        company_id: str | None = ...,
        company_name: str | None = ...,
        company_email: str | None = ...,
        request_id: str | None = ...,
    ) -> None: ...
