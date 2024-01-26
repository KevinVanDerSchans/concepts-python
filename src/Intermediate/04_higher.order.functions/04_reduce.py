# reduce

from functools import reduce

numbers = [2, 5, 10, 21, 30]

def sum_two_values(first_value, second_value):
  return first_value + second_value

print(reduce(sum_two_values, numbers)) # 68
