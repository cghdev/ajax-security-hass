from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBackupChannelResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "hub_device_already_added",
            "hub_error",
            "hub_is_busy",
            "hub_not_found",
            "hub_offline",
            "mcu_invalid_state",
            "mcu_io_error",
            "mcu_no_response_from_mcu",
            "need_update_hub_firmware",
            "objects_limit_exceeded",
            "permission_denied",
            "search_timeout",
            "space_armed",
            "space_not_found",
            "unknown_hub_device",
            "unsupported_hub_device",
            "video_edge_is_offline",
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
        SEARCH_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
        HUB_IS_BUSY_FIELD_NUMBER: _ClassVar[int]
        WRONG_HUB_STATE_FIELD_NUMBER: _ClassVar[int]
        OBJECTS_LIMIT_EXCEEDED_FIELD_NUMBER: _ClassVar[int]
        HUB_DEVICE_ALREADY_ADDED_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN_HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        UNSUPPORTED_HUB_DEVICE_FIELD_NUMBER: _ClassVar[int]
        NEED_UPDATE_HUB_FIRMWARE_FIELD_NUMBER: _ClassVar[int]
        HUB_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_IS_OFFLINE_FIELD_NUMBER: _ClassVar[int]
        MCU_IO_ERROR_FIELD_NUMBER: _ClassVar[int]
        MCU_INVALID_STATE_FIELD_NUMBER: _ClassVar[int]
        MCU_NO_RESPONSE_FROM_MCU_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        space_not_found: _response_pb2.Error
        permission_denied: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        hub_not_found: _response_pb2.Error
        space_armed: _response_pb2.Error
        hub_error: _response_pb2.Error
        search_timeout: _response_pb2.Error
        hub_is_busy: _response_pb2.Error
        wrong_hub_state: _response_pb2.Error
        objects_limit_exceeded: _response_pb2.Error
        hub_device_already_added: _response_pb2.Error
        unknown_hub_device: _response_pb2.Error
        unsupported_hub_device: _response_pb2.Error
        need_update_hub_firmware: _response_pb2.Error
        hub_offline: _response_pb2.Error
        video_edge_is_offline: _response_pb2.Error
        mcu_io_error: _response_pb2.Error
        mcu_invalid_state: _response_pb2.Error
        mcu_no_response_from_mcu: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            hub_not_found: _response_pb2.Error | _Mapping | None = ...,
            space_armed: _response_pb2.Error | _Mapping | None = ...,
            hub_error: _response_pb2.Error | _Mapping | None = ...,
            search_timeout: _response_pb2.Error | _Mapping | None = ...,
            hub_is_busy: _response_pb2.Error | _Mapping | None = ...,
            wrong_hub_state: _response_pb2.Error | _Mapping | None = ...,
            objects_limit_exceeded: _response_pb2.Error | _Mapping | None = ...,
            hub_device_already_added: _response_pb2.Error | _Mapping | None = ...,
            unknown_hub_device: _response_pb2.Error | _Mapping | None = ...,
            unsupported_hub_device: _response_pb2.Error | _Mapping | None = ...,
            need_update_hub_firmware: _response_pb2.Error | _Mapping | None = ...,
            hub_offline: _response_pb2.Error | _Mapping | None = ...,
            video_edge_is_offline: _response_pb2.Error | _Mapping | None = ...,
            mcu_io_error: _response_pb2.Error | _Mapping | None = ...,
            mcu_invalid_state: _response_pb2.Error | _Mapping | None = ...,
            mcu_no_response_from_mcu: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CreateBackupChannelResponse.Success
    failure: CreateBackupChannelResponse.Failure
    def __init__(
        self,
        success: CreateBackupChannelResponse.Success | _Mapping | None = ...,
        failure: CreateBackupChannelResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
