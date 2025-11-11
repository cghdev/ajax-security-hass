from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    door_protect_pb2 as _door_protect_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    double_button_pb2 as _double_button_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    en54_fire_base_pb2 as _en54_fire_base_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    home_siren_fibra_pb2 as _home_siren_fibra_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    home_siren_pb2 as _home_siren_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    motion_cam_pb2 as _motion_cam_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    motion_protect_curtain_outdoor_pb2 as _motion_protect_curtain_outdoor_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    motion_protect_pb2 as _motion_protect_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    multi_transmitter_pb2 as _multi_transmitter_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    range_extender2_pb2 as _range_extender2_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    smart_lock_pb2 as _smart_lock_pb2,
)
from systems.ajax.api.ecosystem.v2.hubsvc.commonmodels.device import (
    street_siren_pb2 as _street_siren_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubDevice(_message.Message):
    __slots__ = (
        "curtain_cam_outdoor_hm_phod",
        "door_protect",
        "door_protect_s",
        "double_button",
        "en54_a",
        "en54_h",
        "en54_h_a",
        "en54_h_v",
        "en54_h_va",
        "en54_hs_va",
        "en54_s",
        "en54_s_a",
        "en54_s_v",
        "en54_v",
        "en54_va",
        "home_siren",
        "home_siren_fibra",
        "home_siren_g3",
        "home_siren_s",
        "motion_cam_g3",
        "motion_protect",
        "motion_protect_curtain_outdoor_mini",
        "motion_protect_g3",
        "motion_protect_plus_g3",
        "motion_protect_s",
        "multi_transmitter_g3",
        "range_extender2",
        "range_extender2_fire",
        "range_extender2_s",
        "smart_lock_yale",
        "street_siren",
        "street_siren_plus_g3",
    )
    DOOR_PROTECT_FIELD_NUMBER: _ClassVar[int]
    DOOR_PROTECT_S_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    EN54_A_FIELD_NUMBER: _ClassVar[int]
    EN54_VA_FIELD_NUMBER: _ClassVar[int]
    EN54_V_FIELD_NUMBER: _ClassVar[int]
    EN54_H_VA_FIELD_NUMBER: _ClassVar[int]
    EN54_HS_VA_FIELD_NUMBER: _ClassVar[int]
    EN54_H_FIELD_NUMBER: _ClassVar[int]
    EN54_S_FIELD_NUMBER: _ClassVar[int]
    EN54_S_V_FIELD_NUMBER: _ClassVar[int]
    EN54_S_A_FIELD_NUMBER: _ClassVar[int]
    EN54_H_V_FIELD_NUMBER: _ClassVar[int]
    EN54_H_A_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_S_FIELD_NUMBER: _ClassVar[int]
    HOME_SIREN_FIBRA_FIELD_NUMBER: _ClassVar[int]
    HOME_SIREN_FIELD_NUMBER: _ClassVar[int]
    STREET_SIREN_FIELD_NUMBER: _ClassVar[int]
    STREET_SIREN_PLUS_G3_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_CURTAIN_OUTDOOR_MINI_FIELD_NUMBER: _ClassVar[int]
    HOME_SIREN_G3_FIELD_NUMBER: _ClassVar[int]
    HOME_SIREN_S_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_G3_FIELD_NUMBER: _ClassVar[int]
    MOTION_PROTECT_PLUS_G3_FIELD_NUMBER: _ClassVar[int]
    SMART_LOCK_YALE_FIELD_NUMBER: _ClassVar[int]
    MOTION_CAM_G3_FIELD_NUMBER: _ClassVar[int]
    RANGE_EXTENDER2_FIELD_NUMBER: _ClassVar[int]
    RANGE_EXTENDER2_FIRE_FIELD_NUMBER: _ClassVar[int]
    CURTAIN_CAM_OUTDOOR_HM_PHOD_FIELD_NUMBER: _ClassVar[int]
    MULTI_TRANSMITTER_G3_FIELD_NUMBER: _ClassVar[int]
    RANGE_EXTENDER2_S_FIELD_NUMBER: _ClassVar[int]
    door_protect: _door_protect_pb2.DoorProtect
    door_protect_s: _door_protect_pb2.DoorProtectS
    double_button: _double_button_pb2.DoubleButton
    en54_a: _en54_fire_base_pb2.En54A
    en54_va: _en54_fire_base_pb2.En54Va
    en54_v: _en54_fire_base_pb2.En54V
    en54_h_va: _en54_fire_base_pb2.En54HVa
    en54_hs_va: _en54_fire_base_pb2.En54HsVa
    en54_h: _en54_fire_base_pb2.En54H
    en54_s: _en54_fire_base_pb2.En54S
    en54_s_v: _en54_fire_base_pb2.En54SV
    en54_s_a: _en54_fire_base_pb2.En54SA
    en54_h_v: _en54_fire_base_pb2.En54HV
    en54_h_a: _en54_fire_base_pb2.En54Ha
    motion_protect: _motion_protect_pb2.MotionProtect
    motion_protect_s: _motion_protect_pb2.MotionProtectS
    home_siren_fibra: _home_siren_fibra_pb2.HomeSirenFibra
    home_siren: _home_siren_pb2.HomeSiren
    street_siren: _street_siren_pb2.StreetSiren
    street_siren_plus_g3: _street_siren_pb2.StreetSirenPlusG3
    motion_protect_curtain_outdoor_mini: (
        _motion_protect_curtain_outdoor_pb2.MotionProtectCurtainOutdoorMini
    )
    home_siren_g3: _home_siren_pb2.HomeSirenG3
    home_siren_s: _home_siren_pb2.HomeSirenS
    motion_protect_g3: _motion_protect_pb2.MotionProtectG3
    motion_protect_plus_g3: _motion_protect_pb2.MotionProtectPlusG3
    smart_lock_yale: _smart_lock_pb2.SmartLockYale
    motion_cam_g3: _motion_cam_pb2.MotionCamG3
    range_extender2: _range_extender2_pb2.RangeExtender2
    range_extender2_fire: _range_extender2_pb2.RangeExtender2Fire
    curtain_cam_outdoor_hm_phod: _motion_cam_pb2.CurtainCamOutdoorHmPhod
    multi_transmitter_g3: _multi_transmitter_pb2.MultiTransmitterG3
    range_extender2_s: _range_extender2_pb2.RangeExtender2S
    def __init__(
        self,
        door_protect: _door_protect_pb2.DoorProtect | _Mapping | None = ...,
        door_protect_s: _door_protect_pb2.DoorProtectS | _Mapping | None = ...,
        double_button: _double_button_pb2.DoubleButton | _Mapping | None = ...,
        en54_a: _en54_fire_base_pb2.En54A | _Mapping | None = ...,
        en54_va: _en54_fire_base_pb2.En54Va | _Mapping | None = ...,
        en54_v: _en54_fire_base_pb2.En54V | _Mapping | None = ...,
        en54_h_va: _en54_fire_base_pb2.En54HVa | _Mapping | None = ...,
        en54_hs_va: _en54_fire_base_pb2.En54HsVa | _Mapping | None = ...,
        en54_h: _en54_fire_base_pb2.En54H | _Mapping | None = ...,
        en54_s: _en54_fire_base_pb2.En54S | _Mapping | None = ...,
        en54_s_v: _en54_fire_base_pb2.En54SV | _Mapping | None = ...,
        en54_s_a: _en54_fire_base_pb2.En54SA | _Mapping | None = ...,
        en54_h_v: _en54_fire_base_pb2.En54HV | _Mapping | None = ...,
        en54_h_a: _en54_fire_base_pb2.En54Ha | _Mapping | None = ...,
        motion_protect: _motion_protect_pb2.MotionProtect | _Mapping | None = ...,
        motion_protect_s: _motion_protect_pb2.MotionProtectS | _Mapping | None = ...,
        home_siren_fibra: _home_siren_fibra_pb2.HomeSirenFibra | _Mapping | None = ...,
        home_siren: _home_siren_pb2.HomeSiren | _Mapping | None = ...,
        street_siren: _street_siren_pb2.StreetSiren | _Mapping | None = ...,
        street_siren_plus_g3: _street_siren_pb2.StreetSirenPlusG3
        | _Mapping
        | None = ...,
        motion_protect_curtain_outdoor_mini: _motion_protect_curtain_outdoor_pb2.MotionProtectCurtainOutdoorMini
        | _Mapping
        | None = ...,
        home_siren_g3: _home_siren_pb2.HomeSirenG3 | _Mapping | None = ...,
        home_siren_s: _home_siren_pb2.HomeSirenS | _Mapping | None = ...,
        motion_protect_g3: _motion_protect_pb2.MotionProtectG3 | _Mapping | None = ...,
        motion_protect_plus_g3: _motion_protect_pb2.MotionProtectPlusG3
        | _Mapping
        | None = ...,
        smart_lock_yale: _smart_lock_pb2.SmartLockYale | _Mapping | None = ...,
        motion_cam_g3: _motion_cam_pb2.MotionCamG3 | _Mapping | None = ...,
        range_extender2: _range_extender2_pb2.RangeExtender2 | _Mapping | None = ...,
        range_extender2_fire: _range_extender2_pb2.RangeExtender2Fire
        | _Mapping
        | None = ...,
        curtain_cam_outdoor_hm_phod: _motion_cam_pb2.CurtainCamOutdoorHmPhod
        | _Mapping
        | None = ...,
        multi_transmitter_g3: _multi_transmitter_pb2.MultiTransmitterG3
        | _Mapping
        | None = ...,
        range_extender2_s: _range_extender2_pb2.RangeExtender2S | _Mapping | None = ...,
    ) -> None: ...
