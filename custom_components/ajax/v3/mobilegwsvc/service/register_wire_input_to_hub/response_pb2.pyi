from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterWireInputToHubResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("cancel_registration", "device_added", "search_started")
        class DeviceAdded(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class SearchStarted(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        class CancelRegistration(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        DEVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        SEARCH_STARTED_FIELD_NUMBER: _ClassVar[int]
        CANCEL_REGISTRATION_FIELD_NUMBER: _ClassVar[int]
        device_added: RegisterWireInputToHubResponse.Success.DeviceAdded
        search_started: RegisterWireInputToHubResponse.Success.SearchStarted
        cancel_registration: RegisterWireInputToHubResponse.Success.CancelRegistration
        def __init__(
            self,
            device_added: RegisterWireInputToHubResponse.Success.DeviceAdded
            | _Mapping
            | None = ...,
            search_started: RegisterWireInputToHubResponse.Success.SearchStarted
            | _Mapping
            | None = ...,
            cancel_registration: RegisterWireInputToHubResponse.Success.CancelRegistration
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "device_registration_restricted",
            "device_search_timeout",
            "hub_busy",
            "hub_firmware_not_supported",
            "hub_not_found",
            "hub_offline",
            "hub_request_already_performed",
            "hub_type_not_supported",
            "hub_wrong_state",
            "limit_exceeded_of_one_byte_devices",
            "limit_exceeded_on_fibra_line",
            "objects_limit_exceeded",
            "permission_denied",
            "unknown_device",
        )
        class UnknownDeviceError(_message.Message):
            __slots__ = ("available_fw_update",)
            class AvailableFwUpdate(_message.Message):
                __slots__ = ("firmware_version", "firmware_version_raw")
                FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
                FIRMWARE_VERSION_RAW_FIELD_NUMBER: _ClassVar[int]
                firmware_version: str
                firmware_version_raw: int
                def __init__(
                    self,
                    firmware_version: str | None = ...,
                    firmware_version_raw: int | None = ...,
                ) -> None: ...

            AVAILABLE_FW_UPDATE_FIELD_NUMBER: _ClassVar[int]
            available_fw_update: RegisterWireInputToHubResponse.Failure.UnknownDeviceError.AvailableFwUpdate
            def __init__(
                self,
                available_fw_update: RegisterWireInputToHubResponse.Failure.UnknownDeviceError.AvailableFwUpdate
                | _Mapping
                | None = ...,
            ) -> None: ...

        class HubFirmwareNotSupportedError(_message.Message):
            __slots__ = ("available_fw_update",)
            class AvailableFwUpdate(_message.Message):
                __slots__ = ("firmware_version", "firmware_version_raw")
                FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
                FIRMWARE_VERSION_RAW_FIELD_NUMBER: _ClassVar[int]
                firmware_version: str
                firmware_version_raw: int
                def __init__(
                    self,
                    firmware_version: str | None = ...,
                    firmware_version_raw: int | None = ...,
                ) -> None: ...

            AVAILABLE_FW_UPDATE_FIELD_NUMBER: _ClassVar[int]
            available_fw_update: RegisterWireInputToHubResponse.Failure.HubFirmwareNotSupportedError.AvailableFwUpdate
            def __init__(
                self,
                available_fw_update: RegisterWireInputToHubResponse.Failure.HubFirmwareNotSupportedError.AvailableFwUpdate
                | _Mapping
                | None = ...,
            ) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_SEARCH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_DEVICE_FIELD_NUMBER: _ClassVar[int]
        HUB_TYPE_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        HUB_FIRMWARE_NOT_SUPPORTED_FIELD_NUMBER: _ClassVar[int]
        DEVICE_REGISTRATION_RESTRICTED_FIELD_NUMBER: _ClassVar[int]
        LIMIT_EXCEEDED_ON_FIBRA_LINE_FIELD_NUMBER: _ClassVar[int]
        LIMIT_EXCEEDED_OF_ONE_BYTE_DEVICES_FIELD_NUMBER: _ClassVar[int]
        OBJECTS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_REQUEST_ALREADY_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        permission_denied: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_offline: _response_pb2.Error
        device_search_timeout: _response_pb2.Error
        unknown_device: RegisterWireInputToHubResponse.Failure.UnknownDeviceError
        hub_type_not_supported: _response_pb2.Error
        hub_firmware_not_supported: (
            RegisterWireInputToHubResponse.Failure.HubFirmwareNotSupportedError
        )
        device_registration_restricted: _response_pb2.Error
        limit_exceeded_on_fibra_line: _response_pb2.Error
        limit_exceeded_of_one_byte_devices: _response_pb2.Error
        objects_limit_exceeded: _response_pb2.Error
        hub_request_already_performed: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            hub_not_found: _response_pb2.Error | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            device_search_timeout: _response_pb2.Error | _Mapping | None = ...,
            unknown_device: RegisterWireInputToHubResponse.Failure.UnknownDeviceError
            | _Mapping
            | None = ...,
            hub_type_not_supported: _response_pb2.Error | _Mapping | None = ...,
            hub_firmware_not_supported: RegisterWireInputToHubResponse.Failure.HubFirmwareNotSupportedError
            | _Mapping
            | None = ...,
            device_registration_restricted: _response_pb2.Error | _Mapping | None = ...,
            limit_exceeded_on_fibra_line: _response_pb2.Error | _Mapping | None = ...,
            limit_exceeded_of_one_byte_devices: _response_pb2.Error
            | _Mapping
            | None = ...,
            objects_limit_exceeded: _response_pb2.Error | _Mapping | None = ...,
            hub_request_already_performed: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: RegisterWireInputToHubResponse.Success
    failure: RegisterWireInputToHubResponse.Failure
    def __init__(
        self,
        success: RegisterWireInputToHubResponse.Success | _Mapping | None = ...,
        failure: RegisterWireInputToHubResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
