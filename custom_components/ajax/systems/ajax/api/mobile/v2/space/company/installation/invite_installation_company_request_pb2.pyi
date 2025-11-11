from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class InviteInstallationCompanyRequest(_message.Message):
    __slots__ = ("company_hex_id", "space_id")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    space_id: str
    def __init__(
        self, company_hex_id: str | None = ..., space_id: str | None = ...
    ) -> None: ...

class InviteInstallationCompanyResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_locked",
            "permission_denied",
            "space_already_on_installation",
            "space_armed",
            "space_locked",
            "space_not_found",
            "users_limit_exceed",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_LOCKED_FIELD_NUMBER: _ClassVar[int]
        USERS_LIMIT_EXCEED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ALREADY_ON_INSTALLATION_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        hub_locked: _response_pb2.DefaultError
        users_limit_exceed: _response_pb2.DefaultError
        space_already_on_installation: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        space_armed: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_locked: _response_pb2.DefaultError | _Mapping | None = ...,
            users_limit_exceed: _response_pb2.DefaultError | _Mapping | None = ...,
            space_already_on_installation: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: InviteInstallationCompanyResponse.Success
    failure: InviteInstallationCompanyResponse.Failure
    def __init__(
        self,
        success: InviteInstallationCompanyResponse.Success | _Mapping | None = ...,
        failure: InviteInstallationCompanyResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
