# Using Python 3
# https://open.kattis.com/problems/bits

n = int(input())

nb = []
for i in range(n):
    nb.append(input())


for number in nb:
    out = 0
    for i in range(1,len(number)+1):
        out = max(out, bin(int(number[:i])).count('1'))

    print(out)
