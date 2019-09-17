# Using Python 3
# https://open.kattis.com/problems/3dprinter

import math

# Getting statues to print
N = int(input())
days = math.ceil(math.log(N, 2)) + 1
print(days)
