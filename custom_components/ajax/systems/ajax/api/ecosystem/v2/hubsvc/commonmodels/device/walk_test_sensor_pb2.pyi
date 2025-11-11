from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class WalkTestSensor(_message.Message):
    __slots__ = (
        "co_sensor",
        "custom_event",
        "duress_code",
        "external_contact",
        "fire_sensor",
        "gas_sensor",
        "glass_break_sensor",
        "intrusion_sensor",
        "leak_sensor",
        "magnetic_contact",
        "malfunction",
        "masking_sensor",
        "masking_sensor_left",
        "masking_sensor_right",
        "medical_alarm",
        "motion_sensor",
        "motion_sensor_left",
        "motion_sensor_right",
        "panic_button",
        "roller_shutter_sensor",
        "seismic_sensor",
        "shock_sensor",
        "smoke_sensor",
        "tamper_sensor",
        "temperature_sensor",
        "tilt_sensor",
    )
    class MagneticContact(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class ExternalContact(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MotionSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MotionSensorRight(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MotionSensorLeft(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MaskingSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MaskingSensorRight(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MaskingSensorLeft(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class SmokeSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class CoSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class SeismicSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class PanicButton(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class GlassBreakSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class TemperatureSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class ShockSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class TiltSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class TamperSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class IntrusionSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class FireSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class GasSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class MedicalAlarm(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Malfunction(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class LeakSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class CustomEvent(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class DuressCode(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class RollerShutterSensor(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    MAGNETIC_CONTACT_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_CONTACT_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    MOTION_SENSOR_LEFT_FIELD_NUMBER: _ClassVar[int]
    SMOKE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    GAS_SENSOR_FIELD_NUMBER: _ClassVar[int]
    CO_SENSOR_FIELD_NUMBER: _ClassVar[int]
    PANIC_BUTTON_FIELD_NUMBER: _ClassVar[int]
    GLASS_BREAK_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    SEISMIC_SENSOR_FIELD_NUMBER: _ClassVar[int]
    SHOCK_SENSOR_FIELD_NUMBER: _ClassVar[int]
    TILT_SENSOR_FIELD_NUMBER: _ClassVar[int]
    TAMPER_SENSOR_FIELD_NUMBER: _ClassVar[int]
    INTRUSION_SENSOR_FIELD_NUMBER: _ClassVar[int]
    FIRE_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MEDICAL_ALARM_FIELD_NUMBER: _ClassVar[int]
    MALFUNCTION_FIELD_NUMBER: _ClassVar[int]
    LEAK_SENSOR_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EVENT_FIELD_NUMBER: _ClassVar[int]
    DURESS_CODE_FIELD_NUMBER: _ClassVar[int]
    ROLLER_SHUTTER_SENSOR_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_RIGHT_FIELD_NUMBER: _ClassVar[int]
    MASKING_SENSOR_LEFT_FIELD_NUMBER: _ClassVar[int]
    magnetic_contact: WalkTestSensor.MagneticContact
    external_contact: WalkTestSensor.ExternalContact
    motion_sensor: WalkTestSensor.MotionSensor
    motion_sensor_right: WalkTestSensor.MotionSensorRight
    motion_sensor_left: WalkTestSensor.MotionSensorLeft
    smoke_sensor: WalkTestSensor.SmokeSensor
    gas_sensor: WalkTestSensor.GasSensor
    co_sensor: WalkTestSensor.CoSensor
    panic_button: WalkTestSensor.PanicButton
    glass_break_sensor: WalkTestSensor.GlassBreakSensor
    masking_sensor: WalkTestSensor.MaskingSensor
    temperature_sensor: WalkTestSensor.TemperatureSensor
    seismic_sensor: WalkTestSensor.SeismicSensor
    shock_sensor: WalkTestSensor.ShockSensor
    tilt_sensor: WalkTestSensor.TiltSensor
    tamper_sensor: WalkTestSensor.TamperSensor
    intrusion_sensor: WalkTestSensor.IntrusionSensor
    fire_sensor: WalkTestSensor.FireSensor
    medical_alarm: WalkTestSensor.MedicalAlarm
    malfunction: WalkTestSensor.Malfunction
    leak_sensor: WalkTestSensor.LeakSensor
    custom_event: WalkTestSensor.CustomEvent
    duress_code: WalkTestSensor.DuressCode
    roller_shutter_sensor: WalkTestSensor.RollerShutterSensor
    masking_sensor_right: WalkTestSensor.MaskingSensorRight
    masking_sensor_left: WalkTestSensor.MaskingSensorLeft
    def __init__(
        self,
        magnetic_contact: WalkTestSensor.MagneticContact | _Mapping | None = ...,
        external_contact: WalkTestSensor.ExternalContact | _Mapping | None = ...,
        motion_sensor: WalkTestSensor.MotionSensor | _Mapping | None = ...,
        motion_sensor_right: WalkTestSensor.MotionSensorRight | _Mapping | None = ...,
        motion_sensor_left: WalkTestSensor.MotionSensorLeft | _Mapping | None = ...,
        smoke_sensor: WalkTestSensor.SmokeSensor | _Mapping | None = ...,
        gas_sensor: WalkTestSensor.GasSensor | _Mapping | None = ...,
        co_sensor: WalkTestSensor.CoSensor | _Mapping | None = ...,
        panic_button: WalkTestSensor.PanicButton | _Mapping | None = ...,
        glass_break_sensor: WalkTestSensor.GlassBreakSensor | _Mapping | None = ...,
        masking_sensor: WalkTestSensor.MaskingSensor | _Mapping | None = ...,
        temperature_sensor: WalkTestSensor.TemperatureSensor | _Mapping | None = ...,
        seismic_sensor: WalkTestSensor.SeismicSensor | _Mapping | None = ...,
        shock_sensor: WalkTestSensor.ShockSensor | _Mapping | None = ...,
        tilt_sensor: WalkTestSensor.TiltSensor | _Mapping | None = ...,
        tamper_sensor: WalkTestSensor.TamperSensor | _Mapping | None = ...,
        intrusion_sensor: WalkTestSensor.IntrusionSensor | _Mapping | None = ...,
        fire_sensor: WalkTestSensor.FireSensor | _Mapping | None = ...,
        medical_alarm: WalkTestSensor.MedicalAlarm | _Mapping | None = ...,
        malfunction: WalkTestSensor.Malfunction | _Mapping | None = ...,
        leak_sensor: WalkTestSensor.LeakSensor | _Mapping | None = ...,
        custom_event: WalkTestSensor.CustomEvent | _Mapping | None = ...,
        duress_code: WalkTestSensor.DuressCode | _Mapping | None = ...,
        roller_shutter_sensor: WalkTestSensor.RollerShutterSensor
        | _Mapping
        | None = ...,
        masking_sensor_right: WalkTestSensor.MaskingSensorRight | _Mapping | None = ...,
        masking_sensor_left: WalkTestSensor.MaskingSensorLeft | _Mapping | None = ...,
    ) -> None: ...
