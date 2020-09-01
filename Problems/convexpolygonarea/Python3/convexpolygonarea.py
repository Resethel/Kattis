# Using Python 3
# https://open.kattis.com/problems/convexpolygonarea

n = int(input())
area = [0.0]*n

for poly in range(n):

    data = [int(x) for x in input().split()]
    data.pop(0)

    v = list(zip(data[0::2], data[1::2]))
    size = len(v)

    for i in range(size):
        a = (v[(i+1)%size][0] + v[i][0])
        b = (v[(i+1)%size][1] - v[i][1])
        area[poly] += a * b

    area[poly] = 0.5 * abs(area[poly])

for A in area : print(A)
