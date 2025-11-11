from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.image import image_id_pb2 as _image_id_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.space.security.group import (
    followed_group_ids_pb2 as _followed_group_ids_pb2,
)
from systems.ajax.api.mobile.v2.common.space.security.group import (
    group_auto_arm_pb2 as _group_auto_arm_pb2,
)
from systems.ajax.api.mobile.v2.common.space.security.group import (
    group_auto_disarm_pb2 as _group_auto_disarm_pb2,
)
from systems.ajax.api.mobile.v2.common.space.security.group import (
    two_stage_arming_mode_pb2 as _two_stage_arming_mode_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateGroupRequest(_message.Message):
    __slots__ = (
        "auto_arm_delay",
        "bulk_arm_involved",
        "bulk_disarm_involved",
        "followed_group_ids",
        "following_group_auto_arm",
        "following_group_auto_disarm",
        "group_id",
        "group_name",
        "image",
        "image_id",
        "space_locator",
        "two_stage_arming_mode",
    )
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_NAME_FIELD_NUMBER: _ClassVar[int]
    BULK_ARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    BULK_DISARM_INVOLVED_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TWO_STAGE_ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_GROUP_AUTO_ARM_FIELD_NUMBER: _ClassVar[int]
    FOLLOWING_GROUP_AUTO_DISARM_FIELD_NUMBER: _ClassVar[int]
    AUTO_ARM_DELAY_FIELD_NUMBER: _ClassVar[int]
    FOLLOWED_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    group_id: str
    group_name: str
    bulk_arm_involved: bool
    bulk_disarm_involved: bool
    image_id: str
    two_stage_arming_mode: _two_stage_arming_mode_pb2.TwoStageArmingMode
    image: _image_id_pb2.ImageIdValue
    following_group_auto_arm: _group_auto_arm_pb2.FollowingGroupAutoArm
    following_group_auto_disarm: _group_auto_disarm_pb2.FollowingGroupAutoDisarm
    auto_arm_delay: _duration_pb2.Duration
    followed_group_ids: _followed_group_ids_pb2.FollowedGroupIds
    def __init__(
        self,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        group_id: str | None = ...,
        group_name: str | None = ...,
        bulk_arm_involved: bool = ...,
        bulk_disarm_involved: bool = ...,
        image_id: str | None = ...,
        two_stage_arming_mode: _two_stage_arming_mode_pb2.TwoStageArmingMode
        | str
        | None = ...,
        image: _image_id_pb2.ImageIdValue | _Mapping | None = ...,
        following_group_auto_arm: _group_auto_arm_pb2.FollowingGroupAutoArm
        | str
        | None = ...,
        following_group_auto_disarm: _group_auto_disarm_pb2.FollowingGroupAutoDisarm
        | str
        | None = ...,
        auto_arm_delay: _duration_pb2.Duration | _Mapping | None = ...,
        followed_group_ids: _followed_group_ids_pb2.FollowedGroupIds
        | _Mapping
        | None = ...,
    ) -> None: ...

class UpdateGroupResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "followed_groups_conflict",
            "group_not_found",
            "hub_busy",
            "hub_error",
            "hub_offline",
            "hub_wrong_state",
            "permission_denied",
            "space_armed",
            "space_locked",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        HUB_BUSY_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_WRONG_STATE_FIELD_NUMBER: _ClassVar[int]
        SPACE_LOCKED_FIELD_NUMBER: _ClassVar[int]
        FOLLOWED_GROUPS_CONFLICT_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        hub_offline: _response_pb2.DefaultError
        hub_busy: _response_pb2.HubBusyError
        hub_error: _response_pb2.DefaultError
        hub_wrong_state: _response_pb2.DefaultError
        space_locked: _response_pb2.SpaceLockedError
        followed_groups_conflict: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            group_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_offline: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_busy: _response_pb2.HubBusyError | _Mapping | None = ...,
            hub_error: _response_pb2.DefaultError | _Mapping | None = ...,
            hub_wrong_state: _response_pb2.DefaultError | _Mapping | None = ...,
            space_locked: _response_pb2.SpaceLockedError | _Mapping | None = ...,
            followed_groups_conflict: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: UpdateGroupResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: UpdateGroupResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
