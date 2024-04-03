import datetime

# Get current date
now = datetime.datetime.now()

#TASK 1
# Subtract five days from current date
five_days_ago = now - datetime.timedelta(days=5)

#TASK 2
# Print yesterday, today, tomorrow
yesterday = now - datetime.timedelta(days=1)
tomorrow = now + datetime.timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", now.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#TASK 3
# Drop microseconds from datetime
now_no_microseconds = now.replace(microsecond=0)

print("Now without microseconds:", now_no_microseconds.strftime("%Y-%m-%d %H:%M:%S"))

#TASK 4
# Calculate two date difference in seconds
date1 = datetime.datetime(2022, 1, 1)
date2 = datetime.datetime(2022, 1, 10)

seconds_difference = (date2 - date1).total_seconds()

print("Seconds difference between date1 and date2:", seconds_difference)

# Calculate two date difference in seconds (alternative approach)
date3 = datetime.datetime(2022, 1, 1)
date4 = datetime.datetime(2022, 1, 10)

seconds_difference_alternative = int((date4 - date3).total_seconds())

print("Seconds difference between date3 and date4 (alternative approach):", seconds_difference_alternative)