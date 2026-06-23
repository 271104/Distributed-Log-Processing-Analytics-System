from consumer import RedisConsumer
from postgres_client import PostgresClient

consumer = RedisConsumer()
postgres = PostgresClient()

print("Processor Started...")

while True:

    messages = consumer.read_messages()

    if not messages:
        continue

    for stream_name, entries in messages:

        for message_id, event in entries:

            postgres.insert_log(event)

            consumer.acknowledge(message_id)

            print(
                f"Processed: "
                f"{event['event_type']} "
                f"| {message_id}"
            )