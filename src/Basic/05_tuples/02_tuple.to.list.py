# Tuple to list

my_tuple = (35, 1.77, 'Kevin', 'Schans')

my_tuple = list(my_tuple)
print(type(my_tuple)) # <class 'list'>

my_tuple[2] = 'KEVIN'
my_tuple.insert(3, '2')
print(my_tuple) # [35, 1.77, 'KEVIN', '2', 'Schans']
