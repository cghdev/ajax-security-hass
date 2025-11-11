from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    notification_event_type_pb2 as _notification_event_type_pb2,
)
from v3.mobilegwsvc.commonmodels.video.videoedge.channel.notification import (
    video_notification_alert_with_siren_pb2 as _video_notification_alert_with_siren_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class GetVideoNotificationAlertSettingsResponse(_message.Message):
    __slots__ = ("failure", "success")
    class NotificationAlertSettingsCapability(
        int, metaclass=_enum_type_wrapper.EnumTypeWrapper
    ):
        __slots__ = ()
        NOTIFICATION_ALERT_SETTINGS_CAPABILITY_UNSPECIFIED: _ClassVar[
            GetVideoNotificationAlertSettingsResponse.NotificationAlertSettingsCapability
        ]
        NOTIFICATION_ALERT_SETTINGS_CAPABILITY_ALERT_WITH_SIREN: _ClassVar[
            GetVideoNotificationAlertSettingsResponse.NotificationAlertSettingsCapability
        ]

    NOTIFICATION_ALERT_SETTINGS_CAPABILITY_UNSPECIFIED: (
        GetVideoNotificationAlertSettingsResponse.NotificationAlertSettingsCapability
    )
    NOTIFICATION_ALERT_SETTINGS_CAPABILITY_ALERT_WITH_SIREN: (
        GetVideoNotificationAlertSettingsResponse.NotificationAlertSettingsCapability
    )
    class Success(_message.Message):
        __slots__ = ("alert_with_siren", "capabilities", "notification_event_type")
        ALERT_WITH_SIREN_FIELD_NUMBER: _ClassVar[int]
        CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        alert_with_siren: _video_notification_alert_with_siren_pb2.AlertWithSiren
        capabilities: _containers.RepeatedScalarFieldContainer[
            GetVideoNotificationAlertSettingsResponse.NotificationAlertSettingsCapability
        ]
        notification_event_type: _notification_event_type_pb2.NotificationEventType
        def __init__(
            self,
            alert_with_siren: _video_notification_alert_with_siren_pb2.AlertWithSiren
            | str
            | None = ...,
            capabilities: _Iterable[
                GetVideoNotificationAlertSettingsResponse.NotificationAlertSettingsCapability
                | str
            ]
            | None = ...,
            notification_event_type: _notification_event_type_pb2.NotificationEventType
            | str
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = (
            "bad_request",
            "channel_not_found",
            "permission_denied",
            "space_not_found",
            "video_edge_not_found",
        )
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        VIDEO_EDGE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        space_not_found: _response_pb2.Error
        video_edge_not_found: _response_pb2.Error
        channel_not_found: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
            space_not_found: _response_pb2.Error | _Mapping | None = ...,
            video_edge_not_found: _response_pb2.Error | _Mapping | None = ...,
            channel_not_found: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: GetVideoNotificationAlertSettingsResponse.Success
    failure: GetVideoNotificationAlertSettingsResponse.Failure
    def __init__(
        self,
        success: GetVideoNotificationAlertSettingsResponse.Success
        | _Mapping
        | None = ...,
        failure: GetVideoNotificationAlertSettingsResponse.Failure
        | _Mapping
        | None = ...,
    ) -> None: ...
