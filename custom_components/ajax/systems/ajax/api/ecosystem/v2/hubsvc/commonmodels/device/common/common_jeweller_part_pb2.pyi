from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    assigned_extender_pb2 as _assigned_extender_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    bypass_part_pb2 as _bypass_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    cms_device_index_pb2 as _cms_device_index_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_common_capabilities_pb2 as _device_common_capabilities_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_malfunctions_pb2 as _device_malfunctions_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_migration_status_pb2 as _device_migration_status_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_profile_pb2 as _device_profile_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_telemetry_pb2 as _device_telemetry_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_transmission_power_mode_part_pb2 as _device_transmission_power_mode_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_transmission_power_mode_pb2 as _device_transmission_power_mode_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    self_monitoring_part_pb2 as _self_monitoring_part_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class CommonJewellerPart(_message.Message):
    __slots__ = (
        "assigned_extender",
        "bypass_part",
        "cms_device_index",
        "device_common_capabilities",
        "device_malfunctions",
        "device_migration_status",
        "device_profile",
        "device_telemetry",
        "device_transmission_power_mode",
        "device_transmission_power_mode_part",
        "self_monitoring_part",
    )
    DEVICE_PROFILE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TELEMETRY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRANSMISSION_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_EXTENDER_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    BYPASS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MIGRATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_COMMON_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SELF_MONITORING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRANSMISSION_POWER_MODE_PART_FIELD_NUMBER: _ClassVar[int]
    device_profile: _device_profile_pb2.DeviceProfile
    device_telemetry: _device_telemetry_pb2.DeviceTelemetry
    device_transmission_power_mode: (
        _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
    )
    device_malfunctions: _device_malfunctions_pb2.DeviceMalfunctions
    assigned_extender: _assigned_extender_pb2.AssignedExtender
    cms_device_index: _cms_device_index_pb2.CmsDeviceIndex
    bypass_part: _bypass_part_pb2.BypassPart
    device_migration_status: _device_migration_status_pb2.DeviceMigrationStatus
    device_common_capabilities: _containers.RepeatedScalarFieldContainer[
        _device_common_capabilities_pb2.DeviceCommonCapability
    ]
    self_monitoring_part: _self_monitoring_part_pb2.SelfMonitoringPart
    device_transmission_power_mode_part: (
        _device_transmission_power_mode_part_pb2.DeviceTransmissionPowerModePart
    )
    def __init__(
        self,
        device_profile: _device_profile_pb2.DeviceProfile | _Mapping | None = ...,
        device_telemetry: _device_telemetry_pb2.DeviceTelemetry | _Mapping | None = ...,
        device_transmission_power_mode: _device_transmission_power_mode_pb2.DeviceTransmissionPowerMode
        | str
        | None = ...,
        device_malfunctions: _device_malfunctions_pb2.DeviceMalfunctions
        | _Mapping
        | None = ...,
        assigned_extender: _assigned_extender_pb2.AssignedExtender
        | _Mapping
        | None = ...,
        cms_device_index: _cms_device_index_pb2.CmsDeviceIndex | _Mapping | None = ...,
        bypass_part: _bypass_part_pb2.BypassPart | _Mapping | None = ...,
        device_migration_status: _device_migration_status_pb2.DeviceMigrationStatus
        | str
        | None = ...,
        device_common_capabilities: _Iterable[
            _device_common_capabilities_pb2.DeviceCommonCapability | str
        ]
        | None = ...,
        self_monitoring_part: _self_monitoring_part_pb2.SelfMonitoringPart
        | _Mapping
        | None = ...,
        device_transmission_power_mode_part: _device_transmission_power_mode_part_pb2.DeviceTransmissionPowerModePart
        | _Mapping
        | None = ...,
    ) -> None: ...
