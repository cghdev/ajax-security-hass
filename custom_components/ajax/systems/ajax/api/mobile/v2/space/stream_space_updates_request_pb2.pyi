from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.accounting import (
    extra_services_availability_status_pb2 as _extra_services_availability_status_pb2,
)
from systems.ajax.api.mobile.v2.common.accounting import (
    service_deactivation_pending_status_pb2 as _service_deactivation_pending_status_pb2,
)
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2
from systems.ajax.api.mobile.v2.common.space import (
    current_member_pb2 as _current_member_pb2,
)
from systems.ajax.api.mobile.v2.common.space import (
    space_address_pb2 as _space_address_pb2,
)
from systems.ajax.api.mobile.v2.common.space import (
    space_locator_pb2 as _space_locator_pb2,
)
from systems.ajax.api.mobile.v2.common.space import space_pb2 as _space_pb2
from systems.ajax.api.mobile.v2.common.space import (
    space_profile_pb2 as _space_profile_pb2,
)
from systems.ajax.api.mobile.v2.common.space.capability import (
    space_capabilities_pb2 as _space_capabilities_pb2,
)
from systems.ajax.api.mobile.v2.common.space.company import (
    privacy_override_pb2 as _privacy_override_pb2,
)
from systems.ajax.api.mobile.v2.common.space.company import (
    space_installation_company_pb2 as _space_installation_company_pb2,
)
from systems.ajax.api.mobile.v2.common.space.company import (
    space_monitoring_company_pb2 as _space_monitoring_company_pb2,
)
from systems.ajax.api.mobile.v2.common.space.device import (
    standalone_device_pb2 as _standalone_device_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    pending_member_pb2 as _pending_member_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    space_member_pb2 as _space_member_pb2,
)
from systems.ajax.api.mobile.v2.common.space.room import room_pb2 as _room_pb2
from systems.ajax.api.mobile.v2.common.space.security import (
    space_security_mode_pb2 as _space_security_mode_pb2,
)
from systems.ajax.api.mobile.v2.common.space.security.group import (
    group_pb2 as _group_pb2,
)
from systems.ajax.api.mobile.v2.common.space.stream import (
    external_stream_control_pb2 as _external_stream_control_pb2,
)
from systems.ajax.api.mobile.v2.common.time import time_zone_pb2 as _time_zone_pb2
from systems.ajax.api.mobile.v2.common.video import video_wall_pb2 as _video_wall_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceUpdatesRequest(_message.Message):
    __slots__ = ("space_locator",)
    SPACE_LOCATOR_FIELD_NUMBER: _ClassVar[int]
    space_locator: _space_locator_pb2.SpaceLocator
    def __init__(
        self, space_locator: _space_locator_pb2.SpaceLocator | _Mapping | None = ...
    ) -> None: ...

class StreamSpaceUpdatesResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update", "updates")
        class Updates(_message.Message):
            __slots__ = ("updates",)
            UPDATES_FIELD_NUMBER: _ClassVar[int]
            updates: _containers.RepeatedCompositeFieldContainer[
                StreamSpaceUpdatesResponse.Success.Update
            ]
            def __init__(
                self,
                updates: _Iterable[StreamSpaceUpdatesResponse.Success.Update | _Mapping]
                | None = ...,
            ) -> None: ...

        class Update(_message.Message):
            __slots__ = (
                "address",
                "current_member",
                "device",
                "external_stream_controls",
                "extra_services_availability_status",
                "extra_services_availability_status_v2",
                "group",
                "installation_company",
                "member",
                "monitoring_company",
                "pending_member",
                "privacy_override",
                "profile",
                "room",
                "security_mode",
                "service_deactivation_pending_status",
                "space_capabilities",
                "space_id",
                "space_update_type",
                "time_zone_id",
                "total_notification_unread_counter",
                "video_wall",
            )
            class SpaceUpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SPACE_UPDATE_TYPE_UNKNOWN: _ClassVar[
                    StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
                ]
                SPACE_UPDATE_TYPE_ADD: _ClassVar[
                    StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
                ]
                SPACE_UPDATE_TYPE_UPDATE: _ClassVar[
                    StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
                ]
                SPACE_UPDATE_TYPE_REMOVE: _ClassVar[
                    StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
                ]

            SPACE_UPDATE_TYPE_UNKNOWN: (
                StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            )
            SPACE_UPDATE_TYPE_ADD: (
                StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            )
            SPACE_UPDATE_TYPE_UPDATE: (
                StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            )
            SPACE_UPDATE_TYPE_REMOVE: (
                StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            )
            SPACE_ID_FIELD_NUMBER: _ClassVar[int]
            SPACE_UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
            CURRENT_MEMBER_FIELD_NUMBER: _ClassVar[int]
            TOTAL_NOTIFICATION_UNREAD_COUNTER_FIELD_NUMBER: _ClassVar[int]
            SECURITY_MODE_FIELD_NUMBER: _ClassVar[int]
            GROUP_FIELD_NUMBER: _ClassVar[int]
            PROFILE_FIELD_NUMBER: _ClassVar[int]
            MEMBER_FIELD_NUMBER: _ClassVar[int]
            ROOM_FIELD_NUMBER: _ClassVar[int]
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            INSTALLATION_COMPANY_FIELD_NUMBER: _ClassVar[int]
            MONITORING_COMPANY_FIELD_NUMBER: _ClassVar[int]
            PRIVACY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
            TIME_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
            PENDING_MEMBER_FIELD_NUMBER: _ClassVar[int]
            VIDEO_WALL_FIELD_NUMBER: _ClassVar[int]
            ADDRESS_FIELD_NUMBER: _ClassVar[int]
            SERVICE_DEACTIVATION_PENDING_STATUS_FIELD_NUMBER: _ClassVar[int]
            EXTRA_SERVICES_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
            SPACE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
            EXTRA_SERVICES_AVAILABILITY_STATUS_V2_FIELD_NUMBER: _ClassVar[int]
            EXTERNAL_STREAM_CONTROLS_FIELD_NUMBER: _ClassVar[int]
            space_id: str
            space_update_type: StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
            current_member: _current_member_pb2.CurrentMember
            total_notification_unread_counter: int
            security_mode: _space_security_mode_pb2.SpaceSecurityMode
            group: _group_pb2.Group
            profile: _space_profile_pb2.SpaceProfile
            member: _space_member_pb2.SpaceMember
            room: _room_pb2.Room
            device: _standalone_device_pb2.StandaloneDevice
            installation_company: (
                _space_installation_company_pb2.SpaceInstallationCompany
            )
            monitoring_company: _space_monitoring_company_pb2.SpaceMonitoringCompany
            privacy_override: _privacy_override_pb2.PrivacyOverride
            time_zone_id: _time_zone_pb2.TimeZone
            pending_member: _pending_member_pb2.PendingMember
            video_wall: _video_wall_pb2.VideoWall
            address: _space_address_pb2.SpaceAddress
            service_deactivation_pending_status: _service_deactivation_pending_status_pb2.ServiceDeactivationPendingStatus
            extra_services_availability_status: (
                _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
            )
            space_capabilities: _space_capabilities_pb2.SpaceCapabilities
            extra_services_availability_status_v2: (
                _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
            )
            external_stream_controls: _external_stream_control_pb2.ExternalStreamControl
            def __init__(
                self,
                space_id: str | None = ...,
                space_update_type: StreamSpaceUpdatesResponse.Success.Update.SpaceUpdateType
                | str
                | None = ...,
                current_member: _current_member_pb2.CurrentMember
                | _Mapping
                | None = ...,
                total_notification_unread_counter: int | None = ...,
                security_mode: _space_security_mode_pb2.SpaceSecurityMode
                | _Mapping
                | None = ...,
                group: _group_pb2.Group | _Mapping | None = ...,
                profile: _space_profile_pb2.SpaceProfile | _Mapping | None = ...,
                member: _space_member_pb2.SpaceMember | _Mapping | None = ...,
                room: _room_pb2.Room | _Mapping | None = ...,
                device: _standalone_device_pb2.StandaloneDevice | _Mapping | None = ...,
                installation_company: _space_installation_company_pb2.SpaceInstallationCompany
                | _Mapping
                | None = ...,
                monitoring_company: _space_monitoring_company_pb2.SpaceMonitoringCompany
                | _Mapping
                | None = ...,
                privacy_override: _privacy_override_pb2.PrivacyOverride
                | _Mapping
                | None = ...,
                time_zone_id: _time_zone_pb2.TimeZone | _Mapping | None = ...,
                pending_member: _pending_member_pb2.PendingMember
                | _Mapping
                | None = ...,
                video_wall: _video_wall_pb2.VideoWall | _Mapping | None = ...,
                address: _space_address_pb2.SpaceAddress | _Mapping | None = ...,
                service_deactivation_pending_status: _service_deactivation_pending_status_pb2.ServiceDeactivationPendingStatus
                | str
                | None = ...,
                extra_services_availability_status: _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
                | str
                | None = ...,
                space_capabilities: _space_capabilities_pb2.SpaceCapabilities
                | _Mapping
                | None = ...,
                extra_services_availability_status_v2: _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
                | str
                | None = ...,
                external_stream_controls: _external_stream_control_pb2.ExternalStreamControl
                | _Mapping
                | None = ...,
            ) -> None: ...

        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        UPDATES_FIELD_NUMBER: _ClassVar[int]
        snapshot: _space_pb2.Space
        update: StreamSpaceUpdatesResponse.Success.Update
        updates: StreamSpaceUpdatesResponse.Success.Updates
        def __init__(
            self,
            snapshot: _space_pb2.Space | _Mapping | None = ...,
            update: StreamSpaceUpdatesResponse.Success.Update | _Mapping | None = ...,
            updates: StreamSpaceUpdatesResponse.Success.Updates | _Mapping | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied", "space_not_found")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        SPACE_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.DefaultError
        space_not_found: _response_pb2.DefaultError
        permission_denied: _response_pb2.DefaultError
        def __init__(
            self,
            bad_request: _response_pb2.DefaultError | _Mapping | None = ...,
            space_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            permission_denied: _response_pb2.DefaultError | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamSpaceUpdatesResponse.Success
    failure: StreamSpaceUpdatesResponse.Failure
    def __init__(
        self,
        success: StreamSpaceUpdatesResponse.Success | _Mapping | None = ...,
        failure: StreamSpaceUpdatesResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
