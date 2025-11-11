from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import image_urls_pb2 as _image_urls_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("email", "first_name", "id", "image_urls", "last_name", "phone")
    ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URLS_FIELD_NUMBER: _ClassVar[int]
    id: str
    first_name: str
    last_name: str
    email: _email_address_pb2.EmailAddress
    phone: _phone_number_pb2.PhoneNumber
    image_urls: _image_urls_pb2.ImageUrls
    def __init__(
        self,
        id: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        email: _email_address_pb2.EmailAddress | _Mapping | None = ...,
        phone: _phone_number_pb2.PhoneNumber | _Mapping | None = ...,
        image_urls: _image_urls_pb2.ImageUrls | _Mapping | None = ...,
    ) -> None: ...
