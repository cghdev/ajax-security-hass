from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.video import (
    types_pb2 as _types_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class DirectExportRequestedData(_message.Message):
    __slots__ = (
        "channel_id",
        "channel_name",
        "export_ranges",
        "initiator_member_id",
        "initiator_name",
        "timezone_id",
    )
    INITIATOR_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_NAME_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    EXPORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_ID_FIELD_NUMBER: _ClassVar[int]
    initiator_member_id: str
    initiator_name: str
    channel_id: str
    channel_name: str
    export_ranges: _containers.RepeatedCompositeFieldContainer[
        _types_pb2.TimestampRange
    ]
    timezone_id: str
    def __init__(
        self,
        initiator_member_id: str | None = ...,
        initiator_name: str | None = ...,
        channel_id: str | None = ...,
        channel_name: str | None = ...,
        export_ranges: _Iterable[_types_pb2.TimestampRange | _Mapping] | None = ...,
        timezone_id: str | None = ...,
    ) -> None: ...
