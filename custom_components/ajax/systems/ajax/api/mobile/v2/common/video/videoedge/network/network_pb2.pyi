from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class Network(_message.Message):
    __slots__ = (
        "configuration_status",
        "connection_failure_alarm_delay",
        "ethernet",
        "server_ping_interval",
        "wifi",
    )
    SERVER_PING_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FAILURE_ALARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    ETHERNET_FIELD_NUMBER: _ClassVar[int]
    WIFI_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    server_ping_interval: _duration_pb2.Duration
    connection_failure_alarm_delay: _duration_pb2.Duration
    ethernet: NetworkTechnology
    wifi: NetworkTechnology
    configuration_status: NetworkConfigurationStatus
    def __init__(
        self,
        server_ping_interval: _duration_pb2.Duration | _Mapping | None = ...,
        connection_failure_alarm_delay: _duration_pb2.Duration | _Mapping | None = ...,
        ethernet: NetworkTechnology | _Mapping | None = ...,
        wifi: NetworkTechnology | _Mapping | None = ...,
        configuration_status: NetworkConfigurationStatus | _Mapping | None = ...,
    ) -> None: ...

class NetworkTechnology(_message.Message):
    __slots__ = ("supported",)
    SUPPORTED_FIELD_NUMBER: _ClassVar[int]
    supported: bool
    def __init__(self, supported: bool = ...) -> None: ...

class NetworkConfigurationStatus(_message.Message):
    __slots__ = ("request_id", "state")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[NetworkConfigurationStatus.State]
        OK: _ClassVar[NetworkConfigurationStatus.State]
        FAILED: _ClassVar[NetworkConfigurationStatus.State]

    NONE: NetworkConfigurationStatus.State
    OK: NetworkConfigurationStatus.State
    FAILED: NetworkConfigurationStatus.State
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    request_id: str
    state: NetworkConfigurationStatus.State
    def __init__(
        self,
        request_id: str | None = ...,
        state: NetworkConfigurationStatus.State | str | None = ...,
    ) -> None: ...
