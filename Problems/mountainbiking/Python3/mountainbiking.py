# Using Python 3
# https://open.kattis.com/problems/mountainbiking

from math import pow
from math import cos
from math import radians
from math import sqrt


N, gravity = input().split(' ')
N = int(N)
gravity = float(gravity)

seg = []

for _ in range(N):
    dist, angle = input().split()
    dist = float(dist)
    angle = float(angle)
    accel = gravity * cos(radians(angle))

    seg.append((dist, angle, accel))


for i in range(N):
    speed = 0.0
    for dist, angle, accel in seg[i:]:
        speed = sqrt((dist * 2 * accel) + pow(speed,2))

    print(speed)
