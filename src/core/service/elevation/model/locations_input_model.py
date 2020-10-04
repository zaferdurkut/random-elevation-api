from typing import List

from pydantic import Field, BaseModel


class LocationPointModel(BaseModel):
    name: str = Field(None)
    lat: float = Field(None)
    long: float = Field(None)


class LocationsInputModel(BaseModel):
    locations: List[LocationPointModel] = Field(...)
