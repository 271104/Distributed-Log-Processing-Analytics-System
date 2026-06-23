# device_simulator.py

import random

def get_device():
    return random.choices(
        population=["mobile", "desktop", "tablet"],
        weights=[70, 25, 5],
        k=1
    )[0]