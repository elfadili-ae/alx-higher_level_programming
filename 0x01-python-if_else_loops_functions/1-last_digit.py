#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = abs(number) % 10

print(f"Last digit of {number:d} is", end=" ")

if lastD > 5:
    print("{lastD} and is greater than 5")
elif lastD == 0:
    print("{lastD} and is 0")
else:
    print("-{lastD} and is less than 6 and not 0")
