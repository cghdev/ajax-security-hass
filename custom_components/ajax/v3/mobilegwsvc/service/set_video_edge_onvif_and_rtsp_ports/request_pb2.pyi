from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SetVideoEdgeOnvifAndRtspPortsRequest(_message.Message):
    __slots__ = ("onvif_http_port", "rtsp_http_port", "space_id", "video_edge_id")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
    ONVIF_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    RTSP_HTTP_PORT_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    video_edge_id: str
    onvif_http_port: int
    rtsp_http_port: int
    def __init__(
        self,
        space_id: str | None = ...,
        video_edge_id: str | None = ...,
        onvif_http_port: int | None = ...,
        rtsp_http_port: int | None = ...,
    ) -> None: ...
