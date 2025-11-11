from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ResponsiblePerson(_message.Message):
    __slots__ = (
        "email_addresses",
        "facility_id",
        "first_name",
        "id",
        "last_name",
        "phone_numbers",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    id: str
    facility_id: str
    first_name: str
    last_name: str
    phone_numbers: _containers.RepeatedCompositeFieldContainer[
        _phone_number_pb2.PhoneNumber
    ]
    email_addresses: _containers.RepeatedCompositeFieldContainer[
        _email_address_pb2.EmailAddress
    ]
    def __init__(
        self,
        id: str | None = ...,
        facility_id: str | None = ...,
        first_name: str | None = ...,
        last_name: str | None = ...,
        phone_numbers: _Iterable[_phone_number_pb2.PhoneNumber | _Mapping] | None = ...,
        email_addresses: _Iterable[_email_address_pb2.EmailAddress | _Mapping]
        | None = ...,
    ) -> None: ...
