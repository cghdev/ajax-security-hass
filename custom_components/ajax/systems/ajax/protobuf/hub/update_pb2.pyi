from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub import access_card_rc_pb2 as _access_card_rc_pb2
from systems.ajax.protobuf.hub import (
    access_card_reader_state_pb2 as _access_card_reader_state_pb2,
)
from systems.ajax.protobuf.hub import access_key_pb2 as _access_key_pb2
from systems.ajax.protobuf.hub import camera_pb2 as _camera_pb2
from systems.ajax.protobuf.hub import company_binding_pb2 as _company_binding_pb2
from systems.ajax.protobuf.hub import (
    config_migration_state_pb2 as _config_migration_state_pb2,
)
from systems.ajax.protobuf.hub import group_pb2 as _group_pb2
from systems.ajax.protobuf.hub import (
    hub_access_response_pb2 as _hub_access_response_pb2,
)
from systems.ajax.protobuf.hub import room_pb2 as _room_pb2
from systems.ajax.protobuf.hub import scenario_pb2 as _scenario_pb2
from systems.ajax.protobuf.hub import user_pb2 as _user_pb2
from systems.ajax.protobuf.hub.device import device_pb2 as _device_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Update(_message.Message):
    __slots__ = (
        "access_card_rc",
        "access_card_reader_state",
        "access_key_update",
        "camera",
        "company_binding",
        "config_migration_state",
        "device",
        "group",
        "hub_access_response",
        "mask",
        "room",
        "scenario",
        "settings_id",
        "type",
        "user",
    )
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UPDATE: _ClassVar[Update.Type]
        ADD: _ClassVar[Update.Type]
        DELETE: _ClassVar[Update.Type]
        SETTINGS_ID: _ClassVar[Update.Type]
        LOGS_DROPPED: _ClassVar[Update.Type]
        PROFI_HUB_ACCESS_RESPONSE_RESULT: _ClassVar[Update.Type]
        ACCESS_CARD_STATE_CHANGED: _ClassVar[Update.Type]
        ACCESS_CARD_RC: _ClassVar[Update.Type]
        ACCESS_KEY_REGISTERED: _ClassVar[Update.Type]
        ACCESS_KEY_TIMEOUT: _ClassVar[Update.Type]
        DEV_REG_SEARCH_STARTED: _ClassVar[Update.Type]
        UNREG_DEVICE_FOUND: _ClassVar[Update.Type]

    UPDATE: Update.Type
    ADD: Update.Type
    DELETE: Update.Type
    SETTINGS_ID: Update.Type
    LOGS_DROPPED: Update.Type
    PROFI_HUB_ACCESS_RESPONSE_RESULT: Update.Type
    ACCESS_CARD_STATE_CHANGED: Update.Type
    ACCESS_CARD_RC: Update.Type
    ACCESS_KEY_REGISTERED: Update.Type
    ACCESS_KEY_TIMEOUT: Update.Type
    DEV_REG_SEARCH_STARTED: Update.Type
    UNREG_DEVICE_FOUND: Update.Type
    ROOM_FIELD_NUMBER: _ClassVar[int]
    GROUP_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    CAMERA_FIELD_NUMBER: _ClassVar[int]
    SCENARIO_FIELD_NUMBER: _ClassVar[int]
    COMPANY_BINDING_FIELD_NUMBER: _ClassVar[int]
    CONFIG_MIGRATION_STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    HUB_ACCESS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_READER_STATE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_RC_FIELD_NUMBER: _ClassVar[int]
    ACCESS_KEY_UPDATE_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_ID_FIELD_NUMBER: _ClassVar[int]
    room: _room_pb2.Room
    group: _group_pb2.Group
    user: _user_pb2.User
    camera: _camera_pb2.Camera
    scenario: _scenario_pb2.Scenario
    company_binding: _company_binding_pb2.CompanyBinding
    config_migration_state: _config_migration_state_pb2.ConfigMigrationState
    device: _device_pb2.Device
    hub_access_response: _hub_access_response_pb2.HubAccessResponse
    access_card_reader_state: _access_card_reader_state_pb2.AccessCardReaderState
    access_card_rc: _access_card_rc_pb2.AccessCardRc
    access_key_update: _access_key_pb2.AccessKeyUpdate
    mask: _field_mask_pb2.FieldMask
    type: Update.Type
    settings_id: str
    def __init__(
        self,
        room: _room_pb2.Room | _Mapping | None = ...,
        group: _group_pb2.Group | _Mapping | None = ...,
        user: _user_pb2.User | _Mapping | None = ...,
        camera: _camera_pb2.Camera | _Mapping | None = ...,
        scenario: _scenario_pb2.Scenario | _Mapping | None = ...,
        company_binding: _company_binding_pb2.CompanyBinding | _Mapping | None = ...,
        config_migration_state: _config_migration_state_pb2.ConfigMigrationState
        | _Mapping
        | None = ...,
        device: _device_pb2.Device | _Mapping | None = ...,
        hub_access_response: _hub_access_response_pb2.HubAccessResponse
        | _Mapping
        | None = ...,
        access_card_reader_state: _access_card_reader_state_pb2.AccessCardReaderState
        | _Mapping
        | None = ...,
        access_card_rc: _access_card_rc_pb2.AccessCardRc | _Mapping | None = ...,
        access_key_update: _access_key_pb2.AccessKeyUpdate | _Mapping | None = ...,
        mask: _field_mask_pb2.FieldMask | _Mapping | None = ...,
        type: Update.Type | str | None = ...,
        settings_id: str | None = ...,
    ) -> None: ...
