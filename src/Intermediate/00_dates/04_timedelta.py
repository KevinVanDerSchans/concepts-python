# timedelta

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

sum_timedelta = end_timedelta + start_timedelta
subtract_timedelta = end_timedelta - start_timedelta
# multiply_timedelta = end_timedelta * start_timedelta
division_timedelta = end_timedelta / start_timedelta

print(sum_timedelta) # 661 days, 0:03:20.000200
print(subtract_timedelta) # 121 days, 0:00:00
# print(multiply_timedelta) Prints: unsupported operand type(s) for *: 'datetime.timedelta' and 'datetime.timedelta'
print(division_timedelta) # 1.4481462270804388
