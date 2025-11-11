from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.accounting import (
    feature_target_pb2 as _feature_target_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateServicesRequest(_message.Message):
    __slots__ = (
        "agreement_version",
        "feature_target",
        "feature_target_id",
        "reseller_id",
        "service_to_activate",
    )
    class ServiceToActivate(_message.Message):
        __slots__ = ("feature_id", "package_id")
        FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
        feature_id: str
        package_id: str
        def __init__(
            self, feature_id: str | None = ..., package_id: str | None = ...
        ) -> None: ...

    FEATURE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    SERVICE_TO_ACTIVATE_FIELD_NUMBER: _ClassVar[int]
    RESELLER_ID_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    feature_target_id: _containers.RepeatedScalarFieldContainer[str]
    feature_target: _feature_target_pb2.FeatureTarget
    service_to_activate: _containers.RepeatedCompositeFieldContainer[
        ActivateServicesRequest.ServiceToActivate
    ]
    reseller_id: str
    agreement_version: str
    def __init__(
        self,
        feature_target_id: _Iterable[str] | None = ...,
        feature_target: _feature_target_pb2.FeatureTarget | str | None = ...,
        service_to_activate: _Iterable[
            ActivateServicesRequest.ServiceToActivate | _Mapping
        ]
        | None = ...,
        reseller_id: str | None = ...,
        agreement_version: str | None = ...,
    ) -> None: ...
