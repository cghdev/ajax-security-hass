from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from v3.mobilegwsvc.commonmodels.accounting import (
    enriched_target_info_pb2 as _enriched_target_info_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import (
    service_group_pb2 as _service_group_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class AvailablePrePaymentServiceGroup(_message.Message):
    __slots__ = ("feature_target_infos", "service_group")
    SERVICE_GROUP_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_INFOS_FIELD_NUMBER: _ClassVar[int]
    service_group: _service_group_pb2.ServiceGroup
    feature_target_infos: _containers.RepeatedCompositeFieldContainer[
        _enriched_target_info_pb2.EnrichedTargetInfo
    ]
    def __init__(
        self,
        service_group: _service_group_pb2.ServiceGroup | _Mapping | None = ...,
        feature_target_infos: _Iterable[
            _enriched_target_info_pb2.EnrichedTargetInfo | _Mapping
        ]
        | None = ...,
    ) -> None: ...
