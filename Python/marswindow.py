# Using Python 3
# https://open.kattis.com/problems/marswindow

from math import floor

request = int(input())

month = 3
year = 2018

while(year < request):
    month += 26;
    year += floor(month / 12)
    month = month%12

if(year == request):
    print("yes")
else:
    print("no")
