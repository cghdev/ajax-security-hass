from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common import (
    connection_status_pb2 as _connection_status_pb2,
)
from systems.ajax.api.mobile.v2.common.hub import (
    battery_save_mode_pb2 as _battery_save_mode_pb2,
)
from systems.ajax.api.mobile.v2.common.space import (
    space_profile_pb2 as _space_profile_pb2,
)
from systems.ajax.api.mobile.v2.common.space.security import (
    displayed_space_security_state_pb2 as _displayed_space_security_state_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LiteSpace(_message.Message):
    __slots__ = (
        "bsm_status",
        "hub_connection_status",
        "hub_id",
        "id",
        "malfunctions_count",
        "new_notifications_count",
        "pagination_token",
        "profile",
        "security_state",
        "sorting_key",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_STATE_FIELD_NUMBER: _ClassVar[int]
    NEW_NOTIFICATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SORTING_KEY_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HUB_CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    BSM_STATUS_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    profile: _space_profile_pb2.SpaceProfile
    security_state: _displayed_space_security_state_pb2.DisplayedSpaceSecurityState
    new_notifications_count: int
    malfunctions_count: int
    sorting_key: str
    pagination_token: str
    hub_connection_status: _connection_status_pb2.ConnectionStatus
    bsm_status: _battery_save_mode_pb2.BatterySaveModeStatus
    hub_id: str
    def __init__(
        self,
        id: str | None = ...,
        profile: _space_profile_pb2.SpaceProfile | _Mapping | None = ...,
        security_state: _displayed_space_security_state_pb2.DisplayedSpaceSecurityState
        | str
        | None = ...,
        new_notifications_count: int | None = ...,
        malfunctions_count: int | None = ...,
        sorting_key: str | None = ...,
        pagination_token: str | None = ...,
        hub_connection_status: _connection_status_pb2.ConnectionStatus
        | str
        | None = ...,
        bsm_status: _battery_save_mode_pb2.BatterySaveModeStatus | str | None = ...,
        hub_id: str | None = ...,
    ) -> None: ...
