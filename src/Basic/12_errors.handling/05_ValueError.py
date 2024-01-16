# ValueError

numberOne = 2
numberTwo = 5

numberTwo = '5'

try:
    print(numberOne + numberTwo)
    print('An error has not occurred.')
except ValueError as error:
    print(error) # prints: TypeError: unsupported operand type(s) for +: 'int' and 'str'
except Exception as exception:
    print(exception)
