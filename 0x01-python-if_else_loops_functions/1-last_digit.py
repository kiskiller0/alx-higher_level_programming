#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
remainder = str(number)[-1]

if remainder:

    if remainder > 5:
        msg = "greater than 5"
    elif remainder < 6:
        msg = "less than 6 and not 0"

else:
    msg = "is 0"

print("Last digit of {} is {} and is {}".format(number, remainder, msg)
