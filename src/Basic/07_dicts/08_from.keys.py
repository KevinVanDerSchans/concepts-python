# fromkeys()

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

my_new_dict = dict.fromkeys(("name", 1))
print(my_new_dict)
