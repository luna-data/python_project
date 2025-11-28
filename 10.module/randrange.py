import random

def roll_dice():
    return random.randrange(1, 7)

for _ in range(10):
    print(roll_dice())