# Using Python 3
# https://open.kattis.com/problems/faktor

var = [int(x) for x in input().split(' ')]
print(var[0]*(var[1]-1) + 1)
