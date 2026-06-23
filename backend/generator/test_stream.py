import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

stream_id = r.xadd(
    "log_stream",
    {
        "event_type": "LOGIN",
        "user_id": "123"
    }
)

print("Added:", stream_id)