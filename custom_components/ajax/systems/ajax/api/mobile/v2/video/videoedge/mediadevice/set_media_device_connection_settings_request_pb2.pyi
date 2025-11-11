from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import (
    media_device_capabilities_pb2 as _media_device_capabilities_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import (
    media_device_pb2 as _media_device_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mediadevice import (
    media_device_settings_pb2 as _media_device_settings_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetMediaDeviceConnectionSettingsRequest(_message.Message):
    __slots__ = (
        "connection_settings",
        "media_device_id",
        "space_locator",
        "video_edge_id",
    )
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    media_device_id: str
    connection_settings: _media_device_settings_pb2.ConnectionSettings
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        media_device_id: str | None = ...,
        connection_settings: _media_device_settings_pb2.ConnectionSettings
        | _Mapping
        | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class SetMediaDeviceConnectionSettingsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("capabilities",)
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        capabilities: _media_device_capabilities_pb2.MediaDeviceCapabilities
        def __init__(
            self,
            capabilities: _media_device_capabilities_pb2.MediaDeviceCapabilities
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "connection_failed",
            "device_not_found",
            "permission_denied",
            "space_armed",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        class ConnectionFailedError(_message.Message):
            __slots__ = ("media_device_state",)
            MEDIA_DEVICE_STATE_FIELD_NUMBER: _ClassVar[int]
            media_device_state: _media_device_pb2.MediaDeviceState
            def __init__(
                self,
                media_device_state: _media_device_pb2.MediaDeviceState
                | str
                | None = ...,
            ) -> None: ...

        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FAILED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        device_not_found: _response_pb2.DefaultError
        connection_failed: (
            SetMediaDeviceConnectionSettingsResponse.Failure.ConnectionFailedError
        )
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            device_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            connection_failed: SetMediaDeviceConnectionSettingsResponse.Failure.ConnectionFailedError
            | _Mapping
            | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetMediaDeviceConnectionSettingsResponse.Success
    failure: SetMediaDeviceConnectionSettingsResponse.Failure
    def __init__(
        self,
        success: SetMediaDeviceConnectionSettingsResponse.Success
        | _Mapping
        | None = ...,
        failure: SetMediaDeviceConnectionSettingsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
