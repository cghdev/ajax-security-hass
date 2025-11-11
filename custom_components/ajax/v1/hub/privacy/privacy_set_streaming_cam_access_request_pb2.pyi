from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1.hub.privacy import (
    privacy_streaming_cam_access_pb2 as _privacy_streaming_cam_access_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class PrivacySetStreamingCamAccessRequest(_message.Message):
    __slots__ = ("hub_id", "privacy_access")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    privacy_access: _privacy_streaming_cam_access_pb2.PrivacyStreamingCamAccess
    def __init__(
        self,
        hub_id: str | None = ...,
        privacy_access: _privacy_streaming_cam_access_pb2.PrivacyStreamingCamAccess
        | _Mapping
        | None = ...,
    ) -> None: ...
