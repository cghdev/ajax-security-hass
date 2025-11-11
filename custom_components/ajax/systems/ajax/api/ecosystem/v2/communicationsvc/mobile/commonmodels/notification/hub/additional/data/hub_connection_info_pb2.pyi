from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class HubConnectionInfo(_message.Message):
    __slots__ = (
        "hub_connection_status",
        "original_timestamp",
        "parent_notification_id",
    )
    class HubConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HUB_CONNECTION_STATUS_UNSPECIFIED: _ClassVar[
            HubConnectionInfo.HubConnectionStatus
        ]
        ONLINE: _ClassVar[HubConnectionInfo.HubConnectionStatus]
        OFFLINE: _ClassVar[HubConnectionInfo.HubConnectionStatus]

    HUB_CONNECTION_STATUS_UNSPECIFIED: HubConnectionInfo.HubConnectionStatus
    ONLINE: HubConnectionInfo.HubConnectionStatus
    OFFLINE: HubConnectionInfo.HubConnectionStatus
    ORIGINAL_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HUB_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    PARENT_NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    original_timestamp: _timestamp_pb2.Timestamp
    hub_connection_status: HubConnectionInfo.HubConnectionStatus
    parent_notification_id: str
    def __init__(
        self,
        original_timestamp: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        hub_connection_status: HubConnectionInfo.HubConnectionStatus | str | None = ...,
        parent_notification_id: str | None = ...,
    ) -> None: ...
