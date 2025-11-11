from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceAddress(_message.Message):
    __slots__ = ("city", "country", "location", "postcode", "region")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    POSTCODE_FIELD_NUMBER: _ClassVar[int]
    location: str
    city: str
    region: str
    country: str
    postcode: str
    def __init__(
        self,
        location: str | None = ...,
        city: str | None = ...,
        region: str | None = ...,
        country: str | None = ...,
        postcode: str | None = ...,
    ) -> None: ...
