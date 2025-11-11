from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = (
        "address_line1",
        "address_line2",
        "city",
        "country",
        "state",
        "zip_code",
    )
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE1_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_LINE2_FIELD_NUMBER: _ClassVar[int]
    country: str
    state: str
    city: str
    zip_code: str
    address_line1: str
    address_line2: str
    def __init__(
        self,
        country: str | None = ...,
        state: str | None = ...,
        city: str | None = ...,
        zip_code: str | None = ...,
        address_line1: str | None = ...,
        address_line2: str | None = ...,
    ) -> None: ...
