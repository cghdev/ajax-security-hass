from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.protobuf.hub import camera_pb2 as _camera_pb2
from systems.ajax.protobuf.hub import company_binding_pb2 as _company_binding_pb2
from systems.ajax.protobuf.hub import (
    config_migration_state_pb2 as _config_migration_state_pb2,
)
from systems.ajax.protobuf.hub import group_pb2 as _group_pb2
from systems.ajax.protobuf.hub import room_pb2 as _room_pb2
from systems.ajax.protobuf.hub import scenario_pb2 as _scenario_pb2
from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.hub.device import device_pb2 as _device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Hub(_message.Message):
    __slots__ = (
        "cameras",
        "company_bindings",
        "config_migration_state",
        "devices",
        "groups",
        "rooms",
        "scenarios",
        "settings_id",
        "users",
    )
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    CAMERAS_FIELD_NUMBER: _ClassVar[int]
    SCENARIOS_FIELD_NUMBER: _ClassVar[int]
    COMPANY_BINDINGS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_ID_FIELD_NUMBER: _ClassVar[int]
    devices: _containers.RepeatedCompositeFieldContainer[_device_pb2.Device]
    rooms: _containers.RepeatedCompositeFieldContainer[_room_pb2.Room]
    groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.Group]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    cameras: _containers.RepeatedCompositeFieldContainer[_camera_pb2.Camera]
    scenarios: _containers.RepeatedCompositeFieldContainer[_scenario_pb2.Scenario]
    company_bindings: _containers.RepeatedCompositeFieldContainer[
        _company_binding_pb2.CompanyBinding
    ]
    config_migration_state: _config_migration_state_pb2.ConfigMigrationState
    settings_id: str
    def __init__(
        self,
        devices: _Iterable[_device_pb2.Device | _Mapping] | None = ...,
        rooms: _Iterable[_room_pb2.Room | _Mapping] | None = ...,
        groups: _Iterable[_group_pb2.Group | _Mapping] | None = ...,
        users: _Iterable[_user_pb2.User | _Mapping] | None = ...,
        cameras: _Iterable[_camera_pb2.Camera | _Mapping] | None = ...,
        scenarios: _Iterable[_scenario_pb2.Scenario | _Mapping] | None = ...,
        company_bindings: _Iterable[_company_binding_pb2.CompanyBinding | _Mapping]
        | None = ...,
        config_migration_state: _config_migration_state_pb2.ConfigMigrationState
        | _Mapping
        | None = ...,
        settings_id: str | None = ...,
    ) -> None: ...
