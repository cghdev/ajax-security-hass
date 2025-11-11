from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.accounting import (
    feature_target_pb2 as _feature_target_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class RestoreTargetRequest(_message.Message):
    __slots__ = ("feature_id", "feature_target", "feature_target_id", "package_id")
    FEATURE_TARGET_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_TARGET_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    feature_target_id: str
    feature_target: _feature_target_pb2.FeatureTarget
    feature_id: str
    package_id: str
    def __init__(
        self,
        feature_target_id: str | None = ...,
        feature_target: _feature_target_pb2.FeatureTarget | str | None = ...,
        feature_id: str | None = ...,
        package_id: str | None = ...,
    ) -> None: ...
