from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.type import datetime_pb2 as _datetime_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class LifeQualityDataDiscreteness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIFE_QUALITY_DATA_DISCRETENESS_UNSPECIFIED: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_MINUTE: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_HOUR: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_DAY: _ClassVar[LifeQualityDataDiscreteness]
    LIFE_QUALITY_DATA_DISCRETENESS_MONTH: _ClassVar[LifeQualityDataDiscreteness]

LIFE_QUALITY_DATA_DISCRETENESS_UNSPECIFIED: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_MINUTE: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_HOUR: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_DAY: LifeQualityDataDiscreteness
LIFE_QUALITY_DATA_DISCRETENESS_MONTH: LifeQualityDataDiscreteness

class LifeQualityDataItem(_message.Message):
    __slots__ = ("value_y", "value_y_range")
    VALUE_Y_FIELD_NUMBER: _ClassVar[int]
    VALUE_Y_RANGE_FIELD_NUMBER: _ClassVar[int]
    value_y: float
    value_y_range: LifeQualityDataRange
    def __init__(
        self,
        value_y: float | None = ...,
        value_y_range: LifeQualityDataRange | _Mapping | None = ...,
    ) -> None: ...

class LifeQualityDataRange(_message.Message):
    __slots__ = ("max_value_y", "min_value_y")
    MIN_VALUE_Y_FIELD_NUMBER: _ClassVar[int]
    MAX_VALUE_Y_FIELD_NUMBER: _ClassVar[int]
    min_value_y: float
    max_value_y: float
    def __init__(
        self, min_value_y: float | None = ..., max_value_y: float | None = ...
    ) -> None: ...

class LifeQualityDataResponse(_message.Message):
    __slots__ = ("values_airquality", "values_humidity", "values_temperature")
    class ValuesTemperatureEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LifeQualityDataItem
        def __init__(
            self,
            key: int | None = ...,
            value: LifeQualityDataItem | _Mapping | None = ...,
        ) -> None: ...

    class ValuesHumidityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LifeQualityDataItem
        def __init__(
            self,
            key: int | None = ...,
            value: LifeQualityDataItem | _Mapping | None = ...,
        ) -> None: ...

    class ValuesAirqualityEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LifeQualityDataItem
        def __init__(
            self,
            key: int | None = ...,
            value: LifeQualityDataItem | _Mapping | None = ...,
        ) -> None: ...

    VALUES_TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    VALUES_HUMIDITY_FIELD_NUMBER: _ClassVar[int]
    VALUES_AIRQUALITY_FIELD_NUMBER: _ClassVar[int]
    values_temperature: _containers.MessageMap[int, LifeQualityDataItem]
    values_humidity: _containers.MessageMap[int, LifeQualityDataItem]
    values_airquality: _containers.MessageMap[int, LifeQualityDataItem]
    def __init__(
        self,
        values_temperature: _Mapping[int, LifeQualityDataItem] | None = ...,
        values_humidity: _Mapping[int, LifeQualityDataItem] | None = ...,
        values_airquality: _Mapping[int, LifeQualityDataItem] | None = ...,
    ) -> None: ...

class LifeQualityDataRequest(_message.Message):
    __slots__ = (
        "device_hex_id",
        "discreteness",
        "end_timestamp",
        "hub_hex_id",
        "start_timestamp",
        "time_zone",
    )
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DISCRETENESS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    device_hex_id: str
    discreteness: LifeQualityDataDiscreteness
    time_zone: _datetime_pb2.TimeZone
    start_timestamp: int
    end_timestamp: int
    def __init__(
        self,
        hub_hex_id: str | None = ...,
        device_hex_id: str | None = ...,
        discreteness: LifeQualityDataDiscreteness | str | None = ...,
        time_zone: _datetime_pb2.TimeZone | _Mapping | None = ...,
        start_timestamp: int | None = ...,
        end_timestamp: int | None = ...,
    ) -> None: ...

class StreamLifeQualityDataRequest(_message.Message):
    __slots__ = (
        "device_hex_id",
        "discreteness",
        "hub_hex_id",
        "start_timestamp",
        "time_zone",
    )
    HUB_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HEX_ID_FIELD_NUMBER: _ClassVar[int]
    DISCRETENESS_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    hub_hex_id: str
    device_hex_id: str
    discreteness: LifeQualityDataDiscreteness
    time_zone: _datetime_pb2.TimeZone
    start_timestamp: int
    def __init__(
        self,
        hub_hex_id: str | None = ...,
        device_hex_id: str | None = ...,
        discreteness: LifeQualityDataDiscreteness | str | None = ...,
        time_zone: _datetime_pb2.TimeZone | _Mapping | None = ...,
        start_timestamp: int | None = ...,
    ) -> None: ...
