import time

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from src.infra.config.app_config import LOG_IS_ENABLED

LOG_MIDDLEWARE_IS_ENABLED = True


class RequestResponseMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        self.process_request(request)
        response = await call_next(request)
        self.process_response(request, response)
        return response

    @staticmethod
    def check_media_type(media_type: str):
        if media_type is not None and ("json" in media_type or "text" in media_type):
            return True
        return False

    @staticmethod
    def process_request(request: Request):
        if LOG_IS_ENABLED is not True:
            return

        if LOG_MIDDLEWARE_IS_ENABLED is True:
            request.state.start_time = time.time()

        return request

    @staticmethod
    def process_response(request: Request, response: Response):
        if LOG_IS_ENABLED is False or LOG_MIDDLEWARE_IS_ENABLED is False:
            return

        if b"content-length" in dict(response.raw_headers):
            data_len = str(dict(response.raw_headers)[b"content-length"], "utf-8")
        else:
            data_len = "-"

        elapsed_ms = int((time.time() - request.state.start_time) * 1000)
        http_status_code = response.status_code
        log_template = "{0} | {1} | {2} | {3}ms"

        if b"user-agent" in dict(request.headers.raw):
            user_agent = str(dict(request.headers.raw)[b"user-agent"], "utf-8")
        else:
            user_agent = "-"

        log_data = {
            "logger": "middleware",
            "remote_addr": request.client.host,
            "http_m": request.method,
            "uri": request.url.path,
            "http_s": http_status_code,
            "data_len": data_len,
            "user_agent": user_agent,
            "elapsed_ms": elapsed_ms,
        }

        if http_status_code >= 400:
            if http_status_code >= 500:
                print(
                    str.format(
                        log_template,
                        request.url.path,
                        request.method,
                        http_status_code,
                        elapsed_ms,
                    ),
                    log_data,
                )
            else:
                print(
                    str.format(
                        log_template,
                        request.url.path,
                        request.method,
                        http_status_code,
                        elapsed_ms,
                    ),
                    log_data,
                )
        else:
            if str.endswith(request.url.path, "/healthcheck") is False:
                print(
                    str.format(
                        log_template,
                        request.url.path,
                        request.method,
                        http_status_code,
                        elapsed_ms,
                    ),
                    log_data,
                )
