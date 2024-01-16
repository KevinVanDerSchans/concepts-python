# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print('My condition is greater than or equal to 10.')


while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print('Mi condición es 15.')
        break
    print(my_condition)
print('The loop is over.')
