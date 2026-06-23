import redis

r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

r.set("project", "Distributed Log Processing System")

print(r.get("project"))