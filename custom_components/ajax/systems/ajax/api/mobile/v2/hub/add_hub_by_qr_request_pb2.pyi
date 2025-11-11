from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.hub import hub_box_type_pb2 as _hub_box_type_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.space.device import (
    device_color_pb2 as _device_color_pb2,
)
from systems.ajax.api.mobile.v2.common.space.device import (
    device_label_pb2 as _device_label_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AddHubByQrRequest(_message.Message):
    __slots__ = (
        "box_type",
        "device_color",
        "device_label",
        "hub_name",
        "hub_qr_code",
        "room_id",
        "space_locator",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    HUB_QR_CODE_FIELD_NUMBER: _ClassVar[int]
    HUB_NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COLOR_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LABEL_FIELD_NUMBER: _ClassVar[int]
    BOX_TYPE_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    hub_qr_code: str
    hub_name: str
    room_id: str
    device_color: _device_color_pb2.DeviceColor
    device_label: _device_label_pb2.DeviceLabel
    box_type: _hub_box_type_pb2.HubBoxType
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        hub_qr_code: str | None = ...,
        hub_name: str | None = ...,
        room_id: str | None = ...,
        device_color: _device_color_pb2.DeviceColor | str | None = ...,
        device_label: _device_label_pb2.DeviceLabel | str | None = ...,
        box_type: _hub_box_type_pb2.HubBoxType | str | None = ...,
    ) -> None: ...

class AddHubByQrResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "active_hubs_limit_exceeded",
            "bad_request",
            "groups_limit_exceeded",
            "hub_already_in_space",
            "hub_busy",
            "hub_claim_error",
            "hub_error",
            "hub_firmware_version_not_support_groups",
            "hub_firmware_version_not_support_migration",
            "hub_in_use",
            "hub_in_use_by_space_with_no_admin",
            "hub_not_empty",
            "hub_not_found",
            "hub_offline",
            "hub_qr_code_invalid",
            "hub_wrong_state",
            "member_not_authorized_add_fibra_and_hybrid_hub",
            "member_not_authorized_add_hub",
            "member_not_support_add_fibra_and_hybrid_hub",
            "members_limit_exceeded",
            "passive_hubs_limit_exceeded",
            "permission_denied",
            "room_not_found",
            "rooms_limit_exceeded",
            "space_armed",
            "space_locked",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        HUB_ALREADY_IN_SPACE_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_HUBS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        PASSIVE_HUBS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_IN_USE_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_QR_CODE_INVALID_FIELD_NUMBER: _ClassVar[int]
        HUB_CLAIM_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_EMPTY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_SUPPORT_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_HUB_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NOT_AUTHORIZED_ADD_FIBRA_AND_HYBRID_HUB_FIELD_NUMBER: _ClassVar[int]
        HUB_FIRMWARE_VERSION_NOT_SUPPORT_MIGRATION_FIELD_NUMBER: _ClassVar[int]
        MEMBERS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        ROOMS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        GROUPS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_FIRMWARE_VERSION_NOT_SUPPORT_GROUPS_FIELD_NUMBER: _ClassVar[int]
        HUB_IN_USE_BY_SPACE_WITH_NO_ADMIN_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        hub_already_in_space: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        active_hubs_limit_exceeded: _response_pb2.LimitExceededError
        passive_hubs_limit_exceeded: _response_pb2.LimitExceededError
        hub_in_use: _response_pb2.DefaultError
        hub_not_found: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_qr_code_invalid: _response_pb2.DefaultError
        hub_claim_error: _response_pb2.DefaultError
        hub_not_empty: _response_pb2.DefaultError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        member_not_support_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
        member_not_authorized_add_hub: _response_pb2.DefaultError
        member_not_authorized_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
        hub_firmware_version_not_support_migration: _response_pb2.DefaultError
        members_limit_exceeded: _response_pb2.LimitExceededError
        rooms_limit_exceeded: _response_pb2.LimitExceededError
        groups_limit_exceeded: _response_pb2.LimitExceededError
        hub_firmware_version_not_support_groups: _response_pb2.DefaultError
        hub_in_use_by_space_with_no_admin: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            hub_already_in_space: _response_pb2.DefaultError | _Mapping | None = ...,
            room_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            active_hubs_limit_exceeded: _response_pb2.LimitExceededError
            | _Mapping
            | None = ...,
            passive_hubs_limit_exceeded: _response_pb2.LimitExceededError
            | _Mapping
            | None = ...,
            hub_in_use: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_qr_code_invalid: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_claim_error: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_not_empty: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_error: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            member_not_support_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            member_not_authorized_add_hub: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            member_not_authorized_add_fibra_and_hybrid_hub: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_firmware_version_not_support_migration: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            members_limit_exceeded: _response_pb2.LimitExceededError
            | _Mapping
            | None = ...,
            rooms_limit_exceeded: _response_pb2.LimitExceededError
            | _Mapping
            | None = ...,
            groups_limit_exceeded: _response_pb2.LimitExceededError
            | _Mapping
            | None = ...,
            hub_firmware_version_not_support_groups: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            hub_in_use_by_space_with_no_admin: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: AddHubByQrResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: AddHubByQrResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
