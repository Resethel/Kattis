# Using Python 3
# https://open.kattis.com/problems/qaly

n = int(input())

QALY = 0.0
for i in range(n):
    quality, years = map(float, input().split())
    QALY += quality * years

print(QALY)
