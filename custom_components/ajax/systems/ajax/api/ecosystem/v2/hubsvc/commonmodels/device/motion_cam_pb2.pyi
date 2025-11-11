from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import (
    common_arming_part_pb2 as _common_arming_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_device_notifications_part_pb2 as _common_device_notifications_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_jeweller_part_pb2 as _common_jeweller_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_masking_part_pb2 as _common_masking_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_wings_part_pb2 as _common_wings_part_pb2,
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
    device_temperature_pb2 as _device_temperature_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_warnings_pb2 as _device_warnings_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    external_power_pb2 as _external_power_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    gyroscope_pb2 as _gyroscope_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    led_indication_part_pb2 as _led_indication_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    motion_detection_part_pb2 as _motion_detection_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common.photo import (
    photo_access_part_pb2 as _photo_access_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common.photo import (
    photo_part_pb2 as _photo_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common.photo import (
    take_photo_part_pb2 as _take_photo_part_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class MotionCamG3(_message.Message):
    __slots__ = (
        "common_arming_part",
        "common_jeweller_part",
        "common_masking_part",
        "common_wings_part",
        "device_battery_without_charging_part",
        "device_tamper_status",
        "device_temperature",
        "led_indication_part",
        "motion_detection_part",
        "photo_access_part",
        "photo_part",
        "siren_triggers",
        "take_photo_part",
    )
    COMMON_ARMING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_WITHOUT_CHARGING_PART_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_MASKING_PART_FIELD_NUMBER: _ClassVar[int]
    PHOTO_PART_FIELD_NUMBER: _ClassVar[int]
    TAKE_PHOTO_PART_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ACCESS_PART_FIELD_NUMBER: _ClassVar[int]
    common_arming_part: _common_arming_part_pb2.CommonArmingPart
    device_temperature: _device_temperature_pb2.DeviceTemperature
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    led_indication_part: _led_indication_part_pb2.LedIndicationPart
    device_battery_without_charging_part: (
        _device_battery_pb2.DeviceBatteryWithoutCharging
    )
    motion_detection_part: _motion_detection_part_pb2.MotionDetectionPart
    common_masking_part: _common_masking_part_pb2.CommonMaskingPart
    photo_part: _photo_part_pb2.PhotoPart
    take_photo_part: _take_photo_part_pb2.TakePhotoPart
    photo_access_part: _photo_access_part_pb2.PhotoAccessPart
    def __init__(
        self,
        common_arming_part: _common_arming_part_pb2.CommonArmingPart
        | _Mapping
        | None = ...,
        device_temperature: _device_temperature_pb2.DeviceTemperature
        | _Mapping
        | None = ...,
        device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
        | str
        | None = ...,
        siren_triggers: _device_siren_triggers_pb2.SirenTriggers
        | _Mapping
        | None = ...,
        common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
        | _Mapping
        | None = ...,
        common_wings_part: _common_wings_part_pb2.CommonWingsPart
        | _Mapping
        | None = ...,
        led_indication_part: _led_indication_part_pb2.LedIndicationPart
        | _Mapping
        | None = ...,
        device_battery_without_charging_part: _device_battery_pb2.DeviceBatteryWithoutCharging
        | _Mapping
        | None = ...,
        motion_detection_part: _motion_detection_part_pb2.MotionDetectionPart
        | _Mapping
        | None = ...,
        common_masking_part: _common_masking_part_pb2.CommonMaskingPart
        | _Mapping
        | None = ...,
        photo_part: _photo_part_pb2.PhotoPart | _Mapping | None = ...,
        take_photo_part: _take_photo_part_pb2.TakePhotoPart | _Mapping | None = ...,
        photo_access_part: _photo_access_part_pb2.PhotoAccessPart
        | _Mapping
        | None = ...,
    ) -> None: ...

class CurtainCamOutdoorHmPhod(_message.Message):
    __slots__ = (
        "common_arming_part",
        "common_jeweller_part",
        "common_masking_part",
        "common_wings_part",
        "device_battery_without_charging_part",
        "device_notifications_part",
        "device_tamper_status",
        "device_temperature",
        "device_warnings",
        "external_power",
        "gyroscope",
        "led_indication_part",
        "motion_detection_part",
        "photo_access_part",
        "photo_part",
        "siren_triggers",
        "take_photo_part",
    )
    COMMON_ARMING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_WITHOUT_CHARGING_PART_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_WARNINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_MASKING_PART_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_FIELD_NUMBER: _ClassVar[int]
    PHOTO_PART_FIELD_NUMBER: _ClassVar[int]
    TAKE_PHOTO_PART_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ACCESS_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NOTIFICATIONS_PART_FIELD_NUMBER: _ClassVar[int]
    common_arming_part: _common_arming_part_pb2.CommonArmingPart
    device_temperature: _device_temperature_pb2.DeviceTemperature
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    siren_triggers: _device_siren_triggers_pb2.SirenTriggers
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    led_indication_part: _led_indication_part_pb2.LedIndicationPart
    device_battery_without_charging_part: (
        _device_battery_pb2.DeviceBatteryWithoutCharging
    )
    motion_detection_part: _motion_detection_part_pb2.MotionDetectionPart
    device_warnings: _device_warnings_pb2.DeviceWarnings
    common_masking_part: _common_masking_part_pb2.CommonMaskingPart
    external_power: _external_power_pb2.ExternalPower
    gyroscope: _gyroscope_pb2.Gyroscope
    photo_part: _photo_part_pb2.PhotoPart
    take_photo_part: _take_photo_part_pb2.TakePhotoPart
    photo_access_part: _photo_access_part_pb2.PhotoAccessPart
    device_notifications_part: (
        _common_device_notifications_part_pb2.CommonDeviceNotificationsPart
    )
    def __init__(
        self,
        common_arming_part: _common_arming_part_pb2.CommonArmingPart
        | _Mapping
        | None = ...,
        device_temperature: _device_temperature_pb2.DeviceTemperature
        | _Mapping
        | None = ...,
        device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
        | str
        | None = ...,
        siren_triggers: _device_siren_triggers_pb2.SirenTriggers
        | _Mapping
        | None = ...,
        common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
        | _Mapping
        | None = ...,
        common_wings_part: _common_wings_part_pb2.CommonWingsPart
        | _Mapping
        | None = ...,
        led_indication_part: _led_indication_part_pb2.LedIndicationPart
        | _Mapping
        | None = ...,
        device_battery_without_charging_part: _device_battery_pb2.DeviceBatteryWithoutCharging
        | _Mapping
        | None = ...,
        motion_detection_part: _motion_detection_part_pb2.MotionDetectionPart
        | _Mapping
        | None = ...,
        device_warnings: _device_warnings_pb2.DeviceWarnings | _Mapping | None = ...,
        common_masking_part: _common_masking_part_pb2.CommonMaskingPart
        | _Mapping
        | None = ...,
        external_power: _external_power_pb2.ExternalPower | _Mapping | None = ...,
        gyroscope: _gyroscope_pb2.Gyroscope | _Mapping | None = ...,
        photo_part: _photo_part_pb2.PhotoPart | _Mapping | None = ...,
        take_photo_part: _take_photo_part_pb2.TakePhotoPart | _Mapping | None = ...,
        photo_access_part: _photo_access_part_pb2.PhotoAccessPart
        | _Mapping
        | None = ...,
        device_notifications_part: _common_device_notifications_part_pb2.CommonDeviceNotificationsPart
        | _Mapping
        | None = ...,
    ) -> None: ...
