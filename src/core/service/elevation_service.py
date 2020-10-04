import random

from src.core.config.cache_constants import CacheManagementConstants
from src.core.service.elevation.model.locations_input_model import (
    LocationPointModel,
    LocationsInputModel,
)
from src.core.service.elevation.model.locations_output_model import (
    LocationPointElevationOutputModel,
    ElevationsOutputModel,
)
from src.infra.adapter.redis.redis_adapter import RedisAdapter


class ElevationService:
    def __init__(
        self,
    ):
        self.redis_client = RedisAdapter()
        self.cache_constants = CacheManagementConstants()

    def get_elevations_from_locations(
        self, locations_model: LocationsInputModel, is_locations: bool = False
    ) -> ElevationsOutputModel:
        elevations_model = ElevationsOutputModel()
        for location_model in locations_model.locations:
            elevation_output_model = self.get_elevation_from_location(
                location_model=location_model, is_locations=is_locations
            )
            elevations_model.elevations.append(elevation_output_model)
        return elevations_model

    def get_elevation_from_location(
        self, location_model: LocationPointModel, is_locations: bool = False
    ) -> LocationPointElevationOutputModel:

        if is_locations:
            return LocationPointElevationOutputModel(
                name=location_model.name,
                lat=location_model.lat,
                long=location_model.long,
                # TODO: should be update elevation with client
                elevation=random.uniform(1, 700),
            )
        else:
            return LocationPointElevationOutputModel(
                name=location_model.name,
                # TODO: should be update elevation with client
                elevation=random.uniform(1, 700),
            )
