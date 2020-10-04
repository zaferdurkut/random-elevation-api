from dotenv import load_dotenv
from starlette.config import Config

load_dotenv()

config = Config(".env")

JAEGER_HOST = config('JAEGER_HOST')
JAEGER_PORT = config('JAEGER_PORT')
JAEGER_SAMPLER_TYPE = config('JAEGER_SAMPLER_TYPE')
JAEGER_SAMPLER_RATE = config('JAEGER_SAMPLER_RATE')

REDIS_HOST = config('REDIS_HOST')
REDIS_PORT = config('REDIS_PORT')
REDIS_DB = config('REDIS_DB')

DATABASE_URL = config('DATABASE_URL')

LOG_IS_ENABLED = config('LOG_IS_ENABLED', cast=bool)
