# Closures

def sum_ten():
  def add(value):
    return value + 10
  return add

add_closure = sum_ten()
print(add_closure(5)) # 15
