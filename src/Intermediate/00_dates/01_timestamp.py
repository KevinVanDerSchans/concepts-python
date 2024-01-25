# timesstamp()

"""
To obtain the time value in seconds since midnight (00:00:00) on January 1,
1970 in Coordinated Universal Time (UTC). This value is commonly known as the
"Unix timestamp" or "epoch timestamp".
"""

from datetime import datetime

now = datetime.now()

timestamp = now.timestamp()
print(timestamp) # now: 1705419198.622817

year_2023 = datetime(2023, 1, 1)
