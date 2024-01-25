# range()

my_original_list = [0, 1, 2, 3, 4, 5]

my_range = range(6)
print(list(my_range)) # [0, 1, 2, 3, 4, 5]


my_list = [i + 1 for i in range(6)]
print(my_list) # [1, 2, 3, 4, 5, 6]

my_list = [i * 2 for i in range(6)]
print(my_list) # [0, 2, 4, 6, 8, 10]

my_list = [i * i for i in range(6)]
print(my_list) # [0, 1, 4, 9, 16, 25]
