from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.company.templates import (
    company_template_type_pb2 as _company_template_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FindAllLightweightCompanyTemplatesRequest(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _company_template_type_pb2.CompanyTemplateType
    def __init__(
        self, type: _company_template_type_pb2.CompanyTemplateType | str | None = ...
    ) -> None: ...
