# map

numbers = [2, 5, 10, 21]

def multiply_two(number):
  return number * 2

print(list(map(multiply_two, numbers))) # [4, 10, 20, 42]
print(list(map(lambda number: number * 2, numbers))) # [4, 10, 20, 42]
