from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import wrappers_pb2 as _wrappers_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class PhoneNumber(_message.Message):
    __slots__ = ("country_code", "description", "number")
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    number: str
    country_code: _wrappers_pb2.StringValue
    description: _wrappers_pb2.StringValue
    def __init__(
        self,
        number: str | None = ...,
        country_code: _wrappers_pb2.StringValue | _Mapping | None = ...,
        description: _wrappers_pb2.StringValue | _Mapping | None = ...,
    ) -> None: ...
