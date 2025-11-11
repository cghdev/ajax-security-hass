from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.accounting import (
    extra_services_availability_status_pb2 as _extra_services_availability_status_pb2,
)
from systems.ajax.api.mobile.v2.common.accounting import (
    service_deactivation_pending_status_pb2 as _service_deactivation_pending_status_pb2,
)
from systems.ajax.api.mobile.v2.common.space import (
    current_member_pb2 as _current_member_pb2,
)
from systems.ajax.api.mobile.v2.common.space import (
    space_address_pb2 as _space_address_pb2,
)
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
    space_cobranded_company_pb2 as _space_cobranded_company_pb2,
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
    space_security_pb2 as _space_security_pb2,
)
from systems.ajax.api.mobile.v2.common.space.stream import (
    external_stream_control_pb2 as _external_stream_control_pb2,
)
from systems.ajax.api.mobile.v2.common.time import time_zone_pb2 as _time_zone_pb2
from systems.ajax.api.mobile.v2.common.video import video_wall_pb2 as _video_wall_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = (
        "address",
        "after_alarm_video_access_disabled",
        "current_member",
        "devices",
        "extra_services_availability_status",
        "extra_services_availability_status_v2",
        "id",
        "installation_companies",
        "is_oversized",
        "members",
        "monitoring_companies",
        "pending_members",
        "privacy_overrides",
        "profile",
        "rooms",
        "security",
        "service_deactivation_pending_status",
        "space_capabilities",
        "space_cobranded_companies",
        "stream_controls",
        "time_zone",
        "total_notification_unread_counter",
        "video_wall",
    )
    ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_MEMBER_FIELD_NUMBER: _ClassVar[int]
    TOTAL_NOTIFICATION_UNREAD_COUNTER_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    DEVICES_FIELD_NUMBER: _ClassVar[int]
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    IS_OVERSIZED_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    MONITORING_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    SPACE_COBRANDED_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    PENDING_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_WALL_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DEACTIVATION_PENDING_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_SERVICES_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTRA_SERVICES_AVAILABILITY_STATUS_V2_FIELD_NUMBER: _ClassVar[int]
    AFTER_ALARM_VIDEO_ACCESS_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SPACE_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    STREAM_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    id: str
    current_member: _current_member_pb2.CurrentMember
    total_notification_unread_counter: int
    members: _containers.RepeatedCompositeFieldContainer[_space_member_pb2.SpaceMember]
    security: _space_security_pb2.SpaceSecurity
    devices: _containers.RepeatedCompositeFieldContainer[
        _standalone_device_pb2.StandaloneDevice
    ]
    profile: _space_profile_pb2.SpaceProfile
    rooms: _containers.RepeatedCompositeFieldContainer[_room_pb2.Room]
    is_oversized: bool
    installation_companies: _containers.RepeatedCompositeFieldContainer[
        _space_installation_company_pb2.SpaceInstallationCompany
    ]
    monitoring_companies: _containers.RepeatedCompositeFieldContainer[
        _space_monitoring_company_pb2.SpaceMonitoringCompany
    ]
    space_cobranded_companies: _containers.RepeatedCompositeFieldContainer[
        _space_cobranded_company_pb2.SpaceCobrandedCompany
    ]
    privacy_overrides: _containers.RepeatedCompositeFieldContainer[
        _privacy_override_pb2.PrivacyOverride
    ]
    pending_members: _containers.RepeatedCompositeFieldContainer[
        _pending_member_pb2.PendingMember
    ]
    time_zone: _time_zone_pb2.TimeZone
    video_wall: _video_wall_pb2.VideoWall
    address: _space_address_pb2.SpaceAddress
    service_deactivation_pending_status: (
        _service_deactivation_pending_status_pb2.ServiceDeactivationPendingStatus
    )
    extra_services_availability_status: (
        _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
    )
    extra_services_availability_status_v2: (
        _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
    )
    after_alarm_video_access_disabled: bool
    space_capabilities: _space_capabilities_pb2.SpaceCapabilities
    stream_controls: _containers.RepeatedCompositeFieldContainer[
        _external_stream_control_pb2.ExternalStreamControl
    ]
    def __init__(
        self,
        id: str | None = ...,
        current_member: _current_member_pb2.CurrentMember | _Mapping | None = ...,
        total_notification_unread_counter: int | None = ...,
        members: _Iterable[_space_member_pb2.SpaceMember | _Mapping] | None = ...,
        security: _space_security_pb2.SpaceSecurity | _Mapping | None = ...,
        devices: _Iterable[_standalone_device_pb2.StandaloneDevice | _Mapping]
        | None = ...,
        profile: _space_profile_pb2.SpaceProfile | _Mapping | None = ...,
        rooms: _Iterable[_room_pb2.Room | _Mapping] | None = ...,
        is_oversized: bool = ...,
        installation_companies: _Iterable[
            _space_installation_company_pb2.SpaceInstallationCompany | _Mapping
        ]
        | None = ...,
        monitoring_companies: _Iterable[
            _space_monitoring_company_pb2.SpaceMonitoringCompany | _Mapping
        ]
        | None = ...,
        space_cobranded_companies: _Iterable[
            _space_cobranded_company_pb2.SpaceCobrandedCompany | _Mapping
        ]
        | None = ...,
        privacy_overrides: _Iterable[_privacy_override_pb2.PrivacyOverride | _Mapping]
        | None = ...,
        pending_members: _Iterable[_pending_member_pb2.PendingMember | _Mapping]
        | None = ...,
        time_zone: _time_zone_pb2.TimeZone | _Mapping | None = ...,
        video_wall: _video_wall_pb2.VideoWall | _Mapping | None = ...,
        address: _space_address_pb2.SpaceAddress | _Mapping | None = ...,
        service_deactivation_pending_status: _service_deactivation_pending_status_pb2.ServiceDeactivationPendingStatus
        | str
        | None = ...,
        extra_services_availability_status: _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
        | str
        | None = ...,
        extra_services_availability_status_v2: _extra_services_availability_status_pb2.ExtraServicesAvailabilityStatus
        | str
        | None = ...,
        after_alarm_video_access_disabled: bool = ...,
        space_capabilities: _space_capabilities_pb2.SpaceCapabilities
        | _Mapping
        | None = ...,
        stream_controls: _Iterable[
            _external_stream_control_pb2.ExternalStreamControl | _Mapping
        ]
        | None = ...,
    ) -> None: ...
