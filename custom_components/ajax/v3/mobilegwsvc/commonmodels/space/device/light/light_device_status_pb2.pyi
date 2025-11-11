from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device.common import (
    device_signal_level_pb2 as _device_signal_level_pb2,
)
from systems.ajax.api.mobile.v2.common.space.smartlock import (
    smart_lock_pb2 as _smart_lock_pb2,
)
from v3.mobilegwsvc.commonmodels.hub.device.common import (
    sim_card_status_pb2 as _sim_card_status_pb2,
)
from v3.mobilegwsvc.commonmodels.space.device.light import (
    life_quality_status_pb2 as _life_quality_status_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class LightDeviceStatus(_message.Message):
    __slots__ = (
        "access_card_disabled",
        "active_subscription",
        "always_active",
        "annunciation_test_active",
        "anti_masking_alert",
        "arc_reporting_disabled",
        "arc_spark_detected",
        "armed_in_night_mode",
        "battery",
        "ble",
        "bukhoor",
        "camera_view",
        "case_drilling_detected",
        "chimes_enabled",
        "co_level_detected",
        "contact_hang",
        "current_short_circuit",
        "delay_when_leaving",
        "device_firmware_status",
        "device_installation_warning",
        "door_need_anti_masking",
        "door_opened",
        "en54_disablement",
        "en54_fault",
        "en54_fire_buzzer_status",
        "en54_vad_status",
        "end_of_service_life",
        "external_contact_alert",
        "external_contact_broken",
        "fire_alarm_fp",
        "fire_buzzer_active",
        "gsm_status",
        "high_current_protection",
        "high_diff_temperature_detected",
        "high_frame_interconnect",
        "high_temperature_detected",
        "high_voltage",
        "interconnect",
        "interference_detected",
        "leak_detected",
        "lid_opened",
        "life_quality",
        "light_switch_through_pass",
        "line_supply_high_temperature",
        "low_voltage",
        "malfunction",
        "migration_in_process",
        "monitoring",
        "motion_detected",
        "nfc",
        "one_time_deactivation",
        "one_time_deactivation_tamper",
        "one_time_deactivation_whole",
        "onvif_user_auth_enabled",
        "pd_compliance_warning",
        "power_line_low",
        "power_management",
        "privacy",
        "real_active",
        "relay_stuck",
        "rex_connected",
        "roller_shutter",
        "sia_compliance_warning",
        "signal_strength",
        "sim_status",
        "smart_bracket_unlocked",
        "smart_lock",
        "smoke_detected",
        "someone_can_make_photo",
        "someone_has_camera_stream_access",
        "standard_compliance_warning",
        "storage_device",
        "switch_alarm_pressed",
        "temperature",
        "temporary_deactivation",
        "temporary_deactivation_alarms",
        "temporary_deactivation_tamper",
        "temporary_deactivation_timer",
        "temporary_deactivation_whole",
        "transmitter_status",
        "ul_not_compliant",
        "walk_test_status",
        "water_stop_prevention_warning",
        "water_stop_valve_stuck",
        "wifi_signal_level_status",
        "wire_input_status",
    )
    class CustomAlarmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CUSTOM_ALARM_TYPE_UNSPECIFIED: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_INTRUSION: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_FIRE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_MEDICAL: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_PANIC: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_GAS: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_TAMPER: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_MALFUNCTION: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_LEAK: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_SERVICE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_KEY_ARM: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_GLASS_BREAK: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_HIGH_TEMPERATURE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_LOW_TEMPERATURE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_MASKING: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_DURESS_CODE: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_VIBRATION: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_BLOCKING_ELEMENT: _ClassVar[LightDeviceStatus.CustomAlarmType]
        CUSTOM_ALARM_TYPE_BOLT_CONTACT: _ClassVar[LightDeviceStatus.CustomAlarmType]

    CUSTOM_ALARM_TYPE_UNSPECIFIED: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_INTRUSION: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_FIRE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_MEDICAL: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_PANIC: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_GAS: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_TAMPER: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_MALFUNCTION: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_LEAK: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_SERVICE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_KEY_ARM: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_GLASS_BREAK: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_HIGH_TEMPERATURE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_LOW_TEMPERATURE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_MASKING: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_DURESS_CODE: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_VIBRATION: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_BLOCKING_ELEMENT: LightDeviceStatus.CustomAlarmType
    CUSTOM_ALARM_TYPE_BOLT_CONTACT: LightDeviceStatus.CustomAlarmType
    class WifiSignalLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WIFI_SIGNAL_LEVEL_UNSPECIFIED: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_NO_SIGNAL: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_WEAK: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_NORMAL: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_STRONG: _ClassVar[LightDeviceStatus.WifiSignalLevel]
        WIFI_SIGNAL_LEVEL_DISCONNECTED: _ClassVar[LightDeviceStatus.WifiSignalLevel]

    WIFI_SIGNAL_LEVEL_UNSPECIFIED: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_NO_SIGNAL: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_WEAK: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_NORMAL: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_STRONG: LightDeviceStatus.WifiSignalLevel
    WIFI_SIGNAL_LEVEL_DISCONNECTED: LightDeviceStatus.WifiSignalLevel
    class StorageDevice(_message.Message):
        __slots__ = ("storage_device_status", "storage_device_type")
        class StorageDeviceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STORAGE_DEVICE_STATUS_UNSPECIFIED: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceStatus
            ]
            STORAGE_DEVICE_STATUS_OK: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceStatus
            ]
            STORAGE_DEVICE_STATUS_WARNING: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceStatus
            ]
            STORAGE_DEVICE_STATUS_ERROR: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceStatus
            ]
            STORAGE_DEVICE_STATUS_UNAVAILABLE: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceStatus
            ]

        STORAGE_DEVICE_STATUS_UNSPECIFIED: (
            LightDeviceStatus.StorageDevice.StorageDeviceStatus
        )
        STORAGE_DEVICE_STATUS_OK: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        STORAGE_DEVICE_STATUS_WARNING: (
            LightDeviceStatus.StorageDevice.StorageDeviceStatus
        )
        STORAGE_DEVICE_STATUS_ERROR: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        STORAGE_DEVICE_STATUS_UNAVAILABLE: (
            LightDeviceStatus.StorageDevice.StorageDeviceStatus
        )
        class StorageDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STORAGE_DEVICE_TYPE_UNSPECIFIED: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceType
            ]
            STORAGE_DEVICE_TYPE_SD_CARD: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceType
            ]
            STORAGE_DEVICE_TYPE_HARD_DRIVE: _ClassVar[
                LightDeviceStatus.StorageDevice.StorageDeviceType
            ]

        STORAGE_DEVICE_TYPE_UNSPECIFIED: (
            LightDeviceStatus.StorageDevice.StorageDeviceType
        )
        STORAGE_DEVICE_TYPE_SD_CARD: LightDeviceStatus.StorageDevice.StorageDeviceType
        STORAGE_DEVICE_TYPE_HARD_DRIVE: (
            LightDeviceStatus.StorageDevice.StorageDeviceType
        )
        STORAGE_DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        STORAGE_DEVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
        storage_device_type: LightDeviceStatus.StorageDevice.StorageDeviceType
        storage_device_status: LightDeviceStatus.StorageDevice.StorageDeviceStatus
        def __init__(
            self,
            storage_device_type: LightDeviceStatus.StorageDevice.StorageDeviceType
            | str
            | None = ...,
            storage_device_status: LightDeviceStatus.StorageDevice.StorageDeviceStatus
            | str
            | None = ...,
        ) -> None: ...

    class Simple(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class SimStatus(_message.Message):
        __slots__ = ("sim_card_status",)
        SIM_CARD_STATUS_FIELD_NUMBER: _ClassVar[int]
        sim_card_status: _sim_card_status_pb2.SimCardStatus
        def __init__(
            self, sim_card_status: _sim_card_status_pb2.SimCardStatus | str | None = ...
        ) -> None: ...

    class Monitoring(_message.Message):
        __slots__ = ("cms_active",)
        CMS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        cms_active: bool
        def __init__(self, cms_active: bool = ...) -> None: ...

    class CameraView(_message.Message):
        __slots__ = ("has_access",)
        HAS_ACCESS_FIELD_NUMBER: _ClassVar[int]
        has_access: bool
        def __init__(self, has_access: bool = ...) -> None: ...

    class SignalStrength(_message.Message):
        __slots__ = ("device_signal_level",)
        DEVICE_SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        device_signal_level: _device_signal_level_pb2.DeviceSignalLevel
        def __init__(
            self,
            device_signal_level: _device_signal_level_pb2.DeviceSignalLevel
            | str
            | None = ...,
        ) -> None: ...

    class Battery(_message.Message):
        __slots__ = ("battery_state", "charge_level_percentage", "is_without_charge")
        class BatteryState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BATTERY_STATE_UNSPECIFIED: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_OK: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_ERROR: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_WARNING: _ClassVar[LightDeviceStatus.Battery.BatteryState]
            BATTERY_STATE_ALERT: _ClassVar[LightDeviceStatus.Battery.BatteryState]

        BATTERY_STATE_UNSPECIFIED: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_OK: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_ERROR: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_WARNING: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_ALERT: LightDeviceStatus.Battery.BatteryState
        BATTERY_STATE_FIELD_NUMBER: _ClassVar[int]
        CHARGE_LEVEL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        IS_WITHOUT_CHARGE_FIELD_NUMBER: _ClassVar[int]
        battery_state: LightDeviceStatus.Battery.BatteryState
        charge_level_percentage: int
        is_without_charge: bool
        def __init__(
            self,
            battery_state: LightDeviceStatus.Battery.BatteryState | str | None = ...,
            charge_level_percentage: int | None = ...,
            is_without_charge: bool = ...,
        ) -> None: ...

    class Nfc(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class Ble(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...

    class MotionDetected(_message.Message):
        __slots__ = ("detected_at",)
        DETECTED_AT_FIELD_NUMBER: _ClassVar[int]
        detected_at: _timestamp_pb2.Timestamp
        def __init__(
            self, detected_at: _timestamp_pb2.Timestamp | _Mapping | None = ...
        ) -> None: ...

    class Privacy(_message.Message):
        __slots__ = ("enabled", "is_video_surveillance")
        IS_VIDEO_SURVEILLANCE_FIELD_NUMBER: _ClassVar[int]
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        is_video_surveillance: bool
        enabled: bool
        def __init__(
            self, is_video_surveillance: bool = ..., enabled: bool = ...
        ) -> None: ...

    class GsmStatus(_message.Message):
        __slots__ = ("status", "type")
        class GsmType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            GSM_TYPE_UNSPECIFIED: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]
            GSM_TYPE_2G: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]
            GSM_TYPE_3G: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]
            GSM_TYPE_4G: _ClassVar[LightDeviceStatus.GsmStatus.GsmType]

        GSM_TYPE_UNSPECIFIED: LightDeviceStatus.GsmStatus.GsmType
        GSM_TYPE_2G: LightDeviceStatus.GsmStatus.GsmType
        GSM_TYPE_3G: LightDeviceStatus.GsmStatus.GsmType
        GSM_TYPE_4G: LightDeviceStatus.GsmStatus.GsmType
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.GsmStatus.Status]
            STATUS_DISCONNECTED: _ClassVar[LightDeviceStatus.GsmStatus.Status]
            STATUS_CONNECTED: _ClassVar[LightDeviceStatus.GsmStatus.Status]

        STATUS_UNSPECIFIED: LightDeviceStatus.GsmStatus.Status
        STATUS_DISCONNECTED: LightDeviceStatus.GsmStatus.Status
        STATUS_CONNECTED: LightDeviceStatus.GsmStatus.Status
        TYPE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        type: LightDeviceStatus.GsmStatus.GsmType
        status: LightDeviceStatus.GsmStatus.Status
        def __init__(
            self,
            type: LightDeviceStatus.GsmStatus.GsmType | str | None = ...,
            status: LightDeviceStatus.GsmStatus.Status | str | None = ...,
        ) -> None: ...

    class DeviceFirmware(_message.Message):
        __slots__ = ("critical_firmware_available", "failed", "in_progress")
        IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        CRITICAL_FIRMWARE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
        in_progress: LightDeviceStatus.Simple
        failed: LightDeviceStatus.Simple
        critical_firmware_available: LightDeviceStatus.Simple
        def __init__(
            self,
            in_progress: LightDeviceStatus.Simple | _Mapping | None = ...,
            failed: LightDeviceStatus.Simple | _Mapping | None = ...,
            critical_firmware_available: LightDeviceStatus.Simple
            | _Mapping
            | None = ...,
        ) -> None: ...

    class SmartLock(_message.Message):
        __slots__ = ("failed", "in_progress")
        IN_PROGRESS_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        in_progress: LightDeviceStatus.Simple
        failed: LightDeviceStatus.Simple
        def __init__(
            self,
            in_progress: LightDeviceStatus.Simple | _Mapping | None = ...,
            failed: LightDeviceStatus.Simple | _Mapping | None = ...,
        ) -> None: ...

    class LifeQualityStatus(_message.Message):
        __slots__ = (
            "actual_co2",
            "actual_humidity",
            "actual_temperature",
            "co2_statuses",
            "hardware_malfunctions",
            "humidity_statuses",
            "temperature_statuses",
        )
        ACTUAL_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_CO2_FIELD_NUMBER: _ClassVar[int]
        HARDWARE_MALFUNCTIONS_FIELD_NUMBER: _ClassVar[int]
        TEMPERATURE_STATUSES_FIELD_NUMBER: _ClassVar[int]
        HUMIDITY_STATUSES_FIELD_NUMBER: _ClassVar[int]
        CO2_STATUSES_FIELD_NUMBER: _ClassVar[int]
        actual_temperature: int
        actual_humidity: int
        actual_co2: int
        hardware_malfunctions: _containers.RepeatedScalarFieldContainer[
            _life_quality_status_pb2.HardwareMalfunction
        ]
        temperature_statuses: _containers.RepeatedScalarFieldContainer[
            _life_quality_status_pb2.TemperatureStatus
        ]
        humidity_statuses: _containers.RepeatedScalarFieldContainer[
            _life_quality_status_pb2.HumidityStatus
        ]
        co2_statuses: _containers.RepeatedScalarFieldContainer[
            _life_quality_status_pb2.Co2Status
        ]
        def __init__(
            self,
            actual_temperature: int | None = ...,
            actual_humidity: int | None = ...,
            actual_co2: int | None = ...,
            hardware_malfunctions: _Iterable[
                _life_quality_status_pb2.HardwareMalfunction | str
            ]
            | None = ...,
            temperature_statuses: _Iterable[
                _life_quality_status_pb2.TemperatureStatus | str
            ]
            | None = ...,
            humidity_statuses: _Iterable[_life_quality_status_pb2.HumidityStatus | str]
            | None = ...,
            co2_statuses: _Iterable[_life_quality_status_pb2.Co2Status | str]
            | None = ...,
        ) -> None: ...

    class ValueStatus(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: int | None = ...) -> None: ...

    class WireInputStatus(_message.Message):
        __slots__ = ("contact_index", "is_alert", "type")
        CONTACT_INDEX_FIELD_NUMBER: _ClassVar[int]
        IS_ALERT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        contact_index: int
        is_alert: bool
        type: LightDeviceStatus.CustomAlarmType
        def __init__(
            self,
            contact_index: int | None = ...,
            is_alert: bool = ...,
            type: LightDeviceStatus.CustomAlarmType | str | None = ...,
        ) -> None: ...

    class TransmitterStatus(_message.Message):
        __slots__ = ("is_alert", "type")
        IS_ALERT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        is_alert: bool
        type: LightDeviceStatus.CustomAlarmType
        def __init__(
            self,
            is_alert: bool = ...,
            type: LightDeviceStatus.CustomAlarmType | str | None = ...,
        ) -> None: ...

    class RexConnected(_message.Message):
        __slots__ = ("is_rex_online",)
        IS_REX_ONLINE_FIELD_NUMBER: _ClassVar[int]
        is_rex_online: bool
        def __init__(self, is_rex_online: bool = ...) -> None: ...

    class En54FireBuzzerStatus(_message.Message):
        __slots__ = ("status",)
        class BuzzerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BUZZER_STATUS_UNSPECIFIED: _ClassVar[
                LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
            ]
            BUZZER_STATUS_ACTIVE: _ClassVar[
                LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
            ]
            BUZZER_STATUS_SILENCED: _ClassVar[
                LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
            ]
            BUZZER_STATUS_INACTIVE: _ClassVar[
                LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
            ]

        BUZZER_STATUS_UNSPECIFIED: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        BUZZER_STATUS_ACTIVE: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        BUZZER_STATUS_SILENCED: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        BUZZER_STATUS_INACTIVE: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
        def __init__(
            self,
            status: LightDeviceStatus.En54FireBuzzerStatus.BuzzerStatus
            | str
            | None = ...,
        ) -> None: ...

    class En54VadStatus(_message.Message):
        __slots__ = ("status",)
        class VadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VAD_STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]
            VAD_STATUS_ACTIVE: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]
            VAD_STATUS_SILENCED: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]
            VAD_STATUS_INACTIVE: _ClassVar[LightDeviceStatus.En54VadStatus.VadStatus]

        VAD_STATUS_UNSPECIFIED: LightDeviceStatus.En54VadStatus.VadStatus
        VAD_STATUS_ACTIVE: LightDeviceStatus.En54VadStatus.VadStatus
        VAD_STATUS_SILENCED: LightDeviceStatus.En54VadStatus.VadStatus
        VAD_STATUS_INACTIVE: LightDeviceStatus.En54VadStatus.VadStatus
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: LightDeviceStatus.En54VadStatus.VadStatus
        def __init__(
            self, status: LightDeviceStatus.En54VadStatus.VadStatus | str | None = ...
        ) -> None: ...

    class WalkTestStatus(_message.Message):
        __slots__ = ("status",)
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATUS_UNSPECIFIED: _ClassVar[LightDeviceStatus.WalkTestStatus.Status]
            STATUS_LAUNCH: _ClassVar[LightDeviceStatus.WalkTestStatus.Status]
            STATUS_PROCESS: _ClassVar[LightDeviceStatus.WalkTestStatus.Status]

        STATUS_UNSPECIFIED: LightDeviceStatus.WalkTestStatus.Status
        STATUS_LAUNCH: LightDeviceStatus.WalkTestStatus.Status
        STATUS_PROCESS: LightDeviceStatus.WalkTestStatus.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        status: LightDeviceStatus.WalkTestStatus.Status
        def __init__(
            self, status: LightDeviceStatus.WalkTestStatus.Status | str | None = ...
        ) -> None: ...

    class WifiSignalLevelStatus(_message.Message):
        __slots__ = ("wifi_signal_level",)
        WIFI_SIGNAL_LEVEL_FIELD_NUMBER: _ClassVar[int]
        wifi_signal_level: LightDeviceStatus.WifiSignalLevel
        def __init__(
            self,
            wifi_signal_level: LightDeviceStatus.WifiSignalLevel | str | None = ...,
        ) -> None: ...

    GSM_STATUS_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_STRENGTH_FIELD_NUMBER: _ClassVar[int]
    SIM_STATUS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_FIELD_NUMBER: _ClassVar[int]
    CAMERA_VIEW_FIELD_NUMBER: _ClassVar[int]
    SOMEONE_HAS_CAMERA_STREAM_ACCESS_FIELD_NUMBER: _ClassVar[int]
    SOMEONE_CAN_MAKE_PHOTO_FIELD_NUMBER: _ClassVar[int]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    ALWAYS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    REX_CONNECTED_FIELD_NUMBER: _ClassVar[int]
    DELAY_WHEN_LEAVING_FIELD_NUMBER: _ClassVar[int]
    ARMED_IN_NIGHT_MODE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_CARD_DISABLED_FIELD_NUMBER: _ClassVar[int]
    SMOKE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CO_LEVEL_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_TEMPERATURE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_BROKEN_FIELD_NUMBER: _ClassVar[int]
    CASE_DRILLING_DETECTED_FIELD_NUMBER: _ClassVar[int]
    FIRE_ALARM_FP_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_ALERT_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_FIELD_NUMBER: _ClassVar[int]
    DOOR_OPENED_FIELD_NUMBER: _ClassVar[int]
    LEAK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    NFC_FIELD_NUMBER: _ClassVar[int]
    BLE_FIELD_NUMBER: _ClassVar[int]
    POWER_MANAGEMENT_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    INTERCONNECT_FIELD_NUMBER: _ClassVar[int]
    HIGH_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    LOW_VOLTAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_SHORT_CIRCUIT_FIELD_NUMBER: _ClassVar[int]
    HIGH_CURRENT_PROTECTION_FIELD_NUMBER: _ClassVar[int]
    CONTACT_HANG_FIELD_NUMBER: _ClassVar[int]
    MIGRATION_IN_PROCESS_FIELD_NUMBER: _ClassVar[int]
    PD_COMPLIANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
    SIA_COMPLIANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
    UL_NOT_COMPLIANT_FIELD_NUMBER: _ClassVar[int]
    STANDARD_COMPLIANCE_WARNING_FIELD_NUMBER: _ClassVar[int]
    CHIMES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    REAL_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_FIELD_NUMBER: _ClassVar[int]
    RELAY_STUCK_FIELD_NUMBER: _ClassVar[int]
    LIGHT_SWITCH_THROUGH_PASS_FIELD_NUMBER: _ClassVar[int]
    ARC_SPARK_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HIGH_DIFF_TEMPERATURE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    END_OF_SERVICE_LIFE_FIELD_NUMBER: _ClassVar[int]
    HIGH_FRAME_INTERCONNECT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ANTI_MASKING_ALERT_FIELD_NUMBER: _ClassVar[int]
    INTERFERENCE_DETECTED_FIELD_NUMBER: _ClassVar[int]
    DOOR_NEED_ANTI_MASKING_FIELD_NUMBER: _ClassVar[int]
    SWITCH_ALARM_PRESSED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_WHOLE_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_TAMPER_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_ALARMS_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_TIMER_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_DEACTIVATION_WHOLE_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_DEACTIVATION_TAMPER_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_DEACTIVATION_FIELD_NUMBER: _ClassVar[int]
    ONE_TIME_DEACTIVATION_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_FIELD_NUMBER: _ClassVar[int]
    LINE_SUPPLY_HIGH_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    BUKHOOR_FIELD_NUMBER: _ClassVar[int]
    SMART_BRACKET_UNLOCKED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INSTALLATION_WARNING_FIELD_NUMBER: _ClassVar[int]
    POWER_LINE_LOW_FIELD_NUMBER: _ClassVar[int]
    LIFE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    WIRE_INPUT_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRANSMITTER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    WATER_STOP_VALVE_STUCK_FIELD_NUMBER: _ClassVar[int]
    WATER_STOP_PREVENTION_WARNING_FIELD_NUMBER: _ClassVar[int]
    EN54_FAULT_FIELD_NUMBER: _ClassVar[int]
    ANNUNCIATION_TEST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    LID_OPENED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_FIELD_NUMBER: _ClassVar[int]
    WIFI_SIGNAL_LEVEL_STATUS_FIELD_NUMBER: _ClassVar[int]
    ONVIF_USER_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    EN54_FIRE_BUZZER_STATUS_FIELD_NUMBER: _ClassVar[int]
    FIRE_BUZZER_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    EN54_VAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    EN54_DISABLEMENT_FIELD_NUMBER: _ClassVar[int]
    ARC_REPORTING_DISABLED_FIELD_NUMBER: _ClassVar[int]
    WALK_TEST_STATUS_FIELD_NUMBER: _ClassVar[int]
    gsm_status: LightDeviceStatus.GsmStatus
    signal_strength: LightDeviceStatus.SignalStrength
    sim_status: LightDeviceStatus.SimStatus
    monitoring: LightDeviceStatus.Monitoring
    camera_view: LightDeviceStatus.CameraView
    someone_has_camera_stream_access: LightDeviceStatus.Simple
    someone_can_make_photo: LightDeviceStatus.Simple
    battery: LightDeviceStatus.Battery
    always_active: LightDeviceStatus.Simple
    rex_connected: LightDeviceStatus.RexConnected
    delay_when_leaving: LightDeviceStatus.Simple
    armed_in_night_mode: LightDeviceStatus.Simple
    access_card_disabled: LightDeviceStatus.Simple
    smoke_detected: LightDeviceStatus.Simple
    co_level_detected: LightDeviceStatus.Simple
    high_temperature_detected: LightDeviceStatus.Simple
    external_contact_broken: LightDeviceStatus.Simple
    case_drilling_detected: LightDeviceStatus.Simple
    fire_alarm_fp: LightDeviceStatus.Simple
    external_contact_alert: LightDeviceStatus.Simple
    roller_shutter: LightDeviceStatus.Simple
    door_opened: LightDeviceStatus.Simple
    leak_detected: LightDeviceStatus.Simple
    nfc: LightDeviceStatus.Nfc
    ble: LightDeviceStatus.Ble
    power_management: LightDeviceStatus.Simple
    motion_detected: LightDeviceStatus.MotionDetected
    interconnect: LightDeviceStatus.Simple
    high_voltage: LightDeviceStatus.Simple
    low_voltage: LightDeviceStatus.Simple
    current_short_circuit: LightDeviceStatus.Simple
    high_current_protection: LightDeviceStatus.Simple
    contact_hang: LightDeviceStatus.Simple
    migration_in_process: LightDeviceStatus.Simple
    pd_compliance_warning: LightDeviceStatus.Simple
    sia_compliance_warning: LightDeviceStatus.Simple
    ul_not_compliant: LightDeviceStatus.Simple
    standard_compliance_warning: LightDeviceStatus.Simple
    chimes_enabled: LightDeviceStatus.Simple
    real_active: LightDeviceStatus.Simple
    privacy: LightDeviceStatus.Privacy
    relay_stuck: LightDeviceStatus.Simple
    light_switch_through_pass: LightDeviceStatus.Simple
    arc_spark_detected: LightDeviceStatus.Simple
    high_diff_temperature_detected: LightDeviceStatus.Simple
    malfunction: LightDeviceStatus.Simple
    end_of_service_life: LightDeviceStatus.Simple
    high_frame_interconnect: LightDeviceStatus.Simple
    device_firmware_status: LightDeviceStatus.DeviceFirmware
    anti_masking_alert: LightDeviceStatus.Simple
    interference_detected: LightDeviceStatus.Simple
    door_need_anti_masking: LightDeviceStatus.Simple
    switch_alarm_pressed: LightDeviceStatus.Simple
    temporary_deactivation_whole: LightDeviceStatus.Simple
    temporary_deactivation_tamper: LightDeviceStatus.Simple
    temporary_deactivation_alarms: LightDeviceStatus.Simple
    temporary_deactivation_timer: LightDeviceStatus.Simple
    one_time_deactivation_whole: LightDeviceStatus.Simple
    one_time_deactivation_tamper: LightDeviceStatus.Simple
    temporary_deactivation: LightDeviceStatus.Simple
    one_time_deactivation: LightDeviceStatus.Simple
    smart_lock: _smart_lock_pb2.SmartLockStatus.LockStatus
    line_supply_high_temperature: LightDeviceStatus.Simple
    bukhoor: LightDeviceStatus.Simple
    smart_bracket_unlocked: LightDeviceStatus.Simple
    device_installation_warning: LightDeviceStatus.Simple
    power_line_low: LightDeviceStatus.Simple
    life_quality: LightDeviceStatus.LifeQualityStatus
    temperature: LightDeviceStatus.ValueStatus
    wire_input_status: LightDeviceStatus.WireInputStatus
    transmitter_status: LightDeviceStatus.TransmitterStatus
    active_subscription: LightDeviceStatus.Simple
    water_stop_valve_stuck: LightDeviceStatus.Simple
    water_stop_prevention_warning: LightDeviceStatus.Simple
    en54_fault: LightDeviceStatus.Simple
    annunciation_test_active: LightDeviceStatus.Simple
    lid_opened: LightDeviceStatus.Simple
    storage_device: LightDeviceStatus.StorageDevice
    wifi_signal_level_status: LightDeviceStatus.WifiSignalLevelStatus
    onvif_user_auth_enabled: LightDeviceStatus.Simple
    en54_fire_buzzer_status: LightDeviceStatus.En54FireBuzzerStatus
    fire_buzzer_active: LightDeviceStatus.Simple
    en54_vad_status: LightDeviceStatus.En54VadStatus
    en54_disablement: LightDeviceStatus.Simple
    arc_reporting_disabled: LightDeviceStatus.Simple
    walk_test_status: LightDeviceStatus.WalkTestStatus
    def __init__(
        self,
        gsm_status: LightDeviceStatus.GsmStatus | _Mapping | None = ...,
        signal_strength: LightDeviceStatus.SignalStrength | _Mapping | None = ...,
        sim_status: LightDeviceStatus.SimStatus | _Mapping | None = ...,
        monitoring: LightDeviceStatus.Monitoring | _Mapping | None = ...,
        camera_view: LightDeviceStatus.CameraView | _Mapping | None = ...,
        someone_has_camera_stream_access: LightDeviceStatus.Simple
        | _Mapping
        | None = ...,
        someone_can_make_photo: LightDeviceStatus.Simple | _Mapping | None = ...,
        battery: LightDeviceStatus.Battery | _Mapping | None = ...,
        always_active: LightDeviceStatus.Simple | _Mapping | None = ...,
        rex_connected: LightDeviceStatus.RexConnected | _Mapping | None = ...,
        delay_when_leaving: LightDeviceStatus.Simple | _Mapping | None = ...,
        armed_in_night_mode: LightDeviceStatus.Simple | _Mapping | None = ...,
        access_card_disabled: LightDeviceStatus.Simple | _Mapping | None = ...,
        smoke_detected: LightDeviceStatus.Simple | _Mapping | None = ...,
        co_level_detected: LightDeviceStatus.Simple | _Mapping | None = ...,
        high_temperature_detected: LightDeviceStatus.Simple | _Mapping | None = ...,
        external_contact_broken: LightDeviceStatus.Simple | _Mapping | None = ...,
        case_drilling_detected: LightDeviceStatus.Simple | _Mapping | None = ...,
        fire_alarm_fp: LightDeviceStatus.Simple | _Mapping | None = ...,
        external_contact_alert: LightDeviceStatus.Simple | _Mapping | None = ...,
        roller_shutter: LightDeviceStatus.Simple | _Mapping | None = ...,
        door_opened: LightDeviceStatus.Simple | _Mapping | None = ...,
        leak_detected: LightDeviceStatus.Simple | _Mapping | None = ...,
        nfc: LightDeviceStatus.Nfc | _Mapping | None = ...,
        ble: LightDeviceStatus.Ble | _Mapping | None = ...,
        power_management: LightDeviceStatus.Simple | _Mapping | None = ...,
        motion_detected: LightDeviceStatus.MotionDetected | _Mapping | None = ...,
        interconnect: LightDeviceStatus.Simple | _Mapping | None = ...,
        high_voltage: LightDeviceStatus.Simple | _Mapping | None = ...,
        low_voltage: LightDeviceStatus.Simple | _Mapping | None = ...,
        current_short_circuit: LightDeviceStatus.Simple | _Mapping | None = ...,
        high_current_protection: LightDeviceStatus.Simple | _Mapping | None = ...,
        contact_hang: LightDeviceStatus.Simple | _Mapping | None = ...,
        migration_in_process: LightDeviceStatus.Simple | _Mapping | None = ...,
        pd_compliance_warning: LightDeviceStatus.Simple | _Mapping | None = ...,
        sia_compliance_warning: LightDeviceStatus.Simple | _Mapping | None = ...,
        ul_not_compliant: LightDeviceStatus.Simple | _Mapping | None = ...,
        standard_compliance_warning: LightDeviceStatus.Simple | _Mapping | None = ...,
        chimes_enabled: LightDeviceStatus.Simple | _Mapping | None = ...,
        real_active: LightDeviceStatus.Simple | _Mapping | None = ...,
        privacy: LightDeviceStatus.Privacy | _Mapping | None = ...,
        relay_stuck: LightDeviceStatus.Simple | _Mapping | None = ...,
        light_switch_through_pass: LightDeviceStatus.Simple | _Mapping | None = ...,
        arc_spark_detected: LightDeviceStatus.Simple | _Mapping | None = ...,
        high_diff_temperature_detected: LightDeviceStatus.Simple
        | _Mapping
        | None = ...,
        malfunction: LightDeviceStatus.Simple | _Mapping | None = ...,
        end_of_service_life: LightDeviceStatus.Simple | _Mapping | None = ...,
        high_frame_interconnect: LightDeviceStatus.Simple | _Mapping | None = ...,
        device_firmware_status: LightDeviceStatus.DeviceFirmware
        | _Mapping
        | None = ...,
        anti_masking_alert: LightDeviceStatus.Simple | _Mapping | None = ...,
        interference_detected: LightDeviceStatus.Simple | _Mapping | None = ...,
        door_need_anti_masking: LightDeviceStatus.Simple | _Mapping | None = ...,
        switch_alarm_pressed: LightDeviceStatus.Simple | _Mapping | None = ...,
        temporary_deactivation_whole: LightDeviceStatus.Simple | _Mapping | None = ...,
        temporary_deactivation_tamper: LightDeviceStatus.Simple | _Mapping | None = ...,
        temporary_deactivation_alarms: LightDeviceStatus.Simple | _Mapping | None = ...,
        temporary_deactivation_timer: LightDeviceStatus.Simple | _Mapping | None = ...,
        one_time_deactivation_whole: LightDeviceStatus.Simple | _Mapping | None = ...,
        one_time_deactivation_tamper: LightDeviceStatus.Simple | _Mapping | None = ...,
        temporary_deactivation: LightDeviceStatus.Simple | _Mapping | None = ...,
        one_time_deactivation: LightDeviceStatus.Simple | _Mapping | None = ...,
        smart_lock: _smart_lock_pb2.SmartLockStatus.LockStatus | str | None = ...,
        line_supply_high_temperature: LightDeviceStatus.Simple | _Mapping | None = ...,
        bukhoor: LightDeviceStatus.Simple | _Mapping | None = ...,
        smart_bracket_unlocked: LightDeviceStatus.Simple | _Mapping | None = ...,
        device_installation_warning: LightDeviceStatus.Simple | _Mapping | None = ...,
        power_line_low: LightDeviceStatus.Simple | _Mapping | None = ...,
        life_quality: LightDeviceStatus.LifeQualityStatus | _Mapping | None = ...,
        temperature: LightDeviceStatus.ValueStatus | _Mapping | None = ...,
        wire_input_status: LightDeviceStatus.WireInputStatus | _Mapping | None = ...,
        transmitter_status: LightDeviceStatus.TransmitterStatus | _Mapping | None = ...,
        active_subscription: LightDeviceStatus.Simple | _Mapping | None = ...,
        water_stop_valve_stuck: LightDeviceStatus.Simple | _Mapping | None = ...,
        water_stop_prevention_warning: LightDeviceStatus.Simple | _Mapping | None = ...,
        en54_fault: LightDeviceStatus.Simple | _Mapping | None = ...,
        annunciation_test_active: LightDeviceStatus.Simple | _Mapping | None = ...,
        lid_opened: LightDeviceStatus.Simple | _Mapping | None = ...,
        storage_device: LightDeviceStatus.StorageDevice | _Mapping | None = ...,
        wifi_signal_level_status: LightDeviceStatus.WifiSignalLevelStatus
        | _Mapping
        | None = ...,
        onvif_user_auth_enabled: LightDeviceStatus.Simple | _Mapping | None = ...,
        en54_fire_buzzer_status: LightDeviceStatus.En54FireBuzzerStatus
        | _Mapping
        | None = ...,
        fire_buzzer_active: LightDeviceStatus.Simple | _Mapping | None = ...,
        en54_vad_status: LightDeviceStatus.En54VadStatus | _Mapping | None = ...,
        en54_disablement: LightDeviceStatus.Simple | _Mapping | None = ...,
        arc_reporting_disabled: LightDeviceStatus.Simple | _Mapping | None = ...,
        walk_test_status: LightDeviceStatus.WalkTestStatus | _Mapping | None = ...,
    ) -> None: ...
