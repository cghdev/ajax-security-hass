from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.context import company_pb2 as _company_pb2
from systems.ajax.api.mobile.v2.common.context import personal_pb2 as _personal_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ApproveRequestedFullPermissionsRequest(_message.Message):
    __slots__ = ("company_context", "personal_context", "request_id", "space_locator")
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    PERSONAL_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    COMPANY_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    request_id: str
    personal_context: _personal_pb2.PersonalContext
    company_context: _company_pb2.CompanyContext
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        request_id: str | None = ...,
        personal_context: _personal_pb2.PersonalContext | _Mapping | None = ...,
        company_context: _company_pb2.CompanyContext | _Mapping | None = ...,
    ) -> None: ...

class ApproveRequestedFullPermissionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "request_expired",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        REQUEST_EXPIRED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        request_expired: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            request_expired: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: ApproveRequestedFullPermissionsResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: ApproveRequestedFullPermissionsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
