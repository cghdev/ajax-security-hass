from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    channel_permission_pb2 as _channel_permission_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video.additional.data.privacy import (
    requested_video_channel_data_pb2 as _requested_video_channel_data_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class TemporaryVideoAccessRequestFromCompanyData(_message.Message):
    __slots__ = ("channels", "duration", "initiator_email", "permissions", "request_id")
    INITIATOR_EMAIL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNELS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    initiator_email: str
    request_id: str
    channels: _containers.RepeatedCompositeFieldContainer[
        _requested_video_channel_data_pb2.RequestedVideoChannelData
    ]
    permissions: _containers.RepeatedScalarFieldContainer[
        _channel_permission_pb2.ChannelPermission
    ]
    duration: _duration_pb2.Duration
    def __init__(
        self,
        initiator_email: str | None = ...,
        request_id: str | None = ...,
        channels: _Iterable[
            _requested_video_channel_data_pb2.RequestedVideoChannelData | _Mapping
        ]
        | None = ...,
        permissions: _Iterable[_channel_permission_pb2.ChannelPermission | str]
        | None = ...,
        duration: _duration_pb2.Duration | _Mapping | None = ...,
    ) -> None: ...
