# Errors

# print(5 + "5")
# Error: unsupported operand type(s) for +: 'int' and 'str'

numberOne = 2
numberTwo = 5

numberTwo = '5'

try:
    print(numberOne + numberTwo)
    print('An error has not occurred.')
except:
    print('An error has occurred.')
