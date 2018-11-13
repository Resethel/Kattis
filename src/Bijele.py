# Using Python 3
# https://open.kattis.com/problems/bijele

pieces = [int(x) for x in input().split()]
for res in ([s - p for s, p in zip([1,1,2,2,2,8], pieces)]): print(res, end = ' ')
print()
