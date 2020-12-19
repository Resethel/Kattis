#!/usr/bin/env python3
# https://github.com/JonSteinn/Kattis-Solutions/blob/master/src/Early%20Winter/Python%203/main.py


if __name__ == "__main__":

    d = tuple(map(int, input().split()))[1]

    earliest_year = -1
    for i, k in enumerate(input().split()):
        if int(k) <= d:
            earliest_year = i
            break

    if earliest_year == -1:
        print('It had never snowed this early!')
    else:
        print("It hadn't snowed this early in {} years!".format(earliest_year))
