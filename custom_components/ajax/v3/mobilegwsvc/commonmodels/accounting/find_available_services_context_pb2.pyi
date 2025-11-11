from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from v3.mobilegwsvc.commonmodels.accounting import (
    enriched_target_info_pb2 as _enriched_target_info_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import reseller_pb2 as _reseller_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class FindAvailableServicesContext(_message.Message):
    __slots__ = ("selected_feature_target_info", "selected_reseller")
    SELECTED_FEATURE_TARGET_INFO_FIELD_NUMBER: _ClassVar[int]
    SELECTED_RESELLER_FIELD_NUMBER: _ClassVar[int]
    selected_feature_target_info: _enriched_target_info_pb2.EnrichedTargetInfo
    selected_reseller: _reseller_pb2.Reseller
    def __init__(
        self,
        selected_feature_target_info: _enriched_target_info_pb2.EnrichedTargetInfo
        | _Mapping
        | None = ...,
        selected_reseller: _reseller_pb2.Reseller | _Mapping | None = ...,
    ) -> None: ...
