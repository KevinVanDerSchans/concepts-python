# TypeError

numberOne = 2
numberTwo = 5

numberTwo = '5'

try:
    print(numberOne + numberTwo)
    print('An error has not occurred.')
except TypeError:
    print('An error has occurred.')
