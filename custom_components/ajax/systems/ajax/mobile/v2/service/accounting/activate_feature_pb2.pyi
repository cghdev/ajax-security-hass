from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import (
    feature_on_target_pb2 as _feature_on_target_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class ActivateFeatureRequest(_message.Message):
    __slots__ = ("feature_id", "feature_target_id", "reseller_id")
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    RESELLER_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    feature_id: str
    reseller_id: str
    feature_target_id: str
    def __init__(
        self,
        feature_id: str | None = ...,
        reseller_id: str | None = ...,
        feature_target_id: str | None = ...,
    ) -> None: ...

class ActivateFeatureResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("feature",)
        FEATURE_FIELD_NUMBER: _ClassVar[int]
        feature: _feature_on_target_pb2.FeatureOnTarget
        def __init__(
            self,
            feature: _feature_on_target_pb2.FeatureOnTarget | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: str | None = ...) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: ActivateFeatureResponse.Success
    failure: ActivateFeatureResponse.Failure
    def __init__(
        self,
        success: ActivateFeatureResponse.Success | _Mapping | None = ...,
        failure: ActivateFeatureResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
