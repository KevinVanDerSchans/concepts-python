# for dict

my_dict = {
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

for element in my_dict:
    print(element)

"""
Print:

name
surname
edad
1
languages
"""

# with .values() we can access the values of each property

for element in my_dict.values():
    print(element)
else:
    print('The for loop for dict is finished.')

"""
Print:

Kevin
Schans
29
python
{'Java', 'Python', 'JavaScript'}
"""

# break
for element in my_dict:
    print(element)
    if element == "age":
        print('Age has been reached, the loop stops.')
        break
else:
    print('The for loop for dict is finished.')

"""
Print:

Kevin
Schans
29
python
{'Java', 'Python', 'JavaScript'}
"""

# continue (use with consideration)
for element in my_dict:
    print(element)
    if element == "age":
        print('Age has been reached, the loop stops.')
        continue
else:
    print('The for loop for dict is finished.')

"""
Print:

Kevin
Schans
29
python
{'Java', 'Python', 'JavaScript'}
"""
