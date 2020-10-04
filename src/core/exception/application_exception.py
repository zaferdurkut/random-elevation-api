from src.infra.util.errors import errors


class ApplicationException(Exception):
    def __init__(self, error_code: int, exception: Exception = None) -> None:
        if error_code in errors:
            pass
        else:
            error_code = 1999

        self.error_message = errors[error_code]
        self.error_code = error_code
        self.exception = exception
