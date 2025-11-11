from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.protobuf.hub import name_pb2 as _name_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class WireSiren(_message.Message):
    __slots__ = (
        "alarm_duration",
        "associated_group_id",
        "beep_on_arm_disarm",
        "beep_on_arm_disarm_v2",
        "beep_on_delay",
        "beep_on_delay_v2",
        "cms_device_index",
        "enabled",
        "group_id",
        "id",
        "name",
        "room_id",
    )
    class BeepOnArmDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_ARM_DISARM_INFO: _ClassVar[WireSiren.BeepOnArmDisarm]
        BEEP_ON_ARM: _ClassVar[WireSiren.BeepOnArmDisarm]
        BEEP_ON_DISARM: _ClassVar[WireSiren.BeepOnArmDisarm]
        BEEP_ON_NIGHT_ARM: _ClassVar[WireSiren.BeepOnArmDisarm]
        BEEP_ON_NIGHT_DISARM: _ClassVar[WireSiren.BeepOnArmDisarm]

    NO_BEEP_ON_ARM_DISARM_INFO: WireSiren.BeepOnArmDisarm
    BEEP_ON_ARM: WireSiren.BeepOnArmDisarm
    BEEP_ON_DISARM: WireSiren.BeepOnArmDisarm
    BEEP_ON_NIGHT_ARM: WireSiren.BeepOnArmDisarm
    BEEP_ON_NIGHT_DISARM: WireSiren.BeepOnArmDisarm
    class BeepOnDelay(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_BEEP_ON_DELAY_INFO: _ClassVar[WireSiren.BeepOnDelay]
        BEEP_ON_ARM_DELAY: _ClassVar[WireSiren.BeepOnDelay]
        BEEP_ON_DISARM_DELAY: _ClassVar[WireSiren.BeepOnDelay]
        BEEP_ON_NIGHT_ARM_DELAY: _ClassVar[WireSiren.BeepOnDelay]
        BEEP_ON_NIGHT_DISARM_DELAY: _ClassVar[WireSiren.BeepOnDelay]

    NO_BEEP_ON_DELAY_INFO: WireSiren.BeepOnDelay
    BEEP_ON_ARM_DELAY: WireSiren.BeepOnDelay
    BEEP_ON_DISARM_DELAY: WireSiren.BeepOnDelay
    BEEP_ON_NIGHT_ARM_DELAY: WireSiren.BeepOnDelay
    BEEP_ON_NIGHT_DISARM_DELAY: WireSiren.BeepOnDelay
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ALARM_DURATION_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_ARM_DISARM_V2_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_FIELD_NUMBER: _ClassVar[int]
    BEEP_ON_DELAY_V2_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATED_GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    CMS_DEVICE_INDEX_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: _name_pb2.Name
    group_id: str
    room_id: str
    enabled: bool
    alarm_duration: int
    beep_on_arm_disarm: bool
    beep_on_arm_disarm_v2: _containers.RepeatedScalarFieldContainer[
        WireSiren.BeepOnArmDisarm
    ]
    beep_on_delay: bool
    beep_on_delay_v2: _containers.RepeatedScalarFieldContainer[WireSiren.BeepOnDelay]
    associated_group_id: str
    cms_device_index: int
    def __init__(
        self,
        id: str | None = ...,
        name: _name_pb2.Name | _Mapping | None = ...,
        group_id: str | None = ...,
        room_id: str | None = ...,
        enabled: bool = ...,
        alarm_duration: int | None = ...,
        beep_on_arm_disarm: bool = ...,
        beep_on_arm_disarm_v2: _Iterable[WireSiren.BeepOnArmDisarm | str] | None = ...,
        beep_on_delay: bool = ...,
        beep_on_delay_v2: _Iterable[WireSiren.BeepOnDelay | str] | None = ...,
        associated_group_id: str | None = ...,
        cms_device_index: int | None = ...,
    ) -> None: ...
