from typing import List

from pydantic import Field, BaseModel

from src.core.service.elevation.model.locations_output_model import (
    ElevationsOutputModel,
    LocationPointElevationOutputModel)


class LocationPointElevationOutputDto(BaseModel):
    name: str = Field(None, title="Location Name", example="Location-1")
    lat: float = Field(None, title="Latitude of Location", example=36.152)
    long: float = Field(None, title="Longitude of Location", example=42.232)
    elevation: float = Field(None, title="Elevation of Location", example=150.123)

    def from_model(model: LocationPointElevationOutputModel):

        return LocationPointElevationOutputDto(**model.dict(exclude_none=True))



class ElevationsOutputDto(BaseModel):
    elevations: List[LocationPointElevationOutputDto] = Field(default=[])

    def from_model(model: ElevationsOutputModel):

        return ElevationsOutputDto(**model.dict(exclude_none=True))
