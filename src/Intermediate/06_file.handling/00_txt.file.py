# .txt file

open("my_file.txt") # FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'


import os

txt_file = open("Intermediate/06_file.handling/my_file.txt", "r+")
print(txt_file.read())
