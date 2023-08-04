import time

completeTime = time.strftime("%H:%M:%S")
print("Current Time is:", completeTime)  # Current Time in HH:MM:SS format

hour = input(str(time.strftime("%H\n")))
print(hour)

if hour < "12":
    print("Good Morning")
elif hour < "16":
    print("Good Afternoon")
elif hour < "20":
    print("Good Evening")
else:
    print("Good Night")

# q :make this code for accpting the date and month and year and print the day of the week

# q :make this code for accpting the date and month and year and print the day of the week

""" make this code accpeting the date and month and year and print the day of the week"""
import datetime
import calendar


def findDay(date):
    born = datetime.datetime.strptime(date, "%d %m %Y").weekday()
    return calendar.day_name[born]


# Driver program
date = input("enter the date in dd mm yyyy format")

print(findDay(date))


""" test cases"""
# 1. 31 08 2019
# 2. 01 09 2019
# 3. 02 09 2019
# 4. 03 09 2019
# 5. 04 09 2019
# 6. 05 09 2019

""" output"""
# 1. Saturday
# 2. Sunday
# 3. Monday
# 4. Tuesday
# 5. Wednesday
# 6. Thursday
