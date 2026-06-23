# event_factory.py

import uuid
import random
from datetime import datetime, timezone

from config import EVENT_TYPES
from user_simulator import get_random_user
from device_simulator import get_device
from country_simulator import get_country


def create_event():

    event = {
        "event_id": str(uuid.uuid4()),

        "user_id": get_random_user(),

        "event_type": random.choice(EVENT_TYPES),

        "device_type": get_device(),

        "country": get_country(),

        "timestamp": datetime.now(
            timezone.utc
        ).isoformat()
    }

    return event