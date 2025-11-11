from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from v1.facility import facility_pb2 as _facility_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class JoinSpaceByCompanyRequest(_message.Message):
    __slots__ = ("hub_qr",)
    HUB_QR_FIELD_NUMBER: _ClassVar[int]
    hub_qr: str
    def __init__(self, hub_qr: str | None = ...) -> None: ...

class JoinSpaceByCompanyResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("facility",)
        FACILITY_FIELD_NUMBER: _ClassVar[int]
        facility: _facility_pb2.Facility
        def __init__(
            self, facility: _facility_pb2.Facility | _Mapping | None = ...
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("hub_error",)
        class HubError(_message.Message):
            __slots__ = (
                "bad_request",
                "hub_claim_error",
                "hub_claim_forbidden_by_company_error",
                "hub_not_found",
                "hub_offline",
                "hub_qr_code_invalid",
                "space_armed",
                "space_not_found",
            )
            BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
            SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
            HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
            HUB_QR_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
            HUB_CLAIM_ERROR_FIELD_NUMBER: _ClassVar[int]
            SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
            HUB_CLAIM_FORBIDDEN_BY_COMPANY_ERROR_FIELD_NUMBER: _ClassVar[int]
            HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
            bad_request: _response_pb2.DefaultError
            space_not_found: _response_pb2.DefaultError
            hub_not_found: _response_pb2.DefaultError
            hub_qr_code_invalid: _response_pb2.DefaultError
            hub_claim_error: _response_pb2.DefaultError
            space_armed: _response_pb2.DefaultError
            hub_claim_forbidden_by_company_error: _response_pb2.DefaultError
            hub_offline: _response_pb2.DefaultError
            def __init__(
                self,
                bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
                space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
                hub_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
                hub_qr_code_invalid: _response_pb2.DefaultError | _Mapping | None = ...,
                hub_claim_error: _response_pb2.DefaultError | _Mapping | None = ...,
                space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
                hub_claim_forbidden_by_company_error: _response_pb2.DefaultError
                | _Mapping
                | None = ...,
                hub_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            ) -> None: ...

        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        hub_error: JoinSpaceByCompanyResponse.Failure.HubError
        def __init__(
            self,
            hub_error: JoinSpaceByCompanyResponse.Failure.HubError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: JoinSpaceByCompanyResponse.Success
    failure: JoinSpaceByCompanyResponse.Failure
    def __init__(
        self,
        success: JoinSpaceByCompanyResponse.Success | _Mapping | None = ...,
        failure: JoinSpaceByCompanyResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
