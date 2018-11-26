# Using Python 3
# https://open.kattis.com/problems/bribingeve

N = int(input())

tests = []
xM = [0,0]

for i in range(N):
    x1, x2 = map(int, input().split())
    tests.append([x1, x2])

    if(i == 0):
        xM = [x1, x2]

x1_tab = [i[0] for i in tests]
x2_tab = [i[1] for i in tests]
xS_tab = [i[1] for i in tests]

x1_tab.sort()
x2_tab.sort()

a = x1_tab.index(xM[0])
b = x2_tab.index(xM[1])

print(len(tests) - max(a,b), len(tests) - min(a,b))
