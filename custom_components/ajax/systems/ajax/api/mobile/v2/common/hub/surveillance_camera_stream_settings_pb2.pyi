from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class SurveillanceCameraStreamSettings(_message.Message):
    __slots__ = (
        "crc",
        "dahua_or_uniview_settings",
        "hikvision_or_safire_settings",
        "service_type",
        "stream_data_url",
    )
    class ServiceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NO_SERVICE_TYPE_INFO: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        RTSP_STREAM: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        XMEYE: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        HIKVISION: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        DAHUA: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        SAFIRE: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        UNIVIEW: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]
        IVIDEON: _ClassVar[SurveillanceCameraStreamSettings.ServiceType]

    NO_SERVICE_TYPE_INFO: SurveillanceCameraStreamSettings.ServiceType
    RTSP_STREAM: SurveillanceCameraStreamSettings.ServiceType
    XMEYE: SurveillanceCameraStreamSettings.ServiceType
    HIKVISION: SurveillanceCameraStreamSettings.ServiceType
    DAHUA: SurveillanceCameraStreamSettings.ServiceType
    SAFIRE: SurveillanceCameraStreamSettings.ServiceType
    UNIVIEW: SurveillanceCameraStreamSettings.ServiceType
    IVIDEON: SurveillanceCameraStreamSettings.ServiceType
    class HikvisionOrSafireSettings(_message.Message):
        __slots__ = (
            "area_domain",
            "auth_domain",
            "auth_id",
            "expire_date",
            "no",
            "refresh_token",
            "serial",
            "token",
            "verification_code",
        )
        AREA_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        AUTH_DOMAIN_FIELD_NUMBER: _ClassVar[int]
        AUTH_ID_FIELD_NUMBER: _ClassVar[int]
        EXPIRE_DATE_FIELD_NUMBER: _ClassVar[int]
        NO_FIELD_NUMBER: _ClassVar[int]
        REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
        area_domain: str
        auth_domain: str
        auth_id: str
        expire_date: _timestamp_pb2.Timestamp
        no: int
        refresh_token: str
        serial: str
        token: str
        verification_code: str
        def __init__(
            self,
            area_domain: str | None = ...,
            auth_domain: str | None = ...,
            auth_id: str | None = ...,
            expire_date: _timestamp_pb2.Timestamp | _Mapping | None = ...,
            no: int | None = ...,
            refresh_token: str | None = ...,
            serial: str | None = ...,
            token: str | None = ...,
            verification_code: str | None = ...,
        ) -> None: ...

    class DahuaOrUniviewSettings(_message.Message):
        __slots__ = ("login", "no", "password", "serial")
        LOGIN_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_FIELD_NUMBER: _ClassVar[int]
        SERIAL_FIELD_NUMBER: _ClassVar[int]
        NO_FIELD_NUMBER: _ClassVar[int]
        login: str
        password: str
        serial: str
        no: int
        def __init__(
            self,
            login: str | None = ...,
            password: str | None = ...,
            serial: str | None = ...,
            no: int | None = ...,
        ) -> None: ...

    SERVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    STREAM_DATA_URL_FIELD_NUMBER: _ClassVar[int]
    HIKVISION_OR_SAFIRE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    DAHUA_OR_UNIVIEW_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    service_type: SurveillanceCameraStreamSettings.ServiceType
    crc: int
    stream_data_url: str
    hikvision_or_safire_settings: (
        SurveillanceCameraStreamSettings.HikvisionOrSafireSettings
    )
    dahua_or_uniview_settings: SurveillanceCameraStreamSettings.DahuaOrUniviewSettings
    def __init__(
        self,
        service_type: SurveillanceCameraStreamSettings.ServiceType | str | None = ...,
        crc: int | None = ...,
        stream_data_url: str | None = ...,
        hikvision_or_safire_settings: SurveillanceCameraStreamSettings.HikvisionOrSafireSettings
        | _Mapping
        | None = ...,
        dahua_or_uniview_settings: SurveillanceCameraStreamSettings.DahuaOrUniviewSettings
        | _Mapping
        | None = ...,
    ) -> None: ...
