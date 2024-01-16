# Remove value

my_dict = {
  "name": "Kevin",
  "surname": "Schans",
  "edad": 29,
  1: 'python',
  "languages": {
    "Python",
    "JavaScript",
    "Java"
  },
  'city': 'Malaga'
}

del my_dict["city"]
print(my_dict)

"""
{
  'name': 'Kevin',
  'surname': 'Schans',
  'edad': 29,
  1: 'python',
  'languages': {'Java', 'JavaScript', 'Python'},
}
"""
