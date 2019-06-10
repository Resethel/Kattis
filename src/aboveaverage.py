# Using Python 3
# https://open.kattis.com/problems/aboveaverage

from copy import deepcopy

C = int(input())
outputs = []

for _ in range(C):
    # Getting inputs
    inputs = [int(x) for x in input().split(' ')]
    N = deepcopy(inputs[0])
    grades = deepcopy(inputs[1:])

    # calculating the average
    average = 0
    for grade in grades:
        average += grade
    average /= N

    # Getting the result of students above average
    above_average = 0
    for grade in grades:
        if grade > average:
            above_average += 1

    outputs += ["{:02.3f}%".format(above_average/N*100.0)]

for result in outputs:
    print(result)
