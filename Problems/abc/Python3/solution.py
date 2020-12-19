# Using Python 3
# https://open.kattis.com/problems/abc

n = [int(x) for x in input().split(' ')]
n.sort()
out = ""

for i in list(input()):
    out += str(n[ord(i) - ord('A')]) + " "

print(out[:len(out)-1])
