from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveBackupChannelResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_device_not_found",
            "hub_error",
            "hub_is_busy",
            "hub_not_found",
            "hub_offline",
            "permission_denied",
            "space_armed",
            "space_not_found",
            "video_edge_not_found",
            "wrong_hub_state",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        SPACE_ARMED_FIELD_NUMBER: _ClassVar[int]
        HUB_ERROR_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_BUSY_FIELD_NUMBER: _ClassVar[int]
        WRONG_HUB_STATE_FIELD_NUMBER: _ClassVar[int]
        HUB_DEVICE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        hub_error: _response_pb2.Error
        hub_is_busy: _response_pb2.Error
        wrong_hub_state: _response_pb2.Error
        hub_device_not_found: _response_pb2.Error
        hub_offline: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            hub_not_found: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
            hub_is_busy: _response_pb2.Error | _Mapping | None = ...,
            wrong_hub_state: _response_pb2.Error | _Mapping | None = ...,
            hub_device_not_found: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: RemoveBackupChannelResponse.Success
    failure: RemoveBackupChannelResponse.Failure
    def __init__(
        self,
        success: RemoveBackupChannelResponse.Success | _Mapping | None = ...,
        failure: RemoveBackupChannelResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
