from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceDeactivationPendingStatus(
    int, metaclass=_enum_type_wrapper.EnumTypeWrapper
):
    __slots__ = ()
    SERVICE_DEACTIVATION_PENDING_STATUS_UNSPECIFIED: _ClassVar[
        ServiceDeactivationPendingStatus
    ]
    SERVICE_DEACTIVATION_PENDING_STATUS_PENDING: _ClassVar[
        ServiceDeactivationPendingStatus
    ]
    SERVICE_DEACTIVATION_PENDING_STATUS_NONE: _ClassVar[
        ServiceDeactivationPendingStatus
    ]

SERVICE_DEACTIVATION_PENDING_STATUS_UNSPECIFIED: ServiceDeactivationPendingStatus
SERVICE_DEACTIVATION_PENDING_STATUS_PENDING: ServiceDeactivationPendingStatus
SERVICE_DEACTIVATION_PENDING_STATUS_NONE: ServiceDeactivationPendingStatus
