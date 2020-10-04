from typing import List

from pydantic import Field, BaseModel

from src.core.service.elevation.model.locations_input_model import LocationsInputModel, LocationPointModel


class LocationPointInputDto(BaseModel):
    name: str = Field(..., title="Name")
    lat: float = Field(
        ...,
        ge=-90,
        le=90,
        title="Latitude",
        description="Latitude e.g. 40.75677",
        example="37.774929",
    )
    long: float = Field(
        ...,
        ge=-180,
        le=180,
        title="Longitude",
        description="Longitude e.g. 73.99034",
        example="-122.419418",
    )

    def to_model(self) -> LocationPointModel:
        return LocationPointModel(**self.dict())



class LocationsInputDto(BaseModel):
    is_locations: bool = Field(default=False,
        title="",
        description="If you want to see the locations in the output model, you can set the parameter to True.",
        example=False,
    )
    locations: List[LocationPointInputDto] = Field(
        ...,
        title="Location point list",
        example=[
            LocationPointInputDto(
                name="location-1",
                lat=34.774929,
                long=35.419418,
            ),
            LocationPointInputDto(
                name="location-2",
                lat=36.75677,
                long=46.99034,
            ),
            LocationPointInputDto(
                name="location-3",
                lat=33.75677,
                long=45.99034,
            ),
        ],
    )

    def to_model(self) -> LocationsInputModel:
        return LocationsInputModel(**self.dict())
