#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number:
    if number < 0:
        print("is negative")
    else:
        print("is positive")
else:
    print("is zero")
