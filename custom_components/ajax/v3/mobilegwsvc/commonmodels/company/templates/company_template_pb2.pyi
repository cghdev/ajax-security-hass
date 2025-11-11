from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.company.templates import (
    company_template_setting_pb2 as _company_template_setting_pb2,
)
from v3.mobilegwsvc.commonmodels.company.templates import (
    company_template_type_pb2 as _company_template_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyTemplate(_message.Message):
    __slots__ = ("company_id", "description", "id", "name", "settings", "type")
    ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    company_id: str
    name: str
    description: str
    settings: _containers.RepeatedCompositeFieldContainer[
        _company_template_setting_pb2.CompanyTemplateSetting
    ]
    type: _company_template_type_pb2.CompanyTemplateType
    def __init__(
        self,
        id: str | None = ...,
        company_id: str | None = ...,
        name: str | None = ...,
        description: str | None = ...,
        settings: _Iterable[
            _company_template_setting_pb2.CompanyTemplateSetting | _Mapping
        ]
        | None = ...,
        type: _company_template_type_pb2.CompanyTemplateType | str | None = ...,
    ) -> None: ...
