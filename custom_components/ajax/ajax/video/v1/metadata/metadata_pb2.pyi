from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

from ajax.video.v1.types import types_pb2 as _types_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class Dummy(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Batch(_message.Message):
    __slots__ = ("frames", "type")
    class Frame(_message.Message):
        __slots__ = ("data", "ts", "tz_offset")
        TS_FIELD_NUMBER: _ClassVar[int]
        TZ_OFFSET_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        ts: int
        tz_offset: int
        data: bytes
        def __init__(
            self,
            ts: int | None = ...,
            tz_offset: int | None = ...,
            data: bytes | None = ...,
        ) -> None: ...

    TYPE_FIELD_NUMBER: _ClassVar[int]
    FRAMES_FIELD_NUMBER: _ClassVar[int]
    type: str
    frames: _containers.RepeatedCompositeFieldContainer[Batch.Frame]
    def __init__(
        self,
        type: str | None = ...,
        frames: _Iterable[Batch.Frame | _Mapping] | None = ...,
    ) -> None: ...

class Figures(_message.Message):
    __slots__ = ("duration", "items", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[Figures.Type]
        DEBUG: _ClassVar[Figures.Type]
        SUBTITLES: _ClassVar[Figures.Type]
        MOTION_DETECTOR: _ClassVar[Figures.Type]
        OBJECT_DETECTOR: _ClassVar[Figures.Type]

    UNKNOWN: Figures.Type
    DEBUG: Figures.Type
    SUBTITLES: Figures.Type
    MOTION_DETECTOR: Figures.Type
    OBJECT_DETECTOR: Figures.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    type: Figures.Type
    items: _containers.RepeatedCompositeFieldContainer[Figure]
    duration: _duration_pb2.Duration
    def __init__(
        self,
        type: Figures.Type | str | None = ...,
        items: _Iterable[Figure | _Mapping] | None = ...,
        duration: _duration_pb2.Duration | _Mapping | None = ...,
    ) -> None: ...

class Figure(_message.Message):
    __slots__ = (
        "alpha",
        "color",
        "label",
        "line",
        "mask",
        "rect",
        "rect_with_text",
        "thickness",
    )
    class Thickness(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        T_NONE: _ClassVar[Figure.Thickness]
        T_THIN: _ClassVar[Figure.Thickness]
        T_NORMAL: _ClassVar[Figure.Thickness]
        T_THICK: _ClassVar[Figure.Thickness]

    T_NONE: Figure.Thickness
    T_THIN: Figure.Thickness
    T_NORMAL: Figure.Thickness
    T_THICK: Figure.Thickness
    COLOR_FIELD_NUMBER: _ClassVar[int]
    THICKNESS_FIELD_NUMBER: _ClassVar[int]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    RECT_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    RECT_WITH_TEXT_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    color: _types_pb2.Color
    thickness: Figure.Thickness
    alpha: float
    rect: _types_pb2.Rect2f
    label: Label
    line: _types_pb2.Line2f
    rect_with_text: RectWithText
    mask: Mask
    def __init__(
        self,
        color: _types_pb2.Color | str | None = ...,
        thickness: Figure.Thickness | str | None = ...,
        alpha: float | None = ...,
        rect: _types_pb2.Rect2f | _Mapping | None = ...,
        label: Label | _Mapping | None = ...,
        line: _types_pb2.Line2f | _Mapping | None = ...,
        rect_with_text: RectWithText | _Mapping | None = ...,
        mask: Mask | _Mapping | None = ...,
    ) -> None: ...

class Label(_message.Message):
    __slots__ = ("extents", "text")
    EXTENTS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    extents: _types_pb2.Rect2f
    text: str
    def __init__(
        self, extents: _types_pb2.Rect2f | _Mapping | None = ..., text: str | None = ...
    ) -> None: ...

class RectWithText(_message.Message):
    __slots__ = ("alignment", "rect", "text")
    class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        A_NONE: _ClassVar[RectWithText.Alignment]
        A_TOP_LEFT: _ClassVar[RectWithText.Alignment]
        A_TOP_CENTER: _ClassVar[RectWithText.Alignment]
        A_TOP_RIGHT: _ClassVar[RectWithText.Alignment]
        A_CENTER_LEFT: _ClassVar[RectWithText.Alignment]
        A_CENTER_CENTER: _ClassVar[RectWithText.Alignment]
        A_CENTER_RIGHT: _ClassVar[RectWithText.Alignment]
        A_BOTTOM_LEFT: _ClassVar[RectWithText.Alignment]
        A_BOTTOM_CENTER: _ClassVar[RectWithText.Alignment]
        A_BOTTOM_RIGHT: _ClassVar[RectWithText.Alignment]

    A_NONE: RectWithText.Alignment
    A_TOP_LEFT: RectWithText.Alignment
    A_TOP_CENTER: RectWithText.Alignment
    A_TOP_RIGHT: RectWithText.Alignment
    A_CENTER_LEFT: RectWithText.Alignment
    A_CENTER_CENTER: RectWithText.Alignment
    A_CENTER_RIGHT: RectWithText.Alignment
    A_BOTTOM_LEFT: RectWithText.Alignment
    A_BOTTOM_CENTER: RectWithText.Alignment
    A_BOTTOM_RIGHT: RectWithText.Alignment
    RECT_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    rect: _types_pb2.Rect2f
    text: str
    alignment: RectWithText.Alignment
    def __init__(
        self,
        rect: _types_pb2.Rect2f | _Mapping | None = ...,
        text: str | None = ...,
        alignment: RectWithText.Alignment | str | None = ...,
    ) -> None: ...

class Thumbnail(_message.Message):
    __slots__ = ("data", "format")
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[Thumbnail.Format]
        JPEG: _ClassVar[Thumbnail.Format]

    NONE: Thumbnail.Format
    JPEG: Thumbnail.Format
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    format: Thumbnail.Format
    data: bytes
    def __init__(
        self, format: Thumbnail.Format | str | None = ..., data: bytes | None = ...
    ) -> None: ...

class A(_message.Message):
    __slots__ = (
        "alarm",
        "duration_ms",
        "ended",
        "motion",
        "objects",
        "offline",
        "ring",
        "sound",
    )
    class Motion(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Sound(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Alarm(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Offline(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    class Objects(_message.Message):
        __slots__ = ("class_mask",)
        CLASS_MASK_FIELD_NUMBER: _ClassVar[int]
        class_mask: int
        def __init__(self, class_mask: int | None = ...) -> None: ...

    class Ring(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...

    MOTION_FIELD_NUMBER: _ClassVar[int]
    SOUND_FIELD_NUMBER: _ClassVar[int]
    ALARM_FIELD_NUMBER: _ClassVar[int]
    OFFLINE_FIELD_NUMBER: _ClassVar[int]
    OBJECTS_FIELD_NUMBER: _ClassVar[int]
    RING_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    ENDED_FIELD_NUMBER: _ClassVar[int]
    motion: A.Motion
    sound: A.Sound
    alarm: A.Alarm
    offline: A.Offline
    objects: A.Objects
    ring: A.Ring
    duration_ms: int
    ended: bool
    def __init__(
        self,
        motion: A.Motion | _Mapping | None = ...,
        sound: A.Sound | _Mapping | None = ...,
        alarm: A.Alarm | _Mapping | None = ...,
        offline: A.Offline | _Mapping | None = ...,
        objects: A.Objects | _Mapping | None = ...,
        ring: A.Ring | _Mapping | None = ...,
        duration_ms: int | None = ...,
        ended: bool = ...,
    ) -> None: ...

class Motion(_message.Message):
    __slots__ = ("detected", "mask")
    DETECTED_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    detected: bool
    mask: Mask
    def __init__(
        self, detected: bool = ..., mask: Mask | _Mapping | None = ...
    ) -> None: ...

class Mask(_message.Message):
    __slots__ = ("data", "height", "width")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    data: bytes
    def __init__(
        self,
        width: int | None = ...,
        height: int | None = ...,
        data: bytes | None = ...,
    ) -> None: ...

class Objects(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[DObject]
    def __init__(self, items: _Iterable[DObject | _Mapping] | None = ...) -> None: ...

class DObject(_message.Message):
    __slots__ = ("bbox", "confidence", "track")
    class Track(_message.Message):
        __slots__ = ("duration_ms", "id", "points")
        ID_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        id: int
        points: _containers.RepeatedCompositeFieldContainer[_types_pb2.Point2f]
        duration_ms: int
        def __init__(
            self,
            id: int | None = ...,
            points: _Iterable[_types_pb2.Point2f | _Mapping] | None = ...,
            duration_ms: int | None = ...,
        ) -> None: ...

    BBOX_FIELD_NUMBER: _ClassVar[int]
    CLASS_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    TRACK_FIELD_NUMBER: _ClassVar[int]
    bbox: _types_pb2.Rect2f
    confidence: int
    track: DObject.Track
    def __init__(
        self,
        bbox: _types_pb2.Rect2f | _Mapping | None = ...,
        confidence: int | None = ...,
        track: DObject.Track | _Mapping | None = ...,
        **kwargs,
    ) -> None: ...

class PirMotion(_message.Message):
    __slots__ = ("detected", "raw_pir_data")
    class RawPirData(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: bytes | None = ...) -> None: ...

    DETECTED_FIELD_NUMBER: _ClassVar[int]
    RAW_PIR_DATA_FIELD_NUMBER: _ClassVar[int]
    detected: bool
    raw_pir_data: PirMotion.RawPirData
    def __init__(
        self,
        detected: bool = ...,
        raw_pir_data: PirMotion.RawPirData | _Mapping | None = ...,
    ) -> None: ...

class Ring(_message.Message):
    __slots__ = ("detected",)
    DETECTED_FIELD_NUMBER: _ClassVar[int]
    detected: bool
    def __init__(self, detected: bool = ...) -> None: ...
