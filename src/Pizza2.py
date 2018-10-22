#Using Python 3
#https://open.kattis.com/problems/pizza2

import math

dim = [float(x) for x in input().split(' ')]

area = math.pi * dim[0]**2
cheese = math.pi * (dim[0] - dim[1])**2

print(format(100*cheese/area, '.6f'))
