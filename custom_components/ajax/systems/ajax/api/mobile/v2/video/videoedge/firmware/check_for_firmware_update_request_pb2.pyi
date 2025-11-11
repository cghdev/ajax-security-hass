from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import (
    firmware_version_pb2 as _firmware_version_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.firmware import (
    release_notes_pb2 as _release_notes_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CheckForFirmwareUpdateRequest(_message.Message):
    __slots__ = ("language_code", "space_locator", "video_edge_id")
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    video_edge_id: str
    language_code: str
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self,
        video_edge_id: str | None = ...,
        language_code: str | None = ...,
        space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...,
    ) -> None: ...

class CheckForFirmwareUpdateResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("firmwareUpdate",)
        class FirmwareUpdate(_message.Message):
            __slots__ = ("firmware_version", "release_notes")
            FIRMWARE_VERSION_FIELD_NUMBER: _ClassVar[int]
            RELEASE_NOTES_FIELD_NUMBER: _ClassVar[int]
            firmware_version: _firmware_version_pb2.FirmwareVersion
            release_notes: _release_notes_pb2.ReleaseNotes
            def __init__(
                self,
                firmware_version: _firmware_version_pb2.FirmwareVersion
                | _Mapping
                | None = ...,
                release_notes: _release_notes_pb2.ReleaseNotes | _Mapping | None = ...,
            ) -> None: ...

        FIRMWAREUPDATE_FIELD_NUMBER: _ClassVar[int]
        firmwareUpdate: CheckForFirmwareUpdateResponse.Success.FirmwareUpdate
        def __init__(
            self,
            firmwareUpdate: CheckForFirmwareUpdateResponse.Success.FirmwareUpdate
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "video_edge_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        video_edge_not_found: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: CheckForFirmwareUpdateResponse.Success
    failure: CheckForFirmwareUpdateResponse.Failure
    def __init__(
        self,
        success: CheckForFirmwareUpdateResponse.Success | _Mapping | None = ...,
        failure: CheckForFirmwareUpdateResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
