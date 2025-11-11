from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class PhotoPart(_message.Message):
    __slots__ = (
        "alarms_with_photo_verification",
        "available_photo_backlights",
        "available_photo_params",
        "capabilities",
        "hdr_image",
        "image_resolution",
        "photo_backlight",
        "photos_by_alarm",
        "photos_on_demand",
    )
    class ImageResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE_RESOLUTION_UNSPECIFIED: _ClassVar[PhotoPart.ImageResolution]
        IMAGE_RESOLUTION_160X120: _ClassVar[PhotoPart.ImageResolution]
        IMAGE_RESOLUTION_320X240: _ClassVar[PhotoPart.ImageResolution]
        IMAGE_RESOLUTION_960X720: _ClassVar[PhotoPart.ImageResolution]
        IMAGE_RESOLUTION_640X480: _ClassVar[PhotoPart.ImageResolution]

    IMAGE_RESOLUTION_UNSPECIFIED: PhotoPart.ImageResolution
    IMAGE_RESOLUTION_160X120: PhotoPart.ImageResolution
    IMAGE_RESOLUTION_320X240: PhotoPart.ImageResolution
    IMAGE_RESOLUTION_960X720: PhotoPart.ImageResolution
    IMAGE_RESOLUTION_640X480: PhotoPart.ImageResolution
    class HdrImage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HDR_IMAGE_UNSPECIFIED: _ClassVar[PhotoPart.HdrImage]
        HDR_IMAGE_OFF: _ClassVar[PhotoPart.HdrImage]
        HDR_IMAGE_ON: _ClassVar[PhotoPart.HdrImage]

    HDR_IMAGE_UNSPECIFIED: PhotoPart.HdrImage
    HDR_IMAGE_OFF: PhotoPart.HdrImage
    HDR_IMAGE_ON: PhotoPart.HdrImage
    class Capability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CAPABILITY_UNSPECIFIED: _ClassVar[PhotoPart.Capability]
        CAPABILITY_PHOD: _ClassVar[PhotoPart.Capability]
        CAPABILITY_HDR: _ClassVar[PhotoPart.Capability]
        CAPABILITY_PHOD_COUNT_SETTING: _ClassVar[PhotoPart.Capability]
        CAPABILITY_ALARMS_WITH_PHOTO_VERIFICATION: _ClassVar[PhotoPart.Capability]
        CAPABILITY_PHOTO_BACKLIGHT: _ClassVar[PhotoPart.Capability]

    CAPABILITY_UNSPECIFIED: PhotoPart.Capability
    CAPABILITY_PHOD: PhotoPart.Capability
    CAPABILITY_HDR: PhotoPart.Capability
    CAPABILITY_PHOD_COUNT_SETTING: PhotoPart.Capability
    CAPABILITY_ALARMS_WITH_PHOTO_VERIFICATION: PhotoPart.Capability
    CAPABILITY_PHOTO_BACKLIGHT: PhotoPart.Capability
    class PhotoBacklight(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHOTO_BACKLIGHT_UNSPECIFIED: _ClassVar[PhotoPart.PhotoBacklight]
        PHOTO_BACKLIGHT_OPEN_SPACE: _ClassVar[PhotoPart.PhotoBacklight]
        PHOTO_BACKLIGHT_ALONG_RIGHT_WALL: _ClassVar[PhotoPart.PhotoBacklight]
        PHOTO_BACKLIGHT_ALONG_LEFT_WALL: _ClassVar[PhotoPart.PhotoBacklight]

    PHOTO_BACKLIGHT_UNSPECIFIED: PhotoPart.PhotoBacklight
    PHOTO_BACKLIGHT_OPEN_SPACE: PhotoPart.PhotoBacklight
    PHOTO_BACKLIGHT_ALONG_RIGHT_WALL: PhotoPart.PhotoBacklight
    PHOTO_BACKLIGHT_ALONG_LEFT_WALL: PhotoPart.PhotoBacklight
    class PhotoPartSettings(_message.Message):
        __slots__ = (
            "alarms_with_photo_verification",
            "hdr_image",
            "image_resolution",
            "photo_backlight",
            "photos_by_alarm",
            "photos_on_demand",
        )
        IMAGE_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ALARMS_WITH_PHOTO_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
        PHOTOS_BY_ALARM_FIELD_NUMBER: _ClassVar[int]
        PHOTOS_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
        HDR_IMAGE_FIELD_NUMBER: _ClassVar[int]
        PHOTO_BACKLIGHT_FIELD_NUMBER: _ClassVar[int]
        image_resolution: PhotoPart.ImageResolution
        alarms_with_photo_verification: PhotoPart.AlarmsWithPhotoVerification
        photos_by_alarm: int
        photos_on_demand: int
        hdr_image: PhotoPart.HdrImage
        photo_backlight: PhotoPart.PhotoBacklight
        def __init__(
            self,
            image_resolution: PhotoPart.ImageResolution | str | None = ...,
            alarms_with_photo_verification: PhotoPart.AlarmsWithPhotoVerification
            | _Mapping
            | None = ...,
            photos_by_alarm: int | None = ...,
            photos_on_demand: int | None = ...,
            hdr_image: PhotoPart.HdrImage | str | None = ...,
            photo_backlight: PhotoPart.PhotoBacklight | str | None = ...,
        ) -> None: ...

    class AlarmsWithPhotoVerification(_message.Message):
        __slots__ = ("alarms_with_photo_verification", "all")
        class All(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...

        ALARMS_WITH_PHOTO_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
        ALL_FIELD_NUMBER: _ClassVar[int]
        alarms_with_photo_verification: int
        all: PhotoPart.AlarmsWithPhotoVerification.All
        def __init__(
            self,
            alarms_with_photo_verification: int | None = ...,
            all: PhotoPart.AlarmsWithPhotoVerification.All | _Mapping | None = ...,
        ) -> None: ...

    class AvailablePhotoParams(_message.Message):
        __slots__ = ("image_resolution", "max_photo_by_alarm", "max_photo_on_demand")
        IMAGE_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        MAX_PHOTO_BY_ALARM_FIELD_NUMBER: _ClassVar[int]
        MAX_PHOTO_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
        image_resolution: PhotoPart.ImageResolution
        max_photo_by_alarm: int
        max_photo_on_demand: int
        def __init__(
            self,
            image_resolution: PhotoPart.ImageResolution | str | None = ...,
            max_photo_by_alarm: int | None = ...,
            max_photo_on_demand: int | None = ...,
        ) -> None: ...

    IMAGE_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    ALARMS_WITH_PHOTO_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_BY_ALARM_FIELD_NUMBER: _ClassVar[int]
    PHOTOS_ON_DEMAND_FIELD_NUMBER: _ClassVar[int]
    HDR_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_PHOTO_PARAMS_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_PHOTO_BACKLIGHTS_FIELD_NUMBER: _ClassVar[int]
    PHOTO_BACKLIGHT_FIELD_NUMBER: _ClassVar[int]
    image_resolution: PhotoPart.ImageResolution
    alarms_with_photo_verification: PhotoPart.AlarmsWithPhotoVerification
    photos_by_alarm: int
    photos_on_demand: int
    hdr_image: PhotoPart.HdrImage
    capabilities: _containers.RepeatedScalarFieldContainer[PhotoPart.Capability]
    available_photo_params: _containers.RepeatedCompositeFieldContainer[
        PhotoPart.AvailablePhotoParams
    ]
    available_photo_backlights: _containers.RepeatedScalarFieldContainer[
        PhotoPart.PhotoBacklight
    ]
    photo_backlight: PhotoPart.PhotoBacklight
    def __init__(
        self,
        image_resolution: PhotoPart.ImageResolution | str | None = ...,
        alarms_with_photo_verification: PhotoPart.AlarmsWithPhotoVerification
        | _Mapping
        | None = ...,
        photos_by_alarm: int | None = ...,
        photos_on_demand: int | None = ...,
        hdr_image: PhotoPart.HdrImage | str | None = ...,
        capabilities: _Iterable[PhotoPart.Capability | str] | None = ...,
        available_photo_params: _Iterable[PhotoPart.AvailablePhotoParams | _Mapping]
        | None = ...,
        available_photo_backlights: _Iterable[PhotoPart.PhotoBacklight | str]
        | None = ...,
        photo_backlight: PhotoPart.PhotoBacklight | str | None = ...,
    ) -> None: ...
