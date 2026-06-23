# config.py

TOTAL_USERS = 10000

EVENT_TYPES = [
    "LOGIN",
    "LOGOUT",
    "PASSWORD_RESET",
    "SEARCH",
    "VIEW_PRODUCT",
    "ADD_TO_CART",
    "REMOVE_FROM_CART",
    "PURCHASE",
    "PAYMENT_SUCCESS",
    "PAYMENT_FAILED"
]

DEVICE_TYPES = [
    "mobile",
    "desktop",
    "tablet"
]

COUNTRIES = [
    "India",
    "USA",
    "UK",
    "Germany",
    "Canada"
]

REDIS_HOST = "localhost"
REDIS_PORT = 6379

STREAM_NAME = "log_stream"

EVENTS_PER_SECOND = 10