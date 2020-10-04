import redis

from src.infra.config.app_config import REDIS_HOST, REDIS_PORT, REDIS_DB


def get_redis_client():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=int(REDIS_DB))
    return client
