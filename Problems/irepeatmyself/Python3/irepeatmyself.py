# Using Python 3
# https://open.kattis.com/problems/irepeatmyself

n = int(input())
out = []
for i in range(n):

    s = input()
    l = len(s)

    for j in range(1, l + 1):
        if( s == (s[0:j] * (int(l // j) + 1))[0:l]):
            out.append(j)
            break

for o in out: print(o)
