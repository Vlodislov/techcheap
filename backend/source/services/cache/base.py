import pickle
from typing import Any, Optional
import redis

from source.core.settings import settings


class Cache:
    redis_connection = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)

    @classmethod
    def get(cls, key: str) -> Optional[Any]:
        data = cls.redis_connection.get(key)
        if data:
            return pickle.loads(data)

    @classmethod
    def put(cls, key: str, data: Any) -> None:
        print(data)
        cls.redis_connection.append(key, data)

    @classmethod
    def invalidate(cls, key: str) -> None:
        if cls.redis_connection.exists(key):
            cls.redis_connection.delete(key)
