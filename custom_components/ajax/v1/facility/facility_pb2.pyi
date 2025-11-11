from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from v1.common import address_pb2 as _address_pb2
from v1.common import email_address_pb2 as _email_address_pb2
from v1.common import phone_number_pb2 as _phone_number_pb2
from v1.facility import (
    facility_monitoring_status_pb2 as _facility_monitoring_status_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class Facility(_message.Message):
    __slots__ = (
        "company_id",
        "connection_status",
        "facility_general_info",
        "hub_id",
        "hub_locked_by_company",
        "hub_name",
        "id",
        "monitoring_status",
        "privacy_override_status",
        "sleep_until",
        "space_id",
        "status",
        "version",
    )
    class ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFFLINE: _ClassVar[Facility.ConnectionStatus]
        ONLINE: _ClassVar[Facility.ConnectionStatus]

    OFFLINE: Facility.ConnectionStatus
    ONLINE: Facility.ConnectionStatus
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MONITORING_APPROVED: _ClassVar[Facility.Status]
        MONITORING_REQUESTED: _ClassVar[Facility.Status]
        IN_SLEEP_MODE: _ClassVar[Facility.Status]
        NO_MONITORING: _ClassVar[Facility.Status]

    MONITORING_APPROVED: Facility.Status
    MONITORING_REQUESTED: Facility.Status
    IN_SLEEP_MODE: Facility.Status
    NO_MONITORING: Facility.Status
    class PrivacyOverrideStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIVACY_OVERRIDE_STATUS_UNSPECIFIED: _ClassVar[Facility.PrivacyOverrideStatus]
        PRIVACY_OVERRIDE_STATUS_DISABLED: _ClassVar[Facility.PrivacyOverrideStatus]
        PRIVACY_OVERRIDE_STATUS_ENABLED: _ClassVar[Facility.PrivacyOverrideStatus]

    PRIVACY_OVERRIDE_STATUS_UNSPECIFIED: Facility.PrivacyOverrideStatus
    PRIVACY_OVERRIDE_STATUS_DISABLED: Facility.PrivacyOverrideStatus
    PRIVACY_OVERRIDE_STATUS_ENABLED: Facility.PrivacyOverrideStatus
    class GeneralInfo(_message.Message):
        __slots__ = (
            "address",
            "email_addresses",
            "name",
            "phone_numbers",
            "registration_number",
        )
        NAME_FIELD_NUMBER: _ClassVar[int]
        REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
        name: str
        registration_number: str
        address: _address_pb2.Address
        phone_numbers: _containers.RepeatedCompositeFieldContainer[
            _phone_number_pb2.PhoneNumber
        ]
        email_addresses: _containers.RepeatedCompositeFieldContainer[
            _email_address_pb2.EmailAddress
        ]
        def __init__(
            self,
            name: str | None = ...,
            registration_number: str | None = ...,
            address: _address_pb2.Address | _Mapping | None = ...,
            phone_numbers: _Iterable[_phone_number_pb2.PhoneNumber | _Mapping]
            | None = ...,
            email_addresses: _Iterable[_email_address_pb2.EmailAddress | _Mapping]
            | None = ...,
        ) -> None: ...

    class Note(_message.Message):
        __slots__ = ("facility_id", "id", "index", "text", "version")
        ID_FIELD_NUMBER: _ClassVar[int]
        FACILITY_ID_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        id: str
        facility_id: str
        text: str
        version: int
        index: int
        def __init__(
            self,
            id: str | None = ...,
            facility_id: str | None = ...,
            text: str | None = ...,
            version: int | None = ...,
            index: int | None = ...,
        ) -> None: ...

    ID_FIELD_NUMBER: _ClassVar[int]
    HUB_ID_FIELD_NUMBER: _ClassVar[int]
    HUB_NAME_FIELD_NUMBER: _ClassVar[int]
    COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
    FACILITY_GENERAL_INFO_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    HUB_LOCKED_BY_COMPANY_FIELD_NUMBER: _ClassVar[int]
    SLEEP_UNTIL_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OVERRIDE_STATUS_FIELD_NUMBER: _ClassVar[int]
    MONITORING_STATUS_FIELD_NUMBER: _ClassVar[int]
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    hub_id: str
    hub_name: str
    company_id: str
    facility_general_info: Facility.GeneralInfo
    status: Facility.Status
    connection_status: Facility.ConnectionStatus
    version: int
    hub_locked_by_company: bool
    sleep_until: _timestamp_pb2.Timestamp
    privacy_override_status: Facility.PrivacyOverrideStatus
    monitoring_status: _facility_monitoring_status_pb2.MonitoringStatus
    space_id: str
    def __init__(
        self,
        id: str | None = ...,
        hub_id: str | None = ...,
        hub_name: str | None = ...,
        company_id: str | None = ...,
        facility_general_info: Facility.GeneralInfo | _Mapping | None = ...,
        status: Facility.Status | str | None = ...,
        connection_status: Facility.ConnectionStatus | str | None = ...,
        version: int | None = ...,
        hub_locked_by_company: bool = ...,
        sleep_until: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        privacy_override_status: Facility.PrivacyOverrideStatus | str | None = ...,
        monitoring_status: _facility_monitoring_status_pb2.MonitoringStatus
        | str
        | None = ...,
        space_id: str | None = ...,
    ) -> None: ...
