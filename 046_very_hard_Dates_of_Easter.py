"""
Dates of Easter
The Christian holiday of Easter Sunday is a movable feast. It can occur on any date from March 22 to April 25. The date depends on the timing between the Paschal Full Moon and the spring equinox. It wasn't until the late 19th century that a formula was developed to accurately predict Easter's date for a given year.

Your task is to use this formula, also known as Butcher's Algorithm, to write a function that will return the date of Easter for any year after 1600. See the Resources tab for a detailed description of the algorithm.

Examples
easter_date(1600) ➞ "April 2"

easter_date(2020) ➞ "April 12"

easter_date(1853) ➞ "March 27"

easter_date(3535) ➞ "April 14"
Notes
Before 1600 the Julian calendar was used in most countries. The algorithm we're using is based on the Gregorian calendar, which is still in use today.
"""

def easter_date(year):
    
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    
    month_name = "March" if month == 3 else "April"
    return "{} {}".format(month_name, day)




print(easter_date(1715)) # "April 21")
print(easter_date(1758)) # "March 26")
print(easter_date(1872)) # "March 31")
print(easter_date(1899)) # "April 2")
print(easter_date(1900)) # "April 15")
print(easter_date(1944)) # "April 9")
print(easter_date(1989)) # "March 26")
print(easter_date(2000)) # "April 23")
print(easter_date(2070)) # "March 30")
print(easter_date(2099)) # "April 12")
print(easter_date(6009)) # "April 12")
print(easter_date(9999)) # "March 28")