from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.protobuf.hub import (
    config_migration_state_pb2 as _config_migration_state_pb2,
)
from systems.ajax.protobuf.hub import lightweight_hub_pb2 as _lightweight_hub_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class HubForMigration(_message.Message):
    __slots__ = ("config_migration_state", "hub")
    HUB_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    hub: _lightweight_hub_pb2.LightweightHub
    config_migration_state: _config_migration_state_pb2.ConfigMigrationState
    def __init__(
        self,
        hub: _lightweight_hub_pb2.LightweightHub | _Mapping | None = ...,
        config_migration_state: _config_migration_state_pb2.ConfigMigrationState
        | _Mapping
        | None = ...,
    ) -> None: ...
