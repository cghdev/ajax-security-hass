from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.company.templates import (
    company_template_type_pb2 as _company_template_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LightweightCompanyTemplate(_message.Message):
    __slots__ = ("company_id", "description", "id", "name", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    company_id: str
    name: str
    description: str
    type: _company_template_type_pb2.CompanyTemplateType
    def __init__(
        self,
        id: str | None = ...,
        company_id: str | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        type: _company_template_type_pb2.CompanyTemplateType | str | None = ...,
    ) -> None: ...
