# The Fibonacci sequence

"""
Write a program that prints the first 50
numbers of the Fibonacci sequence starting
at 0. Fibonacci series starting at 0.

- The Fibonacci series is a sequence of numbers in which
the next number is always the sum of the previous two.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def fibonacci():

    prev = 0
    next = 1

    for index in range(0, 50):
        print(prev)
        fib = prev + next
        prev = next
        next = fib


fibonacci()
