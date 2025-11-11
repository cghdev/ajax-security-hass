from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.video import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCloudArchiveVideoFragmentsContentRequest(_message.Message):
    __slots__ = ("get", "init")
    class Init(_message.Message):
        __slots__ = ("channel_id", "space_id", "stream_type", "video_edge_id")
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        video_edge_id: str
        channel_id: str
        stream_type: _types_pb2.StreamType
        def __init__(
            self,
            space_id: str | None = ...,
            video_edge_id: str | None = ...,
            channel_id: str | None = ...,
            stream_type: _types_pb2.StreamType | str | None = ...,
        ) -> None: ...

    class Get(_message.Message):
        __slots__ = ("entries", "tag")
        class Entry(_message.Message):
            __slots__ = ("fragment_id", "fragment_part")
            FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
            FRAGMENT_PART_FIELD_NUMBER: _ClassVar[int]
            fragment_id: int
            fragment_part: (
                StreamCloudArchiveVideoFragmentsContentRequest.Get.FragmentPart
            )
            def __init__(
                self,
                fragment_id: int | None = ...,
                fragment_part: StreamCloudArchiveVideoFragmentsContentRequest.Get.FragmentPart
                | _Mapping
                | None = ...,
            ) -> None: ...

        class FragmentPart(_message.Message):
            __slots__ = ("fragment_id", "offset")
            FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            fragment_id: int
            offset: int
            def __init__(
                self, fragment_id: int | None = ..., offset: int | None = ...
            ) -> None: ...

        TAG_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        tag: str
        entries: _containers.RepeatedCompositeFieldContainer[
            StreamCloudArchiveVideoFragmentsContentRequest.Get.Entry
        ]
        def __init__(
            self,
            tag: str | None = ...,
            entries: _Iterable[
                StreamCloudArchiveVideoFragmentsContentRequest.Get.Entry | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    INIT_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    init: StreamCloudArchiveVideoFragmentsContentRequest.Init
    get: StreamCloudArchiveVideoFragmentsContentRequest.Get
    def __init__(
        self,
        init: StreamCloudArchiveVideoFragmentsContentRequest.Init
        | _Mapping
        | None = ...,
        get: StreamCloudArchiveVideoFragmentsContentRequest.Get | _Mapping | None = ...,
    ) -> None: ...
