# Parameters with return

def sum_two_values_with_return (first_number, second_number):
  return first_number + second_number

my_result = sum_two_values_with_return(4, 5)
print(my_result)


def print_name (name, surname):
  print(f"{name} {surname}")

print_name('Kevin', 'Schans') # Kevin Schans
print_name(surname = 'Kevin', name = 'Schans') # Schans Kevin
