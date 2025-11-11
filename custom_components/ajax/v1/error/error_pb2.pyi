from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorResponse(_message.Message):
    __slots__ = ("errors", "message")
    class Error(_message.Message):
        __slots__ = (
            "message",
            "message_parameters",
            "message_template",
            "property_index_path",
            "property_name_path",
            "resource",
        )
        class MessageParametersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(
                self, key: str | None = ..., value: str | None = ...
            ) -> None: ...

        RESOURCE_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_NAME_PATH_FIELD_NUMBER: _ClassVar[int]
        PROPERTY_INDEX_PATH_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        resource: str
        property_name_path: str
        property_index_path: str
        message_template: str
        message_parameters: _containers.ScalarMap[str, str]
        message: str
        def __init__(
            self,
            resource: str | None = ...,
            property_name_path: str | None = ...,
            property_index_path: str | None = ...,
            message_template: str | None = ...,
            message_parameters: _Mapping[str, str] | None = ...,
            message: str | None = ...,
        ) -> None: ...

    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    message: str
    errors: _containers.RepeatedCompositeFieldContainer[ErrorResponse.Error]
    def __init__(
        self,
        message: str | None = ...,
        errors: _Iterable[ErrorResponse.Error | _Mapping] | None = ...,
    ) -> None: ...

class ErrorId(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: str | None = ...) -> None: ...
