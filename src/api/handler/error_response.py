from pydantic.main import BaseModel


class ErrorResponse(BaseModel):
    error_code: int = None
    error_message: str = None
    error_detail: list = []
