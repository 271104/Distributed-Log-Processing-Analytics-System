import redis

from config import (
    REDIS_HOST,
    REDIS_PORT,
    STREAM_NAME,
    GROUP_NAME,
    CONSUMER_NAME
)


class RedisConsumer:

    def __init__(self):

        self.redis_client = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            decode_responses=True
        )

    def read_messages(self):

        messages = self.redis_client.xreadgroup(
            GROUP_NAME,
            CONSUMER_NAME,
            {STREAM_NAME: ">"},
            count=10,
            block=5000
        )

        return messages

    def acknowledge(self, message_id):

        self.redis_client.xack(
            STREAM_NAME,
            GROUP_NAME,
            message_id
        )