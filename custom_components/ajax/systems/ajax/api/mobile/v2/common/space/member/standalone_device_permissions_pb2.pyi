from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.space.member import (
    hub_standalone_device_permissions_pb2 as _hub_standalone_device_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_device_permissions_pb2 as _smart_lock_device_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.video.privacy import (
    video_edge_permissions_pb2 as _video_edge_permissions_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StandaloneDevicePermissions(_message.Message):
    __slots__ = ("hub_permissions", "smart_lock_permissions", "video_edge_permissions")
    VIDEO_EDGE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    video_edge_permissions: _video_edge_permissions_pb2.VideoEdgePermissions
    hub_permissions: (
        _hub_standalone_device_permissions_pb2.HubStandaloneDevicePermissions
    )
    smart_lock_permissions: _smart_lock_device_permissions_pb2.SmartLockPermissions
    def __init__(
        self,
        video_edge_permissions: _video_edge_permissions_pb2.VideoEdgePermissions
        | _Mapping
        | None = ...,
        hub_permissions: _hub_standalone_device_permissions_pb2.HubStandaloneDevicePermissions
        | _Mapping
        | None = ...,
        smart_lock_permissions: _smart_lock_device_permissions_pb2.SmartLockPermissions
        | _Mapping
        | None = ...,
    ) -> None: ...
