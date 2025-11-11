from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.company.templates import (
    company_template_pb2 as _company_template_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetCompanyTemplateByIdResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("template",)
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        template: _company_template_pb2.CompanyTemplate
        def __init__(
            self,
            template: _company_template_pb2.CompanyTemplate | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("illegal_argument", "not_found", "permission_denied")
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        illegal_argument: _response_pb2.Error
        not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetCompanyTemplateByIdResponse.Success
    failure: GetCompanyTemplateByIdResponse.Failure
    def __init__(
        self,
        success: GetCompanyTemplateByIdResponse.Success | _Mapping | None = ...,
        failure: GetCompanyTemplateByIdResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
