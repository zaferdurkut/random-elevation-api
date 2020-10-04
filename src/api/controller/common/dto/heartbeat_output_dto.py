from pydantic import BaseModel, Field


class HeartbeatOutputDto(BaseModel):
    host_name: str = Field(...)

    @staticmethod
    def to_model(host_name: str):
        return HeartbeatOutputDto(host_name=host_name)
