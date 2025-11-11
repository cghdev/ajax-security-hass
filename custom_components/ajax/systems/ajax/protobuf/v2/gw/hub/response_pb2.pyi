from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.protobuf.gw import error_pb2 as _error_pb2
from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.v2.hub import hub_for_migration_pb2 as _hub_for_migration_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionResponse(_message.Message):
    __slots__ = ("permissions", "timestamp_to_drop")
    TIMESTAMP_TO_DROP_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    timestamp_to_drop: int
    permissions: _containers.RepeatedScalarFieldContainer[_user_pb2.User.Permission]
    def __init__(
        self,
        timestamp_to_drop: int | None = ...,
        permissions: _Iterable[_user_pb2.User.Permission | str] | None = ...,
    ) -> None: ...

class GetHubForMigrationResponse(_message.Message):
    __slots__ = ("error", "hub_for_migration")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HUB_FOR_MIGRATION_FIELD_NUMBER: _ClassVar[int]
    error: _error_pb2.GwError
    hub_for_migration: _hub_for_migration_pb2.HubForMigration
    def __init__(
        self,
        error: _error_pb2.GwError | _Mapping | None = ...,
        hub_for_migration: _hub_for_migration_pb2.HubForMigration
        | _Mapping
        | None = ...,
    ) -> None: ...
