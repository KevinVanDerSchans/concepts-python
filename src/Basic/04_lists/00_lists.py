# Lists

"""
Differences between List and Array

- In a List, the elements we store can be of different data types.
  In an Array, the elements must be of the same type.

- Lists are more versatile and flexible data structures.
  In this sense, Arrays have a more limited functionality.

- Lists are a built-in data structure in Python, so there is no need to import them.
  To use Arrays, you need to import them.
"""

my_list = list()
my_other_list = []

print(len(my_list)) # 0

my_list = [23, 45, 21, 34, 21, 1, 6]
print(my_list)

print(type(my_list))
