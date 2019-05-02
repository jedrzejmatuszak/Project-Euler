#! usr/bin/python3
# Project Euler 19 - Counting Sundays
year = 1900
day = 1
week = 1  # 1 - MON, 2 - TUE, 3 - WED, 4 - THU, 5 - FRI, 6 - SAT, 7 - SUN; set MON couse 1st JAN 1900 was MON
counter = 0
year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 31, 12: 31}
leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 31, 12: 31}
# setting day of a week at 1st JAN 1901
# year 1900 isn't leap year, cause it's century year and isn't divisible by 400
while day < 366:
    if week == 8:
        week = 1
    # print(day, week)
    day += 1
    week += 1
day = 1
year += 1
print('Congratulations :) you are at 1901 year')
print('1st JAN 1901 is', week)
while year < 2001:
    # if leap year
    if year % 4 == 0:
        while day < 367:
            # print('Leap year: ', year)
            if week == 8:
                week = 1
            day += 1
            week += 1
            if week == 7:
                counter += 1
                print(year, day, week, counter)
        day = 1
        year += 1
    else:
        while day < 366:
            # print('Year: ', year)
            if week == 8:
                week = 1
            day += 1
            week += 1
            if week == 7:
                counter += 1
                print(year, day, week, counter)
        day = 1
        year += 1
print(counter) # counting number of sundays in 20th century