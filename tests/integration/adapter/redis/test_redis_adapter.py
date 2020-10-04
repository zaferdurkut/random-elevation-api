from unittest import TestCase
from fastapi.testclient import TestClient
from src.application import create_app
from src.infra.adapter.redis.redis_adapter import RedisAdapter
import json

client = TestClient(create_app())


class CacheController(TestCase):
    redis_adapter = RedisAdapter()

    def test_cache_adapter_get(self, ):
        result = self.redis_adapter.set(key="test_key", value=json.dumps("test_value", default=str), expires=6000)
        assert result == True

        result = self.redis_adapter.get(key="test_key")
        result = json.loads(result)
        assert result == "test_value"

        result = self.redis_adapter.exist(key="test_key")
        assert result == True

        self.redis_adapter.delete_key(key="test_key")
        result = self.redis_adapter.exist(key="test_key")
        assert result == False
