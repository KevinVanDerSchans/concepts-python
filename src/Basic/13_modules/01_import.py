# import

import my_module
my_module.sum(5, 3, 1)
my_module.printValue('Hello')

from my_module import sum

sum(5, 3, 1)

"""
Prints:

9
<built-in function print> # no está la function importada
9
"""
