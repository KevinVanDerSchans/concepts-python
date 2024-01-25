# Modify dates

from datetime import date

current_date = date(2024, 1, 16)
print(current_date) # 2024-01-16

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date) # 2024-02-16
