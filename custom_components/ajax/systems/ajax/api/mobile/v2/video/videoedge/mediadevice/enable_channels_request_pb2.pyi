from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class EnableMediaDeviceChannelsRequest(_message.Message):
    __slots__ = ("media_device_id", "new_channels", "space_locator", "video_edge_id")
    class NewChannel(_message.Message):
        __slots__ = ("channel_id_on_media_device", "group_id", "name", "room_id")
        CHANNEL_ID_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_ID_FIELD_NUMBER: _ClassVar[int]
        channel_id_on_media_device: str
        name: str
        room_id: str
        group_id: str
        def __init__(
            self,
            channel_id_on_media_device: str | None = ...,
            name: str | None = ...,
            room_id: str | None = ...,
            group_id: str | None = ...,
        ) -> None: ...

    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    media_device_id: str
    new_channels: _containers.RepeatedCompositeFieldContainer[
        EnableMediaDeviceChannelsRequest.NewChannel
    ]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        media_device_id: str | None = ...,
        new_channels: _Iterable[EnableMediaDeviceChannelsRequest.NewChannel | _Mapping]
        | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class EnableMediaDeviceChannelsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("channel_ids",)
        CHANNEL_IDS_FIELD_NUMBER: _ClassVar[int]
        channel_ids: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, channel_ids: _Iterable[str] | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "channels_number_constraint_violation",
            "device_not_found",
            "group_not_found",
            "permission_denied",
            "room_not_found",
            "space_armed",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        ROOM_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        GROUP_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_NUMBER_CONSTRAINT_VIOLATION_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        device_not_found: _response_pb2.DefaultError
        channel_not_found: _response_pb2.DefaultError
        room_not_found: _response_pb2.DefaultError
        group_not_found: _response_pb2.DefaultError
        channels_number_constraint_violation: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            device_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            channel_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            room_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            group_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            channels_number_constraint_violation: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: EnableMediaDeviceChannelsResponse.Success
    failure: EnableMediaDeviceChannelsResponse.Failure
    def __init__(
        self,
        success: EnableMediaDeviceChannelsResponse.Success | _Mapping | None = ...,
        failure: EnableMediaDeviceChannelsResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
