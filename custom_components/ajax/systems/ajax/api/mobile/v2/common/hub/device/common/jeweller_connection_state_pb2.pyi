from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class JewellerConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JEWELLER_CONNECTION_STATE_UNSPECIFIED: _ClassVar[JewellerConnectionState]
    JEWELLER_CONNECTION_STATE_OFFLINE: _ClassVar[JewellerConnectionState]
    JEWELLER_CONNECTION_STATE_ONLINE: _ClassVar[JewellerConnectionState]

JEWELLER_CONNECTION_STATE_UNSPECIFIED: JewellerConnectionState
JEWELLER_CONNECTION_STATE_OFFLINE: JewellerConnectionState
JEWELLER_CONNECTION_STATE_ONLINE: JewellerConnectionState
