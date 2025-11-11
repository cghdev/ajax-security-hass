from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space.company import (
    space_monitoring_company_pb2 as _space_monitoring_company_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetMonitoringCompanyRequest(_message.Message):
    __slots__ = ("company_hex_id", "space_id")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    space_id: str
    def __init__(
        self, company_hex_id: str | None = ..., space_id: str | None = ...
    ) -> None: ...

class GetMonitoringCompanyResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("company",)
        COMPANY_FIELD_NUMBER: _ClassVar[int]
        company: _space_monitoring_company_pb2.SpaceMonitoringCompany
        def __init__(
            self,
            company: _space_monitoring_company_pb2.SpaceMonitoringCompany
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request",)
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        def __init__(
            self, bad_request: _response_pb2.DefaultError | _Mapping | None = ...
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetMonitoringCompanyResponse.Success
    failure: GetMonitoringCompanyResponse.Failure
    def __init__(
        self,
        success: GetMonitoringCompanyResponse.Success | _Mapping | None = ...,
        failure: GetMonitoringCompanyResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
