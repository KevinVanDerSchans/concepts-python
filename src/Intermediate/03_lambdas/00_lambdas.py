# Lambdas

sum_two_value = lambda first_value, second_value: first_value + second_value
print(sum_two_value(2, 3)) # 5

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(5, 4)) # 17

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4)) # 11

