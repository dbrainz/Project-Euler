# Project Euler - Problem 19
# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#
# Darren Brain
# darren.brain@gmail.com
# 3/4/2016

# 0 = Sunday, 1 = Monday, 2 = Tuesday, etc
# Jan 1, 1901 = Tuesday
start_day = 2
sunday_count = 0

for year in range(1901,2001):
    for month in range(1, 13):
        if month in [4,6,9,11]:
            start_day = (start_day + 30) % 7
        elif month == 2:
            if year % 4 == 0:
                start_day =  (start_day + 29) % 7
            else:
                start_day = (start_day + 28) % 7
        else:
            start_day = (start_day + 31) % 7

        if start_day == 0:
            sunday_count += 1

if start_day == 0:
    sunday_count  -= 1

print(sunday_count)