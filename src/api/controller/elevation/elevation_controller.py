import pandas as pd
from fastapi import APIRouter, Depends, Query, File, UploadFile

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
from src.core.exception.application_exception import ApplicationException
from src.core.service.elevation.elevation_service import ElevationService

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


@router.post(
    "-from-file",
    response_model=None,
    status_code=200,
    responses={
        200: {"model": None},
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
def get_elevations_from_file(
    file: UploadFile = File(
        ...,
    ),
    elevation_service: ElevationService = Depends(ElevationService),
):
    """

    :param file: \n
        csv file should be 3 columns. that's delimiter should be ;. \n
        file don't include headers (columns names). \n
        First column should be name. \n
        Second column should be latitude. Latitude should be between -90 and 90 \n
        Third column should be longitude. Longitude should be between -180 and 180 \n
        If location interval rule have not, API does not calculate for these item. \n
        For example (File Content);
            loc-1;37.34;32.23
            loc-1;36.34;34.23
            loc-2;37.35;36.24
            loc-3;33.36;35.25
    """

    if str(file.filename).endswith(".csv") is False:
        return ApplicationException(error_code=2000)

    colnames = ["name", "lat", "long"]

    try:
        dataframe = pd.read_csv(file.file, delimiter=";", names=colnames, header=None)
        dataframe.lat = dataframe.lat.astype(float)
        dataframe.long = dataframe.long.astype(float)
        dataframe = dataframe[(dataframe.lat < 90) & (dataframe.lat > -90)]
        dataframe = dataframe[(dataframe.long < 180) & (dataframe.long > -180)]

    except Exception as e:
        print(e)
        raise ApplicationException(error_code=2002, exception=e)

    if len(dataframe.columns) != 3:
        ApplicationException(error_code=2001)

    dataframe_items = dataframe.to_dict(orient="records")
    print(dataframe_items)
    try:
        input_model = LocationsInputDto(
            is_locations=True,
            locations=[
                LocationPointInputDto.parse_obj(item) for item in dataframe_items
            ],
        )
    except Exception as e:
        print(e)
        raise ApplicationException(error_code=2002, exception=e)

    response_model = elevation_service.get_elevations_from_locations(
        locations_model=input_model.to_model(), is_locations=input_model.is_locations
    )

    return ElevationsOutputDto.from_model(response_model)
