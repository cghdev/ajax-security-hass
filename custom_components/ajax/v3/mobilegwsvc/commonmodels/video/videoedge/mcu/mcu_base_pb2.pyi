from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    battery_charged_state_pb2 as _battery_charged_state_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import (
    chime_pb2 as _chime_pb2,
)
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import mcu_pb2 as _mcu_pb2
from systems.ajax.api.mobile.v2.common.video.videoedge.mcu import (
    operating_mode_pb2 as _operating_mode_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class McuBase(_message.Message):
    __slots__ = (
        "battery_charged_state",
        "battery_state",
        "battery_temperature_state",
        "capabilities",
        "chime",
        "external_power_state",
        "mcu_state",
        "operating_mode",
        "pir_motion_led_indication",
        "ring_button_bell_state",
    )
    EXTERNAL_POWER_STATE_FIELD_NUMBER: _ClassVar[int]
    MCU_STATE_FIELD_NUMBER: _ClassVar[int]
    OPERATING_MODE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_STATE_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CHARGED_STATE_FIELD_NUMBER: _ClassVar[int]
    CHIME_FIELD_NUMBER: _ClassVar[int]
    BATTERY_TEMPERATURE_STATE_FIELD_NUMBER: _ClassVar[int]
    PIR_MOTION_LED_INDICATION_FIELD_NUMBER: _ClassVar[int]
    RING_BUTTON_BELL_STATE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    external_power_state: _mcu_pb2.Mcu.ExternalPowerState
    mcu_state: _mcu_pb2.Mcu.McuState
    operating_mode: _operating_mode_pb2.OperatingMode
    battery_state: _mcu_pb2.Mcu.BatteryState
    battery_charged_state: _battery_charged_state_pb2.BatteryChargedState
    chime: _chime_pb2.Chime
    battery_temperature_state: _mcu_pb2.Mcu.BatteryTemperatureState
    pir_motion_led_indication: _mcu_pb2.Mcu.PirMotionLedIndication
    ring_button_bell_state: _mcu_pb2.Mcu.RingButtonBellState
    capabilities: _mcu_pb2.Mcu.Capabilities
    def __init__(
        self,
        external_power_state: _mcu_pb2.Mcu.ExternalPowerState | str | None = ...,
        mcu_state: _mcu_pb2.Mcu.McuState | str | None = ...,
        operating_mode: _operating_mode_pb2.OperatingMode | str | None = ...,
        battery_state: _mcu_pb2.Mcu.BatteryState | str | None = ...,
        battery_charged_state: _battery_charged_state_pb2.BatteryChargedState
        | str
        | None = ...,
        chime: _chime_pb2.Chime | _Mapping | None = ...,
        battery_temperature_state: _mcu_pb2.Mcu.BatteryTemperatureState
        | str
        | None = ...,
        pir_motion_led_indication: _mcu_pb2.Mcu.PirMotionLedIndication
        | str
        | None = ...,
        ring_button_bell_state: _mcu_pb2.Mcu.RingButtonBellState | str | None = ...,
        capabilities: _mcu_pb2.Mcu.Capabilities | _Mapping | None = ...,
    ) -> None: ...
