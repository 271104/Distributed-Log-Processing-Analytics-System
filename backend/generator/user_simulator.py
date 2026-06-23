# user_simulator.py

import random
from config import TOTAL_USERS

def get_random_user():
    return random.randint(1, TOTAL_USERS)