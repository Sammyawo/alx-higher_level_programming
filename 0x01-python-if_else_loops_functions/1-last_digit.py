#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    number1 = number % 10
    if number1 > 5:
        print(f'Last digit of {number} is {number1} and is greater than 5')
    elif number1 == 0:
        print(f'Last digit of {number} is {number1} and is 0')
    else:
        print(f'Last digit of {number} is {number1} is less than 6 and not 0')
else:
    number1 = -(number) % 10
    number1 = -number1
    if number1 == 0:
        print(f'Last digit of {number} is {number1} and is 0')
    else:
        print(f'Last digit of {number} is {number1} is less than 6 and not 0')
