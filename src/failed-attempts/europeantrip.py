# Using Python 3
# https://open.kattis.com/problems/europeantrip

from copy import deepcopy
from math import sqrt

points = []

# Test points. These points are the left, up, right and down relative neighbours
# (arranged circularly) to the current_point at a distance of test_distance from current_point
test_point = [ [ -1.0, 0.0 ],
               [ 0.0, 1.0 ],
               [ 1.0, 0.0 ],
               [ 0.0, -1.0 ]]
# Lowest Limit till which we are going to run the main while loop lower the
# limit higher the accuracy
lower_limit = 0.00001


def distSum(point, pt_array):
    sum = 0

    for i in range(len(pt_array)):
        dist_x = abs(pt_array[i][0] - point[0])
        dist_y = abs(pt_array[i][1] - point[1])

        sum += sqrt((dist_x * dist_x) + (dist_y * dist_y))

    return sum
# End def distSum


def geometricMedian(pt_array):
    N = len(pt_array)
    current_point = [0, 0]

    for i in range(N):
        current_point[0] += pt_array[i][0]
        current_point[1] += pt_array[i][1]

    # Here current_point becomes the geographic MidPoint or Center of Gravity of
    # equal discrete mass distributions
    current_point[0] /= N
    current_point[1] /= N

    # Minimum_distance becomes sum of all distances from MidPoint to  all given
    # points
    minimum_distance = distSum(current_point, pt_array)

    k = 0
    while k < N:
        for i in range(N):
            if i != k:
                continue
            else:
                new_point = pt_array[i]
                new_distance = distSum(new_point, pt_array)
                if (new_distance < minimum_distance):
                    minimum_distance = new_distance;
                    current_point = deepcopy(new_point)
                # fi
            # fi
        # rof
        k += 1
    # elihw

    # Assuming test_distance to be 1000
    test_distance = 1000
    flag = False

    while test_distance > lower_limit:

        flag = False

        # Loop for iterating over all 4 neighbours
        for i in range(4):
            # Finding neighbours
            new_point = [0, 0]
            new_point[0] = deepcopy(current_point[0]) + test_distance * test_point[i][0]
            new_point[1] = deepcopy(current_point[1]) + test_distance * test_point[i][1]

            # New sum of Euclidean distances from the neighbor to the given
            # data points
            new_distance = distSum(new_point, pt_array)

            if new_distance < minimum_distance:
                # Approximating and changing current_point
                minimum_distance = new_distance
                current_point = deepcopy(new_point)
                flag = True
                break
            # fi
        # rof

        if not flag:
            test_distance /= 2
    # elihw

    return current_point[0], current_point[1]

# End def geometricMedian

def main():
    points = []
    # Input the points
    for i in range(3):
        points += [[int(j) for j in input().split(' ')]]

    geometric_median_point = geometricMedian(points)

    print("{} {}".format(*geometric_median_point))

# End def main

main()
