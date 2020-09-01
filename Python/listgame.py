# Using python 3
# https://open.kattis.com/problems/listgame

# The solution to this problem is to find the prime factors of the number X
# and count them. This is a well-known case of cryptology
# Hower for the worst case (which is 999999937) the classic implementation of the
# algorithm would fail. Therefore, we have to stop counting when k is is >= sqrt(X).
# To be even faster, instead of calculating roots and so on, we perform the second
# part of the algorithm using the pwd2 of the divider.

# ==== Main Algorithm ==========================================================


X = int(input())
k = int()

divider = 2
while X % divider == 0:
    k += 1
    X /= divider

divider = 3
X2 = X
while divider * divider <= X:
    while X2 % divider > 0 and divider * divider <= X:
        divider += 2
    if X2 % divider != 0:
        break
    X2 //= divider
    k += 1

print(k+1 if X2 > 1 else k)
