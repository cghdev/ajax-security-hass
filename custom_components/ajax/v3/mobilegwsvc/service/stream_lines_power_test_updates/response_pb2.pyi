from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels import (
    object_type_pb2 as _object_type_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_fibra_part_pb2 as _common_fibra_part_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamLinesPowerTestResponse(_message.Message):
    __slots__ = ("failure", "success")
    class PowerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POWER_STATE_UNSPECIFIED: _ClassVar[StreamLinesPowerTestResponse.PowerState]
        POWER_STATE_OK: _ClassVar[StreamLinesPowerTestResponse.PowerState]
        POWER_STATE_LOW: _ClassVar[StreamLinesPowerTestResponse.PowerState]
        POWER_STATE_LOST: _ClassVar[StreamLinesPowerTestResponse.PowerState]

    POWER_STATE_UNSPECIFIED: StreamLinesPowerTestResponse.PowerState
    POWER_STATE_OK: StreamLinesPowerTestResponse.PowerState
    POWER_STATE_LOW: StreamLinesPowerTestResponse.PowerState
    POWER_STATE_LOST: StreamLinesPowerTestResponse.PowerState
    class Success(_message.Message):
        __slots__ = ("line_power_test",)
        LINE_POWER_TEST_FIELD_NUMBER: _ClassVar[int]
        line_power_test: StreamLinesPowerTestResponse.LinesPowerTest
        def __init__(
            self,
            line_power_test: StreamLinesPowerTestResponse.LinesPowerTest
            | _Mapping
            | None = ...,
        ) -> None: ...

    class LinesPowerTest(_message.Message):
        __slots__ = ("active", "blocked", "finished", "unknown")
        UNKNOWN_FIELD_NUMBER: _ClassVar[int]
        BLOCKED_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        FINISHED_FIELD_NUMBER: _ClassVar[int]
        unknown: StreamLinesPowerTestResponse.Unknown
        blocked: StreamLinesPowerTestResponse.Blocked
        active: StreamLinesPowerTestResponse.Active
        finished: StreamLinesPowerTestResponse.Finished
        def __init__(
            self,
            unknown: StreamLinesPowerTestResponse.Unknown | _Mapping | None = ...,
            blocked: StreamLinesPowerTestResponse.Blocked | _Mapping | None = ...,
            active: StreamLinesPowerTestResponse.Active | _Mapping | None = ...,
            finished: StreamLinesPowerTestResponse.Finished | _Mapping | None = ...,
        ) -> None: ...

    class Unknown(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Blocked(_message.Message):
        __slots__ = ("malfunction", "malfunction_on_rings", "no_fibra_devices")
        class NoFibraDevices(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

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

        NO_FIBRA_DEVICES_FIELD_NUMBER: _ClassVar[int]
        MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
        MALFUNCTION_ON_RINGS_FIELD_NUMBER: _ClassVar[int]
        no_fibra_devices: StreamLinesPowerTestResponse.Blocked.NoFibraDevices
        malfunction: StreamLinesPowerTestResponse.Blocked.Malfunction
        malfunction_on_rings: StreamLinesPowerTestResponse.Blocked.MalfunctionOnRings
        def __init__(
            self,
            no_fibra_devices: StreamLinesPowerTestResponse.Blocked.NoFibraDevices
            | _Mapping
            | None = ...,
            malfunction: StreamLinesPowerTestResponse.Blocked.Malfunction
            | _Mapping
            | None = ...,
            malfunction_on_rings: StreamLinesPowerTestResponse.Blocked.MalfunctionOnRings
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Active(_message.Message):
        __slots__ = ("duration", "is_soft_short_circuit", "power_test_active_state")
        class PowerTestActiveState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            POWER_TEST_ACTIVE_STATE_UNSPECIFIED: _ClassVar[
                StreamLinesPowerTestResponse.Active.PowerTestActiveState
            ]
            POWER_TEST_ACTIVE_STATE_READY_TO_START: _ClassVar[
                StreamLinesPowerTestResponse.Active.PowerTestActiveState
            ]
            POWER_TEST_ACTIVE_STATE_STARTING: _ClassVar[
                StreamLinesPowerTestResponse.Active.PowerTestActiveState
            ]
            POWER_TEST_ACTIVE_STATE_IN_PROGRESS: _ClassVar[
                StreamLinesPowerTestResponse.Active.PowerTestActiveState
            ]
            POWER_TEST_ACTIVE_STATE_FINISHING: _ClassVar[
                StreamLinesPowerTestResponse.Active.PowerTestActiveState
            ]

        POWER_TEST_ACTIVE_STATE_UNSPECIFIED: (
            StreamLinesPowerTestResponse.Active.PowerTestActiveState
        )
        POWER_TEST_ACTIVE_STATE_READY_TO_START: (
            StreamLinesPowerTestResponse.Active.PowerTestActiveState
        )
        POWER_TEST_ACTIVE_STATE_STARTING: (
            StreamLinesPowerTestResponse.Active.PowerTestActiveState
        )
        POWER_TEST_ACTIVE_STATE_IN_PROGRESS: (
            StreamLinesPowerTestResponse.Active.PowerTestActiveState
        )
        POWER_TEST_ACTIVE_STATE_FINISHING: (
            StreamLinesPowerTestResponse.Active.PowerTestActiveState
        )
        DURATION_FIELD_NUMBER: _ClassVar[int]
        IS_SOFT_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
        POWER_TEST_ACTIVE_STATE_FIELD_NUMBER: _ClassVar[int]
        duration: _duration_pb2.Duration
        is_soft_short_circuit: bool
        power_test_active_state: (
            StreamLinesPowerTestResponse.Active.PowerTestActiveState
        )
        def __init__(
            self,
            duration: _duration_pb2.Duration | _Mapping | None = ...,
            is_soft_short_circuit: bool = ...,
            power_test_active_state: StreamLinesPowerTestResponse.Active.PowerTestActiveState
            | str
            | None = ...,
        ) -> None: ...

    class Finished(_message.Message):
        __slots__ = (
            "finish_timestamp",
            "interrupted",
            "power_test_finished_state",
            "success",
        )
        class PowerTestFinishedState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            POWER_TEST_FINISHED_STATE_UNSPECIFIED: _ClassVar[
                StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
            ]
            POWER_TEST_FINISHED_STATE_RESETTING: _ClassVar[
                StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
            ]
            POWER_TEST_FINISHED_STATE_READY_TO_RESET: _ClassVar[
                StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
            ]

        POWER_TEST_FINISHED_STATE_UNSPECIFIED: (
            StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
        )
        POWER_TEST_FINISHED_STATE_RESETTING: (
            StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
        )
        POWER_TEST_FINISHED_STATE_READY_TO_RESET: (
            StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
        )
        class Success(_message.Message):
            __slots__ = ("line_power_states", "power_state")
            POWER_STATE_FIELD_NUMBER: _ClassVar[int]
            LINE_POWER_STATES_FIELD_NUMBER: _ClassVar[int]
            power_state: StreamLinesPowerTestResponse.PowerState
            line_power_states: _containers.RepeatedCompositeFieldContainer[
                StreamLinesPowerTestResponse.LinePowerState
            ]
            def __init__(
                self,
                power_state: StreamLinesPowerTestResponse.PowerState | str | None = ...,
                line_power_states: _Iterable[
                    StreamLinesPowerTestResponse.LinePowerState | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class Interrupted(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        FINISH_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        POWER_TEST_FINISHED_STATE_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        INTERRUPTED_FIELD_NUMBER: _ClassVar[int]
        finish_timestamp: _timestamp_pb2.Timestamp
        power_test_finished_state: (
            StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
        )
        success: StreamLinesPowerTestResponse.Finished.Success
        interrupted: StreamLinesPowerTestResponse.Finished.Interrupted
        def __init__(
            self,
            finish_timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            power_test_finished_state: StreamLinesPowerTestResponse.Finished.PowerTestFinishedState
            | str
            | None = ...,
            success: StreamLinesPowerTestResponse.Finished.Success
            | _Mapping
            | None = ...,
            interrupted: StreamLinesPowerTestResponse.Finished.Interrupted
            | _Mapping
            | None = ...,
        ) -> None: ...

    class LinePowerState(_message.Message):
        __slots__ = ("device_power_states", "line", "power_state")
        LINE_FIELD_NUMBER: _ClassVar[int]
        POWER_STATE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_POWER_STATES_FIELD_NUMBER: _ClassVar[int]
        line: _common_fibra_part_pb2.FibraLine
        power_state: StreamLinesPowerTestResponse.PowerState
        device_power_states: _containers.RepeatedCompositeFieldContainer[
            StreamLinesPowerTestResponse.DevicePowerState
        ]
        def __init__(
            self,
            line: _common_fibra_part_pb2.FibraLine | _Mapping | None = ...,
            power_state: StreamLinesPowerTestResponse.PowerState | str | None = ...,
            device_power_states: _Iterable[
                StreamLinesPowerTestResponse.DevicePowerState | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class DevicePowerState(_message.Message):
        __slots__ = (
            "device_id",
            "device_name",
            "device_type",
            "line_extender",
            "power_state",
        )
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LINE_EXTENDER_FIELD_NUMBER: _ClassVar[int]
        POWER_STATE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        device_name: str
        device_type: _object_type_pb2.ObjectType
        line_extender: _common_fibra_part_pb2.LineExtender
        power_state: StreamLinesPowerTestResponse.PowerState
        device_id: str
        def __init__(
            self,
            device_name: str | None = ...,
            device_type: _object_type_pb2.ObjectType | _Mapping | None = ...,
            line_extender: _common_fibra_part_pb2.LineExtender | _Mapping | None = ...,
            power_state: StreamLinesPowerTestResponse.PowerState | str | None = ...,
            device_id: str | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamLinesPowerTestResponse.Success
    failure: StreamLinesPowerTestResponse.Failure
    def __init__(
        self,
        success: StreamLinesPowerTestResponse.Success | _Mapping | None = ...,
        failure: StreamLinesPowerTestResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
