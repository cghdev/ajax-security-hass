from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_fibra_part_pb2 as _common_fibra_part_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceCommandStartScanFibraDevicesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "command_not_performed",
            "hub_busy",
            "hub_error",
            "hub_offline",
            "hub_wrong_state",
            "permission_denied",
            "power_disabled_on_lines",
            "unknown_command",
            "unregistered_rings",
        )
        class UnregisteredRings(_message.Message):
            __slots__ = ("lines",)
            LINES_FIELD_NUMBER: _ClassVar[int]
            lines: _containers.RepeatedCompositeFieldContainer[
                _common_fibra_part_pb2.FibraLine
            ]
            def __init__(
                self,
                lines: _Iterable[_common_fibra_part_pb2.FibraLine | _Mapping]
                | None = ...,
            ) -> None: ...

        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_COMMAND_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        POWER_DISABLED_ON_LINES_FIELD_NUMBER: _ClassVar[int]
        UNREGISTERED_RINGS_FIELD_NUMBER: _ClassVar[int]
        command_not_performed: _response_pb2.Error
        permission_denied: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        hub_offline: _response_pb2.Error
        unknown_command: _response_pb2.Error
        hub_error: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        power_disabled_on_lines: _response_pb2.Error
        unregistered_rings: (
            DeviceCommandStartScanFibraDevicesResponse.Failure.UnregisteredRings
        )
        def __init__(
            self,
            command_not_performed: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            unknown_command: _response_pb2.Error | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            power_disabled_on_lines: _response_pb2.Error | _Mapping | None = ...,
            unregistered_rings: DeviceCommandStartScanFibraDevicesResponse.Failure.UnregisteredRings
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: DeviceCommandStartScanFibraDevicesResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: DeviceCommandStartScanFibraDevicesResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
