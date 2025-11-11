from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.video.videoedge.network import (
    network_wifi_credentials_pb2 as _network_wifi_credentials_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectVideoEdgeToWifiRequest(_message.Message):
    __slots__ = ("credentials", "network_interface_id", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INTERFACE_ID_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    network_interface_id: str
    credentials: _network_wifi_credentials_pb2.NetworkWifiCredentials
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        network_interface_id: str | None = ...,
        credentials: _network_wifi_credentials_pb2.NetworkWifiCredentials
        | _Mapping
        | None = ...,
    ) -> None: ...
