from jaeger_client import Config

from src.infra.config.app_config import JAEGER_HOST, JAEGER_PORT, JAEGER_SAMPLER_TYPE, JAEGER_SAMPLER_RATE
from src.infra.util.constants import APP_NAME


def init_tracer(service_name: str = "Elevation-Api"):
    trace_id_header: str = "X-TRACE-ID"
    config = Config(
        config={
            "local_agent": {
                "reporting_host": JAEGER_HOST,
                "reporting_port": JAEGER_PORT
            },
            "sampler": {
                "type": JAEGER_SAMPLER_TYPE,
                "param": JAEGER_SAMPLER_RATE,
            },
            "logging": True,
            "trace_id_header": trace_id_header
        },
        service_name=service_name,
        validate=True
    )

    return config.initialize_tracer()


tracer = init_tracer(APP_NAME)
