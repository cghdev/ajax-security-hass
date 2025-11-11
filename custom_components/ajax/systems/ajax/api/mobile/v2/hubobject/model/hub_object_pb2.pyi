from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.hub import (
    hub_connection_properties_pb2 as _hub_connection_properties_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.company.installation import (
    installation_company_pb2 as _installation_company_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.company.monitoring import (
    monitoring_company_pb2 as _monitoring_company_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.company.privacy import (
    photo_on_demand_company_access_pb2 as _photo_on_demand_company_access_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.company.privacy import (
    privacy_override_pb2 as _privacy_override_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.company.privacy import (
    surveillance_cameras_company_access_pb2 as _surveillance_cameras_company_access_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.firmware import (
    device_firmware_update_pb2 as _device_firmware_update_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.firmware import (
    system_firmware_update_pb2 as _system_firmware_update_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class HubObject(_message.Message):
    __slots__ = (
        "device_firmware_updates",
        "hex_id",
        "hub_connection_properties",
        "installation_companies",
        "monitoring_companies",
        "photo_on_demand_companies_access",
        "privacy_overrides",
        "sim_card",
        "surveillance_cameras_companies_access",
        "system_firmware_update",
    )
    class InstallationCompanies(_message.Message):
        __slots__ = ("installation_company",)
        INSTALLATION_COMPANY_FIELD_NUMBER: _ClassVar[int]
        installation_company: _containers.RepeatedCompositeFieldContainer[
            _installation_company_pb2.InstallationCompany
        ]
        def __init__(
            self,
            installation_company: _Iterable[
                _installation_company_pb2.InstallationCompany | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class MonitoringCompanies(_message.Message):
        __slots__ = ("monitoring_company",)
        MONITORING_COMPANY_FIELD_NUMBER: _ClassVar[int]
        monitoring_company: _containers.RepeatedCompositeFieldContainer[
            _monitoring_company_pb2.MonitoringCompany
        ]
        def __init__(
            self,
            monitoring_company: _Iterable[
                _monitoring_company_pb2.MonitoringCompany | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class PhotoOnDemandCompaniesAccess(_message.Message):
        __slots__ = ("company_access",)
        COMPANY_ACCESS_FIELD_NUMBER: _ClassVar[int]
        company_access: _containers.RepeatedCompositeFieldContainer[
            _photo_on_demand_company_access_pb2.PhotoOnDemandCompanyAccess
        ]
        def __init__(
            self,
            company_access: _Iterable[
                _photo_on_demand_company_access_pb2.PhotoOnDemandCompanyAccess
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class SurveillanceCamerasCompaniesAccess(_message.Message):
        __slots__ = ("company_access",)
        COMPANY_ACCESS_FIELD_NUMBER: _ClassVar[int]
        company_access: _containers.RepeatedCompositeFieldContainer[
            _surveillance_cameras_company_access_pb2.SurveillanceCamerasCompanyAccess
        ]
        def __init__(
            self,
            company_access: _Iterable[
                _surveillance_cameras_company_access_pb2.SurveillanceCamerasCompanyAccess
                | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class PrivacyOverrides(_message.Message):
        __slots__ = ("privacy_override",)
        PRIVACY_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
        privacy_override: _containers.RepeatedCompositeFieldContainer[
            _privacy_override_pb2.PrivacyOverride
        ]
        def __init__(
            self,
            privacy_override: _Iterable[
                _privacy_override_pb2.PrivacyOverride | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class DeviceFirmwareUpdates(_message.Message):
        __slots__ = ("device_firmware_update",)
        DEVICE_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
        device_firmware_update: _containers.RepeatedCompositeFieldContainer[
            _device_firmware_update_pb2.DeviceFirmwareUpdate
        ]
        def __init__(
            self,
            device_firmware_update: _Iterable[
                _device_firmware_update_pb2.DeviceFirmwareUpdate | _Mapping
            ]
            | None = ...,
        ) -> None: ...

    class SimCard(_message.Message):
        __slots__ = ("active_sim_card", "deactivation_date", "imei", "sim_card_status")
        class SimCardStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SIM_CARD_STATUS_NO_INFO: _ClassVar[HubObject.SimCard.SimCardStatus]
            SIM_CARD_STATUS_INACTIVE: _ClassVar[HubObject.SimCard.SimCardStatus]
            SIM_CARD_STATUS_ACTIVE: _ClassVar[HubObject.SimCard.SimCardStatus]

        SIM_CARD_STATUS_NO_INFO: HubObject.SimCard.SimCardStatus
        SIM_CARD_STATUS_INACTIVE: HubObject.SimCard.SimCardStatus
        SIM_CARD_STATUS_ACTIVE: HubObject.SimCard.SimCardStatus
        ACTIVE_SIM_CARD_FIELD_NUMBER: _ClassVar[int]
        SIM_CARD_STATUS_FIELD_NUMBER: _ClassVar[int]
        IMEI_FIELD_NUMBER: _ClassVar[int]
        DEACTIVATION_DATE_FIELD_NUMBER: _ClassVar[int]
        active_sim_card: int
        sim_card_status: HubObject.SimCard.SimCardStatus
        imei: str
        deactivation_date: _timestamp_pb2.Timestamp
        def __init__(
            self,
            active_sim_card: int | None = ...,
            sim_card_status: HubObject.SimCard.SimCardStatus | str | None = ...,
            imei: str | None = ...,
            deactivation_date: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        ) -> None: ...

    HEX_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    MONITORING_COMPANIES_FIELD_NUMBER: _ClassVar[int]
    PHOTO_ON_DEMAND_COMPANIES_ACCESS_FIELD_NUMBER: _ClassVar[int]
    SURVEILLANCE_CAMERAS_COMPANIES_ACCESS_FIELD_NUMBER: _ClassVar[int]
    PRIVACY_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    SIM_CARD_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIRMWARE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIRMWARE_UPDATE_FIELD_NUMBER: _ClassVar[int]
    HUB_CONNECTION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    hex_id: str
    installation_companies: HubObject.InstallationCompanies
    monitoring_companies: HubObject.MonitoringCompanies
    photo_on_demand_companies_access: HubObject.PhotoOnDemandCompaniesAccess
    surveillance_cameras_companies_access: HubObject.SurveillanceCamerasCompaniesAccess
    privacy_overrides: HubObject.PrivacyOverrides
    sim_card: HubObject.SimCard
    device_firmware_updates: HubObject.DeviceFirmwareUpdates
    system_firmware_update: _system_firmware_update_pb2.SystemFirmwareUpdate
    hub_connection_properties: _hub_connection_properties_pb2.HubConnectionProperties
    def __init__(
        self,
        hex_id: str | None = ...,
        installation_companies: HubObject.InstallationCompanies | _Mapping | None = ...,
        monitoring_companies: HubObject.MonitoringCompanies | _Mapping | None = ...,
        photo_on_demand_companies_access: HubObject.PhotoOnDemandCompaniesAccess
        | _Mapping
        | None = ...,
        surveillance_cameras_companies_access: HubObject.SurveillanceCamerasCompaniesAccess
        | _Mapping
        | None = ...,
        privacy_overrides: HubObject.PrivacyOverrides | _Mapping | None = ...,
        sim_card: HubObject.SimCard | _Mapping | None = ...,
        device_firmware_updates: HubObject.DeviceFirmwareUpdates
        | _Mapping
        | None = ...,
        system_firmware_update: _system_firmware_update_pb2.SystemFirmwareUpdate
        | _Mapping
        | None = ...,
        hub_connection_properties: _hub_connection_properties_pb2.HubConnectionProperties
        | _Mapping
        | None = ...,
    ) -> None: ...
