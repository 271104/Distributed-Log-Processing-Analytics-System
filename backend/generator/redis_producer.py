import redis
from config import (
    REDIS_HOST,
    REDIS_PORT,
    STREAM_NAME
)

class RedisProducer:

    def __init__(self):
        self.redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )

    def publish_event(self, event):
        stream_id = self.redis_client.xadd(
            STREAM_NAME,
            event
        )

        return stream_id