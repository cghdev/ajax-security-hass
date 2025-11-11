from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import (
    feature_target_info_pb2 as _feature_target_info_pb2,
)
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ApplyForMonitoringRequest(_message.Message):
    __slots__ = ("account_number", "company_hex_id", "space_id")
    COMPANY_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    company_hex_id: str
    space_id: str
    account_number: str
    def __init__(
        self,
        company_hex_id: str | None = ...,
        space_id: str | None = ...,
        account_number: str | None = ...,
    ) -> None: ...

class ApplyForMonitoringResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("feature_target_info",)
        FEATURE_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
        feature_target_info: _feature_target_info_pb2.FeatureTargetInfo
        def __init__(
            self,
            feature_target_info: _feature_target_info_pb2.FeatureTargetInfo
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "account_number_exists",
            "account_number_required",
            "bad_request",
            "cannot_perform_action_for_initiator",
            "hub_locked",
            "permission_denied",
            "space_armed",
            "space_locked",
            "space_not_found",
            "space_on_monitoring_already_exists",
            "users_limit_exceed",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ON_MONITORING_ALREADY_EXISTS_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_LOCKED_FIELD_NUMBER: _ClassVar[int]
        USERS_LIMIT_EXCEED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NUMBER_REQUIRED_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_NUMBER_EXISTS_FIELD_NUMBER: _ClassVar[int]
        CANNOT_PERFORM_ACTION_FOR_INITIATOR_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_on_monitoring_already_exists: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        hub_locked: _response_pb2.DefaultError
        users_limit_exceed: _response_pb2.DefaultError
        account_number_required: _response_pb2.DefaultError
        account_number_exists: _response_pb2.DefaultError
        cannot_perform_action_for_initiator: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_on_monitoring_already_exists: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_locked: _response_pb2.DefaultError | _Mapping | None = ...,
            users_limit_exceed: _response_pb2.DefaultError | _Mapping | None = ...,
            account_number_required: _response_pb2.DefaultError | _Mapping | None = ...,
            account_number_exists: _response_pb2.DefaultError | _Mapping | None = ...,
            cannot_perform_action_for_initiator: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ApplyForMonitoringResponse.Success
    failure: ApplyForMonitoringResponse.Failure
    def __init__(
        self,
        success: ApplyForMonitoringResponse.Success | _Mapping | None = ...,
        failure: ApplyForMonitoringResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
