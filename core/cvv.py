import random

def generatecvv():
    random_number = random.randint(100, 999)
    return f"{random_number:03}"
