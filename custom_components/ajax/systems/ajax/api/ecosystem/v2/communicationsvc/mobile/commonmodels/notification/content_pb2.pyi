from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.accounting import (
    content_pb2 as _content_pb2_1_1_1_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.blank import (
    content_pb2 as _content_pb2_1_1_1_1_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.company import (
    content_pb2 as _content_pb2_1_1_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.hub import (
    content_pb2 as _content_pb2,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.smartlock import (
    content_pb2 as _content_pb2_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.space import (
    content_pb2 as _content_pb2_1_1_1,
)
from systems.ajax.api.ecosystem.v2.communicationsvc.mobile.commonmodels.notification.video import (
    content_pb2 as _content_pb2_1,
)

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationContent(_message.Message):
    __slots__ = (
        "accounting_notification_content",
        "blank_notification_content",
        "company_notification_content",
        "hub_notification_content",
        "smart_lock_notification_content",
        "space_notification_content",
        "video_notification_content",
    )
    HUB_NOTIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    SPACE_NOTIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_NOTIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_NOTIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    COMPANY_NOTIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTING_NOTIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    BLANK_NOTIFICATION_CONTENT_FIELD_NUMBER: _ClassVar[int]
    hub_notification_content: _content_pb2.HubNotificationContent
    space_notification_content: _content_pb2_1_1_1.SpaceNotificationContent
    video_notification_content: _content_pb2_1.VideoNotificationContent
    smart_lock_notification_content: _content_pb2_1_1.SmartLockNotificationContent
    company_notification_content: _content_pb2_1_1_1_1.CompanyNotificationContent
    accounting_notification_content: (
        _content_pb2_1_1_1_1_1.AccountingNotificationContent
    )
    blank_notification_content: _content_pb2_1_1_1_1_1_1.BlankNotificationContent
    def __init__(
        self,
        hub_notification_content: _content_pb2.HubNotificationContent
        | _Mapping
        | None = ...,
        space_notification_content: _content_pb2_1_1_1.SpaceNotificationContent
        | _Mapping
        | None = ...,
        video_notification_content: _content_pb2_1.VideoNotificationContent
        | _Mapping
        | None = ...,
        smart_lock_notification_content: _content_pb2_1_1.SmartLockNotificationContent
        | _Mapping
        | None = ...,
        company_notification_content: _content_pb2_1_1_1_1.CompanyNotificationContent
        | _Mapping
        | None = ...,
        accounting_notification_content: _content_pb2_1_1_1_1_1.AccountingNotificationContent
        | _Mapping
        | None = ...,
        blank_notification_content: _content_pb2_1_1_1_1_1_1.BlankNotificationContent
        | _Mapping
        | None = ...,
    ) -> None: ...
