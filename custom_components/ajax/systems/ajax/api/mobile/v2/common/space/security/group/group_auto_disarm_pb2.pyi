from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class FollowingGroupAutoDisarm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FOLLOWING_GROUP_AUTO_DISARM_UNSPECIFIED: _ClassVar[FollowingGroupAutoDisarm]
    FOLLOWING_GROUP_AUTO_DISARM_DISABLED: _ClassVar[FollowingGroupAutoDisarm]
    FOLLOWING_GROUP_AUTO_DISARM_ENABLED: _ClassVar[FollowingGroupAutoDisarm]

FOLLOWING_GROUP_AUTO_DISARM_UNSPECIFIED: FollowingGroupAutoDisarm
FOLLOWING_GROUP_AUTO_DISARM_DISABLED: FollowingGroupAutoDisarm
FOLLOWING_GROUP_AUTO_DISARM_ENABLED: FollowingGroupAutoDisarm
