from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.commonmodels.device.common import (
    common_arming_part_pb2 as _common_arming_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    alarm_restriction_pb2 as _alarm_restriction_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    alarm_verification_pb2 as _alarm_verification_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    arming_restrictions_part_pb2 as _arming_restrictions_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_beep_part_pb2 as _common_beep_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_device_notifications_part_pb2 as _common_device_notifications_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_masking_part_pb2 as _common_masking_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_siren_part_pb2 as _common_siren_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_siren_tamper_part_pb2 as _common_siren_tamper_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_sound_compliance_pattern_part_pb2 as _common_sound_compliance_pattern_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    detection_mode_part_pb2 as _detection_mode_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_battery_pb2 as _device_battery_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_profile_pb2 as _device_profile_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_siren_triggers_pb2 as _device_siren_triggers_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_transmission_power_mode_part_pb2 as _device_transmission_power_mode_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    group_association_pb2 as _group_association_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    gyroscope_pb2 as _gyroscope_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    led_indication_part_pb2 as _led_indication_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    light_indication_area_part_pb2 as _light_indication_area_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    light_indication_pb2 as _light_indication_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    masking_sensitivity_pb2 as _masking_sensitivity_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    motion_detection_part_pb2 as _motion_detection_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    post_alarm_indication_pb2 as _post_alarm_indication_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    radio_interference_detection_part_pb2 as _radio_interference_detection_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    self_monitoring_part_pb2 as _self_monitoring_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common.photo import (
    photo_part_pb2 as _photo_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common.photo import (
    take_photo_part_pb2 as _take_photo_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.smartlock import (
    smart_lock_part_pb2 as _smart_lock_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.smartlock import (
    smart_lock_yale_part_pb2 as _smart_lock_yale_part_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Update(_message.Message):
    __slots__ = (
        "alarm_restriction_settings",
        "alarm_verification_settings",
        "arming_restrictions_part_settings",
        "common_arming_part_settings",
        "common_beep_part_settings",
        "common_masking_part_settings",
        "common_siren_tamper_part_settings",
        "common_sound_compliance_pattern_part_settings",
        "detection_mode_part_settings",
        "device_battery_settings",
        "device_notifications_part_settings",
        "device_profile_settings",
        "device_transmission_power_mode_settings",
        "group_association_settings",
        "gyroscope_sensor_settings",
        "led_indication_part_settings",
        "light_indication_area_part_settings",
        "light_indication_settings",
        "masking_sensitivity_settings",
        "motion_detection_part_settings",
        "photo_part_settings",
        "post_alarm_indication_settings",
        "radio_interference_detection_settings",
        "self_monitoring_part_settings",
        "siren_settings",
        "siren_trigger_settings",
        "smart_lock_part_settings",
        "smart_lock_yale_part_settings",
        "take_photo_part_settings",
    )
    DEVICE_PROFILE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LIGHT_INDICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_BEEP_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALARM_RESTRICTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SIREN_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GROUP_ASSOCIATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_SENSOR_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SELF_MONITORING_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LIGHT_INDICATION_AREA_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_SOUND_COMPLIANCE_PATTERN_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RADIO_INTERFERENCE_DETECTION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_TAMPER_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_MASKING_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DETECTION_MODE_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NOTIFICATIONS_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    LED_INDICATION_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    COMMON_ARMING_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTION_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_YALE_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSITIVITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TAKE_PHOTO_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ARMING_RESTRICTIONS_PART_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRANSMISSION_POWER_MODE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    device_profile_settings: _device_profile_pb2.DeviceProfile.DeviceProfileSettings
    light_indication_settings: (
        _light_indication_pb2.LightIndication.LightIndicationSettings
    )
    common_beep_part_settings: (
        _common_beep_part_pb2.CommonBeepPart.CommonBeepPartSettings
    )
    alarm_restriction_settings: (
        _alarm_restriction_pb2.AlarmRestriction.AlarmRestrictionSettings
    )
    alarm_verification_settings: (
        _alarm_verification_pb2.AlarmVerification.AlarmVerificationSettings
    )
    post_alarm_indication_settings: (
        _post_alarm_indication_pb2.PostAlarmIndication.PostAlarmIndicationSettings
    )
    siren_settings: _common_siren_part_pb2.CommonSirenPart.SirenSettings
    group_association_settings: (
        _group_association_pb2.GroupAssociation.GroupAssociationSettings
    )
    gyroscope_sensor_settings: _gyroscope_pb2.Gyroscope.GyroscopeSensorSettings
    self_monitoring_part_settings: (
        _self_monitoring_part_pb2.SelfMonitoringPart.SelfMonitoringPartSettings
    )
    light_indication_area_part_settings: _light_indication_area_part_pb2.LightIndicationAreaPart.LightIndicationAreaPartSettings
    common_sound_compliance_pattern_part_settings: _common_sound_compliance_pattern_part_pb2.CommonSoundCompliancePatternPart.CommonSoundCompliancePatternPartSettings
    radio_interference_detection_settings: _radio_interference_detection_part_pb2.RadioInterferenceDetectionPart.RadioInterferenceDetectionSettings
    common_siren_tamper_part_settings: _common_siren_tamper_part_pb2.CommonSirenTamperPart.CommonSirenTamperPartSettings
    common_masking_part_settings: (
        _common_masking_part_pb2.CommonMaskingPart.CommonMaskingPartSettings
    )
    detection_mode_part_settings: (
        _detection_mode_part_pb2.DetectionModePart.DetectionModePartSettings
    )
    device_notifications_part_settings: _common_device_notifications_part_pb2.CommonDeviceNotificationsPart.DeviceNotificationsPartSettings
    led_indication_part_settings: (
        _led_indication_part_pb2.LedIndicationPart.LedIndicationPartSettings
    )
    siren_trigger_settings: (
        _device_siren_triggers_pb2.SirenTriggers.SirenTriggerSettings
    )
    common_arming_part_settings: (
        _common_arming_part_pb2.CommonArmingPart.CommonArmingPartSettings
    )
    motion_detection_part_settings: (
        _motion_detection_part_pb2.MotionDetectionPart.MotionDetectionPartSettings
    )
    smart_lock_part_settings: _smart_lock_part_pb2.SmartLockPart.SmartLockPartSettings
    smart_lock_yale_part_settings: (
        _smart_lock_yale_part_pb2.SmartLockYalePart.SmartLockYalePartSettings
    )
    masking_sensitivity_settings: (
        _masking_sensitivity_pb2.MaskingSensitivity.MaskingSensitivitySettings
    )
    photo_part_settings: _photo_part_pb2.PhotoPart.PhotoPartSettings
    take_photo_part_settings: _take_photo_part_pb2.TakePhotoPart.TakePhotoPartSettings
    arming_restrictions_part_settings: _arming_restrictions_part_pb2.ArmingRestrictionsPart.ArmingRestrictionsPartSettings
    device_battery_settings: _device_battery_pb2.DeviceBattery.DeviceBatterySettings
    device_transmission_power_mode_settings: _device_transmission_power_mode_part_pb2.DeviceTransmissionPowerModePart.DeviceTransmissionPowerModePartSettings
    def __init__(
        self,
        device_profile_settings: _device_profile_pb2.DeviceProfile.DeviceProfileSettings
        | _Mapping
        | None = ...,
        light_indication_settings: _light_indication_pb2.LightIndication.LightIndicationSettings
        | _Mapping
        | None = ...,
        common_beep_part_settings: _common_beep_part_pb2.CommonBeepPart.CommonBeepPartSettings
        | _Mapping
        | None = ...,
        alarm_restriction_settings: _alarm_restriction_pb2.AlarmRestriction.AlarmRestrictionSettings
        | _Mapping
        | None = ...,
        alarm_verification_settings: _alarm_verification_pb2.AlarmVerification.AlarmVerificationSettings
        | _Mapping
        | None = ...,
        post_alarm_indication_settings: _post_alarm_indication_pb2.PostAlarmIndication.PostAlarmIndicationSettings
        | _Mapping
        | None = ...,
        siren_settings: _common_siren_part_pb2.CommonSirenPart.SirenSettings
        | _Mapping
        | None = ...,
        group_association_settings: _group_association_pb2.GroupAssociation.GroupAssociationSettings
        | _Mapping
        | None = ...,
        gyroscope_sensor_settings: _gyroscope_pb2.Gyroscope.GyroscopeSensorSettings
        | _Mapping
        | None = ...,
        self_monitoring_part_settings: _self_monitoring_part_pb2.SelfMonitoringPart.SelfMonitoringPartSettings
        | _Mapping
        | None = ...,
        light_indication_area_part_settings: _light_indication_area_part_pb2.LightIndicationAreaPart.LightIndicationAreaPartSettings
        | _Mapping
        | None = ...,
        common_sound_compliance_pattern_part_settings: _common_sound_compliance_pattern_part_pb2.CommonSoundCompliancePatternPart.CommonSoundCompliancePatternPartSettings
        | _Mapping
        | None = ...,
        radio_interference_detection_settings: _radio_interference_detection_part_pb2.RadioInterferenceDetectionPart.RadioInterferenceDetectionSettings
        | _Mapping
        | None = ...,
        common_siren_tamper_part_settings: _common_siren_tamper_part_pb2.CommonSirenTamperPart.CommonSirenTamperPartSettings
        | _Mapping
        | None = ...,
        common_masking_part_settings: _common_masking_part_pb2.CommonMaskingPart.CommonMaskingPartSettings
        | _Mapping
        | None = ...,
        detection_mode_part_settings: _detection_mode_part_pb2.DetectionModePart.DetectionModePartSettings
        | _Mapping
        | None = ...,
        device_notifications_part_settings: _common_device_notifications_part_pb2.CommonDeviceNotificationsPart.DeviceNotificationsPartSettings
        | _Mapping
        | None = ...,
        led_indication_part_settings: _led_indication_part_pb2.LedIndicationPart.LedIndicationPartSettings
        | _Mapping
        | None = ...,
        siren_trigger_settings: _device_siren_triggers_pb2.SirenTriggers.SirenTriggerSettings
        | _Mapping
        | None = ...,
        common_arming_part_settings: _common_arming_part_pb2.CommonArmingPart.CommonArmingPartSettings
        | _Mapping
        | None = ...,
        motion_detection_part_settings: _motion_detection_part_pb2.MotionDetectionPart.MotionDetectionPartSettings
        | _Mapping
        | None = ...,
        smart_lock_part_settings: _smart_lock_part_pb2.SmartLockPart.SmartLockPartSettings
        | _Mapping
        | None = ...,
        smart_lock_yale_part_settings: _smart_lock_yale_part_pb2.SmartLockYalePart.SmartLockYalePartSettings
        | _Mapping
        | None = ...,
        masking_sensitivity_settings: _masking_sensitivity_pb2.MaskingSensitivity.MaskingSensitivitySettings
        | _Mapping
        | None = ...,
        photo_part_settings: _photo_part_pb2.PhotoPart.PhotoPartSettings
        | _Mapping
        | None = ...,
        take_photo_part_settings: _take_photo_part_pb2.TakePhotoPart.TakePhotoPartSettings
        | _Mapping
        | None = ...,
        arming_restrictions_part_settings: _arming_restrictions_part_pb2.ArmingRestrictionsPart.ArmingRestrictionsPartSettings
        | _Mapping
        | None = ...,
        device_battery_settings: _device_battery_pb2.DeviceBattery.DeviceBatterySettings
        | _Mapping
        | None = ...,
        device_transmission_power_mode_settings: _device_transmission_power_mode_part_pb2.DeviceTransmissionPowerModePart.DeviceTransmissionPowerModePartSettings
        | _Mapping
        | None = ...,
    ) -> None: ...
