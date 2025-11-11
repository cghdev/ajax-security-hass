from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import (
    feature_target_pb2 as _feature_target_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    hub_additional_info_pb2 as _hub_additional_info_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    video_edge_additional_info_pb2 as _video_edge_additional_info_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class EnrichedTargetInfo(_message.Message):
    __slots__ = (
        "hub_additional_info",
        "name",
        "room_name",
        "target",
        "target_id",
        "video_edge_additional_info",
    )
    TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
    HUB_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
    target_id: str
    target: _feature_target_pb2.FeatureTarget
    name: str
    room_name: str
    hub_additional_info: _hub_additional_info_pb2.HubAdditionalInfo
    video_edge_additional_info: _video_edge_additional_info_pb2.VideoEdgeAdditionalInfo
    def __init__(
        self,
        target_id: str | None = ...,
        target: _feature_target_pb2.FeatureTarget | str | None = ...,
        name: str | None = ...,
        room_name: str | None = ...,
        hub_additional_info: _hub_additional_info_pb2.HubAdditionalInfo
        | _Mapping
        | None = ...,
        video_edge_additional_info: _video_edge_additional_info_pb2.VideoEdgeAdditionalInfo
        | _Mapping
        | None = ...,
    ) -> None: ...
