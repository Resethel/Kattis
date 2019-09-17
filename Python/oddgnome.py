# Using Python 3
# https://open.kattis.com/problems/oddgnome

n = int(input())
king = [0]*n

for i in range(n):
    grp = [int(x) for x in input().split(' ')]

    for j in range(1,len(grp)-1):
        if(grp[j+1] - grp[j] != 1 ):
            king[i] = j+1
            break

for k in range(n):
    print(king[k])
