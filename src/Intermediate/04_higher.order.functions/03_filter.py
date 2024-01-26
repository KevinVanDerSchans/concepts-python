# filter

numbers = [2, 5, 10, 21, 30]

def filter_greater_than_ten(number):
  if number > 10:
    return True
  return False

print(list(filter(filter_greater_than_ten, numbers))) # [21, 30]
