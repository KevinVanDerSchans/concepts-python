# try else

numberOne = 2
numberTwo = 5

# numberTwo = '5'

try:
    print(numberOne + numberTwo)
    print('An error has not occurred.')
except:
    print('An error has occurred.')
else:
    print('The execution continues correctly...')

"""
Print:

7
An error has not occurred.
The execution continues correctly...
"""
