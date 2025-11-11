from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    data_channel_connection_state_pb2 as _data_channel_connection_state_pb2,
)
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    data_channel_signal_quality_pb2 as _data_channel_signal_quality_pb2,
)
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    device_arming_mode_pb2 as _device_arming_mode_pb2,
)
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    device_state_pb2 as _device_state_pb2,
)
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    device_transmition_power_mode_pb2 as _device_transmition_power_mode_pb2,
)
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    jeweller_connection_state_pb2 as _jeweller_connection_state_pb2,
)
from systems.ajax.api.mobile.v2.common.hub.device.common import (
    jeweller_signal_quality_pb2 as _jeweller_signal_quality_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class BackupChannelInfo(_message.Message):
    __slots__ = (
        "alarm_delay_seconds",
        "arm_delay_seconds",
        "assigned_extender_device_index",
        "assigned_extender_info",
        "chime_signal",
        "chime_triggers",
        "data_channel_connection_state",
        "data_channel_signal_quality",
        "device_arming_mode",
        "device_index",
        "device_state",
        "device_transmition_power_mode",
        "jeweller_connection_state",
        "jeweller_signal_quality",
        "night_mode_alarm_delay_seconds",
        "night_mode_arm_delay_seconds",
        "siren_triggers",
    )
    class SirenTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SIREN_TRIGGER_UNSPECIFIED: _ClassVar[BackupChannelInfo.SirenTrigger]
        SIREN_TRIGGER_MOTION: _ClassVar[BackupChannelInfo.SirenTrigger]

    SIREN_TRIGGER_UNSPECIFIED: BackupChannelInfo.SirenTrigger
    SIREN_TRIGGER_MOTION: BackupChannelInfo.SirenTrigger
    class ChimeTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHIME_TRIGGER_UNSPECIFIED: _ClassVar[BackupChannelInfo.ChimeTrigger]
        CHIME_TRIGGER_BUTTON: _ClassVar[BackupChannelInfo.ChimeTrigger]

    CHIME_TRIGGER_UNSPECIFIED: BackupChannelInfo.ChimeTrigger
    CHIME_TRIGGER_BUTTON: BackupChannelInfo.ChimeTrigger
    class AssignedExtenderInfo(_message.Message):
        __slots__ = ("device_index", "is_online", "name")
        DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
        device_index: int
        name: str
        is_online: bool
        def __init__(
            self,
            device_index: int | None = ...,
            name: str | None = ...,
            is_online: bool = ...,
        ) -> None: ...

    JEWELLER_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    JEWELLER_SIGNAL_QUALITY_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    DATA_CHANNEL_SIGNAL_QUALITY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TRANSMITION_POWER_MODE_FIELD_NUMBER: _ClassVar[int]
    ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    NIGHT_MODE_ALARM_DELAY_SECONDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_ARMING_MODE_FIELD_NUMBER: _ClassVar[int]
    SIREN_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_TRIGGERS_FIELD_NUMBER: _ClassVar[int]
    CHIME_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_EXTENDER_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    DEVICE_STATE_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    ASSIGNED_EXTENDER_INFO_FIELD_NUMBER: _ClassVar[int]
    jeweller_connection_state: _jeweller_connection_state_pb2.JewellerConnectionState
    jeweller_signal_quality: _jeweller_signal_quality_pb2.JewellerSignalQuality
    data_channel_connection_state: (
        _data_channel_connection_state_pb2.DataChannelConnectionState
    )
    data_channel_signal_quality: (
        _data_channel_signal_quality_pb2.DataChannelSignalQuality
    )
    device_transmition_power_mode: (
        _device_transmition_power_mode_pb2.DeviceTransmitionPowerMode
    )
    arm_delay_seconds: int
    alarm_delay_seconds: int
    night_mode_arm_delay_seconds: int
    night_mode_alarm_delay_seconds: int
    device_arming_mode: _device_arming_mode_pb2.DeviceArmingMode
    siren_triggers: _containers.RepeatedScalarFieldContainer[
        BackupChannelInfo.SirenTrigger
    ]
    chime_triggers: _containers.RepeatedScalarFieldContainer[
        BackupChannelInfo.ChimeTrigger
    ]
    chime_signal: int
    assigned_extender_device_index: int
    device_state: _device_state_pb2.DeviceState
    device_index: int
    assigned_extender_info: BackupChannelInfo.AssignedExtenderInfo
    def __init__(
        self,
        jeweller_connection_state: _jeweller_connection_state_pb2.JewellerConnectionState
        | str
        | None = ...,
        jeweller_signal_quality: _jeweller_signal_quality_pb2.JewellerSignalQuality
        | str
        | None = ...,
        data_channel_connection_state: _data_channel_connection_state_pb2.DataChannelConnectionState
        | str
        | None = ...,
        data_channel_signal_quality: _data_channel_signal_quality_pb2.DataChannelSignalQuality
        | str
        | None = ...,
        device_transmition_power_mode: _device_transmition_power_mode_pb2.DeviceTransmitionPowerMode
        | str
        | None = ...,
        arm_delay_seconds: int | None = ...,
        alarm_delay_seconds: int | None = ...,
        night_mode_arm_delay_seconds: int | None = ...,
        night_mode_alarm_delay_seconds: int | None = ...,
        device_arming_mode: _device_arming_mode_pb2.DeviceArmingMode | str | None = ...,
        siren_triggers: _Iterable[BackupChannelInfo.SirenTrigger | str] | None = ...,
        chime_triggers: _Iterable[BackupChannelInfo.ChimeTrigger | str] | None = ...,
        chime_signal: int | None = ...,
        assigned_extender_device_index: int | None = ...,
        device_state: _device_state_pb2.DeviceState | str | None = ...,
        device_index: int | None = ...,
        assigned_extender_info: BackupChannelInfo.AssignedExtenderInfo
        | _Mapping
        | None = ...,
    ) -> None: ...
