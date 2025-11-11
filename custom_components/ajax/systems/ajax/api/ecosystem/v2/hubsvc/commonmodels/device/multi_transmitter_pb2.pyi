from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    arming_restrictions_part_pb2 as _arming_restrictions_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_device_notifications_part_pb2 as _common_device_notifications_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_jeweller_part_pb2 as _common_jeweller_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_wings_part_pb2 as _common_wings_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    detectors_power_line_part_pb2 as _detectors_power_line_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_battery_pb2 as _device_battery_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_siren_triggers_pb2 as _device_siren_triggers_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_tamper_status_pb2 as _device_tamper_status_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    external_power_pb2 as _external_power_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    external_tamper_part_pb2 as _external_tamper_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    led_indication_part_pb2 as _led_indication_part_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class MultiTransmitterG3(_message.Message):
    __slots__ = (
        "arming_restrictions_part",
        "common_jeweller_part",
        "common_wings_part",
        "detectors_power_line_part",
        "device_battery",
        "device_notifications_part",
        "device_tamper_status",
        "external_power",
        "external_tamper",
        "led_indication_part",
        "siren_triggers",
    )
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_TAMPER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_FIELD_NUMBER: _ClassVar[int]
    DETECTORS_POWER_LINE_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NOTIFICATIONS_PART_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    ARMING_RESTRICTIONS_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    device_battery: _device_battery_pb2.DeviceBattery
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    external_tamper: _external_tamper_part_pb2.ExternalTamperPart
    external_power: _external_power_pb2.ExternalPower
    detectors_power_line_part: _detectors_power_line_part_pb2.DetectorsPowerLinePart
    device_notifications_part: (
        _common_device_notifications_part_pb2.CommonDeviceNotificationsPart
    )
    led_indication_part: _led_indication_part_pb2.LedIndicationPart
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    arming_restrictions_part: _arming_restrictions_part_pb2.ArmingRestrictionsPart
    def __init__(
        self,
        common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
        | _Mapping
        | None = ...,
        common_wings_part: _common_wings_part_pb2.CommonWingsPart
        | _Mapping
        | None = ...,
        device_battery: _device_battery_pb2.DeviceBattery | _Mapping | None = ...,
        device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
        | str
        | None = ...,
        external_tamper: _external_tamper_part_pb2.ExternalTamperPart
        | _Mapping
        | None = ...,
        external_power: _external_power_pb2.ExternalPower | _Mapping | None = ...,
        detectors_power_line_part: _detectors_power_line_part_pb2.DetectorsPowerLinePart
        | _Mapping
        | None = ...,
        device_notifications_part: _common_device_notifications_part_pb2.CommonDeviceNotificationsPart
        | _Mapping
        | None = ...,
        led_indication_part: _led_indication_part_pb2.LedIndicationPart
        | _Mapping
        | None = ...,
        siren_triggers: _device_siren_triggers_pb2.SirenTriggers
        | _Mapping
        | None = ...,
        arming_restrictions_part: _arming_restrictions_part_pb2.ArmingRestrictionsPart
        | _Mapping
        | None = ...,
    ) -> None: ...
