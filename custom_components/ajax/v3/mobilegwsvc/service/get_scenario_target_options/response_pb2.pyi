from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetScenarioTargetOptionsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("scenario_target_options",)
        SCENARIO_TARGET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        scenario_target_options: _containers.RepeatedCompositeFieldContainer[
            GetScenarioTargetOptionsResponse.ScenarioTargetOption
        ]
        def __init__(
            self,
            scenario_target_options: _Iterable[
                GetScenarioTargetOptionsResponse.ScenarioTargetOption | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permissions_denied",
            "space_armed",
            "space_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSIONS_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permissions_denied: _response_pb2.Error
        space_armed: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            permissions_denied: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    class ScenarioTargetOption(_message.Message):
        __slots__ = (
            "phod_target_option",
            "schedule_access_target_option",
            "smart_lock_target_option",
            "switching_state_target_option",
            "video_edge_target_option",
        )
        SCHEDULE_ACCESS_TARGET_OPTION_FIELD_NUMBER: _ClassVar[int]
        PHOD_TARGET_OPTION_FIELD_NUMBER: _ClassVar[int]
        SWITCHING_STATE_TARGET_OPTION_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_TARGET_OPTION_FIELD_NUMBER: _ClassVar[int]
        SMART_LOCK_TARGET_OPTION_FIELD_NUMBER: _ClassVar[int]
        schedule_access_target_option: (
            GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption
        )
        phod_target_option: GetScenarioTargetOptionsResponse.GenericObjectTargetOption
        switching_state_target_option: (
            GetScenarioTargetOptionsResponse.GenericObjectTargetOption
        )
        video_edge_target_option: GetScenarioTargetOptionsResponse.VideoEdgeTargetOption
        smart_lock_target_option: (
            GetScenarioTargetOptionsResponse.GenericObjectTargetOption
        )
        def __init__(
            self,
            schedule_access_target_option: GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption
            | _Mapping
            | None = ...,
            phod_target_option: GetScenarioTargetOptionsResponse.GenericObjectTargetOption
            | _Mapping
            | None = ...,
            switching_state_target_option: GetScenarioTargetOptionsResponse.GenericObjectTargetOption
            | _Mapping
            | None = ...,
            video_edge_target_option: GetScenarioTargetOptionsResponse.VideoEdgeTargetOption
            | _Mapping
            | None = ...,
            smart_lock_target_option: GetScenarioTargetOptionsResponse.GenericObjectTargetOption
            | _Mapping
            | None = ...,
        ) -> None: ...

    class GenericObjectTargetOption(_message.Message):
        __slots__ = ("object_id",)
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        object_id: str
        def __init__(self, object_id: str | None = ...) -> None: ...

    class ScheduleAccessTargetOption(_message.Message):
        __slots__ = ("has_full_access_for_any_group", "object_id", "type")
        class ScheduleAccessTargetType(
            int, metaclass=_enum_type_wrapper.EnumTypeWrapper
        ):
            __slots__ = ()
            SCHEDULE_ACCESS_TARGET_TYPE_UNSPECIFIED: _ClassVar[
                GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
            ]
            SCHEDULE_ACCESS_TARGET_TYPE_ACCESS_CARD: _ClassVar[
                GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
            ]
            SCHEDULE_ACCESS_TARGET_TYPE_ACCESS_CODE: _ClassVar[
                GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
            ]

        SCHEDULE_ACCESS_TARGET_TYPE_UNSPECIFIED: GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
        SCHEDULE_ACCESS_TARGET_TYPE_ACCESS_CARD: GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
        SCHEDULE_ACCESS_TARGET_TYPE_ACCESS_CODE: GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
        OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        HAS_FULL_ACCESS_FOR_ANY_GROUP_FIELD_NUMBER: _ClassVar[int]
        object_id: str
        type: GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
        has_full_access_for_any_group: bool
        def __init__(
            self,
            object_id: str | None = ...,
            type: GetScenarioTargetOptionsResponse.ScheduleAccessTargetOption.ScheduleAccessTargetType
            | str
            | None = ...,
            has_full_access_for_any_group: bool = ...,
        ) -> None: ...

    class VideoEdgeTargetOption(_message.Message):
        __slots__ = ("channels", "video_edge_id")
        class Channel(_message.Message):
            __slots__ = ("channel_id",)
            CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
            channel_id: str
            def __init__(self, channel_id: str | None = ...) -> None: ...

        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channels: _containers.RepeatedCompositeFieldContainer[
            GetScenarioTargetOptionsResponse.VideoEdgeTargetOption.Channel
        ]
        def __init__(
            self,
            video_edge_id: str | None = ...,
            channels: _Iterable[
                GetScenarioTargetOptionsResponse.VideoEdgeTargetOption.Channel
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetScenarioTargetOptionsResponse.Success
    failure: GetScenarioTargetOptionsResponse.Failure
    def __init__(
        self,
        success: GetScenarioTargetOptionsResponse.Success | _Mapping | None = ...,
        failure: GetScenarioTargetOptionsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
