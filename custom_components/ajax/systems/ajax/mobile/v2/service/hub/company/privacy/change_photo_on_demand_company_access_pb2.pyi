from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.hub import (
    photo_on_demand_company_rights_pb2 as _photo_on_demand_company_rights_pb2,
)
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ChangePhotoOnDemandCompanyAccessRequest(_message.Message):
    __slots__ = ("company_id", "company_rights", "hub_id")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    COMPANY_RIGHTS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    company_id: str
    company_rights: _photo_on_demand_company_rights_pb2.PhotoOnDemandCompanyRights
    def __init__(
        self,
        hub_id: str | None = ...,
        company_id: str | None = ...,
        company_rights: _photo_on_demand_company_rights_pb2.PhotoOnDemandCompanyRights
        | _Mapping
        | None = ...,
    ) -> None: ...

class ChangePhotoOnDemandCompanyAccessResponse(_message.Message):
    __slots__ = ("error", "success")
    class Error(_message.Message):
        __slots__ = (
            "company_on_hub_not_found_error",
            "deadline_exceeded_error",
            "internal_error",
            "permission_denied_error",
        )
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        COMPANY_ON_HUB_NOT_FOUND_ERROR_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_ERROR_FIELD_NUMBER: _ClassVar[int]
        DEADLINE_EXCEEDED_ERROR_FIELD_NUMBER: _ClassVar[int]
        internal_error: _response_pb2.InternalError
        company_on_hub_not_found_error: _response_pb2.CompanyOnHubNotFoundError
        permission_denied_error: _response_pb2.PermissionDeniedError
        deadline_exceeded_error: _response_pb2.DeadlineExceededError
        def __init__(
            self,
            internal_error: _response_pb2.InternalError | _Mapping | None = ...,
            company_on_hub_not_found_error: _response_pb2.CompanyOnHubNotFoundError
            | _Mapping
            | None = ...,
            permission_denied_error: _response_pb2.PermissionDeniedError
            | _Mapping
            | None = ...,
            deadline_exceeded_error: _response_pb2.DeadlineExceededError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    error: ChangePhotoOnDemandCompanyAccessResponse.Error
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        error: ChangePhotoOnDemandCompanyAccessResponse.Error | _Mapping | None = ...,
    ) -> None: ...
