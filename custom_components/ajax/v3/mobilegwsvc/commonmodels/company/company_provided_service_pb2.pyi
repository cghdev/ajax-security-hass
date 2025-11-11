from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class CompanyProvidedService(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    COMPANY_PROVIDED_SERVICE_UNSPECIFIED: _ClassVar[CompanyProvidedService]
    COMPANY_PROVIDED_SERVICE_INSTALLATION: _ClassVar[CompanyProvidedService]
    COMPANY_PROVIDED_SERVICE_MONITORING: _ClassVar[CompanyProvidedService]

COMPANY_PROVIDED_SERVICE_UNSPECIFIED: CompanyProvidedService
COMPANY_PROVIDED_SERVICE_INSTALLATION: CompanyProvidedService
COMPANY_PROVIDED_SERVICE_MONITORING: CompanyProvidedService
