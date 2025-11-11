from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class StreamCloudArchiveMetadataFragmentsContentRequest(_message.Message):
    __slots__ = ("get", "init")
    class Init(_message.Message):
        __slots__ = ("channel_id", "metadata_type", "space_id", "video_edge_id")
        SPACE_ID_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_ID_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
        METADATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        space_id: str
        video_edge_id: str
        channel_id: str
        metadata_type: str
        def __init__(
            self,
            space_id: str | None = ...,
            video_edge_id: str | None = ...,
            channel_id: str | None = ...,
            metadata_type: str | None = ...,
        ) -> None: ...

    class Get(_message.Message):
        __slots__ = ("entries", "tag")
        class Entry(_message.Message):
            __slots__ = ("fragment_id",)
            FRAGMENT_ID_FIELD_NUMBER: _ClassVar[int]
            fragment_id: int
            def __init__(self, fragment_id: int | None = ...) -> None: ...

        TAG_FIELD_NUMBER: _ClassVar[int]
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        tag: str
        entries: _containers.RepeatedCompositeFieldContainer[
            StreamCloudArchiveMetadataFragmentsContentRequest.Get.Entry
        ]
        def __init__(
            self,
            tag: str | None = ...,
            entries: _Iterable[
                StreamCloudArchiveMetadataFragmentsContentRequest.Get.Entry | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    INIT_FIELD_NUMBER: _ClassVar[int]
    GET_FIELD_NUMBER: _ClassVar[int]
    init: StreamCloudArchiveMetadataFragmentsContentRequest.Init
    get: StreamCloudArchiveMetadataFragmentsContentRequest.Get
    def __init__(
        self,
        init: StreamCloudArchiveMetadataFragmentsContentRequest.Init
        | _Mapping
        | None = ...,
        get: StreamCloudArchiveMetadataFragmentsContentRequest.Get
        | _Mapping
        | None = ...,
    ) -> None: ...
