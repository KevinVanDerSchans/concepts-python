# Tuples

"""
They are used to store an ordered collection of elements, like lists, but
their immutability makes them useful in situations where you want to make
sure in situations where you want to make sure that the data does not change.
"""

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, 'Kevin', 'Schans')
print(my_tuple) # (35, 1.77, 'Kevin', 'Schans')

print(type(my_tuple)) # <class 'tuple'>
print(type(my_other_tuple)) # <class 'tuple'>
