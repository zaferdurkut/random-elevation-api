from pydantic import BaseModel, Field


class TokenOutputModel(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)

    @staticmethod
    def to_model(access_token: str, token_type: str):
        return TokenOutputModel(access_token=access_token, token_type=token_type)
