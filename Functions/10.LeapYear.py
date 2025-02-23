def is_leap_year(year):

    if year % 4 !=0:
        return False
    elif year % 100 !=0:
        return True
    elif year % 400 !=0:
        return False
    else:
        return True

year = int(input("Enter a Year : "))

if is_leap_year(year):
    print(year, 'is a leap year..')
else:
     print(year, 'is a not leap year.')

# ----------------Output---------------#

# Enter a Year : 2012
# 2012 is a leap year..

# Enter a Year : 2017
# 2017 is a not leap year.