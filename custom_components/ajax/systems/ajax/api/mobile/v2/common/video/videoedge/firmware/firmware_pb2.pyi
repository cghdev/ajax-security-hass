from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import (
    firmware_version_pb2 as _firmware_version_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class FirmwareUpdateState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUS_OTHER: _ClassVar[FirmwareUpdateState]
    FUS_IDLE: _ClassVar[FirmwareUpdateState]
    FUS_DOWNLOADING: _ClassVar[FirmwareUpdateState]
    FUS_APPLYING: _ClassVar[FirmwareUpdateState]

class FirmwareUpdateError(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUR_OTHER: _ClassVar[FirmwareUpdateError]
    FUR_OK: _ClassVar[FirmwareUpdateError]
    FUR_ABORTED: _ClassVar[FirmwareUpdateError]
    FUR_DOWNLOAD_FAILED: _ClassVar[FirmwareUpdateError]
    FUR_BAD_IMAGE: _ClassVar[FirmwareUpdateError]
    FUR_INCOMPATIBLE_VERSION: _ClassVar[FirmwareUpdateError]
    FUR_PRODUCT_MISMATCH: _ClassVar[FirmwareUpdateError]
    FUR_PLATFORM_MISMATCH: _ClassVar[FirmwareUpdateError]
    FUR_FLASHING_FAILED: _ClassVar[FirmwareUpdateError]
    FUR_USERDATA_MOVE_FAILED: _ClassVar[FirmwareUpdateError]
    FUR_FWSWITCH_FAILED: _ClassVar[FirmwareUpdateError]
    FUR_IMAGE_VALIDATION_FAILED: _ClassVar[FirmwareUpdateError]
    FUR_LIFETIME_VALIDATION_FAILED: _ClassVar[FirmwareUpdateError]

FUS_OTHER: FirmwareUpdateState
FUS_IDLE: FirmwareUpdateState
FUS_DOWNLOADING: FirmwareUpdateState
FUS_APPLYING: FirmwareUpdateState
FUR_OTHER: FirmwareUpdateError
FUR_OK: FirmwareUpdateError
FUR_ABORTED: FirmwareUpdateError
FUR_DOWNLOAD_FAILED: FirmwareUpdateError
FUR_BAD_IMAGE: FirmwareUpdateError
FUR_INCOMPATIBLE_VERSION: FirmwareUpdateError
FUR_PRODUCT_MISMATCH: FirmwareUpdateError
FUR_PLATFORM_MISMATCH: FirmwareUpdateError
FUR_FLASHING_FAILED: FirmwareUpdateError
FUR_USERDATA_MOVE_FAILED: FirmwareUpdateError
FUR_FWSWITCH_FAILED: FirmwareUpdateError
FUR_IMAGE_VALIDATION_FAILED: FirmwareUpdateError
FUR_LIFETIME_VALIDATION_FAILED: FirmwareUpdateError

class Firmware(_message.Message):
    __slots__ = ("critical_update_available", "update_status")
    UPDATE_STATUS_FIELD_NUMBER: _ClassVar[int]
    CRITICAL_UPDATE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    update_status: FirmwareUpdateStatus
    critical_update_available: bool
    def __init__(
        self,
        update_status: FirmwareUpdateStatus | _Mapping | None = ...,
        critical_update_available: bool = ...,
    ) -> None: ...

class FirmwareUpdateStatus(_message.Message):
    __slots__ = ("error", "progress", "state", "version")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    version: _firmware_version_pb2.FirmwareVersion
    state: FirmwareUpdateState
    progress: int
    error: FirmwareUpdateError
    def __init__(
        self,
        version: _firmware_version_pb2.FirmwareVersion | _Mapping | None = ...,
        state: FirmwareUpdateState | str | None = ...,
        progress: int | None = ...,
        error: FirmwareUpdateError | str | None = ...,
    ) -> None: ...
