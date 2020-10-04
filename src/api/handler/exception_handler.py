import traceback
from fastapi import HTTPException

from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from starlette import status
from starlette.responses import JSONResponse

from src.api.handler.error_response import ErrorResponse
from src.core.exception.application_exception import ApplicationException
from src.infra.util.errors import errors


def unhandled_exception_handler(request, exc: Exception):
    error_code = 1999
    print(generate_error_message(error_code), exc)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=generate_error_content(
            error_code=error_code, error_detail=[generate_stack_trace(exc)]
        ),
    )


def http_exception_handler_manual(exc: HTTPException):
    error_code = 1999

    # TODO : this case special exception should be thrown
    if status.HTTP_401_UNAUTHORIZED == exc.status_code:
        error_code = 1200

    if status.HTTP_403_FORBIDDEN == exc.status_code:
        error_code = 1201

    if status.HTTP_422_UNPROCESSABLE_ENTITY == exc.status_code:
        error_code = 1999

    print(generate_error_message(error_code), exc)

    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            ErrorResponse(error_code=error_code, error_message=str(exc.detail)).dict()
        ),
    )


def http_exception_handler(request, exc: HTTPException):
    error_code = 1999

    # TODO : this case special exception should be thrown
    if status.HTTP_401_UNAUTHORIZED == exc.status_code:
        error_code = 1200

    if status.HTTP_403_FORBIDDEN == exc.status_code:
        error_code = 1201

    print(generate_error_message(error_code), exc)

    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(
            ErrorResponse(
                error_code=error_code, error_message=errors[error_code]
            ).dict()
        ),
    )


def validation_exception_handler(request, exc: RequestValidationError):
    error_code = 1000
    print(generate_error_message(error_code), exc)
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=generate_error_content(
            error_code=error_code, error_detail=exc.errors()
        ),
    )


def application_exception_handler(request, exc: ApplicationException):
    print(generate_error_message(exc.error_code))
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            ErrorResponse(
                error_code=exc.error_code,
                error_message=exc.error_message,
                error_detail=[exc.exception],
            ).dict()
        ),
    )


def generate_error_message(error_code):
    return "error code: {}, error message: {}".format(error_code, errors[error_code])


def generate_stack_trace(exc: Exception) -> str:
    return "".join(traceback.TracebackException.from_exception(exc).format())


def generate_error_content(error_code: int, error_detail: list):
    return jsonable_encoder(
        ErrorResponse(
            error_code=error_code,
            error_message=errors[error_code],
            error_detail=error_detail,
        ).dict()
    )
