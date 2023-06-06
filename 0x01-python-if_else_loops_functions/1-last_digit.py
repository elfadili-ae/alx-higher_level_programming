#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = abs(number) % 10

print(f"Last digit of {number} is", end=" ")

if lastD > 5:
    print(f"{lastD} and is greater than 5")
elif lastD == 0:
    print(f"{lastD} and is 0")
else:
    if number < 0:
        print("-", end="")
    print(f"{lastD} and is less than 6 and not 0")
