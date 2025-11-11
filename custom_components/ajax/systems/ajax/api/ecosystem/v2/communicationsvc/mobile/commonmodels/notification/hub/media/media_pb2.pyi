from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import (
    image_status_pb2 as _image_status_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub.media import (
    resource_status_pb2 as _resource_status_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubNotificationMedia(_message.Message):
    __slots__ = ("audio", "expirationTime", "images")
    class Image(_message.Message):
        __slots__ = ("file_name", "status", "url")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        status: _image_status_pb2.ImageStatus
        file_name: str
        url: str
        def __init__(
            self,
            status: _image_status_pb2.ImageStatus | str | None = ...,
            file_name: str | None = ...,
            url: str | None = ...,
        ) -> None: ...

    class Audio(_message.Message):
        __slots__ = ("file_name", "status", "url")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        FILE_NAME_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        status: _resource_status_pb2.ResourceStatus
        file_name: str
        url: str
        def __init__(
            self,
            status: _resource_status_pb2.ResourceStatus | str | None = ...,
            file_name: str | None = ...,
            url: str | None = ...,
        ) -> None: ...

    EXPIRATIONTIME_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    expirationTime: _timestamp_pb2.Timestamp
    images: _containers.RepeatedCompositeFieldContainer[HubNotificationMedia.Image]
    audio: _containers.RepeatedCompositeFieldContainer[HubNotificationMedia.Audio]
    def __init__(
        self,
        expirationTime: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        images: _Iterable[HubNotificationMedia.Image | _Mapping] | None = ...,
        audio: _Iterable[HubNotificationMedia.Audio | _Mapping] | None = ...,
    ) -> None: ...
