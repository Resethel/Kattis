# Using Python 3
# https://open.kattis.com/problems/tarifa

X = int(input())
N = int(input())
P = 0
for _ in range(N):
    P += (int(X) - int(input()))

print(P+X)
