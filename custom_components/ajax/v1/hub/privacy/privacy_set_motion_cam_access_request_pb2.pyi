from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v1.hub.privacy import (
    privacy_motion_cam_access_pb2 as _privacy_motion_cam_access_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class PrivacySetMotionCamAccessRequest(_message.Message):
    __slots__ = ("hub_id", "privacy_access")
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_ACCESS_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    privacy_access: _privacy_motion_cam_access_pb2.PrivacyMotionCamAccess
    def __init__(
        self,
        hub_id: str | None = ...,
        privacy_access: _privacy_motion_cam_access_pb2.PrivacyMotionCamAccess
        | _Mapping
        | None = ...,
    ) -> None: ...
