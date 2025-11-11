from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class Country(_message.Message):
    __slots__ = ("code", "name")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    def __init__(self, code: str | None = ..., name: str | None = ...) -> None: ...

class GetCountriesRequest(_message.Message):
    __slots__ = ("locale",)
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    locale: str
    def __init__(self, locale: str | None = ...) -> None: ...

class GetCountriesResponse(_message.Message):
    __slots__ = ("countries", "locale")
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    COUNTRIES_FIELD_NUMBER: _ClassVar[int]
    locale: str
    countries: _containers.RepeatedCompositeFieldContainer[Country]
    def __init__(
        self,
        locale: str | None = ...,
        countries: _Iterable[Country | _Mapping] | None = ...,
    ) -> None: ...
