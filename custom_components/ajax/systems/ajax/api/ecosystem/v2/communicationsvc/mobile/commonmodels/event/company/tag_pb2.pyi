from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message

DESCRIPTOR: _descriptor.FileDescriptor

class InstallationCompanyInvited(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InstallationCompanyRemoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PermanentPermissionsRequested(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TemporaryPermissionsRequested(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedPermanentPermissionsApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedTemporaryPermissionsApproved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RequestedPermissionsRejected(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MonitoringCompanyInvited(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MonitoringCompanyRemoved(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CompanyEventTag(_message.Message):
    __slots__ = (
        "installation_company_invited",
        "installation_company_removed",
        "monitoring_company_invited",
        "monitoring_company_removed",
        "permanent_permissions_requested",
        "requested_permanent_permissions_approved",
        "requested_permissions_rejected",
        "requested_temporary_permissions_approved",
        "temporary_permissions_requested",
    )
    INSTALLATION_COMPANY_INVITED_FIELD_NUMBER: _ClassVar[int]
    INSTALLATION_COMPANY_REMOVED_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_PERMISSIONS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_PERMISSIONS_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_PERMANENT_PERMISSIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TEMPORARY_PERMISSIONS_APPROVED_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_PERMISSIONS_REJECTED_FIELD_NUMBER: _ClassVar[int]
    MONITORING_COMPANY_INVITED_FIELD_NUMBER: _ClassVar[int]
    MONITORING_COMPANY_REMOVED_FIELD_NUMBER: _ClassVar[int]
    installation_company_invited: InstallationCompanyInvited
    installation_company_removed: InstallationCompanyRemoved
    permanent_permissions_requested: PermanentPermissionsRequested
    temporary_permissions_requested: TemporaryPermissionsRequested
    requested_permanent_permissions_approved: RequestedPermanentPermissionsApproved
    requested_temporary_permissions_approved: RequestedTemporaryPermissionsApproved
    requested_permissions_rejected: RequestedPermissionsRejected
    monitoring_company_invited: MonitoringCompanyInvited
    monitoring_company_removed: MonitoringCompanyRemoved
    def __init__(
        self,
        installation_company_invited: InstallationCompanyInvited
        | _Mapping
        | None = ...,
        installation_company_removed: InstallationCompanyRemoved
        | _Mapping
        | None = ...,
        permanent_permissions_requested: PermanentPermissionsRequested
        | _Mapping
        | None = ...,
        temporary_permissions_requested: TemporaryPermissionsRequested
        | _Mapping
        | None = ...,
        requested_permanent_permissions_approved: RequestedPermanentPermissionsApproved
        | _Mapping
        | None = ...,
        requested_temporary_permissions_approved: RequestedTemporaryPermissionsApproved
        | _Mapping
        | None = ...,
        requested_permissions_rejected: RequestedPermissionsRejected
        | _Mapping
        | None = ...,
        monitoring_company_invited: MonitoringCompanyInvited | _Mapping | None = ...,
        monitoring_company_removed: MonitoringCompanyRemoved | _Mapping | None = ...,
    ) -> None: ...
