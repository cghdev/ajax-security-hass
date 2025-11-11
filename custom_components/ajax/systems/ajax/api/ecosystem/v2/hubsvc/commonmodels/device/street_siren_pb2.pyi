from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    alarm_restriction_pb2 as _alarm_restriction_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    alarm_verification_pb2 as _alarm_verification_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    bracket_state_pb2 as _bracket_state_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_jeweller_part_pb2 as _common_jeweller_part_pb2,
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
    common_standard_compliance_part_pb2 as _common_standard_compliance_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    common_wings_part_pb2 as _common_wings_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_battery_pb2 as _device_battery_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_tamper_status_pb2 as _device_tamper_status_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_temperature_pb2 as _device_temperature_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    external_power_pb2 as _external_power_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    group_association_pb2 as _group_association_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    gyroscope_pb2 as _gyroscope_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    light_indication_area_part_pb2 as _light_indication_area_part_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    post_alarm_indication_pb2 as _post_alarm_indication_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    radio_interference_detection_part_pb2 as _radio_interference_detection_part_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class StreetSiren(_message.Message):
    __slots__ = (
        "alarm_restriction",
        "alarm_verification",
        "common_jeweller_part",
        "common_siren_part",
        "common_standard_compliance_part",
        "common_wings_part",
        "device_battery",
        "device_tamper_status",
        "device_temperature",
        "external_power",
        "group_association",
        "gyroscope",
        "post_alarm_indication_props",
    )
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    ALARM_RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_PROPS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMMON_STANDARD_COMPLIANCE_PART_FIELD_NUMBER: _ClassVar[int]
    GROUP_ASSOCIATION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_FIELD_NUMBER: _ClassVar[int]
    GYROSCOPE_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_siren_part: _common_siren_part_pb2.CommonSirenPart
    alarm_verification: _alarm_verification_pb2.AlarmVerification
    alarm_restriction: _alarm_restriction_pb2.AlarmRestriction
    post_alarm_indication_props: _post_alarm_indication_pb2.PostAlarmIndication
    device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
    device_temperature: _device_temperature_pb2.DeviceTemperature
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    common_standard_compliance_part: (
        _common_standard_compliance_part_pb2.CommonStandardCompliancePart
    )
    group_association: _group_association_pb2.GroupAssociation
    external_power: _external_power_pb2.ExternalPower
    gyroscope: _gyroscope_pb2.Gyroscope
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    def __init__(
        self,
        common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
        | _Mapping
        | None = ...,
        common_siren_part: _common_siren_part_pb2.CommonSirenPart
        | _Mapping
        | None = ...,
        alarm_verification: _alarm_verification_pb2.AlarmVerification
        | _Mapping
        | None = ...,
        alarm_restriction: _alarm_restriction_pb2.AlarmRestriction
        | _Mapping
        | None = ...,
        post_alarm_indication_props: _post_alarm_indication_pb2.PostAlarmIndication
        | _Mapping
        | None = ...,
        device_battery: _device_battery_pb2.DeviceBatteryWithoutCharging
        | _Mapping
        | None = ...,
        device_temperature: _device_temperature_pb2.DeviceTemperature
        | _Mapping
        | None = ...,
        device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
        | str
        | None = ...,
        common_standard_compliance_part: _common_standard_compliance_part_pb2.CommonStandardCompliancePart
        | _Mapping
        | None = ...,
        group_association: _group_association_pb2.GroupAssociation
        | _Mapping
        | None = ...,
        external_power: _external_power_pb2.ExternalPower | _Mapping | None = ...,
        gyroscope: _gyroscope_pb2.Gyroscope | _Mapping | None = ...,
        common_wings_part: _common_wings_part_pb2.CommonWingsPart
        | _Mapping
        | None = ...,
    ) -> None: ...

class StreetSirenPlusG3(_message.Message):
    __slots__ = (
        "alarm_restriction_part",
        "alarm_verification_part",
        "bracket_state_part",
        "common_jeweller_part",
        "common_siren_part",
        "common_siren_tamper_part",
        "common_sound_compliance_pattern_part",
        "common_standard_compliance_part",
        "common_wings_part",
        "device_battery_without_charging_part",
        "device_tamper_status",
        "device_temperature_part",
        "external_power_part",
        "group_association_part",
        "light_indication_area_part",
        "post_alarm_indication_part",
        "radio_interference_detection_part",
    )
    COMMON_JEWELLER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_VERIFICATION_PART_FIELD_NUMBER: _ClassVar[int]
    ALARM_RESTRICTION_PART_FIELD_NUMBER: _ClassVar[int]
    POST_ALARM_INDICATION_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BATTERY_WITHOUT_CHARGING_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TEMPERATURE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIREN_TAMPER_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_STANDARD_COMPLIANCE_PART_FIELD_NUMBER: _ClassVar[int]
    GROUP_ASSOCIATION_PART_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_PART_FIELD_NUMBER: _ClassVar[int]
    BRACKET_STATE_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_WINGS_PART_FIELD_NUMBER: _ClassVar[int]
    COMMON_SOUND_COMPLIANCE_PATTERN_PART_FIELD_NUMBER: _ClassVar[int]
    RADIO_INTERFERENCE_DETECTION_PART_FIELD_NUMBER: _ClassVar[int]
    LIGHT_INDICATION_AREA_PART_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TAMPER_STATUS_FIELD_NUMBER: _ClassVar[int]
    common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
    common_siren_part: _common_siren_part_pb2.CommonSirenPart
    alarm_verification_part: _alarm_verification_pb2.AlarmVerification
    alarm_restriction_part: _alarm_restriction_pb2.AlarmRestriction
    post_alarm_indication_part: _post_alarm_indication_pb2.PostAlarmIndication
    device_battery_without_charging_part: (
        _device_battery_pb2.DeviceBatteryWithoutCharging
    )
    device_temperature_part: _device_temperature_pb2.DeviceTemperature
    common_siren_tamper_part: _common_siren_tamper_part_pb2.CommonSirenTamperPart
    common_standard_compliance_part: (
        _common_standard_compliance_part_pb2.CommonStandardCompliancePart
    )
    group_association_part: _group_association_pb2.GroupAssociation
    external_power_part: _external_power_pb2.ExternalPower
    bracket_state_part: _bracket_state_pb2.BracketStatePart
    common_wings_part: _common_wings_part_pb2.CommonWingsPart
    common_sound_compliance_pattern_part: (
        _common_sound_compliance_pattern_part_pb2.CommonSoundCompliancePatternPart
    )
    radio_interference_detection_part: (
        _radio_interference_detection_part_pb2.RadioInterferenceDetectionPart
    )
    light_indication_area_part: _light_indication_area_part_pb2.LightIndicationAreaPart
    device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
    def __init__(
        self,
        common_jeweller_part: _common_jeweller_part_pb2.CommonJewellerPart
        | _Mapping
        | None = ...,
        common_siren_part: _common_siren_part_pb2.CommonSirenPart
        | _Mapping
        | None = ...,
        alarm_verification_part: _alarm_verification_pb2.AlarmVerification
        | _Mapping
        | None = ...,
        alarm_restriction_part: _alarm_restriction_pb2.AlarmRestriction
        | _Mapping
        | None = ...,
        post_alarm_indication_part: _post_alarm_indication_pb2.PostAlarmIndication
        | _Mapping
        | None = ...,
        device_battery_without_charging_part: _device_battery_pb2.DeviceBatteryWithoutCharging
        | _Mapping
        | None = ...,
        device_temperature_part: _device_temperature_pb2.DeviceTemperature
        | _Mapping
        | None = ...,
        common_siren_tamper_part: _common_siren_tamper_part_pb2.CommonSirenTamperPart
        | _Mapping
        | None = ...,
        common_standard_compliance_part: _common_standard_compliance_part_pb2.CommonStandardCompliancePart
        | _Mapping
        | None = ...,
        group_association_part: _group_association_pb2.GroupAssociation
        | _Mapping
        | None = ...,
        external_power_part: _external_power_pb2.ExternalPower | _Mapping | None = ...,
        bracket_state_part: _bracket_state_pb2.BracketStatePart | _Mapping | None = ...,
        common_wings_part: _common_wings_part_pb2.CommonWingsPart
        | _Mapping
        | None = ...,
        common_sound_compliance_pattern_part: _common_sound_compliance_pattern_part_pb2.CommonSoundCompliancePatternPart
        | _Mapping
        | None = ...,
        radio_interference_detection_part: _radio_interference_detection_part_pb2.RadioInterferenceDetectionPart
        | _Mapping
        | None = ...,
        light_indication_area_part: _light_indication_area_part_pb2.LightIndicationAreaPart
        | _Mapping
        | None = ...,
        device_tamper_status: _device_tamper_status_pb2.DeviceTamperStatus
        | str
        | None = ...,
    ) -> None: ...
