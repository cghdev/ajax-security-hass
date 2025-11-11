from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FormatStorageRequest(_message.Message):
    __slots__ = ("space_locator", "storage_device_id", "video_edge_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    storage_device_id: str
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        storage_device_id: str | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class FormatStorageResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "permission_denied",
            "space_not_disarmed",
            "storage_device_not_found",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_DISARMED_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        space_not_disarmed: _response_pb2.DefaultError
        storage_device_not_found: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_disarmed: _response_pb2.DefaultError | _Mapping | None = ...,
            storage_device_not_found: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: FormatStorageResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: FormatStorageResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
