from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from v1.facility import facility_pb2 as _facility_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateFacilityOnInstallationRequest(_message.Message):
    __slots__ = ("device_qr_code", "facility_name", "registration_number")
    FACILITY_NAME_FIELD_NUMBER: _ClassVar[int]
    REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    facility_name: str
    registration_number: str
    device_qr_code: str
    def __init__(
        self,
        facility_name: str | None = ...,
        registration_number: str | None = ...,
        device_qr_code: str | None = ...,
    ) -> None: ...

class CreateFacilityOnInstallationResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("add_device_failed", "facility")
        FACILITY_FIELD_NUMBER: _ClassVar[int]
        ADD_DEVICE_FAILED_FIELD_NUMBER: _ClassVar[int]
        facility: _facility_pb2.Facility
        add_device_failed: _response_pb2.AddDeviceError
        def __init__(
            self,
            facility: _facility_pb2.Facility | _Mapping | None = ...,
            add_device_failed: _response_pb2.AddDeviceError | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "empty_spaces_limit_exceeded",
            "registration_number_not_unique",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        REGISTRATION_NUMBER_NOT_UNIQUE_FIELD_NUMBER: _ClassVar[int]
        EMPTY_SPACES_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        registration_number_not_unique: _response_pb2.DefaultError
        empty_spaces_limit_exceeded: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            registration_number_not_unique: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            empty_spaces_limit_exceeded: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateFacilityOnInstallationResponse.Success
    failure: CreateFacilityOnInstallationResponse.Failure
    def __init__(
        self,
        success: CreateFacilityOnInstallationResponse.Success | _Mapping | None = ...,
        failure: CreateFacilityOnInstallationResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
