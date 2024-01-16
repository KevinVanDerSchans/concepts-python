# dicts

"""
A data structure that represents a collection of key-value pairs.
Each element in a dictionary consists of a unique key and an associated value.
"""

my_dict = dict()
my_other_dict = {}

print(type(my_dict)) # <class 'dict'>
print(type(my_other_dict))

my_other_dict = {
  "name": "Kevin",
  "surname": "Schans",
  "edad": 29,
  1: 'python',
  "languages": {
    "Python",
    "JavaScript",
    "Java"
  }
}

print(my_other_dict)
