from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.network import (
    network_interface_pb2 as _network_interface_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SetNetworkDesiredConfigurationRequest(_message.Message):
    __slots__ = (
        "desired_configuration",
        "network_interface_id",
        "space_locator",
        "video_edge_id",
    )
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    DESIRED_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    network_interface_id: str
    desired_configuration: _network_interface_pb2.NetworkConfiguration
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        network_interface_id: str | None = ...,
        desired_configuration: _network_interface_pb2.NetworkConfiguration
        | _Mapping
        | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class SetNetworkDesiredConfigurationResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("network_configuration_timeout", "requestId")
        REQUESTID_FIELD_NUMBER: _ClassVar[int]
        NETWORK_CONFIGURATION_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        requestId: str
        network_configuration_timeout: _duration_pb2.Duration
        def __init__(
            self,
            requestId: str | None = ...,
            network_configuration_timeout: _duration_pb2.Duration
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "network_interface_configuration_in_progress",
            "network_interface_not_found",
            "permission_denied",
            "space_armed",
            "video_edge_is_offline",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        NETWORK_INTERFACE_CONFIGURATION_IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        space_armed: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        network_interface_not_found: _response_pb2.DefaultError
        network_interface_configuration_in_progress: _response_pb2.DefaultError
        video_edge_is_offline: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            space_armed: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            network_interface_not_found: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            network_interface_configuration_in_progress: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
            video_edge_is_offline: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: SetNetworkDesiredConfigurationResponse.Success
    failure: SetNetworkDesiredConfigurationResponse.Failure
    def __init__(
        self,
        success: SetNetworkDesiredConfigurationResponse.Success | _Mapping | None = ...,
        failure: SetNetworkDesiredConfigurationResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
