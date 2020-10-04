from fastapi import APIRouter, Depends, Query

from src.api.controller.elevation.dto.locations_input_dto import (
    LocationsInputDto,
    LocationPointInputDto,
)
from src.api.controller.elevation.dto.locations_output_dto import (
    ElevationsOutputDto,
    LocationPointElevationOutputDto,
)
from src.api.docs.openapi import (
    generate_validation_error_response,
    generate_unprocessable_entity_error_response,
)
from src.api.handler.error_response import ErrorResponse
from src.core.service.elevation_service import ElevationService

router = APIRouter()


@router.get(
    "",
    response_model=LocationPointElevationOutputDto,
    status_code=200,
    responses={
        200: {"model": LocationPointElevationOutputDto},
        400: {
            "model": ErrorResponse,
            "content": generate_validation_error_response(
                invalid_field_location=["query", "lat"]
            ),
        },
        422: {
            "model": ErrorResponse,
            "content": generate_unprocessable_entity_error_response(),
        },
    },
    response_model_exclude_none=True,
)
def get_elevation_from_location(
    lat: float = Query(
        ...,
        ge=-90,
        le=90,
        title="Latitude",
        description="Latitude",
        example="37.774929",
    ),
    long: float = Query(
        ...,
        ge=-180,
        le=180,
        title="Longitude",
        description="Longitude",
        example="-122.419418",
    ),
    elevation_service: ElevationService = Depends(ElevationService),
):
    input_model = LocationPointInputDto(name="Location", lat=lat, long=long)

    response_model = elevation_service.get_elevation_from_location(
        location_model=input_model.to_model()
    )

    return LocationPointElevationOutputDto.from_model(response_model)


@router.post(
    "",
    response_model=ElevationsOutputDto,
    status_code=200,
    responses={
        200: {"model": ElevationsOutputDto},
        400: {
            "model": ErrorResponse,
            "content": generate_validation_error_response(
                invalid_field_location=["body", "lat"]
            ),
        },
        422: {
            "model": ErrorResponse,
            "content": generate_unprocessable_entity_error_response(),
        },
    },
    response_model_exclude_none=True,
)
def get_elevations_from_locations(
    input_model: LocationsInputDto,
    elevation_service: ElevationService = Depends(ElevationService),
):

    response_model = elevation_service.get_elevations_from_locations(
        locations_model=input_model.to_model(), is_locations=input_model.is_locations
    )

    return ElevationsOutputDto.from_model(response_model)
