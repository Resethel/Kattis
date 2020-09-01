# Using Python 3
# https://open.kattis.com/problems/prsteni

from fractions import Fraction
from math import gcd

n = int(input())
rings = [int(x) for x in input().split(' ')]

for i in range(1,n):
    ratio = 1
    for j in range(1,i+1):
        ratio *= rings[j-1]/rings[j]
    ratio_frac = Fraction(ratio).limit_denominator()

    if(ratio_frac.denominator == 1):
        print(ratio_frac, end = '')
        print("/1")
    else:
        print(ratio_frac)
