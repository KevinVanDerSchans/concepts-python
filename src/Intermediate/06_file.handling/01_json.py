# .json file

import json

json_file = open("Intermediate/06_file.handling/my_file.json", "w+")


json_test = {
  "name": "Kevin",
  "surname": "Schans",
  "age": 29,
  "tech": "Python"
}

json_file.write(json_test)

json.dump(json_test, json_file, indent = 8)

json.file.close()

json_dict = json.load(open("Intermediate/06_file.handling/my_file.json"))
print(json_dict)
print(type(json_dict))
