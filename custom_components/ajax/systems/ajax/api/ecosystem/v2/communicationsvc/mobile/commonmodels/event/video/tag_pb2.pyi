from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class ServerConnectionLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TamperOpened(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoScenarioTriggered(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChannelDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StorageErrorDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StorageWriteErrorDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoExportPrepared(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoExportFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FWUpdateStarted(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FWUpdateFinished(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FWUpdateFailed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StoragePoweredOffOverheated(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ChannelAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExternalPowerLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RingButtonPressed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PowerLow(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryDisconnected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HardFault(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MotionDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class HumanDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PetDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CarDetected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LineCrossed(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessRequestFromPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessRequestFromCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessDeniedForPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessApprovedToCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessApprovedToPro(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryVideoAccessDeniedForCompany(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DirectExportRequested(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BatteryTemperatureOutOfRange(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceBackupCommunicationChannelAdded(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceBackupCommunicationLoss(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class OnvifAuthEnabled(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceMoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeviceHit(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FanError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class StorageDeviceEjected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetArchiveStorageDeviceWriteModeMirrored(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SetArchiveStorageDeviceWriteModeRoundRobin(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class VideoEventTag(_message.Message):
    __slots__ = (
        "battery_disconnected",
        "battery_temperature_out_of_range",
        "car_detected",
        "channel_added",
        "channel_disconnected",
        "device_backup_communication_channel_added",
        "device_backup_communication_loss",
        "device_hit",
        "device_moved",
        "direct_export_requested",
        "external_power_loss",
        "fan_error",
        "fw_update_failed",
        "fw_update_finished",
        "fw_update_started",
        "hard_fault",
        "human_detected",
        "line_crossed",
        "motion_detected",
        "onvif_auth_enabled",
        "pet_detected",
        "power_low",
        "ring_button_pressed",
        "server_connection_loss",
        "set_archive_storage_device_write_mode_mirrored",
        "set_archive_storage_device_write_mode_round_robin",
        "storage_device_ejected",
        "storage_error_detected",
        "storage_powered_off_overheated",
        "storage_write_error_detected",
        "tamper_opened",
        "temporary_video_access_approved_to_company",
        "temporary_video_access_approved_to_pro",
        "temporary_video_access_denied_for_company",
        "temporary_video_access_denied_for_pro",
        "temporary_video_access_request_from_company",
        "temporary_video_access_request_from_pro",
        "video_export_failed",
        "video_export_prepared",
        "video_scenario_triggered",
    )
    SERVER_CONNECTION_LOSS_FIELD_NUMBER: _ClassVar[int]
    TAMPER_OPENED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SCENARIO_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_ERROR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_WRITE_ERROR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_POWERED_OFF_OVERHEATED_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DEVICE_EJECTED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EXPORT_PREPARED_FIELD_NUMBER: _ClassVar[int]
    VIDEO_EXPORT_FAILED_FIELD_NUMBER: _ClassVar[int]
    DIRECT_EXPORT_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    SET_ARCHIVE_STORAGE_DEVICE_WRITE_MODE_MIRRORED_FIELD_NUMBER: _ClassVar[int]
    SET_ARCHIVE_STORAGE_DEVICE_WRITE_MODE_ROUND_ROBIN_FIELD_NUMBER: _ClassVar[int]
    FW_UPDATE_STARTED_FIELD_NUMBER: _ClassVar[int]
    FW_UPDATE_FINISHED_FIELD_NUMBER: _ClassVar[int]
    FW_UPDATE_FAILED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ADDED_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_POWER_LOSS_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_PRESSED_FIELD_NUMBER: _ClassVar[int]
    POWER_LOW_FIELD_NUMBER: _ClassVar[int]
    BATTERY_DISCONNECTED_FIELD_NUMBER: _ClassVar[int]
    HARD_FAULT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_TEMPERATURE_OUT_OF_RANGE_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_REQUEST_FROM_PRO_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_REQUEST_FROM_COMPANY_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_DENIED_FOR_PRO_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_APPROVED_TO_COMPANY_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_APPROVED_TO_PRO_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_VIDEO_ACCESS_DENIED_FOR_COMPANY_FIELD_NUMBER: _ClassVar[int]
    MOTION_DETECTED_FIELD_NUMBER: _ClassVar[int]
    HUMAN_DETECTED_FIELD_NUMBER: _ClassVar[int]
    PET_DETECTED_FIELD_NUMBER: _ClassVar[int]
    CAR_DETECTED_FIELD_NUMBER: _ClassVar[int]
    LINE_CROSSED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BACKUP_COMMUNICATION_CHANNEL_ADDED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BACKUP_COMMUNICATION_LOSS_FIELD_NUMBER: _ClassVar[int]
    ONVIF_AUTH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MOVED_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HIT_FIELD_NUMBER: _ClassVar[int]
    FAN_ERROR_FIELD_NUMBER: _ClassVar[int]
    server_connection_loss: ServerConnectionLoss
    tamper_opened: TamperOpened
    video_scenario_triggered: VideoScenarioTriggered
    storage_error_detected: StorageErrorDetected
    storage_write_error_detected: StorageWriteErrorDetected
    storage_powered_off_overheated: StoragePoweredOffOverheated
    storage_device_ejected: StorageDeviceEjected
    video_export_prepared: VideoExportPrepared
    video_export_failed: VideoExportFailed
    direct_export_requested: DirectExportRequested
    set_archive_storage_device_write_mode_mirrored: (
        SetArchiveStorageDeviceWriteModeMirrored
    )
    set_archive_storage_device_write_mode_round_robin: (
        SetArchiveStorageDeviceWriteModeRoundRobin
    )
    fw_update_started: FWUpdateStarted
    fw_update_finished: FWUpdateFinished
    fw_update_failed: FWUpdateFailed
    channel_disconnected: ChannelDisconnected
    channel_added: ChannelAdded
    external_power_loss: ExternalPowerLoss
    ring_button_pressed: RingButtonPressed
    power_low: PowerLow
    battery_disconnected: BatteryDisconnected
    hard_fault: HardFault
    battery_temperature_out_of_range: BatteryTemperatureOutOfRange
    temporary_video_access_request_from_pro: TemporaryVideoAccessRequestFromPro
    temporary_video_access_request_from_company: TemporaryVideoAccessRequestFromCompany
    temporary_video_access_denied_for_pro: TemporaryVideoAccessDeniedForPro
    temporary_video_access_approved_to_company: TemporaryVideoAccessApprovedToCompany
    temporary_video_access_approved_to_pro: TemporaryVideoAccessApprovedToPro
    temporary_video_access_denied_for_company: TemporaryVideoAccessDeniedForCompany
    motion_detected: MotionDetected
    human_detected: HumanDetected
    pet_detected: PetDetected
    car_detected: CarDetected
    line_crossed: LineCrossed
    device_backup_communication_channel_added: DeviceBackupCommunicationChannelAdded
    device_backup_communication_loss: DeviceBackupCommunicationLoss
    onvif_auth_enabled: OnvifAuthEnabled
    device_moved: DeviceMoved
    device_hit: DeviceHit
    fan_error: FanError
    def __init__(
        self,
        server_connection_loss: ServerConnectionLoss | _Mapping | None = ...,
        tamper_opened: TamperOpened | _Mapping | None = ...,
        video_scenario_triggered: VideoScenarioTriggered | _Mapping | None = ...,
        storage_error_detected: StorageErrorDetected | _Mapping | None = ...,
        storage_write_error_detected: StorageWriteErrorDetected | _Mapping | None = ...,
        storage_powered_off_overheated: StoragePoweredOffOverheated
        | _Mapping
        | None = ...,
        storage_device_ejected: StorageDeviceEjected | _Mapping | None = ...,
        video_export_prepared: VideoExportPrepared | _Mapping | None = ...,
        video_export_failed: VideoExportFailed | _Mapping | None = ...,
        direct_export_requested: DirectExportRequested | _Mapping | None = ...,
        set_archive_storage_device_write_mode_mirrored: SetArchiveStorageDeviceWriteModeMirrored
        | _Mapping
        | None = ...,
        set_archive_storage_device_write_mode_round_robin: SetArchiveStorageDeviceWriteModeRoundRobin
        | _Mapping
        | None = ...,
        fw_update_started: FWUpdateStarted | _Mapping | None = ...,
        fw_update_finished: FWUpdateFinished | _Mapping | None = ...,
        fw_update_failed: FWUpdateFailed | _Mapping | None = ...,
        channel_disconnected: ChannelDisconnected | _Mapping | None = ...,
        channel_added: ChannelAdded | _Mapping | None = ...,
        external_power_loss: ExternalPowerLoss | _Mapping | None = ...,
        ring_button_pressed: RingButtonPressed | _Mapping | None = ...,
        power_low: PowerLow | _Mapping | None = ...,
        battery_disconnected: BatteryDisconnected | _Mapping | None = ...,
        hard_fault: HardFault | _Mapping | None = ...,
        battery_temperature_out_of_range: BatteryTemperatureOutOfRange
        | _Mapping
        | None = ...,
        temporary_video_access_request_from_pro: TemporaryVideoAccessRequestFromPro
        | _Mapping
        | None = ...,
        temporary_video_access_request_from_company: TemporaryVideoAccessRequestFromCompany
        | _Mapping
        | None = ...,
        temporary_video_access_denied_for_pro: TemporaryVideoAccessDeniedForPro
        | _Mapping
        | None = ...,
        temporary_video_access_approved_to_company: TemporaryVideoAccessApprovedToCompany
        | _Mapping
        | None = ...,
        temporary_video_access_approved_to_pro: TemporaryVideoAccessApprovedToPro
        | _Mapping
        | None = ...,
        temporary_video_access_denied_for_company: TemporaryVideoAccessDeniedForCompany
        | _Mapping
        | None = ...,
        motion_detected: MotionDetected | _Mapping | None = ...,
        human_detected: HumanDetected | _Mapping | None = ...,
        pet_detected: PetDetected | _Mapping | None = ...,
        car_detected: CarDetected | _Mapping | None = ...,
        line_crossed: LineCrossed | _Mapping | None = ...,
        device_backup_communication_channel_added: DeviceBackupCommunicationChannelAdded
        | _Mapping
        | None = ...,
        device_backup_communication_loss: DeviceBackupCommunicationLoss
        | _Mapping
        | None = ...,
        onvif_auth_enabled: OnvifAuthEnabled | _Mapping | None = ...,
        device_moved: DeviceMoved | _Mapping | None = ...,
        device_hit: DeviceHit | _Mapping | None = ...,
        fan_error: FanError | _Mapping | None = ...,
    ) -> None: ...
