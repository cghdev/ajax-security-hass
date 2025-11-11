from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.hub.firmware import (
    firmware_update_pb2 as _firmware_update_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamHubWifiModuleUpdateResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("available_firmware_update", "not_available", "up_to_date")
        UP_TO_DATE_FIELD_NUMBER: _ClassVar[int]
        NOT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        AVAILABLE_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        up_to_date: StreamHubWifiModuleUpdateResponse.UpToDate
        not_available: StreamHubWifiModuleUpdateResponse.NotAvailable
        available_firmware_update: (
            StreamHubWifiModuleUpdateResponse.AvailableFirmwareUpdate
        )
        def __init__(
            self,
            up_to_date: StreamHubWifiModuleUpdateResponse.UpToDate
            | _Mapping
            | None = ...,
            not_available: StreamHubWifiModuleUpdateResponse.NotAvailable
            | _Mapping
            | None = ...,
            available_firmware_update: StreamHubWifiModuleUpdateResponse.AvailableFirmwareUpdate
            | _Mapping
            | None = ...,
        ) -> None: ...

    class UpToDate(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class NotAvailable(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class AvailableFirmwareUpdate(_message.Message):
        __slots__ = ("firmware_update",)
        FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        firmware_update: _firmware_update_pb2.FirmwareUpdate
        def __init__(
            self,
            firmware_update: _firmware_update_pb2.FirmwareUpdate
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("hub_not_found", "illegal_argument", "message")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ILLEGAL_ARGUMENT_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        message: str
        illegal_argument: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        def __init__(
            self,
            message: str | None = ...,
            illegal_argument: _response_pb2.Error | _Mapping | None = ...,
            hub_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamHubWifiModuleUpdateResponse.Success
    failure: StreamHubWifiModuleUpdateResponse.Failure
    def __init__(
        self,
        success: StreamHubWifiModuleUpdateResponse.Success | _Mapping | None = ...,
        failure: StreamHubWifiModuleUpdateResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
