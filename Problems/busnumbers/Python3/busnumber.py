# -*- coding: utf-8 -*-
# https://open.kattis.com/problems/busnumbers
# Using Python3

from itertools import groupby
from operator import itemgetter


def main():
    # Discard first input
    _ = input()

    # Get the bus numbers, sorted
    bus_num = sorted([int(x) for x in input().split()])
    bus_num_list = []

    # Group the bus numbers by consecutive numbers
    for k, g in groupby(enumerate(bus_num), lambda ix: ix[0] - ix[1]):
        group = list(map(itemgetter(1), g))
        # for groups smaller than 2, just extend the list
        if len(group) <= 2:
            bus_num_list.extend(group)
        else:
            # Else concatenate the first number and the last
            bus_num_list.append("{}-{}".format(group[0], group[-1]))

    # Print the output
    print(*bus_num_list)
# End def main

if __name__ == '__main__':
    main()
