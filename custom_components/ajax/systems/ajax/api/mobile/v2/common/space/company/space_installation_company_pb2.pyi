from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.space.member import (
    display_member_permissions_pb2 as _display_member_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    space_permissions_pb2 as _space_permissions_pb2,
)
from systems.ajax.api.mobile.v2.common.space.member import (
    standalone_device_permissions_pb2 as _standalone_device_permissions_pb2,
)
from systems.ajax.api.mobile.v2.hubobject.model.company import (
    company_info_pb2 as _company_info_pb2,
)

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceInstallationCompany(_message.Message):
    __slots__ = (
        "company_info",
        "devices_permissions",
        "display_member_permissions",
        "hub_user_index",
        "permissions_expired_at",
        "space_member_id",
        "space_permissions",
        "type",
    )
    class InstallationCompanyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INSTALLATION_COMPANY_TYPE_UNSPECIFIED: _ClassVar[
            SpaceInstallationCompany.InstallationCompanyType
        ]
        INSTALLATION_COMPANY_TYPE_INSTALLATION: _ClassVar[
            SpaceInstallationCompany.InstallationCompanyType
        ]
        INSTALLATION_COMPANY_TYPE_SERVICE: _ClassVar[
            SpaceInstallationCompany.InstallationCompanyType
        ]

    INSTALLATION_COMPANY_TYPE_UNSPECIFIED: (
        SpaceInstallationCompany.InstallationCompanyType
    )
    INSTALLATION_COMPANY_TYPE_INSTALLATION: (
        SpaceInstallationCompany.InstallationCompanyType
    )
    INSTALLATION_COMPANY_TYPE_SERVICE: SpaceInstallationCompany.InstallationCompanyType
    COMPANY_INFO_FIELD_NUMBER: _ClassVar[int]
    SPACE_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEVICES_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_EXPIRED_AT_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_MEMBER_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    HUB_USER_INDEX_FIELD_NUMBER: _ClassVar[int]
    SPACE_MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    company_info: _company_info_pb2.CompanyInfo
    space_permissions: _space_permissions_pb2.SpacePermissions
    devices_permissions: _containers.RepeatedCompositeFieldContainer[
        _standalone_device_permissions_pb2.StandaloneDevicePermissions
    ]
    permissions_expired_at: _timestamp_pb2.Timestamp
    display_member_permissions: _display_member_permissions_pb2.DisplayMemberPermissions
    hub_user_index: int
    space_member_id: str
    type: SpaceInstallationCompany.InstallationCompanyType
    def __init__(
        self,
        company_info: _company_info_pb2.CompanyInfo | _Mapping | None = ...,
        space_permissions: _space_permissions_pb2.SpacePermissions
        | _Mapping
        | None = ...,
        devices_permissions: _Iterable[
            _standalone_device_permissions_pb2.StandaloneDevicePermissions | _Mapping
        ]
        | None = ...,
        permissions_expired_at: _timestamp_pb2.Timestamp | _Mapping | None = ...,
        display_member_permissions: _display_member_permissions_pb2.DisplayMemberPermissions
        | _Mapping
        | None = ...,
        hub_user_index: int | None = ...,
        space_member_id: str | None = ...,
        type: SpaceInstallationCompany.InstallationCompanyType | str | None = ...,
    ) -> None: ...
