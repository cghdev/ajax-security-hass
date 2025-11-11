from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyNotificationSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPANY_SOURCE_TYPE_UNSPECIFIED: _ClassVar[CompanyNotificationSourceType]
    INSTALLATION_COMPANY: _ClassVar[CompanyNotificationSourceType]
    MONITORING_COMPANY: _ClassVar[CompanyNotificationSourceType]
    SPACE_MEMBER: _ClassVar[CompanyNotificationSourceType]

COMPANY_SOURCE_TYPE_UNSPECIFIED: CompanyNotificationSourceType
INSTALLATION_COMPANY: CompanyNotificationSourceType
MONITORING_COMPANY: CompanyNotificationSourceType
SPACE_MEMBER: CompanyNotificationSourceType
