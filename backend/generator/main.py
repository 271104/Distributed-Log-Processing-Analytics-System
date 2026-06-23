import time

from event_factory import create_event
from redis_producer import RedisProducer
from config import EVENTS_PER_SECOND

producer = RedisProducer()

count = 0

while True:

    event = create_event()

    stream_id = producer.publish_event(event)

    count += 1

    print(
        f"[{count}] Published -> "
        f"{event['event_type']} | "
        f"Stream ID: {stream_id}"
    )

    time.sleep(
        1 / EVENTS_PER_SECOND
    )