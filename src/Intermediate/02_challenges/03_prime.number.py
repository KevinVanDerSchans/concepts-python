# Prime number

"""
Write a program to check whether a number is prime or not.
Once this is done, print the prime numbers between 1 and 100.
"""

def is_prime():

  for number in range(1, 101):

    if number >= 2:

      is_divisible = False

      for index in range(2, number):
          if number % index == 0:
              is_divisible = True
              break

      if not is_divisible:
          print(number)


is_prime()
