from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class SwitchServiceForSubscriptionRequest(_message.Message):
    __slots__ = (
        "agreement_version",
        "current_subscription_id",
        "feature_id",
        "package_id",
    )
    CURRENT_SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    FEATURE_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_ID_FIELD_NUMBER: _ClassVar[int]
    AGREEMENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    current_subscription_id: str
    feature_id: str
    package_id: str
    agreement_version: str
    def __init__(
        self,
        current_subscription_id: str | None = ...,
        feature_id: str | None = ...,
        package_id: str | None = ...,
        agreement_version: str | None = ...,
    ) -> None: ...
