# Fizz Buzz

"""
Write a program that displays the numbers 1 to 100
(both included and with a line break between numbers
from 1 to 100 (both included and with a line break in
between each each printout), substituting the following:

- Multiples of 3 for the word "fizz".
- Multiples of 5 for the word "buzz".
- Multiples of 3 and 5 at the same time for the word "fizzbuzz".
"""

def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuz")
        elif index % 3 == 0:
            print("fizz")
        elif index % 5 == 0:
            print("buzz")
        else:
            print(index)

fizzbuzz()
