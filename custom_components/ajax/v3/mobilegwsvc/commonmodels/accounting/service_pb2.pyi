from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import feature_pb2 as _feature_pb2
from v3.mobilegwsvc.commonmodels.accounting import (
    current_service_agreement_pb2 as _current_service_agreement_pb2,
)
from v3.mobilegwsvc.commonmodels.accounting import package_pb2 as _package_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Service(_message.Message):
    __slots__ = (
        "current_service_agreement",
        "feature",
        "max_target_count_to_assign",
        "package",
    )
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SERVICE_AGREEMENT_FIELD_NUMBER: _ClassVar[int]
    MAX_TARGET_COUNT_TO_ASSIGN_FIELD_NUMBER: _ClassVar[int]
    feature: _feature_pb2.Feature
    package: _package_pb2.Package
    current_service_agreement: _current_service_agreement_pb2.CurrentServiceAgreement
    max_target_count_to_assign: int
    def __init__(
        self,
        feature: _feature_pb2.Feature | _Mapping | None = ...,
        package: _package_pb2.Package | _Mapping | None = ...,
        current_service_agreement: _current_service_agreement_pb2.CurrentServiceAgreement
        | _Mapping
        | None = ...,
        max_target_count_to_assign: int | None = ...,
    ) -> None: ...
