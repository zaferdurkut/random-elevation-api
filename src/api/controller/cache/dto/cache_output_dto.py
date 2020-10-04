from pydantic import BaseModel, Field


class CacheOutputDto(BaseModel):
    status: bool = Field(...)
    message: list = Field(...)

    @staticmethod
    def to_model(status: bool, message: str):
        return CacheOutputDto(status=status, message=message)
