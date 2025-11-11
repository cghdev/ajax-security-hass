from collections.abc import Iterable as _Iterable
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from systems.ajax.api.mobile.v2.common.image import image_pb2 as _image_pb2
from systems.ajax.api.mobile.v2.common.response import response_pb2 as _response_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class InitiateUserDeletionRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class InitiateUserDeletionResponse(_message.Message):
    __slots__ = ("failure", "success")
    class Failure(_message.Message):
        __slots__ = (
            "cannot_send_confirmation_codes",
            "protected_from_deletion_due_to_spaces",
            "user_is_employee_in_companies",
            "user_is_owner_in_companies",
            "user_not_found",
        )
        class ProtectedFromDeletionDueToCompaniesError(_message.Message):
            __slots__ = ("companies",)
            class Company(_message.Message):
                __slots__ = ("company_id", "image", "name")
                COMPANY_ID_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                company_id: str
                name: str
                image: _image_pb2.Images
                def __init__(
                    self,
                    company_id: str | None = ...,
                    name: str | None = ...,
                    image: _image_pb2.Images | _Mapping | None = ...,
                ) -> None: ...

            COMPANIES_FIELD_NUMBER: _ClassVar[int]
            companies: _containers.RepeatedCompositeFieldContainer[
                InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToCompaniesError.Company
            ]
            def __init__(
                self,
                companies: _Iterable[
                    InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToCompaniesError.Company
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        class ProtectedFromDeletionDueToSpacesError(_message.Message):
            __slots__ = ("last_user_in_spaces",)
            class Space(_message.Message):
                __slots__ = ("image", "name", "space_id")
                SPACE_ID_FIELD_NUMBER: _ClassVar[int]
                NAME_FIELD_NUMBER: _ClassVar[int]
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                space_id: str
                name: str
                image: _image_pb2.Images
                def __init__(
                    self,
                    space_id: str | None = ...,
                    name: str | None = ...,
                    image: _image_pb2.Images | _Mapping | None = ...,
                ) -> None: ...

            LAST_USER_IN_SPACES_FIELD_NUMBER: _ClassVar[int]
            last_user_in_spaces: _containers.RepeatedCompositeFieldContainer[
                InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToSpacesError.Space
            ]
            def __init__(
                self,
                last_user_in_spaces: _Iterable[
                    InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToSpacesError.Space
                    | _Mapping
                ]
                | None = ...,
            ) -> None: ...

        USER_NOT_FOUND_FIELD_NUMBER: _ClassVar[int]
        USER_IS_OWNER_IN_COMPANIES_FIELD_NUMBER: _ClassVar[int]
        USER_IS_EMPLOYEE_IN_COMPANIES_FIELD_NUMBER: _ClassVar[int]
        PROTECTED_FROM_DELETION_DUE_TO_SPACES_FIELD_NUMBER: _ClassVar[int]
        CANNOT_SEND_CONFIRMATION_CODES_FIELD_NUMBER: _ClassVar[int]
        user_not_found: _response_pb2.DefaultError
        user_is_owner_in_companies: InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToCompaniesError
        user_is_employee_in_companies: InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToCompaniesError
        protected_from_deletion_due_to_spaces: (
            InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToSpacesError
        )
        cannot_send_confirmation_codes: _response_pb2.DefaultError
        def __init__(
            self,
            user_not_found: _response_pb2.DefaultError | _Mapping | None = ...,
            user_is_owner_in_companies: InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToCompaniesError
            | _Mapping
            | None = ...,
            user_is_employee_in_companies: InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToCompaniesError
            | _Mapping
            | None = ...,
            protected_from_deletion_due_to_spaces: InitiateUserDeletionResponse.Failure.ProtectedFromDeletionDueToSpacesError
            | _Mapping
            | None = ...,
            cannot_send_confirmation_codes: _response_pb2.DefaultError
            | _Mapping
            | None = ...,
        ) -> None: ...

    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    success: _response_pb2.Success
    failure: InitiateUserDeletionResponse.Failure
    def __init__(
        self,
        success: _response_pb2.Success | _Mapping | None = ...,
        failure: InitiateUserDeletionResponse.Failure | _Mapping | None = ...,
    ) -> None: ...
