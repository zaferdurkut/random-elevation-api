from dotenv import load_dotenv
from src.infra.config.app_config import config

load_dotenv()

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT")
REDIS_CELERY_BROKER_DB = config("REDIS_CELERY_BROKER_DB")
REDIS_CELERY_BACKEND_DB = config("REDIS_CELERY_BACKEND_DB")
