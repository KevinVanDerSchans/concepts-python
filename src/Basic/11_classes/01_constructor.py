# Constructor

class Person:
    def __init__(self, name, surname, alias = 'KevinSchansDelgado'):
        self.name = name
        self.surname = surname

my_person = Person('Kevin', 'Schans')

print(my_person.name) # Kevin
print(f"{my_person.name} {my_person.surname}") # Kevin Schans


# Another way, by defining the parameters in the constructor

class OtherPerson:
    def __init__(self):
        self.name = "Kevin"
        self.surname = "Schans"

my_other_person = OtherPerson()

print(my_other_person.name) # Kevin
print(f"{my_other_person.name} {my_other_person.surname}") # Kevin Schans


# Full name, creating a new stored property

class FullNamePerson:
    def __init__(self, name, surname):
      self.full_name = f"{name} {surname}"

    def walk (self):
        print(f"{self.full_name} is walking...")

my_full_name_person = FullNamePerson('Schans', 'Kevin')
print(my_full_name_person.full_name)

walk_action = my_full_name_person.walk()
print(walk_action)
