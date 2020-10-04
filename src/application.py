from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from src.api.controller.cache import cache_controller
from src.api.controller.common import common_controller
from src.api.controller.elevation import elevation_controller

from src.api.handler.exception_handler import (
    http_exception_handler,
    validation_exception_handler,
    application_exception_handler,
    unhandled_exception_handler,
)
from src.api.middleware.request_response_middleware import RequestResponseMiddleware
from src.core.exception.application_exception import ApplicationException


def create_app():
    app = FastAPI(
        title="Elevation API",
        description="Find out elevation information with Elevation API",
        version="0.1.0",
        openapi_url="/openapi.json",
        docs_url="/",
        redoc_url="/redoc",
    )

    app.add_exception_handler(Exception, unhandled_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(ApplicationException, application_exception_handler)
    app.add_middleware(RequestResponseMiddleware)

    app.include_router(
        common_controller.router, prefix="/api/v1/common", tags=["common"]
    )
    app.include_router(cache_controller.router, prefix="/api/v1/cache", tags=["cache"])
    app.include_router(elevation_controller.router, prefix="/api/v1/elevations", tags=["elevation"])

    return app
