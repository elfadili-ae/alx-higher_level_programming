#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = number % 10

print(f"Last digit of {number:d} is {lastD:d}", end = " ")

if lastD > 5:
    print("and is greater than 5")
elif lastD == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
