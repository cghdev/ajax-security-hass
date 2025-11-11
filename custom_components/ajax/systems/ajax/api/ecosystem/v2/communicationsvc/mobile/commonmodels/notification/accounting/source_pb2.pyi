from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification import (
    source_image_info_pb2 as _source_image_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting import (
    source_info_pb2 as _source_info_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting import (
    source_type_pb2 as _source_type_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AccountingNotificationSource(_message.Message):
    __slots__ = ("id", "image_info", "name", "source_info", "type")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    IMAGE_INFO_FIELD_NUMBER: _ClassVar[int]
    type: _source_type_pb2.AccountingNotificationSourceType
    id: str
    name: str
    source_info: _source_info_pb2.AccountingNotificationSourceInfo
    image_info: _source_image_info_pb2.SourceImageInfo
    def __init__(
        self,
        type: _source_type_pb2.AccountingNotificationSourceType | str | None = ...,
        id: str | None = ...,
        name: str | None = ...,
        source_info: _source_info_pb2.AccountingNotificationSourceInfo
        | _Mapping
        | None = ...,
        image_info: _source_image_info_pb2.SourceImageInfo | _Mapping | None = ...,
    ) -> None: ...
