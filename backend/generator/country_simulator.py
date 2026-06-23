# country_simulator.py

import random

def get_country():
    return random.choices(
        population=[
            "India",
            "USA",
            "UK",
            "Germany",
            "Canada"
        ],
        weights=[
            50,
            20,
            10,
            10,
            10
        ],
        k=1
    )[0]