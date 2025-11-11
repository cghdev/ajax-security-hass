from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.hub import (
    surveillance_camera_stream_settings_pb2 as _surveillance_camera_stream_settings_pb2,
)
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetStreamSettingsRequest(_message.Message):
    __slots__ = ("camera_hex_id", "hub_hex_id", "service_id")
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    CAMERA_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    camera_hex_id: str
    service_id: str
    def __init__(
        self,
        hub_hex_id: str | None = ...,
        camera_hex_id: str | None = ...,
        service_id: str | None = ...,
    ) -> None: ...

class GetStreamSettingsResponse(_message.Message):
    __slots__ = ("error", "success")
    class Success(_message.Message):
        __slots__ = ("stream_settings",)
        STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        stream_settings: (
            _surveillance_camera_stream_settings_pb2.SurveillanceCameraStreamSettings
        )
        def __init__(
            self,
            stream_settings: _surveillance_camera_stream_settings_pb2.SurveillanceCameraStreamSettings
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Error(_message.Message):
        __slots__ = ("internal_error",)
        INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        internal_error: _response_pb2.InternalError
        def __init__(
            self, internal_error: _response_pb2.InternalError | _Mapping | None = ...
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: GetStreamSettingsResponse.Success
    error: GetStreamSettingsResponse.Error
    def __init__(
        self,
        success: GetStreamSettingsResponse.Success | _Mapping | None = ...,
        error: GetStreamSettingsResponse.Error | _Mapping | None = ...,
    ) -> None: ...
