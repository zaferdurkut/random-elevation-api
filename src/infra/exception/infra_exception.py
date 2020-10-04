from src.core.exception.application_exception import ApplicationException


class InfraApplicationException(ApplicationException):
    def __init__(self, error_code: int, exception: Exception = None) -> None:
        super().__init__(error_code, exception)

class ClientException(Exception):
    def __init__(self, detail):
        self.detail = detail
        super().__init__(detail)
