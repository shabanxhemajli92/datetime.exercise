import calendar
from cgitb import reset
from colorama import *
init()

print(Back.BLUE,"####################",Back.RESET)
print(Back.BLUE,"####LEAP CHECKER####",Back.RESET)
print(Back.BLUE,"####################",Back.RESET)
year_check=int((input("Enter the year: ")))
leap_checker=calendar.isleap(year_check)
if leap_checker==True:
    print(Back.GREEN,year_check,"is a leap year",Back.RESET)
else:
    print(Back.RED,year_check,"is not a leap year",Back.RESET)    