from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class ExtraServiceState(_message.Message):
    __slots__ = ("active", "deactivated", "suspended")
    class Active(_message.Message):
        __slots__ = ("expires_on", "renews_on")
        RENEWS_ON_FIELD_NUMBER: _ClassVar[int]
        EXPIRES_ON_FIELD_NUMBER: _ClassVar[int]
        renews_on: _timestamp_pb2.Timestamp
        expires_on: _timestamp_pb2.Timestamp
        def __init__(
            self,
            renews_on: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            expires_on: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        ) -> None: ...

    class Suspended(_message.Message):
        __slots__ = ("paused_on",)
        PAUSED_ON_FIELD_NUMBER: _ClassVar[int]
        paused_on: _timestamp_pb2.Timestamp
        def __init__(
            self, paused_on: _timestamp_pb2.Timestamp | _Mapping | None = ...
        ) -> None: ...

    class Deactivated(_message.Message):
        __slots__ = ("expired_on",)
        EXPIRED_ON_FIELD_NUMBER: _ClassVar[int]
        expired_on: _timestamp_pb2.Timestamp
        def __init__(
            self, expired_on: _timestamp_pb2.Timestamp | _Mapping | None = ...
        ) -> None: ...

    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    SUSPENDED_FIELD_NUMBER: _ClassVar[int]
    DEACTIVATED_FIELD_NUMBER: _ClassVar[int]
    active: ExtraServiceState.Active
    suspended: ExtraServiceState.Suspended
    deactivated: ExtraServiceState.Deactivated
    def __init__(
        self,
        active: ExtraServiceState.Active | _Mapping | None = ...,
        suspended: ExtraServiceState.Suspended | _Mapping | None = ...,
        deactivated: ExtraServiceState.Deactivated | _Mapping | None = ...,
    ) -> None: ...
