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

class AddVideoEdgeRequest(_message.Message):
    __slots__ = (
        "family",
        "make_permanent",
        "model",
        "name",
        "source_video_edge_id",
        "space_locator",
        "video_edge_id",
    )
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    MAKE_PERMANENT_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    family: str
    model: str
    name: str
    source_video_edge_id: str
    space_locator: _space_locator_pb2.SpaceLocator
    make_permanent: bool
    def __init__(
        self,
        video_edge_id: str | None = ...,
        family: str | None = ...,
        model: str | None = ...,
        name: str | None = ...,
        source_video_edge_id: str | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
        make_permanent: bool = ...,
    ) -> None: ...

class AddVideoEdgeResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("channels", "media_device_id")
        MEDIA_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_FIELD_NUMBER: _ClassVar[int]
        media_device_id: str
        channels: _containers.RepeatedCompositeFieldContainer[
            AddVideoEdgeResponse.AvailableChannel
        ]
        def __init__(
            self,
            media_device_id: str | None = ...,
            channels: _Iterable[AddVideoEdgeResponse.AvailableChannel | _Mapping]
            | None = ...,
        ) -> None: ...

    class AvailableChannel(_message.Message):
        __slots__ = ("id_on_media_device",)
        ID_ON_MEDIA_DEVICE_FIELD_NUMBER: _ClassVar[int]
        id_on_media_device: str
        def __init__(self, id_on_media_device: str | None = ...) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_device_family",
            "bad_device_model",
            "bad_request",
            "channels_number_constraint_violation",
            "connection_failed",
            "onvif_authorization_failed",
            "permission_denied",
            "source_video_edge_not_found",
            "space_armed",
            "space_not_found",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SOURCE_VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        BAD_DEVICE_FAMILY_FIELD_NUMBER: _ClassVar[int]
        BAD_DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
        ONVIF_AUTHORIZATION_FAILED_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FAILED_FIELD_NUMBER: _ClassVar[int]
        CHANNELS_NUMBER_CONSTRAINT_VIOLATION_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        source_video_edge_not_found: _response_pb2.DefaultError
        bad_device_family: _response_pb2.DefaultError
        bad_device_model: _response_pb2.DefaultError
        onvif_authorization_failed: _response_pb2.DefaultError
        connection_failed: _response_pb2.DefaultError
        channels_number_constraint_violation: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            source_video_edge_not_found: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            bad_device_family: _response_pb2.DefaultError | _Mapping | None = ...,
            bad_device_model: _response_pb2.DefaultError | _Mapping | None = ...,
            onvif_authorization_failed: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            connection_failed: _response_pb2.DefaultError | _Mapping | None = ...,
            channels_number_constraint_violation: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: AddVideoEdgeResponse.Success
    failure: AddVideoEdgeResponse.Failure
    def __init__(
        self,
        success: AddVideoEdgeResponse.Success | _Mapping | None = ...,
        failure: AddVideoEdgeResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
