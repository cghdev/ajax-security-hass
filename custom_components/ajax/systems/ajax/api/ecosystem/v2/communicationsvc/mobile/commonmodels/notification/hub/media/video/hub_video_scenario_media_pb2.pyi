from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class HubVideoScenarioMedia(_message.Message):
    __slots__ = ("channel_metadata",)
    class ChannelAlarmFrameMetadata(_message.Message):
        __slots__ = (
            "channel_id",
            "channel_name",
            "frame_data_result",
            "room_name",
            "video_edge_id",
        )
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        FRAME_DATA_RESULT_FIELD_NUMBER: _ClassVar[int]
        video_edge_id: str
        channel_id: str
        channel_name: str
        room_name: str
        frame_data_result: HubVideoScenarioMedia.FrameDataResult
        def __init__(
            self,
            video_edge_id: str | None = ...,
            channel_id: str | None = ...,
            channel_name: str | None = ...,
            room_name: str | None = ...,
            frame_data_result: HubVideoScenarioMedia.FrameDataResult
            | _Mapping
            | None = ...,
        ) -> None: ...

    class FrameDataResult(_message.Message):
        __slots__ = ("permission_denied", "url_list")
        URL_LIST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        url_list: HubVideoScenarioMedia.UrlList
        permission_denied: HubVideoScenarioMedia.PermissionDenied
        def __init__(
            self,
            url_list: HubVideoScenarioMedia.UrlList | _Mapping | None = ...,
            permission_denied: HubVideoScenarioMedia.PermissionDenied
            | _Mapping
            | None = ...,
        ) -> None: ...

    class UrlList(_message.Message):
        __slots__ = ("urls",)
        URLS_FIELD_NUMBER: _ClassVar[int]
        urls: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, urls: _Iterable[str] | None = ...) -> None: ...

    class PermissionDenied(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    CHANNEL_METADATA_FIELD_NUMBER: _ClassVar[int]
    channel_metadata: _containers.RepeatedCompositeFieldContainer[
        HubVideoScenarioMedia.ChannelAlarmFrameMetadata
    ]
    def __init__(
        self,
        channel_metadata: _Iterable[
            HubVideoScenarioMedia.ChannelAlarmFrameMetadata | _Mapping
        ]
        | None = ...,
    ) -> None: ...
