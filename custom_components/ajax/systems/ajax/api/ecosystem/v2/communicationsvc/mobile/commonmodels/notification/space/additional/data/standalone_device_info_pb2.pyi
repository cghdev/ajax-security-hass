from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    hub_info_pb2 as _hub_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space.additional.data import (
    video_edge_info_pb2 as _video_edge_info_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StandaloneDeviceInfo(_message.Message):
    __slots__ = ("hub_in_space_info", "video_edge_in_space_info")
    HUB_IN_SPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_IN_SPACE_INFO_FIELD_NUMBER: _ClassVar[int]
    hub_in_space_info: _hub_info_pb2.HubInSpaceInfo
    video_edge_in_space_info: _video_edge_info_pb2.VideoEdgeInSpaceInfo
    def __init__(
        self,
        hub_in_space_info: _hub_info_pb2.HubInSpaceInfo | _Mapping | None = ...,
        video_edge_in_space_info: _video_edge_info_pb2.VideoEdgeInSpaceInfo
        | _Mapping
        | None = ...,
    ) -> None: ...
