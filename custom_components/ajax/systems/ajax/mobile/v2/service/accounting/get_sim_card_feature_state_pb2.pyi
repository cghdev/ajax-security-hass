from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import (
    feature_on_target_pb2 as _feature_on_target_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetSimCardFeatureStateRequest(_message.Message):
    __slots__ = ("hub_id",)
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    hub_id: str
    def __init__(self, hub_id: str | None = ...) -> None: ...

class GetSimCardFeatureStateResponse(_message.Message):
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
    success: GetSimCardFeatureStateResponse.Success
    failure: GetSimCardFeatureStateResponse.Failure
    def __init__(
        self,
        success: GetSimCardFeatureStateResponse.Success | _Mapping | None = ...,
        failure: GetSimCardFeatureStateResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
