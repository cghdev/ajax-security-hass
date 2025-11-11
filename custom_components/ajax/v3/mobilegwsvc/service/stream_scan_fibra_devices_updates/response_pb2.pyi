from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_fibra_part_pb2 as _common_fibra_part_pb2,
)
from v3.mobilegwsvc.commonmodels.hub.device import (
    hub_device_view_source_pb2 as _hub_device_view_source_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamScanFibraDevicesUpdatesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("device_added", "device_triggered", "state_update")
        class State(_message.Message):
            __slots__ = ("blocked", "finished", "in_progress", "not_started")
            class NotStarted(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...

            class InProgress(_message.Message):
                __slots__ = ("found_devices_count",)
                FOUND_DEVICES_COUNT_FIELD_NUMBER: _ClassVar[int]
                found_devices_count: int
                def __init__(self, found_devices_count: int | None = ...) -> None: ...

            class Finished(_message.Message):
                __slots__ = ("no_fibra_devices_found", "scanned_devices")
                class ScannedDevices(_message.Message):
                    __slots__ = ("scanned_devices",)
                    SCANNED_DEVICES_FIELD_NUMBER: _ClassVar[int]
                    scanned_devices: _containers.RepeatedCompositeFieldContainer[
                        StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevice
                    ]
                    def __init__(
                        self,
                        scanned_devices: _Iterable[
                            StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevice
                            | _Mapping
                        ]
                        | None = ...,
                    ) -> None: ...

                class ScannedDevice(_message.Message):
                    __slots__ = ("hub_device_view_source", "line", "marketing_id")
                    MARKETING_ID_FIELD_NUMBER: _ClassVar[int]
                    LINE_FIELD_NUMBER: _ClassVar[int]
                    HUB_DEVICE_VIEW_SOURCE_FIELD_NUMBER: _ClassVar[int]
                    marketing_id: str
                    line: _common_fibra_part_pb2.FibraLine
                    hub_device_view_source: (
                        _hub_device_view_source_pb2.HubDeviceViewSource
                    )
                    def __init__(
                        self,
                        marketing_id: str | None = ...,
                        line: _common_fibra_part_pb2.FibraLine | _Mapping | None = ...,
                        hub_device_view_source: _hub_device_view_source_pb2.HubDeviceViewSource
                        | _Mapping
                        | None = ...,
                    ) -> None: ...

                class NoFibraDevicesFound(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...

                SCANNED_DEVICES_FIELD_NUMBER: _ClassVar[int]
                NO_FIBRA_DEVICES_FOUND_FIELD_NUMBER: _ClassVar[int]
                scanned_devices: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevices
                no_fibra_devices_found: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.NoFibraDevicesFound
                def __init__(
                    self,
                    scanned_devices: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.ScannedDevices
                    | _Mapping
                    | None = ...,
                    no_fibra_devices_found: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished.NoFibraDevicesFound
                    | _Mapping
                    | None = ...,
                ) -> None: ...

            class Blocked(_message.Message):
                __slots__ = ("malfunction", "malfunction_on_rings")
                class Malfunction(_message.Message):
                    __slots__ = ()
                    def __init__(self) -> None: ...

                class MalfunctionOnRings(_message.Message):
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

                MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
                MALFUNCTION_ON_RINGS_FIELD_NUMBER: _ClassVar[int]
                malfunction: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.Malfunction
                malfunction_on_rings: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.MalfunctionOnRings
                def __init__(
                    self,
                    malfunction: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.Malfunction
                    | _Mapping
                    | None = ...,
                    malfunction_on_rings: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked.MalfunctionOnRings
                    | _Mapping
                    | None = ...,
                ) -> None: ...

            NOT_STARTED_FIELD_NUMBER: _ClassVar[int]
            IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
            FINISHED_FIELD_NUMBER: _ClassVar[int]
            BLOCKED_FIELD_NUMBER: _ClassVar[int]
            not_started: StreamScanFibraDevicesUpdatesResponse.Success.State.NotStarted
            in_progress: StreamScanFibraDevicesUpdatesResponse.Success.State.InProgress
            finished: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished
            blocked: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked
            def __init__(
                self,
                not_started: StreamScanFibraDevicesUpdatesResponse.Success.State.NotStarted
                | _Mapping
                | None = ...,
                in_progress: StreamScanFibraDevicesUpdatesResponse.Success.State.InProgress
                | _Mapping
                | None = ...,
                finished: StreamScanFibraDevicesUpdatesResponse.Success.State.Finished
                | _Mapping
                | None = ...,
                blocked: StreamScanFibraDevicesUpdatesResponse.Success.State.Blocked
                | _Mapping
                | None = ...,
            ) -> None: ...

        class DeviceTriggered(_message.Message):
            __slots__ = ("device_id", "timestamp")
            DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
            TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
            device_id: str
            timestamp: _timestamp_pb2.Timestamp
            def __init__(
                self,
                device_id: str | None = ...,
                timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            ) -> None: ...

        class DeviceAdded(_message.Message):
            __slots__ = ("device_id",)
            DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
            device_id: str
            def __init__(self, device_id: str | None = ...) -> None: ...

        STATE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ADDED_FIELD_NUMBER: _ClassVar[int]
        state_update: StreamScanFibraDevicesUpdatesResponse.Success.State
        device_triggered: StreamScanFibraDevicesUpdatesResponse.Success.DeviceTriggered
        device_added: StreamScanFibraDevicesUpdatesResponse.Success.DeviceAdded
        def __init__(
            self,
            state_update: StreamScanFibraDevicesUpdatesResponse.Success.State
            | _Mapping
            | None = ...,
            device_triggered: StreamScanFibraDevicesUpdatesResponse.Success.DeviceTriggered
            | _Mapping
            | None = ...,
            device_added: StreamScanFibraDevicesUpdatesResponse.Success.DeviceAdded
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "command_not_performed",
            "hub_busy",
            "hub_error",
            "hub_offline",
            "hub_wrong_state",
            "message",
            "permission_denied",
            "unknown_command",
        )
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_COMMAND_FIELD_NUMBER: _ClassVar[int]
        COMMAND_NOT_PERFORMED_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        message: str
        bad_request: _response_pb2.Error
        unknown_command: _response_pb2.Error
        command_not_performed: _response_pb2.Error
        hub_wrong_state: _response_pb2.HubWrongStateError
        permission_denied: _response_pb2.Error
        hub_offline: _response_pb2.Error
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.Error
        def __init__(
            self,
            message: str | None = ...,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            unknown_command: _response_pb2.Error | _Mapping | None = ...,
            command_not_performed: _response_pb2.Error | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.HubWrongStateError | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamScanFibraDevicesUpdatesResponse.Success
    failure: StreamScanFibraDevicesUpdatesResponse.Failure
    def __init__(
        self,
        success: StreamScanFibraDevicesUpdatesResponse.Success | _Mapping | None = ...,
        failure: StreamScanFibraDevicesUpdatesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
