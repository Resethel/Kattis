# Using Python 3
# https://open.kattis.com/problems/secretmessage

from math import ceil
from math import sqrt
from math import pow


# This function rotate the string by transforming it
# into a matrix, doing the rotation, and retransforming it
def rotate90(str):

    N = int(sqrt(len(str)))
    matrix = [[str[x+y*N] for x in range(N)] for y in range(N)]

    zip(*matrix)
    rot = list(list(x)[::-1] for x in zip(*matrix))

    res = ""
    for x in range(N):
        for y in range(N):
            res += rot[x][y]

    return res

#########################################

n = int(input())
message = [""] * n

for i in range(n):
    message[i] = input()
    M = int(pow(ceil(sqrt(len(message[i]))),2))
    for j in range(M - len(message[i])):
        message[i] += '*'
    message[i] = rotate90(message[i])

for m in message:
    for k in range(len(m)):
        if (m[k] != '*'):
            print(m[k], end = '')
    print()
