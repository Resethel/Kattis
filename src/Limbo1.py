# Using Python 3
# https://open.kattis.com/problems/limbo1

T = int(input())
timeFactors = []

for _ in range(T):
    L, R = map(int, input().split(' '))

    ls = ((L+R) * (L+R+1))//2 + 1 #ls is the first number in the layer
    timeFactors.append(ls + R)

for fact in timeFactors: print(fact)
