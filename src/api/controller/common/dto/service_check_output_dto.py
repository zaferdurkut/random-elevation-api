from pydantic import BaseModel, Field


class ServiceCheckOutputDto(BaseModel):
    redis_cache_check: bool = Field(...)
    db_connection_check: bool = Field(...)

    @staticmethod
    def to_model(redis_cache_check: bool, db_connection_check: bool):
        return ServiceCheckOutputDto(
            redis_cache_check=redis_cache_check,
            db_connection_check=db_connection_check)
