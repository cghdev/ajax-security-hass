from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyTemplateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPANY_TEMPLATE_TYPE_UNSPECIFIED: _ClassVar[CompanyTemplateType]
    COMPANY_TEMPLATE_TYPE_TELEPHONY_SETTINGS: _ClassVar[CompanyTemplateType]
    COMPANY_TEMPLATE_TYPE_VIDEO_EDGE: _ClassVar[CompanyTemplateType]

COMPANY_TEMPLATE_TYPE_UNSPECIFIED: CompanyTemplateType
COMPANY_TEMPLATE_TYPE_TELEPHONY_SETTINGS: CompanyTemplateType
COMPANY_TEMPLATE_TYPE_VIDEO_EDGE: CompanyTemplateType
