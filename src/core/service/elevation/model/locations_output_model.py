from typing import List

from pydantic import Field, BaseModel


class LocationPointElevationOutputModel(BaseModel):
    name: str = Field(None)
    lat: float = Field(None)
    long: float = Field(None)
    elevation: float = Field(None)

class ElevationsOutputModel(BaseModel):
    elevations: List[LocationPointElevationOutputModel] = Field(default=[])
