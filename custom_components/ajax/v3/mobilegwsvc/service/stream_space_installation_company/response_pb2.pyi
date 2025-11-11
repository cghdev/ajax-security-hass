from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from systems.ajax.api.mobile.v2.common.space.company import (
    space_installation_company_pb2 as _space_installation_company_pb2,
)
from v3.mobilegwsvc.commonmodels.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class StreamSpaceInstallationCompanyResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Success(_message.Message):
        __slots__ = ("snapshot", "update")
        class Snapshot(_message.Message):
            __slots__ = ("space_installation_company",)
            SPACE_INSTALLATION_COMPANY_FIELD_NUMBER: _ClassVar[int]
            space_installation_company: (
                _space_installation_company_pb2.SpaceInstallationCompany
            )
            def __init__(
                self,
                space_installation_company: _space_installation_company_pb2.SpaceInstallationCompany
                | _Mapping
                | None = ...,
            ) -> None: ...

        class Update(_message.Message):
            __slots__ = ("space_installation_company", "update_type")
            class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UPDATE_TYPE_UNSPECIFIED: _ClassVar[
                    StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
                ]
                UPDATE_TYPE_UPDATE: _ClassVar[
                    StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
                ]
                UPDATE_TYPE_REMOVE: _ClassVar[
                    StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
                ]

            UPDATE_TYPE_UNSPECIFIED: (
                StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
            )
            UPDATE_TYPE_UPDATE: (
                StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
            )
            UPDATE_TYPE_REMOVE: (
                StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
            )
            SPACE_INSTALLATION_COMPANY_FIELD_NUMBER: _ClassVar[int]
            UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
            space_installation_company: (
                _space_installation_company_pb2.SpaceInstallationCompany
            )
            update_type: (
                StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
            )
            def __init__(
                self,
                space_installation_company: _space_installation_company_pb2.SpaceInstallationCompany
                | _Mapping
                | None = ...,
                update_type: StreamSpaceInstallationCompanyResponse.Success.Update.UpdateType
                | str
                | None = ...,
            ) -> None: ...

        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        UPDATE_FIELD_NUMBER: _ClassVar[int]
        snapshot: StreamSpaceInstallationCompanyResponse.Success.Snapshot
        update: StreamSpaceInstallationCompanyResponse.Success.Update
        def __init__(
            self,
            snapshot: StreamSpaceInstallationCompanyResponse.Success.Snapshot
            | _Mapping
            | None = ...,
            update: StreamSpaceInstallationCompanyResponse.Success.Update
            | _Mapping
            | None = ...,
        ) -> None: ...

    class Failure(_message.Message):
        __slots__ = ("bad_request", "permission_denied")
        BAD_REQUEST_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_FIELD_NUMBER: _ClassVar[int]
        bad_request: _response_pb2.Error
        permission_denied: _response_pb2.Error
        def __init__(
            self,
            bad_request: _response_pb2.Error | _Mapping | None = ...,
            permission_denied: _response_pb2.Error | _Mapping | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: StreamSpaceInstallationCompanyResponse.Success
    failure: StreamSpaceInstallationCompanyResponse.Failure
    def __init__(
        self,
        success: StreamSpaceInstallationCompanyResponse.Success | _Mapping | None = ...,
        failure: StreamSpaceInstallationCompanyResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
