# Access dict

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

print(my_dict["name"]) # Kevin

my_dict["name"] = 'Michael'
print(my_dict) # {'name': 'Michael', 'surname': 'Schans', 'edad': 29, 1: 'python', 'languages': {'JavaScript', 'Java', 'Python'}}
