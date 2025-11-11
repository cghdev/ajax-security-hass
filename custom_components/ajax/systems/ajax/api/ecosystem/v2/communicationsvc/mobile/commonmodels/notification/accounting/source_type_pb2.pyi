from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class AccountingNotificationSourceType(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = ()
    ACCOUNTING_NOTIFICATION_SOURCE_TYPE_UNSPECIFIED: _ClassVar[
        AccountingNotificationSourceType
    ]
    HUB: _ClassVar[AccountingNotificationSourceType]
    VIDEO_EDGE: _ClassVar[AccountingNotificationSourceType]
    SUBSCRIPTION: _ClassVar[AccountingNotificationSourceType]

ACCOUNTING_NOTIFICATION_SOURCE_TYPE_UNSPECIFIED: AccountingNotificationSourceType
HUB: AccountingNotificationSourceType
VIDEO_EDGE: AccountingNotificationSourceType
SUBSCRIPTION: AccountingNotificationSourceType
