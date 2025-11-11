from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper

DESCRIPTOR: _descriptor.FileDescriptor

class X509Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    X509_VERSION_UNSPECIFIED: _ClassVar[X509Version]
    X509_VERSION_1: _ClassVar[X509Version]
    X509_VERSION_2: _ClassVar[X509Version]
    X509_VERSION_3: _ClassVar[X509Version]

X509_VERSION_UNSPECIFIED: X509Version
X509_VERSION_1: X509Version
X509_VERSION_2: X509Version
X509_VERSION_3: X509Version

class X509Certificate(_message.Message):
    __slots__ = ("alias", "id", "sha256_fingerprint", "used")
    ID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    SHA256_FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    USED_FIELD_NUMBER: _ClassVar[int]
    id: str
    alias: str
    sha256_fingerprint: str
    used: bool
    def __init__(
        self,
        id: str | None = ...,
        alias: str | None = ...,
        sha256_fingerprint: str | None = ...,
        used: bool = ...,
    ) -> None: ...
